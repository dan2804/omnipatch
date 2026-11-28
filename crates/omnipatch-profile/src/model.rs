use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum PresetEntry {
    Simple(String),
    Detailed {
        #[serde(default)]
        index: Option<u32>,
        name: String,
        #[serde(default)]
        category: Option<String>,
        #[serde(default)]
        full_name: Option<String>,
    },
}

impl PresetEntry {
    pub fn display_name(&self) -> &str {
        match self {
            PresetEntry::Simple(s) => s,
            PresetEntry::Detailed { full_name, name, .. } => {
                full_name.as_deref().unwrap_or(name)
            }
        }
    }

    pub fn category_name(&self) -> Option<&str> {
        match self {
            PresetEntry::Simple(_) => None,
            PresetEntry::Detailed { category, .. } => category.as_deref(),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeviceProfile {
    #[serde(alias = "model")]
    pub name: String,
    pub manufacturer: String,
    #[serde(default, alias = "type")]
    pub category: String,
    #[serde(default, alias = "year")]
    pub release_year: Option<u32>,
    
    #[serde(default)]
    pub hardware: Option<HashMap<String, serde_yaml::Value>>,

    #[serde(default)]
    pub midi: MidiConfig,

    #[serde(default)]
    pub sysex: Option<serde_yaml::Value>,

    #[serde(default)]
    pub control_protocol: Option<String>,

    #[serde(default)]
    pub ui_theme: Option<HashMap<String, serde_yaml::Value>>,

    #[serde(default)]
    pub parameters: Vec<ParameterDef>,

    #[serde(alias = "bank_presets")]
    #[serde(default)]
    pub factory_presets: Option<HashMap<String, Vec<PresetEntry>>>,
}

impl DeviceProfile {
    pub fn parameter_edit_format(&self) -> Option<&str> {
        self.sysex.as_ref().and_then(|val| {
            val.get("parameter_edit_format").and_then(|v| v.as_str())
        })
    }

    pub fn checksum_type(&self) -> &str {
        self.sysex.as_ref()
            .and_then(|val| val.get("checksum").and_then(|v| v.as_str()))
            .unwrap_or("none")
    }

    pub fn default_device_id(&self) -> u8 {
        self.midi.device_id.unwrap_or(0)
    }
}

#[derive(Debug, Clone, Default, Serialize, Deserialize)]
pub struct MidiConfig {
    #[serde(default)]
    pub manufacturer_id: Option<serde_yaml::Value>,
    #[serde(default)]
    pub device_id: Option<u8>,
    #[serde(default)]
    pub model_id: Option<u8>,
    #[serde(default)]
    pub channel: Option<u8>,
    #[serde(default)]
    pub bank_select: Option<serde_yaml::Value>,
    #[serde(default)]
    pub program_change: Option<serde_yaml::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ParameterDef {
    pub id: String,
    pub name: String,

    #[serde(default)]
    pub page: Option<String>,

    #[serde(default)]
    pub index: Option<u32>,

    #[serde(default)]
    pub cc: Option<u8>,

    #[serde(default)]
    pub param_id: Option<u32>,

    #[serde(rename = "type")]
    #[serde(default)]
    pub param_type: Option<String>,

    #[serde(default)]
    pub range: Option<Vec<i32>>,

    #[serde(default)]
    pub default: Option<i32>,

    #[serde(default)]
    pub unit: Option<String>,

    #[serde(default)]
    pub options: Option<serde_yaml::Value>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ParameterType {
    Linear,
    Enum,
    Logarithmic,
    Bipolar,
}
