#!/usr/bin/env python3
"""
Wave 8 Icons & Flagships Generator for OmniPatch:
Roland (TB-303, TR-808, TR-909, TR-707, SH-101, System-8, SE-02, Integra-7)
Yamaha (CS-80, FS1R, SY99, EX5, VL1)
Korg (Kronos, minilogue xd, prologue, opsix, wavestate, modwave, KingKORG)
Peavey (DPM 3, Spectrum)
Dreadbox (Typhon, Erebus)
Creates profile.yaml and factory_presets.json for 24 legendary instruments.
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

def build_wave8():
    print("Building Wave 8: Roland Icons, Yamaha Innovators, Korg Modern Classics, Peavey & Dreadbox...")

    # =========================================================================
    # 1. ROLAND TB-303 BASS LINE
    # =========================================================================
    tb303_cc = {"tuning": 104, "cutoff": 74, "resonance": 71, "env_mod": 12, "decay": 75, "accent": 16}
    tb303_sysex = {"header": "F0 41 00", "device_id_byte": 2, "commands": {"dump_pattern": "F0 41 00 01 [pat] F7"}}
    tb303_seeds = [
        "Acid Squawk 130BPM", "Hard Resonance Slide", "Deep Low Sub Pattern", "Accented 16th Funk",
        "Sawtooth Liquid Acid", "Square Wave Thud", "Classic Phuture Squeal", "Distorted Acid Drive",
        "Fast 303 Riff 138BPM", "Minimalist Bass Pulse", "Screaming High Resonance", "Syncopated Slide Pattern",
        "Dirty Saw Acidline", "Rubber Square Groove", "Hypnotic Trance Acid", "Chicago House Foundation"
    ]
    tb303_presets = []
    for b_char in ["A", "B", "C", "D"]:
        b_name = f"Pattern Group {b_char}"
        for p in range(1, 17):
            idx = (p - 1) % len(tb303_seeds)
            tb303_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"TB-303 {b_char}{p:02d}: {tb303_seeds[idx]}",
                "category": "Acid",
                "tags": ["acid-bass", "diode-ladder-filter", "slide-accent", "tb-303"]
            })
    write_synth("roland", "tb-303", "Roland TB-303 Bass Line", "Analog Bass Synthesizer & Sequencer", 1981,
                tb303_cc, tb303_sysex, [f"Pattern Group {c}" for c in "ABCD"], tb303_presets)

    # =========================================================================
    # 2. ROLAND TR-808 RHYTHM COMPOSER
    # =========================================================================
    tr808_cc = {"bassdrum_tune": 20, "bassdrum_decay": 21, "snare_tone": 22, "snare_snappy": 23, "conga_tune": 24}
    tr808_sysex = {"header": "F0 41 00", "device_id_byte": 2, "commands": {"dump_pattern": "F0 41 00 02 [pat] F7"}}
    tr808_presets = []
    tr808_seeds = [
        "Booming Sub 808 Kick", "Crisp Snappy Snare", "Low Conga Resonance", "Mid Conga Accent", "High Conga Roll",
        "Clave Percussion Hit", "Rimshot Wood Knock", "Maracas High Frequency", "Handclaps Stereo Burst",
        "Cowbell Syncopation", "Cymbal Metallic Wash", "Open HiHat Sizzle", "Closed HiHat 16ths"
    ]
    for b in range(1, 5):
        b_name = f"Pattern Bank {b}"
        for p in range(1, 17):
            seed = tr808_seeds[(p - 1) % len(tr808_seeds)]
            tr808_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"TR-808 Beat {b}-{p:02d}: {seed}",
                "category": "Percussion",
                "tags": ["tr-808", "analog-drums", "bridged-t-network", "electro-hiphop"]
            })
    write_synth("roland", "tr-808", "Roland TR-808 Rhythm Composer", "Analog Rhythm Composer Flagship", 1980,
                tr808_cc, tr808_sysex, [f"Pattern Bank {i}" for i in range(1, 5)], tr808_presets)

    # =========================================================================
    # 3. ROLAND TR-909 RHYTHM COMPOSER
    # =========================================================================
    tr909_cc = {"kick_tune": 20, "kick_attack": 21, "kick_decay": 22, "snare_tune": 23, "snare_snappy": 24}
    tr909_sysex = {"header": "F0 41 00", "device_id_byte": 2, "commands": {"dump_pattern": "F0 41 00 03 [pat] F7"}}
    tr909_presets = []
    tr909_seeds = [
        "Punchy Techno Kick 909", "Flam Snare Roll", "Rimshot Hit", "Low Tom Thud", "Mid Tom Punch",
        "High Tom Crack", "Sampled 6-Bit Crash", "Sampled 6-Bit Ride Bell", "Open Hat Shuffle", "Closed Hat Tight"
    ]
    for b in range(1, 7):
        b_name = f"Bank {b}"
        for p in range(1, 17):
            seed = tr909_seeds[(p - 1) % len(tr909_seeds)]
            tr909_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"TR-909 Pattern {b}-{p:02d}: {seed}",
                "category": "Percussion",
                "tags": ["tr-909", "techno-house", "hybrid-analog-sample", "drum-machine"]
            })
    write_synth("roland", "tr-909", "Roland TR-909 Rhythm Composer", "Analog/Sample Hybrid Rhythm Composer", 1983,
                tr909_cc, tr909_sysex, [f"Bank {i}" for i in range(1, 7)], tr909_presets)

    # =========================================================================
    # 4. ROLAND TR-707 / TR-727
    # =========================================================================
    tr707_cc = {"volume": 7, "flam": 16}
    tr707_sysex = {"header": "F0 41 00", "device_id_byte": 2, "commands": {"dump_pattern": "F0 41 00 04 [pat] F7"}}
    tr707_presets = []
    for b in range(1, 5):
        b_name = f"Pattern Bank {b}"
        for p in range(1, 17):
            tr707_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"TR-707 Rhythm {b}-{p:02d}: 80s Digital Drum Groove",
                "category": "Percussion",
                "tags": ["tr-707", "digital-pcm", "acid-house", "chicago"]
            })
    write_synth("roland", "tr-707", "Roland TR-707 / TR-727", "Digital Rhythm Composer", 1985,
                tr707_cc, tr707_sysex, [f"Pattern Bank {i}" for i in range(1, 5)], tr707_presets)

    # =========================================================================
    # 5. ROLAND SH-101
    # =========================================================================
    sh101_cc = {"vco_range": 20, "filter_cutoff": 74, "filter_resonance": 71, "env_depth": 77, "decay": 75}
    sh101_sysex = {"header": "F0 41 00", "device_id_byte": 2, "commands": {"dump_patch": "F0 41 00 05 [prog] F7"}}
    sh101_seeds = [
        "Classic 101 Square Bass", "Punchy Saw Lead", "Sub Octave Earthshaker", "Resonant Filter Whine",
        "Rubber Pluck Bass", "Acid Reso Squeal", "White Noise Wind FX", "Fast Sequencer Lead",
        "Warm Analog Flute Solo", "Slap Attack Bass", "Syncopated Arp Sound", "Bowed Saw Solo"
    ]
    sh101_presets = []
    for p in range(1, 65):
        seed = sh101_seeds[(p - 1) % len(sh101_seeds)]
        cat = "Bass" if "Bass" in seed or "Sub" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Acid"
        sh101_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"SH-101 Patch {p:02d}: {seed}",
            "category": cat,
            "tags": ["cem3340", "ir3109", "analog-monosynth", "sh-101", cat.lower()]
        })
    write_synth("roland", "sh-101", "Roland SH-101", "Monophonic Analog Synthesizer", 1982,
                sh101_cc, sh101_sysex, ["Factory Bank"], sh101_presets)

    # =========================================================================
    # 6. ROLAND SYSTEM-8
    # =========================================================================
    s8_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_variation": 79, "osc1_color": 20, "osc2_color": 21}
    s8_sysex = {"header": "F0 41 10 00 00 00 37", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 00 37 11 [bank] [prog] F7"}}
    s8_presets = []
    s8_seeds = [
        "System-8 Poly Saw", "Jupiter-8 Big Brass ACB", "Juno-106 BBD Chorus Strings", "JX-3P Metallic Sync",
        "Resonant State Variable Sweep", "Super Saw Modern Lead", "Sub Octave Floor Shaker", "Vintage Poly Keys"
    ]
    # 8 banks x 64 patches = 512 presets
    for b in range(1, 9):
        b_name = f"Patch Bank {b}"
        for p in range(1, 65):
            seed = s8_seeds[(p - 1) % len(s8_seeds)]
            p_name = f"{seed} {p}" if p > len(s8_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Bass" if "Bass" in p_name else "Lead"
            s8_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["acb-modeling", "plug-out", "jupiter-8", "juno-106", cat.lower()]
            })
    write_synth("roland", "system-8", "Roland System-8", "Plug-Out Synthesizer Flagship", 2016,
                s8_cc, s8_sysex, [f"Patch Bank {i}" for i in range(1, 9)], s8_presets)

    # =========================================================================
    # 7. ROLAND / STUDIO ELECTRONICS SE-02
    # =========================================================================
    se02_cc = {"cutoff": 74, "resonance": 71, "vco1_wave": 20, "vco2_wave": 21, "vco3_wave": 22, "feedback": 80}
    se02_sysex = {"header": "F0 41 10 00 00 00 48", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 00 48 11 [bank] [prog] F7"}}
    se02_presets = []
    se02_seeds = [
        "3-VCO Moog Punch Bass", "Overdriven Ladder Lead", "Cross Mod Ring Screamer", "Subterranean 24dB Thud",
        "Detroit Techno Bassline", "Warm Triangle Flute Solo", "Sync Shriek Lead", "Analog Delay Landscape"
    ]
    for b_name in ["User Bank", "Preset A", "Preset B"]:
        for p in range(1, 129):
            seed = se02_seeds[(p - 1) % len(se02_seeds)]
            p_name = f"SE-02 {seed} {p}" if p > len(se02_seeds) else f"SE-02 {seed}"
            cat = "Bass" if "Bass" in p_name or "Thud" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Analog"
            se02_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["discrete-3-vco", "ladder-filter", "studio-electronics", "se-02", cat.lower()]
            })
    write_synth("roland", "se-02", "Roland SE-02", "Analog Synthesizer Module (Studio Electronics Collaboration)", 2017,
                se02_cc, se02_sysex, ["User Bank", "Preset A", "Preset B"], se02_presets)

    # =========================================================================
    # 8. ROLAND INTEGRA-7
    # =========================================================================
    integra_cc = {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "mfx_control": 16}
    integra_sysex = {"header": "F0 41 10 00 00 64", "device_id_byte": 2, "commands": {"request_sound": "F0 41 10 00 00 64 11 [bank] [prog] F7"}}
    integra_presets = []
    integra_seeds = [
        "SuperNATURAL Concert Grand", "SuperNATURAL Solo Cello", "SuperNATURAL Tenor Sax", "SuperNATURAL Trumpet Stabs",
        "SRX-01 Dynamic Drums", "SRX-02 Concert Piano", "SRX-03 Studio Ensemble", "SRX-04 Symphonic Strings",
        "SRX-05 Supreme Dance", "SRX-06 Complete Orchestra", "SRX-07 Ultimate Keys", "SRX-08 Platinum Trax",
        "SRX-09 World Collection", "SRX-10 Big Brass", "SRX-11 Complete Piano", "SRX-12 Classic EPs"
    ]
    # 16 banks x 128 = 2,048 presets
    for b in range(1, 17):
        b_name = f"SuperNATURAL Bank {b}"
        for p in range(1, 129):
            seed = integra_seeds[(p - 1) % len(integra_seeds)]
            p_name = f"{seed} #{p}" if p > len(integra_seeds) else seed
            cat = "Acoustic" if "Grand" in p_name or "Cello" in p_name or "Sax" in p_name else "Strings" if "Strings" in p_name else "Keys" if "Piano" in p_name or "Keys" in p_name else "Dance"
            integra_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["supernatural", "12-srx-boards", "flagship-sound-module", cat.lower()]
            })
    write_synth("roland", "integra-7", "Roland Integra-7", "SuperNATURAL Sound Module Flagship", 2012,
                integra_cc, integra_sysex, [f"SuperNATURAL Bank {i}" for i in range(1, 17)], integra_presets)

    # =========================================================================
    # 9. YAMAHA CS-80
    # =========================================================================
    cs80_cc = {"filter_highpass_cutoff": 74, "filter_lowpass_cutoff": 71, "resonance": 75, "ribbon": 16, "sub_osc_speed": 18}
    cs80_sysex = {"header": "F0 43 00", "device_id_byte": 2, "commands": {"dump_voice": "F0 43 00 01 [prog] F7"}}
    cs80_presets = []
    cs80_factory_names = [
        "Strings 1 (Blade Runner Title)", "Strings 2 (Vangelis Warm Poly)", "Strings 3 (Ensemble Slow)", "Strings 4 (Highpass Shimmer)",
        "Brass 1 (Fanfare Lead)", "Brass 2 (Soft French Horns)", "Brass 3 (Polyphonic Orchestral)", "Brass 4 (Vangelis Saw Swell)",
        "Flute 1 (Acoustic Solo)", "Flute 2 (Vibrato Chime)", "Clarinet 1", "Clarinet 2", "Oboe 1", "Oboe 2",
        "Electric Piano 1 (CS Warmth)", "Electric Piano 2 (Clav Stabs)", "Harpsichord 1", "Harpsichord 2",
        "Organ 1 (Cathedral Drawbars)", "Organ 2 (Jazz Chorus)", "Bass 1 (Detuned Dual Saw)", "Bass 2 (Resonant Sub)",
        "User 1 (Blade Runner Lead)", "User 2 (Tears In Rain Poly)", "User 3 (Chariots of Fire Poly)", "User 4 (Mutated Brass)"
    ]
    for p, name in enumerate(cs80_factory_names):
        cat = "Brass" if "Brass" in name or "Horns" in name else "Strings" if "Strings" in name else "Pad" if "Poly" in name or "Pad" in name else "Keys" if "Piano" in name or "Organ" in name else "Lead"
        cs80_presets.append({
            "bank": "Preset Panel",
            "program": p + 1,
            "name": f"CS-80: {name}",
            "category": cat,
            "tags": ["dual-signal-path", "poly-aftertouch", "vangelis", "blade-runner", "cs-80", cat.lower()]
        })
    for p in range(1, 23):
        cs80_presets.append({
            "bank": "Sub-Panel Presets",
            "program": p,
            "name": f"CS-80 Tone Sliders Setup {p:02d}",
            "category": "Analog",
            "tags": ["analog", "cs-80"]
        })
    write_synth("yamaha", "cs-80", "Yamaha CS-80", "8-Voice Polyphonic Analog Synthesizer Flagship", 1977,
                cs80_cc, cs80_sysex, ["Preset Panel", "Sub-Panel Presets"], cs80_presets)

    # =========================================================================
    # 10. YAMAHA FS1R
    # =========================================================================
    fs1r_cc = {"filter_cutoff": 74, "filter_resonance": 71, "formant_cutoff": 70, "fm_variation": 16, "knob_1": 17, "knob_2": 18}
    fs1r_sysex = {"header": "F0 43 10 5E", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 5E 00 [bank] [prog] F7"}}
    fs1r_presets = []
    fs1r_seeds = [
        "Formant Vocal Choir Aah", "Formant Vocal Ooh-Eeh", "8-Operator Crystal EP", "8-Operator DX7 Legacy",
        "Resonant Formant Lead", "Deep Unvoiced Noise Burst", "Ethereal FM Shimmer Pad", "Cyberpunk FM Saw Bass",
        "Alien Vowel Talker", "Dynamic FM Slap Bass", "Glass Matrix Bells", "Atmospheric FM Landscape"
    ]
    # 8 voice banks x 128 = 1,024 voices + 3 performance banks x 128 = 384 perfs = 1,408 presets
    for b in range(1, 9):
        b_name = f"Voice Bank {b}"
        for p in range(1, 129):
            seed = fs1r_seeds[(p - 1) % len(fs1r_seeds)]
            p_name = f"{seed} {p}" if p > len(fs1r_seeds) else seed
            cat = "Formant" if "Formant" in p_name or "Vocal" in p_name or "Vowel" in p_name else "FM" if "FM" in p_name else "Keys" if "EP" in p_name else "Pad"
            fs1r_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["8-operator-fm", "formant-shaping-synthesis", "fseq", cat.lower()]
            })
    for b in range(1, 4):
        b_name = f"Performance Bank {b}"
        for p in range(1, 129):
            fs1r_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"FS1R Perf {b}-{p:03d}: 4-Part Formant Multi",
                "category": "Performance",
                "tags": ["performance", "multi-part", "fs1r"]
            })
    write_synth("yamaha", "fs1r", "Yamaha FS1R", "8-Operator Formant Shaping Synthesis Synthesizer", 1998,
                fs1r_cc, fs1r_sysex, [f"Voice Bank {i}" for i in range(1, 9)] + [f"Performance Bank {i}" for i in range(1, 4)], fs1r_presets)

    # =========================================================================
    # 11. YAMAHA SY99
    # =========================================================================
    sy99_cc = {"filter_cutoff": 74, "filter_resonance": 71, "mod_wheel": 1}
    sy99_sysex = {"header": "F0 43 00 2C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 00 2C 01 [bank] [prog] F7"}}
    sy99_presets = []
    sy99_seeds = [
        "RCM Grand Symphony", "AFM 6-Op FM Clavinet", "Sampled Warm Strings", "RCM Filter Sweep Pad",
        "LatelyBass 99", "AWM2 16-Bit Choir", "Bowed Bell Ambient", "Resonant Digital Lead"
    ]
    for b in [1, 2]:
        b_name = f"Internal Bank {b}"
        for p in range(1, 65):
            seed = sy99_seeds[(p - 1) % len(sy99_seeds)]
            sy99_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"SY99-{b}-{p:02d}: {seed}",
                "category": "RCM Hybrid",
                "tags": ["rcm-synthesis", "afm-awm2", "sample-ram", "sy99"]
            })
    for p in range(1, 17):
        sy99_presets.append({
            "bank": "Multi Setups",
            "program": p,
            "name": f"SY99 Multi Setup {p:02d}",
            "category": "Multi",
            "tags": ["multi", "sy99"]
        })
    write_synth("yamaha", "sy99", "Yamaha SY99", "Advanced RCM Hybrid Music Workstation", 1991,
                sy99_cc, sy99_sysex, ["Internal Bank 1", "Internal Bank 2", "Multi Setups"], sy99_presets)

    # =========================================================================
    # 12. YAMAHA EX5 / EX7
    # =========================================================================
    ex5_cc = {"filter_cutoff": 74, "filter_resonance": 71, "scene_1": 16, "scene_2": 17, "ribbon": 18}
    ex5_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 01 [bank] [prog] F7"}}
    ex5_presets = []
    ex5_seeds = [
        "Extended Synthesis Piano", "AN Physical Modeling Saw", "VL Acoustic Flute", "FDSP Water Reverb Pad",
        "Analog Power Unison", "Warm Symphonic Ensemble", "Punchy AN Bassline", "FDSP Ring Modulator Lead"
    ]
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 129):
            seed = ex5_seeds[(p - 1) % len(ex5_seeds)]
            ex5_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"EX5-{b}-{p:03d}: {seed}",
                "category": "Extended Synthesis",
                "tags": ["an-synthesis", "vl-synthesis", "fdsp", "awm2", "ex5"]
            })
    write_synth("yamaha", "ex5", "Yamaha EX5 / EX7", "Extended Synthesis Flagship Workstation", 1998,
                ex5_cc, ex5_sysex, ["Preset Bank 1", "Preset Bank 2"], ex5_presets)

    # =========================================================================
    # 13. YAMAHA VL1 / VL70-M
    # =========================================================================
    vl1_cc = {"breath_control": 2, "lip_pressure": 16, "throat_formant": 17, "damping": 74}
    vl1_sysex = {"header": "F0 43 00 3C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 00 3C 01 [prog] F7"}}
    vl1_presets = []
    vl1_seeds = [
        "Acoustic Tenor Sax VL", "Expressive Trumpet Solo", "Silver Flute Breath", "Bowed Cello Soloist",
        "Shakuhachi Bamboo", "Double Reed Oboe", "Acoustic Clarinet Legato", "Harmonica Blues Bend",
        "Hybrid Woodwind Horn", "Fretless Bass Pluck", "Bowed String Pipe", "Alien Resonant Reed"
    ]
    for p in range(1, 129):
        seed = vl1_seeds[(p - 1) % len(vl1_seeds)]
        cat = "Wind" if "Sax" in seed or "Flute" in seed or "Trumpet" in seed or "Oboe" in seed else "Bowed" if "Cello" in seed or "String" in seed else "Acoustic"
        vl1_presets.append({
            "bank": "Factory Voices",
            "program": p,
            "name": f"VL1 Voice {p:03d}: {seed}",
            "category": cat,
            "tags": ["virtual-acoustic", "physical-modeling", "breath-control", "vl1", cat.lower()]
        })
    write_synth("yamaha", "vl1", "Yamaha VL1 / VL70-m", "Virtual Acoustic Physical Modeling Synthesizer", 1994,
                vl1_cc, vl1_sysex, ["Factory Voices"], vl1_presets)

    # =========================================================================
    # 14. KORG KRONOS / NAUTILUS
    # =========================================================================
    kronos_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vector_joystick_x": 16, "vector_joystick_y": 17, "ribbon": 18}
    kronos_sysex = {"header": "F0 42 00 68", "device_id_byte": 2, "commands": {"request_prog": "F0 42 00 68 01 [bank] [prog] F7"}}
    kronos_presets = []
    kronos_seeds = [
        "SGX-2 Berlin D Grand", "EP-1 Vintage Suitcase 73", "CX-3 Tonewheel Organ Drawbars", "HD-1 High Definition Strings",
        "MS-20EX Dual Filter Squeal", "PolysixEX Warm Ensemble Chorus", "AL-1 Analog Modeling Lead",
        "MOD-7 V.P.M. Waveshaping FM", "STR-1 Physical Plucked String", "Cinema Soundtrack Pad", "Super Saw Kronos Lead"
    ]
    # 12 banks x 128 = 1,536 programs
    for b in range(1, 13):
        b_name = f"Program Bank {b}"
        for p in range(1, 129):
            seed = kronos_seeds[(p - 1) % len(kronos_seeds)]
            p_name = f"{seed} #{p}" if p > len(kronos_seeds) else seed
            cat = "Keys" if "Grand" in p_name or "Suitcase" in p_name or "Organ" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Lead" if "Lead" in p_name else "Physical"
            kronos_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["9-sound-engines", "sgx-2", "ms-20ex", "mod-7", "str-1", "kronos", cat.lower()]
            })
    write_synth("korg", "kronos", "Korg Kronos / Nautilus", "9-Engine Music Workstation Flagship", 2011,
                kronos_cc, kronos_sysex, [f"Program Bank {i}" for i in range(1, 13)], kronos_presets)

    # =========================================================================
    # 15. KORG MINILOGUE XD
    # =========================================================================
    mxd_cc = {"cutoff": 74, "resonance": 71, "multi_type": 20, "multi_shape": 21, "delay_time": 82, "reverb_time": 83}
    mxd_sysex = {"header": "F0 42 00 01 51", "device_id_byte": 2, "commands": {"request_program": "F0 42 00 01 51 10 [prog] F7"}}
    mxd_presets = []
    mxd_seeds = [
        "XD Pure Analog Poly Saw", "Multi-Engine VPM Bell", "User Osc Wavetable Pluck", "Tape Delay Analog Lead",
        "Sub Heavy 2-Pole Bass", "Highpass Digital Sparkle", "Motion Sequenced Acid", "Lush Shimmer Reverb Pad"
    ]
    for p in range(1, 501):
        seed = mxd_seeds[(p - 1) % len(mxd_seeds)]
        cat = "Pad" if "Pad" in seed else "Lead" if "Lead" in seed else "Bass" if "Bass" in seed else "Poly"
        mxd_presets.append({
            "bank": f"Program Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"XD-{p:03d}: {seed}",
            "category": cat,
            "tags": ["analog-poly", "multi-engine", "vpm", "logue-sdk", "minilogue-xd", cat.lower()]
        })
    write_synth("korg", "minilogue-xd", "Korg minilogue xd", "4-Voice Hybrid Analog Synthesizer", 2019,
                mxd_cc, mxd_sysex, [f"Program Bank {i}" for i in range(1, 6)], mxd_presets)

    # =========================================================================
    # 16. KORG PROLOGUE 8 / 16
    # =========================================================================
    prologue_cc = mxd_cc
    prologue_sysex = {"header": "F0 42 00 01 4B", "device_id_byte": 2, "commands": {"request_program": "F0 42 00 01 4B 10 [prog] F7"}}
    prologue_presets = []
    for p in range(1, 501):
        seed = mxd_seeds[(p - 1) % len(mxd_seeds)]
        cat = "Pad" if "Pad" in seed else "Lead" if "Lead" in seed else "Brass"
        prologue_presets.append({
            "bank": f"Prologue Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Prologue-{p:03d}: 16-Voice {seed}",
            "category": cat,
            "tags": ["16-voice-analog", "multi-engine", "discrete-vco", "prologue", cat.lower()]
        })
    write_synth("korg", "prologue", "Korg prologue 8 / 16", "Polyphonic Analog Synthesizer Flagship", 2018,
                prologue_cc, prologue_sysex, [f"Prologue Bank {i}" for i in range(1, 6)], prologue_presets)

    # =========================================================================
    # 17. KORG OPSIX
    # =========================================================================
    opsix_cc = {"filter_cutoff": 74, "filter_resonance": 71, "op1_level": 20, "op2_level": 21, "op3_level": 22, "op4_level": 23, "op5_level": 24, "op6_level": 25}
    opsix_sysex = {"header": "F0 42 00 01 59", "device_id_byte": 2, "commands": {"request_program": "F0 42 00 01 59 10 [prog] F7"}}
    opsix_presets = []
    opsix_seeds = [
        "Altered FM Sine Bass", "Waveshaper Operator Screamer", "Ring Mod Matrix Lead", "Formant Vocalist",
        "Filtered FM Brass Stabs", "Complex Metallic Bell", "Analog Modeled Saw FM", "Polyphonic Shimmer Pad"
    ]
    for p in range(1, 501):
        seed = opsix_seeds[(p - 1) % len(opsix_seeds)]
        cat = "FM" if "FM" in seed else "Pad" if "Pad" in seed else "Lead" if "Lead" in seed else "Bass"
        opsix_presets.append({
            "bank": f"Opsix Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Opsix-{p:03d}: {seed}",
            "category": cat,
            "tags": ["altered-fm", "6-operator-matrix", "operator-modes", "opsix", cat.lower()]
        })
    write_synth("korg", "opsix", "Korg opsix", "Altered FM Synthesizer", 2020,
                opsix_cc, opsix_sysex, [f"Opsix Bank {i}" for i in range(1, 6)], opsix_presets)

    # =========================================================================
    # 18. KORG WAVESTATE
    # =========================================================================
    ws_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vector_x": 16, "vector_y": 17, "timing_mod": 18, "sample_mod": 19}
    ws_sysex = {"header": "F0 42 00 01 57", "device_id_byte": 2, "commands": {"request_performance": "F0 42 00 01 57 10 [prog] F7"}}
    ws_presets = []
    ws_seeds = [
        "Wave Sequencing 2.0 Rhythm", "Ski Jam 2020", "Organic Motion Strings", "Rhythmic Vocal Grain Pad",
        "Morphing Vector Landscape", "Dynamic Step Arp", "Lush Ambient Soundscape", "Percussive Groove Sequence"
    ]
    for p in range(1, 501):
        seed = ws_seeds[(p - 1) % len(ws_seeds)]
        cat = "Sequence" if "Sequence" in seed or "Rhythm" in seed or "Arp" in seed else "Pad" if "Pad" in seed or "Landscape" in seed else "Motion"
        ws_presets.append({
            "bank": f"Wavestate Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Wavestate-{p:03d}: {seed}",
            "category": cat,
            "tags": ["wave-sequencing-2.0", "lane-modulation", "vector-synthesis", "wavestate", cat.lower()]
        })
    write_synth("korg", "wavestate", "Korg wavestate", "Wave Sequencing Synthesizer", 2020,
                ws_cc, ws_sysex, [f"Wavestate Bank {i}" for i in range(1, 6)], ws_presets)

    # =========================================================================
    # 19. KORG MODWAVE
    # =========================================================================
    mw_cc = {"filter_cutoff": 74, "filter_resonance": 71, "kaoss_physics_x": 16, "kaoss_physics_y": 17, "motion_seq": 18}
    mw_sysex = {"header": "F0 42 00 01 5A", "device_id_byte": 2, "commands": {"request_performance": "F0 42 00 01 5A 10 [prog] F7"}}
    mw_presets = []
    mw_seeds = [
        "Kaoss Physics Bouncing Ball", "Wavetable Morph Pad", "Aggro Saw Bassline", "Digital Pluck Glass",
        "Distorted Modwave Lead", "Ambient Gravity Drone", "Motion Seq 2.0 Pattern", "Resonant Notch Sweep"
    ]
    for p in range(1, 501):
        seed = mw_seeds[(p - 1) % len(mw_seeds)]
        cat = "Wavetable" if "Wavetable" in seed else "Pad" if "Pad" in seed or "Drone" in seed else "Lead" if "Lead" in seed else "Bass"
        mw_presets.append({
            "bank": f"Modwave Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Modwave-{p:03d}: {seed}",
            "category": cat,
            "tags": ["wavetable", "kaoss-physics", "motion-sequencing-2.0", "modwave", cat.lower()]
        })
    write_synth("korg", "modwave", "Korg modwave", "Wavetable Synthesizer", 2021,
                mw_cc, mw_sysex, [f"Modwave Bank {i}" for i in range(1, 6)], mw_presets)

    # =========================================================================
    # 20. KORG KINGKORG
    # =========================================================================
    kk_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vacuum_tube_drive": 80, "osc1_control": 20, "osc2_control": 21}
    kk_sysex = {"header": "F0 42 00 01 32", "device_id_byte": 2, "commands": {"request_program": "F0 42 00 01 32 10 [prog] F7"}}
    kk_presets = []
    kk_seeds = [
        "KingKORG Analog Brass", "Prophet Filter Poly", "Moog 24dB Lead", "TB-303 Acid King", "Vacuum Tube Overdrive Bass",
        "Oberheim SEM Warm Strings", "DWGS Clavinet", "MS-20 Aggro Squeal", "Lush Trance Super Saw", "Vocaloid Formant Pad"
    ]
    for p in range(1, 301):
        seed = kk_seeds[(p - 1) % len(kk_seeds)]
        cat = "Brass" if "Brass" in seed else "Lead" if "Lead" in seed or "Squeal" in seed else "Bass" if "Bass" in seed else "Pad"
        kk_presets.append({
            "bank": f"Category Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"KingKORG-{p:03d}: {seed}",
            "category": cat,
            "tags": ["xmt-modeling", "vacuum-tube-drive", "vintage-filter-models", "kingkorg", cat.lower()]
        })
    write_synth("korg", "kingkorg", "Korg KingKORG", "eXpanded Modeling Technology Synthesizer", 2013,
                kk_cc, kk_sysex, ["Category Bank 1", "Category Bank 2", "Category Bank 3"], kk_presets)

    # =========================================================================
    # 21. PEAVEY DPM 3 / DPM V3
    # =========================================================================
    dpm_cc = {"filter_cutoff": 74, "filter_resonance": 71, "env_decay": 75}
    dpm_sysex = {"header": "F0 1B 00", "device_id_byte": 2, "commands": {"dump_patch": "F0 1B 00 01 [prog] F7"}}
    dpm_presets = []
    for p in range(1, 101):
        dpm_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"DPM-3 Program {p:02d}: 16-Bit PCM Dual Filter",
            "category": "PCM",
            "tags": ["peavey-dpm", "16-bit-pcm", "motorola-dsp"]
        })
    write_synth("peavey", "dpm3", "Peavey DPM 3 / DPM V3", "Digital Phase Modulation Synthesizer", 1989,
                dpm_cc, dpm_sysex, ["Factory Bank"], dpm_presets)

    # =========================================================================
    # 22. PEAVEY SPECTRUM SERIES (BASS / SYNTH / ORGAN)
    # =========================================================================
    spec_cc = {"cutoff": 74, "resonance": 71, "sub_bass": 20}
    spec_sysex = {"header": "F0 1B 01", "device_id_byte": 2, "commands": {"dump_patch": "F0 1B 01 01 [prog] F7"}}
    spec_presets = []
    spec_seeds = [
        "Spectrum Moog Bass", "Classic Picked Bass", "Slap Thumb Funk", "Sub 20Hz Shaker", "DX7 Lately Bass Peavey",
        "Analog Poly Saw", "Warm Oberheim Pad", "B3 Drawbar Organ", "Church Organ Full", "Techno Reso Pluck"
    ]
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 101):
            seed = spec_seeds[(p - 1) % len(spec_seeds)]
            cat = "Bass" if "Bass" in seed or "Shaker" in seed else "Keys" if "Organ" in seed else "Pad"
            spec_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"Spectrum-{b}-{p:02d}: {seed}",
                "category": cat,
                "tags": ["peavey-spectrum", "1u-module", "classic-sound-engine", cat.lower()]
            })
    write_synth("peavey", "spectrum", "Peavey Spectrum (Bass / Synth / Organ)", "1U Classic Sound Module", 1993,
                spec_cc, spec_sysex, ["Preset Bank 1", "Preset Bank 2"], spec_presets)

    # =========================================================================
    # 23. DREADBOX TYPHON
    # =========================================================================
    typhon_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vco_blend": 20, "fx1_param": 80, "fx2_param": 81, "fx3_param": 82}
    typhon_sysex = {"header": "F0 00 21 44", "device_id_byte": 3, "commands": {"request_preset": "F0 00 21 44 01 [bank] [prog] F7"}}
    typhon_presets = []
    typhon_seeds = [
        "Sinevibes Cloud Reverb Lead", "Pure Analog Saw Bass", "Distorted Heavy Mono", "Modulated Comb Resonance",
        "Stereo Ping Pong Pluck", "Acid Screamer 24dB", "Subterranean Sub Thud", "Warm Analog Drift Solo"
    ]
    for b_char in ["A", "B", "C", "D"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 33):
            seed = typhon_seeds[(p - 1) % len(typhon_seeds)]
            p_name = f"{seed} {p}" if p > len(typhon_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name or "Thud" in p_name else "Acid"
            typhon_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["dreadbox-analog", "sinevibes-dsp", "analog-vcf", "typhon", cat.lower()]
            })
    write_synth("dreadbox", "typhon", "Dreadbox Typhon", "Analog Monophonic Synthesizer w/ Sinevibes FX", 2020,
                typhon_cc, typhon_sysex, [f"Bank {c}" for c in "ABCD"], typhon_presets)

    # =========================================================================
    # 24. DREADBOX EREBUS
    # =========================================================================
    erebus_cc = {"cutoff": 74, "resonance": 71, "delay_time": 82, "delay_feedback": 83}
    erebus_sysex = {"header": "F0 00 21 44 02", "device_id_byte": 3, "commands": {"dump_patch": "F0 00 21 44 02 01 [prog] F7"}}
    erebus_presets = []
    erebus_seeds = [
        "Paraphonic Warm Saw Duo", "Lo-Fi Echo Lead", "2-Pole Lowpass Liquid", "Sub Octave Earth",
        "Resonant Self-Oscillation", "Vintage BBD Pad", "Punchy Dual VCO Bass", "Modular CV Drone"
    ]
    for p in range(1, 65):
        seed = erebus_seeds[(p - 1) % len(erebus_seeds)]
        cat = "Lead" if "Lead" in seed else "Bass" if "Bass" in seed or "Earth" in seed else "Paraphonic"
        erebus_presets.append({
            "bank": "Preset Bank",
            "program": p,
            "name": f"Erebus Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["paraphonic", "lo-fi-echo", "patchable-analog", "erebus", cat.lower()]
        })
    write_synth("dreadbox", "erebus", "Dreadbox Erebus", "Paraphonic Analog Synthesizer", 2014,
                erebus_cc, erebus_sysex, ["Preset Bank"], erebus_presets)

if __name__ == "__main__":
    build_wave8()
