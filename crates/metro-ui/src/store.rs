use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::sync::{Arc, RwLock};

/// Dynamic value types supported by the Metro UI parameter store
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
#[serde(untagged)]
pub enum ParamValue {
    Integer(i64),
    Float(f64),
    Boolean(bool),
    Text(String),
    IntList(Vec<i64>),
}

impl ParamValue {
    pub fn as_i64(&self) -> Option<i64> {
        match self {
            ParamValue::Integer(v) => Some(*v),
            ParamValue::Float(v) => Some(*v as i64),
            ParamValue::Boolean(b) => Some(if *b { 1 } else { 0 }),
            _ => None,
        }
    }

    pub fn as_bool(&self) -> Option<bool> {
        match self {
            ParamValue::Boolean(b) => Some(*b),
            ParamValue::Integer(v) => Some(*v != 0),
            _ => None,
        }
    }

    pub fn as_str(&self) -> Option<&str> {
        match self {
            ParamValue::Text(s) => Some(s.as_str()),
            _ => None,
        }
    }
}

/// Reactive parameter store that can be shared across UI renderers and audio/MIDI engines
#[derive(Debug, Clone, Default)]
pub struct ParameterStore {
    state: Arc<RwLock<HashMap<String, ParamValue>>>,
}

impl ParameterStore {
    pub fn new() -> Self {
        Self {
            state: Arc::new(RwLock::new(HashMap::new())),
        }
    }

    pub fn set(&self, param_id: &str, value: ParamValue) {
        if let Ok(mut map) = self.state.write() {
            map.insert(param_id.to_string(), value);
        }
    }

    pub fn set_i64(&self, param_id: &str, value: i64) {
        self.set(param_id, ParamValue::Integer(value));
    }

    pub fn set_bool(&self, param_id: &str, value: bool) {
        self.set(param_id, ParamValue::Boolean(value));
    }

    pub fn get(&self, param_id: &str) -> Option<ParamValue> {
        self.state.read().ok().and_then(|map| map.get(param_id).cloned())
    }

    pub fn get_i64(&self, param_id: &str) -> Option<i64> {
        self.get(param_id).and_then(|v| v.as_i64())
    }

    pub fn get_bool(&self, param_id: &str) -> Option<bool> {
        self.get(param_id).and_then(|v| v.as_bool())
    }

    pub fn export_json(&self) -> String {
        if let Ok(map) = self.state.read() {
            serde_json::to_string_pretty(&*map).unwrap_or_else(|_| "{}".to_string())
        } else {
            "{}".to_string()
        }
    }

    pub fn import_json(&self, json_str: &str) -> anyhow::Result<()> {
        let incoming: HashMap<String, ParamValue> = serde_json::from_str(json_str)?;
        if let Ok(mut map) = self.state.write() {
            for (k, v) in incoming {
                map.insert(k, v);
            }
        }
        Ok(())
    }
}
