#!/usr/bin/env python3
"""
Wave 10 Rares, Boutiques & Vintage Masters Generator for OmniPatch:
- OSCar (Oxford Synthesiser Company)
- Cheetah (MS6)
- Crumar (Bit One / 99)
- Siel (Opera 6 / DK600)
- UDO Audio (Super 6 / Super Gemini)
- Black Corporation (Deckard's Dream)
- Pioneer DJ / Dave Smith (Toraiz AS-1, Toraiz SP-16)
- Studio FX: TC Electronic (2290), Strymon (BigSky, TimeLine), Eventide (Rose)
- Korg Vintage Classics: Mono/Poly, Polysix, Poly-800
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

def build_wave10():
    print("Building Wave 10: OSCar, Cheetah, Crumar, Siel, UDO, Black Corp, Toraiz, Strymon, TC & Vintage Korg...")

    # =========================================================================
    # 1. OXFORD SYNTHESISER COMPANY OSCAR
    # =========================================================================
    oscar_cc = {"filter_cutoff": 74, "filter_separation": 71, "filter_resonance": 75, "drive": 80, "filter_mode": 79}
    oscar_sysex = {"header": "F0 00 00 2F", "device_id_byte": 2, "commands": {"dump_patch": "F0 00 00 2F 01 [prog] F7"}}
    oscar_seeds = [
        "OSCar Dual Filter Scream", "Overdriven Additive Lead", "Separation Dual Peak Bass", "Rubber Reso Bass",
        "Waveform 16 Harmonics Solo", "Highpass Peak Squeal", "Sync Screamer OSCar", "Plucked Transistor Clav"
    ]
    oscar_presets = []
    for p in range(1, 25):
        seed = oscar_seeds[(p - 1) % len(oscar_seeds)]
        cat = "Lead" if "Lead" in seed or "Solo" in seed or "Scream" in seed else "Bass"
        oscar_presets.append({
            "bank": "Factory ROM",
            "program": p,
            "name": f"OSCar ROM {p:02d}: {seed}",
            "category": cat,
            "tags": ["oscar", "dual-filter-separation", "additive-waveforms", "analog-overdrive", cat.lower()]
        })
    for p in range(1, 13):
        oscar_presets.append({
            "bank": "User RAM",
            "program": p,
            "name": f"User Waveform {p:02d}",
            "category": "User",
            "tags": ["user", "additive"]
        })
    write_synth("oscar", "oscar", "Oxford Synthesiser Company OSCar", "Monophonic Additive / Analog Synthesizer", 1983,
                oscar_cc, oscar_sysex, ["Factory ROM", "User RAM"], oscar_presets)

    # =========================================================================
    # 2. CHEETAH MS6
    # =========================================================================
    ms6_cc = {"filter_cutoff": 74, "filter_resonance": 71, "dco1_wave": 20, "dco2_wave": 21, "vcf_env": 77}
    ms6_sysex = {"header": "F0 24 00", "device_id_byte": 2, "commands": {"request_patch": "F0 24 00 01 [prog] F7"}}
    ms6_presets = []
    ms6_seeds = [
        "MS6 Warm Poly Brass", "CEM3396 Reso Bass", "6-Voice Unison Lead", "Lush 80s Poly Strings",
        "Detuned Saw Stabs", "Soft Analog Pad", "Punchy Clavinet", "Syncopated Arp Sound"
    ]
    for p in range(1, 65):
        seed = ms6_seeds[(p - 1) % len(ms6_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Pad" in seed or "Strings" in seed else "Bass" if "Bass" in seed else "Lead"
        ms6_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"MS6-{p:02d}: {seed}",
            "category": cat,
            "tags": ["cem3396", "multitimbral", "analog-module", "cheetah-ms6", cat.lower()]
        })
    write_synth("cheetah", "ms6", "Cheetah MS6", "6-Voice Multitimbral Analog Synthesizer Module", 1988,
                ms6_cc, ms6_sysex, ["Factory Bank"], ms6_presets)

    # =========================================================================
    # 3. CRUMAR BIT ONE / 99 / 01
    # =========================================================================
    bit_cc = {"vcf_cutoff": 74, "vcf_resonance": 71, "dco1_shape": 20, "dco2_shape": 21, "env_decay": 75}
    bit_sysex = {"header": "F0 27 00", "device_id_byte": 2, "commands": {"dump_prog": "F0 27 00 01 [prog] F7"}}
    bit_presets = []
    bit_seeds = [
        "Italian Warm Poly Brass", "CEM3328 Resonant Sweep", "Bit 99 Dual DCO Bass", "Chorus Ensemble Strings",
        "Velocity Sensitive Pluck", "Warm Sine Organ", "Punchy Electro Stab", "Dark Vintage Drone"
    ]
    for p in range(1, 76):
        seed = bit_seeds[(p - 1) % len(bit_seeds)]
        cat = "Brass" if "Brass" in seed else "Pad" if "Strings" in seed or "Drone" in seed else "Bass" if "Bass" in seed else "Lead"
        bit_presets.append({
            "bank": "Factory Programs",
            "program": p,
            "name": f"Bit-{p:02d}: {seed}",
            "category": cat,
            "tags": ["cem3328", "dual-dco", "analog-poly", "crumar-bit", cat.lower()]
        })
    write_synth("crumar", "bit", "Crumar Bit One / Bit 99 / Bit 01", "Polyphonic Analog Synthesizer", 1984,
                bit_cc, bit_sysex, ["Factory Programs"], bit_presets)

    # =========================================================================
    # 4. SIEL OPERA 6 / DK600
    # =========================================================================
    siel_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo_depth": 1, "dco_range": 20}
    siel_sysex = {"header": "F0 21 00", "device_id_byte": 2, "commands": {"dump_patch": "F0 21 00 01 [prog] F7"}}
    siel_presets = []
    siel_seeds = [
        "SSM2044 Silky Poly Strings", "Opera 6 Rich Brass", "Dual DCO Warm Bass", "Italian Space Pad",
        "Resonant Filter Flute", "Vintage Analog Clav", "Chorus Stereo Lead", "Dark Cathedral Organ"
    ]
    for p in range(1, 96):
        seed = siel_seeds[(p - 1) % len(siel_seeds)]
        cat = "Strings" if "Strings" in seed else "Brass" if "Brass" in seed else "Bass" if "Bass" in seed else "Pad"
        siel_presets.append({
            "bank": "Internal Bank",
            "program": p,
            "name": f"Opera-{p:02d}: {seed}",
            "category": cat,
            "tags": ["ssm2044-filter", "dual-dco", "analog-poly", "siel-opera", cat.lower()]
        })
    write_synth("siel", "opera-6", "Siel Opera 6 / DK600", "6-Voice Polyphonic Analog Synthesizer", 1983,
                siel_cc, siel_sysex, ["Internal Bank"], siel_presets)

    # =========================================================================
    # 5. UDO AUDIO SUPER 6 / SUPER GEMINI
    # =========================================================================
    udo_cc = {"filter_cutoff": 74, "filter_resonance": 71, "binaural_spread": 10, "dds1_shape": 20, "dds2_detune": 21, "delay_time": 82}
    udo_sysex = {"header": "F0 00 21 4B", "device_id_byte": 3, "commands": {"request_patch": "F0 00 21 4B 01 [bank] [prog] F7"}}
    udo_seeds = [
        "Binaural 12-Voice Super Saw", "SSI2144 Silky Analog Lowpass", "High-Resolution DDS Wavetable", "Stereo Spatial Cloud Pad",
        "Binaural Detuned Poly Brass", "Punchy Analog Bass 24dB", "Resonant Bandpass Pluck", "Lush Shimmer Chorus Solo"
    ]
    udo_presets = []
    # 8 banks x 16 patches = 128 presets
    for b in range(1, 9):
        b_name = f"Bank {b}"
        for p in range(1, 17):
            idx = (b - 1) * 16 + (p - 1)
            seed = udo_seeds[idx % len(udo_seeds)]
            p_name = f"Super6 {b}-{p:02d}: {seed}"
            cat = "Pad" if "Pad" in seed or "Cloud" in seed else "Brass" if "Brass" in seed else "Bass" if "Bass" in seed else "Lead"
            udo_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["binaural-synthesis", "fpga-dds", "ssi2144-filter", "udo-super-6", cat.lower()]
            })
    write_synth("udo_audio", "super-6", "UDO Audio Super 6 / Super Gemini", "Binaural 12-Voice Polyphonic Synthesizer", 2020,
                udo_cc, udo_sysex, [f"Bank {i}" for i in range(1, 9)], udo_presets)

    # =========================================================================
    # 6. BLACK CORPORATION DECKARD'S DREAM / KIJIMI
    # =========================================================================
    dd_cc = {"vcf1_cutoff": 74, "vcf1_resonance": 71, "vcf2_cutoff": 79, "poly_aftertouch": 1, "ribbon": 16}
    dd_sysex = {"header": "F0 00 21 3F", "device_id_byte": 3, "commands": {"request_preset": "F0 00 21 3F 01 [bank] [prog] F7"}}
    dd_seeds = [
        "Blade Runner 2049 Poly Lead", "Dual Discrete 8-Voice Swell", "Poly Aftertouch Brass Section", "Vangelis Nostalgia Strings",
        "CS-80 Pure Triangle Flute", "Highpass Shimmer Reverb Pad", "Detuned Dual Saw Heavy Low", "Expressive Polyphonic Swell"
    ]
    dd_presets = []
    for b_name in ["Factory Bank", "User Bank"]:
        for p in range(1, 129):
            seed = dd_seeds[(p - 1) % len(dd_seeds)]
            p_name = f"DDRM {seed} {p}" if p > len(dd_seeds) else f"DDRM {seed}"
            cat = "Brass" if "Brass" in p_name else "Strings" if "Strings" in p_name or "Pad" in p_name or "Swell" in p_name else "Lead" if "Lead" in p_name or "Flute" in p_name else "Bass"
            dd_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["cs-80-lineage", "poly-aftertouch", "discrete-analog", "deckards-dream", cat.lower()]
            })
    write_synth("black_corporation", "deckards-dream", "Black Corporation Deckard's Dream / Kijimi", "8-Voice Polyphonic Analog Synthesizer", 2017,
                dd_cc, dd_sysex, ["Factory Bank", "User Bank"], dd_presets)

    # =========================================================================
    # 7. PIONEER DJ / DSI TORAIZ AS-1
    # =========================================================================
    as1_cc = {"filter_cutoff": 74, "filter_resonance": 71, "highpass_cutoff": 79, "distortion": 80, "sub_osc": 20, "glide": 5}
    as1_sysex = {"header": "F0 01 2F", "device_id_byte": 3, "commands": {"request_program": "F0 01 2F 05 [bank] [prog] F7"}}
    as1_seeds = [
        "Prophet-6 Monophonic Bass", "Dual Discrete VCO Lead", "Cross-Mod Screamer", "Sub Octave Floor Shaker",
        "Highpass Filtered Acid", "Analog BBD Chorus Solo", "Punchy 4-Pole Pluck", "Vintage Detuned Saw Mono"
    ]
    as1_presets = []
    # 5 factory banks x 99 = 495 presets
    for b in range(1, 6):
        b_name = f"Factory Bank {b}"
        for p in range(1, 100):
            seed = as1_seeds[(p - 1) % len(as1_seeds)]
            p_name = f"AS1-{b}-{p:02d}: {seed}"
            cat = "Bass" if "Bass" in seed or "Shaker" in seed else "Lead" if "Lead" in seed or "Solo" in seed or "Screamer" in seed else "Acid"
            as1_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["prophet-6-voice", "dave-smith", "discrete-analog-mono", "toraiz-as1", cat.lower()]
            })
    write_synth("pioneer_dj", "toraiz-as1", "Pioneer DJ / Dave Smith Toraiz AS-1", "Monophonic Analog Synthesizer", 2017,
                as1_cc, as1_sysex, [f"Factory Bank {i}" for i in range(1, 6)], as1_presets)

    # =========================================================================
    # 8. PIONEER DJ / DSI TORAIZ SP-16
    # =========================================================================
    sp16_cc = {"filter_cutoff": 74, "filter_resonance": 71, "drive": 80}
    sp16_sysex = {"header": "F0 01 2E 02", "device_id_byte": 3, "commands": {"dump_project": "F0 01 2E 02 01 [proj] F7"}}
    sp16_presets = []
    for p in range(1, 129):
        sp16_presets.append({
            "bank": f"Project Bank {(p - 1) // 32 + 1}",
            "program": p,
            "name": f"SP-16 Project {p:03d}: Dave Smith Analog Filter Groove",
            "category": "Sampler/Groove",
            "tags": ["dave-smith-filters", "prophet-6-filter", "professional-sampler", "toraiz-sp16"]
        })
    write_synth("pioneer_dj", "toraiz-sp16", "Pioneer DJ / Dave Smith Toraiz SP-16", "Professional Sampler & Step Sequencer", 2016,
                sp16_cc, sp16_sysex, [f"Project Bank {i}" for i in range(1, 5)], sp16_presets)

    # =========================================================================
    # 9. TC ELECTRONIC 2290
    # =========================================================================
    tc_cc = {"delay_time": 82, "feedback": 83, "dynamic_ducking": 16, "modulation_depth": 17, "fx_mix": 91}
    tc_sysex = {"header": "F0 00 20 1F", "device_id_byte": 3, "commands": {"dump_prog": "F0 00 20 1F 01 [prog] F7"}}
    tc_presets = []
    tc_seeds = [
        "The Edge Dotted 8th Dynamic Delay", "Stereo Ducking Vocal Echo", "Panned Chorus Delay 350ms", "Analog Warm Tape Simulation",
        "Dynamic Modulated Delay 500ms", "Slapback Vintage Rock 120ms", "Long Ambient Canyon Echo 4s", "Reverse Pitch Shift Delay"
    ]
    for p in range(1, 101):
        seed = tc_seeds[(p - 1) % len(tc_seeds)]
        tc_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"TC-2290 Prog {p:02d}: {seed}",
            "category": "Delay",
            "tags": ["tc-2290", "dynamic-digital-delay", "studio-reference-delay"]
        })
    write_synth("tc_electronic", "tc-2290", "TC Electronic 2290", "Dynamic Digital Delay + Effects Processor", 1985,
                tc_cc, tc_sysex, ["Factory Bank"], tc_presets)

    # =========================================================================
    # 10. STRYMON BIGSKY
    # =========================================================================
    bs_cc = {"decay": 74, "predelay": 18, "tone": 19, "param1": 20, "param2": 21, "mix": 91}
    bs_sysex = {"header": "F0 00 01 55 12", "device_id_byte": 4, "commands": {"request_preset": "F0 00 01 55 12 01 [prog] F7"}}
    bs_seeds = [
        "Cloud Ethereal Ambient Space", "Shimmer Octave Up Angels", "Bloom Swelling Infinite", "Chorale Vocal Choir Reverb",
        "Magneto Multi-Head Tape Echo", "Reflections Small Studio Room", "Plate Bright Studio Vocal", "Hall Concert 5.0s",
        "Room Natural Wood Ambience", "Nonlinear Gated Snare Reverb", "Swell Slow Fade In Cloud", "Spring Dual Tank Vintage"
    ]
    bs_presets = []
    for p in range(1, 301):
        seed = bs_seeds[(p - 1) % len(bs_seeds)]
        bs_presets.append({
            "bank": f"Bank {(p - 1) // 2 + 1} ({'A' if p % 2 != 0 else 'B'})",
            "program": p,
            "name": f"BigSky {p:03d}: {seed}",
            "category": "Reverb",
            "tags": ["strymon", "bigsky", "shimmer", "cloud-reverb", "studio-reverb"]
        })
    write_synth("strymon", "bigsky", "Strymon BigSky", "Multidimensional Reverb Processor", 2013,
                bs_cc, bs_sysex, [f"Bank {i}" for i in range(1, 151)], bs_presets)

    # =========================================================================
    # 11. STRYMON TIMELINE
    # =========================================================================
    tl_cc = {"delay_time": 82, "repeats": 83, "filter": 19, "grit": 20, "speed": 21, "depth": 22, "mix": 91}
    tl_sysex = {"header": "F0 00 01 55 11", "device_id_byte": 4, "commands": {"request_preset": "F0 00 01 55 11 01 [prog] F7"}}
    tl_seeds = [
        "dTape Vintage Space Echo", "dBucket Warm BBD Chorus", "Digital Pristine 24-Bit", "Dual Series/Parallel Taps",
        "Pattern Polyrhythmic 8-Tap", "Reverse Psychedelic Swell", "Ice Shimmer Pitch Shift Delay", "Duck Dynamic Sidechain Echo",
        "Swell Slow Attack Ambient", "Tremolo Pulsing Modulation Delay", "Filter Swept Resonant Delay", "Lo-Fi Gritty Vinyl 12-Bit"
    ]
    tl_presets = []
    for p in range(1, 301):
        seed = tl_seeds[(p - 1) % len(tl_seeds)]
        tl_presets.append({
            "bank": f"Bank {(p - 1) // 2 + 1} ({'A' if p % 2 != 0 else 'B'})",
            "program": p,
            "name": f"TimeLine {p:03d}: {seed}",
            "category": "Delay",
            "tags": ["strymon", "timeline", "dtape", "dbucket", "ice-delay"]
        })
    write_synth("strymon", "timeline", "Strymon TimeLine", "Multidimensional Delay Processor", 2011,
                tl_cc, tl_sysex, [f"Bank {i}" for i in range(1, 151)], tl_presets)

    # =========================================================================
    # 12. EVENTIDE ROSE / PITCHFACTOR
    # =========================================================================
    rose_cc = {"delay_time": 82, "feedback": 83, "filter": 74, "rate": 18, "depth": 19, "mix": 91}
    rose_sysex = {"header": "F0 1C 05", "device_id_byte": 3, "commands": {"request_preset": "F0 1C 05 01 [prog] F7"}}
    rose_presets = []
    rose_seeds = [
        "Modulated Analog BBD Delay", "Reverse Tape Flanger", "Pitch Shift Octave Shimmer", "Fast Slapback Room",
        "Infinite Feedback Drone", "Ducked Echo Vocal", "Envelope Modulated Filter Sweep", "Glitch Pitch Randomizer"
    ]
    for p in range(1, 101):
        seed = rose_seeds[(p - 1) % len(rose_seeds)]
        rose_presets.append({
            "bank": "Factory Presets",
            "program": p,
            "name": f"Rose/Pitch-{p:02d}: {seed}",
            "category": "Delay/Pitch",
            "tags": ["eventide-rose", "analog-digital-hybrid", "pitchfactor"]
        })
    write_synth("eventide", "rose", "Eventide Rose / PitchFactor", "Modulated Delay & Pitch Processor", 2019,
                rose_cc, rose_sysex, ["Factory Presets"], rose_presets)

    # =========================================================================
    # 13. KORG MONO/POLY MP-4
    # =========================================================================
    mp_cc = {"cutoff": 74, "resonance": 71, "eg_intensity": 77, "vco1_tune": 20, "vco2_tune": 21, "vco3_tune": 22, "vco4_tune": 23}
    mp_sysex = {"header": "F0 42 00 00", "device_id_byte": 2, "commands": {"dump_patch": "F0 42 00 00 01 [prog] F7"}}
    mp_presets = []
    mp_seeds = [
        "4-VCO Cycling Arpeggiator", "SSM2044 Resonant Scream", "Cross-Mod & Sync Lead", "Subterranean 4-VCO Bass",
        "Paraphonic Chord Memory", "Detuned 4-Saw Monster", "Warm SSM Flute Lead", "Alien FX Cross-Mod Wind"
    ]
    for p in range(1, 65):
        seed = mp_seeds[(p - 1) % len(mp_seeds)]
        cat = "Arp" if "Arpeggiator" in seed else "Lead" if "Lead" in seed or "Scream" in seed else "Bass" if "Bass" in seed else "Paraphonic"
        mp_presets.append({
            "bank": "Factory Patches",
            "program": p,
            "name": f"Mono/Poly Patch {p:02d}: {seed}",
            "category": cat,
            "tags": ["4-vco", "ssm2044-vcf", "cycling-arpeggiator", "korg-mono-poly", cat.lower()]
        })
    write_synth("korg", "mono-poly", "Korg Mono/Poly MP-4", "4-VCO Analog Synthesizer", 1981,
                mp_cc, mp_sysex, ["Factory Patches"], mp_presets)

    # =========================================================================
    # 14. KORG POLYSIX PS-6
    # =========================================================================
    ps6_cc = {"vcf_cutoff": 74, "vcf_resonance": 71, "sub_osc": 20, "vcf_eg": 77, "ensemble_depth": 92}
    ps6_sysex = {"header": "F0 42 00 02", "device_id_byte": 2, "commands": {"dump_prog": "F0 42 00 02 01 [prog] F7"}}
    ps6_presets = []
    ps6_seeds = [
        "Polysix Ensemble Strings", "SSM2044 Warm Poly Brass", "Sub Octave Analog Bass", "Detuned 6-Voice Unison Lead",
        "BBD Chorus Warm Pad", "Arpeggiated Reso Pluck", "Vintage Analog Organ", "Soft Polyphonic Clav"
    ]
    for p in range(1, 65):
        seed = ps6_seeds[(p - 1) % len(ps6_seeds)]
        cat = "Strings" if "Strings" in seed else "Brass" if "Brass" in seed else "Bass" if "Bass" in seed else "Pad" if "Pad" in seed else "Lead"
        ps6_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"Polysix-{p:02d}: {seed}",
            "category": cat,
            "tags": ["ssm2044-filter", "bbd-ensemble-chorus", "analog-poly", "korg-polysix", cat.lower()]
        })
    write_synth("korg", "polysix", "Korg Polysix PS-6", "6-Voice Polyphonic Analog Synthesizer", 1981,
                ps6_cc, ps6_sysex, ["Factory Bank"], ps6_presets)

    # =========================================================================
    # 15. KORG POLY-800
    # =========================================================================
    p800_cc = {"cutoff": 74, "resonance": 71, "dco1_octave": 20, "dco2_octave": 21, "chorus": 93}
    p800_sysex = {"header": "F0 42 00 06", "device_id_byte": 2, "commands": {"dump_prog": "F0 42 00 06 01 [prog] F7"}}
    p800_presets = []
    p800_seeds = [
        "Poly-800 Stereo Brass", "Paraphonic Synth Bass", "80s Italo Disco Strings", "Chirp Resonant Pluck",
        "Stereo Chorus Poly Pad", "Square Wave Funk Bass", "Sci-Fi Noise Zap", "Bowed Synth Violin"
    ]
    for p in range(1, 65):
        seed = p800_seeds[(p - 1) % len(p800_seeds)]
        cat = "Brass" if "Brass" in seed else "Strings" if "Strings" in seed or "Pad" in seed else "Bass" if "Bass" in seed else "Lead"
        p800_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"Poly800-{p:02d}: {seed}",
            "category": cat,
            "tags": ["8-dco-paraphonic", "deg-envelopes", "korg-poly-800", cat.lower()]
        })
    write_synth("korg", "poly-800", "Korg Poly-800", "Programmable Polyphonic Synthesizer", 1983,
                p800_cc, p800_sysex, ["Factory Bank"], p800_presets)

if __name__ == "__main__":
    build_wave10()
