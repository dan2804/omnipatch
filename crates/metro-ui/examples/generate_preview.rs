use metro_ui::{create_juno_106_hub, MetroHtmlRenderer};
use std::fs;

fn main() -> anyhow::Result<()> {
    let (hub, theme) = create_juno_106_hub();
    let html = MetroHtmlRenderer::render_to_html(&hub, &theme);
    
    let out_path = "preview/metro_engine_demo.html";
    fs::write(out_path, html)?;
    println!("Successfully generated standalone Metro UI engine preview at {}", out_path);
    Ok(())
}
