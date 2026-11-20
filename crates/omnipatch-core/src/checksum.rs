use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum ChecksumType {
    /// Access Virus: sum of payload bytes & 0x7F
    Sum7bit,
    /// Roland / Boss: 128 - (sum % 128) & 0x7F (also known as 2's complement of 7-bit sum)
    Roland,
    /// Yamaha DX/TX series: 2's complement of 7-bit sum ((-sum) & 0x7F)
    Yamaha,
    /// Waldor / Kawai / Korg specific
    None,
}

impl ChecksumType {
    /// Calculate checksum over slice of bytes
    pub fn calculate(&self, data: &[u8]) -> Option<u8> {
        match self {
            ChecksumType::Sum7bit => {
                let sum: u32 = data.iter().map(|&b| b as u32).sum();
                Some((sum & 0x7F) as u8)
            }
            ChecksumType::Roland => {
                let sum: u32 = data.iter().map(|&b| b as u32).sum();
                let remainder = sum % 128;
                let chk = (128 - remainder) & 0x7F;
                Some(chk as u8)
            }
            ChecksumType::Yamaha => {
                let sum: i32 = data.iter().map(|&b| b as i32).sum();
                Some(((-sum) & 0x7F) as u8)
            }
            ChecksumType::None => None,
        }
    }

    /// Verifies if the data plus provided checksum byte is valid
    pub fn verify(&self, data: &[u8], expected_checksum: u8) -> bool {
        match self.calculate(data) {
            Some(actual) => actual == expected_checksum,
            None => true,
        }
    }
}

/// E-MU Systems 14-bit data packing helpers (LSB first)
pub mod emu {
    pub fn encode_14bit(val: u16) -> (u8, u8) {
        let lsb = (val & 0x7F) as u8;
        let msb = ((val >> 7) & 0x7F) as u8;
        (lsb, msb)
    }

    pub fn decode_14bit(lsb: u8, msb: u8) -> u16 {
        ((msb as u16 & 0x7F) << 7) | (lsb as u16 & 0x7F)
    }

    pub fn encode_14bit_signed(val: i16) -> (u8, u8) {
        // 14-bit signed 2's complement
        let unsigned = (val as u16) & 0x3FFF;
        encode_14bit(unsigned)
    }

    pub fn decode_14bit_signed(lsb: u8, msb: u8) -> i16 {
        let unsigned = decode_14bit(lsb, msb);
        if unsigned & 0x2000 != 0 {
            // Negative: sign extend from bit 13
            (unsigned | 0xC000) as i16
        } else {
            unsigned as i16
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_roland_checksum() {
        // Roland classic test vector: [0x41, 0x10, 0x16, 0x12, 0x00, 0x00, 0x00, 0x00, 0x00]
        // Sum of address + data: 0x00 + 0x00 + 0x00 + 0x00 = 0 -> Checksum = 0
        let data = [0x00, 0x00, 0x00, 0x00];
        assert_eq!(ChecksumType::Roland.calculate(&data), Some(0x00));

        let data2 = [0x01, 0x00, 0x00, 0x01]; // sum = 2 -> 128 - 2 = 126 (0x7E)
        assert_eq!(ChecksumType::Roland.calculate(&data2), Some(0x7E));
    }

    #[test]
    fn test_virus_checksum() {
        // Sum 7-bit
        let data = [0x10, 0x20, 0x30]; // 0x60 -> 96
        assert_eq!(ChecksumType::Sum7bit.calculate(&data), Some(0x60));
    }

    #[test]
    fn test_emu_14bit() {
        let (lsb, msb) = emu::encode_14bit(300);
        assert_eq!(emu::decode_14bit(lsb, msb), 300);

        let (lsb_s, msb_s) = emu::encode_14bit_signed(-50);
        assert_eq!(emu::decode_14bit_signed(lsb_s, msb_s), -50);
    }
}
