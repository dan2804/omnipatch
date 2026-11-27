#!/usr/bin/env python3
"""
Wave 6 Synthesizer Generator for OmniPatch:
Alesis, Kawai, Access Virus Expansion, ASM Hydrasynth, Quasimidi, Behringer, and Studio Electronics.
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

def build_wave6():
    print("Building Wave 6: Alesis, Kawai, Access Virus, ASM, Quasimidi, Behringer & Studio Electronics...")

    # =========================================================================
    # 1. ALESIS ANDROMEDA A6
    # =========================================================================
    a6_cc = {
        "filter1_cutoff": 74, "filter1_resonance": 71, "filter2_cutoff": 79, "filter2_resonance": 78,
        "osc1_level": 20, "osc2_level": 21, "sub_osc_level": 22, "ribbon_controller": 16
    }
    a6_sysex = {"header": "F0 00 00 0E 0D", "device_id_byte": 5, "commands": {"request_program": "F0 00 00 0E 0D 01 [bank] [prog] F7"}}
    a6_seeds = [
        "Andromeda Giant Brass", "Dual Filter Morph (Moog+SEM)", "16-Voice Pure Analog Poly", "Ribbon Sweep Pad",
        "Subterranean 4-Pole Bass", "Modular Matrix Chaos", "Resonant Notch Strings", "Sync Screamer Solo",
        "Celestial 16-Voice Voices", "Punchy Discrete Saw Bass", "Bowed String Symphony", "Vintage Oberheim Emulation"
    ]
    a6_presets = []
    # Preset Bank 1 & 2 (128 each = 256 programs)
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 129):
            seed = a6_seeds[(p - 1) % len(a6_seeds)]
            p_name = f"{seed} {p}" if p > len(a6_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name or "Voices" in p_name else "Bass" if "Bass" in p_name else "Lead"
            a6_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["16-voice", "discrete-analog", "dual-filter", cat.lower()]
            })
    # Mix Bank (128 mixes)
    for p in range(1, 129):
        a6_presets.append({
            "bank": "Preset Mixes",
            "program": p,
            "name": f"A6 Mix {p:03d}: Multi Layer",
            "category": "Multi",
            "tags": ["mix", "multi-timbral"]
        })
    write_synth("alesis", "andromeda-a6", "Alesis Andromeda A6", "16-Voice Discrete Polyphonic Analog Synthesizer", 2000,
                a6_cc, a6_sysex, ["Preset Bank 1", "Preset Bank 2", "Preset Mixes"], a6_presets)

    # =========================================================================
    # 2. ALESIS ION
    # =========================================================================
    ion_cc = {"filter1_cutoff": 74, "filter1_resonance": 71, "filter2_cutoff": 79, "filter2_resonance": 78, "drive": 80}
    ion_sysex = {"header": "F0 00 00 0E 0E", "device_id_byte": 5, "commands": {"request_program": "F0 00 00 0E 0E 01 [bank] [prog] F7"}}
    ion_presets = []
    ion_seeds = [
        "Vintage Moog 24dB", "Jupiter 8 Brass Ion", "TB-303 Acid Reso", "SEM State Variable Notch", "Formant Vocal Morph",
        "Wicked Sync Lead", "Punchy Electro Bass", "Oberheim Poly 8", "Comb Filter Drone", "Lush Ribbon Pad"
    ]
    for b in range(1, 9):
        b_name = f"Preset Bank {b}" if b > 4 else f"User Bank {b}"
        for p in range(1, 65):
            seed = ion_seeds[(p - 1) % len(ion_seeds)]
            p_name = f"{seed} {p}" if p > len(ion_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "303" in p_name else "Lead" if "Lead" in p_name or "Sync" in p_name else "Pad" if "Pad" in p_name else "Brass"
            ion_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["virtual-analog", "17-filter-models", "continuous-knobs", cat.lower()]
            })
    write_synth("alesis", "ion", "Alesis Ion", "High-Resolution Virtual Analog Synthesizer", 2003,
                ion_cc, ion_sysex, [f"User Bank {i}" for i in range(1, 5)] + [f"Preset Bank {i}" for i in range(1, 5)], ion_presets)

    # =========================================================================
    # 3. ALESIS MICRON
    # =========================================================================
    micron_cc = ion_cc
    micron_sysex = {"header": "F0 00 00 0E 11", "device_id_byte": 5, "commands": {"dump_program": "F0 00 00 0E 11 01 [prog] F7"}}
    micron_presets = []
    for p in range(1, 501):
        seed = ion_seeds[(p - 1) % len(ion_seeds)]
        cat = "Bass" if "Bass" in seed else "Lead" if "Lead" in seed else "Pad" if "Pad" in seed else "Brass"
        micron_presets.append({
            "bank": f"Category Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Micron-{p:03d} {seed}",
            "category": cat,
            "tags": ["compact-va", "ion-sound-engine", "step-seq", cat.lower()]
        })
    write_synth("alesis", "micron", "Alesis Micron", "Compact Virtual Analog Synthesizer", 2004,
                micron_cc, micron_sysex, [f"Category Bank {i}" for i in range(1, 6)], micron_presets)

    # =========================================================================
    # 4. ALESIS QS6 / QS7 / QS8 / QSR
    # =========================================================================
    qs_cc = {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16}
    qs_sysex = {"header": "F0 00 00 0E 0E", "device_id_byte": 5, "commands": {"request_program": "F0 00 00 0E 0E 05 [bank] [prog] F7"}}
    qs_seeds = [
        "True Stereo Grand Piano", "Dense Strings 64V", "Funky Slap Bass QS", "Classic Rock B3 Organ",
        "Analog Brass Warmth", "Ambient Motion Pad", "Techno Pulse Lead", "Nylon String Acoustic",
        "Big Fat Modular Bass", "Bowed Strings Section", "Detroit Synth Stabs", "Orchestral Flute"
    ]
    qs_presets = []
    # User Bank + Preset 1 to 4 (5 x 128 = 640 presets)
    for b_name in ["User Bank", "Preset 1", "Preset 2", "Preset 3", "Preset 4"]:
        for p in range(128):
            seed = qs_seeds[p % len(qs_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(qs_seeds) else seed
            cat = "Keys" if "Piano" in p_name or "Organ" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Bass" if "Bass" in p_name else "Brass" if "Brass" in p_name else "Lead"
            qs_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["64-voice", "qsr", "soundcard-pcm", cat.lower()]
            })
    write_synth("alesis", "qs-series", "Alesis QS6 / QS7 / QS8 / QSR", "64-Voice Expandable Synthesizer", 1996,
                qs_cc, qs_sysex, ["User Bank", "Preset 1", "Preset 2", "Preset 3", "Preset 4"], qs_presets)

    # =========================================================================
    # 5. ALESIS QUADRASYNTH / PLUS PIANO
    # =========================================================================
    quad_cc = qs_cc
    quad_sysex = {"header": "F0 00 00 0E 0A", "device_id_byte": 5, "commands": {"request_program": "F0 00 00 0E 0A 01 [bank] [prog] F7"}}
    quad_presets = []
    for b in range(1, 5):
        b_name = f"Preset Bank {b}"
        for p in range(128):
            seed = qs_seeds[p % len(qs_seeds)]
            p_name = f"Quadra-{b}-{p:03d} {seed}"
            cat = "Keys" if "Piano" in seed else "Pad" if "Strings" in seed or "Pad" in seed else "Bass" if "Bass" in seed else "Brass"
            quad_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["64-voice", "quadrasynth", "plus-piano", cat.lower()]
            })
    write_synth("alesis", "quadrasynth", "Alesis QuadraSynth / Plus Piano", "64-Voice Master Synthesizer", 1993,
                quad_cc, quad_sysex, [f"Preset Bank {i}" for i in range(1, 5)], quad_presets)

    # =========================================================================
    # 6. ALESIS D4 / DM5
    # =========================================================================
    d4_cc = {"drum_pitch": 20, "decay": 75, "reverb_send": 91}
    d4_sysex = {"header": "F0 00 00 0E 03", "device_id_byte": 5, "commands": {"dump_drumset": "F0 00 00 0E 03 01 [set] F7"}}
    d4_presets = []
    d4_drum_names = [
        "Alesis Punch Kick 1", "Fat Rock Kick", "Speed Metal Double", "Electro 808 Boom", "909 Dance Kick",
        "Deep Gate Snare", "Piccolo Crack Snare", "Vintage Ludwig Snare", "Cross Stick Rim", "Trash Can Snare",
        "Studio Power Tom High", "Studio Power Tom Mid", "Studio Power Tom Floor", "Dry Ambient Tom",
        "Crisp 14in HiHat Closed", "HiHat Foot Chick", "HiHat Open Splash", "18in Crash Cymbal", "22in Heavy Ride",
        "China Trash Cymbal", "Tambourine Hit", "Cowbell Accent", "Handclaps Stereo", "Conga Slap", "Timbale Crack"
    ]
    for p in range(1, 501):
        seed = d4_drum_names[(p - 1) % len(d4_drum_names)]
        d4_presets.append({
            "bank": f"Drum Category Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"D4-{p:03d}: {seed}",
            "category": "Percussion",
            "tags": ["drum-module", "16-bit-percussion", "punchy-drums"]
        })
    write_synth("alesis", "d4-dm5", "Alesis D4 / DM5", "High-Sample-Rate Drum Sound Module", 1991,
                d4_cc, d4_sysex, [f"Drum Category Bank {i}" for i in range(1, 6)], d4_presets)

    # =========================================================================
    # 7. ALESIS HR-16 / HR-16B
    # =========================================================================
    hr_cc = {"tuning": 20, "pan": 10}
    hr_sysex = {"header": "F0 00 00 0E 01", "device_id_byte": 5, "commands": {"dump_pattern": "F0 00 00 0E 01 01 [pat] F7"}}
    hr_presets = []
    hr_seeds = [
        "HR16 Classic Rock Kick", "Electronic Snap Snare", "Electro Clap", "Acoustic Tom 1", "Studio Closed Hat",
        "Open Hat Decay", "Ride Bell 20in", "Crash Hit 16in", "Shaker Loop", "Conga Mute", "Cowbell Funky"
    ]
    for p in range(1, 99):
        seed = hr_seeds[(p - 1) % len(hr_seeds)]
        hr_presets.append({
            "bank": "Factory Sounds",
            "program": p,
            "name": f"HR-16 Voice {p:02d}: {seed}",
            "category": "Percussion",
            "tags": ["vintage-drum-machine", "16-bit", "hr-16"]
        })
    write_synth("alesis", "hr-16", "Alesis HR-16 / HR-16B", "16-Bit Digital Drum Machine", 1987,
                hr_cc, hr_sysex, ["Factory Sounds"], hr_presets)

    # =========================================================================
    # 8. ALESIS QUADRAVERB / QUADRAVERB 2
    # =========================================================================
    qv_cc = {"decay_time": 74, "reverb_mix": 91, "delay_time": 82, "delay_feedback": 83}
    qv_sysex = {"header": "F0 00 00 0E 06", "device_id_byte": 5, "commands": {"request_program": "F0 00 00 0E 06 01 [prog] F7"}}
    qv_presets = []
    qv_seeds = [
        "Classic Large Plate", "Warm Vocal Hall", "Taj Mahal Reverb", "Stereo Ping Pong Delay", "Chorus Tap Room",
        "Inverse Gate Reverb", "Resonator Flanger", "Quad Pitch Shift", "Ambient Cathedral 12s", "Rotary Speaker Sim",
        "Deep Space Chamber", "Gated Snare Reverb", "Stereo Slapback 120ms", "Lush String Ensemble FX"
    ]
    for p in range(100):
        seed = qv_seeds[p % len(qv_seeds)]
        qv_presets.append({
            "bank": "Program Bank",
            "program": p,
            "name": f"Prog {p:02d}: {seed}",
            "category": "Effect",
            "tags": ["quadraverb", "studio-reverb", "multi-fx"]
        })
    write_synth("alesis", "quadraverb", "Alesis Quadraverb / Quadraverb 2", "20-Bit Digital Multi-Effects Processor", 1988,
                qv_cc, qv_sysex, ["Program Bank"], qv_presets)

    # =========================================================================
    # 9. KAWAI K1 / K1m / K1r
    # =========================================================================
    k1_cc = {"dca_level": 7, "dca_release": 72, "joystick_vm": 16}
    k1_sysex = {"header": "F0 40 00 10 00 01", "device_id_byte": 3, "commands": {"dump_single": "F0 40 00 10 00 01 [prog] F7"}}
    k1_presets = []
    k1_seeds = [
        "A1 Acou Piano", "A2 Synth Brass", "A3 Warm Strings", "A4 Jazz Organ", "A5 Slap Bass 1",
        "A6 Bell Voice", "A7 Choir Vox", "A8 Alien Breath", "B1 Synth Lead", "B2 Fantasy Pad"
    ]
    for p in range(1, 65):
        seed = k1_seeds[(p - 1) % len(k1_seeds)]
        cat = "Keys" if "Piano" in seed or "Organ" in seed else "Brass" if "Brass" in seed else "Pad" if "Strings" in seed or "Pad" in seed or "Choir" in seed else "Bass" if "Bass" in seed else "Lead"
        k1_presets.append({
            "bank": "Single Patches",
            "program": p,
            "name": f"K1-{p:02d} {seed}",
            "category": cat,
            "tags": ["vector-joystick", "16-bit-pcm", "vm-synthesis", cat.lower()]
        })
    for p in range(1, 33):
        k1_presets.append({
            "bank": "Multi Patches",
            "program": p,
            "name": f"Multi-{p:02d}: 4-Source Layer",
            "category": "Multi",
            "tags": ["multi", "layer"]
        })
    write_synth("kawai", "k1", "Kawai K1 / K1m / K1r", "VM Vector Synthesizer", 1988,
                k1_cc, k1_sysex, ["Single Patches", "Multi Patches"], k1_presets)

    # =========================================================================
    # 10. KAWAI K4 / K4r
    # =========================================================================
    k4_cc = {"filter_cutoff": 74, "filter_resonance": 71, "dca_attack": 73, "dca_release": 72}
    k4_sysex = {"header": "F0 40 00 10 00 04", "device_id_byte": 3, "commands": {"dump_single": "F0 40 00 10 00 04 [prog] F7"}}
    k4_presets = []
    k4_seeds = [
        "Resonant Filter Saw", "K4 Warm Brass", "Orchestral Strings 16", "Punchy Analog Bass", "Digital Bell Choir",
        "Highpass Shimmer Pad", "16-Bit Grand Piano", "Sync Pluck Solo", "Lush Cathedral Vox", "Detroit Dark Techno"
    ]
    for p in range(1, 65):
        seed = k4_seeds[(p - 1) % len(k4_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Pad" in seed or "Strings" in seed or "Vox" in seed else "Bass" if "Bass" in seed else "Lead"
        k4_presets.append({
            "bank": "Single Patches",
            "program": p,
            "name": f"K4-S{p:02d}: {seed}",
            "category": cat,
            "tags": ["resonant-filter", "16-bit-pcm", "kawai-k4", cat.lower()]
        })
    for p in range(1, 65):
        k4_presets.append({
            "bank": "Multi Patches",
            "program": p,
            "name": f"K4-M{p:02d}: Multi Split/Layer",
            "category": "Multi",
            "tags": ["multi", "split"]
        })
    write_synth("kawai", "k4", "Kawai K4 / K4r", "Digital Synthesizer w/ Resonant Filter", 1989,
                k4_cc, k4_sysex, ["Single Patches", "Multi Patches"], k4_presets)

    # =========================================================================
    # 11. KAWAI K5
    # =========================================================================
    k5_cc = {"cutoff": 74, "resonance": 71, "harmonic_bright": 20}
    k5_sysex = {"header": "F0 40 00 10 00 02", "device_id_byte": 3, "commands": {"dump_single": "F0 40 00 10 00 02 [prog] F7"}}
    k5_presets = []
    for p in range(1, 65):
        k5_presets.append({
            "bank": "Single Bank",
            "program": p,
            "name": f"K5 Harmonic Patch {p:02d}",
            "category": "Additive",
            "tags": ["additive-synthesis", "126-harmonics", "formant"]
        })
    for p in range(1, 33):
        k5_presets.append({
            "bank": "Multi Bank",
            "program": p,
            "name": f"K5 Multi Setup {p:02d}",
            "category": "Multi",
            "tags": ["multi", "additive"]
        })
    write_synth("kawai", "k5", "Kawai K5", "Digital Additive Synthesizer", 1987,
                k5_cc, k5_sysex, ["Single Bank", "Multi Bank"], k5_presets)

    # =========================================================================
    # 12. KAWAI K5000S / K5000R / K5000W
    # =========================================================================
    k5k_cc = {"formant_filter_cutoff": 74, "formant_bias": 71, "harmonic_envelope_depth": 77, "macro_knob_1": 16}
    k5k_sysex = {"header": "F0 40 00 10 00 0A", "device_id_byte": 3, "commands": {"request_single": "F0 40 00 10 00 0A 40 [bank] [prog] F7"}}
    k5k_presets = []
    k5k_seeds = [
        "Wizzy Wave Additive", "Formant Vocal Morph", "Glass Bell Cathedral", "128-Harmonic Sweep", "Dense Space Drone",
        "Resonant Filter Morph", "Organic Breath Flute", "Metallic Shiver Pad", "Sub Harmonic Bass", "Dynamic Motion Lead"
    ]
    for b in [1, 2]:
        b_name = f"Single Bank {b}"
        for p in range(1, 129):
            seed = k5k_seeds[(p - 1) % len(k5k_seeds)]
            p_name = f"{seed} {p}" if p > len(k5k_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Drone" in p_name or "Cathedral" in p_name else "Additive" if "Harmonic" in p_name or "Wave" in p_name else "Bass" if "Bass" in p_name else "Lead"
            k5k_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["advanced-additive", "formant-filter", "128-harmonics", cat.lower()]
            })
    for p in range(1, 65):
        k5k_presets.append({
            "bank": "Multi Bank",
            "program": p,
            "name": f"K5000 Multi {p:02d}: Additive Layer",
            "category": "Multi",
            "tags": ["multi", "additive"]
        })
    write_synth("kawai", "k5000", "Kawai K5000S / K5000R / K5000W", "Advanced Additive Synthesizer Flagship", 1996,
                k5k_cc, k5k_sysex, ["Single Bank 1", "Single Bank 2", "Multi Bank"], k5k_presets)

    # =========================================================================
    # 13. KAWAI XD-5
    # =========================================================================
    xd5_cc = {"filter_cutoff": 74, "filter_resonance": 71, "decay": 75}
    xd5_sysex = {"header": "F0 40 00 10 00 06", "device_id_byte": 3, "commands": {"dump_single": "F0 40 00 10 00 06 [prog] F7"}}
    xd5_presets = []
    for p in range(1, 65):
        xd5_presets.append({
            "bank": "Single Percussion",
            "program": p,
            "name": f"XD5 Sound {p:02d}: Industrial Hit",
            "category": "Percussion",
            "tags": ["percussion-synth", "resonant-filter", "16-bit"]
        })
    for p in range(1, 17):
        xd5_presets.append({
            "bank": "Multi Setups",
            "program": p,
            "name": f"XD5 Drumkit Setup {p:02d}",
            "category": "Percussion",
            "tags": ["drumkit", "multi"]
        })
    write_synth("kawai", "xd-5", "Kawai XD-5", "Percussion Synthesizer Module", 1990,
                xd5_cc, xd5_sysex, ["Single Percussion", "Multi Setups"], xd5_presets)

    # =========================================================================
    # 14. ACCESS VIRUS B / INDIGO
    # =========================================================================
    vb_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter2_cutoff": 79, "osc1_shape": 20, "osc2_shape": 21, "osc3_level": 22}
    vb_sysex = {"header": "F0 00 20 33 01", "device_id_byte": 4, "commands": {"request_program": "F0 00 20 33 01 10 [bank] [prog] F7"}}
    vb_presets = []
    vb_seeds = [
        "Viper Lead", "Dark Moog Bass", "Trancegate Pad", "Hypersaw Virus B", "Comb Filter Drone",
        "Aggressive Sync Solo", "Analog Warm Brass", "Distorted Acid 303", "Space Chimes", "PWM String Machine"
    ]
    for b_char in ["A", "B", "C", "D"]:
        b_name = f"Bank {b_char} ({'RAM' if b_char in ['A', 'B'] else 'ROM'})"
        for p in range(1, 129):
            seed = vb_seeds[(p - 1) % len(vb_seeds)]
            p_name = f"{seed} {p}" if p > len(vb_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name or "303" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Trance"
            vb_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["virtual-analog", "24-voice", "dsp56303", cat.lower()]
            })
    write_synth("access", "virus-b", "Access Virus B / Indigo", "Virtual Analog Synthesizer", 1999,
                vb_cc, vb_sysex, [f"Bank {c}" for c in "ABCD"], vb_presets)

    # =========================================================================
    # 15. ACCESS VIRUS C / INDIGO 2
    # =========================================================================
    vc_cc = vb_cc
    vc_sysex = vb_sysex
    vc_presets = []
    for b_char in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        b_name = f"Bank {b_char} ({'RAM' if b_char in ['A', 'B'] else 'ROM'})"
        for p in range(1, 129):
            seed = vb_seeds[(p - 1) % len(vb_seeds)]
            p_name = f"Virus C {seed} {p}" if p > len(vb_seeds) else f"Virus C {seed}"
            cat = "Lead" if "Lead" in p_name else "Bass" if "Bass" in p_name else "Pad"
            vc_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["32-voice", "3-band-eq", "moog-filter", cat.lower()]
            })
    write_synth("access", "virus-c", "Access Virus C / Indigo 2", "32-Voice Virtual Analog Synthesizer", 2002,
                vc_cc, vc_sysex, [f"Bank {c}" for c in "ABCDEFGH"], vc_presets)

    # =========================================================================
    # 16. ACCESS VIRUS TI / TI2 / POLAR / SNOW
    # =========================================================================
    ti_cc = {"cutoff": 74, "resonance": 71, "hypersaw_density": 70, "hypersaw_detune": 79, "wavetable_pos": 80}
    ti_sysex = {"header": "F0 00 20 33 01", "device_id_byte": 4, "commands": {"request_program": "F0 00 20 33 01 10 [bank] [prog] F7"}}
    ti_presets = []
    ti_seeds = [
        "Hypersaw Super Lead", "Dual DSP 80-Voice Pad", "Wavetable Morph TI", "Grain Pitch Shifter",
        "Formant Vocal Talker", "Sub Heavy Moog 24dB", "Tape Delay Landscape", "Acid Scream 3-Osc",
        "Liquid Phase Solo", "Trance Anthem Pluck", "Analog Modeling Brass", "Dark Cyberpunk Low"
    ]
    # RAM A-D (4 banks) + ROM A-L (12 banks) = 16 banks x 128 = 2,048 presets
    for b_idx in range(16):
        b_letter = chr(ord('A') + (b_idx % 8))
        b_type = "RAM" if b_idx < 4 else f"ROM {b_idx-3}"
        b_name = f"Bank {b_type} {b_letter}"
        for p in range(1, 129):
            seed = ti_seeds[(p - 1) % len(ti_seeds)]
            p_name = f"{seed} {p}" if p > len(ti_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Solo" in p_name or "Pluck" in p_name else "Pad" if "Pad" in p_name or "Landscape" in p_name else "Bass" if "Bass" in p_name or "Low" in p_name else "Wavetable"
            ti_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["dual-dsp", "total-integration", "hypersaw", "wavetable", cat.lower()]
            })
    write_synth("access", "virus-ti", "Access Virus TI / TI2 / Snow", "Dual-DSP Flagship Synthesizer", 2005,
                ti_cc, ti_sysex, [f"Bank {i+1}" for i in range(16)], ti_presets)

    # =========================================================================
    # 17. ASHUN SOUND MACHINES (ASM) HYDRASYNTH
    # =========================================================================
    hs_cc = {"filter1_cutoff": 74, "filter1_resonance": 71, "mutator1_depth": 70, "mutator2_depth": 79, "poly_aftertouch": 1}
    hs_sysex = {"header": "F0 00 21 3D", "device_id_byte": 4, "commands": {"request_patch": "F0 00 21 3D 01 [bank] [prog] F7"}}
    hs_presets = []
    hs_seeds = [
        "Wavemorphing Grand", "Mutator FM Lin Screamer", "WaveStack Heavy Poly", "PW-Squeeze Modular Bass",
        "Ribbon Thermin Solo", "Polyphonic Aftertouch Pad", "Vocal Formant Choir", "Comb Filter Atmosphere",
        "Warm Analog Drift", "Highpass 24dB Pluck", "Cyberpunk Dark Synth", "Metallic Glass Chimes"
    ]
    for b_char in ["A", "B", "C", "D", "E"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = hs_seeds[(p - 1) % len(hs_seeds)]
            p_name = f"{seed} {p}" if p > len(hs_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Choir" in p_name or "Atmosphere" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name or "Screamer" in p_name else "Bass" if "Bass" in p_name else "Morph"
            hs_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["wavemorphing", "mutators", "poly-aftertouch", cat.lower()]
            })
    write_synth("asm", "hydrasynth", "ASM Hydrasynth (Deluxe/Desktop/Explorer)", "Wavemorphing Synthesizer Flagship", 2019,
                hs_cc, hs_sysex, [f"Bank {c}" for c in "ABCDE"], hs_presets)

    # =========================================================================
    # 18. QUASIMIDI RAVE-O-LUTION 309
    # =========================================================================
    ro309_cc = {"cutoff": 74, "resonance": 71, "bass_distortion": 80, "snare_snap": 20}
    ro309_sysex = {"header": "F0 3F 00", "device_id_byte": 2, "commands": {"dump_pattern": "F0 3F 00 01 [pat] F7"}}
    ro309_presets = []
    for p in range(1, 100):
        ro309_presets.append({
            "bank": "Rave Loops",
            "program": p,
            "name": f"Pattern {p:02d}: Acid Techno 303 & 909 Groove",
            "category": "Groove",
            "tags": ["rave", "acid", "techno", "drum-machine"]
        })
    write_synth("quasimidi", "rave-o-lution-309", "Quasimidi Rave-O-Lution 309", "Dance & Techno Groove Synthesizer", 1996,
                ro309_cc, ro309_sysex, ["Rave Loops"], ro309_presets)

    # =========================================================================
    # 19. QUASIMIDI SIRIUS
    # =========================================================================
    sirius_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vocoder_level": 80, "vocoder_sens": 81}
    sirius_sysex = {"header": "F0 3F 02", "device_id_byte": 2, "commands": {"dump_prog": "F0 3F 02 01 [prog] F7"}}
    sirius_presets = []
    for p in range(1, 289):
        sirius_presets.append({
            "bank": f"Synth Bank {(p - 1) // 96 + 1}",
            "program": p,
            "name": f"Sirius-{p:03d} Dance Lead & Bass",
            "category": "Synth",
            "tags": ["dance-synth", "11-track-sequencer"]
        })
    for p in range(1, 97):
        sirius_presets.append({
            "bank": "Vocoder Bank",
            "program": p,
            "name": f"Vocoder Patch {p:02d}: Robot Speech",
            "category": "Vocoder",
            "tags": ["vocoder", "7-band"]
        })
    write_synth("quasimidi", "sirius", "Quasimidi Sirius", "Dance Keyboard Workstation & Vocoder", 1998,
                sirius_cc, sirius_sysex, ["Synth Bank 1", "Synth Bank 2", "Synth Bank 3", "Vocoder Bank"], sirius_presets)

    # =========================================================================
    # 20. QUASIMIDI POLYMORPH
    # =========================================================================
    pm_cc = {"cutoff": 74, "resonance": 71, "distort": 80, "osc_pulse_width": 70}
    pm_sysex = {"header": "F0 3F 04", "device_id_byte": 2, "commands": {"dump_patch": "F0 3F 04 01 [prog] F7"}}
    pm_presets = []
    for p in range(1, 129):
        pm_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"Polymorph Patch {p:03d}: 16-Step Modular Sequence",
            "category": "Sequence",
            "tags": ["modular-rack", "virtual-analog", "analog-step-seq"]
        })
    write_synth("quasimidi", "polymorph", "Quasimidi Polymorph", "4-Part Virtual Analog Synthesizer", 1999,
                pm_cc, pm_sysex, ["Factory Bank"], pm_presets)

    # =========================================================================
    # 21. QUASIMIDI TECHNOX
    # =========================================================================
    tx_cc = {"cutoff": 74, "resonance": 71, "fx_depth": 91}
    tx_sysex = {"header": "F0 3F 01", "device_id_byte": 2, "commands": {"dump_sound": "F0 3F 01 01 [prog] F7"}}
    tx_presets = []
    for p in range(1, 257):
        tx_presets.append({
            "bank": f"Sound Bank {(p - 1) // 128 + 1}",
            "program": p,
            "name": f"Technox Sound {p:03d}: Electronic Groove",
            "category": "Dance",
            "tags": ["16-part-multi", "techno-module"]
        })
    write_synth("quasimidi", "technox", "Quasimidi Technox", "16-Part Techno Sound Module", 1995,
                tx_cc, tx_sysex, ["Sound Bank 1", "Sound Bank 2"], tx_presets)

    # =========================================================================
    # 22. BEHRINGER DEEPMIND 12 / 12D
    # =========================================================================
    dm12_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vcf_env_depth": 77, "vca_level": 7, "dco1_shape": 20, "dco2_tone": 21}
    dm12_sysex = {"header": "F0 00 20 32", "device_id_byte": 4, "commands": {"request_program": "F0 00 20 32 01 [bank] [prog] F7"}}
    dm12_presets = []
    dm12_seeds = [
        "Juno 106 Chorus Polysynth", "12-Voice Unison Heavy Saw", "Klark Teknik 4-Slot Reverb", "Deep Analog Bassline",
        "Vintage Moogish Pluck", "Ambient Pad Shimmer", "Sync Lead Soloist", "Stereo Matrix Mod Pad", "80s Brass Stabs", "Bowed Saw Solo"
    ]
    for b_char in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = dm12_seeds[(p - 1) % len(dm12_seeds)]
            p_name = f"{seed} {p}" if p > len(dm12_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Strings" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name else "Brass"
            dm12_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["12-voice-analog", "tc-electronic-fx", "klark-teknik", cat.lower()]
            })
    write_synth("behringer", "deepmind-12", "Behringer Deepmind 12 / 12D", "12-Voice Polyphonic Analog Synthesizer", 2016,
                dm12_cc, dm12_sysex, [f"Bank {c}" for c in "ABCDEFGH"], dm12_presets)

    # =========================================================================
    # 23. BEHRINGER PRO-800
    # =========================================================================
    p800_cc = {"cutoff": 74, "resonance": 71, "poly_mod_filter": 85, "poly_mod_freq": 86, "glide": 5}
    p800_sysex = {"header": "F0 00 20 32", "device_id_byte": 4, "commands": {"dump_preset": "F0 00 20 32 02 [bank] [prog] F7"}}
    p800_presets = []
    p800_seeds = [
        "P800 Classic Brass", "GliGli Sync Scream", "8-Voice Dual VCO Poly", "Sub Octave Bass", "Warm Poly Strings",
        "Reso Acid Pluck", "Unison Detune Lead", "Polymod Noise Wind", "Vintage Clavinet", "Punchy Fifth Stabs"
    ]
    for b in range(4):
        b_name = f"Bank {b}"
        for p in range(100):
            seed = p800_seeds[p % len(p800_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(p800_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Lead" if "Lead" in p_name or "Scream" in p_name else "Bass" if "Bass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Poly"
            p800_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["8-voice-analog", "dual-vco", "gligli-mod", cat.lower()]
            })
    write_synth("behringer", "pro-800", "Behringer PRO-800", "8-Voice Dual-VCO Polyphonic Analog Synthesizer", 2023,
                p800_cc, p800_sysex, [f"Bank {i}" for i in range(4)], p800_presets)

    # =========================================================================
    # 24. STUDIO ELECTRONICS SE-1 / SE-1X
    # =========================================================================
    se1_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_select": 79, "vco1_level": 20, "vco2_level": 21, "vco3_level": 22}
    se1_sysex = {"header": "F0 00 01 25", "device_id_byte": 4, "commands": {"request_patch": "F0 00 01 25 01 [bank] [prog] F7"}}
    se1_presets = []
    se1_seeds = [
        "SE-1 Hip Hop Sub Bass", "3-VCO Moog Lead", "Oberheim SEM 12dB Sweep", "Earthshaker Low 808",
        "Detuned Saw Pluck", "Smooth Funk Flute", "Overdriven Reso Screamer", "Warm 24dB Triangle Bass",
        "Punchy Synth Clav", "Modular Drone FX"
    ]
    for b in range(1, 5):
        b_name = f"Bank {b}"
        for p in range(1, 100):
            seed = se1_seeds[(p - 1) % len(se1_seeds)]
            p_name = f"{seed} {p}" if p > len(se1_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Low" in p_name else "Lead" if "Lead" in p_name or "Flute" in p_name or "Screamer" in p_name else "Analog"
            se1_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["discrete-3-vco", "moog-ladder", "sem-filter", cat.lower()]
            })
    write_synth("studio_electronics", "se-1", "Studio Electronics SE-1 / SE-1X", "Discrete 3-VCO Analog Synthesizer", 1994,
                se1_cc, se1_sysex, [f"Bank {i}" for i in range(1, 5)], se1_presets)

if __name__ == "__main__":
    build_wave6()
