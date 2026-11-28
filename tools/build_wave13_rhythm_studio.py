#!/usr/bin/env python3
"""
Wave 13 Rhythm Composers, Drum Machines & Boss Studio Multi-Effects Generator for OmniPatch:
- Roland Drums & Master Controllers: R-8 / R-8M, R-70, TR-606, TR-505, TR-626, CR-78, SPD-20, A-880, A-50, A-80
- Boss Dr. Rhythm & Studio Multi-FX: DR-550, DR-660, DR-770, DR-880, SE-50, SE-70, SX-700, VF-1, GT-6, ME-10, ME-5
- Yamaha Vintage Rhythm Programmers: RY30 (AWM2 w/ pitch wheel), RX5, RX7, RX11
- Korg Vintage Rhythm & Drums: DDD-1, DDD-5, S3 Rhythm Workstation, KPR-77
- Alesis: SR-16 (16-Bit Stereo Drum Machine classic)
Creates profile.yaml and factory_presets.json for 30 iconic instruments.
"""

import os
import json
import yaml

def write_synth(manufacturer, model_id, name, synth_type, year, midi_cc_map, sysex_spec, banks, presets):
    base_dir = os.path.join("devices", manufacturer, model_id)
    os.makedirs(base_dir, exist_ok=True)
    
    profile = {
        "manufacturer": manufacturer.replace("_", " ").title(),
        "model": name,
        "type": synth_type,
        "year": year,
        "midi": {
            "channels": 16,
            "cc_map": midi_cc_map
        },
        "sysex": sysex_spec,
        "banks": banks
    }
    
    with open(os.path.join(base_dir, "profile.yaml"), "w") as f:
        yaml.dump(profile, f, sort_keys=False, default_flow_style=False)
        
    with open(os.path.join(base_dir, "factory_presets.json"), "w") as f:
        json.dump(presets, f, indent=2)
        
    print(f"Created {manufacturer}/{model_id}: {name} ({len(presets)} presets)")

def build_wave13():
    print("Building Wave 13: Rhythm Composers, Drum Machines & Boss Studio Multi-Effects (30 Instruments)...")

    # =========================================================================
    # 1. ROLAND R-8 / R-8M (Human Rhythm Composer)
    # =========================================================================
    r8_cc = {"volume": 7, "pan": 10, "pitch_bend": 0, "decay": 72, "nuance": 16}
    r8_sysex = {"header": "F0 41 10 28", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 28 11 [addr] [size] [chk] F7"}}
    r8_banks = [{"name": "Preset Instrument Kit", "type": "ROM", "size": 68}, {"name": "Feel Patches", "type": "ROM", "size": 32}]
    r8_presets = []
    r8_names = [
        "Acoustic Bass Drum Dry", "Acoustic Bass Drum Room", "Power Bass Drum", "Gate Bass Drum", "Solid Bass Drum",
        "Acoustic Snare Drum Wood", "Acoustic Snare Drum Brass", "Piccolo Snare", "Rim Shot Natural", "Brush Snare Tap",
        "Brush Snare Swirl", "Side Stick Rim", "Cross Stick Snare", "Low Floor Tom", "Low Mid Tom", "High Mid Tom",
        "High Tom", "Rototom Low", "Rototom High", "Closed Hi-Hat Natural", "Half-Open Hi-Hat", "Open Hi-Hat Sizzle",
        "Pedal Hi-Hat Chiff", "Crash Cymbal 16\"", "Crash Cymbal 18\"", "Ride Cymbal Bow", "Ride Cymbal Bell",
        "China Cymbal Trash", "Splash Cymbal 10\"", "Cup Chime", "Tambourine Shake", "Cowbell High", "Cowbell Low",
        "Hand Claps Studio", "Cabasa Stroke", "Maracas Crisp", "Claves Studio", "Woodblock High", "Woodblock Low",
        "Bongo High Slap", "Bongo Low Open", "Conga High Slap", "Conga High Open", "Conga Low Open", "Timbale High",
        "Timbale Low", "Agogo High", "Agogo Low", "Triangle Open", "Triangle Mute", "Cuica High", "Cuica Low",
        "Vibraslap Sound", "Guiro Up", "Guiro Down", "Whistle Short", "Whistle Long", "Castanet Snap", "Shaker Latin",
        "Sleigh Bells", "Finger Snap Studio", "Orchestra Timpani", "Taiko Drum Slam", "Reverse Cymbal Hit",
        "TR-808 Bass Drum Deep", "TR-808 Snare Crisp", "TR-808 Hand Claps", "R-8 Master Feel Signature"
    ]
    for i, name in enumerate(r8_names):
        r8_presets.append({"name": f"R8 {name}", "bank": "Preset Instrument Kit", "number": i + 1, "category": "Drums", "tags": ["roland", "r-8", "human rhythm", "16-bit", "drums"]})
    for i in range(32):
        r8_presets.append({"name": f"R8 Feel Velocity Curve {i+1:02d}", "bank": "Feel Patches", "number": i + 1, "category": "Feel", "tags": ["roland", "r-8", "groove", "human timing"]})
    write_synth("roland", "r-8", "R-8 / R-8M", "Human Rhythm Composer", 1989, r8_cc, r8_sysex, r8_banks, r8_presets)

    # =========================================================================
    # 2. ROLAND R-70 (Human Rhythm Composer w/ Positional Pad)
    # =========================================================================
    r70_cc = {"volume": 7, "pan": 10, "decay": 72, "position": 16, "pitch": 17}
    r70_sysex = {"header": "F0 41 10 49", "device_id_byte": 2, "commands": {"request_drum": "F0 41 10 49 11 [addr] [size] [chk] F7"}}
    r70_banks = [{"name": "Internal Drum Library", "type": "ROM", "size": 100}, {"name": "Preset Rhythm Patterns", "type": "ROM", "size": 100}]
    r70_presets = []
    for i in range(100):
        r70_pool = ["Studio Maple Kick", "Fat Piccolo Snare", "Gated Ambience Tom", "Crisp Edge Hi-Hat", "Stage Sizzle Ride",
                    "TR-909 Attack Kick", "Electro 808 Snare", "Positional Latin Conga", "Natural Brazilian Pandeiro", "R-70 Dynamic Layer Hit"]
        base = r70_pool[i % len(r70_pool)]
        r70_presets.append({"name": f"R70 {base} #{i+1:02d}", "bank": "Internal Drum Library", "number": i + 1, "category": "Drums", "tags": ["roland", "r-70", "human rhythm", "positional pad"]})
    for i in range(100):
        r70_presets.append({"name": f"R70 Groove Pattern {i+1:02d}", "bank": "Preset Rhythm Patterns", "number": i + 1, "category": "Pattern", "tags": ["roland", "r-70", "pattern", "groove"]})
    write_synth("roland", "r-70", "R-70", "Human Rhythm Composer", 1992, r70_cc, r70_sysex, r70_banks, r70_presets)

    # =========================================================================
    # 3. ROLAND TR-606 (Drumatix)
    # =========================================================================
    tr606_cc = {"tempo": 20, "accent": 16, "volume": 7}
    tr606_sysex = {"header": "F0 41 00 00", "device_id_byte": 2, "commands": {"sync": "F8"}}
    tr606_banks = [{"name": "Pattern Bank A", "type": "RAM", "size": 16}, {"name": "Pattern Bank B", "type": "RAM", "size": 16}]
    tr606_presets = []
    tr606_names = ["Electro Bass Drum", "Snappy Snare Drum", "Low Tom Metallic", "High Tom Metallic", "Closed Cymbal-like Hat", "Open Metallic Hat", "Cymbal Wash Splash", "Accent Pulse Beat"]
    for b in ["Pattern Bank A", "Pattern Bank B"]:
        for i in range(16):
            base = tr606_names[i % len(tr606_names)]
            tr606_presets.append({"name": f"TR-606 {base} #{i+1:02d}", "bank": b, "number": i + 1, "category": "Drums", "tags": ["roland", "tr-606", "drumatix", "analog drums", "acid"]})
    write_synth("roland", "tr-606", "TR-606 Drumatix", "Analog Rhythm Composer", 1981, tr606_cc, tr606_sysex, tr606_banks, tr606_presets)

    # =========================================================================
    # 4. ROLAND TR-505 (Rhythm Composer)
    # =========================================================================
    tr505_cc = {"volume": 7, "pan": 10}
    tr505_sysex = {"header": "F0 41 00 12", "device_id_byte": 2, "commands": {"request_pattern": "F0 41 00 12 00 [pattern] F7"}}
    tr505_banks = [{"name": "Preset Rhythm Patterns", "type": "ROM", "size": 48}, {"name": "Drum Tones", "type": "ROM", "size": 16}]
    tr505_presets = []
    tr505_tones = ["Low Kick", "High Kick", "Snare Drum", "Low Tom", "Mid Tom", "High Tom", "Rim Shot", "Hand Clap",
                   "Closed Hi-Hat", "Open Hi-Hat", "Crash Cymbal", "Ride Cymbal", "Low Conga", "High Conga", "Timbale", "Cowbell"]
    for i, name in enumerate(tr505_tones):
        tr505_presets.append({"name": f"TR-505 {name}", "bank": "Drum Tones", "number": i + 1, "category": "Drums", "tags": ["roland", "tr-505", "pcm drums", "vintage", "latin"]})
    for i in range(48):
        tr505_presets.append({"name": f"TR-505 Rhythm Pattern {i+1:02d}", "bank": "Preset Rhythm Patterns", "number": i + 1, "category": "Pattern", "tags": ["roland", "tr-505", "rhythm", "groove"]})
    write_synth("roland", "tr-505", "TR-505", "Digital Rhythm Composer", 1986, tr505_cc, tr505_sysex, tr505_banks, tr505_presets)

    # =========================================================================
    # 5. ROLAND TR-626 (Rhythm Composer)
    # =========================================================================
    tr626_cc = {"volume": 7, "pan": 10, "pitch": 16}
    tr626_sysex = {"header": "F0 41 00 1B", "device_id_byte": 2, "commands": {"request_pattern": "F0 41 00 1B 00 [pattern] F7"}}
    tr626_banks = [{"name": "Preset Patterns", "type": "ROM", "size": 48}, {"name": "Drum Voice Bank", "type": "ROM", "size": 30}]
    tr626_presets = []
    tr626_voices = [
        "Bass Drum 1 Standard", "Bass Drum 2 Punch", "Snare Drum 1 Acoustic", "Snare Drum 2 Gated", "Snare Drum 3 Fat",
        "Rim Shot Natural", "Cross Stick Crisp", "Low Tom 1", "Low Tom 2", "Mid Tom 1", "Mid Tom 2", "High Tom 1", "High Tom 2",
        "Closed Hi-Hat 1", "Closed Hi-Hat 2", "Open Hi-Hat Sizzle", "Crash Cymbal 1", "Crash Cymbal 2", "Ride Cymbal Cup",
        "China Cymbal Trash", "Cup Chime", "Hand Clap Studio", "Tambourine Shake", "Cowbell Latin", "Claves Studio",
        "High Bongo Slap", "Low Bongo", "Mute Conga Slap", "Open Conga Low", "High Timbale Rim"
    ]
    for i, name in enumerate(tr626_voices):
        tr626_presets.append({"name": f"TR-626 {name}", "bank": "Drum Voice Bank", "number": i + 1, "category": "Drums", "tags": ["roland", "tr-626", "pcm drums", "tuning", "latin"]})
    for i in range(48):
        tr626_presets.append({"name": f"TR-626 Pattern Preset {i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["roland", "tr-626", "pattern"]})
    write_synth("roland", "tr-626", "TR-626", "Digital Rhythm Composer", 1987, tr626_cc, tr626_sysex, tr626_banks, tr626_presets)

    # =========================================================================
    # 6. ROLAND CR-78 (CompuRhythm)
    # =========================================================================
    cr78_cc = {"tempo": 20, "accent": 16, "volume": 7}
    cr78_sysex = {"header": "F0 41 00 00", "device_id_byte": 2, "commands": {"clock": "F8"}}
    cr78_banks = [{"name": "Preset Rhythms", "type": "ROM", "size": 34}, {"name": "Drum Voices", "type": "ROM", "size": 14}]
    cr78_presets = []
    cr78_rhythms = [
        "Rock 1", "Rock 2", "Rock 3", "Rock 4", "Disco 1", "Disco 2", "Waltz", "Shuffle", "Slow Rock", "Swing",
        "Fox Trot", "Tango", "Cha-Cha", "Rumba", "Bossa Nova", "Samba", "Mambo", "Enka", "Beguine", "Habanera",
        "Add Rock 1", "Add Rock 2", "Add Rock 3", "Add Rock 4", "Add Disco 1", "Add Disco 2", "Add Waltz", "Add Shuffle",
        "Add Slow Rock", "Add Swing", "Add Fox Trot", "Add Tango", "Add Cha-Cha", "Add Rumba"
    ]
    for i, name in enumerate(cr78_rhythms):
        cr78_presets.append({"name": f"CR-78 {name}", "bank": "Preset Rhythms", "number": i + 1, "category": "Rhythm", "tags": ["roland", "cr-78", "compurhythm", "vintage", "analog"]})
    cr78_tones = ["Bass Drum", "Snare Drum", "Rim Shot", "High Bongo", "Low Bongo", "High Conga", "Low Conga", "Cowbell", "Tambourine", "Maracas", "Guiro", "Claves", "Cymbal", "Hi-Hat Metallic"]
    for i, name in enumerate(cr78_tones):
        cr78_presets.append({"name": f"CR-78 Voice {name}", "bank": "Drum Voices", "number": i + 1, "category": "Drums", "tags": ["roland", "cr-78", "analog voice"]})
    write_synth("roland", "cr-78", "CR-78 CompuRhythm", "Classic Analog Rhythm Machine", 1978, cr78_cc, cr78_sysex, cr78_banks, cr78_presets)

    # =========================================================================
    # 7. ROLAND SPD-20 (Total Percussion Pad)
    # =========================================================================
    spd_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_level": 91}
    spd_sysex = {"header": "F0 41 10 00 24", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 24 11 [patch] F7"}}
    spd_banks = [{"name": "Preset Drum Kits", "type": "ROM", "size": 99}]
    spd_presets = []
    for i in range(99):
        spd_pool = ["Acoustic Studio Kit", "Indian Tabla & Dholak", "Latin Salsa Percussion", "African Djembe Dunun", "Orchestral Concert Kit",
                    "TR-808/909 Dance Kit", "Heavy Rock Stadium Kit", "Jazz Brush Percussion", "Japanese Taiko Ensemble", "World Ethnic Shakers"]
        base = spd_pool[i % len(spd_pool)]
        spd_presets.append({"name": f"SPD-20 {base} #{i+1:02d}", "bank": "Preset Drum Kits", "number": i + 1, "category": "Percussion", "tags": ["roland", "spd-20", "electronic percussion", "octapad", "world"]})
    write_synth("roland", "spd-20", "SPD-20", "Total Percussion Pad Controller", 1998, spd_cc, spd_sysex, spd_banks, spd_presets)

    # =========================================================================
    # 8. ROLAND A-880 (8-In / 8-Out MIDI Patcher & Merger)
    # =========================================================================
    a880_cc = {"merge_mode": 16, "panic": 123}
    a880_sysex = {"header": "F0 41 10 21", "device_id_byte": 2, "commands": {"request_program": "F0 41 10 21 11 [addr] [size] [chk] F7"}}
    a880_banks = [{"name": "Patch Memory", "type": "RAM", "size": 64}]
    a880_presets = []
    for i in range(64):
        a880_presets.append({"name": f"A-880 Routing Matrix {i+1:02d}", "bank": "Patch Memory", "number": i + 1, "category": "Routing", "tags": ["roland", "a-880", "midi patcher", "merger", "utility"]})
    write_synth("roland", "a-880", "A-880", "8-In / 8-Out MIDI Patcher / Mixer", 1988, a880_cc, a880_sysex, a880_banks, a880_presets)

    # =========================================================================
    # 9. ROLAND A-50 (76-Key MIDI Master Keyboard Controller w/ Poly Aftertouch)
    # =========================================================================
    a50_cc = {"mod_wheel": 1, "pitch_bend": 0, "slider1": 16, "slider2": 17, "slider3": 18, "slider4": 19, "aftertouch": 2}
    a50_sysex = {"header": "F0 41 10 27", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 27 11 [patch] F7"}}
    a50_banks = [{"name": "Zone Performance Memories", "type": "RAM", "size": 64}]
    a50_presets = []
    for i in range(64):
        a50_presets.append({"name": f"A-50 4-Zone Setup {i+1:02d}", "bank": "Zone Performance Memories", "number": i + 1, "category": "Performance", "tags": ["roland", "a-50", "master keyboard", "poly aftertouch"]})
    write_synth("roland", "a-50", "A-50", "76-Key MIDI Master Keyboard Controller", 1989, a50_cc, a50_sysex, a50_banks, a50_presets)

    # =========================================================================
    # 10. ROLAND A-80 (88-Key Weighted Hammer Master Keyboard Controller)
    # =========================================================================
    a80_cc = {"mod_wheel": 1, "pitch_bend": 0, "slider1": 16, "slider2": 17, "slider3": 18, "slider4": 19, "aftertouch": 2}
    a80_sysex = {"header": "F0 41 10 26", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 26 11 [patch] F7"}}
    a80_banks = [{"name": "Zone Performance Memories", "type": "RAM", "size": 64}]
    a80_presets = []
    for i in range(64):
        a80_presets.append({"name": f"A-80 Concert Setup {i+1:02d}", "bank": "Zone Performance Memories", "number": i + 1, "category": "Performance", "tags": ["roland", "a-80", "weighted keys", "master controller"]})
    write_synth("roland", "a-80", "A-80", "88-Key Weighted Master Keyboard Controller", 1989, a80_cc, a80_sysex, a80_banks, a80_presets)

    # =========================================================================
    # 11. BOSS DR-550 (Dr. Rhythm)
    # =========================================================================
    dr550_cc = {"volume": 7, "pan": 10, "pitch": 16}
    dr550_sysex = {"header": "F0 41 00 2B", "device_id_byte": 2, "commands": {"request_pattern": "F0 41 00 2B 00 [pattern] F7"}}
    dr550_banks = [{"name": "Preset Patterns", "type": "ROM", "size": 64}, {"name": "Drum Voices", "type": "ROM", "size": 48}]
    dr550_presets = []
    for i in range(48):
        dr550_presets.append({"name": f"DR-550 Drum Voice #{i+1:02d}", "bank": "Drum Voices", "number": i + 1, "category": "Drums", "tags": ["boss", "dr-550", "dr rhythm", "16-bit"]})
    for i in range(64):
        dr550_presets.append({"name": f"DR-550 Pattern {i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["boss", "dr-550", "pattern"]})
    write_synth("boss", "dr-550", "DR-550 Dr. Rhythm", "16-Bit Digital Drum Machine", 1990, dr550_cc, dr550_sysex, dr550_banks, dr550_presets)

    # =========================================================================
    # 12. BOSS DR-660 (Dr. Rhythm)
    # =========================================================================
    dr660_cc = {"volume": 7, "pan": 10, "decay": 72, "pitch": 16, "reverb_level": 91, "chorus_level": 93}
    dr660_sysex = {"header": "F0 41 00 4B", "device_id_byte": 2, "commands": {"request_kit": "F0 41 00 4B 00 [kit] F7"}}
    dr660_banks = [{"name": "Preset Drum Kits", "type": "ROM", "size": 39}, {"name": "Preset Patterns", "type": "ROM", "size": 100}]
    dr660_presets = []
    for i in range(39):
        dr660_pool = ["Standard Studio Drum Kit", "Deep Power Rock Kit", "TR-808/909 Dance Kit", "Acoustic Jazz Brush", "Latin Salsa Percussion", "Reggae Ska Drum Set"]
        base = dr660_pool[i % len(dr660_pool)]
        dr660_presets.append({"name": f"DR-660 {base} #{i+1:02d}", "bank": "Preset Drum Kits", "number": i + 1, "category": "Drums", "tags": ["boss", "dr-660", "dr rhythm", "drum kit"]})
    for i in range(100):
        dr660_presets.append({"name": f"DR-660 Groove Pattern {i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["boss", "dr-660", "groove", "rhythm"]})
    write_synth("boss", "dr-660", "DR-660 Dr. Rhythm", "16-Bit Dynamic Drum Machine w/ Effects", 1992, dr660_cc, dr660_sysex, dr660_banks, dr660_presets)

    # =========================================================================
    # 13. BOSS DR-770 (Dr. Rhythm)
    # =========================================================================
    dr770_cc = {"volume": 7, "pan": 10, "reverb_level": 91, "flanger_level": 93, "equalizer_gain": 80}
    dr770_sysex = {"header": "F0 41 00 00 1E", "device_id_byte": 2, "commands": {"request_kit": "F0 41 00 00 1E 00 [kit] F7"}}
    dr770_banks = [{"name": "Preset Drum Kits", "type": "ROM", "size": 64}, {"name": "Preset Patterns", "type": "ROM", "size": 100}]
    dr770_presets = []
    for i in range(64):
        dr770_presets.append({"name": f"DR-770 Drum Kit #{i+1:02d}", "bank": "Preset Drum Kits", "number": i + 1, "category": "Drums", "tags": ["boss", "dr-770", "dr rhythm", "dpac"]})
    for i in range(100):
        dr770_presets.append({"name": f"DR-770 Pattern #{i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["boss", "dr-770", "pattern"]})
    write_synth("boss", "dr-770", "DR-770 Dr. Rhythm", "Advanced Drum Machine with DPAC", 1999, dr770_cc, dr770_sysex, dr770_banks, dr770_presets)

    # =========================================================================
    # 14. BOSS DR-880 (Dr. Rhythm Flagship Guitar/Bass/Drum Workstation)
    # =========================================================================
    dr880_cc = {"volume": 7, "pan": 10, "reverb_level": 91, "chorus_level": 93, "cosm_amp": 80}
    dr880_sysex = {"header": "F0 41 00 00 75", "device_id_byte": 2, "commands": {"request_kit": "F0 41 00 00 75 00 [kit] F7"}}
    dr880_banks = [{"name": "Preset Drum/Bass Kits", "type": "ROM", "size": 100}, {"name": "Preset Patterns", "type": "ROM", "size": 100}]
    dr880_presets = []
    for i in range(100):
        dr880_pool = ["Studio Rock Bass & Drums", "Funk Slap Bass Groove Kit", "Modern R&B Acoustic Kit", "Hip-Hop Boomy Sub & Hat", "COSM Blues Band Setup"]
        base = dr880_pool[i % len(dr880_pool)]
        dr880_presets.append({"name": f"DR-880 {base} #{i+1:02d}", "bank": "Preset Drum/Bass Kits", "number": i + 1, "category": "Drums", "tags": ["boss", "dr-880", "cosm", "bass and drums", "flagship"]})
    for i in range(100):
        dr880_presets.append({"name": f"DR-880 Performance Groove {i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["boss", "dr-880", "groove"]})
    write_synth("boss", "dr-880", "DR-880 Dr. Rhythm", "Flagship Rhythm & Guitar/Bass Workstation", 2004, dr880_cc, dr880_sysex, dr880_banks, dr880_presets)

    # =========================================================================
    # 15. BOSS SE-50 (Stereo Effects Processor)
    # =========================================================================
    se50_cc = {"input_level": 7, "output_level": 8, "fx_bypass": 84, "mix": 91}
    se50_sysex = {"header": "F0 41 10 3F", "device_id_byte": 2, "commands": {"request_program": "F0 41 10 3F 11 [prog] F7"}}
    se50_banks = [{"name": "Factory Preset Programs", "type": "ROM", "size": 100}]
    se50_presets = []
    se50_names = [
        "Stereo Hall Reverb", "Warm Room Reverb", "Plate Studio Reverb", "Vocal Multi Reverb", "Gated Reverb 80s",
        "Stereo Delay Ping Pong", "Multi-Tap Rhythm Delay", "Analog Chorus Warm", "Dimension Stereo Spatializer",
        "Space Flanger Jet", "12-Stage Phaser", "Rotary Speaker Sim", "Pitch Shifter Detune", "Vocoder 10-Band",
        "Guitar Multi Overdrive", "Metal Distortion Solo", "Bass Multi Equalizer", "Stereo Enhancer", "Ring Modulator Bell",
        "Slow Gear Swell"
    ]
    for i in range(100):
        base = se50_names[i % len(se50_names)]
        se50_presets.append({"name": f"SE50 {base} #{i+1:02d}", "bank": "Factory Preset Programs", "number": i + 1, "category": "FX", "tags": ["boss", "se-50", "half-rack", "multi-effects", "studio classic"]})
    write_synth("boss", "se-50", "SE-50", "Stereo Multi-Effects Processor", 1990, se50_cc, se50_sysex, se50_banks, se50_presets)

    # =========================================================================
    # 16. BOSS SE-70 (Super Effects Processor)
    # =========================================================================
    se70_cc = {"input_level": 7, "output_level": 8, "fx_bypass": 84, "mix": 91, "param1": 16, "param2": 17}
    se70_sysex = {"header": "F0 41 10 5B", "device_id_byte": 2, "commands": {"request_program": "F0 41 10 5B 11 [prog] F7"}}
    se70_banks = [{"name": "Preset Program Bank", "type": "ROM", "size": 100}]
    se70_presets = []
    se70_names = [
        "Concert Hall Reverb Large", "Studio Vocal Plate", "Multi-Tap Stereo Delay", "21-Band Vocoder", "Guitar Multi Clean Chorus",
        "Lead Guitar Stack Distortion", "Bass Multi Slap Funky", "Rotary Speaker Slow/Fast", "Intelligent Pitch Harmonizer",
        "Stereo Modulation Flanger", "Dual Pitch Micro Shift", "Analog Resonant Filter Sweep", "Stereo Dimension Chorus",
        "Acoustic Guitar Simulator", "Ring Modulator Sci-Fi", "Slow Gear Volume Swell", "Compressor Limiter Studio",
        "Parametric 4-Band EQ", "Guitar Synth Monophonic", "SE-70 Master Multi-Rack"
    ]
    for i in range(100):
        base = se70_names[i % len(se70_names)]
        se70_presets.append({"name": f"SE70 {base} #{i+1:02d}", "bank": "Preset Program Bank", "number": i + 1, "category": "FX", "tags": ["boss", "se-70", "super effects", "analog distortion", "half-rack"]})
    write_synth("boss", "se-70", "SE-70", "Super Multi-Effects Processor", 1993, se70_cc, se70_sysex, se70_banks, se70_presets)

    # =========================================================================
    # 17. BOSS SX-700 (Studio Effects Processor w/ RSS 3D)
    # =========================================================================
    sx700_cc = {"mix": 91, "rss_azimuth": 16, "rss_elevation": 17, "fx_bypass": 84}
    sx700_sysex = {"header": "F0 41 10 00 05", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 05 11 [patch] F7"}}
    sx700_banks = [{"name": "Preset Studio Patches", "type": "ROM", "size": 100}]
    sx700_presets = []
    for i in range(100):
        sx_pool = ["RSS 3D Spatial Concert Hall", "3D Circular Panning Delay", "Warm Studio Plate Reverb", "Multi-Band Spatial Chorus",
                   "Flanger 3D Jet Fly-By", "Phaser Overhead Swirl", "RSS Binaural Room Ambience", "Intelligent Harmonizer 3D",
                   "Rotary Speaker 3D Doppler", "SX-700 Master 3D Spatializer"]
        base = sx_pool[i % len(sx_pool)]
        sx700_presets.append({"name": f"SX700 {base} #{i+1:02d}", "bank": "Preset Studio Patches", "number": i + 1, "category": "FX", "tags": ["boss", "sx-700", "rss", "3d sound", "studio processor"]})
    write_synth("boss", "sx-700", "SX-700", "Studio Effects Processor with RSS 3D", 1996, sx700_cc, sx700_sysex, sx700_banks, sx700_presets)

    # =========================================================================
    # 18. BOSS VF-1 (24-bit Multi-Effects Processor COSM)
    # =========================================================================
    vf1_cc = {"mix": 91, "cosm_gain": 80, "fx_bypass": 84, "ctrl1": 16, "ctrl2": 17}
    vf1_sysex = {"header": "F0 41 10 00 1E", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 1E 11 [patch] F7"}}
    vf1_banks = [{"name": "Preset Programs", "type": "ROM", "size": 200}]
    vf1_presets = []
    for i in range(200):
        vf_pool = ["COSM Lead Guitar Stack", "Acoustic Guitar Simulator", "Bass Multi Drive & Compressor", "Vocal Channel Strip Pro",
                   "Concert Hall 24-Bit Reverb", "Stereo Multi-Tap Delay", "Analog Rotary Organ Simulator", "Step Modulated Phaser",
                   "Stereo Pitch Shifter Harmonizer", "VF-1 Signature Mastering Rack"]
        base = vf_pool[i % len(vf_pool)]
        vf1_presets.append({"name": f"VF1 {base} #{i+1:03d}", "bank": "Preset Programs", "number": i + 1, "category": "FX", "tags": ["boss", "vf-1", "cosm", "24-bit", "half-rack multi-effects"]})
    write_synth("boss", "vf-1", "VF-1", "24-Bit Multiple Effects Processor", 1999, vf1_cc, vf1_sysex, vf1_banks, vf1_presets)

    # =========================================================================
    # 19. BOSS GT-6 (Guitar Effects Processor w/ COSM Modeling)
    # =========================================================================
    gt6_cc = {"expression_pedal": 11, "fx_on_off": 80, "gain": 81, "mix": 91}
    gt6_sysex = {"header": "F0 41 10 00 46", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 46 11 [patch] F7"}}
    gt6_banks = [{"name": "Preset Patches", "type": "ROM", "size": 140}, {"name": "User Memory", "type": "RAM", "size": 200}]
    gt6_presets = []
    for b, bname in enumerate(["Preset Patches", "User Memory"]):
        sz = 140 if b == 0 else 200
        for i in range(sz):
            gt_pool = ["COSM JC-120 Clean Chorus", "Tweed Blues Crunch Solo", "Plexi Marshall Lead Crunch", "5150 High Gain Shredder",
                       "Rectifier Modern Heavy Metal", "Wah-Wah Expression Lead", "Uni-Vibe Vintage Swirl", "Slow Gear Ambient Swell",
                       "Acoustic Guitar Piezo Sim", "GT-6 Stadium Soloist"]
            base = gt_pool[i % len(gt_pool)]
            gt6_presets.append({"name": f"GT6 {base} #{i+1:03d}", "bank": bname, "number": i + 1, "category": "Guitar", "tags": ["boss", "gt-6", "cosm", "guitar multi-effects", "amp modeling"]})
    write_synth("boss", "gt-6", "GT-6", "COSM Guitar Effects Processor", 2001, gt6_cc, gt6_sysex, gt6_banks, gt6_presets)

    # =========================================================================
    # 20. BOSS ME-10 (Vintage Multiple Effects Floorboard)
    # =========================================================================
    me10_cc = {"drive": 80, "master_vol": 7, "mix": 91, "delay_time": 16}
    me10_sysex = {"header": "F0 41 10 4E", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 4E 11 [patch] F7"}}
    me10_banks = [{"name": "Factory Preset Bank", "type": "ROM", "size": 64}, {"name": "User Memory Bank", "type": "RAM", "size": 64}]
    me10_presets = []
    for b, bname in enumerate(["Factory Preset Bank", "User Memory Bank"]):
        for i in range(64):
            me_pool = ["Vintage Tube Drive Solo", "Stereo Chorus Clean", "Warm Analog Delay Lead", "Heavy Metal Distortion", "Funk Compressor Auto Wah", "Ambient Reverb Swell"]
            base = me_pool[i % len(me_pool)]
            me10_presets.append({"name": f"ME10 {base} #{i+1:02d}", "bank": bname, "number": i + 1, "category": "Guitar", "tags": ["boss", "me-10", "floorboard", "guitar multi-effects"]})
    write_synth("boss", "me-10", "ME-10", "Guitar Multiple Effects Floorboard", 1992, me10_cc, me10_sysex, me10_banks, me10_presets)

    # =========================================================================
    # 21. BOSS ME-5 (Classic 1988 Analog/Digital Guitar Multi-Effects)
    # =========================================================================
    me5_cc = {"compressor_sw": 80, "overdrive_sw": 81, "equalizer_sw": 82, "chorus_flanger_sw": 83, "digital_delay_sw": 84}
    me5_sysex = {"header": "F0 41 10 23", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 23 11 [patch] F7"}}
    me5_banks = [{"name": "Preset Patches", "type": "ROM", "size": 64}]
    me5_presets = []
    for i in range(64):
        me5_pool = ["TS-9 Style Warm Tube Overdrive", "DS-1 Style Crisp Distortion", "CE-2 Stereo Chorus Clean", "BF-2 Jet Flanger Lead", "DM-2 Warm Delay Solo", "CS-2 Sustained Lead"]
        base = me5_pool[i % len(me5_pool)]
        me5_presets.append({"name": f"ME5 {base} #{i+1:02d}", "bank": "Preset Patches", "number": i + 1, "category": "Guitar", "tags": ["boss", "me-5", "analog distortion", "ce-2 chorus", "vintage"]})
    write_synth("boss", "me-5", "ME-5", "Multiple Effects Processor (Analog Core)", 1988, me5_cc, me5_sysex, me5_banks, me5_presets)

    # =========================================================================
    # 22. YAMAHA RY30 (AWM2 Rhythm Programmer w/ Pitch Wheel)
    # =========================================================================
    ry30_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "filter_resonance": 71, "pitch_bend": 0}
    ry30_sysex = {"header": "F0 43 10 32", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 32 00 [voice] F7"}}
    ry30_banks = [{"name": "Preset Drum Voices", "type": "ROM", "size": 96}, {"name": "Preset Rhythm Patterns", "type": "ROM", "size": 100}]
    ry30_presets = []
    ry30_voices = [
        "Acoustic Maple Kick", "Gate Punch Kick", "Studio Birch Snare", "Piccolo Brass Snare", "Rim Shot Natural",
        "Acoustic Low Tom", "Acoustic Mid Tom", "Acoustic High Tom", "Closed Hat Natural", "Open Hat Sizzle",
        "Crash Cymbal 16\"", "Ride Cymbal Bell", "Cup Chime", "Hand Clap Studio", "Tambourine Shake", "Cowbell Latin",
        "Conga High Slap", "Conga Low Open", "Bongo High Slap", "Timbale High", "Shaker Latin", "Cabasa Stroke",
        "Agogo Bell High", "Triangle High", "Whistle Short", "Reverse Snare Gated", "Analog 808 Kick Saw", "Analog 909 Snare Punch"
    ]
    for i in range(96):
        base = ry30_voices[i % len(ry30_voices)]
        ry30_presets.append({"name": f"RY30 {base} #{i+1:02d}", "bank": "Preset Drum Voices", "number": i + 1, "category": "Drums", "tags": ["yamaha", "ry30", "awm2", "pitch wheel", "dynamic filter"]})
    for i in range(100):
        ry30_presets.append({"name": f"RY30 Pattern Groove {i+1:02d}", "bank": "Preset Rhythm Patterns", "number": i + 1, "category": "Pattern", "tags": ["yamaha", "ry30", "groove", "pattern"]})
    write_synth("yamaha", "ry30", "RY30", "AWM2 Programmable Rhythm Synthesizer", 1991, ry30_cc, ry30_sysex, ry30_banks, ry30_presets)

    # =========================================================================
    # 23. YAMAHA RX5 (Digital Rhythm Programmer w/ Voice Tuning & Envelopes)
    # =========================================================================
    rx5_cc = {"volume": 7, "pan": 10, "pitch": 16, "decay": 72}
    rx5_sysex = {"header": "F0 43 10 1B", "device_id_byte": 2, "commands": {"request_pattern": "F0 43 10 1B 00 [pattern] F7"}}
    rx5_banks = [{"name": "Internal Voice Bank", "type": "ROM", "size": 24}, {"name": "Preset Patterns", "type": "ROM", "size": 64}]
    rx5_presets = []
    rx5_voices = [
        "BD 1 Normal Punch", "BD 2 Deep Acoustic", "SD 1 Crisp Wood", "SD 2 Gated 80s", "Rim Shot Studio",
        "Tom 1 High", "Tom 2 Mid", "Tom 3 Low", "Tom 4 Floor", "Hi-Hat Closed Crisp", "Hi-Hat Open Sizzle",
        "Crash Cymbal 1", "Ride Cymbal Cup", "China Cymbal Trash", "Hand Clap Studio", "Tambourine Shake",
        "Cowbell Latin", "Shaker High", "Castanet Snap", "Whistle Solo", "Electric Bass Slap", "Electric Bass Pull",
        "Guitar Chord Pluck", "Orchestra Hit Chord"
    ]
    for i, name in enumerate(rx5_voices):
        rx5_presets.append({"name": f"RX5 {name}", "bank": "Internal Voice Bank", "number": i + 1, "category": "Drums", "tags": ["yamaha", "rx5", "12-bit", "reverse", "envelope", "classic 80s"]})
    for i in range(64):
        rx5_presets.append({"name": f"RX5 Pattern #{i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["yamaha", "rx5", "pattern"]})
    write_synth("yamaha", "rx5", "RX5", "Digital Rhythm Programmer", 1986, rx5_cc, rx5_sysex, rx5_banks, rx5_presets)

    # =========================================================================
    # 24. YAMAHA RX7 (Digital Rhythm Programmer w/ 100 Sounds)
    # =========================================================================
    rx7_cc = {"volume": 7, "pan": 10, "pitch": 16}
    rx7_sysex = {"header": "F0 43 10 24", "device_id_byte": 2, "commands": {"request_pattern": "F0 43 10 24 00 [pattern] F7"}}
    rx7_banks = [{"name": "Preset Instrument Voices", "type": "ROM", "size": 100}, {"name": "Preset Patterns", "type": "ROM", "size": 100}]
    rx7_presets = []
    for i in range(100):
        rx7_presets.append({"name": f"RX7 Instrument #{i+1:03d}", "bank": "Preset Instrument Voices", "number": i + 1, "category": "Drums", "tags": ["yamaha", "rx7", "pcm drums", "100 voices"]})
    for i in range(100):
        rx7_presets.append({"name": f"RX7 Pattern #{i+1:03d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["yamaha", "rx7", "pattern"]})
    write_synth("yamaha", "rx7", "RX7", "Digital Rhythm Programmer (100 Voices)", 1987, rx7_cc, rx7_sysex, rx7_banks, rx7_presets)

    # =========================================================================
    # 25. YAMAHA RX11 (Digital Rhythm Programmer)
    # =========================================================================
    rx11_cc = {"volume": 7, "pan": 10}
    rx11_sysex = {"header": "F0 43 00 00", "device_id_byte": 2, "commands": {"sync": "F8"}}
    rx11_banks = [{"name": "Preset Drum Sounds", "type": "ROM", "size": 29}, {"name": "Preset Patterns", "type": "ROM", "size": 50}]
    rx11_presets = []
    rx11_names = [
        "Bass Drum 1 Heavy", "Bass Drum 2 Tight", "Bass Drum 3 Crisp", "Snare Drum 1 Acoustic", "Snare Drum 2 Punch",
        "Snare Drum 3 Fat", "Snare Drum 4 Rim", "Rim Shot Natural", "Tom 1 High", "Tom 2 Mid-High", "Tom 3 Mid-Low",
        "Tom 4 Low Floor", "Hi-Hat Closed 1", "Hi-Hat Closed 2", "Hi-Hat Open 1", "Hi-Hat Open 2", "Crash Cymbal 1",
        "Crash Cymbal 2", "Ride Cymbal 1", "Ride Cymbal 2", "Hand Claps Studio", "Tambourine Shake", "Cowbell High",
        "Cowbell Low", "Shaker Studio", "Bongo High", "Bongo Low", "Conga High", "Conga Low"
    ]
    for i, name in enumerate(rx11_names):
        rx11_presets.append({"name": f"RX11 {name}", "bank": "Preset Drum Sounds", "number": i + 1, "category": "Drums", "tags": ["yamaha", "rx11", "vintage 1984", "digital drums"]})
    for i in range(50):
        rx11_presets.append({"name": f"RX11 Pattern #{i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["yamaha", "rx11", "pattern"]})
    write_synth("yamaha", "rx11", "RX11", "Digital Rhythm Programmer", 1984, rx11_cc, rx11_sysex, rx11_banks, rx11_presets)

    # =========================================================================
    # 26. KORG DDD-1 (Dynamic Digital Drums w/ Touch Sensitive Pads & ROM Cards)
    # =========================================================================
    ddd1_cc = {"volume": 7, "pan": 10, "pitch": 16, "decay": 72}
    ddd1_sysex = {"header": "F0 42 30 11", "device_id_byte": 2, "commands": {"request_pattern": "F0 42 30 11 00 [pattern] F7"}}
    ddd1_banks = [{"name": "Factory Drum Sounds", "type": "ROM", "size": 18}, {"name": "Preset Patterns", "type": "ROM", "size": 64}]
    ddd1_presets = []
    ddd1_names = [
        "Bass Drum 1 Punch", "Bass Drum 2 Deep", "Snare Drum 1 Wood", "Snare Drum 2 Gated", "Rim Shot Crisp",
        "High Tom", "Mid Tom", "Low Tom", "Closed Hi-Hat", "Open Hi-Hat Sizzle", "Crash Cymbal", "Ride Cymbal Cup",
        "Hand Clap Studio", "Tambourine Shake", "Cowbell Latin", "High Conga", "Low Conga", "Cabasa Stroke"
    ]
    for i, name in enumerate(ddd1_names):
        ddd1_presets.append({"name": f"DDD1 {name}", "bank": "Factory Drum Sounds", "number": i + 1, "category": "Drums", "tags": ["korg", "ddd-1", "12-bit", "sampling drums", "touch pads"]})
    for i in range(64):
        ddd1_presets.append({"name": f"DDD1 Pattern #{i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["korg", "ddd-1", "pattern"]})
    write_synth("korg", "ddd-1", "DDD-1", "Dynamic Digital Drums", 1986, ddd1_cc, ddd1_sysex, ddd1_banks, ddd1_presets)

    # =========================================================================
    # 27. KORG DDD-5 (Dynamic Digital Drums)
    # =========================================================================
    ddd5_cc = {"volume": 7, "pan": 10, "pitch": 16}
    ddd5_sysex = {"header": "F0 42 30 17", "device_id_byte": 2, "commands": {"request_pattern": "F0 42 30 17 00 [pattern] F7"}}
    ddd5_banks = [{"name": "Preset Drum Voices", "type": "ROM", "size": 29}, {"name": "Preset Patterns", "type": "ROM", "size": 64}]
    ddd5_presets = []
    for i in range(29):
        ddd5_presets.append({"name": f"DDD5 Drum Voice #{i+1:02d}", "bank": "Preset Drum Voices", "number": i + 1, "category": "Drums", "tags": ["korg", "ddd-5", "digital drums"]})
    for i in range(64):
        ddd5_presets.append({"name": f"DDD5 Pattern #{i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["korg", "ddd-5", "pattern"]})
    write_synth("korg", "ddd-5", "DDD-5", "Dynamic Digital Drums", 1987, ddd5_cc, ddd5_sysex, ddd5_banks, ddd5_presets)

    # =========================================================================
    # 28. KORG S3 (Advanced Rhythm Workstation w/ SMPTE & Multi-Effects)
    # =========================================================================
    s3_cc = {"volume": 7, "pan": 10, "pitch": 16, "reverb_level": 91}
    s3_sysex = {"header": "F0 42 30 33", "device_id_byte": 2, "commands": {"request_kit": "F0 42 30 33 00 [kit] F7"}}
    s3_banks = [{"name": "Drum Kit Presets", "type": "ROM", "size": 30}, {"name": "Preset Patterns", "type": "ROM", "size": 100}]
    s3_presets = []
    for i in range(30):
        s3_pool = ["Acoustic Master Kit", "Heavy Rock Arena Kit", "Electronic Dance 90s Kit", "Latin Fiesta Kit", "Studio Funk Percussion"]
        base = s3_pool[i % len(s3_pool)]
        s3_presets.append({"name": f"S3 {base} #{i+1:02d}", "bank": "Drum Kit Presets", "number": i + 1, "category": "Drums", "tags": ["korg", "s3", "rhythm workstation", "multi-effects", "16-bit"]})
    for i in range(100):
        s3_presets.append({"name": f"S3 Workstation Pattern {i+1:02d}", "bank": "Preset Patterns", "number": i + 1, "category": "Pattern", "tags": ["korg", "s3", "pattern", "groove"]})
    write_synth("korg", "s3", "S3", "Advanced Rhythm Workstation", 1991, s3_cc, s3_sysex, s3_banks, s3_presets)

    # =========================================================================
    # 29. KORG KPR-77 (Programmable Rhythm)
    # =========================================================================
    kpr_cc = {"tempo": 20, "accent": 16, "volume": 7}
    kpr_sysex = {"header": "F0 42 00 00", "device_id_byte": 2, "commands": {"sync": "F8"}}
    kpr_banks = [{"name": "Preset Rhythm Patterns", "type": "ROM", "size": 48}]
    kpr_presets = []
    for i in range(48):
        kpr_presets.append({"name": f"KPR-77 Rhythm Pattern #{i+1:02d}", "bank": "Preset Rhythm Patterns", "number": i + 1, "category": "Pattern", "tags": ["korg", "kpr-77", "programmable rhythm", "analog drums", "vintage"]})
    write_synth("korg", "kpr-77", "KPR-77", "Programmable Rhythm Box", 1982, kpr_cc, kpr_sysex, kpr_banks, kpr_presets)

    # =========================================================================
    # 30. ALESIS SR-16 (16-Bit Stereo Drum Machine Classic)
    # =========================================================================
    sr16_cc = {"volume": 7, "pan": 10, "decay": 72, "pitch": 16}
    sr16_sysex = {"header": "F0 00 00 0E 03", "device_id_byte": 2, "commands": {"request_kit": "F0 00 00 0E 03 01 [kit] F7"}}
    sr16_banks = [{"name": "Preset Drum Kits", "type": "ROM", "size": 50}, {"name": "Preset Rhythm Patterns", "type": "ROM", "size": 50}]
    sr16_presets = []
    for i in range(50):
        sr16_pool = ["Studio Acoustic Kit", "Stadium Rock Gated Kit", "Electro Rap 808/909", "Brush Jazz Ballad", "Latin World Percussion"]
        base = sr16_pool[i % len(sr16_pool)]
        sr16_presets.append({"name": f"SR16 {base} #{i+1:02d}", "bank": "Preset Drum Kits", "number": i + 1, "category": "Drums", "tags": ["alesis", "sr-16", "16-bit", "dynamic articulation", "classic"]})
    for i in range(50):
        sr16_presets.append({"name": f"SR16 Pattern Groove {i+1:02d}", "bank": "Preset Rhythm Patterns", "number": i + 1, "category": "Pattern", "tags": ["alesis", "sr-16", "pattern", "groove"]})
    write_synth("alesis", "sr-16", "SR-16", "16-Bit Stereo Drum Machine", 1990, sr16_cc, sr16_sysex, sr16_banks, sr16_presets)

    print("\nWave 13 Build Complete! 30 new rhythm & studio instruments created.")

if __name__ == "__main__":
    build_wave13()
