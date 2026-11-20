use std::time::Duration;
use serde::{Deserialize, Serialize};

/// Pacing configuration for vintage synthesizers
/// Different hardware requires specific pauses to prevent buffer overflow (e.g. Roland D-50, Yamaha TX81Z)
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub struct PacingConfig {
    /// Delay between individual bytes in milliseconds (usually 0 to 5ms)
    pub inter_byte_delay_ms: u64,
    /// Delay between chunked SysEx messages or handshakes in milliseconds (usually 20 to 100ms)
    pub inter_message_delay_ms: u64,
    /// Maximum chunk size before pausing
    pub chunk_size_bytes: usize,
}

impl Default for PacingConfig {
    fn default() -> Self {
        Self {
            inter_byte_delay_ms: 0,
            inter_message_delay_ms: 30,
            chunk_size_bytes: 256,
        }
    }
}

impl PacingConfig {
    /// Safe profile for vintage 1980s microcontrollers (e.g. Roland D-50, Akai AX60, Casio CZ)
    pub fn vintage_safe() -> Self {
        Self {
            inter_byte_delay_ms: 2,
            inter_message_delay_ms: 80,
            chunk_size_bytes: 64,
        }
    }

    /// Fast profile for 1990s/2000s DSP synths (Access Virus, E-MU Audity 2000, Nord Lead)
    pub fn modern_dsp() -> Self {
        Self {
            inter_byte_delay_ms: 0,
            inter_message_delay_ms: 15,
            chunk_size_bytes: 512,
        }
    }
}

pub struct SysExThrottler {
    pub config: PacingConfig,
}

impl SysExThrottler {
    pub fn new(config: PacingConfig) -> Self {
        Self { config }
    }

    pub fn inter_message_duration(&self) -> Duration {
        Duration::from_millis(self.config.inter_message_delay_ms)
    }

    pub fn inter_byte_duration(&self) -> Duration {
        Duration::from_millis(self.config.inter_byte_delay_ms)
    }
}
