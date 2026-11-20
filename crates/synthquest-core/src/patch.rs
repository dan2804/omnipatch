use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Patch {
    pub name: String,
    pub category: Option<String>,
    pub device_name: String,
    pub bank_index: u32,
    pub program_index: u32,
    pub sysex_dump: Vec<u8>,
    pub metadata: std::collections::HashMap<String, String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PatchBank {
    pub bank_name: String,
    pub device_name: String,
    pub bank_index: u32,
    pub is_read_only: bool,
    pub patches: Vec<Patch>,
}
