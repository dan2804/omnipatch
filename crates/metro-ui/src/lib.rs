//! # Metro UI Engine
//!
//! A high-performance, cross-platform Windows 8 Metro / Modern UI framework.
//! Features strict 0px border-radius geometry, Segoe UI typographic hierarchies,
//! full-bleed saturated color blocks, interactive live tiles, and panoramic hubs.

pub mod layout;
pub mod renderer;
pub mod store;
pub mod theme;
pub mod widget;

pub use layout::{AppBarAction, MetroColumn, MetroHub, MetroTile, TileSize};
pub use renderer::MetroHtmlRenderer;
pub use store::{ParamValue, ParameterStore};
pub use theme::{MetroPalette, MetroTheme, VibrancyMode};
pub use widget::{ParameterDef, WidgetType};

/// Helper function to generate an iconic Roland Juno-106 Metro Hub
pub fn create_juno_106_hub() -> (MetroHub, MetroTheme) {
    let theme = MetroTheme::juno_106();
    let mut hub = MetroHub::new("juno 106", "polyphonic synthesizer", "ROLAND");
    hub.active_patch_name = "A-11 STRING ENS 1".to_string();

    // Column 1: DCO
    let col1 = MetroColumn::new("dco", "dco oscillators", &theme.palette.col1, &theme.palette.col1_text)
        .with_subtitle("dco 01")
        .add_param(ParameterDef::new_segment("dco_oct", "Octave Range", &["16'", "8'", "4'"], 1))
        .add_param(ParameterDef::new_toggle("dco_pulse", "Pulse Wave [ ⎍ ]", true))
        .add_param(ParameterDef::new_toggle("dco_saw", "Sawtooth Wave [ ⩘ ]", true))
        .add_param(ParameterDef::new_slider("dco_pwm", "Pulse Width Modulation", 0, 127, 64, None))
        .add_param(ParameterDef::new_slider("dco_sub", "Sub-Oscillator Level", 0, 127, 75, None))
        .with_footer("DCO SYNTH CORE", "6 VOICES");
    hub.add_column(col1);

    // Column 2: VCF
    let col2 = MetroColumn::new("vcf", "filter & vcf", &theme.palette.col2, &theme.palette.col2_text)
        .with_subtitle("ir3109")
        .add_param(ParameterDef::new_segment("hpf_pos", "High-Pass Filter", &["0", "1", "2", "3"], 0))
        .add_param(ParameterDef::new_slider("vcf_cut", "Cutoff Frequency (24dB)", 0, 127, 84, None))
        .add_param(ParameterDef::new_slider("vcf_res", "Resonance (Self-Osc)", 0, 127, 42, None))
        .add_param(ParameterDef::new_slider("vcf_env", "Envelope Modulation", 0, 127, 70, None))
        .with_footer("ANALOG LOWPASS", "24 DB/OCT");
    hub.add_column(col2);

    // Column 3: Envelope
    let col3 = MetroColumn::new("adsr", "envelope adsr", &theme.palette.col3, &theme.palette.col3_text)
        .with_width(340)
        .with_subtitle("transient")
        .add_param(ParameterDef::new_slider("adsr_att", "Attack Time", 0, 127, 15, Some("ms")))
        .add_param(ParameterDef::new_slider("adsr_dec", "Decay Time", 0, 127, 65, Some("ms")))
        .add_param(ParameterDef::new_slider("adsr_sus", "Sustain Level", 0, 127, 95, None))
        .add_param(ParameterDef::new_slider("adsr_rel", "Release Time", 0, 127, 45, Some("ms")))
        .with_footer("ANALOG GENERATOR", "SHAPE 01");
    hub.add_column(col3);

    // Column 4: Arpeggiator & Rhythmic Sequencer (Demonstrates complex sub-systems)
    let col4 = MetroColumn::new("arp", "phrase arpeggiator", &theme.palette.col4, &theme.palette.col4_text)
        .with_width(360)
        .with_subtitle("clock sync")
        .add_param(ParameterDef::new_toggle("arp_on", "Arpeggiator Enable", true))
        .add_param(ParameterDef::new_segment("arp_mode", "Motif Direction", &["UP", "DOWN", "U/D", "RANDOM"], 0))
        .add_param(ParameterDef::new_slider("arp_rate", "Clock Rate / Tempo", 40, 240, 120, Some("BPM")))
        .add_param(ParameterDef::new_arpeggiator("arp_steps", "16-Step Pattern", 16))
        .with_footer("STEP MATRIX", "16 STEPS");
    hub.add_column(col4);

    // Add Live Tiles for the Start Screen view
    hub.add_tile(
        MetroTile::new("tile_juno", "Juno-106", &theme.palette.col1, "#ffffff")
            .wide()
            .with_badge("ROLAND")
            .with_subtitle("128 Patches · DCO Poly · IR3109")
    );
    hub.add_tile(
        MetroTile::new("tile_dx7", "DX7-II FD", "#00a499", "#000000")
            .with_badge("YAMAHA")
            .with_subtitle("32 Algs · 6-Op FM")
    );
    hub.add_tile(
        MetroTile::new("tile_nord", "Nord Lead 2X", "#d90429", "#ffffff")
            .with_badge("CLAVIA")
            .with_subtitle("Virtual Analog Poly")
    );
    hub.add_tile(
        MetroTile::new("tile_orbit", "Orbit-3 / XL-1", "#ffe600", "#000000")
            .with_badge("E-MU")
            .with_subtitle("Z-Plane Morphing")
    );

    (hub, theme)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_create_hub_and_render_html() {
        let (hub, theme) = create_juno_106_hub();
        assert_eq!(hub.columns.len(), 4);
        assert_eq!(hub.tiles.len(), 4);

        let html = MetroHtmlRenderer::render_to_html(&hub, &theme);
        assert!(html.contains("juno 106"));
        assert!(html.contains("dco oscillators"));
        assert!(html.contains("phrase arpeggiator"));
        assert!(html.contains("mode-solid"));
    }

    #[test]
    fn test_parameter_store_reactivity() {
        let store = ParameterStore::new();
        store.set_i64("cutoff", 84);
        assert_eq!(store.get_i64("cutoff"), Some(84));

        store.set_bool("lfo_sync", true);
        assert_eq!(store.get_bool("lfo_sync"), Some(true));

        let json = store.export_json();
        assert!(json.contains("84"));
    }
}
