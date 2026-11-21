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
| **E-MU Xtreme Lead-1** | 64-Voice Dance & Techno Synth | 14 | 512 | Electric yellow chassis, black knobs & buttons, 50 Z-Plane filters, 16-track SuperBEATS |
| **E-MU XL-7** | 128-Voice Desktop Workstation | 18 | 512 | Electric yellow console, 16 black rubber pads, 16 black knobs, 16-track sequencer (384 PPQN) |
| **E-MU XK-6** | 61-Key Dance Performance Keyboard | 10 | 512 | Grey chassis with electric yellow control section, black buttons/knobs, 61 synth-action keys, SuperBEATS |
| **E-MU Virtuoso 2000** | 128-Voice Virtual Orchestra | 10 | 512 | Light silver-grey 1U faceplate, black buttons, 64MB Orchestral Sessions Vol 1 & 2 ROMs, 50 Z-Plane filters |
| **E-MU Vintage Pro** | 128-Voice Vintage Workstation | 10 | 512 | Two-tone Rhodes faceplate (satin black top / brushed grey bottom), fluted knobs, Rhodes/Moog/Prophet |
| **E-MU Vintage Keys** | 32-Voice Vintage Keyboard Module | 10 | 512 | Matte black 1990s 1U chassis, green E-mu logo, retro 2x16 green LCD, classic SysEx ID 0x04 |

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

### E-MU Planet Phatt (64-Voice Hip-Hop / R&B Sound Module with Neon Pink Chassis)
![E-MU Planet Phatt Hardware Editor](assets/screenshots/emu_planet_phatt.png)

### E-MU Planet Earth (64-Voice World Expedition Sound Module with Teal Chassis)
![E-MU Planet Earth Hardware Editor](assets/screenshots/emu_planet_earth.png)

### E-MU Orbit-3 (128-Voice Super Dance Module with Neon Yellow Chassis)
![E-MU Orbit-3 Hardware Editor](assets/screenshots/emu_orbit_3.png)

### E-MU Orbit 9090 (32-Voice 1996 Dance Planet with Golden Yellow Chassis)
![E-MU Orbit 9090 Hardware Editor](assets/screenshots/emu_orbit_9090.png)

### E-MU SP-1200 (12-Bit Linear Sampling Drum Machine & SSM2044 Filter)
![E-MU SP-1200 Hardware Editor](assets/screenshots/emu_sp_1200.png)

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

### Interactive UI Preview

Open `preview/index.html` in any modern web browser to interact with the **Windows 8 Metro UI Studio Hub** and authentic hardware panels for Access Virus A, Akai AX60, E-MU Audity 2000, E-MU B-3, E-MU Carnaval, E-MU Emax, E-MU Emax II, E-MU Xtreme Lead-1, E-MU XL-7 Command Station, E-MU XK-6 Performance Keyboard, E-MU Virtuoso 2000, E-MU Vintage Pro, and E-MU Vintage Keys!

---

## License

Open-source under MIT or Apache 2.0.
