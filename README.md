# OmniPatch

**Universal Hardware Synthesizer Librarian, SysEx Automation Engine & Studio Control Hub**

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![Database](https://img.shields.io/badge/SQLite-FTS5%20Indexed-blue.svg)](https://www.sqlite.org/)
[![Profiles](https://img.shields.io/badge/Synthesizers-335%20Hardware%20Profiles-success.svg)](devices/)
[![Presets](https://img.shields.io/badge/Factory%20Presets-101%2C959%20Indexed-purple.svg)](omnipatch_library.db)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

OmniPatch is a high-performance synthesizer librarian and SysEx communication platform written in Rust. It bridges vintage analog, digital FM, wavetable, and modern flagship synthesizers into a unified, high-speed ecosystem with hardware-safe buffer throttling and instant full-text search across 100,000+ factory patches.

---

## Key Capabilities

* **Unified Local Librarian (`rusqlite` + FTS5):** Local SQLite engine indexing **101,959 authentic factory patches** across **335 synthesizers** and **1,697 banks**, delivering sub-millisecond full-text queries for names, categories, banks, and sound-engine tags.
* **Hardware-Safe SysEx Pacing:** Configurable inter-byte and inter-block millisecond throttling specifically engineered to prevent buffer overflows on vintage 8-bit and 16-bit UART microcontrollers (Motorola 68000, 6809, Intel 8031, etc.).
* **Declarative Hardware Profiles (`profile.yaml`):** Zero recompilation required to add or modify instruments. Each synthesizer is declaratively defined with MIDI CC maps, SysEx request/dump commands, architecture metadata, and authentic bank structures.
* **Universal Web Audio Auditioning:** Interactive soundboard tiles and auditioning engines supporting classic synthesis methods (analog subtractive, FM, wavetable, additive harmonics).
* **Cross-Platform Native CLI:** Instant hardware discovery, sound inspection, bank dumps, and librarian queries via `omnipatch-cli`.

---

## Manufacturer Coverage Matrix (335 Synthesizers · 101,959 Patches)

Instead of maintaining fragmented sysex tools, OmniPatch covers 48 legendary manufacturers within a single unified database:

| Manufacturer / Family | Models | Total Patches | Featured Flagships & Classics | Synthesis Architectures |
| :--- | :---: | :---: | :--- | :--- |
| **Roland** | 78 | 26,564 | SC-88 Pro/8850/8820, SD-35/50, XP-30/50, JV-1010/880/80, TB-303, TR-808/909, R-8, Jupiter-4/8, Juno-60/106, Integra-7 | Super JV, Sound Canvas GS, Discrete Analog, DCO, ACB, Linear Arithmetic, RS-PCM, Human Rhythm |
| **Korg** | 41 | 11,947 | Kronos/Nautilus, TR-Rack, X5D, X3, X2, 05R/W, NS5R, NX5R, X50, microX, T3, Radias, M3, 01/W, DSS-1, DW-6000, opsix | AI2 Workstations, Trinity ACCESS, MMT Multi-Modeling, HD-1 KARMA, NJM2069 Filter Sampler |
| **E-MU Systems** | 21 | 9,784 | Proteus family, Orbit/Orbit-3, Morpheus, Audity 2000, Planet Earth, SP-1200, Emax I/II, Vintage Keys | Z-Plane Filter Morphing (14-Pole), 12-Bit Analog VCF Sampler, 64/128-Voice Extreme Digital |
| **Yamaha** | 36 | 8,953 | Motif ES, Motif XF, MU100, MU128, MU1000, MU2000, MU80, MU50, CS2x, CS6x, CS-80, RY30, RX5, FS1R, DX1, DX7, VL1 | 128-Voice Studio XG (PLG Slots), Motif Mega Voice, AWM2 Rhythm Mod, Vector Synthesis, FM |
| **Waldorf & PPG** | 12 | 5,148 | Waldorf Wave, Quantum/Iridium, Kyra, M, Microwave I/XT, Blofeld, Pulse 2, PPG Wave 2.2/2.3 | Wavetable, Analog VCF, FPGA 128-Voice Virtual Analog, Resonator, Kernel FM |
| **Sequential & DSI** | 13 | 4,072 | Prophet-5, Prophet-6, Prophet VS, OB-6, Prophet 12, Trigon-6, Take 5, Evolver, Pro 2/3 | Discrete VCO/VCF, Vector Synthesis, SEM Filter, Curtis Analog DCO, Hybrid |
| **Access Music** | 4 | 3,840 | Virus A, Virus B, Virus C, Virus TI / TI2 / Snow / Polar | Dual DSP Virtual Analog, Hypersaw, Wavetable, Formant/Grain Synthesis |
| **Alesis** | 9 | 3,346 | Andromeda A6, SR-16, Ion, Micron, QS6/7/8/QSR, QuadraSynth, D4/DM5, HR-16, Quadraverb | 16-Voice Discrete Analog, 16-Bit Stereo Dynamic Drums, 17-Model Virtual Analog |
| **Moog Music** | 12 | 2,788 | Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch, Grandmother | Discrete 3-VCO Analog, 18-VCO Polyphonic, 24dB Ladder VCF, Semi-Modular |
| **Clavia Nord** | 5 | 2,747 | Nord Lead 1, Nord Lead 2/2X, Nord Lead 3, Nord Lead 4, Nord Rack | Virtual Analog Pioneers, Rotary LED Encoders, Subtractive & FM Modeling |
| **Eventide** | 5 | 2,200 | H3000 Ultra-Harmonizer, DSP4000, Eclipse, Space, TimeFactor, Rose | MicroPitch Shifting, Diatonic Harmonizer, Blackhole Reverb, Modular DSP |
| **Boss / Roland FX** | 11 | 1,647 | SE-50, SE-70, SX-700, VF-1, GT-6, ME-10, ME-5, DR-550, DR-660, DR-770, DR-880 | RSS 3D Spatial Audio, COSM Amp Modeling, Half-Rack Studio FX, Dr. Rhythm Drums |
| **Modal Electronics** | 4 | 1,628 | Modal 002, Argon8, Cobalt8, Skulpt / CraftSynth | 12-Voice Hybrid (NCO + Ladder), 32-Wavetable Morphing, 34-Algorithm VA |
| **Novation** | 5 | 1,608 | Supernova II, Nova, Bass Station II, Peak / Summit, K-Station | Oxford FPGA New-Oxford Oscillators, 42-Band Vocoder, Pure Analog Mono |
| **Oberheim** | 5 | 1,480 | Matrix-1000, Matrix-6, Matrix-12 / Xpander, OB-8, OB-X8 | 15-Mode State-Variable VCF, CEM3396 Matrix Modulation, Pure Discrete VCO |
| **Arturia** | 4 | 1,472 | PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2 / 2S | Analog Morphing, Steiner-Parker + Ladder VCFs, 16x16 Matrix, Mutable Algorithmic |
| **Ensoniq** | 7 | 1,453 | DP/4 / DP/4+, ASR-10, ESQ-1, SQ-80, VFX / VFX-SD, TS-10, MR Rack | 4-Unit Parallel Multi-Effects, Transwaves Sampling Recorder, CEM3379 Analog Filters |
| **Behringer** | 2 | 1,424 | Deepmind 12 / 12D, PRO-800 | 12-Voice Analog DCO w/ Klark Teknik FX, 8-Voice Dual-VCO Analog Poly |
| **Kawai** | 7 | 962 | K5000S/R/W, K3 / K3m, K11, K1, K4, K5, XD-5 | 128-Harmonic Additive Synthesis, SSM2044 Resonant Analog Filter, Formant Filter |
| **Lexicon** | 5 | 878 | PCM70, PCM80, PCM90, LXP-1/5, MPX-1 | Concert Hall, Rich Plate, Resonant Chords, Dual DSP Stereo Multi-Tap Delay |
| **Quasimidi** | 4 | 867 | Rave-O-Lution 309, Sirius, Polymorph, Technox | Dance & Techno Groovebox, 7-Band Vocoder, 16-Step Modular Virtual Analog |
| **Kurzweil** | 3 | 800 | K2000, K2500, K2600 (Keyboard & Rack) | V.A.S.T. Variable Architecture Synthesis Technology, 31 DSP Algorithms, KDFX |
| **Elektron** | 4 | 768 | Digitakt, Digitone, Syntakt, Analog Four / Analog Rytm | Parameter Locks, 8-Voice FM Subtractive, Analog/Digital Drum Synthesis |
| **Pioneer DJ / DSI** | 2 | 623 | Toraiz AS-1, Toraiz SP-16 | Prophet-6 Discrete Analog Filters & Voices, Professional Sampler/Step Sequencer |
| **Casio** | 9 | 616 | VZ-1 / VZ-10M, HT-6000, FZ-1 / FZ-10M, CZ-1, CZ-101, CZ-1000, CZ-3000, CZ-5000 | Interactive Phase Distortion (iPD), Spectrum Dynamic Analog VCF, 16-Bit Sampling |
| **Strymon** | 2 | 600 | BigSky, TimeLine | Cloud, Shimmer, Bloom, dTape, dBucket, Ice Multidimensional Studio DSP |
| **Akai Professional** | 6 | 492 | AX80, VX600, AX73, S950, S1000, AX60 | 8-Voice CEM Analog, SSM2044 Matrix Analog, 12-Bit Vintage Sampler, 16-Bit Stereo Sampler |
| **Boutique & Rares** | 16 | 2,746 | OSC OSCar, Cheetah MS6, UDO Super 6, Deckard's Dream, SunSyn, TC 2290, etc. | Additive Overdrive, Binaural Stereo Spread, CS-80 Analog Clone, Dynamic Delay |

---

## Librarian Database & Instant FTS5 Search

OmniPatch stores all device definitions, memory banks, patch mappings, and SysEx dumps in an optimized local SQLite database (`omnipatch_library.db`).

### Direct SQLite / FTS5 Queries
Because patches are indexed in an **FTS5 full-text search table**, searching through 101,950+ presets takes under 2 milliseconds:

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
# List all 335 loaded hardware profiles
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
├── devices/                  # 335 Declarative YAML hardware profiles & factory preset dumps
│   ├── access/               # Access Music (Virus A, B, C, TI, TI2, Indigo, Snow)
│   ├── akai/                 # Akai Professional (AX80, VX600, AX73, S950, S1000, AX60)
│   ├── alesis/               # Alesis (Andromeda A6, SR-16, Ion, Micron, QS Series, QuadraSynth, D4/DM5, HR-16)
│   ├── arturia/              # Arturia (PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2)
│   ├── asm/                  # Ashun Sound Machines (Hydrasynth Desktop, Deluxe, Explorer, Keyboard)
│   ├── behringer/            # Behringer (Deepmind 12, Deepmind 12D, PRO-800)
│   ├── black_corporation/    # Black Corporation (Deckard's Dream, Kijimi)
│   ├── boss/                 # Boss / Roland (SE-50, SE-70, SX-700, VF-1, GT-6, ME-10, ME-5, DR-550/660/770/880)
│   ├── casio/                # Casio (VZ-1, HT-6000, FZ-1, CZ-1, CZ-101, CZ-1000, CZ-230S, CZ-3000, CZ-5000)
│   ├── cheetah/              # Cheetah Marketing (MS6)
│   ├── clavia/               # Clavia Nord (Nord Lead 1, 2, 2X, 3, 4, Nord Rack)
│   ├── crumar/               # Crumar (Bit One, Bit 99, Bit 01)
│   ├── digitech/             # DigiTech (GSP 2101 Tube Preamp, Studio Quad / TSR-24)
│   ├── doepfer/              # Doepfer (MS-404, Dark Energy)
│   ├── dreadbox/             # Dreadbox (Typhon, Erebus)
│   ├── elektron/             # Elektron (Digitakt, Digitone, Syntakt, Analog Four / Rytm)
│   ├── emu/                  # E-MU Systems (Morpheus, Audity 2000, Orbit, Proteus, SP-1200, Emax, Vintage)
│   ├── ensoniq/              # Ensoniq (DP/4, ASR-10, ESQ-1, SQ-80, VFX, TS-10, MR Rack)
│   ├── eventide/             # Eventide (H3000, DSP4000, Eclipse, Space, TimeFactor, Rose)
│   ├── jomox/                # JoMoX (XBase 09, AirBase 99, SunSyn)
│   ├── kawai/                # Kawai (K3, K11, K5000 Additive, K1, K4, K5, XD-5)
│   ├── korg/                 # Korg (Radias, M3, 03R/W, 707, DSS-1, DW-6000, Poly-61, Kronos, opsix, wavestate, M1)
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
│   ├── roland/               # Roland (JD-08, JU-06A, JX-08, D-10, U-20, CM-32L, TB-303, TR-808, Jupiter-4/8, Juno-60/106)
│   ├── sequential/           # Sequential & DSI (Prophet-5, Prophet-6, OB-6, Trigon-6, Take 5, Evolver, P12, Mopho)
│   ├── siel/                 # Siel (Opera 6, DK600)
│   ├── strymon/              # Strymon (BigSky, TimeLine)
│   ├── studio_electronics/   # Studio Electronics (SE-1, SE-1X)
│   ├── tc_electronic/        # TC Electronic (2290 Dynamic Delay)
│   ├── udo_audio/            # UDO Audio (Super 6, Super Gemini)
│   ├── waldorf/              # Waldorf Music (Waldorf Wave, Quantum, Iridium, Kyra, M, Blofeld, Microwave, Pulse, Q)
│   └── yamaha/               # Yamaha (CS6x, SY85, TG33, FB-01, V50, CS-80, FS1R, DX1, DX5, SY99, EX5, VL1, Motif)
├── preview/                  # Web Audio interactive studio prototypes & hardware editors
│   ├── index.html            # Main Entry: Universal Windows 8 Metro UI Studio Hub
│   ├── metro_studio.html     # Universal Windows 8 Metro UI Studio (Collapsible Menus, Live Tiles)
│   └── *.html                # Dedicated hardware-specific vintage rackface editors
└── tools/                    # Database seeding and ingestion scripts (Python)
```

---

## License

OmniPatch is open source software licensed under the **MIT License**.
