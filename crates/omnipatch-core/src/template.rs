use crate::checksum::{emu, ChecksumType};
use crate::sysex::{SysExError, SysExMessage};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum TemplateError {
    #[error("Invalid token: {0}")]
    InvalidToken(String),
    #[error("SysEx error: {0}")]
    SysEx(#[from] SysExError),
    #[error("Missing parameter value for placeholder: {0}")]
    MissingValue(String),
}

/// Context variables used to interpolate a declarative SysEx packet template
#[derive(Debug, Clone, Default)]
pub struct SysExContext {
    pub device_id: u8,
    pub model_id: Option<u8>,
    pub param_id: u32,
    pub value: i32,
    pub bank_id: Option<u32>,
    pub patch_id: Option<u32>,
    pub page: Option<u8>,
    pub channel: Option<u8>,
}

impl SysExContext {
    pub fn new(param_id: u32, value: i32) -> Self {
        Self {
            param_id,
            value,
            ..Default::default()
        }
    }

    pub fn with_device_id(mut self, device_id: u8) -> Self {
        self.device_id = device_id;
        self
    }

    pub fn with_page(mut self, page: u8) -> Self {
        self.page = Some(page);
        self
    }

    pub fn with_bank_and_patch(mut self, bank: u32, patch: u32) -> Self {
        self.bank_id = Some(bank);
        self.patch_id = Some(patch);
        self
    }
}

/// A declarative SysEx message template
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct SysExTemplate {
    raw_template: String,
    tokens: Vec<TemplateToken>,
    checksum_type: ChecksumType,
}

#[derive(Debug, Clone, PartialEq, Eq)]
enum TemplateToken {
    Byte(u8),
    DeviceId,
    ModelId,
    ParamId,
    ParamLsb,
    ParamMsb,
    ValueByte,
    ValueLsb,
    ValueMsb,
    BankId,
    PatchId,
    Page,
    Channel,
    Checksum,
}

impl SysExTemplate {
    /// Parse a template string such as:
    /// "F0 44 00 00 70 <dev_id> <param_id> <val_byte> F7"
    /// or "F0 00 20 33 01 <dev_id> 10 <page> <param_id> <val_byte> <checksum> F7"
    pub fn parse(template_str: &str, checksum_type: ChecksumType) -> Result<Self, TemplateError> {
        let mut tokens = Vec::new();
        for raw_tok in template_str.split_whitespace() {
            let tok = raw_tok.trim();
            if tok.is_empty() {
                continue;
            }

            let normalized = tok.to_lowercase();
            match normalized.as_str() {
                "<dev_id>" | "{dev_id}" | "<device_id>" | "{device_id}" => {
                    tokens.push(TemplateToken::DeviceId);
                }
                "<model_id>" | "{model_id}" => {
                    tokens.push(TemplateToken::ModelId);
                }
                "<param_id>" | "{param_id}" | "<param>" | "{param}" => {
                    tokens.push(TemplateToken::ParamId);
                }
                "<p_lsb>" | "{p_lsb}" | "<param_lsb>" | "{param_lsb}" => {
                    tokens.push(TemplateToken::ParamLsb);
                }
                "<p_msb>" | "{p_msb}" | "<param_msb>" | "{param_msb}" => {
                    tokens.push(TemplateToken::ParamMsb);
                }
                "<val_byte>" | "{val_byte}" | "<val>" | "{val}" | "<value>" | "{value}" => {
                    tokens.push(TemplateToken::ValueByte);
                }
                "<v_lsb>" | "{v_lsb}" | "<val_lsb>" | "{val_lsb}" => {
                    tokens.push(TemplateToken::ValueLsb);
                }
                "<v_msb>" | "{v_msb}" | "<val_msb>" | "{val_msb}" => {
                    tokens.push(TemplateToken::ValueMsb);
                }
                "<bank_id>" | "{bank_id}" | "<bank>" | "{bank}" => {
                    tokens.push(TemplateToken::BankId);
                }
                "<patch_id>" | "{patch_id}" | "<patch>" | "{patch}" => {
                    tokens.push(TemplateToken::PatchId);
                }
                "<page>" | "{page}" => {
                    tokens.push(TemplateToken::Page);
                }
                "<channel>" | "{channel}" | "<chan>" | "{chan}" => {
                    tokens.push(TemplateToken::Channel);
                }
                "<checksum>" | "{checksum}" | "<chk>" | "{chk}" => {
                    tokens.push(TemplateToken::Checksum);
                }
                _ => {
                    // Try parsing as hex byte e.g. "F0", "0x44", "00"
                    let hex_clean = tok.strip_prefix("0x").or_else(|| tok.strip_prefix("0X")).unwrap_or(tok);
                    match u8::from_str_radix(hex_clean, 16) {
                        Ok(b) => tokens.push(TemplateToken::Byte(b)),
                        Err(_) => return Err(TemplateError::InvalidToken(tok.to_string())),
                    }
                }
            }
        }

        Ok(Self {
            raw_template: template_str.to_string(),
            tokens,
            checksum_type,
        })
    }

    /// Format the template into a valid SysExMessage using the given context
    pub fn format(&self, ctx: &SysExContext) -> Result<SysExMessage, TemplateError> {
        let mut bytes = Vec::with_capacity(self.tokens.len() + 2);
        let mut checksum_pos = None;

        for token in &self.tokens {
            match token {
                TemplateToken::Byte(b) => bytes.push(*b),
                TemplateToken::DeviceId => bytes.push(ctx.device_id & 0x7F),
                TemplateToken::ModelId => bytes.push(ctx.model_id.unwrap_or(0) & 0x7F),
                TemplateToken::ParamId => bytes.push((ctx.param_id as u8) & 0x7F),
                TemplateToken::ParamLsb => {
                    let (lsb, _) = emu::encode_14bit(ctx.param_id as u16);
                    bytes.push(lsb);
                }
                TemplateToken::ParamMsb => {
                    let (_, msb) = emu::encode_14bit(ctx.param_id as u16);
                    bytes.push(msb);
                }
                TemplateToken::ValueByte => bytes.push((ctx.value as u8) & 0x7F),
                TemplateToken::ValueLsb => {
                    let (lsb, _) = emu::encode_14bit(ctx.value as u16);
                    bytes.push(lsb);
                }
                TemplateToken::ValueMsb => {
                    let (_, msb) = emu::encode_14bit(ctx.value as u16);
                    bytes.push(msb);
                }
                TemplateToken::BankId => bytes.push(ctx.bank_id.unwrap_or(0) as u8 & 0x7F),
                TemplateToken::PatchId => bytes.push(ctx.patch_id.unwrap_or(0) as u8 & 0x7F),
                TemplateToken::Page => bytes.push(ctx.page.unwrap_or(0) & 0x7F),
                TemplateToken::Channel => bytes.push(ctx.channel.unwrap_or(0) & 0x0F),
                TemplateToken::Checksum => {
                    checksum_pos = Some(bytes.len());
                    bytes.push(0x00); // Placeholder to be calculated
                }
            }
        }

        // If a checksum placeholder was present, compute over payload between manufacturer and checksum
        if let Some(pos) = checksum_pos {
            // Find payload start (skip 0xF0 and manufacturer/header ID)
            let start = if bytes.len() > 5 { 5 } else { 1 };
            if start < pos {
                if let Some(chk) = self.checksum_type.calculate(&bytes[start..pos]) {
                    bytes[pos] = chk;
                }
            }
        }

        let msg = SysExMessage::new(bytes)?;
        Ok(msg)
    }

    pub fn raw_template(&self) -> &str {
        &self.raw_template
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_casio_cz_template() {
        let tpl = SysExTemplate::parse(
            "F0 44 00 00 70 <dev_id> <param_id> <val_byte> F7",
            ChecksumType::None,
        )
        .unwrap();

        let ctx = SysExContext::new(20, 80).with_device_id(0);
        let msg = tpl.format(&ctx).unwrap();
        assert_eq!(msg.to_hex_string(), "F0 44 00 00 70 00 14 50 F7");
    }

    #[test]
    fn test_emu_14bit_template() {
        let tpl = SysExTemplate::parse(
            "F0 18 0F <dev_id> 55 01 02 <p_lsb> <p_msb> <v_lsb> <v_msb> F7",
            ChecksumType::None,
        )
        .unwrap();

        let ctx = SysExContext::new(3, 318).with_device_id(0);
        let msg = tpl.format(&ctx).unwrap();
        assert_eq!(msg.to_hex_string(), "F0 18 0F 00 55 01 02 03 00 3E 02 F7");
    }

    #[test]
    fn test_virus_checksum_template() {
        let tpl = SysExTemplate::parse(
            "F0 00 20 33 01 <dev_id> 10 <page> <param_id> <val_byte> <checksum> F7",
            ChecksumType::Sum7bit,
        )
        .unwrap();

        let ctx = SysExContext::new(40, 100).with_device_id(1).with_page(0);
        let msg = tpl.format(&ctx).unwrap();
        assert_eq!(msg.raw[0], 0xF0);
        assert_eq!(*msg.raw.last().unwrap(), 0xF7);
        assert_eq!(msg.len(), 12);
    }
}
