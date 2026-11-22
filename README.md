# OmniPatch

> **Universal Cross-Platform MIDI/SysEx Librarian & Patch Editor in Rust**
> Compatible with **Windows, macOS, Linux, FreeBSD, and OpenBSD**.

Inspired by Sound Quest's **Midi Quest 13**, **OmniPatch** combines a clean, fast **Windows 8 Metro / Modern UI** navigation hub with authentic, hardware-tailored skins for vintage analog, virtual analog, and digital rackmount synthesizers.

![OmniPatch Windows 8 Metro UI Studio Hub](assets/screenshots/studio_hub.png)

---

## Features

- **Cross-Platform Rust Core:** High-performance, memory-safe engine running natively across Windows, macOS, Linux, FreeBSD, and OpenBSD.
- **Hardware-Specific Authentic Skins:** Individual hardware modules rendered with real-time reactive displays (vintage LCDs, LED segment displays, rotary knobs, sliders, and canvas spectrum curves).
- **Embedded SQLite Librarian (`rusqlite`):** Fast local patch database storing binary `.syx` blobs, categories, bank indices, and user tags with instant full-text search.
- **Declarative Device Profiles (`.yaml`):** Adding support for a new synthesizer requires zero Rust code changes—just drop a YAML definition file into `devices/`.
- **Vintage Hardware Pacing & Throttling:** Configurable inter-byte and chunk delays to protect vintage 8-bit/16-bit microcontrollers from UART buffer overflow.
- **AI / PDF Manual Ingestion Tool:** Automated PDF extraction utility that scans synth manuals, identifies MIDI Implementation Charts and SysEx tables, and outputs draft profiles.

---

## Supported Synthesizers (Initial Release)

| Synthesizer | Type | Parameters | Presets Loaded | Special Features |
| :--- | :--- | :---: | :---: | :--- |
| **Access Virus A** | Virtual Analog (DSP56303) | 17 | 256 | Multi-page SysEx (Pages A, B, C), 256-byte dumps, 7-bit checksum |
| **Akai AX60** | 6-Voice Polyphonic Analog | 23 | 64 | Curtis CEM3394 engine, Tauntek CC mapping (CC 14–74), 3,445B Bank SysEx |
| **E-MU Audity 2000 (v2)** | 64-Voice Modular Rack | 53 | 640 | Light blue metallic chassis, greyish-white buttons, 4 modules (MultiMode, Presets, Arp, FX) |
| **E-MU B-3** | 64-Voice Tonewheel Organ | 25 | 384 | Brownish-white parchment panel, black buttons, 9 Hammond Drawbars, Leslie 122 Rotary |
| **E-MU Carnaval** | 32-Voice Latin & World Percussion | 24 | 640 | BEATS interactive drum machine, X-Factor polyrhythmic groove crossfade, 5 Banks |
| **E-MU Emax** | 12-Bit Analog VCF Sampler | 24 | 72 | SSM2047 24dB/oct resonant analog filters, dual AHDSR envs, dual voice stack, MIDI SDS |
| **E-MU Emax II** | 16-Bit Stereo Workstation | 24 | 80 | 32-voice stereo sampling, digital resonant 4-pole VCF, Spectrum Interpolation, 4-layer stack |
| **E-MU Xtreme Lead-1** | 64-Voice Dance & Techno Synth | 14 | 512 | Electric yellow 1U chassis, black knobs & tactile buttons, 50 Z-Plane filters, 16-track SuperBEATS (Model ID 0x0F) |
| **E-MU XL-7** | 128-Voice Desktop Workstation | 18 | 512 | Electric yellow desktop command station, 16 velocity pads, 16 knobs, 16-track sequencer (384 PPQN) |
| **E-MU XK-6** | 61-Key Dance Performance Keyboard | 10 | 512 | Anthracite & electric yellow 61-key performance keyboard, 61 synth-action keys, SuperBEATS interactive engine |
| **E-MU Virtuoso 2000** | 128-Voice Virtual Orchestra | 10 | 512 | Light silver-grey 1U faceplate, unbroken continuous navy wave line, black tactile buttons, 64MB Orchestral Sessions Vol 1 & 2 ROMs, 50 Z-Plane filters, 2x24 green LCD (Model ID 0x0D) |
| **E-MU Vintage Pro** | 128-Voice Vintage Workstation | 10 | 512 | Two-tone pewter & black anodized faceplate with silver hex bolts, 5 spun-aluminum vintage knobs, 64MB Vintage Collection ROM, 9 Midi Quest 13 editors (Model ID 0x11) |
| **E-MU Vintage Keys** | 32-Voice Vintage Keyboard Module | 10 | 512 | 1993 original 1U matte dark charcoal chassis, 11x5 cyan dot matrix, 2x16 green LCD, 5-button tactile matrix, stepped DATA wheel, red E•MU SYSTEMS logo (Model ID 0x0B) |
| **E-MU Proteus 1000** | 64-Voice 1U Sound Module | 7 | 1,024 | 30th Anniversary Edition, matte black 1U chassis, blue trapezoid LCD frame, ivory ribbed knobs & tactile buttons, 32MB Composer ROM (Model ID 0x0F / 0x04) |
| **E-MU Proteus 2000** | 128-Voice Flagship Sound Module | 8 | 1,024 | Sleek black 1U chassis, greyish-white knobs, 32MB Composer ROM, 4 ROM expansion slots |
| **E-MU Proteus 2500** | 128-Voice Command Station Console | 8 | 1,024 | Industrial grey desktop console, blue accents, 16 velocity pads, 16 knobs, multi-channel sequencer |
| **E-MU Planet Phatt** | 32-Voice Hip-Hop / R&B Sound Module | 24 | 640 | Metallic magenta anodized 1U faceplate, street-art bubble graffiti logo with orbiting planetary ring, cyan cursive "The Swing System" subtitle, 32 digital 6th-order filters, BEATS swing groove engine, 10 Midi Quest 13 editors (Model ID 0x0A) |
| **E-MU Planet Earth** | 64-Voice World Expedition Module | 16 | 1,024 | Oceanic teal / two-tone turquoise metallic 1U chassis, black trapezoid LCD bezel, black knobs with white pointers, 32MB World ROM, 50 Z-Plane filters, SuperBEATS arpeggiator, 9 Midi Quest 13 editors (Model ID 0x0F / 0x05) |
| **E-MU Orbit-3** | 128-Voice Super Dance Module | 7 | 1,024 | Electric neon yellow 1U faceplate, black tactile buttons, Beat Garden & Techno Yard ROMs |
| **E-MU Orbit 9090** | 32-Voice 1996 Dance Planet | 7 | 512 | Classic golden yellow 1U rack, black buttons, 909/808 drum machines, TB-303 acid lines |
| **E-MU SP-1200** | 12-Bit Linear Sampling Drum Machine | 12 | 32 | Classic E-MU blue and grey chassis, SSM2044 dynamic lowpass filter, 8 touch pads & sliders |
| **Casio CZ-1** | Flagship 16-DCO Phase Distortion | 26 | 128 | Professional black chassis, electric blue tactile buttons, velocity & aftertouch, stereo BBD chorus |
| **Casio CZ-1000** | 8-Voice Phase Distortion Keyboard | 22 | 32 | Industrial matte grey chassis, iconic tri-color (blue/yellow/red) membrane touchpads, 49 full-sized keys |
| **Casio CZ-101** | 4/8-Voice Portable Phase Distortion | 22 | 32 | Iconic compact matte black keytar chassis, guitar strap pegs, tri-color membrane buttons, dual line PD |
| **Casio CZ-230S** | Phase Distortion + PCM Rhythm Workstation | 11 | 103 | Light silver-grey console, built-in monitor speakers, RZ-1 derived PCM drums, 99 presets + 20 rhythms |
| **Casio CZ-3000** | 16-DCO Phase Distortion with Chorus | 23 | 64 | Dark anthracite metal chassis, 61 keys, dedicated tactile LED switches, built-in analog BBD stereo chorus |
| **Casio CZ-5000** | Flagship 16-DCO Workstation with Sequencer | 25 | 64 | Dark titanium workstation, 8-track polyphonic hardware sequencer console (3,500 notes), chorus unit |

---

## Hardware Editor Screenshots

### Access Virus A (Virtual Analog Synthesizer)
![Access Virus A Hardware Editor](assets/screenshots/access_virus_a.png)

### Akai AX60 (Polyphonic Analog Synthesizer)
![Akai AX60 Hardware Editor](assets/screenshots/akai_ax60.png)

### E-MU Audity 2000 (Z-Plane Modular Rack Synthesizer)
![E-MU Audity 2000 Hardware Editor](assets/screenshots/emu_audity_2000.png)

### E-MU B-3 (Tonewheel Organ & Leslie 122 Rotary Cabinet)
![E-MU B-3 Tonewheel Organ](assets/screenshots/emu_b3.png)

### E-MU Carnaval (Latin & World Percussion with BEATS Engine)
![E-MU Carnaval BEATS Console](assets/screenshots/emu_carnaval.png)

### E-MU Emax (12-Bit Linear Sampler with SSM2047 Analog VCF)
![E-MU Emax Analog VCF Sampler](assets/screenshots/emu_emax.png)

### E-MU Emax II (16-Bit Stereo Digital Sampling Workstation)
![E-MU Emax II Digital Sampler](assets/screenshots/emu_emax_ii.png)

### E-MU Xtreme Lead-1 (Dance & Techno Synthesizer with SuperBEATS)
![E-MU Xtreme Lead-1 Hardware Editor](assets/screenshots/emu_xl1.png)

### E-MU XL-7 (Command Station Desktop Workstation & Sequencer)
![E-MU XL-7 Command Station](assets/screenshots/emu_xl7.png)

### E-MU XK-6 (61-Key Dance Performance Keyboard)
![E-MU XK-6 Hardware Editor](assets/screenshots/emu_xk6.png)

### E-MU Virtuoso 2000 (128-Voice Virtual Orchestra Sound Module)
![E-MU Virtuoso 2000 Hardware Editor](assets/screenshots/emu_virtuoso_2000.png)

### E-MU Vintage Pro (128-Voice Vintage Workstation Rack)
![E-MU Vintage Pro Hardware Editor](assets/screenshots/emu_vintage_pro.png)

### E-MU Vintage Keys (Classic 1993 1U Rack Sound Module)
![E-MU Vintage Keys Hardware Editor](assets/screenshots/emu_vintage_keys.png)

### E-MU Proteus 1000 (64-Voice 1U Sound Module with White Controls)
![E-MU Proteus 1000 Hardware Editor](assets/screenshots/emu_proteus_1000.png)

### E-MU Proteus 2000 (128-Voice Flagship 1U Sound Module with Composer ROM)
![E-MU Proteus 2000 Hardware Editor](assets/screenshots/emu_proteus_2000.png)

### E-MU Proteus 2500 (128-Voice Command Station Console & Sequencer)
![E-MU Proteus 2500 Hardware Editor](assets/screenshots/emu_proteus_2500.png)

### E-MU Planet Phatt ("The Swing System" 1U Hip-Hop & R&B Sound Module)
![E-MU Planet Phatt Hardware Editor](assets/screenshots/emu_planet_phatt.png)

### E-MU Planet Earth (64-Voice World Expedition 1U Sound Module)
![E-MU Planet Earth Hardware Editor](assets/screenshots/emu_planet_earth.png)

### E-MU Orbit-3 (128-Voice Super Dance Module with Neon Yellow Chassis)
![E-MU Orbit-3 Hardware Editor](assets/screenshots/emu_orbit_3.png)

### E-MU Orbit 9090 (32-Voice 1996 Dance Planet with Golden Yellow Chassis)
![E-MU Orbit 9090 Hardware Editor](assets/screenshots/emu_orbit_9090.png)

### E-MU SP-1200 (12-Bit Linear Sampling Drum Machine & SSM2044 Filter)
![E-MU SP-1200 Hardware Editor](assets/screenshots/emu_sp_1200.png)

### Casio CZ-1 (Flagship 16-DCO Phase Distortion Synthesizer)
![Casio CZ-1 Hardware Editor](assets/screenshots/casio_cz_1.png)

### Casio CZ-1000 (8-Voice Phase Distortion Synthesizer with Membrane Keypad)
![Casio CZ-1000 Hardware Editor](assets/screenshots/casio_cz_1000.png)

### Casio CZ-101 (Portable Keytar Phase Distortion Synthesizer)
![Casio CZ-101 Hardware Editor](assets/screenshots/casio_cz_101.png)

### Casio CZ-230S (Phase Distortion Synthesizer & PCM Rhythm Workstation)
![Casio CZ-230S Hardware Editor](assets/screenshots/casio_cz_230s.png)

### Casio CZ-3000 (16-DCO Professional Phase Distortion Synthesizer)
![Casio CZ-3000 Hardware Editor](assets/screenshots/casio_cz_3000.png)

### Casio CZ-5000 (Flagship Workstation with 8-Track Sequencer)
![Casio CZ-5000 Hardware Editor](assets/screenshots/casio_cz_5000.png)

---

## Workspace Architecture

```
omnipatch/
├── crates/
│   ├── omnipatch-core/       # SysEx encoding, 7-bit checksums, throttling & timing
│   ├── omnipatch-profile/    # Recursive profile discovery & parameter validation
│   ├── omnipatch-midi/       # Cross-platform MIDI I/O via midir with virtual fallback
│   ├── omnipatch-librarian/  # Embedded SQLite patch database & indexing
│   └── omnipatch-cli/        # Command-line interface for device inspection & SysEx testing
├── devices/                  # Self-contained instrument packages: <manufacturer>/<model>/
│   ├── access/
│   │   └── virus-a/          # profile.yaml, factory_presets.json
│   ├── akai/
│   │   └── ax60/             # profile.yaml, factory_presets.json
│   ├── casio/
│   │   ├── cz-1/             # profile.yaml, factory_presets.json
│   │   ├── cz-1000/          # profile.yaml, factory_presets.json
│   │   ├── cz-101/           # profile.yaml, factory_presets.json
│   │   ├── cz-230s/          # profile.yaml, factory_presets.json
│   │   ├── cz-3000/          # profile.yaml, factory_presets.json
│   │   └── cz-5000/          # profile.yaml, factory_presets.json
│   └── emu/
│       ├── audity-2000/      # profile.yaml, factory_presets.json
│       ├── b-3/              # profile.yaml, factory_presets.json
│       ├── carnaval/         # profile.yaml, factory_presets.json
│       ├── emax/             # profile.yaml, factory_presets.json
│       ├── emax-ii/          # profile.yaml, factory_presets.json
│       ├── orbit-3/          # profile.yaml, factory_presets.json
│       ├── orbit-9090/       # profile.yaml, factory_presets.json
│       ├── planet-earth/     # profile.yaml, factory_presets.json
│       ├── planet-phatt/     # profile.yaml, factory_presets.json
│       ├── proteus-1000/     # profile.yaml, factory_presets.json
│       ├── proteus-2000/     # profile.yaml, factory_presets.json
│       ├── proteus-2500/     # profile.yaml, factory_presets.json
│       ├── sp-1200/          # profile.yaml, factory_presets.json
│       ├── vintage-keys/     # profile.yaml, factory_presets.json
│       ├── vintage-pro/      # profile.yaml, factory_presets.json
│       ├── virtuoso-2000/    # profile.yaml, factory_presets.json
│       ├── xk-6/             # profile.yaml, factory_presets.json
│       ├── xl-7/             # profile.yaml, factory_presets.json
│       └── xtreme-lead-1/    # profile.yaml, factory_presets.json
├── preview/                  # Interactive Metro UI prototype (open in browser)
└── tools/                    # Automated PDF manual ingestion tool (Python)
```

---

## Quick Start

### Build & Test

```bash
# Clone the repository
git clone https://github.com/dan2804/omnipatch.git
cd omnipatch

# Run all unit tests
cargo test

# Build release binaries
cargo build --release
```

### CLI Commands

```bash
# List all loaded synth profiles
./target/release/omnipatch devices list --dir devices/

# Inspect specific synth parameters
./target/release/omnipatch devices show "E-MU XL-7" --dir devices/

# Generate bit-perfect SysEx parameter edit
./target/release/omnipatch sysex param-edit "audity" "0x0144" 95
./target/release/omnipatch sysex param-edit "b3" "0x0180" 8
./target/release/omnipatch sysex param-edit "xl1" "0x0144" 80
./target/release/omnipatch sysex param-edit "xl7" "0x0180" 190
./target/release/omnipatch sysex param-edit "xk6" "0x0180" 82
./target/release/omnipatch sysex param-edit "virtuoso" "0x0180" 120
./target/release/omnipatch sysex param-edit "vintpro" "0x0180" 128
./target/release/omnipatch sysex param-edit "vintage keys" "16" 110

# Import all factory presets into local SQLite librarian (4,928 presets)
./target/release/omnipatch librarian import-presets --dir devices/ -b library.db

# Search patches by name or category
./target/release/omnipatch librarian search "Leg Str" -b library.db
./target/release/omnipatch librarian search "Vintage" -b library.db
./target/release/omnipatch librarian search "Hmnd B3" -b library.db
./target/release/omnipatch librarian search "Trancer" -b library.db
```

### Interactive UI & Hardware Previews

Open any of the following interactive prototypes in any modern web browser to test reactive controls, parameter editing, Web Audio sound playback, and real-time SysEx output:

| Synthesizer | Preview File | Highlights |
| :--- | :--- | :--- |
| **OmniPatch Studio Hub** | [`preview/index.html`](preview/index.html) | Windows 8 Metro UI live tile dashboard & rack router |
| **E-MU Proteus 1000** | [`preview/proteus_1000.html`](preview/proteus_1000.html) | 30th Anniversary blue trapezoid LCD, ivory controls, 32MB Composer ROM, Model ID `0x0F` |
| **E-MU Vintage Keys (1993)** | [`preview/vintage_keys.html`](preview/vintage_keys.html) | 1U matte steel, 11x5 cyan dot matrix, 2x16 LCD, 8 keyboard engines, Model ID `0x0B` |
| **E-MU Vintage Pro (2002)** | [`preview/vintage_pro.html`](preview/vintage_pro.html) | Two-tone pewter faceplate, 5 spun-aluminum knobs, 9 Midi Quest 13 editors, Model ID `0x11` |
| **E-MU Virtuoso 2000** | [`preview/virtuoso_2000.html`](preview/virtuoso_2000.html) | Silver 1U rack, unbroken continuous navy wave line, 4-layer orchestral engine, Model ID `0x0D` |
| **E-MU XK-6** | [`preview/xk6.html`](preview/xk6.html) | 61-key performance synthesizer, SuperBEATS groove engine, Model ID `0x0F` |
| **E-MU XL-7 Command Station** | [`preview/xl7.html`](preview/xl7.html) | Electric yellow tabletop console, 16 rubber pads, 16 knobs, 16-track sequencer |
| **E-MU Xtreme Lead-1** | [`preview/xl1.html`](preview/xl1.html) | Electric yellow 1U rack, 50 Z-Plane filters, techno/dance soundboard, Model ID `0x0F` |
| **E-MU Carnaval** | [`preview/carnaval.html`](preview/carnaval.html) | Latin & world percussion, interactive BEATS drum machine, Model ID `0x08` |
| **E-MU B-3** | [`preview/emu_b3.html`](preview/emu_b3.html) | Parchment faceplate, 9 Hammond drawbars, Leslie 122 rotary simulation, Model ID `0x0E` |
| **E-MU Audity 2000 (v2)** | [`preview/audity_2000.html`](preview/audity_2000.html) | Metallic light blue faceplate, 64-voice modular rack, 4 sub-editors, Model ID `0x0C` |
| **Access Virus A** | [`preview/virus_a.html`](preview/virus_a.html) | Red anodized chassis, wood side cheeks, DSP56303 virtual analog engine |
| **Akai AX60** | [`preview/ax60.html`](preview/ax60.html) | Curtis CEM3394 analog sliders, Tauntek CC mapping, sampler input routing |

---

## License

Open-source under MIT or Apache 2.0.
