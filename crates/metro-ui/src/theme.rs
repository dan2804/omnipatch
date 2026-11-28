use serde::{Deserialize, Serialize};

/// Vibrancy modes for Windows 8 Metro UI styling
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum VibrancyMode {
    /// Full solid color blocks across entire module panels (authentic saturated Metro)
    SolidColor,
    /// Pure white canvas with vivid neon accent headers and controls (Surface RT style)
    SurfaceLight,
    /// Deep dark studio background with fluorescent glowing tracks and accents
    NeonDark,
}

impl Default for VibrancyMode {
    fn default() -> Self {
        Self::SolidColor
    }
}

/// A comprehensive color palette for Metro UI layouts
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetroPalette {
    pub page_bg: String,
    pub card_bg: String,
    pub text_primary: String,
    pub text_secondary: String,
    pub accent_primary: String,
    /// Column 1 background / accent color
    pub col1: String,
    pub col1_text: String,
    /// Column 2 background / accent color
    pub col2: String,
    pub col2_text: String,
    /// Column 3 background / accent color
    pub col3: String,
    pub col3_text: String,
    /// Column 4 background / accent color
    pub col4: String,
    pub col4_text: String,
    /// Column 5 background / accent color
    pub col5: String,
    pub col5_text: String,
    /// Rainbow / multi-stripe accent colors
    pub stripes: Vec<String>,
}

/// Complete theme definition for a Metro UI view
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetroTheme {
    pub id: String,
    pub name: String,
    pub manufacturer_badge: String,
    pub mode: VibrancyMode,
    pub palette: MetroPalette,
}

impl MetroTheme {
    /// Roland Juno-106 authentic 5-stripe rainbow theme
    pub fn juno_106() -> Self {
        Self {
            id: "juno_106".to_string(),
            name: "Juno-106 Rainbow".to_string(),
            manufacturer_badge: "ROLAND".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#1c1527".to_string(),
                card_bg: "rgba(0, 0, 0, 0.2)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#d4d4d8".to_string(),
                accent_primary: "#ff5500".to_string(),
                col1: "#ff5500".to_string(), // DCO Warm Orange
                col1_text: "#ffffff".to_string(),
                col2: "#0078d7".to_string(), // VCF Roland Blue
                col2_text: "#ffffff".to_string(),
                col3: "#f59e0b".to_string(), // ADSR Warm Amber
                col3_text: "#000000".to_string(),
                col4: "#008a00".to_string(), // Chorus Emerald
                col4_text: "#ffffff".to_string(),
                col5: "#8a2be2".to_string(), // LFO Violet
                col5_text: "#ffffff".to_string(),
                stripes: vec![
                    "#e51400".to_string(),
                    "#ff5500".to_string(),
                    "#f59e0b".to_string(),
                    "#008a00".to_string(),
                    "#0078d7".to_string(),
                ],
            },
        }
    }

    /// Yamaha DX7-II FM Jade Teal theme
    pub fn yamaha_dx7() -> Self {
        Self {
            id: "yamaha_dx7".to_string(),
            name: "DX7 FM Jade Teal".to_string(),
            manufacturer_badge: "YAMAHA".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#0c1716".to_string(),
                card_bg: "rgba(0, 0, 0, 0.25)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#a7f3d0".to_string(),
                accent_primary: "#00a499".to_string(),
                col1: "#00a499".to_string(), // Jade Teal
                col1_text: "#000000".to_string(),
                col2: "#059669".to_string(), // Operator Emerald
                col2_text: "#ffffff".to_string(),
                col3: "#d97706".to_string(), // Amber Envelope
                col3_text: "#ffffff".to_string(),
                col4: "#0284c7".to_string(), // Alg Sky Blue
                col4_text: "#ffffff".to_string(),
                col5: "#7c3aed".to_string(), // Digital Violet
                col5_text: "#ffffff".to_string(),
                stripes: vec![
                    "#00a499".to_string(),
                    "#059669".to_string(),
                    "#10b981".to_string(),
                    "#d97706".to_string(),
                    "#0284c7".to_string(),
                ],
            },
        }
    }

    /// Clavia Nord Lead Fire Red theme
    pub fn nord_lead() -> Self {
        Self {
            id: "nord_lead".to_string(),
            name: "Nord Fire Red".to_string(),
            manufacturer_badge: "CLAVIA".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#1c0d10".to_string(),
                card_bg: "rgba(0, 0, 0, 0.25)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#fecdd3".to_string(),
                accent_primary: "#d90429".to_string(),
                col1: "#d90429".to_string(), // Nord Crimson
                col1_text: "#ffffff".to_string(),
                col2: "#ff4d6d".to_string(), // Salmon Coral
                col2_text: "#000000".to_string(),
                col3: "#f59e0b".to_string(), // Sunlight Gold
                col3_text: "#000000".to_string(),
                col4: "#b5179e".to_string(), // Deep Magenta
                col4_text: "#ffffff".to_string(),
                col5: "#ef233c".to_string(), // Bright Scarlet
                col5_text: "#ffffff".to_string(),
                stripes: vec![
                    "#d90429".to_string(),
                    "#ef233c".to_string(),
                    "#f59e0b".to_string(),
                    "#d90429".to_string(),
                    "#111116".to_string(),
                ],
            },
        }
    }

    /// E-MU Orbit-3 / Planet Phatt Acid Neon theme
    pub fn emu_orbit() -> Self {
        Self {
            id: "emu_orbit".to_string(),
            name: "E-MU Acid Neon".to_string(),
            manufacturer_badge: "E-MU".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#161608".to_string(),
                card_bg: "rgba(0, 0, 0, 0.3)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#fef08a".to_string(),
                accent_primary: "#ffe600".to_string(),
                col1: "#ffe600".to_string(), // Acid Yellow
                col1_text: "#000000".to_string(),
                col2: "#10b981".to_string(), // Acid Emerald
                col2_text: "#000000".to_string(),
                col3: "#a855f7".to_string(), // Rave Purple
                col3_text: "#ffffff".to_string(),
                col4: "#06b6d4".to_string(), // Radioactive Cyan
                col4_text: "#000000".to_string(),
                col5: "#ec4899".to_string(), // Club Hot Pink
                col5_text: "#ffffff".to_string(),
                stripes: vec![
                    "#ffe600".to_string(),
                    "#10b981".to_string(),
                    "#a855f7".to_string(),
                    "#06b6d4".to_string(),
                    "#ec4899".to_string(),
                ],
            },
        }
    }

    /// Casio CZ / RZ Tri-Color theme
    pub fn casio_cz() -> Self {
        Self {
            id: "casio_cz".to_string(),
            name: "Casio Tri-Color".to_string(),
            manufacturer_badge: "CASIO".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#0c131a".to_string(),
                card_bg: "rgba(0, 0, 0, 0.25)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#bae6fd".to_string(),
                accent_primary: "#0284c7".to_string(),
                col1: "#0284c7".to_string(), // Casio Blue
                col1_text: "#ffffff".to_string(),
                col2: "#ef4444".to_string(), // Casio Red
                col2_text: "#ffffff".to_string(),
                col3: "#eab308".to_string(), // Casio Yellow
                col3_text: "#000000".to_string(),
                col4: "#10b981".to_string(), // Casio Green
                col4_text: "#ffffff".to_string(),
                col5: "#6366f1".to_string(), // Casio Indigo
                col5_text: "#ffffff".to_string(),
                stripes: vec![
                    "#0284c7".to_string(),
                    "#ef4444".to_string(),
                    "#eab308".to_string(),
                    "#10b981".to_string(),
                    "#6366f1".to_string(),
                ],
            },
        }
    }

    /// Classic Windows 8 Cobalt Blue theme
    pub fn windows_8_cobalt() -> Self {
        Self {
            id: "win8_cobalt".to_string(),
            name: "Windows 8 Cobalt".to_string(),
            manufacturer_badge: "MODERN".to_string(),
            mode: VibrancyMode::SolidColor,
            palette: MetroPalette {
                page_bg: "#001e54".to_string(),
                card_bg: "rgba(0, 0, 0, 0.2)".to_string(),
                text_primary: "#ffffff".to_string(),
                text_secondary: "#bfdbfe".to_string(),
                accent_primary: "#0078d7".to_string(),
                col1: "#0050ef".to_string(), // Cobalt Blue
                col1_text: "#ffffff".to_string(),
                col2: "#00aba9".to_string(), // Modern Teal
                col2_text: "#ffffff".to_string(),
                col3: "#6a00ff".to_string(), // Modern Indigo
                col3_text: "#ffffff".to_string(),
                col4: "#d80073".to_string(), // Modern Magenta
                col4_text: "#ffffff".to_string(),
                col5: "#a4c400".to_string(), // Modern Lime
                col5_text: "#000000".to_string(),
                stripes: vec![
                    "#0050ef".to_string(),
                    "#00aba9".to_string(),
                    "#6a00ff".to_string(),
                    "#d80073".to_string(),
                    "#a4c400".to_string(),
                ],
            },
        }
    }
}
