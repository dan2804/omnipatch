#!/usr/bin/env python3
"""
Wave 11 Vintage Titans & German Rarities Generator for OmniPatch:
- Waldorf (Waldorf Wave)
- PPG (PPG Wave 2.2 / 2.3)
- JoMoX (SunSyn)
- MFB (Dominion 1)
- Moog Vintage (Minimoog Model D, Memorymoog, Moog Source, Moog Prodigy)
- Roland Vintage (Jupiter-4, Juno-60, Promars MRS-2)
- Yamaha Vintage FM & Grooves (DX1, DX5, AN200, DX200)
Creates profile.yaml and factory_presets.json for 15 legendary instruments.
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

def build_wave11():
    print("Building Wave 11: Waldorf Wave, PPG, JoMoX SunSyn, MFB, Moog Vintage, Roland Vintage, Yamaha DX1/DX5...")

    # =========================================================================
    # 1. WALDORF WAVE
    # =========================================================================
    wave_cc = {"filter_cutoff": 74, "filter_resonance": 71, "wave1_pos": 70, "wave2_pos": 79, "glide": 5, "env_depth": 77}
    wave_sysex = {"header": "F0 3E 01 00", "device_id_byte": 2, "commands": {"request_sound": "F0 3E 01 00 10 [bank] [prog] F7"}}
    wave_seeds = [
        "Waveform 16-Voice Master", "Curtis 24dB Analog Sweep", "Motorized Panel Grand Poly", "Wavetable Morph Symphony",
        "Resonant Glass Bell", "Sub Harmonic Analog Bass", "Slow Attack Celestial Choir", "PPG Heritage 2.3 Lead",
        "Detuned Dual Wavetable Clav", "Alien Formant Vocal Shifter", "Warm Polyphonic Brass", "Deep Ambient Space Cloud"
    ]
    wave_presets = []
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 129):
            seed = wave_seeds[(p - 1) % len(wave_seeds)]
            p_name = f"Wave-{b}-{p:03d}: {seed}"
            cat = "Pad" if "Pad" in seed or "Choir" in seed or "Cloud" in seed else "Brass" if "Brass" in seed else "Bass" if "Bass" in seed else "Wavetable"
            wave_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["waldorf-wave", "curtis-analog-filter", "motorized-panel", "wavetable-flagship", cat.lower()]
            })
    write_synth("waldorf", "waldorf-wave", "Waldorf Wave", "Flagship Wavetable Synthesizer", 1993,
                wave_cc, wave_sysex, ["Preset Bank 1", "Preset Bank 2"], wave_presets)

    # =========================================================================
    # 2. PPG WAVE 2.2 / 2.3
    # =========================================================================
    ppg_cc = {"cutoff": 74, "resonance": 71, "wavetable": 70, "env_attack": 73, "env_decay": 75}
    ppg_sysex = {"header": "F0 3E 02", "device_id_byte": 2, "commands": {"dump_prog": "F0 3E 02 01 [prog] F7"}}
    ppg_seeds = [
        "PPG Bell Classic", "Upper Wavetable Sweep", "SSM2044 Analog VCF Resonance", "Digital Dream Clav",
        "Tangerine Dream Seq Lead", "Warm Poly Brass PPG", "Subterranean Wavetable Low", "Vocal Formant Choir PPG"
    ]
    ppg_presets = []
    for p in range(1, 101):
        seed = ppg_seeds[(p - 1) % len(ppg_seeds)]
        cat = "Bell" if "Bell" in seed else "Pad" if "Pad" in seed or "Choir" in seed else "Lead" if "Lead" in seed else "Bass"
        ppg_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"PPG-{p:02d}: {seed}",
            "category": cat,
            "tags": ["wolfgang-palm", "ssm2044", "wavetable-pioneer", "ppg-wave", cat.lower()]
        })
    write_synth("ppg", "ppg-wave", "PPG Wave 2.2 / 2.3", "Classic Wavetable Synthesizer", 1982,
                ppg_cc, ppg_sysex, ["Factory Bank"], ppg_presets)

    # =========================================================================
    # 3. JOMOX SUNSYN
    # =========================================================================
    sunsyn_cc = {"filter_cutoff": 74, "filter_resonance": 71, "pole_switching": 79, "rco_sample": 20, "vco_mix": 21}
    sunsyn_sysex = {"header": "F0 33 02", "device_id_byte": 2, "commands": {"request_sound": "F0 33 02 01 [bank] [prog] F7"}}
    sunsyn_seeds = [
        "SunSyn 8-Voice Discrete Poly", "4-Pole Pole-Switching Resonance", "RCO Sampled Wave Saw", "Punchy Analog Bass 24dB",
        "Liquid Modular Filter Sweep", "Cross-Modulated Sync Screamer", "Warm Discrete Poly Brass", "Complex Multi-Tap Modulation"
    ]
    sunsyn_presets = []
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 126):  # 250 presets
            seed = sunsyn_seeds[(p - 1) % len(sunsyn_seeds)]
            p_name = f"SunSyn-{b}-{p:03d}: {seed}"
            cat = "Brass" if "Brass" in seed else "Pad" if "Pad" in seed else "Bass" if "Bass" in seed else "Lead"
            sunsyn_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["rco-waveforms", "pole-switching-filter", "discrete-analog-poly", "sunsyn", cat.lower()]
            })
    write_synth("jomox", "sunsyn", "JoMoX SunSyn", "8-Voice Discrete Analog Synthesizer", 1999,
                sunsyn_cc, sunsyn_sysex, ["Preset Bank 1", "Preset Bank 2"], sunsyn_presets)

    # =========================================================================
    # 4. MFB DOMINION 1
    # =========================================================================
    mfb_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_type": 79, "vco1_shape": 20, "vco2_shape": 21, "vco3_shape": 22}
    mfb_sysex = {"header": "F0 00 20 45", "device_id_byte": 3, "commands": {"request_preset": "F0 00 20 45 01 [prog] F7"}}
    mfb_seeds = [
        "3-VCO Discrete Analog Growl", "12-Filter Multi-Mode Acid", "Ring Mod Screamer Lead", "Sub Octave Earthshaker",
        "Steiner Parker Notch Pluck", "Warm Flute Solo Legato", "Cross-Mod Detuned Saw Solo", "Modular Patchbay Bass"
    ]
    mfb_presets = []
    for p in range(1, 129):
        seed = mfb_seeds[(p - 1) % len(mfb_seeds)]
        cat = "Bass" if "Bass" in seed or "Growl" in seed or "Earthshaker" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Acid"
        mfb_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"Dominion 1 Sound {p:03d}: {seed}",
            "category": cat,
            "tags": ["3-vco", "12-filter-modes", "patchbay", "dominion-1", cat.lower()]
        })
    write_synth("mfb", "dominion-1", "MFB Dominion 1", "3-VCO Analog Synthesizer with 12 Filter Modes", 2014,
                mfb_cc, mfb_sysex, ["Factory Presets"], mfb_presets)

    # =========================================================================
    # 5. MOOG MINIMOOG MODEL D
    # =========================================================================
    mini_d_cc = {"filter_cutoff": 74, "filter_resonance": 71, "osc1_level": 20, "osc2_level": 21, "osc3_level": 22, "glide": 5}
    mini_d_sysex = {"header": "F0 04 00", "device_id_byte": 2, "commands": {"dump_patch": "F0 04 00 01 [prog] F7"}}
    mini_d_names = [
        "Classic 1970 Mini Bass", "Fat 3-VCO Funk Bass", "Lucky Man Solo Lead", "Shine On Crazy Diamond Lead",
        "Parliament P-Funk Bass", "Flashlight Sub Thud", "Warm Triangle Flute Solo", "Detuned Screaming Saw Lead",
        "Modular White Noise Wind", "Punchy Transistor Kick Zap", "Feedback Overdrive Solo", "Deep Moog Lowpass 24dB",
        "Sci-Fi Laser Gun", "Kraftwerk Autobahn Lead", "Krautrock Resonant Drone", "Syncopated Arp Bass",
        "Vintage Organ Bass Pedals", "Liquid Legato Lead", "Veloc Modulated Pluck", "Analog Clarinet Solo",
        "Sub Octave 20Hz Shaker", "Square Wave Punch Bass", "Warm Poly Emulation Unison", "Heavy Distorted Rock Lead",
        "Whammy Pitch Wheel Screamer", "Smooth Moog Brass Lead", "Clicky Electro Bass", "Cathedral Low Organ",
        "Ambient Resonance Sweep", "Modular Sample & Hold FX", "Percussive Cowbell Analog", "Acidic Ladder 24dB",
        "Bowed Saw Bass Solo", "Vintage Funk Slap", "Space Laser Sound", "Warm Acoustic Bass Sim",
        "Harmonic 5th Lead", "Detroit Techno Mono Saw", "Sub Low Sine Floor", "Fast 16th Bassline",
        "Resonant Filter Peak Whine", "Dirty Overdriven Sawtooth", "Chirp Attack Bass", "The Final Minimoog Solo"
    ]
    mini_d_presets = []
    for p, name in enumerate(mini_d_names):
        cat = "Bass" if "Bass" in name or "Thud" in name or "Shaker" in name else "Lead" if "Lead" in name or "Solo" in name else "FX"
        mini_d_presets.append({
            "bank": "Classic Sound Book",
            "program": p + 1,
            "name": f"Model D: {name}",
            "category": cat,
            "tags": ["minimoog", "ladder-filter", "3-vco", "monophonic-legend", cat.lower()]
        })
    write_synth("moog", "minimoog-d", "Moog Minimoog Model D", "Definitive Analog Monophonic Synthesizer", 1970,
                mini_d_cc, mini_d_sysex, ["Classic Sound Book"], mini_d_presets)

    # =========================================================================
    # 6. MOOG MEMORYMOOG
    # =========================================================================
    memo_cc = {"filter_cutoff": 74, "filter_resonance": 71, "contour_amount": 77, "glide": 5}
    memo_sysex = {"header": "F0 04 06", "device_id_byte": 2, "commands": {"dump_prog": "F0 04 06 01 [prog] F7"}}
    memo_presets = []
    memo_seeds = [
        "18-VCO Giant Poly Brass", "Memorymoog Massive Strings", "6-Voice Unison Heavy Monster", "Sub Harmonic Poly Bass",
        "Syncopated Poly Arp", "Soft Moog Poly Pad", "Punchy 3-VCO Clavinet", "Dual Filter Contour Solo",
        "Sci-Fi Polymod Wind", "Vintage Brass Fanfare 1982"
    ]
    for p in range(1, 101):
        seed = memo_seeds[(p - 1) % len(memo_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Strings" in seed or "Pad" in seed else "Bass" if "Bass" in seed else "Lead"
        memo_presets.append({
            "bank": "Factory Programs",
            "program": p,
            "name": f"Memorymoog Prog {p:02d}: {seed}",
            "category": cat,
            "tags": ["18-vco", "6-voice-poly", "ladder-filter", "memorymoog", cat.lower()]
        })
    write_synth("moog", "memorymoog", "Moog Memorymoog / Memorymoog Plus", "6-Voice 18-VCO Analog Polyphonic Synthesizer", 1982,
                memo_cc, memo_sysex, ["Factory Programs"], memo_presets)

    # =========================================================================
    # 7. MOOG SOURCE
    # =========================================================================
    source_cc = {"cutoff": 74, "resonance": 71, "contour": 77, "glide": 5}
    source_sysex = {"header": "F0 04 05 01", "device_id_byte": 2, "commands": {"dump_prog": "F0 04 05 01 01 [prog] F7"}}
    source_presets = []
    source_seeds = [
        "Membrane Panel Funky Bass", "New Wave Sync Lead", "Punchy 24dB Pluck", "Subterranean Moog Low",
        "Digital Control Analog Saw", "Overdriven Reso Whine", "Vintage Solo Flute", "Space Noise Wind"
    ]
    for p in range(1, 65):
        seed = source_seeds[(p - 1) % len(source_seeds)]
        cat = "Bass" if "Bass" in seed or "Low" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Analog"
        source_presets.append({
            "bank": "Internal Bank",
            "program": p,
            "name": f"Source-{p:02d}: {seed}",
            "category": cat,
            "tags": ["membrane-panel", "dual-vco", "ladder-filter", "moog-source", cat.lower()]
        })
    write_synth("moog", "moog-source", "Moog Source", "Microprocessor-Controlled Analog Synthesizer", 1981,
                source_cc, source_sysex, ["Internal Bank"], source_presets)

    # =========================================================================
    # 8. MOOG PRODIGY
    # =========================================================================
    prodigy_cc = {"cutoff": 74, "resonance": 71, "osc_sync": 80, "glide": 5}
    prodigy_sysex = {"header": "F0 04 00 02", "device_id_byte": 2, "commands": {"dump_patch": "F0 04 00 02 01 [prog] F7"}}
    prodigy_presets = []
    prodigy_seeds = [
        "Fat 2-VCO Prodigy Bass", "Sync Screamer Solo (Firestarter)", "Warm Ladder Lowpass Lead", "Punchy Pluck Bass",
        "Sub Octave Thud", "Detuned Dual Saw Riff", "Resonant Squeal Mono", "Vintage Funk Foundation"
    ]
    for p in range(1, 33):
        seed = prodigy_seeds[(p - 1) % len(prodigy_seeds)]
        cat = "Bass" if "Bass" in seed or "Thud" in seed else "Lead" if "Lead" in seed or "Solo" in seed or "Sync" in seed else "Analog"
        prodigy_presets.append({
            "bank": "Preset Patches",
            "program": p,
            "name": f"Prodigy Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["dual-vco", "ladder-filter", "sync-lead", "moog-prodigy", cat.lower()]
        })
    write_synth("moog", "moog-prodigy", "Moog Prodigy", "Dual-VCO Analog Monophonic Synthesizer", 1979,
                prodigy_cc, prodigy_sysex, ["Preset Patches"], prodigy_presets)

    # =========================================================================
    # 9. ROLAND JUPITER-4 COMPUPHONIC
    # =========================================================================
    jp4_cc = {"vcf_cutoff": 74, "vcf_resonance": 71, "ensemble": 92, "sub_osc": 20}
    jp4_sysex = {"header": "F0 41 00 06", "device_id_byte": 2, "commands": {"dump_patch": "F0 41 00 06 01 [prog] F7"}}
    jp4_presets = []
    jp4_seeds = [
        "Compuphonic Pure Brass", "Warm Ensemble Strings", "Discrete Analog Bass JP4", "Arpeggiator Pulse Groove",
        "Resonant Filter Sweep Lead", "Sub Octave Poly Pad", "Vocaloid Formant Synth", "Space Wind Sound"
    ]
    for p in range(1, 33):
        seed = jp4_seeds[(p - 1) % len(jp4_seeds)]
        cat = "Brass" if "Brass" in seed else "Strings" if "Strings" in seed else "Bass" if "Bass" in seed else "Arp" if "Arpeggiator" in seed else "Pad"
        jp4_presets.append({
            "bank": "Factory & User Bank",
            "program": p,
            "name": f"Jupiter-4 Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["compuphonic", "discrete-vco", "ensemble-chorus", "jupiter-4", cat.lower()]
        })
    write_synth("roland", "jupiter-4", "Roland Jupiter-4 Compuphonic", "4-Voice Discrete Polyphonic Synthesizer", 1978,
                jp4_cc, jp4_sysex, ["Factory & User Bank"], jp4_presets)

    # =========================================================================
    # 10. ROLAND JUNO-60
    # =========================================================================
    juno60_cc = {"filter_cutoff": 74, "filter_resonance": 71, "chorus_mode": 92, "sub_level": 20, "vcf_env": 77}
    juno60_sysex = {"header": "F0 41 00 07", "device_id_byte": 2, "commands": {"dump_prog": "F0 41 00 07 01 [prog] F7"}}
    juno60_presets = []
    juno60_seeds = [
        "11 Brass I (Classic Juno)", "12 Brass II (Soft French Horn)", "13 Strings I (Lush BBD Chorus)", "14 Strings II (Slow Swell)",
        "21 Organ I (Rock Drawbar)", "22 Organ II (Jazz Chorus)", "23 Piano I (80s Poly E-Piano)", "24 Clavinet (Funky Thumb)",
        "31 Bass I (Punchy Sub Bass)", "32 Bass II (Resonant Acid Thud)", "33 Lead I (PWM Sync Lead)", "34 Lead II (Solo Flute)",
        "41 Pad I (Celestial Chorus)", "42 Pad II (Dark Shimmer)", "43 Arp I (Fast Clocked Pluck)", "44 Sci-Fi Noise Zap"
    ]
    for p in range(1, 57):
        seed = juno60_seeds[(p - 1) % len(juno60_seeds)]
        cat = "Brass" if "Brass" in seed else "Strings" if "Strings" in seed else "Bass" if "Bass" in seed else "Pad" if "Pad" in seed else "Keys"
        juno60_presets.append({
            "bank": "Factory Memory",
            "program": p,
            "name": f"Juno-60 Memory {p:02d}: {seed}",
            "category": cat,
            "tags": ["ir3109-vcf", "dcb-interface", "bbd-chorus", "juno-60", cat.lower()]
        })
    write_synth("roland", "juno-60", "Roland Juno-60", "6-Voice Polyphonic Analog Synthesizer", 1982,
                juno60_cc, juno60_sysex, ["Factory Memory"], juno60_presets)

    # =========================================================================
    # 11. ROLAND PROMARS MRS-2
    # =========================================================================
    promars_cc = {"vcf_cutoff": 74, "vcf_resonance": 71, "vco2_detune": 20, "sub_osc": 21}
    promars_sysex = {"header": "F0 41 00 08", "device_id_byte": 2, "commands": {"dump_prog": "F0 41 00 08 01 [prog] F7"}}
    promars_presets = []
    promars_seeds = [
        "Dual VCO Compuphonic Lead", "Punchy Detuned Saw Bass", "Warm Analog Flute Solo", "Resonant Scream 24dB",
        "Subterranean Low Thud", "Ensemble Chorus Pad", "Slow Filter Mod Sweep", "Vintage Space Riff"
    ]
    for p in range(1, 31):
        seed = promars_seeds[(p - 1) % len(promars_seeds)]
        cat = "Bass" if "Bass" in seed or "Thud" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Analog"
        promars_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"Promars Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["dual-vco", "compuphonic", "analog-monosynth", "promars", cat.lower()]
        })
    write_synth("roland", "promars", "Roland Promars MRS-2", "Compuphonic Analog Synthesizer", 1979,
                promars_cc, promars_sysex, ["Factory Presets"], promars_presets)

    # =========================================================================
    # 12. YAMAHA DX1
    # =========================================================================
    dx1_cc = {"algorithm": 70, "feedback": 71, "operator_output": 74, "dual_balance": 16}
    dx1_sysex = {"header": "F0 43 00 01", "device_id_byte": 2, "commands": {"request_voice": "F0 43 00 01 01 [prog] F7"}}
    dx1_presets = []
    dx1_seeds = [
        "Dual 6-Operator E.Piano Deluxe", "Grand Wooden Polyphonic FM", "Dual Layered FM Brass", "Deep FM Sub Bass Orchestra",
        "Lush Weighted Keys Strings", "Crystal Bell Matrix DX1", "Polyphonic Aftertouch Soloist", "Ethereal FM Choir Space"
    ]
    for b_name in ["Performance Bank A", "Performance Bank B"]:
        for p in range(1, 65):
            seed = dx1_seeds[(p - 1) % len(dx1_seeds)]
            p_name = f"DX1 Perf {b_name[-1]}-{p:02d}: {seed}"
            cat = "Keys" if "Piano" in seed else "Brass" if "Brass" in seed else "Pad" if "Strings" in seed or "Choir" in seed else "FM"
            dx1_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["dual-6-operator-fm", "poly-aftertouch", "wood-casing", "dx1-flagship", cat.lower()]
            })
    write_synth("yamaha", "dx1", "Yamaha DX1", "Dual 6-Operator FM Digital Synthesizer Flagship", 1983,
                dx1_cc, dx1_sysex, ["Performance Bank A", "Performance Bank B"], dx1_presets)

    # =========================================================================
    # 13. YAMAHA DX5
    # =========================================================================
    dx5_cc = dx1_cc
    dx5_sysex = {"header": "F0 43 00 05", "device_id_byte": 2, "commands": {"request_voice": "F0 43 00 05 01 [prog] F7"}}
    dx5_presets = []
    for b_name in ["Performance Bank A", "Performance Bank B"]:
        for p in range(1, 65):
            seed = dx1_seeds[(p - 1) % len(dx1_seeds)]
            p_name = f"DX5 Perf {b_name[-1]}-{p:02d}: {seed}"
            cat = "Keys" if "Piano" in seed else "Brass" if "Brass" in seed else "Pad"
            dx5_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["dual-6-op-fm", "stage-flagship", "dx5", cat.lower()]
            })
    write_synth("yamaha", "dx5", "Yamaha DX5", "Dual 6-Operator FM Digital Synthesizer", 1985,
                dx5_cc, dx5_sysex, ["Performance Bank A", "Performance Bank B"], dx5_presets)

    # =========================================================================
    # 14. YAMAHA AN200
    # =========================================================================
    an200_cc = {"filter_cutoff": 74, "filter_resonance": 71, "distortion": 80, "fm_depth": 70, "sync": 81}
    an200_sysex = {"header": "F0 43 10 5C 02", "device_id_byte": 2, "commands": {"dump_pattern": "F0 43 10 5C 02 01 [pat] F7"}}
    an200_presets = []
    an200_seeds = [
        "Acidic AN Groove", "Analog Modeling Saw Bass", "Sync Squeal Lead AN", "Distorted Electro Pluck",
        "Free EG Motion Synth", "Resonant Sweep 24dB", "Sub Heavy 303 Killer", "Highpass Cyber Pattern"
    ]
    for p in range(1, 129):
        seed = an200_seeds[(p - 1) % len(an200_seeds)]
        cat = "Bass" if "Bass" in seed else "Lead" if "Lead" in seed or "Squeal" in seed else "Acid"
        an200_presets.append({
            "bank": f"Pattern Bank {(p - 1) // 32 + 1}",
            "program": p,
            "name": f"AN200 Groove {p:03d}: {seed}",
            "category": cat,
            "tags": ["analog-physical-modeling", "an-engine", "free-eg", "an200", cat.lower()]
        })
    write_synth("yamaha", "an200", "Yamaha AN200", "Desktop Analog Modeling Loop Synthesizer", 2001,
                an200_cc, an200_sysex, [f"Pattern Bank {i}" for i in range(1, 5)], an200_presets)

    # =========================================================================
    # 15. YAMAHA DX200
    # =========================================================================
    dx200_cc = {"filter_cutoff": 74, "filter_resonance": 71, "fm_harmonics": 20, "fm_timbre": 21, "decay": 75}
    dx200_sysex = {"header": "F0 43 10 5C 01", "device_id_byte": 2, "commands": {"dump_pattern": "F0 43 10 5C 01 01 [pat] F7"}}
    dx200_presets = []
    dx200_seeds = [
        "6-Operator FM Dance Bass", "Filtered FM Screamer", "DX LatelyBass Loop", "Resonant FM Lead 16th",
        "Metallic Industrial Rhythm", "Subterranean Sine Thud", "Crystal EP Pattern", "Alien Formant FM Groove"
    ]
    for p in range(1, 129):
        seed = dx200_seeds[(p - 1) % len(dx200_seeds)]
        cat = "Bass" if "Bass" in seed or "Thud" in seed else "Lead" if "Lead" in seed else "FM"
        dx200_presets.append({
            "bank": f"Pattern Bank {(p - 1) // 32 + 1}",
            "program": p,
            "name": f"DX200 Pattern {p:03d}: {seed}",
            "category": cat,
            "tags": ["6-operator-fm", "resonant-filter-fm", "dx200", cat.lower()]
        })
    write_synth("yamaha", "dx200", "Yamaha DX200", "Desktop 6-Operator FM Loop Synthesizer", 2001,
                dx200_cc, dx200_sysex, [f"Pattern Bank {i}" for i in range(1, 5)], dx200_presets)

if __name__ == "__main__":
    build_wave11()
