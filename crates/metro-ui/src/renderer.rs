use crate::layout::{MetroColumn, MetroHub, TileSize};
use crate::theme::{MetroTheme, VibrancyMode};
use crate::widget::{ParameterDef, WidgetType};

/// Universal HTML/CSS/JS renderer for Windows 8 Metro UI
pub struct MetroHtmlRenderer;

impl MetroHtmlRenderer {
    /// Compiles a MetroHub and MetroTheme into a self-contained, interactive HTML5 application
    pub fn render_to_html(hub: &MetroHub, theme: &MetroTheme) -> String {
        let mode_class = match theme.mode {
            VibrancyMode::SolidColor => "mode-solid",
            VibrancyMode::SurfaceLight => "mode-light",
            VibrancyMode::NeonDark => "mode-dark",
        };

        let mut columns_html = String::new();
        for (idx, col) in hub.columns.iter().enumerate() {
            columns_html.push_str(&Self::render_column(col, idx + 1));
        }

        let mut tiles_html = String::new();
        for tile in &hub.tiles {
            let (span_class, size_label) = match tile.size {
                TileSize::Square1x1 => ("", "1x1"),
                TileSize::Wide2x1 => ("col-span-2", "2x1"),
                TileSize::Large2x2 => ("col-span-2 row-span-2 p-6", "2x2"),
            };

            let badge_html = tile.badge.as_deref().map(|b| {
                format!(r#"<span class="text-xs font-black uppercase tracking-widest bg-black text-white px-2 py-0.5 font-mono">{}</span>"#, b)
            }).unwrap_or_default();

            let value_html = tile.live_value.as_deref().map(|v| {
                format!(r#"<div class="text-4xl font-light font-mono my-2">{}</div>"#, v)
            }).unwrap_or_default();

            tiles_html.push_str(&format!(
                r#"
                <div class="metro-tile {span_class}" style="background-color: {bg}; color: {text};" onclick="{action}">
                  <div class="flex justify-between items-start">
                    {badge_html}
                    <span class="text-[10px] font-mono font-bold opacity-75">{size_label}</span>
                  </div>
                  <div>
                    {value_html}
                    <div class="text-2xl font-light leading-tight">{title}</div>
                    <div class="text-xs opacity-90 mt-1">{subtitle}</div>
                  </div>
                </div>
                "#,
                span_class = span_class,
                bg = tile.bg_color,
                text = tile.text_color,
                action = tile.action.as_deref().unwrap_or(""),
                badge_html = badge_html,
                size_label = size_label,
                value_html = value_html,
                title = tile.title,
                subtitle = tile.subtitle.as_deref().unwrap_or(""),
            ));
        }

        let stripes_html: String = theme.palette.stripes.iter().map(|c| {
            format!(r#"<span style="background-color: {}; flex: 1;"></span>"#, c)
        }).collect();

        format!(
            r#"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Metro UI Engine</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@200;300;400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

    * {{
      border-radius: 0px !important;
      box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
      user-select: none;
      overflow-x: auto;
      transition: background-color 0.15s ease, color 0.15s ease;
    }}

    .font-mono-code {{ font-family: 'JetBrains Mono', monospace; }}

    /* Typography */
    .metro-title-huge {{
      font-size: 52px;
      font-weight: 200;
      letter-spacing: -0.03em;
      line-height: 1;
    }}

    /* Vibrancy Modes */
    body.mode-solid {{
      background-color: var(--page-bg);
      color: #ffffff;
    }}
    body.mode-solid .metro-col-surface {{
      background-color: var(--col-bg);
      color: var(--col-text);
    }}
    body.mode-solid .metro-card-panel {{
      background-color: rgba(0, 0, 0, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    body.mode-light {{
      background-color: #f4f4f7;
      color: #111116;
    }}
    body.mode-light .metro-col-surface {{
      background-color: #ffffff;
      color: #111116;
      border-top: 8px solid var(--col-bg);
      box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    }}
    body.mode-light .metro-card-panel {{
      background-color: #f9f9fb;
      border: 1px solid #e2e2e8;
    }}

    body.mode-dark {{
      background-color: #0b0c10;
      color: #ffffff;
    }}
    body.mode-dark .metro-col-surface {{
      background-color: #13141c;
      color: #ffffff;
      border-top: 6px solid var(--col-bg);
      border-bottom: 4px solid var(--col-bg);
    }}
    body.mode-dark .metro-card-panel {{
      background-color: #1b1c26;
      border: 1px solid #282a3a;
    }}

    /* Sliders */
    .metro-slider-bar {{
      height: 10px;
      background: rgba(0, 0, 0, 0.35);
      position: relative;
      cursor: pointer;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    .metro-slider-fill {{
      height: 100%;
      background: #ffffff;
      transition: width 0.05s ease;
    }}
    .metro-slider-thumb {{
      width: 14px;
      height: 26px;
      background: #ffffff;
      border: 2px solid #000000;
      position: absolute;
      top: -9px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.4);
      pointer-events: none;
    }}

    /* WinRT Toggle */
    .metro-toggle-box {{
      width: 48px;
      height: 22px;
      border: 2px solid currentColor;
      background: rgba(0, 0, 0, 0.25);
      position: relative;
      cursor: pointer;
      transition: all 0.12s ease;
    }}
    .metro-toggle-box .thumb {{
      width: 12px;
      height: 14px;
      background: #ffffff;
      position: absolute;
      top: 2px;
      left: 2px;
      transition: all 0.12s cubic-bezier(0.1, 0.9, 0.2, 1);
    }}
    .metro-toggle-box.is-on {{
      background: #ffffff;
    }}
    .metro-toggle-box.is-on .thumb {{
      background: #000000;
      left: 30px;
    }}

    /* Tiles */
    .metro-tile {{
      cursor: pointer;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 16px;
      transition: transform 0.08s ease, outline 0.08s ease;
    }}
    .metro-tile:hover {{
      outline: 3px solid #ffffff;
      z-index: 10;
    }}
    .metro-tile:active {{
      transform: perspective(600px) scale(0.97) rotateX(2deg);
    }}
  </style>
</head>
<body class="{mode_class} min-h-screen flex flex-col justify-between" id="metro-root" style="
  --page-bg: {page_bg};
  --accent: {accent};
">

  <!-- Multi-Stripe Accent Ribbon -->
  <div class="h-1.5 w-full flex">
    {stripes_html}
  </div>

  <!-- Header -->
  <header class="px-8 py-3.5 bg-black/40 border-b border-white/10 flex flex-wrap items-center justify-between gap-4">
    <div class="flex items-center gap-6">
      <div class="flex items-center gap-2">
        <span class="text-xs font-black uppercase tracking-widest px-2.5 py-1 text-black font-mono" style="background-color: {accent}">{badge}</span>
        <span class="text-sm font-bold tracking-widest uppercase font-mono">METRO UI ENGINE</span>
      </div>
    </div>

    <!-- Mode & View Switchers -->
    <div class="flex items-center gap-3">
      <div class="flex items-center border border-white/20 bg-black/30 p-0.5">
        <button class="px-3 py-1 text-xs font-bold uppercase cursor-pointer bg-white text-black" onclick="setMode('solid')">Solid Color</button>
        <button class="px-3 py-1 text-xs font-bold uppercase cursor-pointer opacity-70 hover:opacity-100" onclick="setMode('light')">Surface Light</button>
        <button class="px-3 py-1 text-xs font-bold uppercase cursor-pointer opacity-70 hover:opacity-100" onclick="setMode('dark')">Neon Dark</button>
      </div>

      <div class="flex items-center border border-white/20 bg-black/30 p-0.5">
        <button class="px-4 py-1 text-xs font-bold uppercase cursor-pointer bg-white text-black" id="tab-hub" onclick="switchView('hub')">Hub Panorama</button>
        <button class="px-4 py-1 text-xs font-bold uppercase cursor-pointer opacity-70 hover:opacity-100" id="tab-tiles" onclick="switchView('tiles')">Start Screen Tiles</button>
      </div>
    </div>
  </header>

  <!-- Main Panoramic Canvas -->
  <main class="flex-1 px-8 pt-5 pb-4 overflow-x-auto">
    <div id="view-hub" class="space-y-6">
      <div class="flex items-baseline justify-between border-b border-white/15 pb-4">
        <div class="flex items-baseline gap-4">
          <h1 class="metro-title-huge">{title}</h1>
          <span class="text-xl font-light font-mono uppercase opacity-90">{subtitle}</span>
        </div>
        <div class="bg-black/40 border-2 border-white px-5 py-2 flex items-center gap-4">
          <span class="text-xs font-bold uppercase tracking-wider opacity-75">Active:</span>
          <span class="text-base font-bold font-mono tracking-wide">{active_patch}</span>
        </div>
      </div>

      <!-- Panoramic Columns -->
      <div class="flex gap-6 pb-6 pt-1">
        {columns_html}
      </div>
    </div>

    <!-- Start Screen Live Tiles -->
    <div id="view-tiles" class="hidden space-y-6 pb-6">
      <div class="flex items-baseline gap-4 border-b border-white/15 pb-4">
        <h1 class="metro-title-huge">start screen</h1>
        <span class="text-xl font-light font-mono uppercase opacity-75">interactive live tiles</span>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3.5 auto-rows-[140px]">
        {tiles_html}
      </div>
    </div>
  </main>

  <script>
    function setMode(mode) {{
      const r = document.getElementById('metro-root');
      r.className = r.className.replace(/mode-(solid|light|dark)/g, '');
      r.classList.add('mode-' + mode);
    }}

    function switchView(view) {{
      const hub = document.getElementById('view-hub');
      const tiles = document.getElementById('view-tiles');
      if (view === 'hub') {{
        hub.classList.remove('hidden');
        tiles.classList.add('hidden');
      }} else {{
        hub.classList.add('hidden');
        tiles.classList.remove('hidden');
      }}
    }}

    function toggleSwitch(el) {{
      el.classList.toggle('is-on');
    }}

    function setSlider(e, id, max) {{
      const rect = e.currentTarget.getBoundingClientRect();
      const pct = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
      const val = Math.round(pct * max);
      const fill = document.getElementById('fill-' + id);
      const thumb = document.getElementById('thumb-' + id);
      const label = document.getElementById('val-' + id);
      if (fill) fill.style.width = (pct * 100) + '%';
      if (thumb) thumb.style.left = 'calc(' + (pct * 100) + '% - 7px)';
      if (label) label.innerText = val;
    }}
  </script>
</body>
</html>"#,
            title = hub.title,
            subtitle = hub.subtitle,
            badge = hub.manufacturer_badge,
            active_patch = hub.active_patch_name,
            mode_class = mode_class,
            page_bg = theme.palette.page_bg,
            accent = theme.palette.accent_primary,
            stripes_html = stripes_html,
            columns_html = columns_html,
            tiles_html = tiles_html,
        )
    }

    fn render_column(col: &MetroColumn, _col_num: usize) -> String {
        let mut params_html = String::new();
        for param in &col.parameters {
            params_html.push_str(&Self::render_parameter(param));
        }

        let footer_html = if col.footer_labels.len() >= 2 {
            format!(
                r#"<div class="mt-4 pt-3 border-t border-current/20 flex justify-between text-[11px] font-mono opacity-80">
                     <span>{}</span>
                     <span>{}</span>
                   </div>"#,
                col.footer_labels[0], col.footer_labels[1]
            )
        } else {
            String::new()
        };

        format!(
            r#"
            <div class="metro-col-surface p-5 flex flex-col justify-between flex-shrink-0" style="--col-bg: {color}; --col-text: {text_color}; width: {width}px;">
              <div>
                <div class="flex justify-between items-baseline mb-4 border-b border-current/30 pb-2">
                  <h2 class="text-2xl font-light tracking-tight lowercase">{title}</h2>
                  <span class="text-xs font-mono font-bold uppercase opacity-80">{sub}</span>
                </div>
                <div class="space-y-4">
                  {params_html}
                </div>
              </div>
              {footer_html}
            </div>
            "#,
            color = col.color,
            text_color = col.text_color,
            width = col.width_px,
            title = col.title,
            sub = col.subtitle.as_deref().unwrap_or(""),
            params_html = params_html,
            footer_html = footer_html,
        )
    }

    fn render_parameter(param: &ParameterDef) -> String {
        match &param.widget {
            WidgetType::Slider { min, max, unit, .. } => {
                let default_val = param.default_value.as_i64().unwrap_or(*min);
                let pct = if *max > *min { ((default_val - *min) as f64 / (*max - *min) as f64 * 100.0) as i64 } else { 50 };
                let unit_str = unit.as_deref().unwrap_or("");

                format!(
                    r#"
                    <div>
                      <div class="flex justify-between text-xs font-bold mb-1">
                        <span>{name}</span>
                        <span class="font-mono text-sm font-black" id="val-{id}">{val}{unit}</span>
                      </div>
                      <div class="metro-slider-bar" onclick="setSlider(event, '{id}', {max})">
                        <div class="metro-slider-fill" id="fill-{id}" style="width: {pct}%;"></div>
                        <div class="metro-slider-thumb" id="thumb-{id}" style="left: calc({pct}% - 7px);"></div>
                      </div>
                    </div>
                    "#,
                    name = param.name,
                    id = param.id,
                    val = default_val,
                    unit = unit_str,
                    max = max,
                    pct = pct,
                )
            }
            WidgetType::Toggle { on_label, .. } => {
                let is_on = param.default_value.as_bool().unwrap_or(true);
                let active_class = if is_on { "is-on" } else { "" };
                format!(
                    r#"
                    <div class="flex items-center justify-between p-2.5 metro-card-panel">
                      <span class="text-xs font-bold">{name}</span>
                      <div class="flex items-center gap-2">
                        <div class="metro-toggle-box {active_class}" onclick="toggleSwitch(this)">
                          <div class="thumb"></div>
                        </div>
                        <span class="text-xs font-bold uppercase">{label}</span>
                      </div>
                    </div>
                    "#,
                    name = param.name,
                    active_class = active_class,
                    label = on_label,
                )
            }
            WidgetType::SegmentGroup { options } => {
                let buttons_html: String = options.iter().enumerate().map(|(idx, opt)| {
                    let is_active = idx == 0;
                    let style = if is_active {
                        "border-2 border-white bg-white text-black font-black"
                    } else {
                        "border border-current bg-black/20 hover:bg-black/40"
                    };
                    format!(r#"<button class="py-2 text-xs font-bold cursor-pointer {style}">{opt}</button>"#)
                }).collect();

                format!(
                    r#"
                    <div>
                      <span class="text-xs font-bold uppercase tracking-wider block mb-2 opacity-90">{name}</span>
                      <div class="grid grid-cols-{count} gap-1">
                        {buttons}
                      </div>
                    </div>
                    "#,
                    name = param.name,
                    count = options.len().max(1),
                    buttons = buttons_html,
                )
            }
            WidgetType::StepSequencer { steps, tracks } => {
                let mut pads_html = String::new();
                for step in 1..=*steps {
                    let is_downbeat = step % 4 == 1;
                    let pad_style = if is_downbeat { "bg-white text-black font-black" } else { "bg-black/30 text-white font-bold" };
                    pads_html.push_str(&format!(
                        r#"<div class="p-2 border border-current text-center cursor-pointer {pad_style}">
                             <div class="text-[10px]">{step}</div>
                             <div class="h-6 mt-1 bg-current opacity-60"></div>
                           </div>"#
                    ));
                }

                format!(
                    r#"
                    <div class="p-3 metro-card-panel">
                      <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-bold uppercase">{name}</span>
                        <span class="text-[10px] font-mono opacity-80">{tracks}</span>
                      </div>
                      <div class="grid grid-cols-8 gap-1">
                        {pads}
                      </div>
                    </div>
                    "#,
                    name = param.name,
                    tracks = tracks.join(" · "),
                    pads = pads_html,
                )
            }
            _ => String::new(),
        }
    }
}
