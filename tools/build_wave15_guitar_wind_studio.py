#!/usr/bin/env python3
"""
Wave 15 Guitar Synthesizers, Wind Modeling & Studio Pro Processors Generator for OmniPatch:
- Roland Guitar Synths & V-Guitar Modeling: GR-55, GR-33, GR-20, GR-30, GR-09, GR-1, VG-99, VG-88, VG-8, GI-20
- Boss Guitar Synthesizers: SY-300, SY-1000, GP-10
- Akai Wind Instruments: EWI4000S, EWI5000
- Yamaha Wind & Physical Modeling: VL70-m, WT11, WX5
- Line 6 Studio Pro Rack Processors: POD Pro, Bass POD Pro, Echo Pro, Mod Pro, Filter Pro, POD XT Pro
- DigiTech Studio Harmonizers & Processors: IPS-33B, Whammy 5, Vocalist Workstation, TSR-24S, Studio 400
- TC-Helicon: VoiceLive
Creates profile.yaml and factory_presets.json for 30 specialized instruments.
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

def build_wave15():
    print("Building Wave 15: Guitar Synths, Wind Modeling & Studio Pro Processors (30 Instruments)...")

    # =========================================================================
    # 1. ROLAND GR-55 (Guitar Synthesizer & COSM Modeling Flagship)
    # =========================================================================
    gr55_cc = {"volume": 7, "pan": 10, "expression": 11, "ctl_pedal": 80, "pcm1_level": 16, "pcm2_level": 17, "cosm_level": 18}
    gr55_sysex = {"header": "F0 41 10 00 00 53 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 53 11 [addr] [size] [chk] F7"}}
    gr55_banks = [{"name": "Lead Presets", "type": "ROM", "size": 90}, {"name": "Rhythm Presets", "type": "ROM", "size": 90}, {"name": "Other Presets", "type": "ROM", "size": 90}]
    gr55_presets = []
    for bname in ["Lead Presets", "Rhythm Presets", "Other Presets"]:
        for i in range(90):
            g_pool = ["Screaming GR Solo Lead", "Full Concert Grand Guitar", "Dual PCM Warm Pad", "Sitar & Drone String", "Jazz Archtop & Organ",
                      "Heavy Modern High-Gain Stack", "Acoustic 12-String & Choir", "Vintage Analog Saw Solo", "Fat Sub Pulse Bass", "GR-55 Signature Evolution"]
            base = g_pool[i % len(g_pool)]
            gr55_presets.append({"name": f"GR55 {base} #{i+1:02d}", "bank": bname, "number": i + 1, "category": "Lead" if "Lead" in base or "Solo" in base else "Pad" if "Pad" in base else "Guitar", "tags": ["roland", "gr-55", "guitar synthesizer", "cosm", "pcm"]})
    write_synth("roland", "gr-55", "GR-55", "Guitar Synthesizer & COSM Modeler", 2011, gr55_cc, gr55_sysex, gr55_banks, gr55_presets)

    # =========================================================================
    # 2. ROLAND GR-33 (Guitar Synthesizer)
    # =========================================================================
    gr33_cc = {"volume": 7, "pan": 10, "expression": 11, "cutoff": 74, "resonance": 71}
    gr33_sysex = {"header": "F0 41 10 00 1E 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 1E 11 [addr] [size] [chk] F7"}}
    gr33_banks = [{"name": "Preset Bank 1", "type": "ROM", "size": 64}, {"name": "Preset Bank 2", "type": "ROM", "size": 64}]
    gr33_presets = []
    for b in range(2):
        bname = f"Preset Bank {b+1}"
        for i in range(64):
            gr33_presets.append({"name": f"GR33 Voice B{b+1}-{i+1:02d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["roland", "gr-33", "guitar synth", "arpeggiator"]})
    write_synth("roland", "gr-33", "GR-33", "Guitar Synthesizer with Arpeggiator", 2000, gr33_cc, gr33_sysex, gr33_banks, gr33_presets)

    # =========================================================================
    # 3. ROLAND GR-20 (Quick Access Guitar Synthesizer)
    # =========================================================================
    gr20_cc = {"volume": 7, "expression": 11, "glide": 5}
    gr20_sysex = {"header": "F0 41 10 00 6D 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 6D 11 [addr] [size] [chk] F7"}}
    gr20_banks = [{"name": "Lead Bank", "type": "ROM", "size": 50}, {"name": "Strings/Pad Bank", "type": "ROM", "size": 50}]
    gr20_presets = []
    for bname in ["Lead Bank", "Strings/Pad Bank"]:
        for i in range(50):
            gr20_presets.append({"name": f"GR20 Sound #{i+1:02d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["roland", "gr-20", "guitar synth"]})
    write_synth("roland", "gr-20", "GR-20", "Quick Access Guitar Synthesizer", 2004, gr20_cc, gr20_sysex, gr20_banks, gr20_presets)

    # =========================================================================
    # 4. ROLAND GR-30 (Guitar Synthesizer)
    # =========================================================================
    gr30_cc = {"volume": 7, "pan": 10, "expression": 11, "cutoff": 74}
    gr30_sysex = {"header": "F0 41 10 00 03 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 03 11 [addr] [size] [chk] F7"}}
    gr30_banks = [{"name": "Preset Patches", "type": "ROM", "size": 128}]
    gr30_presets = []
    for i in range(128):
        gr30_presets.append({"name": f"GR30 Patch #{i+1:03d}", "bank": "Preset Patches", "number": i + 1, "category": "Synth", "tags": ["roland", "gr-30", "guitar synth", "vintage"]})
    write_synth("roland", "gr-30", "GR-30", "Guitar Synthesizer", 1997, gr30_cc, gr30_sysex, gr30_banks, gr30_presets)

    # =========================================================================
    # 5. ROLAND GR-09 (Compact Guitar Synthesizer)
    # =========================================================================
    gr09_cc = {"volume": 7, "pan": 10, "expression": 11}
    gr09_sysex = {"header": "F0 41 10 57 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 57 11 [addr] [size] [chk] F7"}}
    gr09_banks = [{"name": "Factory Sounds", "type": "ROM", "size": 128}]
    gr09_presets = []
    for i in range(128):
        gr09_presets.append({"name": f"GR09 Tone #{i+1:03d}", "bank": "Factory Sounds", "number": i + 1, "category": "Synth", "tags": ["roland", "gr-09", "guitar synth", "90s"]})
    write_synth("roland", "gr-09", "GR-09", "Guitar Synthesizer Module", 1994, gr09_cc, gr09_sysex, gr09_banks, gr09_presets)

    # =========================================================================
    # 6. ROLAND GR-1 (Vintage Integrated Guitar Synthesizer)
    # =========================================================================
    gr1_cc = {"volume": 7, "pan": 10, "expression": 11}
    gr1_sysex = {"header": "F0 41 10 4F 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 4F 11 [addr] [size] [chk] F7"}}
    gr1_banks = [{"name": "Preset Tone Bank", "type": "ROM", "size": 64}]
    gr1_presets = []
    for i in range(64):
        gr1_presets.append({"name": f"GR-1 Tone #{i+1:02d}", "bank": "Preset Tone Bank", "number": i + 1, "category": "Synth", "tags": ["roland", "gr-1", "vintage guitar synth", "first digital gr"]})
    write_synth("roland", "gr-1", "GR-1", "Guitar Synthesizer with Internal Sound", 1992, gr1_cc, gr1_sysex, gr1_banks, gr1_presets)

    # =========================================================================
    # 7. ROLAND VG-99 (Dual COSM Modeling Guitar System)
    # =========================================================================
    vg99_cc = {"expression": 11, "d_beam": 16, "ribbon": 17, "ctrl1": 80, "ctrl2": 81}
    vg99_sysex = {"header": "F0 41 10 00 00 24 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 24 11 [addr] [size] [chk] F7"}}
    vg99_banks = [{"name": "COSM Preset Bank 1", "type": "ROM", "size": 100}, {"name": "COSM Preset Bank 2", "type": "ROM", "size": 100}]
    vg99_presets = []
    for b in range(2):
        bname = f"COSM Preset Bank {b+1}"
        for i in range(100):
            vg_pool = ["Vintage 1959 Les Paul Stack", "60s Strat Clean Twin", "Acoustic Dreadnought 12-Str", "Nylon Classical Elegance",
                       "GR-300 Analog Poly Lead", "Bow Cello Soundscape", "12-String Rick Ringer", "Resonator Dobro Slide", "Stereo Poly Dual Amp Solo"]
            base = vg_pool[i % len(vg_pool)]
            vg99_presets.append({"name": f"VG99 {base} #{i+1:02d}", "bank": bname, "number": i + 1, "category": "Modeling", "tags": ["roland", "vg-99", "v-guitar", "cosm", "gr-300"]})
    write_synth("roland", "vg-99", "VG-99", "Dual COSM Guitar Modeling System", 2007, vg99_cc, vg99_sysex, vg99_banks, vg99_presets)

    # =========================================================================
    # 8. ROLAND VG-88 (COSM Guitar System)
    # =========================================================================
    vg88_cc = {"expression": 11, "ctrl1": 80, "ctrl2": 81}
    vg88_sysex = {"header": "F0 41 10 00 29 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 29 11 [addr] [size] [chk] F7"}}
    vg88_banks = [{"name": "Preset Memory", "type": "ROM", "size": 160}]
    vg88_presets = []
    for i in range(160):
        vg88_presets.append({"name": f"VG88 COSM Patch #{i+1:03d}", "bank": "Preset Memory", "number": i + 1, "category": "Modeling", "tags": ["roland", "vg-88", "v-guitar", "cosm"]})
    write_synth("roland", "vg-88", "VG-88", "V-Guitar System", 2000, vg88_cc, vg88_sysex, vg88_banks, vg88_presets)

    # =========================================================================
    # 9. ROLAND VG-8 (The Original 1995 V-Guitar System)
    # =========================================================================
    vg8_cc = {"expression": 11, "ctrl1": 80}
    vg8_sysex = {"header": "F0 41 10 65 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 65 11 [addr] [size] [chk] F7"}}
    vg8_banks = [{"name": "Preset Bank", "type": "ROM", "size": 64}]
    vg8_presets = []
    for i in range(64):
        vg8_presets.append({"name": f"VG-8 Classic Patch #{i+1:02d}", "bank": "Preset Bank", "number": i + 1, "category": "Modeling", "tags": ["roland", "vg-8", "first v-guitar", "cosm pioneer"]})
    write_synth("roland", "vg-8", "VG-8", "Original V-Guitar Modeling System", 1995, vg8_cc, vg8_sysex, vg8_banks, vg8_presets)

    # =========================================================================
    # 10. ROLAND GI-20 (GK-MIDI Interface)
    # =========================================================================
    gi20_cc = {"volume": 7, "pan": 10, "pitch_bend": 0}
    gi20_sysex = {"header": "F0 41 10 00 59 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 59 11 [addr] [size] [chk] F7"}}
    gi20_banks = [{"name": "Memory Patches", "type": "RAM", "size": 50}]
    gi20_presets = []
    for i in range(50):
        gi20_presets.append({"name": f"GI20 MIDI Setup #{i+1:02d}", "bank": "Memory Patches", "number": i + 1, "category": "Utility", "tags": ["roland", "gi-20", "gk-midi", "guitar to midi"]})
    write_synth("roland", "gi-20", "GI-20", "GK-MIDI Guitar Interface", 2003, gi20_cc, gi20_sysex, gi20_banks, gi20_presets)

    # =========================================================================
    # 11. BOSS SY-300 (Polyphonic Guitar Synthesizer - Standard 1/4\" Input)
    # =========================================================================
    sy3_cc = {"cutoff": 74, "resonance": 71, "expression": 11, "ctl1": 80, "ctl2": 81, "ctl3": 82}
    sy3_sysex = {"header": "F0 41 10 00 00 00 0A 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 00 0A 11 [addr] [size] [chk] F7"}}
    sy3_banks = [{"name": "Preset Patches", "type": "ROM", "size": 70}, {"name": "User Patches", "type": "RAM", "size": 99}]
    sy3_presets = []
    sy3_pool = ["Fat Analog Saw Solo", "Pulse Width Synth Brass", "Resonant Sweep Pad", "Sub Sonic Bassline", "80s Polysynth Chords",
                "Laser Beam Arp Sound", "Ambient Shimmer Swell", "Ring Mod Sci-Fi Noise", "Octave Lead Screamer", "SY-300 Modern Anthem"]
    for i in range(70):
        base = sy3_pool[i % len(sy3_pool)]
        sy3_presets.append({"name": f"SY300 {base} #{i+1:02d}", "bank": "Preset Patches", "number": i + 1, "category": "Lead" if "Lead" in base or "Solo" in base else "Pad" if "Pad" in base or "Swell" in base else "Synth", "tags": ["boss", "sy-300", "polyphonic", "analog modeling", "no pickup required"]})
    for i in range(99):
        sy3_presets.append({"name": f"SY300 User Sound #{i+1:02d}", "bank": "User Patches", "number": i + 1, "category": "Synth", "tags": ["boss", "sy-300", "user"]})
    write_synth("boss", "sy-300", "SY-300", "Polyphonic Guitar Synthesizer", 2015, sy3_cc, sy3_sysex, sy3_banks, sy3_presets)

    # =========================================================================
    # 12. BOSS SY-1000 (Flagship Guitar Synthesizer & Modeling Processor)
    # =========================================================================
    sy1k_cc = {"expression": 11, "ctl1": 80, "ctl2": 81, "cutoff": 74, "resonance": 71}
    sy1k_sysex = {"header": "F0 41 10 00 00 00 68 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 00 68 11 [addr] [size] [chk] F7"}}
    sy1k_banks = [{"name": "Preset Sound Bank", "type": "ROM", "size": 100}, {"name": "User Sound Bank", "type": "RAM", "size": 100}]
    sy1k_presets = []
    for bname in ["Preset Sound Bank", "User Sound Bank"]:
        for i in range(100):
            sy1k_presets.append({"name": f"SY1000 Flagship #{i+1:03d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["boss", "sy-1000", "flagship guitar synth", "dynamic synth"]})
    write_synth("boss", "sy-1000", "SY-1000", "Guitar Synthesizer & Modeling Processor", 2020, sy1k_cc, sy1k_sysex, sy1k_banks, sy1k_presets)

    # =========================================================================
    # 13. BOSS GP-10 (Guitar Processor w/ COSM & Analog Modeling)
    # =========================================================================
    gp10_cc = {"expression": 11, "ctl": 80}
    gp10_sysex = {"header": "F0 41 10 00 00 7A 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 7A 11 [addr] [size] [chk] F7"}}
    gp10_banks = [{"name": "Preset Patches", "type": "ROM", "size": 99}]
    gp10_presets = []
    for i in range(99):
        gp10_presets.append({"name": f"GP10 Sound #{i+1:02d}", "bank": "Preset Patches", "number": i + 1, "category": "Modeling", "tags": ["boss", "gp-10", "cosm", "analog modeling"]})
    write_synth("boss", "gp-10", "GP-10", "Guitar Processor with Synth & Modeling", 2014, gp10_cc, gp10_sysex, gp10_banks, gp10_presets)

    # =========================================================================
    # 14. AKAI EWI4000S (Electronic Wind Instrument w/ Built-in Analog Modeling)
    # =========================================================================
    ewi4_cc = {"breath_ctrl": 2, "pitch_bend": 0, "glide": 5, "volume": 7, "pan": 10, "mod_wheel": 1}
    ewi4_sysex = {"header": "F0 47 00 5D", "device_id_byte": 2, "commands": {"request_patch": "F0 47 00 5D 40 [prog] F7"}}
    ewi4_banks = [{"name": "Internal Preset Sounds", "type": "ROM", "size": 100}]
    ewi4_presets = []
    ewi_names = [
        "Michael Brecker Lead", "Sweet Soprano Sax", "Warm Analog Brass", "Breathy Pan Flute", "Ocarina Melody",
        "Harmonica Blues Solo", "Dual Saw Sync Screamer", "Sub Octave Pulse Bass", "Fifth Interval Horn", "Space Flute Chiff",
        "Distorted Rock Lead", "Velvet Cello Solo", "Trumpet Mute Jazz", "Clarinet Classic", "Oboe Soloist",
        "Fat Moog Saw Lead", "Vocal Formant Whistle", "Analog Reso Sweep", "EWI Signature Poly", "Wind Controller Master"
    ]
    for i in range(100):
        base = ewi_names[i % len(ewi_names)]
        ewi4_presets.append({"name": f"EWI4K {base} #{i+1:02d}", "bank": "Internal Preset Sounds", "number": i + 1, "category": "Wind", "tags": ["akai", "ewi4000s", "wind controller", "analog modeling", "brecker"]})
    write_synth("akai", "ewi4000s", "EWI4000S", "Electronic Wind Instrument Synthesizer", 2006, ewi4_cc, ewi4_sysex, ewi4_banks, ewi4_presets)

    # =========================================================================
    # 15. AKAI EWI5000 (Wireless Electronic Wind Instrument w/ 3GB Library)
    # =========================================================================
    ewi5_cc = {"breath_ctrl": 2, "pitch_bend": 0, "glide": 5, "volume": 7, "reverb": 91, "chorus": 93}
    ewi5_sysex = {"header": "F0 47 00 7B", "device_id_byte": 2, "commands": {"request_patch": "F0 47 00 7B 40 [prog] F7"}}
    ewi5_banks = [{"name": "Acoustic & Synth Bank", "type": "ROM", "size": 100}]
    ewi5_presets = []
    for i in range(100):
        ewi5_presets.append({"name": f"EWI5K Sound #{i+1:03d}", "bank": "Acoustic & Synth Bank", "number": i + 1, "category": "Wind", "tags": ["akai", "ewi5000", "wireless", "sonivox library"]})
    write_synth("akai", "ewi5000", "EWI5000", "Wireless Electronic Wind Instrument", 2014, ewi5_cc, ewi5_sysex, ewi5_banks, ewi5_presets)

    # =========================================================================
    # 16. YAMAHA VL70-m (Virtual Acoustic Physical Modeling Tone Generator)
    # =========================================================================
    vl70_cc = {"breath_ctrl": 2, "pitch_bend": 0, "volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "variation": 94}
    vl70_sysex = {"header": "F0 43 10 57", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 57 00 [bank] [prog] F7"}}
    vl70_banks = [{"name": "Custom Physical Models", "type": "ROM", "size": 128}, {"name": "Internal Models", "type": "ROM", "size": 128}]
    vl70_presets = []
    vl_names = [
        "Soprano Sax Breathy", "Tenor Sax Growl", "Alto Sax Vibrato", "Concert Flute Air", "Pan Flute Chiff",
        "Clarinet Wood", "Oboe Soloist", "Bassoon Low", "Trumpet Harmon Mute", "Trombone Slur",
        "French Horn Mellow", "Tuba Deep", "Shakuhachi Bamboo", "Bagpipes Celtic", "Bowed Cello Expressive",
        "Violin Virtuoso", "Acoustic Guitar Nylon", "Distorted Lead Guitar", "Resonant Pipe Drone", "VL-70m Signature Wind"
    ]
    for b, bname in enumerate(["Custom Physical Models", "Internal Models"]):
        for i in range(128):
            base = vl_names[i % len(vl_names)]
            vl70_presets.append({"name": f"VL70m {base} B{b+1}-{i+1:03d}", "bank": bname, "number": i + 1, "category": "Physical Modeling", "tags": ["yamaha", "vl70-m", "virtual acoustic", "physical modeling", "wind"]})
    write_synth("yamaha", "vl70-m", "VL70-m", "Virtual Acoustic Tone Generator", 1996, vl70_cc, vl70_sysex, vl70_banks, vl70_presets)

    # =========================================================================
    # 17. YAMAHA WT11 (Wind Tone Generator - 4-Operator FM)
    # =========================================================================
    wt11_cc = {"breath_ctrl": 2, "pitch_bend": 0, "volume": 7, "pan": 10}
    wt11_sysex = {"header": "F0 43 10 23", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 23 00 [voice] F7"}}
    wt11_banks = [{"name": "Preset Internal Voices", "type": "ROM", "size": 128}]
    wt11_presets = []
    for i in range(128):
        wt11_presets.append({"name": f"WT11 Wind FM Voice #{i+1:03d}", "bank": "Preset Internal Voices", "number": i + 1, "category": "Wind", "tags": ["yamaha", "wt11", "wx7", "wx11", "fm wind"]})
    write_synth("yamaha", "wt11", "WT11", "Wind Tone Generator (4-Op FM)", 1988, wt11_cc, wt11_sysex, wt11_banks, wt11_presets)

    # =========================================================================
    # 18. YAMAHA WX5 (Wind MIDI Controller)
    # =========================================================================
    wx5_cc = {"breath_ctrl": 2, "pitch_bend": 0, "mod_wheel": 1, "volume": 7}
    wx5_sysex = {"header": "F0 43 00 00", "device_id_byte": 2, "commands": {"sync": "F8"}}
    wx5_banks = [{"name": "Controller Setups", "type": "ROM", "size": 16}]
    wx5_presets = []
    for i in range(16):
        wx5_presets.append({"name": f"WX5 Lip/Breath Setup #{i+1:02d}", "bank": "Controller Setups", "number": i + 1, "category": "Utility", "tags": ["yamaha", "wx5", "wind controller", "midi wind"]})
    write_synth("yamaha", "wx5", "WX5", "Wind MIDI Controller", 1998, wx5_cc, wx5_sysex, wx5_banks, wx5_presets)

    # =========================================================================
    # 19. LINE 6 POD PRO (Professional Rackmount Guitar Amp Modeler)
    # =========================================================================
    podp_cc = {"drive": 80, "bass": 81, "mid": 82, "treble": 83, "presence": 84, "volume": 7, "delay_mix": 91}
    podp_sysex = {"header": "F0 00 01 0C 03", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 03 00 [prog] F7"}}
    podp_banks = [{"name": "Preset Channel Bank", "type": "ROM", "size": 36}, {"name": "User Program Bank", "type": "RAM", "size": 128}]
    podp_presets = []
    pod_names = [
        "Small Tweed 1952", "Tweed Blues Deluxe", "Blackface Twin 1965", "Tweed 4x10 Bassman", "Vox AC-30 Top Boost",
        "Marshall JTM-45 1968", "Marshall Plexi 50W", "Marshall JCM-800 1981", "Soldano SLO-100 Lead", "Mesa Boogie Dual Rectifier",
        "Roland JC-120 Jazz Clean", "Dumble Overdrive Special", "Matchless Chieftain", "Line 6 Insane Distortion"
    ]
    for i in range(36):
        base = pod_names[i % len(pod_names)]
        podp_presets.append({"name": f"POD Pro {base} #{i+1:02d}", "bank": "Preset Channel Bank", "number": i + 1, "category": "Guitar", "tags": ["line6", "pod-pro", "rackmount", "amp modeling"]})
    for i in range(128):
        podp_presets.append({"name": f"POD Pro User Memory #{i+1:03d}", "bank": "User Program Bank", "number": i + 1, "category": "Guitar", "tags": ["line6", "pod-pro", "user"]})
    write_synth("line6", "pod-pro", "POD Pro", "Professional Rackmount Guitar Amp Modeler", 2000, podp_cc, podp_sysex, podp_banks, podp_presets)

    # =========================================================================
    # 20. LINE 6 BASS POD PRO (Professional Rackmount Bass Modeler)
    # =========================================================================
    bpod_cc = {"drive": 80, "bass": 81, "mid": 82, "treble": 83, "compressor": 84, "volume": 7}
    bpod_sysex = {"header": "F0 00 01 0C 04", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 04 00 [prog] F7"}}
    bpod_banks = [{"name": "Factory Bass Presets", "type": "ROM", "size": 64}]
    bpod_presets = []
    for i in range(64):
        bpod_presets.append({"name": f"Bass POD Pro Rig #{i+1:02d}", "bank": "Factory Bass Presets", "number": i + 1, "category": "Bass", "tags": ["line6", "bass-pod-pro", "ampeg svt", "bass modeler"]})
    write_synth("line6", "bass-pod-pro", "Bass POD Pro", "Professional Bass Amp Modeler", 2001, bpod_cc, bpod_sysex, bpod_banks, bpod_presets)

    # =========================================================================
    # 21. LINE 6 ECHO PRO (Studio Rackmount Delay Modeler)
    # =========================================================================
    echo_cc = {"time": 16, "repeats": 17, "tweak": 18, "tweez": 19, "mix": 91}
    echo_sysex = {"header": "F0 00 01 0C 07", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 07 00 [prog] F7"}}
    echo_banks = [{"name": "Preset Echo Bank", "type": "ROM", "size": 128}]
    echo_presets = []
    echo_pool = ["EP-1 Tube Echoplex Warm", "EP-3 Solid State Tape Delay", "Space Echo Multi-Head", "Deluxe Memory Man Analog Chorus",
                 "Reverse Delay Dreamscape", "Sweep Echo Filter Modulation", "Ping Pong Stereo Delay", "Dynamic Delay Ducking",
                 "Lo-Res 8-Bit Digital Delay", "Stereo Multi-Tap Rhythm Delay"]
    for i in range(128):
        base = echo_pool[i % len(echo_pool)]
        echo_presets.append({"name": f"EchoPro {base} #{i+1:03d}", "bank": "Preset Echo Bank", "number": i + 1, "category": "FX", "tags": ["line6", "echo-pro", "tape delay", "studio rack"]})
    write_synth("line6", "echo-pro", "Echo Pro", "Studio Modeling Delay Processor", 2001, echo_cc, echo_sysex, echo_banks, echo_presets)

    # =========================================================================
    # 22. LINE 6 MOD PRO (Studio Rackmount Modulation Modeler)
    # =========================================================================
    modp_cc = {"speed": 16, "depth": 17, "tweak": 18, "tweez": 19, "mix": 91}
    modp_sysex = {"header": "F0 00 01 0C 08", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 08 00 [prog] F7"}}
    modp_banks = [{"name": "Preset Mod Bank", "type": "ROM", "size": 128}]
    modp_presets = []
    mod_pool = ["CE-1 Classic Chorus Ensemble", "Dimension Stereo Spatializer", "Script Logo Phase 90", "Bi-Phase Dual Modulation",
                "A/DA Stereo Flanger", "Rotary Speaker Leslie 145", "Uni-Vibe Psychedelic Swirl", "Opto Tremolo Fender Twin",
                "Bias Tremolo Vox AC-15", "Panner Stereo Circular Sweep"]
    for i in range(128):
        base = mod_pool[i % len(mod_pool)]
        modp_presets.append({"name": f"ModPro {base} #{i+1:03d}", "bank": "Preset Mod Bank", "number": i + 1, "category": "FX", "tags": ["line6", "mod-pro", "modulation", "chorus", "flanger"]})
    write_synth("line6", "mod-pro", "Mod Pro", "Studio Modeling Modulation Processor", 2001, modp_cc, modp_sysex, modp_banks, modp_presets)

    # =========================================================================
    # 23. LINE 6 FILTER PRO (Studio Rackmount Filter Modeler)
    # =========================================================================
    filt_cc = {"frequency": 16, "q_resonance": 17, "speed": 18, "mix": 91}
    filt_sysex = {"header": "F0 00 01 0C 09", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 09 00 [prog] F7"}}
    filt_banks = [{"name": "Preset Filter Bank", "type": "ROM", "size": 128}]
    filt_presets = []
    filt_pool = ["Mu-Tron III Envelope Follower", "Z-Vex Seek-Wah Step Filter", "Oberheim Voltage Controlled Filter", "Voice Box Vowel Modulator",
                 "Moog 4-Pole Lowpass Sweep", "Korg Dual Filter Resonator", "Auto Wah Funk Pluck", "Sample and Hold Random Filter",
                 "Octave Synth Subharmonic", "FilterPro Synth Texture Drone"]
    for i in range(128):
        base = filt_pool[i % len(filt_pool)]
        filt_presets.append({"name": f"FilterPro {base} #{i+1:03d}", "bank": "Preset Filter Bank", "number": i + 1, "category": "FX", "tags": ["line6", "filter-pro", "envelope filter", "mutron", "synth filter"]})
    write_synth("line6", "filter-pro", "Filter Pro", "Studio Modeling Filter Processor", 2001, filt_cc, filt_sysex, filt_banks, filt_presets)

    # =========================================================================
    # 24. LINE 6 POD XT PRO (24-bit Studio Rack Modeler)
    # =========================================================================
    xt_cc = {"drive": 80, "bass": 81, "mid": 82, "treble": 83, "presence": 84, "volume": 7, "reverb": 91}
    xt_sysex = {"header": "F0 00 01 0C 0A", "device_id_byte": 2, "commands": {"request_program": "F0 00 01 0C 0A 00 [prog] F7"}}
    xt_banks = [{"name": "Preset Channels", "type": "ROM", "size": 128}]
    xt_presets = []
    for i in range(128):
        xt_presets.append({"name": f"POD XT Pro Channel #{i+1:03d}", "bank": "Preset Channels", "number": i + 1, "category": "Guitar", "tags": ["line6", "pod-xt-pro", "24-bit", "amp modeler"]})
    write_synth("line6", "pod-xt-pro", "POD XT Pro", "24-Bit Studio Rack Amp Modeler", 2003, xt_cc, xt_sysex, xt_banks, xt_presets)

    # =========================================================================
    # 25. DIGITECH IPS-33B (Super Harmony Machine)
    # =========================================================================
    ips_cc = {"harmony_interval": 16, "pitch_detune": 17, "mix": 91, "bypass": 84}
    ips_sysex = {"header": "F0 00 00 1A", "device_id_byte": 2, "commands": {"request_program": "F0 00 00 1A 01 [prog] F7"}}
    ips_banks = [{"name": "Intelligent Harmony Presets", "type": "ROM", "size": 99}]
    ips_presets = []
    ips_pool = ["Diatonic 3rd & 5th Solo", "Octave Doubler Fat", "Micro Pitch Detune Stereo", "Major Scale Harmonizer",
                "Minor Scale Harmonizer", "Pitch Shift Whammy Dive", "Arpeggiated Pitch Sequence", "IPS-33B Studio Vocal Double"]
    for i in range(99):
        base = ips_pool[i % len(ips_pool)]
        ips_presets.append({"name": f"IPS33B {base} #{i+1:02d}", "bank": "Intelligent Harmony Presets", "number": i + 1, "category": "Pitch", "tags": ["digitech", "ips-33b", "intelligent harmony", "pitch shifter", "vai"]})
    write_synth("digitech", "ips-33b", "IPS-33B", "Super Harmony Machine", 1989, ips_cc, ips_sysex, ips_banks, ips_presets)

    # =========================================================================
    # 26. DIGITECH WHAMMY 5 (Definitive Whammy Pedal w/ MIDI Control)
    # =========================================================================
    wham_cc = {"expression": 11, "pedal_pos": 16, "bypass": 84}
    wham_sysex = {"header": "F0 00 00 1A 05", "device_id_byte": 2, "commands": {"request_program": "F0 00 00 1A 05 01 [prog] F7"}}
    wham_banks = [{"name": "Whammy Mode Presets", "type": "ROM", "size": 22}]
    wham_presets = []
    wham_modes = [
        "2 Octaves Up Dive/Rise", "1 Octave Up Lead", "1 Octave Down Deep", "2 Octaves Down Sub", "Dive Bomb Deep",
        "Drop Tune -1 Semitone", "Drop Tune -2 Semitones", "Drop Tune -3 Semitones", "Drop Tune -4 Semitones", "Drop Tune -5 Semitones",
        "Drop Tune -6 Semitones", "Drop Tune 1 Octave Down", "Octave Up / Octave Down Dual", "Harmony Octave Up / Octave Down",
        "Harmony 5th Down / 4th Down", "Harmony 4th Down / 3rd Down", "Harmony 5th Up / 6th Up", "Harmony 5th Up / 7th Up",
        "Harmony 4th Up / 5th Up", "Harmony 3rd Up / 4th Up", "Detune Shallow Chorus", "Detune Deep Chorus"
    ]
    for i, name in enumerate(wham_modes):
        wham_presets.append({"name": f"Whammy5 {name}", "bank": "Whammy Mode Presets", "number": i + 1, "category": "Pitch", "tags": ["digitech", "whammy-5", "pitch shifter", "morello", "midi"]})
    write_synth("digitech", "whammy-5", "Whammy (V5)", "Pitch-Shifting MIDI Pedal", 2012, wham_cc, wham_sysex, wham_banks, wham_presets)

    # =========================================================================
    # 27. DIGITECH VOCALIST WORKSTATION (Multi-Voice Vocal Harmonizer)
    # =========================================================================
    voc_cc = {"lead_level": 7, "harmony_level": 8, "reverb": 91, "chorus": 93}
    voc_sysex = {"header": "F0 00 00 1A 02", "device_id_byte": 2, "commands": {"request_patch": "F0 00 00 1A 02 01 [patch] F7"}}
    voc_banks = [{"name": "Preset Vocal Harmonies", "type": "ROM", "size": 50}]
    voc_presets = []
    for i in range(50):
        voc_presets.append({"name": f"Vocalist Harmony Setup #{i+1:02d}", "bank": "Preset Vocal Harmonies", "number": i + 1, "category": "Vocal", "tags": ["digitech", "vocalist", "vocal harmony", "pitch correction"]})
    write_synth("digitech", "vocalist-workstation", "Vocalist Workstation", "Multi-Voice Vocal Harmonizer", 1996, voc_cc, voc_sysex, voc_banks, voc_presets)

    # =========================================================================
    # 28. DIGITECH TSR-24S (True Stereo Reverb & Multi-Effects)
    # =========================================================================
    tsr_cc = {"mix": 91, "bypass": 84, "modifier1": 16, "modifier2": 17}
    tsr_sysex = {"header": "F0 00 00 1A 03", "device_id_byte": 2, "commands": {"request_program": "F0 00 00 1A 03 01 [prog] F7"}}
    tsr_banks = [{"name": "Factory Algorithms", "type": "ROM", "size": 100}]
    tsr_presets = []
    for i in range(100):
        tsr_presets.append({"name": f"TSR24S Algorithm Preset #{i+1:02d}", "bank": "Factory Algorithms", "number": i + 1, "category": "FX", "tags": ["digitech", "tsr-24s", "true stereo", "multi-effects", "s-disc"]})
    write_synth("digitech", "tsr-24s", "TSR-24S", "True Stereo Multi-Effects Processor", 1994, tsr_cc, tsr_sysex, tsr_banks, tsr_presets)

    # =========================================================================
    # 29. DIGITECH STUDIO 400 (4-In / 4-Out Multi-Effects Processor)
    # =========================================================================
    s400_cc = {"mix": 91, "bypass": 84, "param1": 16, "param2": 17}
    s400_sysex = {"header": "F0 00 00 1A 04", "device_id_byte": 2, "commands": {"request_program": "F0 00 00 1A 04 01 [prog] F7"}}
    s400_banks = [{"name": "Studio 400 Factory Programs", "type": "ROM", "size": 100}]
    s400_presets = []
    for i in range(100):
        s400_presets.append({"name": f"Studio400 Multi-FX #{i+1:02d}", "bank": "Studio 400 Factory Programs", "number": i + 1, "category": "FX", "tags": ["digitech", "studio-400", "4-in 4-out", "dual s-disc"]})
    write_synth("digitech", "studio-400", "Studio 400", "4-In / 4-Out Multi-Effects Processor", 1997, s400_cc, s400_sysex, s400_banks, s400_presets)

    # =========================================================================
    # 30. TC-HELICON VOICELIVE (Vocal Processor & Harmonizer)
    # =========================================================================
    vl_cc = {"harmony_level": 16, "lead_level": 7, "reverb": 91, "delay": 92}
    vl_sysex = {"header": "F0 00 20 1F", "device_id_byte": 2, "commands": {"request_preset": "F0 00 20 1F 00 [preset] F7"}}
    vl_banks = [{"name": "Factory Vocal Presets", "type": "ROM", "size": 99}]
    vl_presets = []
    for i in range(99):
        vl_presets.append({"name": f"VoiceLive Harmony Setup #{i+1:02d}", "bank": "Factory Vocal Presets", "number": i + 1, "category": "Vocal", "tags": ["tc-helicon", "voicelive", "vocal harmonizer", "pitch correction"]})
    write_synth("tc_helicon", "voicelive", "VoiceLive", "Professional Vocal Effects Processor", 2004, vl_cc, vl_sysex, vl_banks, vl_presets)

    print("\nWave 15 Build Complete! 30 new guitar synth, wind & studio processors created.")

if __name__ == "__main__":
    build_wave15()
