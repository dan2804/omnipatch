use thiserror::Error;
use std::time::Duration;
use synthquest_core::throttle::PacingConfig;

#[derive(Error, Debug)]
pub enum MidiError {
    #[error("MIDI init error: {0}")]
    InitError(String),
    #[error("MIDI port not found: {0}")]
    PortNotFound(String),
    #[error("MIDI connection error: {0}")]
    ConnectionError(String),
    #[error("MIDI send error: {0}")]
    SendError(String),
}

pub struct MidiManager {
    client_name: String,
}

impl MidiManager {
    pub fn new(client_name: &str) -> Self {
        Self {
            client_name: client_name.to_string(),
        }
    }

    #[cfg(feature = "native-midi")]
    pub fn list_output_ports(&self) -> Result<Vec<(usize, String)>, MidiError> {
        let midi_out = midir::MidiOutput::new(&self.client_name)
            .map_err(|e| MidiError::InitError(e.to_string()))?;
        let ports = midi_out.ports();
        let mut list = Vec::new();
        for (i, p) in ports.iter().enumerate() {
            let name = midi_out.port_name(p).unwrap_or_else(|_| format!("Port {}", i));
            list.push((i, name));
        }
        Ok(list)
    }

    #[cfg(not(feature = "native-midi"))]
    pub fn list_output_ports(&self) -> Result<Vec<(usize, String)>, MidiError> {
        Ok(vec![
            (0, "SynthQuest Virtual Output Loopback 1".to_string()),
            (1, "SynthQuest USB-MIDI Interface 2".to_string()),
        ])
    }

    #[cfg(feature = "native-midi")]
    pub fn list_input_ports(&self) -> Result<Vec<(usize, String)>, MidiError> {
        let midi_in = midir::MidiInput::new(&self.client_name)
            .map_err(|e| MidiError::InitError(e.to_string()))?;
        let ports = midi_in.ports();
        let mut list = Vec::new();
        for (i, p) in ports.iter().enumerate() {
            let name = midi_in.port_name(p).unwrap_or_else(|_| format!("Port {}", i));
            list.push((i, name));
        }
        Ok(list)
    }

    #[cfg(not(feature = "native-midi"))]
    pub fn list_input_ports(&self) -> Result<Vec<(usize, String)>, MidiError> {
        Ok(vec![
            (0, "SynthQuest Virtual Input Loopback 1".to_string()),
        ])
    }
}

pub struct VirtualMidiOutput {
    pub sent_messages: Vec<Vec<u8>>,
}

impl VirtualMidiOutput {
    pub fn new() -> Self {
        Self {
            sent_messages: Vec::new(),
        }
    }

    pub fn send(&mut self, bytes: &[u8]) -> Result<(), MidiError> {
        self.sent_messages.push(bytes.to_vec());
        Ok(())
    }
}

/// Helper to simulate or send throttled SysEx stream
pub fn send_sysex_throttled_virtual(
    out: &mut VirtualMidiOutput,
    bytes: &[u8],
    pacing: &PacingConfig,
) -> Result<(), MidiError> {
    if pacing.inter_byte_delay_ms == 0 {
        out.send(bytes)?;
    } else {
        for &b in bytes {
            out.send(&[b])?;
        }
    }
    Ok(())
}
