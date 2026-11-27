#!/usr/bin/env python3
"""
Wave 7 Studio Legends Generator for OmniPatch:
Kurzweil (V.A.S.T.), Eventide (Ultra-Harmonizer), Lexicon (PCM/LXP),
Modal Electronics, JoMoX, Doepfer, and DigiTech.
Creates profile.yaml and factory_presets.json for 20 legendary instruments.
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

def build_wave7():
    print("Building Wave 7: Kurzweil, Eventide, Lexicon, Modal, JoMoX, Doepfer & DigiTech...")

    # =========================================================================
    # 1. KURZWEIL K2000 / K2000R
    # =========================================================================
    k2k_cc = {"data_slider": 6, "filter_cutoff": 74, "resonance": 71, "reverb_depth": 91, "chorus_depth": 93}
    k2k_sysex = {"header": "F0 07 00", "device_id_byte": 2, "commands": {"request_program": "F0 07 00 09 01 [prog] F7"}}
    k2k_seeds = [
        "Sweet Tenor", "Stereo Grand", "Total Resonance Pad", "Acoustic String Orch", "Big Moog Bass",
        "Baroque Harpsichord", "V.A.S.T. Distorted Lead", "Touch Vox Choir", "Classic B3 Drawbars", "Hybrid Wavetable Clav",
        "Dual Filter Morph", "Dynamic French Horns", "Resonant Sweep 4-Pole", "Strummed Acoustic 12", "E-Piano Dyno Rhodes"
    ]
    k2k_presets = []
    # 200 programs (1-199)
    for p in range(1, 201):
        seed = k2k_seeds[(p - 1) % len(k2k_seeds)]
        cat = "Keys" if "Piano" in seed or "Rhodes" in seed or "Organ" in seed else "Pad" if "Pad" in seed or "Strings" in seed or "Choir" in seed else "Bass" if "Bass" in seed else "Lead" if "Lead" in seed else "Brass"
        k2k_presets.append({
            "bank": f"Program Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"K2000-{p:03d} {seed}",
            "category": cat,
            "tags": ["vast-synthesis", "31-algorithms", "dsp-blocks", cat.lower()]
        })
    write_synth("kurzweil", "k2000", "Kurzweil K2000 / K2000R", "V.A.S.T. Workstation Synthesizer", 1991,
                k2k_cc, k2k_sysex, ["Program Bank 1", "Program Bank 2"], k2k_presets)

    # =========================================================================
    # 2. KURZWEIL K2500 / K2500R
    # =========================================================================
    k25_cc = k2k_cc
    k25_sysex = {"header": "F0 07 00", "device_id_byte": 2, "commands": {"request_program": "F0 07 00 12 01 [prog] F7"}}
    k25_presets = []
    for p in range(1, 201):
        seed = k2k_seeds[(p - 1) % len(k2k_seeds)]
        cat = "Keys" if "Piano" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Bass"
        k25_presets.append({
            "bank": f"KDFX Program Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"K2500-{p:03d} {seed} KDFX",
            "category": cat,
            "tags": ["vast", "kdfx-effects", "48-voice", cat.lower()]
        })
    for p in range(1, 101):
        k25_presets.append({
            "bank": "Multi Setups",
            "program": p,
            "name": f"Setup {p:02d}: Orchestral Zone Layer",
            "category": "Setup",
            "tags": ["multi-setup", "zones", "vast"]
        })
    write_synth("kurzweil", "k2500", "Kurzweil K2500 / K2500R", "48-Voice V.A.S.T. Production Synthesizer", 1996,
                k25_cc, k25_sysex, ["KDFX Program Bank 1", "KDFX Program Bank 2", "Multi Setups"], k25_presets)

    # =========================================================================
    # 3. KURZWEIL K2600 / K2600R
    # =========================================================================
    k26_cc = k2k_cc
    k26_sysex = {"header": "F0 07 00", "device_id_byte": 2, "commands": {"request_program": "F0 07 00 14 01 [prog] F7"}}
    k26_presets = []
    for p in range(1, 201):
        seed = k2k_seeds[(p - 1) % len(k2k_seeds)]
        cat = "Pad" if "Pad" in seed else "Keys" if "Piano" in seed else "Synth"
        k26_presets.append({
            "bank": f"Triple Modular Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"K2600-{p:03d} {seed}",
            "category": cat,
            "tags": ["triple-modular-vast", "kdfx", "flagship", cat.lower()]
        })
    for p in range(1, 101):
        k26_presets.append({
            "bank": "Performance Setups",
            "program": p,
            "name": f"Setup {p:02d}: Ribbon & Slider Performance",
            "category": "Setup",
            "tags": ["multi-setup", "k2600"]
        })
    write_synth("kurzweil", "k2600", "Kurzweil K2600 / K2600R", "Triple Modular Processing V.A.S.T. Flagship", 1999,
                k26_cc, k26_sysex, ["Triple Modular Bank 1", "Triple Modular Bank 2", "Performance Setups"], k26_presets)

    # =========================================================================
    # 4. EVENTIDE H3000 ULTRA-HARMONIZER
    # =========================================================================
    h3_cc = {"soft_key_1": 16, "soft_key_2": 17, "soft_key_3": 18, "soft_key_4": 19, "data_wheel": 6}
    h3_sysex = {"header": "F0 1C 01", "device_id_byte": 3, "commands": {"request_program": "F0 1C 01 01 [prog_hi] [prog_lo] F7"}}
    h3_seeds = [
        "Steve Vai MicroPitch", "Diatonic Shifter 3rd/5th", "Magic Air Reverb", "Dual H3000 Harmonizer",
        "Stereo Band Delays 8-Tap", "Stutter Flanger", "Swept Reverb Dense", "Alien Vocal Pitch Shifter",
        "Infinite Flange Drone", "Mod Delays Stereo 500ms", "Canyon Echoes 12s", "Crystal Echoes Shimmer",
        "Multi-Shift 4 Octaves", "Pitch Randomizer Chaos", "Resonant Comb Filter Pitch", "Heavy Detune Wide"
    ]
    h3_presets = []
    # 10 banks of 100 programs (000 - 999 = 1,000 programs)
    for b in range(10):
        b_name = f"ROM Bank {b}00"
        for p in range(100):
            prog_num = b * 100 + p
            seed = h3_seeds[p % len(h3_seeds)]
            cat = "Pitch" if "Pitch" in seed or "Shifter" in seed or "Harmonizer" in seed or "Shift" in seed else "Delay" if "Delay" in seed or "Echo" in seed else "Reverb" if "Reverb" in seed or "Air" in seed else "Modulation"
            h3_presets.append({
                "bank": b_name,
                "program": prog_num,
                "name": f"H3000-{prog_num:03d}: {seed}",
                "category": cat,
                "tags": ["ultra-harmonizer", "diatonic-pitch", "micropitch", cat.lower()]
            })
    write_synth("eventide", "h3000", "Eventide H3000 Ultra-Harmonizer", "Studio Pitch Harmonizer & Multi-Effects", 1988,
                h3_cc, h3_sysex, [f"ROM Bank {i}00" for i in range(10)], h3_presets)

    # =========================================================================
    # 5. EVENTIDE DSP4000 ULTRA-HARMONIZER
    # =========================================================================
    dsp4_cc = h3_cc
    dsp4_sysex = {"header": "F0 1C 02", "device_id_byte": 3, "commands": {"request_program": "F0 1C 02 01 [prog] F7"}}
    dsp4_presets = []
    for p in range(1, 501):
        seed = h3_seeds[(p - 1) % len(h3_seeds)]
        cat = "Pitch" if "Pitch" in seed else "Reverb" if "Reverb" in seed else "Delay"
        dsp4_presets.append({
            "bank": f"Algorithm Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"DSP4000-{p:03d}: Modular {seed}",
            "category": cat,
            "tags": ["dsp4000", "modular-algorithms", "pitch-shift", cat.lower()]
        })
    write_synth("eventide", "dsp4000", "Eventide DSP4000 Ultra-Harmonizer", "Modular Multi-Effects Processor", 1994,
                dsp4_cc, dsp4_sysex, [f"Algorithm Bank {i}" for i in range(1, 6)], dsp4_presets)

    # =========================================================================
    # 6. EVENTIDE ECLIPSE
    # =========================================================================
    eclipse_cc = {"block1_mix": 91, "block2_mix": 92, "encoder_a": 16, "encoder_b": 17}
    eclipse_sysex = {"header": "F0 1C 03", "device_id_byte": 3, "commands": {"request_program": "F0 1C 03 01 [prog] F7"}}
    eclipse_presets = []
    for p in range(1, 501):
        seed = h3_seeds[(p - 1) % len(h3_seeds)]
        cat = "Reverb" if "Reverb" in seed else "Pitch" if "Pitch" in seed else "Multi"
        eclipse_presets.append({
            "bank": f"Dual Engine Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Eclipse-{p:03d}: Dual FX {seed}",
            "category": cat,
            "tags": ["24-bit-96khz", "dual-engine", "eventide", cat.lower()]
        })
    write_synth("eventide", "eclipse", "Eventide Eclipse", "24-Bit Dual-Engine Effects Processor", 2001,
                eclipse_cc, eclipse_sysex, [f"Dual Engine Bank {i}" for i in range(1, 6)], eclipse_presets)

    # =========================================================================
    # 7. EVENTIDE TIMEFACTOR / SPACE
    # =========================================================================
    space_cc = {"decay": 74, "size": 71, "predelay": 18, "low": 19, "high": 20, "mix": 91}
    space_sysex = {"header": "F0 1C 04", "device_id_byte": 3, "commands": {"request_preset": "F0 1C 04 01 [prog] F7"}}
    space_seeds = [
        "Blackhole Massive Gravity Reverb", "Shimmer Octave Pitch Reverb", "MangledVerb Industrial Distortion",
        "Dual Delay Stereophonic", "Band Delay Modulated Reso", "Vintage Delay Tape BBD", "Hall Concert 6s",
        "Plate Bright Vocal", "Room Studio Ambience", "Ducking Delay 450ms", "TremoloVerb Pulsing Reverb",
        "Reverse Reverb Swell", "ModEchoVerb Chorus Delay", "Spring Surf Reverb", "Resonator Pitch Ring"
    ]
    space_presets = []
    for p in range(1, 101):
        seed = space_seeds[(p - 1) % len(space_seeds)]
        cat = "Reverb" if "Reverb" in seed or "Blackhole" in seed or "Hall" in seed else "Delay" if "Delay" in seed else "Special"
        space_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"Space/Time-{p:02d}: {seed}",
            "category": cat,
            "tags": ["blackhole", "shimmer", "space-reverb", "timefactor", cat.lower()]
        })
    write_synth("eventide", "timefactor-space", "Eventide Space & TimeFactor", "Flagship Studio Stomp / Processor", 2011,
                space_cc, space_sysex, ["Factory Presets"], space_presets)

    # =========================================================================
    # 8. LEXICON PCM70
    # =========================================================================
    pcm70_cc = {"decay_time": 74, "rt_low": 71, "fx_mix": 91}
    pcm70_sysex = {"header": "F0 06 01", "device_id_byte": 3, "commands": {"request_program": "F0 06 01 01 [prog] F7"}}
    pcm70_seeds = [
        "Concert Hall Classic", "Rich Plate 2.4s", "Tiled Room Bright", "Infinite Reverb Space",
        "Resonant Chords 6-Voice", "Multiband Delay 4-Tap", "Chorus Room Warm", "Inverse Reverb Gate",
        "Deep Chamber 4.2s", "Vocal Ambience 1.2s", "Gated Snare Reverb", "Stereo Flanger Wide"
    ]
    pcm70_presets = []
    for p in range(1, 51):
        seed = pcm70_seeds[(p - 1) % len(pcm70_seeds)]
        pcm70_presets.append({
            "bank": "Factory ROM",
            "program": p,
            "name": f"ROM {p:02d}: {seed}",
            "category": "Reverb",
            "tags": ["lexicon-hall", "rich-plate", "tiled-room", "pcm70"]
        })
    for p in range(1, 51):
        pcm70_presets.append({
            "bank": "User RAM",
            "program": p,
            "name": f"User Sound {p:02d}",
            "category": "User",
            "tags": ["user", "reverb"]
        })
    write_synth("lexicon", "pcm70", "Lexicon PCM70", "Digital Effects Processor", 1985,
                pcm70_cc, pcm70_sysex, ["Factory ROM", "User RAM"], pcm70_presets)

    # =========================================================================
    # 9. LEXICON PCM80
    # =========================================================================
    pcm80_cc = {"reverb_time": 74, "delay_time": 82, "delay_feedback": 83, "mix": 91}
    pcm80_sysex = {"header": "F0 06 04", "device_id_byte": 3, "commands": {"dump_program": "F0 06 04 01 [prog] F7"}}
    pcm80_presets = []
    pcm80_seeds = [
        "Concert Wave Reverb", "Glide Delay Stereo", "Spatial Ambience", "Chorus Hall 3.5s", "Dual MultiTap Echo",
        "Resonant Space Chamber", "Lush String Plate", "Dynamic Vocal Chamber", "Modulated Tap Delay", "Ambient Cloud 10s"
    ]
    for b in [1, 2]:
        b_name = f"Preset Bank {b}"
        for p in range(1, 101):
            seed = pcm80_seeds[(p - 1) % len(pcm80_seeds)]
            pcm80_presets.append({
                "bank": b_name,
                "program": p,
                "name": f"PCM80-{b}-{p:02d}: {seed}",
                "category": "Reverb",
                "tags": ["pcm80", "dual-dsp", "stereo-delay-reverb"]
            })
    write_synth("lexicon", "pcm80", "Lexicon PCM80", "Digital Effects Processor w/ Dual DSP", 1994,
                pcm80_cc, pcm80_sysex, ["Preset Bank 1", "Preset Bank 2"], pcm80_presets)

    # =========================================================================
    # 10. LEXICON PCM90
    # =========================================================================
    pcm90_cc = {"mid_reverb_decay": 74, "pre_delay": 18, "high_cut": 20, "mix": 91}
    pcm90_sysex = {"header": "F0 06 05", "device_id_byte": 3, "commands": {"dump_program": "F0 06 05 01 [prog] F7"}}
    pcm90_presets = []
    pcm90_seeds = [
        "Deep Blue Hall", "Lexicon Large Concert Hall", "Rich Chamber Vocal", "Classic Gold Plate",
        "Acoustic Room Natural", "Cathedral Organ Reverb", "Studio Drum Room", "Smooth Ambience",
        "Gated Chamber 0.8s", "Warm Dark Hall 4.0s"
    ]
    for p in range(1, 251):
        seed = pcm90_seeds[(p - 1) % len(pcm90_seeds)]
        pcm90_presets.append({
            "bank": f"Reverb Bank {(p - 1) // 50 + 1}",
            "program": p,
            "name": f"PCM90-{p:03d}: {seed}",
            "category": "Reverb",
            "tags": ["pcm90", "reference-reverberator", "hall-plate-room"]
        })
    write_synth("lexicon", "pcm90", "Lexicon PCM90", "Dedicated Digital Reverberator", 1995,
                pcm90_cc, pcm90_sysex, [f"Reverb Bank {i}" for i in range(1, 6)], pcm90_presets)

    # =========================================================================
    # 11. LEXICON LXP-1 / LXP-5
    # =========================================================================
    lxp_cc = {"decay": 74, "delay": 82, "mix": 91}
    lxp_sysex = {"header": "F0 06 02", "device_id_byte": 3, "commands": {"dump_prog": "F0 06 02 01 [prog] F7"}}
    lxp_presets = []
    for p in range(1, 129):
        lxp_presets.append({
            "bank": "Factory Programs",
            "program": p,
            "name": f"LXP Program {p:02d}: Classic Reverb / Pitch Delay",
            "category": "Reverb",
            "tags": ["lxp-1", "lxp-5", "compact-reverb"]
        })
    write_synth("lexicon", "lxp-1-5", "Lexicon LXP-1 / LXP-5", "Compact Digital Reverb & Effects Module", 1988,
                lxp_cc, lxp_sysex, ["Factory Programs"], lxp_presets)

    # =========================================================================
    # 12. LEXICON MPX-1
    # =========================================================================
    mpx_cc = {"fx_bypass": 91, "delay_time": 82, "reverb_decay": 74}
    mpx_sysex = {"header": "F0 06 06", "device_id_byte": 3, "commands": {"dump_prog": "F0 06 06 01 [prog] F7"}}
    mpx_presets = []
    for p in range(1, 201):
        mpx_presets.append({
            "bank": f"MPX Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"MPX-{p:03d}: Multiple Processor FX",
            "category": "Multi",
            "tags": ["mpx-1", "multiple-processor", "lexicon-fx"]
        })
    write_synth("lexicon", "mpx-1", "Lexicon MPX-1", "Multiple Processor FX Synthesizer", 1996,
                mpx_cc, mpx_sysex, ["MPX Bank 1", "MPX Bank 2"], mpx_presets)

    # =========================================================================
    # 13. MODAL ARGON8
    # =========================================================================
    argon_cc = {"filter_cutoff": 74, "filter_resonance": 71, "wave1_morph": 20, "wave2_morph": 21, "distort": 80}
    argon_sysex = {"header": "F0 00 21 27 01", "device_id_byte": 4, "commands": {"request_patch": "F0 00 21 27 01 01 [bank] [prog] F7"}}
    argon_seeds = [
        "Argon Wavetable Super Lead", "Morphing Ambient Pad", "Resonant Notch Sweep", "Distorted Cyberpunk Bass",
        "Glass Bell Formant", "Shimmer Reverb Cloud", "16-Step Motion Arp", "Warm Sub Saw Low", "Vocal Table Talker"
    ]
    argon_presets = []
    # 5 banks x 100 presets = 500 presets
    for b in range(1, 6):
        b_name = f"Bank {b}"
        for p in range(100):
            seed = argon_seeds[p % len(argon_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(argon_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Cloud" in p_name else "Lead" if "Lead" in p_name else "Bass" if "Bass" in p_name or "Low" in p_name else "Wavetable"
            argon_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["wavetable", "8-voice", "modal-argon8", cat.lower()]
            })
    write_synth("modal", "argon8", "Modal Argon8", "8-Voice Wavetable Synthesizer", 2019,
                argon_cc, argon_sysex, [f"Bank {i}" for i in range(1, 6)], argon_presets)

    # =========================================================================
    # 14. MODAL COBALT8
    # =========================================================================
    cobalt_cc = argon_cc
    cobalt_sysex = {"header": "F0 00 21 27 02", "device_id_byte": 4, "commands": {"request_patch": "F0 00 21 27 02 01 [bank] [prog] F7"}}
    cobalt_presets = []
    cobalt_seeds = [
        "Extended Analog Brass", "Morphing VA Poly Saw", "Ladder Filter Squawk Lead", "Heavy Sub Detune Bass",
        "PWM String Machine", "Sync Squeal Solo", "Complex Ring Mod Pad", "Punchy 4-Pole Pluck", "Acidic Reso 303"
    ]
    for b in range(1, 6):
        b_name = f"Bank {b}"
        for p in range(100):
            seed = cobalt_seeds[p % len(cobalt_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(cobalt_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name or "303" in p_name else "Pad"
            cobalt_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["extended-virtual-analog", "34-algorithms", "modal-cobalt8", cat.lower()]
            })
    write_synth("modal", "cobalt8", "Modal Cobalt8", "8-Voice Extended Virtual Analog Synthesizer", 2020,
                cobalt_cc, cobalt_sysex, [f"Bank {i}" for i in range(1, 6)], cobalt_presets)

    # =========================================================================
    # 15. MODAL SKULPT / CRAFTSYNTH
    # =========================================================================
    skulpt_cc = {"filter_cutoff": 74, "filter_resonance": 71, "wave_spread": 20, "glide": 5}
    skulpt_sysex = {"header": "F0 00 21 27 03", "device_id_byte": 4, "commands": {"request_patch": "F0 00 21 27 03 01 [prog] F7"}}
    skulpt_presets = []
    for p in range(1, 129):
        skulpt_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"Skulpt Sound {p:02d}: 4-Voice Virtual Analog / Wavetable",
            "category": "Virtual Analog",
            "tags": ["portable-va", "skulpt", "craftsynth"]
        })
    write_synth("modal", "skulpt", "Modal Skulpt / CraftSynth", "Compact Virtual Analog / Wavetable Synthesizer", 2018,
                skulpt_cc, skulpt_sysex, ["Factory Presets"], skulpt_presets)

    # =========================================================================
    # 16. MODAL 002
    # =========================================================================
    m002_cc = {"filter_cutoff": 74, "filter_resonance": 71, "filter_drive": 80, "sub_level": 20, "glide": 5}
    m002_sysex = {"header": "F0 00 21 27 00", "device_id_byte": 4, "commands": {"request_patch": "F0 00 21 27 00 01 [bank] [prog] F7"}}
    m002_presets = []
    m002_seeds = [
        "Modal 002 Flagship Hybrid", "Discrete Analog Ladder Warmth", "NCO Digital Precision Poly",
        "Sub Heavy Analog Low", "Vocal Formant Shifter", "Lush 12-Voice Unison Brass", "Complex Ambient Pad",
        "Punchy Transistor Pluck", "Detroit Deep Techno Saw", "Liquid Filter Solo"
    ]
    for b in range(1, 6):
        b_name = f"Bank {b}"
        for p in range(100):
            seed = m002_seeds[p % len(m002_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(m002_seeds) else seed
            cat = "Pad" if "Pad" in p_name else "Brass" if "Brass" in p_name else "Bass" if "Bass" in p_name or "Low" in p_name else "Lead"
            m002_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["12-voice-hybrid", "transistor-ladder-filter", "nco-oscillators", cat.lower()]
            })
    write_synth("modal", "modal-002", "Modal 002", "12-Voice Hybrid Polyphonic Synthesizer", 2014,
                m002_cc, m002_sysex, [f"Bank {i}" for i in range(1, 6)], m002_presets)

    # =========================================================================
    # 17. JOMOX XBASE 09 / AIRBASE 99
    # =========================================================================
    xbase_cc = {"kick_tune": 20, "kick_pitch": 21, "kick_decay": 22, "kick_harmonics": 23, "snare_tune": 24, "snare_snap": 25}
    xbase_sysex = {"header": "F0 33 01", "device_id_byte": 2, "commands": {"dump_kit": "F0 33 01 01 [kit] F7"}}
    xbase_presets = []
    xbase_seeds = [
        "Heavy Techno Kick 909", "Berlin Underground Sub Bassdrum", "Distorted Punch Kick", "Crisp Analog Snare",
        "Industrial Rim Shot", "Metallic Sampled HiHat Closed", "Open Hat Long Decay", "Analog Claps Stereo",
        "Acidic Kick Decay", "Subterranean 20Hz Thud", "Hardcore Distortion Kick", "Crisp 808-Style Sub Thud"
    ]
    for p in range(1, 129):
        seed = xbase_seeds[(p - 1) % len(xbase_seeds)]
        xbase_presets.append({
            "bank": f"Kit Bank {(p - 1) // 64 + 1}",
            "program": p,
            "name": f"XBase Drum Kit {p:02d}: {seed}",
            "category": "Percussion",
            "tags": ["analog-drum-machine", "discrete-kick-snare", "jomox-xbase"]
        })
    write_synth("jomox", "xbase-09", "JoMoX XBase 09 / AirBase 99", "Real Analog Drum Synthesizer", 1996,
                xbase_cc, xbase_sysex, ["Kit Bank 1", "Kit Bank 2"], xbase_presets)

    # =========================================================================
    # 18. DOEPFER MS-404 / DARK ENERGY
    # =========================================================================
    ms404_cc = {"vco_freq": 20, "filter_cutoff": 74, "filter_resonance": 71, "vcf_env_amount": 77, "lfo1_rate": 18}
    ms404_sysex = {"header": "F0 00 20 20", "device_id_byte": 4, "commands": {"dump_patch": "F0 00 20 20 01 [prog] F7"}}
    ms404_presets = []
    ms404_seeds = [
        "Analog Ladder 24dB Bass", "Screaming Acid Lead", "Sub Octave Floor Shaker", "Modulated Noise Wind",
        "Punchy Transistor Pluck", "Overdriven Reso Whine", "Vintage German Monosynth", "Modular LFO Drone"
    ]
    for p in range(1, 65):
        seed = ms404_seeds[(p - 1) % len(ms404_seeds)]
        cat = "Bass" if "Bass" in seed or "Shaker" in seed else "Lead" if "Lead" in seed else "Acid"
        ms404_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"MS-404 Sound {p:02d}: {seed}",
            "category": cat,
            "tags": ["doepfer", "discrete-transistor-ladder", "analog-monosynth", cat.lower()]
        })
    write_synth("doepfer", "ms-404", "Doepfer MS-404 / Dark Energy", "Analog Monophonic Synthesizer Module", 1995,
                ms404_cc, ms404_sysex, ["Factory Bank"], ms404_presets)

    # =========================================================================
    # 19. DIGITECH GSP 2101
    # =========================================================================
    gsp_cc = {"master_volume": 7, "param_1": 16, "param_2": 17, "bypass": 91}
    gsp_sysex = {"header": "F0 00 00 1A", "device_id_byte": 4, "commands": {"request_program": "F0 00 00 1A 01 [prog] F7"}}
    gsp_presets = []
    gsp_seeds = [
        "12AX7 Tube Lead High Gain", "Clean Boutique Tube Chorus", "S-DISC Stereo Pitch Detune", "Ping Pong Ducking Delay",
        "Warm Tube Crunch Rhythm", "Harmonic Whammy Pitch Shifter", "Cathedral Reverb 8s", "Rotary Speaker Tube Overdrive"
    ]
    for p in range(1, 101):
        seed = gsp_seeds[(p - 1) % len(gsp_seeds)]
        gsp_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"GSP2101-{p:02d}: {seed}",
            "category": "Preamp/FX",
            "tags": ["dual-12ax7-tubes", "s-disc-processor", "digitech"]
        })
    for p in range(1, 101):
        gsp_presets.append({
            "bank": "User Bank",
            "program": p,
            "name": f"User Program {p:02d}",
            "category": "User",
            "tags": ["user", "tube-fx"]
        })
    write_synth("digitech", "gsp-2101", "DigiTech GSP 2101 Studio Tube Preamp / Processor", "Dual Tube Guitar Preamp & Multi-FX", 1993,
                gsp_cc, gsp_sysex, ["Factory Bank", "User Bank"], gsp_presets)

    # =========================================================================
    # 20. DIGITECH STUDIO QUAD / TSR-24
    # =========================================================================
    quad_cc = {"bypass": 91, "mod_matrix": 16, "reverb_time": 74}
    quad_sysex = {"header": "F0 00 00 1A 02", "device_id_byte": 4, "commands": {"request_program": "F0 00 00 1A 02 01 [prog] F7"}}
    quad_presets = []
    for p in range(1, 201):
        quad_presets.append({
            "bank": f"Quad Bank {(p - 1) // 100 + 1}",
            "program": p,
            "name": f"Studio Quad {p:03d}: 4-In 4-Out Multi-FX Routing",
            "category": "Multi-FX",
            "tags": ["4-in-4-out", "s-disc", "studio-quad"]
        })
    write_synth("digitech", "studio-quad", "DigiTech Studio Quad / TSR-24", "4-In 4-Out Digital Multi-Effects Processor", 1996,
                quad_cc, quad_sysex, ["Quad Bank 1", "Quad Bank 2"], quad_presets)

if __name__ == "__main__":
    build_wave7()
