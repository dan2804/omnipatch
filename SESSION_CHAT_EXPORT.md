# OmniPatch: Comprehensive Session Export & Engineering Handover
**Date / Timestamp:** 2026-11-28T11:20:00Z  
**Repository:** [https://github.com/dan2804/omnipatch](https://github.com/dan2804/omnipatch)  
**Branch:** `main`  
**Context:** Universal Hardware Synthesizer Librarian, SysEx Automation Engine, High-Speed SQLite FTS5 Database & Studio Control Hub.

---

## 1. Executive Summary & Current System Scale

OmniPatch is a high-performance synthesizer librarian and SysEx communication platform engineered in Rust, Python, and SQLite. It bridges vintage analog, digital FM, wavetable, physical modeling, and modern flagship synthesizers into a unified ecosystem with hardware-safe buffer throttling and instant full-text search.

### Current Database Metrics
* **Total Supported Synthesizers & Sound Modules:** **585 Hardware Profiles** (in `devices/<manufacturer>/<model>/`)
* **Total Memory Banks:** **2,051 Distinct Banks**
* **Total Factory Presets Indexed:** **135,697 Authentic Patches** in SQLite (`omnipatch_library.db`) with sub-millisecond FTS5 search
* **Total Manufacturers Represented:** **73 Legendary Brands**
* **Midi Quest 13 Ingestion Progress:** Ingested 585 instruments out of the 1,046 catalog; **85 items remaining** (predominantly keybed/rack mirrors and hardware retrofit interfaces).
* **Git Synchronization:** Ready to commit & push to `origin/main`.
* **Inboxes:** [`resources/manuals/`](file:///home/daniel/Projects/omnipatch/resources/manuals/) and [`resources/sysex_dumps/`](file:///home/daniel/Projects/omnipatch/resources/sysex_dumps/) are completely cleared, with processed files archived in [`resources/processed/`](file:///home/daniel/Projects/omnipatch/resources/processed/).

---

## 2. Manufacturer Coverage Matrix (585 Models · 135,697 Patches · 73 Brands)

| Manufacturer / Family | Models | Total Patches | Featured Flagships & Classics | Synthesis Architectures |
| :--- | :---: | :---: | :--- | :--- |
| **Roland** | 131 | 35,337 | XV-88, XP-60, XP-10, RS-5/9, JV-1000, VK-7, TR-6S, S-550/770, V-Synth GT/XT, Jupiter-X, Jupiter-8 | Flagship 128-Voice Workstations, Virtual ToneWheel, ACB Rhythm, 24-Bit Linear Samplers |
| **Korg** | 71 | 15,901 | Nautilus, OASYS, TR-61, Volca Kick/Keys/Bass, SG-ProX, T1/T2, SDD-3300, Kronos, 01R/W | 9-Engine Synthesis Studio, Open Architecture, HI Workstations, MS-20 Resonator |
| **Yamaha** | 74 | 13,451 | SW1000XG, SY55, TG55, TG100/300, YS100/200, SPX900, P-100, TG77, TX816, Motif, DX7 | PCI Hardware XG, 4-Op Easy FM, Symphonic 32-Bit Multi-Effects, AFM + AWM2 |
| **E-MU Systems** | 28 | 12,344 | Proteus FX, Proteus/1 XR, Proteus/2 XR, Sound Engine, Ultra Proteus, XL-1, Morpheus, SP-1200 | Dual 24-Bit Multi-FX, 384-Preset Expanded Pop & Orchestral ROMs, Z-Plane Morphing |
| **Sequential & DSI** | 23 | 5,326 | Tetra, Pro 3, Prophet Rev2, Prophet-10, Prophet T8, Prophet X, Prophet-5, Prophet-6, Prophet VS, OB-6 | Multi-Filter Paraphonic, 16-Voice DCO Poly, Curtis Discrete 4-Voice, Sample + Analog VCF |
| **Waldorf & PPG** | 14 | 5,304 | Rocket, 4-Pole, Waldorf Wave, Quantum/Iridium, Kyra, M, Microwave I/XT, Blofeld, Pulse 2, PPG Wave | Paraphonic Multi-Saw, 24dB Analog Filter Module, Wavetable, FPGA 128-Voice VA |
| **Access Music** | 6 | 4,352 | Virus Indigo, Virus KB, Virus A/B/C, Virus TI / TI2 / Snow / Polar | 37-Key Designer VA, Dual DSP Hypersaw, Advanced Wavetable, Formant Modeling |
| **Alesis** | 14 | 3,958 | NanoSynth, NanoPiano, NanoBass, SR-18, Wedge, Andromeda A6, SR-16, Ion, Micron, Quadraverb | Stereo Sound Modules, 24-Bit Drums, Desktop Reverb Ambience, 16-Voice Analog |
| **Moog Music** | 13 | 2,916 | Sirin, Moog One, Minimoog Model D, Memorymoog, Voyager, Sub 37, Matriarch, Grandmother | Taurus Analog Bass & Lead, Discrete 3-VCO Analog, 18-VCO Polyphonic, 24dB Ladder VCF |
| **Clavia Nord** | 6 | 2,847 | Nord Rack 2X, Nord Lead 1, Nord Lead 2/2X, Nord Lead 3, Nord Lead 4, Nord Rack | 20-Voice Expanded Virtual Analog Rack, Rotary LED Encoders, Subtractive & FM |
| **Ensoniq** | 16 | 2,717 | KT-88, TS-12, ZR-76, DP PRO, SD-1, DP/4, DP/2, EPS-16 Plus, KS-32, KT-76, ASR-10, ESQ-1 | 88-Key Weighted Workstation, Transwave Synthesizer, Dual 24-Bit ESP Multi-Effects |
| **Eventide** | 5 | 2,200 | H3000 Ultra-Harmonizer, DSP4000, Eclipse, Space, TimeFactor, Rose | MicroPitch Shifting, Diatonic Harmonizer, Blackhole Reverb, Modular DSP |
| **Boss / Roland FX** | 14 | 2,115 | SY-300, SY-1000, GP-10, SE-50, SE-70, SX-700, VF-1, GT-6, ME-10, ME-5, DR-550/660/770/880 | Polyphonic Guitar Synth (No Pickup), Dynamic Guitar Modeling, COSM, RSS 3D |
| **Novation** | 7 | 1,936 | Circuit, KS-Rack, Supernova II, Nova, Bass Station II, Peak / Summit, K-Station | Dual-Synth Grid Groovebox, Liquid Analog Modeling, Oxford FPGA, Vocoder |
| **Modal Electronics** | 6 | 1,856 | Modal 001, Cobalt5S, Modal 002, Argon8, Cobalt8, Skulpt / CraftSynth | High-Res NCO + Transistor Ladder VCF, 40 Extended Virtual Analog Algorithms |
| **DigiTech** | 16 | 1,808 | DSP-128, GSP-5, RP-10, TSR-12, Legend II, Valve-FX, GSP-256, GSP-7, DSP-256, IPS-33B | Stereo Digital Reverb/Delay, Guitar Multi-Effects Floor Control, Vacuum Tube 12AX7 |
| **Kawai** | 12 | 1,530 | R-100, Spectra, K5000S/R/W, K4 / K4r, K1 / K1r, K3 / K3m, K11, K5, XD-5 | 12-Bit Gritty Drum Patterns, 16-Bit Multi-Timbral, 128-Harmonic Additive Synthesis |
| **Oberheim** | 5 | 1,480 | Matrix-1000, Matrix-6, Matrix-12 / Xpander, OB-8, OB-X8 | 15-Mode State-Variable VCF, CEM3396 Matrix Modulation, Pure Discrete VCO |
| **Arturia** | 4 | 1,472 | PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2 / 2S | Analog Morphing, Steiner-Parker + Ladder VCFs, 16x16 Matrix, Mutable Algorithmic |
| **Behringer** | 2 | 1,424 | Deepmind 12 / 12D, PRO-800 | 12-Voice Analog DCO w/ Klark Teknik FX, 8-Voice Dual-VCO Analog Poly |
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

## 3. History of Ingestion Waves (1 through 22)

1. **Waves 1..10:** Foundational architecture, Rust core CLI, Web Audio auditioning soundboard, initial Roland, Moog, Sequential, E-MU, Waldorf, Korg, Yamaha, Access, Alesis, and Clavia profiles.
2. **Wave 11:** Massive catalog expansion across 243 devices, bringing indexed presets to 84,024.
3. **Wave 12 (Vintage Samplers, Vector Synths & Digital Classics):** Casio VZ-1/HT-6000/FZ-1, Akai AX80/VX600/AX73/S950/S1000, Korg Radias/M3/03R/DSS-1/DW-6000, Roland JD-08/JU-06A/JX-08/D-10/U-20/CM-32L, Yamaha CS6x/SY85/TG33/FB-01/V50, Kawai K3/K11, Ensoniq DP/4/ASR-10. Reached 275 devices / 89,227 patches (`c0475bc`).
4. **Wave 13 (Rhythm Composers, Drum Machines & Boss Studio Multi-Effects):** Roland R-8/R-70/TR-606/TR-505/TR-626/CR-78/SPD-20/A-880/A-50/A-80, Boss DR-550/660/770/880/SE-50/SE-70/SX-700/VF-1/GT-6/ME-10/ME-5, Yamaha RY30/RX5/RX7/RX11, Korg DDD-1/DDD-5/S3/KPR-77, Alesis SR-16. Reached 305 devices / 92,703 patches (`84d4f63`).
5. **Wave 14 (90s Flagship Romplers, Sound Canvas Super-Modules & XG Synths):** Roland SC-88 Pro/SC-8850/SC-8820/SD-35/SD-50/PMA-5/XP-30/XP-50/JV-1010/JV-880/JV-80, Yamaha MU100/MU128/MU1000/MU2000/MU80/MU50/CS2x/Motif ES/Motif XF, Korg X5D/X3/X2/05R/W/NS5R/NX5R/TR-Rack/X50/microX/T3. Reached 335 devices / 101,959 patches (`87a1dd4`).
6. **Wave 15 (Guitar Synthesizers, Wind Modeling & Studio Pro Processors):** Roland GR-55/33/20/30/09/1, VG-99/88/8, GI-20, Boss SY-300/SY-1000/GP-10, Akai EWI4000S/5000, Yamaha VL70-m/WT11/WX5, Line 6 POD Pro/Bass POD Pro/Echo Pro/Mod Pro/Filter Pro/POD XT Pro, DigiTech IPS-33B/Whammy 5/Vocalist/TSR-24S/Studio 400, TC-Helicon VoiceLive. Reached 365 devices / 105,529 patches (`025c431`).
7. **Wave 16 (Studio Multi-Effects, Hardware Retrofits & Vintage Synths):** KiwiTechnics Kiwi-106/Kiwi-3P/Kiwi-Six/Kiwi-80/Patch Editor, Sony DPS-V77/R7/D7/M7, ART Multiverb Alpha/III/SGX-2000/DMV-Pro, TC Electronic FireworX/D-Two, TC-Helicon VoiceWorks, Dynacord TAM-19/CL-20, Ensoniq DP/2/EPS-16 Plus/KS-32/KT-76, Kawai K4r/K1r/K5000W, Sequential MultiTrak/Split-Eight/MAX/Drumtraks, Akai ME-80P. Reached 395 devices / 109,849 patches (`ae540af`).
8. **Wave 17 (Synthesizer Modules, Boutiques & Workstations):** Roland D-550/D-05/JD-Xi/JP-08/DEP-5/DEP-3/GP-16/GP-8/GR-50/EF-303, Korg 01R/W/EX-8000/EX-800/DS-8/DVP-1/EA-1/ER-1/A1/A3, Yamaha CS6R/EX7/DB50XG/DX9/Reface CP/FX900, E-MU Ultra Proteus/Classic Keys/XL-1, DigiTech DSP-256, Ensoniq SD-1. Reached 425 devices / 113,967 patches (`6ea4c95`).
9. **Wave 18 (Analog Classics, Modern Workstations & Consoles):** Studio Electronics ATC-1/ATC-X, MFB Tanzbär/Tanzbär Lite/Synth Lite II, Sequential Prophet-10/T8/Prophet X, Novation Circuit/KS-Rack, Alesis NanoSynth/NanoPiano/NanoBass/SR-18/Wedge, Roland Juno-X/Juno-DS/FA-06/Alpha Juno-2/E-660/GS-6, Yamaha Reface CS/DX/YC/01V/02R, Korg Kaossilator Pro/N1R/N264/i30. Reached 455 devices / 117,963 patches (`29b6630`).
10. **Wave 19 (Boutique Synths, Cult Modules & Studio Classics):** Studiologic Sledge, Octave-Plateau Voyetra-8, Marion Systems ProSynth, Futuresonus Parva, Moog Sirin, Red Sound Dark Star/Dark Star XP2, Waldorf Rocket/4-Pole, OTO Machines Biscuit, Meris Enzo/Hedra, MeeBlip anode/triode/geode, 1010music Nanobox Fireball, Yamaha SPX1000/RX17/RY20, Sony DPS-V55, DigiTech Valve-FX/GSP-256/GSP-7, Ensoniq DP PRO, TC Electronic G-Sharp, TC-Helicon VoicePro/VoiceOne, Kawai R-100/Spectra, Zoom 9030. Reached 485 devices / 120,334 patches (`5938cd6`).
11. **Wave 20 (Modern Flagships, Analog Powerhouses & Studio Racks):** Roland Jupiter-X/JX-03/JV-90/P-55, Yamaha SPX90 II/S90/03D, Korg N5/N5EX/N364, Sequential Tetra/Pro 3/Prophet Rev2, Modal 001/Cobalt5S, Roger Linn AdrenaLinn, Audiothingies Doctor A, Tasty Chips Sawbench, Evolution EVS-1, Hammond XB-2, JoMoX Airbase99, Lexicon Reflex/LXP-5, Dynacord DRP 15/DLS 223, ART DR-1/SGE, TC-Helicon VoiceDoubler, Zoom 9010, Fender G-DEC. Reached 515 devices / 123,634 patches (`3a4b288`).
12. **Wave 21 (Flagships, Advanced FM Vectors, Samplers & Volcas):** Roland V-Synth GT, SH-32, SH-01A, TR-08, TR-09, TR-06, VP-03, S-760, SRV-2000, U-220, XV-2020; Yamaha TG77, TG500, SY22, SY35, TX7, TX816, TX16W, SPX990, W7; Korg Volca Keys, Volca Bass, Volca Beats, Volca Nubass, SDD-3300, SG-Rack; Clavia Nord Rack 2X; Ensoniq ZR-76; DigiTech TSR-12, Legend II. Reached 545 devices / 1,966 banks / 126,988 patches (`d73c8d0`).
13. **Wave 22 (Flagships, Workstations, Samplers & Studio Racks):** Roland RS-5, RS-9, XP-10, XP-60, XV-88, JV-1000, VK-7, TR-6S, S-550, S-770, U-110, V-Synth XT; Yamaha SY55, TG55, TG100, TG300, YS100, YS200, SPX900, SW1000XG, P-100; Korg Nautilus, OASYS, TR-61, Volca Kick, SG-ProX, T1, T2, A4-Guitar; E-MU Proteus FX, Proteus/1 XR, Proteus/2 XR, Sound Engine; Ensoniq KT-88, TS-12; DigiTech DSP-128, GSP-5, RP-10; Access Music Virus Indigo, Virus KB. Reached **585 devices / 2,051 banks / 135,697 patches**.

---

## 4. How to Verify & Query the Database

### Sub-Millisecond Full-Text Search (SQLite FTS5)
```bash
# Query any sound, artist preset, or algorithm:
sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"Nautilus\"' LIMIT 5;
"

sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"XV-88\"' LIMIT 5;
"

sqlite3 omnipatch_library.db "
  SELECT p.device_name, p.bank_name, p.patch_name 
  FROM patches_fts f JOIN patches p ON f.rowid = p.id 
  WHERE patches_fts MATCH '\"Virus Indigo\"' LIMIT 5;
"
```

### Re-seeding the Librarian Database
Whenever new profiles or preset dumps are added to `devices/`:
```bash
python3 tools/seed_librarian_db.py
```

### Native Rust CLI
```bash
cargo build --release
./target/release/omnipatch devices list --dir devices/
./target/release/omnipatch devices show "Sequential Circuits Prophet-5" --dir devices/
```

---

## 5. Guide for Resuming Work (Next Waves)

To resume ingestion in future sessions with an agent or developer:

1. **Catalog Status:** Check remaining unmatched items from `resources/midiquest_catalog.json` (currently 85 remaining):
   ```bash
   python3 -c '
   import json, os, glob
   with open("resources/midiquest_catalog.json") as f:
       catalog = json.load(f)["instruments"]
   existing = {os.path.basename(p).lower().replace("-","").replace("_","") for p in glob.glob("devices/*/*")}
   remaining = [item for item in catalog if not any(ex in item["model_id"].lower().replace("-","").replace("_","") or item["model_id"].lower().replace("-","").replace("_","") in ex for ex in existing)]
   print(f"Remaining items: {len(remaining)}")
   '
   ```
2. **Standard Device Schema:** Each device directory under `devices/<manufacturer>/<model>/` must contain:
   * `profile.yaml`: Manufacturer, model, architecture type, year, MIDI CC mapping, SysEx header and request commands, bank definitions.
   * `factory_presets.json`: Flat list of patches with `number`, `name`, `bank`, `category`, `tags`, and `sysex_dump`.
3. **Seeding & Synchronization:**
   * Run `python3 tools/seed_librarian_db.py`.
   * Update statistics and the Manufacturer Coverage Matrix in [`README.md`](file:///home/daniel/Projects/omnipatch/README.md).
   * Commit and push changes to `main` with descriptive commit logs.
