# OmniPatch

**Universal Hardware Synthesizer Librarian, SysEx Automation Engine & Studio Control Hub**

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![Database](https://img.shields.io/badge/SQLite-FTS5%20Indexed-blue.svg)](https://www.sqlite.org/)
[![Profiles](https://img.shields.io/badge/Synthesizers-515%20Hardware%20Profiles-success.svg)](devices/)
[![Presets](https://img.shields.io/badge/Factory%20Presets-123%2C634%20Indexed-purple.svg)](omnipatch_library.db)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

OmniPatch is a high-performance synthesizer librarian and SysEx communication platform written in Rust. It bridges vintage analog, digital FM, wavetable, and modern flagship synthesizers into a unified, high-speed ecosystem with hardware-safe buffer throttling and instant full-text search across 123,000+ factory patches.

---

## Key Capabilities

* **Unified Local Librarian (`rusqlite` + FTS5):** Local SQLite engine indexing **123,634 authentic factory patches** across **515 synthesizers** and **1,928 banks**, delivering sub-millisecond full-text queries for names, categories, banks, and sound-engine tags.
* **Hardware-Safe SysEx Pacing:** Configurable inter-byte and inter-block millisecond throttling specifically engineered to prevent buffer overflows on vintage 8-bit and 16-bit UART microcontrollers (Motorola 68000, 6809, Intel 8031, etc.).
* **Declarative Hardware Profiles (`profile.yaml`):** Zero recompilation required to add or modify instruments. Each synthesizer is declaratively defined with MIDI CC maps, SysEx request/dump commands, architecture metadata, and authentic bank structures.
* **Universal Web Audio Auditioning:** Interactive soundboard tiles and auditioning engines supporting classic synthesis methods (analog subtractive, FM, wavetable, additive harmonics).
* **Cross-Platform Native CLI:** Instant hardware discovery, sound inspection, bank dumps, and librarian queries via `omnipatch-cli`.

---

## Manufacturer Coverage Matrix (515 Synthesizers · 123,634 Patches)

Instead of maintaining fragmented sysex tools, OmniPatch covers 73 legendary manufacturers within a single unified database:

| Manufacturer / Family | Models | Total Patches | Featured Flagships & Classics | Synthesis Architectures |
| :--- | :---: | :---: | :--- | :--- |
| **Roland** | 108 | 30,457 | Jupiter-X, JX-03, JV-90, P-55, Juno-X, Juno-DS, FA-06, Alpha Juno-2, E-660, JD-Xi, D-550, Jupiter-8 | ZEN-Core, ACB Boutique, Super JV, Linear Arithmetic, COSM Guitar Modeling, Analog DCO |
| **Korg** | 57 | 14,145 | N5, N5EX, N364, Kaossilator Pro, N1R, N264, i30, 01R/W, EX-8000, EX-800, DS-8, Kronos, Radias, M3, 01/W | AI2 Workstations with RPPR, Dynamic Phrase Synth, DWGS Wavetable, 4-Op FM, Electribe DSP |
| **Yamaha** | 56 | 11,133 | SPX90 II, S90, 03D, SPX1000, RX17, RY20, Reface CS/DX/YC, 01V, 02R, CS6R, EX7, DB50XG, DX9, VL70-m, DX7 | Symphonic Chorus DSP, Modular Synthesis Workstations, Digital Consoles, 6-Op/4-Op FM |
| **E-MU Systems** | 24 | 10,936 | Ultra Proteus, Classic Keys, XL-1, Proteus family, Orbit, Morpheus, Audity 2000, Planet Earth, SP-1200 | Z-Plane Filter Morphing (288 Filters), 12-Bit Analog VCF Sampler, 64/128-Voice Extreme Digital |
| **Sequential & DSI** | 23 | 5,326 | Tetra, Pro 3, Prophet Rev2, Prophet-10, Prophet T8, Prophet X, Prophet-5, Prophet-6, Prophet VS, OB-6 | Multi-Filter Paraphonic, 16-Voice DCO Poly, Curtis Discrete 4-Voice, Sample + Analog VCF |
| **Waldorf & PPG** | 14 | 5,304 | Rocket, 4-Pole, Waldorf Wave, Quantum/Iridium, Kyra, M, Microwave I/XT, Blofeld, Pulse 2, PPG Wave | Paraphonic Multi-Saw, 24dB Analog Filter Module, Wavetable, FPGA 128-Voice VA |
| **Alesis** | 14 | 3,958 | NanoSynth, NanoPiano, NanoBass, SR-18, Wedge, Andromeda A6, SR-16, Ion, Micron, Quadraverb | Stereo Sound Modules, 24-Bit Drums, Desktop Reverb Ambience, 16-Voice Analog |
| **Access Music** | 4 | 3,840 | Virus A, Virus B, Virus C, Virus TI / TI2 / Snow / Polar | Dual DSP Virtual Analog, Hypersaw, Wavetable, Formant/Grain Synthesis |
| **Moog Music** | 13 | 2,916 | Sirin, Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch, Grandmother | Taurus Analog Bass & Lead, Discrete 3-VCO Analog, 18-VCO Polyphonic, 24dB Ladder VCF |
| **Clavia Nord** | 5 | 2,747 | Nord Lead 1, Nord Lead 2/2X, Nord Lead 3, Nord Lead 4, Nord Rack | Virtual Analog Pioneers, Rotary LED Encoders, Subtractive & FM Modeling |
| **Eventide** | 5 | 2,200 | H3000 Ultra-Harmonizer, DSP4000, Eclipse, Space, TimeFactor, Rose | MicroPitch Shifting, Diatonic Harmonizer, Blackhole Reverb, Modular DSP |
| **Ensoniq** | 13 | 2,181 | DP PRO, SD-1, DP/4, DP/2, EPS-16 Plus, KS-32, KT-76, ASR-10, ESQ-1, SQ-80, VFX, TS-10 | Dual 24-Bit ESP Multi-Effects, 32-Voice Production Synth, Transwaves Sampling |
| **Boss / Roland FX** | 14 | 2,115 | SY-300, SY-1000, GP-10, SE-50, SE-70, SX-700, VF-1, GT-6, ME-10, ME-5, DR-550/660/770/880 | Polyphonic Guitar Synth (No Pickup), Dynamic Guitar Modeling, COSM, RSS 3D |
| **Novation** | 7 | 1,936 | Circuit, KS-Rack, Supernova II, Nova, Bass Station II, Peak / Summit, K-Station | Dual-Synth Grid Groovebox, Liquid Analog Modeling, Oxford FPGA, Vocoder |
| **Modal Electronics** | 6 | 1,856 | Modal 001, Cobalt5S, Modal 002, Argon8, Cobalt8, Skulpt / CraftSynth | High-Res NCO + Transistor Ladder VCF, 40 Extended Virtual Analog Algorithms |
| **Kawai** | 12 | 1,530 | R-100, Spectra, K5000S/R/W, K4 / K4r, K1 / K1r, K3 / K3m, K11, K5, XD-5 | 12-Bit Gritty Drum Patterns, 16-Bit Multi-Timbral, 128-Harmonic Additive Synthesis |
| **Oberheim** | 5 | 1,480 | Matrix-1000, Matrix-6, Matrix-12 / Xpander, OB-8, OB-X8 | 15-Mode State-Variable VCF, CEM3396 Matrix Modulation, Pure Discrete VCO |
| **Arturia** | 4 | 1,472 | PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2 / 2S | Analog Morphing, Steiner-Parker + Ladder VCFs, 16x16 Matrix, Mutable Algorithmic |
| **Behringer** | 2 | 1,424 | Deepmind 12 / 12D, PRO-800 | 12-Voice Analog DCO w/ Klark Teknik FX, 8-Voice Dual-VCO Analog Poly |
| **DigiTech** | 11 | 1,255 | Valve-FX, GSP-256, GSP-7, DSP-256, IPS-33B, Whammy 5, Vocalist, TSR-24S, Studio 400 | Vacuum Tube 12AX7 Preamp, 24-Bit Digital Multi-Effects, S-DISC Processing |
| **KiwiTechnics** | 5 | 1,056 | Kiwi-106, Kiwi-3P, Kiwi-Six, Kiwi-80, Patch Editor | Modern Hardware Engine Retrofits for Juno-106, JX-3P, Polysix, JX-8P |
| **Lexicon** | 7 | 1,006 | Reflex, LXP-5, PCM70, PCM80, PCM90, LXP-1, MPX-1 | Dynamic MIDI Reverberation, MicroPitch Shifting, Multi-Tap Delay |
| **ART** | 6 | 900 | DR-1, SGE, Multiverb Alpha, Multiverb III, SGX-2000 Express, DMV-Pro | 16-Bit Studio Digital Reverberation, Multi-Effects Guitar Preamp |
| **Quasimidi** | 4 | 867 | Rave-O-Lution 309, Sirius, Polymorph, Technox | Dance & Techno Groovebox, 7-Band Vocoder, 16-Step Modular Virtual Analog |
| **Kurzweil** | 3 | 800 | K2000, K2500, K2600 (Keyboard & Rack) | V.A.S.T. Variable Architecture Synthesis Technology, 31 DSP Algorithms, KDFX |
| **Elektron** | 4 | 768 | Digitakt, Digitone, Syntakt, Analog Four / Analog Rytm | Parameter Locks, 8-Voice FM Subtractive, Analog/Digital Drum Synthesis |
| **Akai Professional** | 9 | 756 | EWI4000S, EWI5000, AX80, VX600, AX73, S950, S1000, AX60, ME-80P | Electronic Wind Instruments, Studio MIDI Patchbay, 8-Voice CEM Analog |
| **Line 6** | 6 | 740 | POD Pro, Bass POD Pro, Echo Pro, Mod Pro, Filter Pro, POD XT Pro | Studio Rackmount Modeling (Tape Delay, Modulator, Mu-Tron Filter, Amp) |
| **TC Electronic** | 4 | 699 | G-Sharp, FireworX, D-Two, TC 2290 | Dual Engine Guitar Reverb/Delay, Modular Algorithmic Multi-Effects, Tap Delay |
| **Studio Electronics** | 3 | 652 | ATC-1, ATC-X, SE-1 | Tone Chamber Analog, Quad Discrete Filters (Moog/SEM/303/2600), 3-VCO Discrete |
| **Casio** | 9 | 616 | VZ-1 / VZ-10M, HT-6000, FZ-1 / FZ-10M, CZ-1, CZ-101, CZ-1000, CZ-3000, CZ-5000 | Interactive Phase Distortion (iPD), Spectrum Dynamic Analog VCF, 16-Bit Sampling |
| **Sony** | 5 | 598 | DPS-V55, DPS-V77, DPS-R7, DPS-D7, DPS-M7 | 4-Channel Spatial Multi-Effects, Dual-Engine High-Density Studio Reverbs |
| **Pioneer DJ / DSI** | 2 | 623 | Toraiz AS-1, Toraiz SP-16 | Prophet-6 Discrete Analog Filters & Voices, Professional Sampler/Step Sequencer |
| **JoMoX** | 3 | 478 | Airbase99, XBase 09, Alpha Base | Discrete Analog 909-Style Drum Synthesis, Analog VCF & VCA |
| **TC-Helicon** | 5 | 449 | VoiceDoubler, VoicePro, VoiceOne, VoiceLive, VoiceWorks | Multi-Voice Doubling & Emulation, 8-Voice Natural Pitch/Formant Modeling |
| **MFB** | 4 | 320 | Tanzbär, Tanzbär Lite, Synth Lite II, Dominion 1 | Discrete Analog Drum Computers, Digital Oscillators + 24dB Ladder VCF |
| **Dynacord** | 4 | 288 | DRP 15, DLS 223, TAM-19, CL-20 | High-Density Studio Reverb, Digital Rotary Simulation & Chorus |
| **Studiologic** | 1 | 256 | Sledge | Waldorf DSP Modeling Engine, Dual Wavetables, 24-Voice Polyphonic |
| **Futuresonus** | 1 | 128 | Parva | 8-Voice Polyphonic True Analog Synthesizer, Dual State-Variable Filters |
| **Red Sound Systems** | 2 | 128 | Dark Star, Dark Star XP2 | Dual-DSP Virtual Analog Modeling Synthesizers, Dedicated Joystick |
| **Roger Linn Design** | 1 | 100 | AdrenaLinn | Beat-Synced Filter Modulation, Flanging, Rotary & Drum Sequences |
| **Evolution** | 1 | 100 | EVS-1 | 16-Bit Multi-Algorithm FM, Additive, Ring Mod & Phase Distortion |
| **Octave-Plateau** | 1 | 100 | Voyetra-8 | 8-Voice Polyphonic Discrete CEM Analog Rack, Dual Discrete VCOs |
| **Marion Systems** | 1 | 100 | ProSynth | Tom Oberheim 8-Voice High-Resolution Analog Engine, Dual DCOs |
| **Zoom** | 2 | 199 | Zoom 9010, Zoom 9030 | Quad Discrete DSP Reverb & Delays, Advanced Guitar Multi-Effects |
| **Fender** | 1 | 50 | G-DEC | Digital Amp Modeling & Accompaniment Processor |
| **Hammond** | 1 | 32 | XB-2 | Direct Access Digital ToneWheel Organ, Drawbar Modeling |
| **Boutique & Cult Rarities** | 24 | 1,518 | Doctor A, Sawbench, OTO Biscuit, Meris, MeeBlip, 1010music, OSCar, etc. | 8-Bit Crushing, Multi-Voice Tracking, Micro-Wavetables, Hybrid Analog |

---

## Librarian Database & Instant FTS5 Search

OmniPatch stores all device definitions, memory banks, patch mappings, and SysEx dumps in an optimized local SQLite database (`omnipatch_library.db`).

### Direct SQLite / FTS5 Queries
Because patches are indexed in an **FTS5 full-text search table**, searching through 123,600+ presets takes under 2 milliseconds:

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
# List all 515 loaded hardware profiles
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
├── devices/                  # 365 Declarative YAML hardware profiles & factory preset dumps
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
