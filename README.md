# OmniPatch

**Universal Hardware Synthesizer Librarian, SysEx Automation Engine & Studio Control Hub**

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![Database](https://img.shields.io/badge/SQLite-FTS5%20Indexed-blue.svg)](https://www.sqlite.org/)
[![Profiles](https://img.shields.io/badge/Synthesizers-243%20Hardware%20Profiles-success.svg)](devices/)
[![Presets](https://img.shields.io/badge/Factory%20Presets-84%2C024%20Indexed-purple.svg)](omnipatch_library.db)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

OmniPatch is a high-performance synthesizer librarian and SysEx communication platform written in Rust. It bridges vintage analog, digital FM, wavetable, and modern flagship synthesizers into a unified, high-speed ecosystem with hardware-safe buffer throttling and instant full-text search across 84,000+ factory patches.

---

## Key Capabilities

* **Unified Local Librarian (`rusqlite` + FTS5):** Local SQLite engine indexing **84,024 authentic factory patches** across **243 synthesizers** and **1,504 banks**, delivering sub-millisecond full-text queries for names, categories, banks, and sound-engine tags.
* **Hardware-Safe SysEx Pacing:** Configurable inter-byte and inter-block millisecond throttling specifically engineered to prevent buffer overflows on vintage 8-bit and 16-bit UART microcontrollers (Motorola 68000, 6809, Intel 8031, etc.).
* **Declarative Hardware Profiles (`profile.yaml`):** Zero recompilation required to add or modify instruments. Each synthesizer is declaratively defined with MIDI CC maps, SysEx request/dump commands, architecture metadata, and authentic bank structures.
* **Universal Web Audio Auditioning:** Interactive soundboard tiles and auditioning engines supporting classic synthesis methods (analog subtractive, FM, wavetable, additive harmonics).
* **Cross-Platform Native CLI:** Instant hardware discovery, sound inspection, bank dumps, and librarian queries via `omnipatch-cli`.

---

## Manufacturer Coverage Matrix (243 Synthesizers · 84,024 Patches)

Instead of maintaining fragmented sysex tools, OmniPatch covers 45 legendary manufacturers within a single unified database:

| Manufacturer / Family | Models | Total Patches | Featured Flagships & Classics | Synthesis Architectures |
| :--- | :---: | :---: | :--- | :--- |
| **Roland** | 51 | 21,782 | TB-303, TR-808/909, Jupiter-4/8, Juno-60/106, JV-1080/2080, JD-800/990, Integra-7, System-8 | Discrete Analog, DCO, ACB, Linear Arithmetic, Super JV, SuperNATURAL |
| **E-MU Systems** | 19 | 9,016 | Proteus 1000/2000/2500, Orbit-3, Planet Earth, SP-1200, Emax I/II, Audity 2000, Vintage Keys | Z-Plane Filter Morphing, 12-Bit Analog VCF Sampler, 128-Voice Rompler |
| **Korg** | 23 | 7,926 | Kronos/Nautilus, M1, Wavestation, Triton, MS2000, minilogue xd, opsix, wavestate, Mono/Poly | 9-Engine Workstation, Wave Sequencing 2.0, Altered FM, Analog Multi-Engine |
| **Waldorf & PPG** | 13 | 5,404 | Waldorf Wave, Quantum/Iridium, Kyra, M, Microwave I/XT, Blofeld, Pulse 2, PPG Wave 2.2/2.3 | Wavetable, Analog VCF, FPGA 128-Voice Virtual Analog, Resonator, Kernel FM |
| **Sequential & DSI** | 13 | 4,072 | Prophet-5, Prophet-6, Prophet VS, OB-6, Prophet 12, Trigon-6, Take 5, Evolver, Pro 2/3 | Discrete VCO/VCF, Vector Synthesis, SEM Filter, Curtis Analog DCO, Hybrid |
| **Yamaha** | 18 | 3,954 | CS-80, FS1R, DX1, DX5, DX7/DX7II, TX81Z, SY99, EX5, VL1 Physical Modeling, Motif | 8-Op Formant FM, 6-Op FM, RCM Hybrid (AFM+AWM2), Virtual Acoustic, Dual VCO Analog |
| **Access Music** | 4 | 3,840 | Virus A, Virus B, Virus C, Virus TI / TI2 / Snow / Polar | Dual DSP Virtual Analog, Hypersaw, Wavetable, Formant/Grain Synthesis |
| **Alesis** | 8 | 3,246 | Andromeda A6, Ion, Micron, QS6/7/8/QSR, QuadraSynth, D4/DM5, HR-16, Quadraverb | 16-Voice Discrete Analog, 17-Model Virtual Analog, 64-Voice 16-Bit PCM |
| **Moog Music** | 16 | 3,028 | Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch, Grandmother | Discrete 3-VCO Analog, 18-VCO Polyphonic, 24dB Ladder VCF, Semi-Modular |
| **Clavia Nord** | 5 | 2,747 | Nord Lead 1, Nord Lead 2/2X, Nord Lead 3, Nord Lead 4, Nord Rack | Virtual Analog Pioneers, Rotary LED Encoders, Subtractive & FM Modeling |
| **Eventide** | 6 | 2,300 | H3000 Ultra-Harmonizer, DSP4000, Eclipse, Space, TimeFactor, Rose | MicroPitch Shifting, Diatonic Harmonizer, Blackhole Reverb, Modular DSP |
| **Modal Electronics** | 4 | 1,628 | Modal 002, Argon8, Cobalt8, Skulpt / CraftSynth | 12-Voice Hybrid (NCO + Ladder), 32-Wavetable Morphing, 34-Algorithm VA |
| **Novation** | 5 | 1,608 | Supernova II, Nova, Bass Station II, Peak / Summit, K-Station | Oxford FPGA New-Oxford Oscillators, 42-Band Vocoder, Pure Analog Mono |
| **Oberheim** | 5 | 1,480 | Matrix-1000, Matrix-6, Matrix-12 / Xpander, OB-8, OB-X8 | 15-Mode State-Variable VCF, CEM3396 Matrix Modulation, Pure Discrete VCO |
| **Arturia** | 4 | 1,472 | PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2 / 2S | Analog Morphing, Steiner-Parker + Ladder VCFs, 16x16 Matrix, Mutable Algorithmic |
| **Behringer** | 2 | 1,424 | Deepmind 12 / 12D, PRO-800 | 12-Voice Analog DCO w/ Klark Teknik FX, 8-Voice Dual-VCO Analog Poly |
| **Ensoniq** | 5 | 953 | ESQ-1, SQ-80, VFX / VFX-SD, TS-10, MR Rack | Curtis CEM3379 Analog Filter, Transwaves, Hyper-Wave Sequencing |
| **Lexicon** | 5 | 878 | PCM70, PCM80, PCM90, LXP-1/5, MPX-1 | Concert Hall, Rich Plate, Resonant Chords, Dual DSP Stereo Multi-Tap Delay |
| **Quasimidi** | 4 | 867 | Rave-O-Lution 309, Sirius, Polymorph, Technox | Dance & Techno Groovebox, 7-Band Vocoder, 16-Step Modular Virtual Analog |
| **Kurzweil** | 3 | 800 | K2000, K2500, K2600 (Keyboard & Rack) | V.A.S.T. Variable Architecture Synthesis Technology, 31 DSP Algorithms, KDFX |
| **Elektron** | 4 | 768 | Digitakt, Digitone, Syntakt, Analog Four / Analog Rytm | Parameter Locks, 8-Voice FM Subtractive, Analog/Digital Drum Synthesis |
| **Kawai** | 5 | 720 | K5000S/R/W, K1, K4, K5, XD-5 | 128-Harmonic Additive Synthesis, Formant Filter (128 Bands), VM Vector |
| **Pioneer DJ / DSI** | 2 | 623 | Toraiz AS-1, Toraiz SP-16 | Prophet-6 Discrete Analog Filters & Voices, Professional Sampler/Step Sequencer |
| **Strymon** | 2 | 600 | BigSky, TimeLine | Cloud, Shimmer, Bloom, dTape, dBucket, Ice Multidimensional Studio DSP |
| **Boutique & Rares** | 16 | 2,746 | OSC OSCar, Cheetah MS6, UDO Super 6, Deckard's Dream, SunSyn, TC 2290, etc. | Additive Overdrive, Binaural Stereo Spread, CS-80 Analog Clone, Dynamic Delay |

---

## Librarian Database & Instant FTS5 Search

OmniPatch stores all device definitions, memory banks, patch mappings, and SysEx dumps in an optimized local SQLite database (`omnipatch_library.db`).

### Direct SQLite / FTS5 Queries
Because patches are indexed in an **FTS5 full-text search table**, searching through 84,020+ presets takes under 2 milliseconds:

```bash
# Search for Vangelis / Blade Runner CS-80 presets
sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"Blade Runner\"' LIMIT 5;
"

# Search for classic Steve Vai Eventide MicroPitch algorithms
sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"MicroPitch\"' LIMIT 5;
"

# Search across all 303, acid, and bassline presets
sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"TB-303\" OR \"Acid\"' LIMIT 10;
"
```

---

## Quick Start & CLI Usage

### 1. Build Native Rust CLI
```bash
cargo build --release
```

### 2. Inspect Devices & Parameters
```bash
# List all 243 loaded hardware profiles
./target/release/omnipatch devices list --dir devices/

# Inspect parameters and MIDI CC mapping for a specific synth
./target/release/omnipatch devices show "Sequential Circuits Prophet-5" --dir devices/
./target/release/omnipatch devices show "Roland TB-303 Bass Line" --dir devices/
./target/release/omnipatch devices show "Waldorf Blofeld" --dir devices/
```

### 3. Re-seed or Update Librarian Database
Whenever new profiles or preset dumps are added to `devices/`:
```bash
python3 tools/seed_librarian_db.py
```

---

## Workspace Architecture

```
omnipatch/
├── crates/                   # High-performance modular Rust crates
│   ├── omnipatch-cli/        # CLI binary commands, SysEx testing, database utilities
│   ├── omnipatch-core/       # Core types, error handling, parameter schemas
│   ├── omnipatch-librarian/  # SQLite local database storage, FTS5 search engine
│   ├── omnipatch-midi/       # midir low-latency packet pacing, hardware throttling
│   ├── omnipatch-profile/    # Declarative YAML parser, parameter mapping engine
│   └── omnipatch-sysex/      # Checksum calculators (Roland, E-MU, Casio, Waldorf)
├── devices/                  # 243 Declarative YAML hardware profiles & factory preset dumps
│   ├── access/               # Access Music (Virus A, B, C, TI, TI2, Indigo, Snow)
│   ├── akai/                 # Akai Professional (AX60)
│   ├── alesis/               # Alesis (Andromeda A6, Ion, Micron, QS Series, QuadraSynth, D4/DM5, HR-16)
│   ├── arturia/              # Arturia (PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2)
│   ├── asm/                  # Ashun Sound Machines (Hydrasynth Desktop, Deluxe, Explorer, Keyboard)
│   ├── behringer/            # Behringer (Deepmind 12, Deepmind 12D, PRO-800)
│   ├── black_corporation/    # Black Corporation (Deckard's Dream, Kijimi)
│   ├── casio/                # Casio Computer Co. (CZ-1, CZ-101, CZ-1000, CZ-230S, CZ-3000, CZ-5000)
│   ├── cheetah/              # Cheetah Marketing (MS6)
│   ├── clavia/               # Clavia Nord (Nord Lead 1, 2, 2X, 3, 4, Nord Rack)
│   ├── crumar/               # Crumar (Bit One, Bit 99, Bit 01)
│   ├── digitech/             # DigiTech (GSP 2101 Tube Preamp, Studio Quad / TSR-24)
│   ├── doepfer/              # Doepfer (MS-404, Dark Energy)
│   ├── dreadbox/             # Dreadbox (Typhon, Erebus)
│   ├── elektron/             # Elektron (Digitakt, Digitone, Syntakt, Analog Four / Rytm)
│   ├── emu/                  # E-MU Systems (Orbit-3, Proteus family, SP-1200, Emax, Vintage, etc.)
│   ├── ensoniq/              # Ensoniq (ESQ-1, SQ-80, VFX, TS-10, MR Rack)
│   ├── eventide/             # Eventide (H3000, DSP4000, Eclipse, Space, TimeFactor, Rose)
│   ├── jomox/                # JoMoX (XBase 09, AirBase 99, SunSyn)
│   ├── kawai/                # Kawai (K1, K4, K5, K5000 Additive Flagship, XD-5)
│   ├── korg/                 # Korg (Kronos, minilogue xd, prologue, opsix, wavestate, Mono/Poly, Polysix, M1, Triton)
│   ├── kurzweil/             # Kurzweil (K2000, K2500, K2600 V.A.S.T. Workstations)
│   ├── lexicon/              # Lexicon (PCM70, PCM80, PCM90, LXP-1/5, MPX-1)
│   ├── mfb/                  # MFB (Dominion 1)
│   ├── modal/                # Modal Electronics (Argon8, Cobalt8, Skulpt, Modal 002)
│   ├── moog/                 # Moog Music (Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch)
│   ├── novation/             # Novation (Bass Station II, Supernova II, Nova, K-Station, Peak)
│   ├── oberheim/             # Oberheim (Matrix-1000, Matrix-6, Matrix-12/Xpander, OB-8, OB-X8)
│   ├── oscar/                # Oxford Synthesiser Company (OSCar)
│   ├── peavey/               # Peavey (DPM 3, Spectrum Series)
│   ├── pioneer_dj/           # Pioneer DJ / Dave Smith (Toraiz AS-1, Toraiz SP-16)
│   ├── ppg/                  # PPG (PPG Wave 2.2 / 2.3)
│   ├── quasimidi/            # Quasimidi (Rave-O-Lution 309, Sirius, Polymorph, Technox)
│   ├── roland/               # Roland Corporation (TB-303, TR-808, TR-909, Jupiter-4/8, Juno-60/106, JV, JD, Integra-7)
│   ├── sequential/           # Sequential & DSI (Prophet-5, Prophet-6, OB-6, Trigon-6, Take 5, Evolver, P12, Mopho)
│   ├── siel/                 # Siel (Opera 6, DK600)
│   ├── strymon/              # Strymon (BigSky, TimeLine)
│   ├── studio_electronics/   # Studio Electronics (SE-1, SE-1X)
│   ├── tc_electronic/        # TC Electronic (2290 Dynamic Delay)
│   ├── udo_audio/            # UDO Audio (Super 6, Super Gemini)
│   ├── waldorf/              # Waldorf Music (Waldorf Wave, Quantum, Iridium, Kyra, M, Blofeld, Microwave, Pulse, Q)
│   └── yamaha/               # Yamaha Corporation (CS-80, FS1R, DX1, DX5, SY99, EX5, VL1, DX7, DX7II, TX81Z, Motif)
├── preview/                  # Web Audio interactive studio prototypes & hardware editors
│   ├── index.html            # Main Entry: Universal Windows 8 Metro UI Studio Hub
│   ├── metro_studio.html     # Universal Windows 8 Metro UI Studio (Collapsible Menus, Live Tiles)
│   └── *.html                # Dedicated hardware-specific vintage rackface editors
└── tools/                    # Database seeding and ingestion scripts (Python)
```

---

## License

OmniPatch is open source software licensed under the **MIT License**.
