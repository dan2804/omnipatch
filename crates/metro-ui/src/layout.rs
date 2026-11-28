use serde::{Deserialize, Serialize};
use crate::widget::ParameterDef;

/// A vertical column within the Metro horizontal panoramic hub
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetroColumn {
    pub id: String,
    pub title: String,
    #[serde(default)]
    pub subtitle: Option<String>,
    pub color: String,
    pub text_color: String,
    pub width_px: u32,
    pub parameters: Vec<ParameterDef>,
    #[serde(default)]
    pub footer_labels: Vec<String>,
}

impl MetroColumn {
    pub fn new(id: &str, title: &str, color: &str, text_color: &str) -> Self {
        Self {
            id: id.to_string(),
            title: title.to_string(),
            subtitle: None,
            color: color.to_string(),
            text_color: text_color.to_string(),
            width_px: 320,
            parameters: Vec::new(),
            footer_labels: Vec::new(),
        }
    }

    pub fn with_width(mut self, width: u32) -> Self {
        self.width_px = width;
        self
    }

    pub fn with_subtitle(mut self, sub: &str) -> Self {
        self.subtitle = Some(sub.to_string());
        self
    }

    pub fn add_param(mut self, param: ParameterDef) -> Self {
        self.parameters.push(param);
        self
    }

    pub fn with_footer(mut self, left: &str, right: &str) -> Self {
        self.footer_labels = vec![left.to_string(), right.to_string()];
        self
    }
}

/// Windows 8 Live Tile size specifications
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum TileSize {
    /// 1x1 Standard square tile (e.g. 140x140)
    Square1x1,
    /// 2x1 Wide rectangular tile (e.g. 290x140)
    Wide2x1,
    /// 2x2 Large square tile (e.g. 290x290)
    Large2x2,
}

impl Default for TileSize {
    fn default() -> Self {
        Self::Square1x1
    }
}

/// A Windows 8 Live Tile
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetroTile {
    pub id: String,
    pub title: String,
    #[serde(default)]
    pub subtitle: Option<String>,
    #[serde(default)]
    pub badge: Option<String>,
    pub size: TileSize,
    pub bg_color: String,
    pub text_color: String,
    #[serde(default)]
    pub live_value: Option<String>,
    #[serde(default)]
    pub action: Option<String>,
}

impl MetroTile {
    pub fn new(id: &str, title: &str, bg_color: &str, text_color: &str) -> Self {
        Self {
            id: id.to_string(),
            title: title.to_string(),
            subtitle: None,
            badge: None,
            size: TileSize::Square1x1,
            bg_color: bg_color.to_string(),
            text_color: text_color.to_string(),
            live_value: None,
            action: None,
        }
    }

    pub fn wide(mut self) -> Self {
        self.size = TileSize::Wide2x1;
        self
    }

    pub fn large(mut self) -> Self {
        self.size = TileSize::Large2x2;
        self
    }

    pub fn with_badge(mut self, badge: &str) -> Self {
        self.badge = Some(badge.to_string());
        self
    }

    pub fn with_subtitle(mut self, sub: &str) -> Self {
        self.subtitle = Some(sub.to_string());
        self
    }

    pub fn with_value(mut self, val: &str) -> Self {
        self.live_value = Some(val.to_string());
        self
    }
}

/// Action button in the circular Windows 8 App Bar
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct AppBarAction {
    pub id: String,
    pub label: String,
    pub icon_glyph: String, // e.g. "▶", "💾", "⤓", "⇄"
}

/// Complete Metro Hub layout representing a full application view
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct MetroHub {
    pub title: String,
    pub subtitle: String,
    pub manufacturer_badge: String,
    pub active_patch_name: String,
    pub columns: Vec<MetroColumn>,
    pub tiles: Vec<MetroTile>,
    pub app_bar_actions: Vec<AppBarAction>,
}

impl MetroHub {
    pub fn new(title: &str, subtitle: &str, badge: &str) -> Self {
        Self {
            title: title.to_string(),
            subtitle: subtitle.to_string(),
            manufacturer_badge: badge.to_string(),
            active_patch_name: "DEFAULT PRESET".to_string(),
            columns: Vec::new(),
            tiles: Vec::new(),
            app_bar_actions: vec![
                AppBarAction { id: "audition".into(), label: "audition".into(), icon_glyph: "▶".into() },
                AppBarAction { id: "save".into(), label: "save".into(), icon_glyph: "💾".into() },
                AppBarAction { id: "export".into(), label: "export .syx".into(), icon_glyph: "⤓".into() },
                AppBarAction { id: "compare".into(), label: "compare a/b".into(), icon_glyph: "⇄".into() },
            ],
        }
    }

    pub fn add_column(&mut self, col: MetroColumn) {
        self.columns.push(col);
    }

    pub fn add_tile(&mut self, tile: MetroTile) {
        self.tiles.push(tile);
    }
}
