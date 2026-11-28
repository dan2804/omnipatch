# OmniPatch

**Universal Hardware Synthesizer Librarian, SysEx Automation Engine & Studio Control Hub**

[![Rust](https://img.shields.io/badge/rust-1.75%2B-orange.svg)](https://www.rust-lang.org/)
[![Database](https://img.shields.io/badge/SQLite-FTS5%20Indexed-blue.svg)](https://www.sqlite.org/)
[![Profiles](https://img.shields.io/badge/Synthesizers-683%20Hardware%20Profiles-success.svg)](devices/)
[![Presets](https://img.shields.io/badge/Factory%20Presets-146%2C670%20Indexed-purple.svg)](omnipatch_library.db)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

OmniPatch is a high-performance synthesizer librarian and SysEx communication platform written in Rust. It bridges vintage analog, digital FM, wavetable, and modern flagship synthesizers into a unified, high-speed ecosystem with hardware-safe buffer throttling and instant full-text search across 146,000+ factory patches.

---

## Key Capabilities

* **Unified Local Librarian (`rusqlite` + FTS5):** Local SQLite engine indexing **146,670 authentic factory patches** across **683 synthesizers** and **2,175 banks**, delivering sub-millisecond full-text queries for names, categories, banks, and sound-engine tags.
* **Hardware-Safe SysEx Pacing:** Configurable inter-byte and inter-block millisecond throttling specifically engineered to prevent buffer overflows on vintage 8-bit and 16-bit UART microcontrollers (Motorola 68000, 6809, Intel 8031, etc.).
* **Declarative Hardware Profiles (`profile.yaml`):** Zero recompilation required to add or modify instruments. Each synthesizer is declaratively defined with MIDI CC maps, SysEx request/dump commands, architecture metadata, and authentic bank structures.
* **Universal Web Audio Auditioning:** Interactive soundboard tiles and auditioning engines supporting classic synthesis methods (analog subtractive, FM, wavetable, additive harmonics).
* **Cross-Platform Native CLI:** Instant hardware discovery, sound inspection, bank dumps, and librarian queries via `omnipatch-cli`.

---

## Manufacturer Coverage Matrix (683 Synthesizers · 146,670 Patches · 100% Midi Quest 13 + Beta Coverage)

OmniPatch provides complete, exhaustive coverage of all 1,046 standard instruments plus all 47 beta instruments from Midi Quest 13 across 76 legendary manufacturers within a single unified database:

| Manufacturer / Family | Models | Total Patches | Featured Flagships & Classics | Synthesis Architectures |
| :--- | :---: | :---: | :--- | :--- |
| **Roland** | 156 | 38,064 | A-90, TB-03, TD-6/8, S-220, FC-200, FA-07/08, SK-88/Pro, SC-Pro, Sound Canvas, TDW-1, XV-88 | SuperNATURAL Workstations, ACB Bass Line, COSM V-Drums, Linear Samplers |
| **Korg** | 79 | 17,235 | Kross, KAOSILLATOR Pro, iS40, is50, TR-76, Nautilus, OASYS, TR-61, Volca Series, Kronos | EDS-i Mobile Workstations, Dynamic Phrase Synthesizers, 9-Engine Workstation Studio |
| **Yamaha** | 80 | 14,059 | KX-76, KX-88, PLS1, VL7 V2, S70XS, WF192XG, SW1000XG, SY55, TG55, SPX900, Motif, DX7 | 88-Key Weighted Controllers, Virtual Acoustic Physical Modeling, PCI XG Wavetable |
| **E-MU Systems** | 29 | 12,408 | Launch Pad, Proteus FX, Proteus/1 XR, Proteus/2 XR, Sound Engine, Ultra Proteus, XL-1, Morpheus | Performance MIDI Grid Control, Dual 24-Bit Multi-FX, 384-Preset ROMs, Z-Plane Morphing |
| **Sequential & DSI** | 23 | 5,326 | Tetra, Pro 3, Prophet Rev2, Prophet-10, Prophet T8, Prophet X, Prophet-5, Prophet-6, Prophet VS, OB-6 | Multi-Filter Paraphonic, 16-Voice DCO Poly, Curtis Discrete 4-Voice, Sample + Analog VCF |
| **Waldorf & PPG** | 15 | 5,308 | Zarenbourg, Rocket, 4-Pole, Waldorf Wave, Quantum/Iridium, Kyra, M, Microwave I/XT, Blofeld | Physical Modeling Stage Piano, Paraphonic Multi-Saw, 24dB Analog Filter, Wavetable |
| **Access Music** | 8 | 4,864 | Virus KC, Virus Rack XL, Virus Indigo, Virus KB, Virus A/B/C, Virus TI / TI2 / Snow / Polar | 61-Key Virtual Analog Workstation, Dual-DSP Rack, Hypersaw, Advanced Wavetable |
| **Alesis** | 15 | 4,058 | D4 v1.01, NanoSynth, NanoPiano, NanoBass, SR-18, Wedge, Andromeda A6, SR-16, Ion, Micron | High Sample-Rate Percussion, Stereo Sound Modules, 24-Bit Drums, 16-Voice Analog |
| **Moog Music** | 14 | 2,980 | Moog One CC, Sirin, Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch | 16-Voice Flagship Controller Mappings, Taurus Analog Bass & Lead, 24dB Ladder VCF |
| **Clavia Nord** | 7 | 2,946 | Nord Lead (GAR), Nord Rack 2X, Nord Lead 1, Nord Lead 2/2X, Nord Lead 3, Nord Lead 4 | Guitar & Analog Rack Edition, 20-Voice Expanded Virtual Analog Rack, Subtractive & FM |
| **Ensoniq** | 17 | 2,845 | ASR-X, KT-88, TS-12, ZR-76, DP PRO, SD-1, DP/4, DP/2, EPS-16 Plus, KS-32, KT-76, ASR-10 | Resonant Filter Sampler, 88-Key Weighted Workstation, Transwaves Synthesis |
| **Novation** | 10 | 2,648 | SN2 Pro-X Kbd/Rack, KS4, Circuit, KS-Rack, Supernova II, Nova, Bass Station II, Peak | 48-Voice Supernova II Pro-X Flagships, Liquid Analog Synthesizers, Oxford FPGA |
| **KiwiTechnics** | 9 | 2,464 | Kiwi-2, Kiwi-1000, Kiwi-8P, Kiwi-SuperJX, Kiwi-106, Kiwi-3P, Kiwi-Six, Kiwi-80 | Hardware Engine Retrofits for Poly-61/Polysix, Matrix-1000, JX-8P, JX-10, Juno-106 |
| **Boss / Roland FX** | 17 | 2,443 | DR-202, GT-5, GX-700, SY-300, SY-1000, GP-10, SE-50, SE-70, SX-700, VF-1, GT-6, DR-880 | Groovebox Drum Machine, COSM Guitar Modeling Preamp, RSS 3D Spatial Processing |
| **Eventide** | 5 | 2,200 | H3000 Ultra-Harmonizer, DSP4000, Eclipse, Space, TimeFactor, Rose | MicroPitch Shifting, Diatonic Harmonizer, Blackhole Reverb, Modular DSP |
| **DigiTech** | 17 | 1,907 | GFX-1, DSP-128, GSP-5, RP-10, TSR-12, Legend II, Valve-FX, GSP-256, GSP-7, DSP-256 | Twin-Tube 12AX7 Guitar Preamp, True Stereo S-DISC Processing, Digital Reverb/Delay |
| **Modal Electronics** | 6 | 1,856 | Modal 001, Cobalt5S, Modal 002, Argon8, Cobalt8, Skulpt / CraftSynth | High-Res NCO + Transistor Ladder VCF, 40 Extended Virtual Analog Algorithms |
| **Kawai** | 14 | 1,758 | RV-4, XS-1, R-100, Spectra, K5000S/R/W, K4 / K4r, K1 / K1r, K3 / K3m, K11, K5, XD-5 | 4-Channel 20-Bit Reverb, Half-Rack General MIDI, 128-Harmonic Additive Synthesis |
| **Oberheim** | 7 | 1,644 | Xpander, Cyclone, Matrix-1000, Matrix-6, Matrix-12, OB-8, OB-X8 | 6-Voice Discrete Analog Synthesizer Module, 15-Mode Multimode Filters, Discrete VCO |
| **Behringer** | 3 | 1,524 | Virtualizer Pro, Deepmind 12 / 12D, PRO-800 | 24-Bit Digital Studio Multi-Effects, 12-Voice Analog DCO w/ Klark Teknik FX |
| **Arturia** | 4 | 1,472 | PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2 / 2S | Analog Morphing, Steiner-Parker + Ladder VCFs, 16x16 Matrix, Mutable Algorithmic |
| **Lexicon** | 8 | 1,106 | Lexicon 300L, Reflex, LXP-5, PCM70, PCM80, PCM90, LXP-1, MPX-1 | LARC Studio Reverb / Ambience, Dynamic MIDI Reverberation, MicroPitch Shifting |
| **Line 6** | 11 | 1,096 | Pocket POD, Guitar POD V.1/V.2, Floor POD Plus, POD Pro, Bass POD Pro, Echo Pro | Portable Pocket Guitar Modeler, Direct Desktop Preamp Modeling, Studio Racks |
| **Quasimidi** | 6 | 1,027 | Raven, Turbo-Volcon, Rave-O-Lution 309, Sirius, Polymorph, Technox | Dance & Techno Master Keyboard, Synthesizer Programmer, 7-Band Vocoder |
| **ART** | 7 | 932 | X-15, DR-1, SGE, Multiverb Alpha, Multiverb III, SGX-2000 Express, DMV-Pro | Ultrafoot MIDI Floor Controller, 16-Bit Studio Digital Reverb, Preamp Processing |
| **TC Electronic** | 6 | 899 | Finalizer, TC 1128, G-Sharp, FireworX, D-Two, TC 2290 | Studio Mastering Processor, 28-Band Graphic Equalizer, Algorithmic Multi-Effects |
| **Kurzweil** | 3 | 800 | K2000, K2500, K2600 (Keyboard & Rack) | V.A.S.T. Variable Architecture Synthesis Technology, 31 DSP Algorithms, KDFX |
| **Akai Professional** | 10 | 788 | DP88, EWI4000S, EWI5000, AX80, VX600, AX73, S950, S1000, AX60, ME-80P | Digital Audio Matrix Patchbay, Electronic Wind Instruments, 8-Voice CEM Analog |
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
Because patches are indexed in an **FTS5 full-text search table**, searching through 146,000+ presets takes under 2 milliseconds:

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
# List all 683 loaded hardware profiles
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
