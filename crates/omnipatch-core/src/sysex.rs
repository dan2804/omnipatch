use serde::{Deserialize, Serialize};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum SysExError {
    #[error("SysEx message must start with 0xF0")]
    MissingStartByte,
    #[error("SysEx message must end with 0xF7")]
    MissingEndByte,
    #[error("SysEx payload contains high-bit byte (0x{0:02X})")]
    InvalidDataByte(u8),
    #[error("SysEx message too short (minimum 3 bytes, got {0})")]
    TooShort(usize),
    #[error("Hex decode error: {0}")]
    HexError(#[from] hex::FromHexError),
}

/// Represents a raw MIDI System Exclusive message
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub struct SysExMessage {
    pub raw: Vec<u8>,
}

impl SysExMessage {
    pub const START_BYTE: u8 = 0xF0;
    pub const END_BYTE: u8 = 0xF7;

    /// Construct and validate a SysEx message
    pub fn new(bytes: Vec<u8>) -> Result<Self, SysExError> {
        if bytes.len() < 3 {
            return Err(SysExError::TooShort(bytes.len()));
        }
        if bytes[0] != Self::START_BYTE {
            return Err(SysExError::MissingStartByte);
        }
        if *bytes.last().unwrap() != Self::END_BYTE {
            return Err(SysExError::MissingEndByte);
        }
        // Verify payload bytes have bit 7 set to 0
        for &b in &bytes[1..bytes.len() - 1] {
            if b >= 0x80 {
                return Err(SysExError::InvalidDataByte(b));
            }
        }
        Ok(Self { raw: bytes })
    }

    /// Construct without validation (useful when constructing templates)
    pub fn new_unchecked(bytes: Vec<u8>) -> Self {
        Self { raw: bytes }
    }

    /// Parse space-separated or plain hex string (e.g. "F0 00 20 33 01 F7")
    pub fn from_hex(hex_str: &str) -> Result<Self, SysExError> {
        let cleaned: String = hex_str.chars().filter(|c| !c.is_whitespace()).collect();
        let bytes = hex::decode(cleaned)?;
        Self::new(bytes)
    }

    pub fn raw_bytes(&self) -> &[u8] {
        &self.raw
    }

    pub fn as_bytes(&self) -> &[u8] {
        &self.raw
    }

    /// Format as standard space-separated hex bytes
    pub fn to_hex_string(&self) -> String {
        self.raw
            .iter()
            .map(|b| format!("{:02X}", b))
            .collect::<Vec<_>>()
            .join(" ")
    }

    /// Returns the Manufacturer ID bytes (either 1 byte or 3 bytes for extended)
    pub fn manufacturer_id(&self) -> &[u8] {
        if self.raw.len() > 1 && self.raw[1] == 0x00 {
            if self.raw.len() >= 4 {
                &self.raw[1..4]
            } else {
                &self.raw[1..]
            }
        } else if self.raw.len() > 1 {
            &self.raw[1..2]
        } else {
            &[]
        }
    }

    /// Slice of payload bytes excluding 0xF0 and 0xF7
    pub fn payload(&self) -> &[u8] {
        if self.raw.len() >= 2 {
            &self.raw[1..self.raw.len() - 1]
        } else {
            &[]
        }
    }

    pub fn len(&self) -> usize {
        self.raw.len()
    }

    pub fn is_empty(&self) -> bool {
        self.raw.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_sysex() {
        let msg = SysExMessage::from_hex("F0 00 20 33 01 10 40 34 00 F7").unwrap();
        assert_eq!(msg.manufacturer_id(), &[0x00, 0x20, 0x33]);
        assert_eq!(msg.raw.len(), 10);
        assert_eq!(msg.to_hex_string(), "F0 00 20 33 01 10 40 34 00 F7");
    }

    #[test]
    fn test_invalid_start_end() {
        assert!(SysExMessage::new(vec![0x00, 0x01, 0xF7]).is_err());
        assert!(SysExMessage::new(vec![0xF0, 0x01, 0x02]).is_err());
        assert!(SysExMessage::new(vec![0xF0, 0x90, 0xF7]).is_err()); // bit 7 high
    }
}
