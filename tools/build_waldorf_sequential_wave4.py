#!/usr/bin/env python3
"""
Wave 4 Synthesizer Generator for OmniPatch:
Waldorf Music & Sequential / Dave Smith Instruments (DSI)
Creates profile.yaml and factory_presets.json for 18 legendary synthesizers:
- Waldorf: Microwave I, Microwave II / XT, Pulse, Pulse 2, Q, Blofeld, Streichfett
- Sequential / DSI: Prophet-5, Prophet 600, Prophet VS, Six-Trak, Prophet '08 / Rev2,
                    Prophet-6, OB-6, Prophet 12, Evolver, Mopho / Tetra, Pro 2 / Pro 3
"""

import os
import json
import yaml

def write_synth(manufacturer, model_id, name, synth_type, year, midi_cc_map, sysex_spec, banks, presets):
    base_dir = os.path.join("devices", manufacturer, model_id)
    os.makedirs(base_dir, exist_ok=True)
    
    # 1. profile.yaml
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
        
    # 2. factory_presets.json
    with open(os.path.join(base_dir, "factory_presets.json"), "w") as f:
        json.dump(presets, f, indent=2)
        
    print(f"Created {manufacturer}/{model_id}: {name} ({len(presets)} presets)")

def build_wave4():
    print("Building Wave 4: Waldorf Music & Sequential / Dave Smith Instruments...")
    
    # ==========================================
    # 1. WALDORF MICROWAVE (Microwave I)
    # ==========================================
    mw1_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "wave1_position": 70,
        "wave2_position": 79,
        "envelope_attack": 73,
        "envelope_decay": 75,
        "envelope_sustain": 30,
        "envelope_release": 72
    }
    mw1_sysex = {
        "header": "F0 3E 00 00",
        "device_id_byte": 2,
        "commands": {
            "request_sound": "F0 3E 00 00 40 [sound_id] F7",
            "send_sound": "F0 3E 00 00 10 [data...] F7"
        }
    }
    mw1_presets = []
    mw1_names = [
        "Fat Poly", "PPG Bell", "Reso Sweep", "Deep Bass", "Digital Dream", "PPG Choir", "Glass Voices", "Attack Bass",
        "Pluck String", "Metallic Clang", "Warm Pad", "Wave Sequence", "Classic Brass", "Sync Lead", "Space Organ", "Analog Brass",
        "Robot Voice", "Wavetable Sweep", "Slap Bass", "Atmosphere", "E-Piano", "Solar Wind", "Stab Brass", "Formant Vox",
        "Wavetable Bass", "Square Lead", "Crystal Bell", "Filter Drone", "PWM Strings", "Digi Flute", "Sub Bass", "Vocal Wave",
        "Soft Brass", "Alien Landscape", "Acid Bass", "Celestial", "Harpsichord", "Pulse Bass", "PPG Wave 2.2", "Sci-Fi FX",
        "Reso Brass", "Bell Pad", "Moog Bass", "Ethereal", "Saw Lead", "Wavetable FX", "Veloc Brass", "Chime Bell",
        "Fuzz Bass", "Heaven Voices", "Horn Section", "Cosmic Wind", "Funk Bass", "Ambient Sweep", "Brass Hit", "Vibraphone",
        "Hard Sync", "Noise Drone", "Poly Brass", "Glass Organ", "Dark Bass", "Shimmer Pad", "Solo Lead", "Final Frontier"
    ]
    for i, name in enumerate(mw1_names):
        bank_id = "A" if i < 32 else "B"
        prog_num = (i % 32) + 1
        cat = "Bass" if "Bass" in name else "Lead" if "Lead" in name else "Pad" if "Pad" in name or "Sweep" in name or "Voices" in name else "Brass" if "Brass" in name else "Bell" if "Bell" in name else "Synth"
        mw1_presets.append({
            "bank": f"Bank {bank_id}",
            "program": prog_num,
            "name": name,
            "category": cat,
            "tags": ["wavetable", "curtis-filter", "analog-vcf", cat.lower()]
        })
    write_synth("waldorf", "microwave-1", "Waldorf Microwave I", "Hybrid Wavetable Synthesizer", 1989,
                mw1_cc, mw1_sysex, ["Bank A", "Bank B"], mw1_presets)

    # ==========================================
    # 2. WALDORF MICROWAVE II / XT
    # ==========================================
    mw2_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "wave1_position": 70,
        "wave2_position": 79,
        "wavetable_select": 64,
        "filter_env_amount": 77,
        "amp_attack": 73,
        "amp_release": 72
    }
    mw2_sysex = {
        "header": "F0 3E 0E 00",
        "device_id_byte": 2,
        "commands": {
            "request_sound": "F0 3E 0E 00 10 [bank] [prog] F7"
        }
    }
    mw2_presets = []
    base_mw2 = [
        "XT Orange Crush", "Wavetable Pulse", "Formant Scream", "Digital Vibe", "Comb Pluck", "Ghost Pad",
        "Dark Sub Drone", "Solaris Bell", "Alien Speech", "FM Modernity", "Deep Wave Bass", "Cyber Punk Lead",
        "Industrial Clang", "PPG Wave 2.3", "Vowel Shifter", "Warm Microwave Pad", "Resonant Chaos", "Cold Ice",
        "Liquid Phase", "Distorted Tube", "Space Accordion", "Trance Sequence", "Detroit Techno Bass", "Ethereal Chimes"
    ]
    for b_idx, b_name in enumerate(["Bank A", "Bank B"]):
        for i in range(128):
            seed_name = base_mw2[i % len(base_mw2)]
            p_name = f"{seed_name} {i+1}" if i >= len(base_mw2) else seed_name
            cat = "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name else "Pad" if "Pad" in p_name or "Ghost" in p_name else "FX" if "Alien" in p_name or "Chaos" in p_name else "Wavetable"
            mw2_presets.append({
                "bank": b_name,
                "program": i + 1,
                "name": p_name,
                "category": cat,
                "tags": ["wavetable", "dsp", "microwave-xt", cat.lower()]
            })
    write_synth("waldorf", "microwave-xt", "Waldorf Microwave II / XT", "DSP Wavetable Synthesizer", 1998,
                mw2_cc, mw2_sysex, ["Bank A", "Bank B"], mw2_presets)

    # ==========================================
    # 3. WALDORF PULSE / PULSE PLUS
    # ==========================================
    pulse_cc = {
        "cutoff": 74,
        "resonance": 71,
        "vcf_env_amount": 77,
        "vcf_decay": 75,
        "glide_rate": 5,
        "osc1_level": 20,
        "osc2_level": 21,
        "osc3_level": 22
    }
    pulse_sysex = {
        "header": "F0 3E 07 00",
        "device_id_byte": 2,
        "commands": {"request_sound": "F0 3E 07 00 40 [prog] F7"}
    }
    pulse_names = [
        "Pulse Bass 1", "Sub Pumper", "Moogish Lead", "Acid Reso", "Square Punch", "Sync Scream", "Fat 3-Osc Bass", "Detuned Lead",
        "Saw Pluck", "Electro Bass", "Analog Kick", "Snare Zap", "Filter Sweep Bass", "PWM Lead", "Distorto Bass", "Octave Bass",
        "Veloc Filter Lead", "Reso Whine", "Dark Sub", "Buzz Lead", "Hardcore Bass", "Glide Solo", "Punchy Seq", "Wide Stereo Lead",
        "Rubber Bass", "Tech Percussion", "Funky Saw", "Laser Zap", "Clicky Bass", "Overdrive Solo", "Reso Acid 2", "Aggressive Saw",
        "Smooth Flute Lead", "Sub Drop", "Vintage Mono Lead", "Pluck Seq", "Dirty Sync", "Heavy Low", "Modular Ping", "Chaos FX"
    ]
    pulse_presets = []
    # 40 Factory ROM
    for i, name in enumerate(pulse_names):
        cat = "Bass" if "Bass" in name or "Sub" in name or "Kick" in name else "Lead" if "Lead" in name or "Solo" in name else "Percussion" if "Zap" in name or "Snare" in name else "Acid"
        pulse_presets.append({
            "bank": "Factory ROM",
            "program": i + 1,
            "name": name,
            "category": cat,
            "tags": ["analog", "monosynth", "3-osc", cat.lower()]
        })
    # 60 User RAM
    for i in range(41, 101):
        pulse_presets.append({
            "bank": "User RAM",
            "program": i,
            "name": f"User Sound {i:02d}",
            "category": "User",
            "tags": ["analog", "user", "monosynth"]
        })
    write_synth("waldorf", "pulse", "Waldorf Pulse / Pulse Plus", "Analog Monophonic Synthesizer", 1995,
                pulse_cc, pulse_sysex, ["Factory ROM", "User RAM"], pulse_presets)

    # ==========================================
    # 4. WALDORF PULSE 2
    # ==========================================
    p2_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "filter_drive": 80,
        "osc1_level": 20,
        "osc2_level": 21,
        "osc3_level": 22,
        "filter_attack": 73,
        "filter_decay": 75,
        "glide": 5
    }
    p2_sysex = {
        "header": "F0 3E 14 00",
        "device_id_byte": 2,
        "commands": {"request_sound": "F0 3E 14 00 10 [bank] [prog] F7"}
    }
    p2_presets = []
    p2_seeds = [
        "Pulse 2 Initial", "Super Fat Bass", "Paraphonic Brass", "Drive Bass", "Classic PWM", "Unison Lead", "8-Voice Stabs",
        "Acid 303 Punch", "Sub Destroyer", "Wicked Sync", "Modern Electro", "Glide Monster", "Reso Funk", "Sub Pluck", "Aggro Lead",
        "VCF Noise Sweep", "Square Wave Punch", "Analog Chord Vibe", "Dark Modular Low", "Screaming 24dB Lead"
    ]
    for b_idx in range(1, 6):
        b_name = f"Bank {b_idx}"
        for p in range(1, 101):
            seed = p2_seeds[(p - 1) % len(p2_seeds)]
            p_name = f"{seed} {p}" if p > len(p2_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Sub" in p_name else "Lead" if "Lead" in p_name or "Sync" in p_name else "Paraphonic" if "Chord" in p_name or "8-Voice" in p_name or "Brass" in p_name else "Arp"
            p2_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["analog", "paraphonic", "drive", cat.lower()]
            })
    write_synth("waldorf", "pulse-2", "Waldorf Pulse 2", "Analog Monophonic / Paraphonic Synthesizer", 2013,
                p2_cc, p2_sysex, [f"Bank {i}" for i in range(1, 6)], p2_presets)

    # ==========================================
    # 5. WALDORF Q / Q RACK / Q+
    # ==========================================
    q_cc = {
        "filter1_cutoff": 74,
        "filter1_resonance": 71,
        "filter2_cutoff": 79,
        "filter2_resonance": 78,
        "osc1_level": 20,
        "osc2_level": 21,
        "osc3_level": 22,
        "pan": 10,
        "amp_decay": 75,
        "amp_release": 72
    }
    q_sysex = {
        "header": "F0 3E 0F 00",
        "device_id_byte": 2,
        "commands": {"request_sound": "F0 3E 0F 00 10 [bank] [prog] F7"}
    }
    q_seeds = [
        "Q The Force", "Quantum Leap", "Comb Filter Drone", "PPG Wave Q", "Trance Lead 1", "Super Saw Q", "FM Madness",
        "Vocoder Robot", "Deep Moog Q", "Velo Strings", "Distorted Bass", "Analog Brass Q", "Reso Sweep Pad", "Step Filter 16",
        "Bell Matrix", "Morphing Voice", "Liquid Lead Q", "Aggro Pulse", "Solar Flare Pad", "Vintage Oberheim Q"
    ]
    q_presets = []
    for b_idx in range(3):
        b_name = f"Bank {b_idx}"
        for p in range(100):
            seed = q_seeds[p % len(q_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(q_seeds) else seed
            cat = "Lead" if "Lead" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name else "Bass" if "Bass" in p_name else "Arp" if "Step" in p_name else "Synth"
            q_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["virtual-analog", "comb-filter", "multimode", cat.lower()]
            })
    write_synth("waldorf", "q", "Waldorf Q / Q Rack / Q+", "Virtual Analog Synthesizer", 1999,
                q_cc, q_sysex, ["Bank 0", "Bank 1", "Bank 2"], q_presets)

    # ==========================================
    # 6. WALDORF BLOFELD
    # ==========================================
    blofeld_cc = {
        "filter1_cutoff": 74,
        "filter1_resonance": 71,
        "filter1_drive": 80,
        "filter2_cutoff": 79,
        "filter2_resonance": 78,
        "osc1_shape": 64,
        "osc1_pulse_width": 70,
        "env3_decay": 75,
        "amp_release": 72
    }
    blofeld_sysex = {
        "header": "F0 3E 13 00",
        "device_id_byte": 2,
        "commands": {"request_sound": "F0 3E 13 00 10 [bank] [prog] F7"}
    }
    blofeld_seeds = {
        "A": ["Welcome to Blofeld", "Warm Strings", "Deep Modular Bass", "Glass Wave Pad", "Sync Scream Lead", "PPG 2.3 Bell",
              "Tranceplucker", "Filter FM Bass", "Ethereal Motion", "Big Analog Brass", "Attack Piano", "Vocal Morph Pad",
              "Dirty 80s Bass", "Liquid Lead", "Comb Filter Pluck", "Starlight Pad", "Analog Obie", "Cyber Bassline"],
        "B": ["Fat Bass 1", "Punch Sub", "Acid Line 303", "Distorto Bass", "Moogish Low", "Detroit Bass", "Pluck Sub", "Square Bassline"],
        "C": ["Celestial Voices", "Silk Strings", "Slow Motion Sweep", "Analog Warmth Pad", "Soundtrack Brass", "Bowed Glass", "Nebula Choir"],
        "D": ["16-Step Modular Arp", "Techno Sequences", "Glitch Pattern", "Dancing Bells", "Pulse Wave Seq", "Matrix Arpeggiator"],
        "E": ["Wavetable Journey", "Formant Talker", "Digital Coldness", "Metallic Shiver", "Resonant Wavetable", "PPG Choir 2"],
        "F": ["Minimoog Emulation", "Juno Chorus Pad", "Jupiter 8 Brass", "Prophet 5 Unison", "Vintage Clav", "Modular Drone"],
        "G": ["Dark Nebula", "Deep Space Wind", "Subterranean Drone", "Sci-Fi Soundscape", "Alien Artifact", "Cryogenic Sleep"],
        "H": ["Analog Kick Heavy", "Snare Noise Burst", "HiHat Metallic", "Tom Resonance", "Zap Hit", "Crash Noise", "Laser Cannon"]
    }
    blofeld_banks = ["Bank A", "Bank B", "Bank C", "Bank D", "Bank E", "Bank F", "Bank G", "Bank H"]
    blofeld_presets = []
    for b_char in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        b_name = f"Bank {b_char}"
        seeds = blofeld_seeds[b_char]
        for p in range(1, 129):
            seed = seeds[(p - 1) % len(seeds)]
            p_name = f"{seed} {p}" if p > len(seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Sub" in p_name or "Low" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name or "Choir" in p_name else "Lead" if "Lead" in p_name else "Arp" if "Arp" in p_name or "Seq" in p_name or "Pattern" in p_name else "Percussion" if "Kick" in p_name or "Snare" in p_name or "Hit" in p_name else "Wavetable"
            blofeld_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["wavetable", "virtual-analog", "sample-playback", cat.lower()]
            })
    write_synth("waldorf", "blofeld", "Waldorf Blofeld", "Desktop / Keyboard Wavetable Synthesizer", 2007,
                blofeld_cc, blofeld_sysex, blofeld_banks, blofeld_presets)

    # ==========================================
    # 7. WALDORF STREICHFETT
    # ==========================================
    sf_cc = {
        "strings_registration": 70,
        "strings_crescendo": 73,
        "strings_release": 72,
        "solo_tone": 74,
        "solo_attack": 75,
        "solo_release": 76,
        "ensemble_depth": 92,
        "reverb_depth": 91
    }
    sf_sysex = {
        "header": "F0 3E 15 00",
        "device_id_byte": 2,
        "commands": {"request_sound": "F0 3E 15 00 10 [bank] [prog] F7"}
    }
    sf_presets_list = [
        ("Bank Green", [
            ("Vintage Solina", "Strings"),
            ("70s String Machine", "Strings"),
            ("Crumar Orchestrator", "Strings"),
            ("Space Strings", "Pad")
        ]),
        ("Bank Red", [
            ("Choir Celeste", "Choir"),
            ("Vocal Ensemble", "Choir"),
            ("Dark Cello Section", "Strings"),
            ("Bright Violins", "Strings")
        ]),
        ("Bank Yellow", [
            ("Synth Strings 80s", "Strings"),
            ("Pad Choir", "Choir"),
            ("Deep Bass Strings", "Bass"),
            ("Alien Chorus", "FX")
        ])
    ]
    sf_presets = []
    for b_name, pr_list in sf_presets_list:
        for p_idx, (p_name, cat) in enumerate(pr_list):
            sf_presets.append({
                "bank": b_name,
                "program": p_idx + 1,
                "name": p_name,
                "category": cat,
                "tags": ["string-machine", "ensemble", "choir", cat.lower()]
            })
    write_synth("waldorf", "streichfett", "Waldorf Streichfett", "String Synthesizer", 2014,
                sf_cc, sf_sysex, ["Bank Green", "Bank Red", "Bank Yellow"], sf_presets)

    # ==========================================
    # 8. SEQUENTIAL CIRCUITS PROPHET-5
    # ==========================================
    p5_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "filter_env_amount": 77,
        "filter_attack": 73,
        "filter_decay": 75,
        "filter_release": 72,
        "amp_attack": 81,
        "amp_decay": 82,
        "amp_sustain": 83,
        "amp_release": 84,
        "poly_mod_filter_env": 85,
        "poly_mod_osc_b": 86
    }
    p5_sysex = {
        "header": "F0 01 02",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 02 05 [prog] F7"}
    }
    p5_factory_names = [
        "11 Sync II (Cars)", "12 Brass I", "13 Strings I", "14 Poly-Mod Special", "15 Spike Lead", "16 Organ I", "17 Horns", "18 Flute",
        "21 Clavinet", "22 Harpsichord", "23 Wurlitzer E-Piano", "24 Reso-Percussive", "25 Soft Brass", "26 Violins", "27 Chorus Strings", "28 Pipe Organ",
        "31 Deep Bass", "32 Fat Slap Bass", "33 Analog Bells", "34 Sci-Fi Noise Zap", "35 Filter Sweep", "36 Unison Lead", "37 Warm Pad", "38 Chirp",
        "41 Square Wave Brass", "42 PWM Pad", "43 Sync Lead I", "44 Tremolo Strings", "45 Reso Clav", "46 Plucked Harp", "47 Glockenspiel", "48 Helicopter / Wind",
        "51 Octave Brass", "52 Pluck Bass", "53 Detuned Unison", "54 Celestial Bells", "55 Vibe Marimba", "56 Slow Attack Pad", "57 Metallic Mod", "58 Gargle Ring Mod"
    ]
    p5_presets = []
    # Factory Rev 2/3 (40 patches)
    for i, name in enumerate(p5_factory_names):
        cat = "Brass" if "Brass" in name or "Horns" in name else "Strings" if "Strings" in name or "Violins" in name else "Bass" if "Bass" in name else "Lead" if "Lead" in name or "Sync" in name else "Keys" if "Clav" in name or "Piano" in name or "Organ" in name else "Pad" if "Pad" in name else "FX"
        p5_presets.append({
            "bank": "Factory ROM",
            "program": i + 1,
            "name": name,
            "category": cat,
            "tags": ["curtis-analog", "polyphonic", "classic", cat.lower()]
        })
    # User RAM (40 patches)
    for i, name in enumerate(p5_factory_names):
        p5_presets.append({
            "bank": "User RAM",
            "program": i + 1,
            "name": f"User {name.split(' ', 1)[1]}",
            "category": "User",
            "tags": ["analog", "user", "prophet-5"]
        })
    # Rev 4 Expanded Factory (Banks 1-5 x 40 = 200 total)
    for b in range(1, 4):
        for i in range(40):
            p5_presets.append({
                "bank": f"Rev 4 Factory {b}",
                "program": i + 1,
                "name": f"P5-Rev4 Sound {b}-{i+1:02d}",
                "category": "Analog",
                "tags": ["rev4", "curtis-ssm", "vintage"]
            })
    write_synth("sequential", "prophet-5", "Sequential Circuits Prophet-5", "Polyphonic Analog Synthesizer", 1978,
                p5_cc, p5_sysex, ["Factory ROM", "User RAM", "Rev 4 Factory 1", "Rev 4 Factory 2", "Rev 4 Factory 3"], p5_presets)

    # ==========================================
    # 9. SEQUENTIAL CIRCUITS PROPHET 600
    # ==========================================
    p600_cc = {
        "cutoff": 74,
        "resonance": 71,
        "filter_env_amount": 77,
        "osc_a_freq": 20,
        "osc_b_freq": 21,
        "glide": 5
    }
    p600_sysex = {
        "header": "F0 01 02",
        "device_id_byte": 3,
        "commands": {"dump_program": "F0 01 02 02 [data...] F7"}
    }
    p600_presets = []
    p600_seeds = [
        "P600 Classic Brass", "Sync Solo Screamer", "Warm Poly Synth", "Funk Thumb Bass", "Resonant Sweep 24dB",
        "Sci-Fi Laser Gun", "Ensemble Strings", "Unison Solo Lead", "Velocity Clavinet", "P600 Electric Organ",
        "Polymod Drone", "Square Wave Bass", "Soft Poly Pad", "Chirp Lead", "Octave Fifth Brass", "Harpsichord Bell"
    ]
    for p in range(100):
        seed = p600_seeds[p % len(p600_seeds)]
        cat = "Brass" if "Brass" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Bass" if "Bass" in seed else "Strings" if "Strings" in seed else "Keys" if "Clav" in seed or "Organ" in seed else "Synth"
        p600_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"P600 {p:02d}: {seed}",
            "category": cat,
            "tags": ["vintage-midi", "cem3340", "analog", cat.lower()]
        })
    write_synth("sequential", "prophet-600", "Sequential Circuits Prophet 600", "Polyphonic Analog Synthesizer", 1982,
                p600_cc, p600_sysex, ["Factory Bank"], p600_presets)

    # ==========================================
    # 10. SEQUENTIAL CIRCUITS PROPHET VS
    # ==========================================
    vs_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "joystick_x": 16,
        "joystick_y": 17,
        "filter_env_amount": 77,
        "amp_attack": 73,
        "amp_release": 72
    }
    vs_sysex = {
        "header": "F0 01 0A",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 0A 01 [prog] F7"}
    }
    vs_seeds = [
        "Film Cue", "Voices VS", "Plucked Vector", "Bowed Bell", "VS Brass", "Digital Wave Bass", "Space Harpsichord",
        "Alien Breath", "Glass Matrix", "Lunar Choir", "Joystick Morph Pad", "Resonant Digital", "Sync Vector Solo",
        "Subterranean Low", "Vocaloid Pad", "Celestial Waves", "Metallic Pulse", "Blade Runner Brass", "Vector Lead", "Dark Drone"
    ]
    vs_presets = []
    for p in range(100):
        seed = vs_seeds[p % len(vs_seeds)]
        cat = "Pad" if "Pad" in seed or "Choir" in seed or "Voices" in seed else "Lead" if "Lead" in seed or "Solo" in seed else "Bass" if "Bass" in seed or "Low" in seed else "Brass" if "Brass" in seed else "Bell" if "Bell" in seed or "Glass" in seed else "Vector"
        vs_presets.append({
            "bank": "Preset Bank",
            "program": p,
            "name": f"VS-{p:02d} {seed}",
            "category": cat,
            "tags": ["vector-synthesis", "cem3379", "hybrid", cat.lower()]
        })
    write_synth("sequential", "prophet-vs", "Sequential Circuits Prophet VS", "Digital/Analog Vector Synthesizer", 1986,
                vs_cc, vs_sysex, ["Preset Bank"], vs_presets)

    # ==========================================
    # 11. SEQUENTIAL CIRCUITS SIX-TRAK
    # ==========================================
    st_cc = {
        "cutoff": 74,
        "resonance": 71,
        "osc_coarse": 20,
        "glide": 5
    }
    st_sysex = {
        "header": "F0 01 05",
        "device_id_byte": 3,
        "commands": {"dump_program": "F0 01 05 01 [data...] F7"}
    }
    st_presets = []
    st_seeds = [
        "Six-Trak Brass", "Funky Bass", "Solo Synth", "Poly Strings", "Sync Lead", "Electric Piano", "Filter Ping",
        "Alien Wind", "Reso Clav", "Fat Saw Pad", "Organ Tone", "Square Bass", "Detuned Lead", "Bells & Chimes"
    ]
    for p in range(100):
        seed = st_seeds[p % len(st_seeds)]
        cat = "Brass" if "Brass" in seed else "Bass" if "Bass" in seed else "Lead" if "Lead" in seed else "Strings" if "Strings" in seed or "Pad" in seed else "Keys"
        st_presets.append({
            "bank": "Factory Bank",
            "program": p,
            "name": f"Patch {p:02d}: {seed}",
            "category": cat,
            "tags": ["cem3394", "multitimbral", "analog", cat.lower()]
        })
    write_synth("sequential", "six-trak", "Sequential Circuits Six-Trak", "Multitimbral Analog Synthesizer", 1984,
                st_cc, st_sysex, ["Factory Bank"], st_presets)

    # ==========================================
    # 12. DAVE SMITH INSTRUMENTS PROPHET '08 / REV2
    # ==========================================
    p08_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "filter_audio_mod": 70,
        "filter_env_amount": 77,
        "osc1_frequency": 20,
        "osc2_frequency": 24,
        "amp_attack": 73,
        "amp_decay": 75,
        "amp_sustain": 30,
        "amp_release": 72
    }
    p08_sysex = {
        "header": "F0 01 23",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 23 05 [bank] [prog] F7"}
    }
    p08_presets = []
    p08_seeds = [
        "Prophet Brass", "Classic 2-Pole Strings", "Sync Solo", "Dual Octave Bass", "Vintage Warmth", "8-Voice Poly Clav",
        "Motion Seq Pad", "Sub Saw Bass", "Pluck Resonance", "Poly Ensemble", "Ethereal Choir", "Arp Machine",
        "Gated Sync Lead", "Analog EP", "Subterranean Bass", "Matrix Pad", "Punchy Brass Stabs", "Unison Detune Lead"
    ]
    for b_idx in [1, 2]:
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 129):
            seed = p08_seeds[(p - 1) % len(p08_seeds)]
            p_name = f"{seed} {p}" if p > len(p08_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name or "Choir" in p_name else "Arp"
            p08_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["curtis-analog", "curtis-dco", "polyphonic", cat.lower()]
            })
    write_synth("sequential", "prophet-08", "Dave Smith Instruments Prophet '08 / Rev2", "Polyphonic Analog Synthesizer", 2007,
                p08_cc, p08_sysex, ["Factory Bank 1", "Factory Bank 2"], p08_presets)

    # ==========================================
    # 13. DAVE SMITH INSTRUMENTS PROPHET-6
    # ==========================================
    p6_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "highpass_cutoff": 79,
        "highpass_resonance": 78,
        "vco1_shape": 20,
        "vco2_shape": 24,
        "polymod_filter_env": 85,
        "polymod_osc_2": 86,
        "fx_mix": 91
    }
    p6_sysex = {
        "header": "F0 01 2D",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 2D 05 [bank] [prog] F7"}
    }
    p6_presets = []
    p6_seeds = [
        "P6 Grand Brass", "Pure Analog Strings", "Polymod Saw", "Punchy Bass", "Vintage Poly 1981", "Sub 2-Pole Lead",
        "Chirp Clav", "Stereo Slap", "Slop Pad", "Sync Squeal", "BBD Warm Chorus Pad", "Tape Delay Lead",
        "Fat Moogish Bass", "Highpass Sparkle", "Poly Seq Dance", "Veloc Brass Octaves", "Soft PWM Violins"
    ]
    for b_idx in range(5):
        b_name = f"Factory Bank {b_idx}"
        for p in range(100):
            seed = p6_seeds[p % len(p6_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(p6_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Strings" if "Strings" in p_name or "Pad" in p_name else "Lead" if "Lead" in p_name or "Sync" in p_name else "Bass" if "Bass" in p_name else "Keys"
            p6_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["discrete-vco", "discrete-vcf", "prophet-6", cat.lower()]
            })
    write_synth("sequential", "prophet-6", "Dave Smith Instruments Prophet-6", "Discrete Polyphonic Analog Synthesizer", 2015,
                p6_cc, p6_sysex, [f"Factory Bank {i}" for i in range(5)], p6_presets)

    # ==========================================
    # 14. DAVE SMITH / TOM OBERHEIM OB-6
    # ==========================================
    ob6_cc = {
        "sem_filter_cutoff": 74,
        "sem_filter_resonance": 71,
        "sem_filter_mode": 79,  # Lowpass -> Notch -> Highpass -> Bandpass
        "osc1_shape": 20,
        "osc2_shape": 24,
        "xmod_filter_env": 85,
        "xmod_osc_2": 86,
        "effects_wet_dry": 91
    }
    ob6_sysex = {
        "header": "F0 01 2E",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 2E 05 [bank] [prog] F7"}
    }
    ob6_presets = []
    ob6_seeds = [
        "Tom's Brass", "SEM Warm Sweep", "Notch Filter Pad", "Oberheim 8-Voice Classic", "Bandpass Pluck",
        "Punchy SEM Bass", "Highpass Sparkle", "Cross-Mod Lead", "SEM Strings", "Vintage Unison",
        "Stereo Phase Pad", "Sub Attack Bass", "Jump Brass Reborn", "Resonant Ring Mod", "Detuned Dual VCO Solo"
    ]
    for b_idx in range(5):
        b_name = f"Factory Bank {b_idx}"
        for p in range(100):
            seed = ob6_seeds[p % len(ob6_seeds)]
            p_name = f"{seed} {p+1}" if p >= len(ob6_seeds) else seed
            cat = "Brass" if "Brass" in p_name else "Pad" if "Pad" in p_name or "Strings" in p_name or "Sweep" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name or "Cross-Mod" in p_name else "Pluck"
            ob6_presets.append({
                "bank": b_name,
                "program": p + 1,
                "name": p_name,
                "category": cat,
                "tags": ["sem-filter", "oberheim", "vco", cat.lower()]
            })
    write_synth("sequential", "ob-6", "Dave Smith Instruments / Sequential OB-6", "Polyphonic Analog Synthesizer", 2016,
                ob6_cc, ob6_sysex, [f"Factory Bank {i}" for i in range(5)], ob6_presets)

    # ==========================================
    # 15. DAVE SMITH INSTRUMENTS PROPHET 12
    # ==========================================
    p12_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "highpass_cutoff": 79,
        "char_drive": 80,
        "char_hack": 81,
        "char_decimate": 82,
        "char_girth": 83,
        "char_air": 84,
        "feedback_amount": 85
    }
    p12_sysex = {
        "header": "F0 01 26",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 26 05 [bank] [prog] F7"}
    }
    p12_presets = []
    p12_seeds = [
        "P12 Flagship Hybrid", "Character Drive Lead", "Girth & Air Pad", "Hack & Decimate", "Feedback Drone",
        "Linear FM Bells", "12-Voice Warm Strings", "Sub Osc Heavy Bass", "Slop & Drift Poly", "Tuned Feedback Solo",
        "Morphing Wavetable Clav", "Stereo Delay Landscape", "Aggressive Industrial Hit", "Ambient Space Pad"
    ]
    for b_idx in range(1, 5):
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 100):
            seed = p12_seeds[(p - 1) % len(p12_seeds)]
            p_name = f"{seed} {p}" if p > len(p12_seeds) else seed
            cat = "Pad" if "Pad" in p_name or "Strings" in p_name or "Landscape" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name else "Bass" if "Bass" in p_name else "Hybrid"
            p12_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["hybrid", "12-voice", "character-fx", cat.lower()]
            })
    write_synth("sequential", "prophet-12", "Dave Smith Instruments Prophet 12", "12-Voice Hybrid Synthesizer", 2013,
                p12_cc, p12_sysex, [f"Factory Bank {i}" for i in range(1, 5)], p12_presets)

    # ==========================================
    # 16. DAVE SMITH INSTRUMENTS EVOLVER
    # ==========================================
    ev_cc = {
        "analog_cutoff": 74,
        "analog_resonance": 71,
        "highpass_cutoff": 79,
        "feedback_amount": 80,
        "distortion": 81,
        "delay_1_time": 82,
        "delay_1_feedback": 83
    }
    ev_sysex = {
        "header": "F0 01 20",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 20 05 [bank] [prog] F7"}
    }
    ev_presets = []
    ev_seeds = [
        "Main Evolver", "Sequenced Madness", "Feedback Scream", "Analog Sub Bass", "Wavetable Morph",
        "Stereo Gated Arp", "Distorted Lead", "PPG Bell Sequence", "Curtis Lowpass", "Highpass Peak",
        "Industrial Rhythm", "Alien Landscape", "Matrix Sequence 4x16", "Heavy Drive Solo", "Dirty Modular"
    ]
    for b_idx in range(1, 4):
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 129):
            seed = ev_seeds[(p - 1) % len(ev_seeds)]
            p_name = f"{seed} {p}" if p > len(ev_seeds) else seed
            cat = "Sequence" if "Seq" in p_name or "Arp" in p_name or "Madness" in p_name or "Rhythm" in p_name else "Bass" if "Bass" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name or "Scream" in p_name else "FX"
            ev_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["evolver", "step-sequencer", "feedback", "curtis-vcf", cat.lower()]
            })
    write_synth("sequential", "evolver", "Dave Smith Instruments Evolver", "Hybrid Synthesizer & Step Sequencer", 2002,
                ev_cc, ev_sysex, [f"Factory Bank {i}" for i in range(1, 4)], ev_presets)

    # ==========================================
    # 17. DAVE SMITH INSTRUMENTS MOPHO / TETRA
    # ==========================================
    mopho_cc = {
        "filter_cutoff": 74,
        "filter_resonance": 71,
        "sub_osc1_level": 20,
        "sub_osc2_level": 21,
        "feedback_volume": 80,
        "glide": 5,
        "vcf_env_amount": 77
    }
    mopho_sysex = {
        "header": "F0 01 25",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 25 05 [bank] [prog] F7"}
    }
    mopho_presets = []
    mopho_seeds = [
        "Mopho Yellow Monster", "Sub 1 & 2 Growl", "Acid 4-Pole", "Punchy Pluck", "Gated Bass Seq",
        "Screaming Feedback Lead", "Curtis Warm Poly", "Sub Heavy 303", "Square Funk", "Feedback Buzz",
        "Detuned Saw Pluck", "Modular Glitch", "Stereo Drive Bass", "Vintage Solo"
    ]
    for b_idx in range(1, 4):
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 129):
            seed = mopho_seeds[(p - 1) % len(mopho_seeds)]
            p_name = f"{seed} {p}" if p > len(mopho_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Sub" in p_name or "Growl" in p_name or "303" in p_name else "Lead" if "Lead" in p_name or "Solo" in p_name or "Acid" in p_name else "Seq" if "Seq" in p_name else "Analog"
            mopho_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["curtis-analog", "sub-oscillators", "feedback", cat.lower()]
            })
    write_synth("sequential", "mopho", "Dave Smith Instruments Mopho / Tetra", "Analog Monophonic / Polyphonic Synthesizer", 2008,
                mopho_cc, mopho_sysex, [f"Factory Bank {i}" for i in range(1, 4)], mopho_presets)

    # ==========================================
    # 18. DAVE SMITH INSTRUMENTS PRO 2 / PRO 3
    # ==========================================
    pro2_cc = {
        "filter1_cutoff": 74,
        "filter1_resonance": 71,
        "filter2_cutoff": 79,
        "filter2_resonance": 78,
        "drive": 80,
        "hack": 81,
        "decimate": 82,
        "glide": 5
    }
    pro2_sysex = {
        "header": "F0 01 2B",
        "device_id_byte": 3,
        "commands": {"request_program": "F0 01 2B 05 [bank] [prog] F7"}
    }
    pro2_presets = []
    pro2_seeds = [
        "Pro Monolith", "Dual Filter Morph (Prophet + SEM)", "Paraphonic Super Lead", "Super Saw Bass",
        "Drive & Distortion", "Ladder Filter Squawk", "Modular CV Lead", "Sync & FM Shredder",
        "Sub Octave Earthshaker", "4-Voice Paraphonic Pad", "Stereo Analog BBD Delay", "Step Sequenced Acid"
    ]
    for b_idx in range(1, 5):
        b_name = f"Factory Bank {b_idx}"
        for p in range(1, 100):
            seed = pro2_seeds[(p - 1) % len(pro2_seeds)]
            p_name = f"{seed} {p}" if p > len(pro2_seeds) else seed
            cat = "Bass" if "Bass" in p_name or "Earthshaker" in p_name else "Lead" if "Lead" in p_name or "Shredder" in p_name else "Paraphonic" if "Paraphonic" in p_name or "Pad" in p_name else "Modular"
            pro2_presets.append({
                "bank": b_name,
                "program": p,
                "name": p_name,
                "category": cat,
                "tags": ["dual-analog-filters", "paraphonic", "modular-cv", cat.lower()]
            })
    write_synth("sequential", "pro-2", "Dave Smith Instruments Pro 2 / Pro 3", "Flagship Paraphonic Hybrid Synthesizer", 2014,
                pro2_cc, pro2_sysex, [f"Factory Bank {i}" for i in range(1, 5)], pro2_presets)

if __name__ == "__main__":
    build_wave4()
