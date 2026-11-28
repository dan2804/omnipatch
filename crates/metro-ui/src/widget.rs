use serde::{Deserialize, Serialize};

/// Type of visual Metro widget to display
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(tag = "type", rename_all = "snake_case")]
pub enum WidgetType {
    /// A horizontal range slider with filled accent track and value pill
    Slider {
        min: i64,
        max: i64,
        #[serde(default = "default_step")]
        step: i64,
        #[serde(default)]
        unit: Option<String>,
        #[serde(default)]
        bipolar: bool,
    },
    /// A Windows 8 WinRT-style flat toggle switch
    Toggle {
        #[serde(default = "default_on_label")]
        on_label: String,
        #[serde(default = "default_off_label")]
        off_label: String,
    },
    /// A horizontal segmented button group for discrete values
    SegmentGroup {
        options: Vec<String>,
    },
    /// Interactive ADSR / multi-stage envelope canvas with synced sliders
    Envelope {
        attack_id: String,
        decay_id: String,
        sustain_id: String,
        release_id: String,
        #[serde(default)]
        curve_type: String, // "analog_exponential", "linear", etc.
    },
    /// 16 or 32-step rhythmic gate / velocity sequencer for arpeggiators
    StepSequencer {
        steps: usize,
        #[serde(default = "default_tracks")]
        tracks: Vec<String>, // e.g. ["gate", "velocity", "pitch"]
    },
    /// Large Segoe UI Light hero digit readout (e.g. 48px live meter)
    ValueTile {
        #[serde(default)]
        unit: Option<String>,
        #[serde(default)]
        caption: Option<String>,
    },
}

fn default_step() -> i64 { 1 }
fn default_on_label() -> String { "ON".to_string() }
fn default_off_label() -> String { "OFF".to_string() }
fn default_tracks() -> Vec<String> { vec!["gate".to_string(), "velocity".to_string()] }

/// Definition of an editable parameter in a Metro UI view
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ParameterDef {
    pub id: String,
    pub name: String,
    #[serde(default)]
    pub subtitle: Option<String>,
    pub widget: WidgetType,
    #[serde(default)]
    pub default_value: serde_json::Value,
    /// Optional SysEx address, CC, or NRPN binding metadata
    #[serde(default)]
    pub midi_binding: Option<serde_json::Value>,
}

impl ParameterDef {
    pub fn new_slider(id: &str, name: &str, min: i64, max: i64, default: i64, unit: Option<&str>) -> Self {
        Self {
            id: id.to_string(),
            name: name.to_string(),
            subtitle: None,
            widget: WidgetType::Slider {
                min,
                max,
                step: 1,
                unit: unit.map(|s| s.to_string()),
                bipolar: min < 0,
            },
            default_value: serde_json::json!(default),
            midi_binding: None,
        }
    }

    pub fn new_toggle(id: &str, name: &str, default: bool) -> Self {
        Self {
            id: id.to_string(),
            name: name.to_string(),
            subtitle: None,
            widget: WidgetType::Toggle {
                on_label: "ON".to_string(),
                off_label: "OFF".to_string(),
            },
            default_value: serde_json::json!(default),
            midi_binding: None,
        }
    }

    pub fn new_segment(id: &str, name: &str, options: &[&str], default_idx: usize) -> Self {
        let opts: Vec<String> = options.iter().map(|s| s.to_string()).collect();
        let default_val = opts.get(default_idx).cloned().unwrap_or_else(|| "".to_string());
        Self {
            id: id.to_string(),
            name: name.to_string(),
            subtitle: None,
            widget: WidgetType::SegmentGroup { options: opts },
            default_value: serde_json::json!(default_val),
            midi_binding: None,
        }
    }

    pub fn new_envelope(id: &str, name: &str, att: &str, dec: &str, sus: &str, rel: &str) -> Self {
        Self {
            id: id.to_string(),
            name: name.to_string(),
            subtitle: Some("ADSR TRANSIENT".to_string()),
            widget: WidgetType::Envelope {
                attack_id: att.to_string(),
                decay_id: dec.to_string(),
                sustain_id: sus.to_string(),
                release_id: rel.to_string(),
                curve_type: "analog_exponential".to_string(),
            },
            default_value: serde_json::json!({}),
            midi_binding: None,
        }
    }

    pub fn new_arpeggiator(id: &str, name: &str, steps: usize) -> Self {
        Self {
            id: id.to_string(),
            name: name.to_string(),
            subtitle: Some("16-STEP VELOCITY / GATE".to_string()),
            widget: WidgetType::StepSequencer {
                steps,
                tracks: vec!["gate".to_string(), "velocity".to_string()],
            },
            default_value: serde_json::json!({
                "gates": vec![true; steps],
                "velocities": vec![100; steps]
            }),
            midi_binding: None,
        }
    }
}
