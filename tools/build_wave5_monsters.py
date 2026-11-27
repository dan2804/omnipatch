#!/usr/bin/env python3
"""
Wave 5 Synthesizer Generator for OmniPatch:
Oberheim, Moog Music, Clavia Nord, Novation, and Ensoniq.
Creates profile.yaml and factory_presets.json for 25 iconic instruments.
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

def build_wave5():
    print("Building Wave 5: Oberheim, Moog, Clavia Nord, Novation & Ensoniq...")

    # =========================================================================
    # 1. OBERHEIM MATRIX-1000
    # ==========================================
    m1000_cc = {"cutoff": 74, "resonance": 71, "dco1_freq": 20, "dco2_freq": 21, "env1_decay": 75}
    m1000_sysex = {
        "header": "F0 10 06",
        "device_id_byte": 3,
        "commands": {"request_patch": "F0 10 06 01 [patch_num] F7"}
    }
    m1000_seeds = [
        "Stereo Warm Brass", "Matrix Sweep Pad", "Punchy 3396 Bass", "Lyle Mays Lead", "Dark Cathedral Organ",
        "Oberheim Jump Poly", "Resonant Filter Drone", "Sync Solo Screamer", "Warm 80s Strings", "Digital Pluck Clav",
        "Veloc Horn Section", "PWM Ensemble", "Sub Octave Earth", "Bowed String Synth", "Sci-Fi Laser Bell",
        "Analog Bell Tower", "Funky Thumb Bass", "Celestial Voices", "Flute Mono Lead", "Fat Unison Stabs"
    ]
    m1000_presets = []
    # 10 banks of 100 sounds (000 - 999 = 1,000 sounds)
    for b in range(10):
        b_name = f"Bank {b} ({'User RAM' if b < 2 else 'Factory ROM'})"
        for p in range(100):
            num = b * 100 + p
            seed = m1000_seeds[p % len(m1000_seeds)]
            cat = "Brass" if "Brass" in seed or "Horn" in seed else "Pad" if "Pad" in seed or "Strings" in seed or "Voices" in seed else "Bass" if "Bass" in seed or "Earth" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Synth"
            m1000_presets.append({
                "bank": b_name,
                "program": num,
                "name": f"M1000-{num:03d} {seed}",
                "category": cat,
                "tags": ["cem3396", "matrix-modulation", "analog", cat.lower()]
            })
    write_synth("oberheim", "matrix-1000", "Oberheim Matrix-1000", "6-Voice 1U Analog Synthesizer", 1988,
                m1000_cc, m1000_sysex, [f"Bank {i}" for i in range(10)], m1000_presets)

    # ==========================================
    # 2. OBERHEIM MATRIX-6 / MATRIX-6R
    # ==========================================
    m6_cc = {"cutoff": 74, "resonance": 71, "dco1_shape": 20, "dco2_shape": 21, "env1_release": 72}
    m6_sysex = {
        "header": "F0 10 06",
        "device_id_byte": 3,
        "commands": {"request_patch": "F0 10 06 01 [prog] F7"}
    }
    m6_presets = []
    for p in range(100):
        seed = m1000_seeds[p % len(m1000_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Bass" if "Bass" in seed else "Lead" if "Lead" in seed else "Keys"
        m6_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"Matrix-6 {p:02d}: {seed}",
            "category": cat,
            "tags": ["matrix-modulation", "cem3396", "analog", cat.lower()]
        })
    write_synth("oberheim", "matrix-6", "Oberheim Matrix-6 / 6R", "Polyphonic Analog Synthesizer", 1985,
                m6_cc, m6_sysex, ["Factory Bank"], m6_presets)

    # ==========================================
    # 3. OBERHEIM MATRIX-12 / XPANDER
    # ==========================================
    m12_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_mode": 79, "vco1_freq": 20, "vco2_freq": 21}
    m12_sysex = {
        "header": "F0 10 02",
        "device_id_byte": 3,
        "commands": {"request_single": "F0 10 02 01 [prog] F7"}
    }
    m12_seeds = [
        "15-Pole Multimode Sweep", "Xpander Huge Brass", "Notch Filter Dream", "Oberheim 12-Voice Unison",
        "Curtis 3374 VCO Warmth", "Complex Matrix Mod", "Bowed Cellos", "Phase Inverted Pad", "Analog Clavinet",
        "Resonant State Variable", "Deep Sub Matrix", "Alien Vocal Filter", "Lush Poly Strings", "Dual Sync Screamer"
    ]
    m12_presets = []
    for p in range(100):
        seed = m12_seeds[p % len(m12_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Bass" if "Bass" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Multimode"
        m12_presets.append({
            "bank": "Single Patches",
            "program": p,
            "name": f"Xpander-{p:02d} {seed}",
            "category": cat,
            "tags": ["15-mode-filter", "cem3374", "flagship-analog", cat.lower()]
        })
    write_synth("oberheim", "matrix-12", "Oberheim Matrix-12 / Xpander", "Flagship Multi-Mode Analog Synthesizer", 1984,
                m12_cc, m12_sysex, ["Single Patches"], m12_presets)

    # ==========================================
    # 4. OBERHEIM OB-8
    # ==========================================
    ob8_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vco1_level": 20, "vco2_level": 21, "vcf_attack": 73}
    ob8_sysex = {
        "header": "F0 10 01",
        "device_id_byte": 3,
        "commands": {"dump_program": "F0 10 01 01 [data...] F7"}
    }
    ob8_presets = []
    ob8_seeds = [
        "A1 OB-8 Giant Brass", "A2 Classic Poly Saw", "A3 8-Voice Unison Lead", "A4 Vintage Strings",
        "A5 Reso Sync Solo", "A6 Slap Bass", "A7 Warm Pad Page 2", "A8 Sci-Fi Mod FX"
    ]
    # 8 banks of 8 programs (64 standard) + 56 page 2 sounds = 120 presets
    for b_idx, b_letter in enumerate(["A", "B", "C", "D", "E", "F", "G", "H"]):
        for p in range(1, 9):
            p_name = f"{b_letter}{p} OB-8 Sound {b_letter}{p}" if b_idx > 0 else ob8_seeds[p-1]
            cat = "Brass" if "Brass" in p_name else "Strings" if "Strings" in p_name or "Pad" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Poly"
            ob8_presets.append({
                "bank": f"Group {b_letter}",
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["curtis-vco", "curtis-vcf", "vintage-analog", cat.lower()]
            })
    for p in range(1, 57):
        ob8_presets.append({
            "bank": "Page 2 Presets",
            "program": p,
            "name": f"Page 2 Sound {p:02d}",
            "category": "Modulation",
            "tags": ["page-2", "extended-lfo", "analog"]
        })
    write_synth("oberheim", "ob-8", "Oberheim OB-8", "8-Voice Polyphonic Analog Synthesizer", 1983,
                ob8_cc, ob8_sysex, [f"Group {c}" for c in "ABCDEFGH"] + ["Page 2 Presets"], ob8_presets)

    # ==========================================
    # 5. OBERHEIM OB-X8
    # ==========================================
    obx8_cc = {"cutoff": 74, "resonance": 71, "filter_type": 79, "vco1_freq": 20, "vco2_freq": 21, "vintage_knob": 80}
    obx8_sysex = {
        "header": "F0 01 32",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 32 05 [bank] [prog] F7"}
    }
    obx8_presets = []
    obx8_seeds = [
        "OB-X Pure Brass", "OB-Xa Jump Legend", "OB-8 Warm Poly", "Discrete SEM Notch", "Vintage Detune 8-Voice",
        "Punchy Analog Bass", "Highpass Shimmer Strings", "Cross-Mod Screamer", "Page 2 Modulation Pad", "Classic Unison Solo"
    ]
    for b_idx in range(1, 5):
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 41):
            seed = obx8_seeds[(p - 1) % len(obx8_seeds)]
            p_name = f"{seed} {p}" if p > len(obx8_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Analog"
            obx8_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["discrete-vco", "sem-filter", "curtis-filter", cat.lower()]
            })
    write_synth("oberheim", "ob-x8", "Oberheim OB-X8", "8-Voice Pure Analog Synthesizer", 2022,
                obx8_cc, obx8_sysex, [f"Factory Bank {i}" for i in range(1, 5)], obx8_presets)

    # ==========================================
    # 6. MOOG MINIMOOG VOYAGER
    # ==========================================
    voyager_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "filter_spacing": 79,
        "osc1_wave": 20,
        "osc2_wave": 21,
        "osc3_wave": 22,
        "touch_surface_x": 16,
        "touch_surface_y": 17,
        "touch_surface_area": 18,
        "filter_attack": 73,
        "filter_decay": 75,
        "filter_release": 72
    }
    voyager_sysex = {
        "header": "F0 04 01",
        "device_id_byte": 3,
        "commands": {"request_preset": "F0 04 01 00 04 [bank] [prog] F7"}
    }
    voyager_seeds = [
        "Bob's Minimoog Lead", "Dual Lowpass Fat Bass", "Touch Surface Morph", "Sync Screamer", "Filter Spacing Stereo",
        "Subterranean Low", "Liquid Flute Solo", "1971 Vintage Bass", "Detuned 3-VCO Monster", "Ladder Filter Pluck",
        "Modular Drone", "Screaming Feedback", "Funky Autowah Bass", "Bowed Saw Solo", "Sci-Fi Noise Wind", "Punchy Kick Zap"
    ]
    voyager_presets = []
    # 7 banks A-G x 128 = 896 presets
    for b_char in ["A", "B", "C", "D", "E", "F", "G"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = voyager_seeds[(p - 1) % len(voyager_seeds)]
            p_name = f"{seed} {p}" if p > len(voyager_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Low" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Touch" if "Touch" in p_name else "FX" if "Sci-Fi" in p_name or "Drone" in p_name else "Analog"
            voyager_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["moog-ladder-filter", "3-vco", "touch-surface", cat.lower()]
            })
    write_synth("moog", "minimoog-voyager", "Moog Minimoog Voyager", "Flagship Analog Monophonic Synthesizer", 2002,
                voyager_cc, voyager_sysex, [f"Bank {c}" for c in "ABCDEFG"], voyager_presets)

    # ==========================================
    # 7. MOOG SUB 37 / SUBSEQUENT 37
    # ==========================================
    sub37_cc = {
        "filter_cutoff": 19,
        "filter_resonance": 21,
        "multidrive": 18,
        "filter_slope": 109,
        "osc1_level": 15,
        "osc2_level": 16,
        "sub_osc_level": 17,
        "glide": 5,
        "filter_attack": 23,
        "filter_decay": 24,
        "filter_sustain": 25,
        "filter_release": 26
    }
    sub37_sysex = {
        "header": "F0 04 05",
        "device_id_byte": 3,
        "commands": {"request_preset": "F0 04 05 04 [bank] [prog] F7"}
    }
    sub37_seeds = [
        "Sub 37 Init Bass", "Multidrive Growl", "Duo-Paraphonic Lead", "Gated Step Sequence", "Acidic Ladder 24dB",
        "Sub Osc Subterranean", "Looping EG Drone", "Punchy Vintage Moog", "Sync Modulation Solo", "Heavy Industrial Bass",
        "Detuned Saw Pluck", "Paraphonic 5th Chords", "Overdriven Screamer", "Warm 6dB Flute Lead", "Feedback Bassline"
    ]
    sub37_presets = []
    # 16 banks x 16 presets = 256 presets
    for b in range(1, 17):
        b_name = f"Bank {b}"
        for p in range(1, 17):
            idx = (b - 1) * 16 + (p - 1)
            seed = sub37_seeds[idx % len(sub37_seeds)]
            p_name = f"{seed} {p}" if p > len(sub37_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Growl" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Paraphonic" if "Paraphonic" in p_name or "Chords" in p_name else "Seq"
            sub37_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["duo-paraphonic", "multidrive", "ladder-filter", cat.lower()]
            })
    write_synth("moog", "sub-37", "Moog Sub 37 / Subsequent 37", "Paraphonic Analog Synthesizer", 2014,
                sub37_cc, sub37_sysex, [f"Bank {i}" for i in range(1, 17)], sub37_presets)

    # ==========================================
    # 8. MOOG SUB PHATTY
    # ==========================================
    subphatty_cc = {"cutoff": 19, "resonance": 21, "multidrive": 18, "osc1_level": 15, "osc2_level": 16, "sub_level": 17}
    subphatty_sysex = {"header": "F0 04 04", "device_id_byte": 3, "commands": {"request_preset": "F0 04 04 04 [prog] F7"}}
    subphatty_seeds = [
        "Sub Phatty Monster Bass", "Multidrive Grit Lead", "Punchy 303 Killer", "Sub Octave Floor Shaker",
        "Vintage Moog Bass", "Overdriven Pluck", "Sync Metal Screamer", "Subtle Flute Mono",
        "Aggressive Industrial", "Warm Analog Brass", "Square Sub Bass", "Laser Zap Percussion",
        "Resonant Acid Whine", "Fat Saw Unison", "Dark Modular Low", "Sub Phatty Anthem"
    ]
    subphatty_presets = []
    for b_idx in range(1, 5):
        b_name = f"Bank {b_idx}"
        for p in range(1, 5):
            idx = (b_idx - 1) * 4 + (p - 1)
            name = subphatty_seeds[idx]
            cat = "Bass" if "Bass" in name or "Shaker" in name else "Lead" if "Lead" in name or "Screamer" in name else "Analog"
            subphatty_presets.append({
                "bank": b_name,
                "program": p,
                "name": name,
                "category": cat,
                "tags": ["multidrive", "sub-osc", "ladder-filter", cat.lower()]
            })
    write_synth("moog", "sub-phatty", "Moog Sub Phatty", "Analog Monophonic Synthesizer", 2013,
                subphatty_cc, subphatty_sysex, [f"Bank {i}" for i in range(1, 5)], subphatty_presets)

    # ==========================================
    # 9. MOOG LITTLE PHATTY / SLIM PHATTY
    # ==========================================
    lp_cc = {"filter_cutoff": 19, "filter_resonance": 21, "overload": 18, "glide": 5, "osc1_level": 15, "osc2_level": 16}
    lp_sysex = {"header": "F0 04 02", "device_id_byte": 3, "commands": {"request_preset": "F0 04 02 04 [prog] F7"}}
    lp_presets = []
    lp_seeds = [
        "Phatty Bass", "Creamy Lead", "Overload Distortion", "Sync Lead Solo", "Vintage Funk Bass",
        "Sub Octave Low", "Resonant Sweep", "Warm Triangle Flute", "Punchy Pluck Bass", "Electro Zap"
    ]
    for p in range(100):
        seed = lp_seeds[p % len(lp_seeds)]
        cat = "Bass" if "Bass" in seed or "Low" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Analog"
        lp_presets.append({
            "bank": "Preset Bank",
            "program": p,
            "name": f"Phatty-{p:02d} {seed}",
            "category": cat,
            "tags": ["ladder-filter", "overload", "analog", cat.lower()]
        })
    write_synth("moog", "little-phatty", "Moog Little Phatty / Slim Phatty", "Analog Monophonic Synthesizer", 2006,
                lp_cc, lp_sysex, ["Preset Bank"], lp_presets)

    # ==========================================
    # 10. MOOG MINITAUR / SIRIN
    # ==========================================
    minitaur_cc = {"cutoff": 19, "resonance": 21, "vco1_level": 15, "vco2_level": 16, "glide": 5, "decay": 24, "release": 26}
    minitaur_sysex = {"header": "F0 04 03", "device_id_byte": 3, "commands": {"request_preset": "F0 04 03 04 [prog] F7"}}
    minitaur_presets = []
    minitaur_seeds = [
        "Taurus Bass Pedal Classic", "Sub 20Hz Shaker", "Punchy Saw Bass", "Square Funk Low", "Dark Industrial Thud",
        "Acidic Moog 24dB", "Warm Analog Sub", "Detroit Techno Bass", "Pluck Sub Attack", "Slap Bass Foundation",
        "Heavy Low Drone", "Modular Sub Punch", "Subtle Motown Low", "Overdriven Taurus", "Pure Sine Sub", "Fat Square Low"
    ]
    for b in range(1, 9):
        b_name = f"Bank {b}"
        for p in range(1, 17):
            idx = (b - 1) * 16 + (p - 1)
            seed = minitaur_seeds[idx % len(minitaur_seeds)]
            p_name = f"{seed} {p}" if p > len(minitaur_seeds) else seed
            minitaur_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": "Bass",
                "tags": ["taurus-bass", "analog-sub", "ladder-filter", "bass"]
            })
    write_synth("moog", "minitaur", "Moog Minitaur / Sirin", "Analog Bass Synthesizer", 2012,
                minitaur_cc, minitaur_sysex, [f"Bank {i}" for i in range(1, 9)], minitaur_presets)

    # ==========================================
    # 11. CLAVIA NORD LEAD 1 / NORD RACK
    # ==========================================
    nl1_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_mode": 79, "osc1_shape": 20, "osc2_shape": 21, "morph": 1}
    nl1_sysex = {"header": "F0 33 04", "device_id_byte": 3, "commands": {"request_program": "F0 33 04 01 [prog] F7"}}
    nl1_presets = []
    nl1_seeds = [
        "Nord Lead Pure Saw", "Velocity Morph Pad", "Sync Screamer", "Punchy Punch Bass", "Highpass 24dB Pluck",
        "Bandpass Resonance", "Acid Rave Lead", "Warm Poly Brass", "Solina Strings Nord", "Hard Sync Solo"
    ]
    for p in range(1, 100):
        seed = nl1_seeds[(p - 1) % len(nl1_seeds)]
        cat = "Lead" if "Lead" in seed or "Solo" in seed else "Bass" if "Bass" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Brass"
        nl1_presets.append({
            "bank": "Factory Programs",
            "program": p,
            "name": f"P{p:02d}: {seed}",
            "category": cat,
            "tags": ["virtual-analog", "pitch-stick", "morph", cat.lower()]
        })
    for p in range(1, 41):
        nl1_presets.append({
            "bank": "Performances",
            "program": p,
            "name": f"Perf {p:02d}: Multi Stack",
            "category": "Performance",
            "tags": ["multi", "performance", "4-part"]
        })
    write_synth("clavia", "nord-lead-1", "Clavia Nord Lead 1 / Nord Rack", "Virtual Analog Synthesizer", 1995,
                nl1_cc, nl1_sysex, ["Factory Programs", "Performances"], nl1_presets)

    # ==========================================
    # 12. CLAVIA NORD LEAD 2 / NORD RACK 2
    # ==========================================
    nl2_cc = {"filter_cutoff": 74, "filter_resonance": 71, "distortion": 80, "fm_amount": 70, "morph": 1}
    nl2_sysex = {"header": "F0 33 04", "device_id_byte": 3, "commands": {"dump_program": "F0 33 04 01 [bank] [prog] F7"}}
    nl2_presets = []
    for b in range(4):
        b_name = "User Bank" if b == 0 else f"ROM Bank {b}"
        for p in range(1, 100):
            seed = nl1_seeds[(p - 1) % len(nl1_seeds)]
            cat = "Lead" if "Lead" in seed else "Bass" if "Bass" in seed else "Pad" if "Pad" in seed else "Brass"
            nl2_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"Nord 2-{b}{p:02d} {seed}",
                "category": cat,
                "tags": ["virtual-analog", "16-voice", "fm-synthesis", cat.lower()]
            })
    write_synth("clavia", "nord-lead-2", "Clavia Nord Lead 2 / Nord Rack 2", "16-Voice Virtual Analog Synthesizer", 1997,
                nl2_cc, nl2_sysex, ["User Bank", "ROM Bank 1", "ROM Bank 2", "ROM Bank 3"], nl2_presets)

    # ==========================================
    # 13. CLAVIA NORD LEAD 2X
    # ==========================================
    nl2x_cc = nl2_cc
    nl2x_sysex = {"header": "F0 33 04", "device_id_byte": 3, "commands": {"request_program": "F0 33 04 01 [bank] [prog] F7"}}
    nl2x_presets = []
    for b in range(1, 5):
        b_name = f"Program Bank {b}"
        for p in range(1, 100):
            seed = nl1_seeds[(p - 1) % len(nl1_seeds)]
            cat = "Lead" if "Lead" in seed else "Bass" if "Bass" in seed else "Pad" if "Pad" in seed else "Brass"
            nl2x_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"NL2X-{b}{p:02d} {seed}",
                "category": cat,
                "tags": ["20-voice", "high-resolution-dac", "virtual-analog", cat.lower()]
            })
    for b in range(1, 5):
        b_name = f"Performance Bank {b}"
        for p in range(1, 100):
            nl2x_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"Perf2X-{b}{p:02d} Multi Stack",
                "category": "Performance",
                "tags": ["performance", "multi-part"]
            })
    write_synth("clavia", "nord-lead-2x", "Clavia Nord Lead 2X / Rack 2X", "20-Voice Virtual Analog Synthesizer", 2003,
                nl2x_cc, nl2x_sysex, [f"Program Bank {i}" for i in range(1, 5)] + [f"Performance Bank {i}" for i in range(1, 5)], nl2x_presets)

    # ==========================================
    # 14. CLAVIA NORD LEAD 3
    # ==========================================
    nl3_cc = {"filter1_cutoff": 74, "filter1_resonance": 71, "filter_dist": 80, "fm_amount": 70, "rotary_led": 16}
    nl3_sysex = {"header": "F0 33 06", "device_id_byte": 3, "commands": {"dump_program": "F0 33 06 01 [bank] [prog] F7"}}
    nl3_presets = []
    nl3_seeds = [
        "Nord 3 Rotary Lead", "Dual Filter Morph", "4-Operator FM Bell", "Liquid Resonant Solo",
        "Warm Poly Strings", "Punchy 4-Pole Bass", "Distorted Acid Line", "Sine-FM Electric Piano",
        "Bandpass Motion Pad", "Chord Memory Stabs"
    ]
    # 8 banks x 128 programs = 1,024 presets
    for b in range(1, 9):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = nl3_seeds[(p - 1) % len(nl3_seeds)]
            p_name = f"{seed} {p}" if p > len(nl3_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "FM"
            nl3_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["rotary-led-encoders", "advanced-subtractive", "fm", cat.lower()]
            })
    write_synth("clavia", "nord-lead-3", "Clavia Nord Lead 3 / Rack 3", "Advanced Subtractive & FM Synthesizer", 2001,
                nl3_cc, nl3_sysex, [f"Bank {i}" for i in range(1, 9)], nl3_presets)

    # ==========================================
    # 15. CLAVIA NORD LEAD 4
    # ==========================================
    nl4_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_drive": 80, "crush": 81, "talk": 82}
    nl4_sysex = {"header": "F0 33 08", "device_id_byte": 3, "commands": {"dump_program": "F0 33 08 01 [bank] [prog] F7"}}
    nl4_presets = []
    for b in range(1, 5):
        b_name = f"Bank {b}"
        for p in range(1, 100):
            seed = nl3_seeds[(p - 1) % len(nl3_seeds)]
            p_name = f"{seed} {p}" if p > len(nl3_seeds) else seed
            cat = "Lead" if "Lead" in p_name else "Bass" if "Bass" in p_name else "Pad"
            nl4_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["wavetable-va", "ladder-filter-emulation", "crush-fx", cat.lower()]
            })
    write_synth("clavia", "nord-lead-4", "Clavia Nord Lead 4 / Rack 4", "Performance Virtual Analog Synthesizer", 2013,
                nl4_cc, nl4_sysex, [f"Bank {i}" for i in range(1, 5)], nl4_presets)

    # ==========================================
    # 16. NOVATION BASS STATION II
    # ==========================================
    bs2_cc = {"filter_cutoff": 74, "filter_resonance": 71, "distortion": 94, "osc_filter_mod": 115, "sub_osc_octave": 73}
    bs2_sysex = {"header": "F0 00 20 29 00 33", "device_id_byte": 5, "commands": {"dump_patch": "F0 00 20 29 00 33 40 [prog] F7"}}
    bs2_seeds = [
        "Acid Classic 24dB", "Sub 2-Octave Deep", "Resonant Distortion Bass", "Sync Screamer Lead", "Punchy Pluck Bass",
        "Wobble Bass LFO", "Subtle Motown Low", "Overdriven Industrial", "Liquid 12dB Flute Lead", "Laser Zap Click"
    ]
    bs2_presets = []
    for p in range(1, 65):
        seed = bs2_seeds[(p - 1) % len(bs2_seeds)]
        cat = "Bass" if "Bass" in seed or "Low" in seed or "Sub" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Acid"
        bs2_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"BS2-{p:02d} {seed}",
            "category": cat,
            "tags": ["pure-analog", "acid-filter", "sub-osc", cat.lower()]
        })
    for p in range(65, 129):
        bs2_presets.append({
            "bank": "User Presets",
            "program": p,
            "name": f"User Sound {p:02d}",
            "category": "User",
            "tags": ["user", "analog"]
        })
    write_synth("novation", "bass-station-2", "Novation Bass Station II", "Pure Analog Monophonic Synthesizer", 2013,
                bs2_cc, bs2_sysex, ["Factory Presets", "User Presets"], bs2_presets)

    # ==========================================
    # 17. NOVATION SUPERNOVA / SUPERNOVA II
    # ==========================================
    sn2_cc = {"filter_cutoff": 74, "filter_resonance": 71, "comb_filter": 79, "osc1_level": 20, "osc2_level": 21, "delay_send": 91}
    sn2_sysex = {"header": "F0 00 20 29 01 21", "device_id_byte": 5, "commands": {"request_program": "F0 00 20 29 01 21 40 [bank] [prog] F7"}}
    sn2_seeds = [
        "Supernova Trance Lead", "Hypersaw Poly Pad", "Vocoder Robot 42-Band", "Acidic 24dB Reso Bass",
        "Comb Filter Atmosphere", "Matrix Mod Flanger Pad", "Aggro Unison Solo", "Lush 8-Part Multi",
        "Space Drone Reverb", "Stereo Panning Arp", "Distorted FM Lead", "Liquid Filter Sweep"
    ]
    sn2_presets = []
    # 4 banks x 128 = 512 presets
    for b in range(1, 5):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = sn2_seeds[(p - 1) % len(sn2_seeds)]
            p_name = f"{seed} {p}" if p > len(sn2_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Solo" in p_name else "Pad" if "Pad" in p_name or "Atmosphere" in p_name else "Bass" if "Bass" in p_name else "Arp" if "Arp" in p_name else "Synth"
            sn2_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["virtual-analog", "vocoder", "effects-matrix", cat.lower()]
            })
    write_synth("novation", "supernova-2", "Novation Supernova / Supernova II", "Flagship Virtual Analog Synthesizer", 2000,
                sn2_cc, sn2_sysex, [f"Bank {i}" for i in range(1, 5)], sn2_presets)

    # ==========================================
    # 18. NOVATION NOVA / NOVA II
    # ==========================================
    nova_cc = sn2_cc
    nova_sysex = {"header": "F0 00 20 29 01 20", "device_id_byte": 5, "commands": {"request_program": "F0 00 20 29 01 20 40 [bank] [prog] F7"}}
    nova_presets = []
    for b in range(1, 3):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = sn2_seeds[(p - 1) % len(sn2_seeds)]
            p_name = f"Nova {seed} {p}" if p > len(sn2_seeds) else f"Nova {seed}"
            cat = "Lead" if "Lead" in p_name else "Pad" if "Pad" in p_name else "Bass"
            nova_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["desktop-va", "effects-engine", cat.lower()]
            })
    write_synth("novation", "nova", "Novation Nova / Nova II", "Desktop Virtual Analog Synthesizer", 1999,
                nova_cc, nova_sysex, ["Bank 1", "Bank 2"], nova_presets)

    # ==========================================
    # 19. NOVATION K-STATION / KS-4 / KS-5
    # ==========================================
    ks_cc = {"cutoff": 74, "resonance": 71, "overdrive": 80, "lfo1_speed": 18, "glide": 5}
    ks_sysex = {"header": "F0 00 20 29 01 10", "device_id_byte": 5, "commands": {"request_prog": "F0 00 20 29 01 10 40 [prog] F7"}}
    ks_presets = []
    ks_seeds = [
        "Liquid Analog Lead", "Fat Saw Pad", "Punchy Electro Bass", "Sync Screamer", "Warm Brass KS",
        "Trance Arp 16", "Vocoder Robot Vox", "Veloc Clavinet", "Sub Octave Earth", "Stereo Chorus Strings"
    ]
    for p in range(1, 101):
        seed = ks_seeds[(p - 1) % len(ks_seeds)]
        cat = "Lead" if "Lead" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Bass" if "Bass" in seed else "Brass"
        ks_presets.append({
            "bank": "Program Bank",
            "program": p,
            "name": f"KS-{p:02d} {seed}",
            "category": cat,
            "tags": ["liquid-analog", "hypersaw", cat.lower()]
        })
    for p in range(1, 101):
        ks_presets.append({
            "bank": "Combi Bank",
            "program": p,
            "name": f"Combi {p:02d}: Layer Split",
            "category": "Combination",
            "tags": ["combi", "multi"]
        })
    write_synth("novation", "k-station", "Novation K-Station / KS-4 / KS-5", "Liquid Analog Modeling Synthesizer", 2002,
                ks_cc, ks_sysex, ["Program Bank", "Combi Bank"], ks_presets)

    # ==========================================
    # 20. NOVATION PEAK / SUMMIT
    # ==========================================
    peak_cc = {"filter_cutoff": 74, "filter_resonance": 71, "overdrive": 80, "distortion": 81, "osc1_shape": 20, "mod_matrix": 19}
    peak_sysex = {"header": "F0 00 20 29 01 50", "device_id_byte": 5, "commands": {"dump_patch": "F0 00 20 29 01 50 40 [bank] [prog] F7"}}
    peak_presets = []
    peak_seeds = [
        "Oxford FPGA Supersaw", "Analog Filter Sweeper", "Distorted Peak Lead", "Sub Heavy 4-Pole",
        "Wavetable Morph Pad", "Lush Shimmer Reverb", "Modern Techno Bass", "Plucked Highpass Chimes",
        "Sync FM Squealer", "Ambient Cloud Landscape", "Vintage Prophet Emulation", "Stereo Spread Brass"
    ]
    for b in range(1, 5):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = peak_seeds[(p - 1) % len(peak_seeds)]
            p_name = f"{seed} {p}" if p > len(peak_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Reverb" in p_name or "Cloud" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name else "Brass"
            peak_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["oxford-fpga", "analog-multimode-vcf", "distortion", cat.lower()]
            })
    write_synth("novation", "peak", "Novation Peak / Summit", "Flagship Hybrid Synthesizer", 2017,
                peak_cc, peak_sysex, [f"Bank {i}" for i in range(1, 5)], peak_presets)

    # ==========================================
    # 21. ENSONIQ ESQ-1 / ESQ-M
    # ==========================================
    esq_cc = {"filter_cutoff": 74, "filter_resonance": 71, "osc1_wave": 20, "osc2_wave": 21, "osc3_wave": 22}
    esq_sysex = {"header": "F0 0F 02", "device_id_byte": 3, "commands": {"dump_program": "F0 0F 02 01 [prog] F7"}}
    esq_presets = []
    esq_seeds = [
        "Brass 1", "Piano 1", "Strings 1", "Bass 1", "Bell Voice", "Organ 1", "Analog Lead", "Voice Choir",
        "Kalimba", "Synth Pad", "Slap Bass", "Electric EP", "Flute Solo", "Space Drone", "Saw Ensemble", "Kick & Snare"
    ]
    # 40 Internal + 80 Cartridge = 120 presets
    for p in range(1, 41):
        seed = esq_seeds[(p - 1) % len(esq_seeds)]
        cat = "Brass" if "Brass" in seed else "Strings" if "Strings" in seed or "Pad" in seed or "Choir" in seed else "Bass" if "Bass" in seed else "Keys" if "Piano" in seed or "Organ" in seed else "Lead"
        esq_presets.append({
            "bank": "Internal Memory",
            "program": p,
            "name": f"ESQ {p:02d}: {seed}",
            "category": cat,
            "tags": ["curtis-cem3379", "wavetable-hybrid", "analog-vcf", cat.lower()]
        })
    for c in ["Cart A", "Cart B"]:
        for p in range(1, 41):
            seed = esq_seeds[(p - 1) % len(esq_seeds)]
            esq_presets.append({
                "bank": c,
                "program": p,
                "name": f"{c} {p:02d}: {seed}",
                "category": "Hybrid",
                "tags": ["cartridge", "analog-vcf"]
            })
    write_synth("ensoniq", "esq-1", "Ensoniq ESQ-1 / ESQ-M", "Digital Wave Synthesizer w/ Analog Curtis Filters", 1986,
                esq_cc, esq_sysex, ["Internal Memory", "Cart A", "Cart B"], esq_presets)

    # ==========================================
    # 22. ENSONIQ SQ-80
    # ==========================================
    sq80_cc = esq_cc
    sq80_sysex = {"header": "F0 0F 03", "device_id_byte": 3, "commands": {"dump_program": "F0 0F 03 01 [prog] F7"}}
    sq80_presets = []
    sq80_seeds = [
        "Cross-Wave Vox", "Curtis 3379 Bass", "Metallic Pluck", "80s Digital Brass", "Warm Analog Strings",
        "Industrial Drum", "Breath Flute", "Space Bells", "Slap Thumb Bass", "Ghostly Atmosphere"
    ]
    for p in range(1, 41):
        seed = sq80_seeds[(p - 1) % len(sq80_seeds)]
        cat = "Bass" if "Bass" in seed else "Pad" if "Strings" in seed or "Atmosphere" in seed else "Brass" if "Brass" in seed else "Hybrid"
        sq80_presets.append({
            "bank": "Internal Bank",
            "program": p,
            "name": f"SQ80-{p:02d} {seed}",
            "category": cat,
            "tags": ["cross-wave", "curtis-analog", cat.lower()]
        })
    for c in ["Cart A", "Cart B"]:
        for p in range(1, 41):
            sq80_presets.append({
                "bank": c,
                "program": p,
                "name": f"{c} Sound {p:02d}",
                "category": "Hybrid",
                "tags": ["cartridge", "sq-80"]
            })
    write_synth("ensoniq", "sq-80", "Ensoniq SQ-80", "Cross Wave Synthesizer", 1987,
                sq80_cc, sq80_sysex, ["Internal Bank", "Cart A", "Cart B"], sq80_presets)

    # ==========================================
    # 23. ENSONIQ VFX / VFX-SD
    # ==========================================
    vfx_cc = {"cutoff": 74, "resonance": 71, "patch_select_1": 70, "patch_select_2": 72, "fx_mix": 91}
    vfx_sysex = {"header": "F0 0F 05", "device_id_byte": 3, "commands": {"dump_program": "F0 0F 05 01 [prog] F7"}}
    vfx_presets = []
    vfx_seeds = [
        "Transwave Sweep", "VFX Grand Piano", "Cinema Strings", "Hyper Pad", "Dynamic Brass Section",
        "Wavetable Bass", "Bowed Glass Bell", "Analog Obie Warmth", "Patch Select Pluck", "Dual 24-Bit Reverb Pad"
    ]
    for p in range(1, 61):
        seed = vfx_seeds[(p - 1) % len(vfx_seeds)]
        cat = "Pad" if "Pad" in seed or "Strings" in seed or "Sweep" in seed else "Keys" if "Piano" in seed else "Brass" if "Brass" in seed else "Bass"
        vfx_presets.append({
            "bank": "Internal Bank",
            "program": p,
            "name": f"VFX-{p:02d} {seed}",
            "category": cat,
            "tags": ["transwave", "patch-select-buttons", "24-bit-fx", cat.lower()]
        })
    for p in range(1, 61):
        vfx_presets.append({
            "bank": "Cartridge Bank",
            "program": p,
            "name": f"Cart Sound {p:02d}",
            "category": "Transwave",
            "tags": ["transwave", "cartridge"]
        })
    write_synth("ensoniq", "vfx", "Ensoniq VFX / VFX-SD", "Transwave Synthesizer Workstation", 1989,
                vfx_cc, vfx_sysex, ["Internal Bank", "Cartridge Bank"], vfx_presets)

    # ==========================================
    # 24. ENSONIQ TS-10 / TS-12
    # ==========================================
    ts_cc = vfx_cc
    ts_sysex = {"header": "F0 0F 08", "device_id_byte": 3, "commands": {"dump_program": "F0 0F 08 01 [prog] F7"}}
    ts_presets = []
    ts_seeds = [
        "Hyper-Wave Evolution", "True Acoustic Piano", "Orchestral Strings TS", "Fat Analog Synth",
        "Punchy Transwave Bass", "Polyphonic Aftertouch Pad", "Resonant Sweep 24dB", "Dynamic Horns"
    ]
    for p in range(1, 61):
        seed = ts_seeds[(p - 1) % len(ts_seeds)]
        cat = "Pad" if "Pad" in seed or "Strings" in seed or "Evolution" in seed else "Keys" if "Piano" in seed else "Bass" if "Bass" in seed else "Brass"
        ts_presets.append({
            "bank": "User ROM",
            "program": p,
            "name": f"TS10-{p:02d} {seed}",
            "category": cat,
            "tags": ["hyper-wave", "sample-playback", "poly-aftertouch", cat.lower()]
        })
    for p in range(1, 61):
        ts_presets.append({
            "bank": "User RAM",
            "program": p,
            "name": f"RAM Sound {p:02d}",
            "category": "User",
            "tags": ["hyper-wave", "ram"]
        })
    write_synth("ensoniq", "ts-10", "Ensoniq TS-10 / TS-12", "Performance Workstation w/ Hyper-Wave", 1993,
                ts_cc, ts_sysex, ["User ROM", "User RAM"], ts_presets)

    # ==========================================
    # 25. ENSONIQ MR RACK / MR-61
    # ==========================================
    mr_cc = {"cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93, "envelope_decay": 75}
    mr_sysex = {"header": "F0 0F 0A", "device_id_byte": 3, "commands": {"dump_sound": "F0 0F 0A 01 [prog] F7"}}
    mr_presets = []
    mr_seeds = [
        "Perfect Piano 16MB", "Ultra Warm Strings", "Punchy Transwave Bass", "Modern Dance Lead",
        "Studio Brass Section", "Organ Leslie Rotor", "Acoustic Nylon Guitar", "Ambient Dream Pad",
        "Slap Thumb Bass", "Vocal Morph Choir", "Techno Pulse Synth", "World Ethnic Flute"
    ]
    for p in range(1, 474):
        seed = mr_seeds[(p - 1) % len(mr_seeds)]
        cat = "Keys" if "Piano" in seed or "Organ" in seed else "Pad" if "Strings" in seed or "Pad" in seed or "Choir" in seed else "Bass" if "Bass" in seed else "Brass" if "Brass" in seed else "Lead"
        mr_presets.append({
            "bank": f"Sound Set Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"MR-{p:03d} {seed}",
            "category": cat,
            "tags": ["64-voice", "idea-pad", "ensoniq-sound-engine", cat.lower()]
        })
    write_synth("ensoniq", "mr-rack", "Ensoniq MR Rack / MR-61", "64-Voice Synthesizer Module", 1996,
                mr_cc, mr_sysex, [f"Sound Set Bank {i}" for i in range(1, 6)], mr_presets)

if __name__ == "__main__":
    build_wave5()
