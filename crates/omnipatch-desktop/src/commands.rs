use anyhow::Result;
use serde::{Deserialize, Serialize};
use std::path::Path;

use omnipatch_core::{ChecksumType, SysExContext, SysExTemplate};
use omnipatch_librarian::{LibrarianDb, PatchRecord};
use omnipatch_midi::MidiManager;
use omnipatch_profile::{DeviceProfile, ProfileRegistry};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeviceSummary {
    pub name: String,
    pub manufacturer: String,
    pub parameter_count: usize,
    pub bank_count: usize,
    pub preset_count: usize,
    pub protocol: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SysExResult {
    pub hex_string: String,
    pub bytes: Vec<u8>,
    pub explanation: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MidiPortInfo {
    pub index: usize,
    pub name: String,
}

/// Retrieve all synthesizer profiles loaded from the devices directory
pub fn get_device_profiles(devices_dir: Option<&str>) -> Result<Vec<DeviceSummary>> {
    let dir = devices_dir.unwrap_or("devices");
    let mut registry = ProfileRegistry::new();
    let _ = registry.load_dir(Path::new(dir));

    let mut summaries: Vec<DeviceSummary> = registry
        .all()
        .into_iter()
        .map(|p| {
            let (bank_count, preset_count) = if let Some(ref banks) = p.factory_presets {
                let total_p: usize = banks.values().map(|v| v.len()).sum();
                (banks.len(), total_p)
            } else {
                (0, 0)
            };

            let protocol = if let Some(ref proto) = p.control_protocol {
                proto.clone()
            } else {
                "sysex".to_string()
            };

            DeviceSummary {
                name: p.name.clone(),
                manufacturer: p.manufacturer.clone(),
                parameter_count: p.parameters.len(),
                bank_count,
                preset_count,
                protocol,
            }
        })
        .collect();

    summaries.sort_by(|a, b| a.name.cmp(&b.name));
    Ok(summaries)
}

/// Retrieve full profile detail for a given synthesizer name
pub fn get_device_detail(name: &str, devices_dir: Option<&str>) -> Option<DeviceProfile> {
    let dir = devices_dir.unwrap_or("devices");
    let mut registry = ProfileRegistry::new();
    let _ = registry.load_dir(Path::new(dir));

    let norm = name.to_lowercase().replace(['-', '_', ' '], "");
    registry.all().into_iter().find(|p| {
        let p_norm = p.name.to_lowercase().replace(['-', '_', ' '], "");
        p_norm.contains(&norm) || norm.contains(&p_norm)
    }).cloned()
}

/// Format parameter change SysEx dynamically using profile templates
pub fn format_parameter_sysex(
    device_name: &str,
    param_id: u32,
    value: i32,
    devices_dir: Option<&str>,
) -> Result<SysExResult> {
    let profile = get_device_detail(device_name, devices_dir)
        .ok_or_else(|| anyhow::anyhow!("Device '{}' not found in registry", device_name))?;

    if let Some(format_str) = profile.parameter_edit_format() {
        let chk = match profile.checksum_type() {
            "sum_7bit" => ChecksumType::Sum7bit,
            "roland" => ChecksumType::Roland,
            "yamaha" => ChecksumType::Yamaha,
            _ => ChecksumType::None,
        };

        let template = SysExTemplate::parse(format_str, chk)
            .map_err(|e| anyhow::anyhow!("Template error: {}", e))?;

        let ctx = SysExContext::new(param_id, value)
            .with_device_id(profile.default_device_id());

        let msg = template
            .format(&ctx)
            .map_err(|e| anyhow::anyhow!("SysEx formatting error: {}", e))?;

        let hex_string = msg.to_hex_string();
        let bytes = msg.as_bytes().to_vec();
        let explanation = format!(
            "Device: {} • Param: {} • Value: {} (Profile: {})",
            profile.name, param_id, value, format_str
        );

        Ok(SysExResult {
            hex_string,
            bytes,
            explanation,
        })
    } else if profile.control_protocol.as_deref() == Some("midi_cc") || device_name.to_lowercase().contains("ax60") {
        let cc = (param_id & 0x7F) as u8;
        let val = (value & 0x7F) as u8;
        let bytes = vec![0xB0, cc, val];
        let hex_string = format!("B0 {:02X} {:02X}", cc, val);
        let explanation = format!(
            "Device: {} • CC: {} • Value: {} (Real-time MIDI CC)",
            profile.name, cc, val
        );

        Ok(SysExResult {
            hex_string,
            bytes,
            explanation,
        })
    } else {
        anyhow::bail!("No parameter edit SysEx format defined for {}", profile.name);
    }
}

/// Transmit parameter change to hardware MIDI port
pub fn send_parameter(
    device_name: &str,
    param_id: u32,
    value: i32,
    port_index: Option<usize>,
    devices_dir: Option<&str>,
) -> Result<SysExResult> {
    let result = format_parameter_sysex(device_name, param_id, value, devices_dir)?;

    let midi = MidiManager::new("OmniPatch Desktop");
    if let Some(idx) = port_index {
        midi.send_raw(idx, &result.bytes)
            .map_err(|e| anyhow::anyhow!("MIDI transmission failed: {}", e))?;
    }

    Ok(result)
}

/// Full-text search across SQLite librarian database using SQLite FTS5
pub fn search_librarian(
    db_path: Option<&str>,
    query: &str,
    device: Option<&str>,
) -> Result<Vec<PatchRecord>> {
    let path = db_path.unwrap_or("omnipatch_library.db");
    let librarian = LibrarianDb::open(path)?;

    let results = if !query.trim().is_empty() {
        if device.is_none() {
            librarian.search_fts(query)?
        } else {
            librarian.search(device, Some(query))?
        }
    } else {
        librarian.search(device, None)?
    };

    Ok(results)
}

/// Scan hardware MIDI output ports
pub fn get_midi_ports() -> Vec<MidiPortInfo> {
    let midi = MidiManager::new("OmniPatch Desktop");
    match midi.list_output_ports() {
        Ok(ports) => ports
            .into_iter()
            .map(|(index, name)| MidiPortInfo { index, name })
            .collect(),
        Err(_) => vec![],
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_desktop_profile_lookup_and_sysex() {
        let profiles = get_device_profiles(Some("../../devices")).unwrap();
        assert!(profiles.len() >= 27);

        let cz_res = format_parameter_sysex("cz101", 20, 80, Some("../../devices")).unwrap();
        assert_eq!(cz_res.hex_string, "F0 44 00 00 70 00 14 50 F7");

        let p2k_res = format_parameter_sysex("proteus2000", 0x0180, 50, Some("../../devices")).unwrap();
        assert_eq!(p2k_res.hex_string, "F0 18 0F 00 55 01 02 00 03 32 00 F7");
    }
}
