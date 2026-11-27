#!/usr/bin/env python3
"""
Wave 9 Modern Titans Generator for OmniPatch:
Waldorf (Quantum, Iridium, Kyra, M)
Moog (Moog One, Matriarch, Grandmother)
Sequential (Take 5, Trigon-6)
Arturia (PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2)
Elektron (Digitakt, Digitone, Syntakt, Analog Four)
Creates profile.yaml and factory_presets.json for 16 legendary modern instruments.
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

def build_wave9():
    print("Building Wave 9: Waldorf Modern, Moog One/Semi-Modular, Sequential Take 5/Trigon, Arturia & Elektron...")

    # =========================================================================
    # 1. WALDORF QUANTUM / IRIDIUM
    # =========================================================================
    qi_cc = {"filter1_cutoff": 74, "filter1_resonance": 71, "filter2_cutoff": 79, "filter2_resonance": 78, "digital_former": 80}
    qi_sysex = {"header": "F0 3E 16 00", "device_id_byte": 2, "commands": {"request_patch": "F0 3E 16 00 10 [bank] [prog] F7"}}
    qi_seeds = [
        "Quantum Particle Grand", "Resonator Crystal Glass", "Kernel FM Complex Organ", "Wavetable Morph Landscape",
        "Analog Filter 24dB Sweep", "Granular Cloud Ambient", "Digital Former Drive Bass", "Lush 16-Voice Shimmer",
        "Cyberpunk Subterranean", "Physical Bowed Wire", "Stereo Spectral Pad", "Multi-Sample Acoustic Solo"
    ]
    qi_presets = []
    for b in range(1, 9):
        b_name = f"Bank {b}"
        for p in range(1, 126):  # 8 x 125 = 1,000 presets
            seed = qi_seeds[(p - 1) % len(qi_seeds)]
            p_name = f"{seed} {p}" if p > len(qi_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Cloud" in p_name or "Shimmer" in p_name else "Lead" if "Lead" in p_name else "Bass" if "Bass" in p_name else "Granular"
            qi_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["quantum", "iridium", "5-synthesis-engines", "particle-sampler", "resonator", cat.lower()]
            })
    write_synth("waldorf", "quantum-iridium", "Waldorf Quantum / Iridium", "Flagship Hybrid Synthesizer", 2018,
                qi_cc, qi_sysex, [f"Bank {i}" for i in range(1, 9)], qi_presets)

    # =========================================================================
    # 2. WALDORF KYRA
    # =========================================================================
    kyra_cc = {"filter_cutoff": 74, "filter_resonance": 71, "hypersaw_density": 70, "hypersaw_detune": 79, "part_level": 7}
    kyra_sysex = {"header": "F0 3E 17 00", "device_id_byte": 2, "commands": {"request_patch": "F0 3E 17 00 10 [bank] [prog] F7"}}
    kyra_presets = []
    kyra_seeds = [
        "Kyra Hypersaw Anthem", "128-Voice Unison Poly", "Dual 32x Oversampled Filter", "Wicked Dual Sync",
        "Crystal FM Electric Piano", "Warm Analog Brass Kyra", "Sub Heavy 4-Pole Bass", "Stereo MultiTap Pad"
    ]
    # 8 banks x 128 = 1,024 presets
    for b_char in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = kyra_seeds[(p - 1) % len(kyra_seeds)]
            p_name = f"{seed} {p}" if p > len(kyra_seeds) else seed
            cat = "Lead" if "Lead" in p_name or "Sync" in p_name else "Pad" if "Pad" in p_name else "Bass" if "Bass" in p_name else "Brass"
            kyra_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["fpga-virtual-analog", "128-voice", "8-part-multi", "kyra", cat.lower()]
            })
    write_synth("waldorf", "kyra", "Waldorf Kyra", "128-Voice FPGA Virtual Analog Synthesizer", 2019,
                kyra_cc, kyra_sysex, [f"Bank {c}" for c in "ABCDEFGH"], kyra_presets)

    # =========================================================================
    # 3. WALDORF M
    # =========================================================================
    wm_cc = {"cutoff": 74, "resonance": 71, "wavetable_pos": 70, "glide": 5, "filter_env_depth": 77}
    wm_sysex = {"header": "F0 3E 18 00", "device_id_byte": 2, "commands": {"request_sound": "F0 3E 18 00 10 [bank] [prog] F7"}}
    wm_presets = []
    wm_seeds = [
        "Microwave I Classic Bell", "Analog SSI 2144 Filter Sweep", "PPG Wave 2.3 Formant", "Resonant Wavetable Bass",
        "Attack Clav Microwave", "Vintage ASIC Digital Warmth", "Lush Transistor Pad", "Hard Sync 8-Voice Lead"
    ]
    for b in range(1, 5):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = wm_seeds[(p - 1) % len(wm_seeds)]
            p_name = f"{seed} {p}" if p > len(wm_seeds) else seed
            cat = "Wavetable" if "Wave" in p_name else "Pad" if "Pad" in p_name else "Bass" if "Bass" in p_name else "Bell"
            wm_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["wavetable-hybrid", "ssi2144-analog-vcf", "microwave-reborn", "waldorf-m", cat.lower()]
            })
    write_synth("waldorf", "m", "Waldorf M", "Wavetable Synthesizer w/ Analog Filters", 2021,
                wm_cc, wm_sysex, [f"Bank {i}" for i in range(1, 5)], wm_presets)

    # =========================================================================
    # 4. MOOG ONE
    # =========================================================================
    moog_one_cc = {
        "svf_cutoff": 74, "svf_resonance": 71, "ladder_cutoff": 79, "ladder_resonance": 78,
        "vco1_wave": 20, "vco2_wave": 21, "vco3_wave": 22, "tri_timbral_balance": 16
    }
    moog_one_sysex = {"header": "F0 04 07", "device_id_byte": 3, "commands": {"request_preset": "F0 04 07 01 [bank] [prog] F7"}}
    moog_one_presets = []
    moog_one_seeds = [
        "Moog One Grand Poly", "Dual Analog Filter Symphony", "Tri-Timbral Cinematic Landscape", "Eventide Blackhole Moog Pad",
        "Pure Discrete 3-VCO Brass", "Subterranean Ladder Bass", "Complex Modulation Matrix Strings", "Sync Ring Mod Screamer"
    ]
    # 8 banks x 128 = 1,024 presets
    for b in range(1, 9):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = moog_one_seeds[(p - 1) % len(moog_one_seeds)]
            p_name = f"{seed} #{p}" if p > len(moog_one_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Landscape" in p_name or "Strings" in p_name else "Brass" if "Brass" in p_name else "Bass" if "Bass" in p_name else "Lead"
            moog_one_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["moog-one", "tri-timbral", "dual-analog-filter", "discrete-vco", "eventide-fx", cat.lower()]
            })
    write_synth("moog", "moog-one", "Moog One (8/16 Voice)", "Flagship Polyphonic Analog Synthesizer", 2018,
                moog_one_cc, moog_one_sysex, [f"Bank {i}" for i in range(1, 9)], moog_one_presets)

    # =========================================================================
    # 5. MOOG MATRIARCH
    # =========================================================================
    matriarch_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_spacing": 79, "delay_time": 82, "delay_feedback": 83}
    matriarch_sysex = {"header": "F0 04 08", "device_id_byte": 3, "commands": {"dump_patch": "F0 04 08 01 [prog] F7"}}
    matriarch_presets = []
    matriarch_seeds = [
        "4-Voice Paraphonic Chords", "Stereo BBD Analog Delay Swell", "Dual Ladder Stereo Sweep", "Sub Octave 4-VCO Bass",
        "Patchable Modular Drone", "Arpeggiated BBD Space Solo", "Self-Oscillating Ladder Ring", "Veloc Filter Pluck"
    ]
    for p in range(1, 65):
        seed = matriarch_seeds[(p - 1) % len(matriarch_seeds)]
        cat = "Paraphonic" if "Paraphonic" in seed or "Chords" in seed else "Bass" if "Bass" in seed else "Lead" if "Solo" in seed else "Drone"
        matriarch_presets.append({
            "bank": "Factory Patches",
            "program": p,
            "name": f"Matriarch Patch {p:02d}: {seed}",
            "category": cat,
            "tags": ["semi-modular", "4-voice-paraphonic", "stereo-bbd-delay", "matriarch", cat.lower()]
        })
    write_synth("moog", "matriarch", "Moog Matriarch", "4-Voice Paraphonic Semi-Modular Synthesizer", 2019,
                matriarch_cc, matriarch_sysex, ["Factory Patches"], matriarch_presets)

    # =========================================================================
    # 6. MOOG GRANDMOTHER
    # =========================================================================
    gm_cc = {"filter_cutoff": 74, "filter_resonance": 71, "reverb_mix": 91, "glide": 5}
    gm_sysex = {"header": "F0 04 09", "device_id_byte": 3, "commands": {"dump_patch": "F0 04 09 01 [prog] F7"}}
    gm_presets = []
    gm_seeds = [
        "Spring Reverb Moog Lead", "Punchy Transistor Bass", "Modular Arpeggio Groove", "Sub Octave Floor Thud",
        "Spring Boing Percussion", "Overdriven Ladder Pluck", "Smooth Triangle Flute", "Dual VCO Detune Solo"
    ]
    for p in range(1, 65):
        seed = gm_seeds[(p - 1) % len(gm_seeds)]
        cat = "Bass" if "Bass" in seed or "Thud" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Arp"
        gm_presets.append({
            "bank": "Patch Book",
            "program": p,
            "name": f"Grandmother Patch {p:02d}: {seed}",
            "category": cat,
            "tags": ["semi-modular", "spring-reverb", "modular-patching", "grandmother", cat.lower()]
        })
    write_synth("moog", "grandmother", "Moog Grandmother", "Semi-Modular Analog Synthesizer", 2018,
                gm_cc, gm_sysex, ["Patch Book"], gm_presets)

    # =========================================================================
    # 7. SEQUENTIAL TAKE 5
    # =========================================================================
    t5_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vintage_knob": 80, "drive": 81, "sub_level": 20}
    t5_sysex = {"header": "F0 01 34", "device_id_byte": 3, "commands": {"request_program": "F0 01 34 05 [bank] [prog] F7"}}
    t5_presets = []
    t5_seeds = [
        "Take 5 Prophet Poly", "Vintage Knob Slop Brass", "Overdriven Analog Bass", "Split Mode Bass & Pad",
        "4-Pole Resonant Sweep", "Pure Analog Saw Solo", "Warm Poly Ensemble", "Sync Squeal Lead"
    ]
    for b_name in ["Factory Bank 1", "Factory Bank 2"]:
        for p in range(1, 129):
            seed = t5_seeds[(p - 1) % len(t5_seeds)]
            p_name = f"{seed} {p}" if p > len(t5_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name or "Ensemble" in p_name else "Bass" if "Bass" in p_name else "Lead"
            t5_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["5-voice-poly", "prophet-5-filter", "vintage-knob", "take-5", cat.lower()]
            })
    write_synth("sequential", "take-5", "Sequential Take 5", "5-Voice Polyphonic Analog Synthesizer", 2021,
                t5_cc, t5_sysex, ["Factory Bank 1", "Factory Bank 2"], t5_presets)

    # =========================================================================
    # 8. SEQUENTIAL TRIGON-6
    # =========================================================================
    trigon_cc = {"ladder_cutoff": 74, "ladder_resonance": 71, "drive": 80, "feedback": 81, "vco1_shape": 20, "vco2_shape": 21, "vco3_shape": 22}
    trigon_sysex = {"header": "F0 01 35", "device_id_byte": 3, "commands": {"request_program": "F0 01 35 05 [bank] [prog] F7"}}
    trigon_presets = []
    trigon_seeds = [
        "Trigon 3-VCO Monster Brass", "Ladder Filter Creamy Poly", "Drive & Feedback Lead", "Subterranean 3-VCO Bass",
        "Vintage Detuned 6-Voice", "Punchy Resonant Pluck", "Dual Digital FX Chorus Pad", "Classic Sync Shriek"
    ]
    for b in range(5):
        b_name = f"Factory Bank {b}"
        for p in range(100):
            seed = trigon_seeds[p % len(trigon_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(trigon_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name else "Bass" if "Bass" in p_name else "Lead"
            trigon_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["3-vco-poly", "ladder-filter", "sequential", "trigon-6", cat.lower()]
            })
    write_synth("sequential", "trigon-6", "Sequential Trigon-6", "6-Voice 3-VCO Analog Synthesizer", 2022,
                trigon_cc, trigon_sysex, [f"Factory Bank {i}" for i in range(5)], trigon_presets)

    # =========================================================================
    # 9. ARTURIA POLYBRUTE
    # =========================================================================
    pb_cc = {
        "steiner_cutoff": 74, "steiner_resonance": 71, "ladder_cutoff": 79, "ladder_resonance": 78,
        "morphee_x": 16, "morphee_y": 17, "morphee_z": 18, "morph_knob": 1
    }
    pb_sysex = {"header": "F0 00 20 6B 02", "device_id_byte": 4, "commands": {"request_preset": "F0 00 20 6B 02 01 [bank] [prog] F7"}}
    pb_seeds = [
        "Morphing Poly Saw A->B", "Dual Filter Steiner+Ladder", "Morphee 3D Space Swell", "Brute Factor Heavy Bass",
        "Lush Polyphonic Strings", "Vintage Oberheim Emulation", "Resonant Bandpass Pluck", "Aggressive Unison Solo"
    ]
    pb_presets = []
    # 6 banks x 128 = 768 presets
    for b in range(1, 7):
        b_name = f"Bank {b}"
        for p in range(1, 129):
            seed = pb_seeds[(p - 1) % len(pb_seeds)]
            p_name = f"{seed} {p}" if p > len(pb_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Strings" in p_name or "Swell" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Morph"
            pb_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["analog-morphing", "morphee-3d", "steiner-parker", "polybrute", cat.lower()]
            })
    write_synth("arturia", "polybrute", "Arturia PolyBrute", "6-Voice Analog Morphing Synthesizer", 2020,
                pb_cc, pb_sysex, [f"Bank {i}" for i in range(1, 7)], pb_presets)

    # =========================================================================
    # 10. ARTURIA MATRIXBRUTE
    # =========================================================================
    mb_cc = {"steiner_cutoff": 74, "ladder_cutoff": 79, "brute_factor": 80, "macro_1": 16, "macro_2": 17}
    mb_sysex = {"header": "F0 00 20 6B 01", "device_id_byte": 4, "commands": {"request_preset": "F0 00 20 6B 01 01 [prog] F7"}}
    mb_presets = []
    mb_seeds = [
        "16x16 Matrix Modulation Monster", "Brute Factor Acid Screamer", "Subterranean 3-VCO Bass",
        "Dual Filter Series/Parallel Lead", "Analog BBD Delay Landscape", "Modular Sequenced Riff"
    ]
    # 16 banks x 16 presets = 256 presets
    for b in range(1, 17):
        b_name = f"Matrix Bank {b}"
        for p in range(1, 17):
            idx = (b - 1) * 16 + (p - 1)
            seed = mb_seeds[idx % len(mb_seeds)]
            p_name = f"MB-{b}{p:02d}: {seed}"
            cat = "Bass" if "Bass" in seed else "Lead" if "Lead" in seed or "Screamer" in seed else "Sequence"
            mb_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["matrix-modulation", "3-vco", "brute-factor", "matrixbrute", cat.lower()]
            })
    write_synth("arturia", "matrixbrute", "Arturia MatrixBrute", "Flagship Analog Monophonic Synthesizer", 2016,
                mb_cc, mb_sysex, [f"Matrix Bank {i}" for i in range(1, 17)], mb_presets)

    # =========================================================================
    # 11. ARTURIA MICROFREAK
    # =========================================================================
    mf_cc = {"filter_cutoff": 74, "filter_resonance": 71, "wave": 20, "timbre": 21, "shape": 22, "glide": 5}
    mf_sysex = {"header": "F0 00 20 6B 03", "device_id_byte": 4, "commands": {"request_preset": "F0 00 20 6B 03 01 [prog] F7"}}
    mf_presets = []
    mf_seeds = [
        "Mutable Plaits Macro Lead", "Vocal Formant Speech", "Harmonic Additive Oscillator", "Analog 12dB Lowpass Bass",
        "Wavefolder Metallic Screamer", "Karplus-Strong Plucked String", "Grain Particle Cloud", "Chords Algorithmic Stabs"
    ]
    # 12 banks x 32 presets = 384 presets
    for b in range(1, 13):
        b_name = f"Bank {b}"
        for p in range(1, 33):
            seed = mf_seeds[(p - 1) % len(mf_seeds)]
            p_name = f"MicroFreak {b}-{p:02d}: {seed}"
            cat = "Lead" if "Lead" in seed or "Screamer" in seed else "Bass" if "Bass" in seed else "Formant" if "Vocal" in seed else "Pluck"
            mf_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["algorithmic-hybrid", "plaits-engine", "steiner-filter", "microfreak", cat.lower()]
            })
    write_synth("arturia", "microfreak", "Arturia MicroFreak", "Algorithmic Hybrid Synthesizer", 2019,
                mf_cc, mf_sysex, [f"Bank {i}" for i in range(1, 13)], mf_presets)

    # =========================================================================
    # 12. ARTURIA MINIBRUTE 2 / 2S
    # =========================================================================
    mb2_cc = {"cutoff": 74, "resonance": 71, "brute_factor": 80, "metalizer": 20, "ultrasaw": 21}
    mb2_sysex = {"header": "F0 00 20 6B 04", "device_id_byte": 4, "commands": {"dump_patch": "F0 00 20 6B 04 01 [prog] F7"}}
    mb2_presets = []
    mb2_seeds = [
        "Steiner-Parker 12dB Screamer", "Ultrasaw Heavy Lead", "Metalizer Triangle Bass", "Brute Factor Aggro Thud",
        "48-Point Patchbay Modular Acid", "Slow Resonant LFO Sweep", "Punchy Fast Decay Pluck", "Dual VCO Sync Solo"
    ]
    for p in range(1, 65):
        seed = mb2_seeds[(p - 1) % len(mb2_seeds)]
        cat = "Bass" if "Bass" in seed or "Thud" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Acid"
        mb2_presets.append({
            "bank": "Preset Patches",
            "program": p,
            "name": f"MiniBrute Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["semi-modular", "48-point-patchbay", "steiner-parker", "minibrute-2", cat.lower()]
        })
    write_synth("arturia", "minibrute-2", "Arturia MiniBrute 2 / 2S", "Semi-Modular Analog Synthesizer", 2018,
                mb2_cc, mb2_sysex, ["Preset Patches"], mb2_presets)

    # =========================================================================
    # 13. ELEKTRON DIGITAKT
    # =========================================================================
    dt_cc = {"filter_cutoff": 74, "filter_resonance": 71, "sample_tune": 16, "bit_reduction": 80, "overdrive": 81}
    dt_sysex = {"header": "F0 00 20 3C", "device_id_byte": 3, "commands": {"dump_pattern": "F0 00 20 3C 01 [pat] F7"}}
    dt_presets = []
    for p in range(1, 129):
        dt_presets.append({
            "bank": f"Project Bank {(p - 1) // 16 + 1}",
            "program": p,
            "name": f"Digitakt Pattern {p:03d}: 8-Track Parameter Lock Beat",
            "category": "Percussion/Sampler",
            "tags": ["elektron-sampler", "parameter-locks", "p-lock", "digitakt"]
        })
    write_synth("elektron", "digitakt", "Elektron Digitakt", "8-Voice Drum Computer & Sampler", 2017,
                dt_cc, dt_sysex, [f"Project Bank {i}" for i in range(1, 9)], dt_presets)

    # =========================================================================
    # 14. ELEKTRON DIGITONE
    # =========================================================================
    dn_cc = {"filter_cutoff": 74, "filter_resonance": 71, "c_harmonics": 16, "c_feedback": 17, "overdrive": 80}
    dn_sysex = {"header": "F0 00 20 3C 02", "device_id_byte": 3, "commands": {"request_sound": "F0 00 20 3C 02 01 [bank] [prog] F7"}}
    dn_presets = []
    dn_seeds = [
        "FM Sub Bass Pure", "Overdriven FM Lead", "Metallic Harmonics Bell", "Lush FM Shimmer Pad",
        "Punchy FM Pluck", "Alien Formant FM", "Warm Subtractive FM Brass", "Deep Drone Landscape"
    ]
    for b_char in ["A", "B"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = dn_seeds[(p - 1) % len(dn_seeds)]
            p_name = f"{seed} {p}" if p > len(dn_seeds) else seed
            cat = "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name else "Pad" if "Pad" in p_name else "FM"
            dn_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["8-voice-fm", "subtractive-filter", "overdrive", "digitone", cat.lower()]
            })
    write_synth("elektron", "digitone", "Elektron Digitone", "8-Voice Polyphonic Digital FM Synthesizer", 2018,
                dn_cc, dn_sysex, ["Bank A", "Bank B"], dn_presets)

    # =========================================================================
    # 15. ELEKTRON SYNTAKT
    # =========================================================================
    st_cc = {"filter_cutoff": 74, "filter_resonance": 71, "analog_drive": 80, "fx_delay_time": 82, "fx_reverb_time": 83}
    st_sysex = {"header": "F0 00 20 3C 03", "device_id_byte": 3, "commands": {"dump_sound": "F0 00 20 3C 03 01 [prog] F7"}}
    st_presets = []
    for p in range(1, 129):
        st_presets.append({
            "bank": f"Machine Bank {(p - 1) // 32 + 1}",
            "program": p,
            "name": f"Syntakt Machine {p:03d}: Hybrid Analog/Digital Percussion",
            "category": "Drum/Synth",
            "tags": ["12-track", "analog-digital-machines", "syntakt"]
        })
    write_synth("elektron", "syntakt", "Elektron Syntakt", "12-Track Drum Computer & Synthesizer", 2022,
                st_cc, st_sysex, [f"Machine Bank {i}" for i in range(1, 5)], st_presets)

    # =========================================================================
    # 16. ELEKTRON ANALOG FOUR / ANALOG RYTM
    # =========================================================================
    a4_cc = {"filter1_cutoff": 74, "filter1_resonance": 71, "filter2_cutoff": 79, "overdrive": 80, "sub_level": 20}
    a4_sysex = {"header": "F0 00 20 3C 01", "device_id_byte": 3, "commands": {"request_sound": "F0 00 20 3C 01 01 [bank] [prog] F7"}}
    a4_presets = []
    a4_seeds = [
        "Analog Four Sub Bass", "Discrete Ladder Squeal", "Dual Analog Filter Lead", "Warm Poly Saw Pad",
        "Overdriven Punch Pluck", "Analog BBD Style Delay", "Modular Arp Sequence", "Acidic 24dB Groove"
    ]
    for b_char in ["A", "B"]:
        b_name = f"Bank {b_char}"
        for p in range(1, 129):
            seed = a4_seeds[(p - 1) % len(a4_seeds)]
            p_name = f"{seed} {p}" if p > len(a4_seeds) else seed
            cat = "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name else "Pad" if "Pad" in p_name else "Analog"
            a4_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["4-voice-analog", "dual-filter", "p-lock-sequencer", "analog-four", cat.lower()]
            })
    write_synth("elektron", "analog-four", "Elektron Analog Four / Analog Rytm", "4-Voice Discrete Analog Synthesizer", 2012,
                a4_cc, a4_sysex, ["Bank A", "Bank B"], a4_presets)

if __name__ == "__main__":
    build_wave9()
