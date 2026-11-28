#!/usr/bin/env python3
"""
OmniPatch Wave 20 Builder: Modern Flagships, Analog Powerhouses, Beat Processors & Studio Racks
Adds 30 high-profile instruments from the Midi Quest 13 catalog:
- Roland: Jupiter-X, JX-03, JV-90, P-55
- Yamaha: SPX90 II, S90, 03D
- Korg: N5, N5EX, N364
- Sequential: Tetra, Pro 3, Prophet Rev2
- Modal: Modal 001, Cobalt5S
- Roger Linn: AdrenaLinn
- Audiothingies: Doctor A
- Tasty Chips: Sawbench
- Evolution: EVS-1
- Hammond: XB-2
- JoMoX: Airbase99
- Lexicon: Reflex, LXP-5
- Dynacord: DRP 15, DLS 223
- ART: DR-1, SGE
- TC-Helicon: VoiceDoubler
- Zoom: 9010
- Fender: G-DEC
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ ROLAND ------------------
    {
        "m_dir": "roland",
        "model_dir": "jupiter-x",
        "manufacturer": "Roland",
        "model": "Jupiter-X",
        "type": "Flagship Synthesizer Workstation",
        "year": 2019,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "drive": 94, "chorus_level": 93, "delay_send": 91},
        "sysex_header": "F0 41 10 00 00 00 5D 12",
        "req_cmd": "F0 41 10 00 00 00 5D 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("ZEN-Core Model Bank", "ROM", 128, "ZEN-Core Advanced Synthesis", [
                f"Jupiter-X Model {i+1:03d}" for i in range(128)
            ]),
            ("Vintage Heritage Bank", "ROM", 128, "Jupiter-8 / Juno-106 / JX-8P / SH-101", [
                f"Heritage Synth {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "jx-03",
        "manufacturer": "Roland",
        "model": "JX-03",
        "type": "Boutique Polyphonic Synthesizer Module",
        "year": 2015,
        "cc_map": {"dco1_wave": 16, "dco2_wave": 17, "dco2_tune": 18, "cross_mod": 19, "vcf_cutoff": 74, "vcf_resonance": 71, "chorus": 93},
        "sysex_header": "F0 41 10 00 00 00 1C 12",
        "req_cmd": "F0 41 10 00 00 00 1C 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "ACB JX-3P Polyphonic Modeling", [
                f"JX-03 Tone {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "jv-90",
        "manufacturer": "Roland",
        "model": "JV-90",
        "type": "Expandable Polyphonic Synthesizer",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 5A 12",
        "req_cmd": "F0 41 10 5A 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank A", "ROM", 64, "Super JV Sound Library", [f"JV-90 Patch A{i+1:02d}" for i in range(64)]),
            ("Preset Bank B", "ROM", 64, "Super JV Sound Library", [f"JV-90 Patch B{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "p-55",
        "manufacturer": "Roland",
        "model": "P-55",
        "type": "Piano Sound Module",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "brightness": 74, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 54 12",
        "req_cmd": "F0 41 10 54 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Tones", "ROM", 64, "Acoustic Grand & Rhodes/Wurlitzer Modeling", [
                f"P-55 Piano {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "spx90-ii",
        "manufacturer": "Yamaha",
        "model": "SPX90 II",
        "type": "Digital Multi-Effects Processor",
        "year": 1986,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "balance": 91},
        "sysex_header": "F0 43 10 15",
        "req_cmd": "F0 43 10 15 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 90, "Symphonic Chorus, Pitch Change & Early Reflections", [
                f"SPX90 II Program {i+1:02d}" for i in range(90)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "s90",
        "manufacturer": "Yamaha",
        "model": "S90",
        "type": "Synthesizer Workstation Keyboard",
        "year": 2002,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 6B",
        "req_cmd": "F0 43 10 6B 00 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Motif S-Core Acoustic Pianos & Keyboards", [
                f"S90 Voice 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Motif S-Core Synthesizers & Orchestral", [
                f"S90 Voice 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "03d",
        "manufacturer": "Yamaha",
        "model": "03D",
        "type": "Compact Digital Mixing Console",
        "year": 1997,
        "cc_map": {"fader1": 1, "fader2": 2, "fader3": 3, "pan": 10, "fx1_send": 91, "master": 7},
        "sysex_header": "F0 43 10 47",
        "req_cmd": "F0 43 10 47 00 00 00 00 F7",
        "banks": [
            ("Scene Memory", "ROM", 50, "Digital Automated Mix Scenes & Dual Effects", [
                f"03D Scene {i+1:02d}" for i in range(50)
            ])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "n5",
        "manufacturer": "Korg",
        "model": "N5",
        "type": "64-Voice AI2 Music Workstation",
        "year": 1998,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 4D",
        "req_cmd": "F0 42 30 4D 10 F7",
        "banks": [
            ("Bank A", "ROM", 100, "AI2 Stereo Dynamic Sounds", [f"N5 Prog A{i+1:02d}" for i in range(100)]),
            ("Bank B", "ROM", 100, "AI2 Synthesizers & GM", [f"N5 Prog B{i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "n5ex",
        "manufacturer": "Korg",
        "model": "N5EX",
        "type": "Expanded AI2 Music Workstation",
        "year": 1999,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 52",
        "req_cmd": "F0 42 30 52 10 F7",
        "banks": [
            ("Bank A", "ROM", 100, "Expanded 18MB PCM Sound Library", [f"N5EX Prog A{i+1:02d}" for i in range(100)]),
            ("Bank B", "ROM", 100, "Synth Leads & Concert Pianos", [f"N5EX Prog B{i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "n364",
        "manufacturer": "Korg",
        "model": "N364",
        "type": "Music Workstation with RPPR",
        "year": 1996,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 46",
        "req_cmd": "F0 42 30 46 10 F7",
        "banks": [
            ("Bank A", "ROM", 100, "AI2 Programs & RPPR Patterns", [f"N364 Prog A{i+1:02d}" for i in range(100)]),
            ("Bank B", "ROM", 100, "Orchestral, Pads & Basses", [f"N364 Prog B{i+1:02d}" for i in range(100)])
        ]
    },

    # ------------------ SEQUENTIAL ------------------
    {
        "m_dir": "sequential",
        "model_dir": "tetra",
        "manufacturer": "Sequential",
        "model": "Tetra",
        "type": "4-Voice Discrete Analog Synthesizer",
        "year": 2009,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_freq": 16, "osc2_freq": 17, "sub_osc1": 18, "sub_osc2": 19, "feedback": 20},
        "sysex_header": "F0 01 26",
        "req_cmd": "F0 01 26 06 00 00 F7",
        "banks": [
            ("Factory Bank 1", "ROM", 128, "Curtis Discrete 4-Voice Polyphonic", [
                f"Tetra Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "sequential",
        "model_dir": "pro-3",
        "manufacturer": "Sequential",
        "model": "Pro 3",
        "type": "Multi-Filter Mono/Paraphonic Synthesizer",
        "year": 2020,
        "cc_map": {"filter_type": 16, "filter_cutoff": 74, "resonance": 71, "filter_drive": 17, "osc3_wavetable": 18, "fx1_mix": 91},
        "sysex_header": "F0 01 32",
        "req_cmd": "F0 01 32 06 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "Prophet/Ladder/OB-6 Filters & Wavetable", [
                f"Pro 3 Program {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "sequential",
        "model_dir": "prophet-rev2",
        "manufacturer": "Sequential",
        "model": "Prophet Rev2",
        "type": "16-Voice Analog Polyphonic Synthesizer",
        "year": 2017,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_shape_mod": 16, "osc2_shape_mod": 17, "sub_octave": 18, "dco_slop": 19, "fx_mix": 91},
        "sysex_header": "F0 01 2F",
        "req_cmd": "F0 01 2F 06 00 00 F7",
        "banks": [
            ("Factory Bank 1", "ROM", 128, "16-Voice Curtis Analog DCO Polyphonic", [
                f"Rev2 Voice 1-{i+1:03d}" for i in range(128)
            ]),
            ("Factory Bank 2", "ROM", 128, "Layered & Split Polyphonic Sounds", [
                f"Rev2 Voice 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ MODAL ------------------
    {
        "m_dir": "modal",
        "model_dir": "001",
        "manufacturer": "Modal",
        "model": "Modal 001",
        "type": "2-Voice Analog/Digital Hybrid Synthesizer",
        "year": 2015,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "nco_wave": 16, "transistor_drive": 17, "sub_level": 18, "envelope_decay": 72},
        "sysex_header": "F0 00 20 7D 01",
        "req_cmd": "F0 00 20 7D 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "High-Res NCO Oscillators & Transistor Ladder VCF", [
                f"Modal 001 Patch {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "modal",
        "model_dir": "cobalt5s",
        "manufacturer": "Modal",
        "model": "Cobalt5S",
        "type": "5-Voice Extended Virtual Analog Synthesizer",
        "year": 2022,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_algorithm": 16, "osc2_algorithm": 17, "morph": 18, "delay_send": 91},
        "sysex_header": "F0 00 20 7D 06",
        "req_cmd": "F0 00 20 7D 06 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "40 Extended Virtual Analog Algorithms", [
                f"Cobalt5S Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ ROGER LINN ------------------
    {
        "m_dir": "roger_linn",
        "model_dir": "adrenalinn",
        "manufacturer": "Roger Linn Design",
        "model": "AdrenaLinn",
        "type": "Filter Modulation & Beat-Synced Multi-Effects",
        "year": 2001,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "tempo": 16, "mod_rate": 17, "drum_level": 18, "fx_mix": 91},
        "sysex_header": "F0 00 01 3E 01",
        "req_cmd": "F0 00 01 3E 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Beat-Synced Filter Sequences, Flanging & Drums", [
                f"AdrenaLinn Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ AUDIOTHINGIES ------------------
    {
        "m_dir": "audiothingies",
        "model_dir": "doctor-a",
        "manufacturer": "Audiothingies",
        "model": "Doctor A",
        "type": "Desktop Multi-FX Delay & Reverb",
        "year": 2019,
        "cc_map": {"delay_time": 16, "delay_feedback": 17, "reverb_decay": 18, "reverb_color": 19, "dry_wet": 91},
        "sysex_header": "F0 00 21 3F 01",
        "req_cmd": "F0 00 21 3F 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "Analog-Voiced Delay & Resonant Hall Reverb", [
                f"Doctor A Preset {i+1:02d}" for i in range(16)
            ])
        ]
    },

    # ------------------ TASTY CHIPS ------------------
    {
        "m_dir": "tasty_chips",
        "model_dir": "sawbench",
        "manufacturer": "Tasty Chips Electronics",
        "model": "Sawbench",
        "type": "Miniature Analog Synthesizer",
        "year": 2014,
        "cc_map": {"cutoff": 74, "resonance": 71, "mod_speed": 16, "mod_depth": 17, "decay": 72},
        "sysex_header": "F0 00 21 40 01",
        "req_cmd": "F0 00 21 40 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "4-Pole 24dB Analog Low-Pass Filter & VCA", [
                f"Sawbench Sound {i+1:02d}" for i in range(16)
            ])
        ]
    },

    # ------------------ EVOLUTION ------------------
    {
        "m_dir": "evolution",
        "model_dir": "evs-1",
        "manufacturer": "Evolution",
        "model": "EVS-1",
        "type": "16-Bit Multi-Algorithm Digital Synthesizer",
        "year": 1990,
        "cc_map": {"volume": 7, "pan": 10, "algorithm": 16, "timbre": 74, "detune": 17},
        "sysex_header": "F0 00 20 0B 01",
        "req_cmd": "F0 00 20 0B 01 00 F7",
        "banks": [
            ("Factory Programs", "ROM", 100, "FM, Additive, Ring Mod & Phase Distortion", [
                f"EVS-1 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ HAMMOND ------------------
    {
        "m_dir": "hammond",
        "model_dir": "xb-2",
        "manufacturer": "Hammond",
        "model": "XB-2",
        "type": "Digital Drawbar Organ Keyboard",
        "year": 1991,
        "cc_map": {"drawbar_16": 16, "drawbar_8": 17, "drawbar_4": 18, "vibrato": 19, "overdrive": 20, "leslie_speed": 68},
        "sysex_header": "F0 55 00 10",
        "req_cmd": "F0 55 00 10 01 00 F7",
        "banks": [
            ("Preset Combinations", "ROM", 32, "Direct Access Digital ToneWheel Organ", [
                f"XB-2 Combination {i+1:02d}" for i in range(32)
            ])
        ]
    },

    # ------------------ JOMOX ------------------
    {
        "m_dir": "jomox",
        "model_dir": "airbase99",
        "manufacturer": "JoMoX",
        "model": "Airbase99",
        "type": "Analog Drum Synthesizer Module",
        "year": 1999,
        "cc_map": {"bd_tune": 16, "bd_pitch": 17, "bd_decay": 18, "snare_tune": 19, "snare_snap": 20, "hihat_decay": 21},
        "sysex_header": "F0 37 01 00",
        "req_cmd": "F0 37 01 00 00 F7",
        "banks": [
            ("Preset Kits", "ROM", 100, "Discrete Analog 909-Style Drum Synthesis", [
                f"Airbase99 Kit {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ LEXICON ------------------
    {
        "m_dir": "lexicon",
        "model_dir": "reflex",
        "manufacturer": "Lexicon",
        "model": "Reflex",
        "type": "Dynamic MIDI Reverberator",
        "year": 1995,
        "cc_map": {"decay_time": 16, "pre_delay": 17, "fx_depth": 18, "mix": 91},
        "sysex_header": "F0 06 05",
        "req_cmd": "F0 06 05 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Rich Plate, Concert Hall & Dynamic Echoes", [
                f"Reflex Preset {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "lexicon",
        "model_dir": "lxp-5",
        "manufacturer": "Lexicon",
        "model": "LXP-5",
        "type": "Multi-Effects Processor",
        "year": 1989,
        "cc_map": {"pitch_shift": 16, "delay_time": 17, "chorus_rate": 18, "reverb_time": 19, "mix": 91},
        "sysex_header": "F0 06 03",
        "req_cmd": "F0 06 03 01 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 64, "MicroPitch Shifter, Delay & Room Reverb", [
                f"LXP-5 Program {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ DYNACORD ------------------
    {
        "m_dir": "dynacord",
        "model_dir": "drp-15",
        "manufacturer": "Dynacord",
        "model": "DRP 15",
        "type": "High-End Studio Reverb & Effects Processor",
        "year": 1993,
        "cc_map": {"rev_time": 16, "pre_delay": 17, "high_damp": 18, "diffusion": 19, "mix": 91},
        "sysex_header": "F0 00 00 2B 03",
        "req_cmd": "F0 00 00 2B 03 01 00 F7",
        "banks": [
            ("Studio Presets", "ROM", 128, "High-Density Studio Reverberation", [
                f"DRP 15 Program {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "dynacord",
        "model_dir": "dls-223",
        "manufacturer": "Dynacord",
        "model": "DLS 223",
        "type": "Digital Rotary Simulation & Chorus",
        "year": 1988,
        "cc_map": {"rotor_speed": 16, "bass_rotor": 17, "acceleration": 18, "mix": 91},
        "sysex_header": "F0 00 00 2B 02",
        "req_cmd": "F0 00 00 2B 02 01 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 32, "Analog/Digital True Rotary Speaker Simulator", [
                f"DLS 223 Program {i+1:02d}" for i in range(32)
            ])
        ]
    },

    # ------------------ ART ------------------
    {
        "m_dir": "art",
        "model_dir": "dr-1",
        "manufacturer": "Art",
        "model": "DR-1",
        "type": "Digital Reverb Processor",
        "year": 1985,
        "cc_map": {"decay": 16, "pre_delay": 17, "hf_damp": 18, "pos_mix": 91},
        "sysex_header": "F0 1A 01",
        "req_cmd": "F0 1A 01 00 F7",
        "banks": [
            ("Factory Reverbs", "ROM", 100, "16-Bit Studio Digital Reverberation", [
                f"DR-1 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "art",
        "model_dir": "sge",
        "manufacturer": "Art",
        "model": "SGE",
        "type": "Studio Guitar Effects Processor",
        "year": 1989,
        "cc_map": {"harmonic_overdrive": 16, "delay_time": 17, "reverb_decay": 18, "chorus_depth": 19, "mix": 91},
        "sysex_header": "F0 1A 03",
        "req_cmd": "F0 1A 03 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Multi-Effects Guitar Preamp Chain", [
                f"SGE Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ TC-HELICON ------------------
    {
        "m_dir": "tc_helicon",
        "model_dir": "voicedoubler",
        "manufacturer": "Tc Helicon",
        "model": "VoiceDoubler",
        "type": "Real-Time Vocal Doubling & Harmony",
        "year": 2008,
        "cc_map": {"voice_level": 16, "pitch_mod": 17, "timing_mod": 18, "emulation": 19, "mix": 91},
        "sysex_header": "F0 00 20 1F 14",
        "req_cmd": "F0 00 20 1F 14 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 50, "Studio Multi-Voice Doubling & Emulation", [
                f"VoiceDoubler Preset {i+1:02d}" for i in range(50)
            ])
        ]
    },

    # ------------------ ZOOM ------------------
    {
        "m_dir": "zoom",
        "model_dir": "9010",
        "manufacturer": "Zoom",
        "model": "9010",
        "type": "Studio 4-In/4-Out Multi-Effects Processor",
        "year": 1990,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "mix": 91},
        "sysex_header": "F0 52 00 08",
        "req_cmd": "F0 52 00 08 01 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 100, "Quad Discrete DSP Reverb & Delays", [
                f"Zoom 9010 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ FENDER ------------------
    {
        "m_dir": "fender",
        "model_dir": "g-dec",
        "manufacturer": "Fender",
        "model": "G-DEC",
        "type": "Guitar Digital Entertainment Center",
        "year": 2005,
        "cc_map": {"amp_gain": 16, "bass": 17, "mid": 18, "treble": 19, "fx_level": 91},
        "sysex_header": "F0 00 01 38 01",
        "req_cmd": "F0 00 01 38 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 50, "Digital Amp Modeling & Accompaniment", [
                f"G-DEC Preset {i+1:02d}" for i in range(50)
            ])
        ]
    }
]

def make_sysex(hdr: str, p_idx: int) -> str:
    parts = hdr.strip().split()
    parts.append(f"{p_idx:02X}")
    parts.append("F7")
    return " ".join(parts)

def build_all():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "devices"))
    print(f"Building Wave 20: Modern Flagships, Analog Powerhouses & Studio Racks ({len(DEVICES)} Instruments)...")

    for dev in DEVICES:
        dev_dir = os.path.join(base_dir, dev["m_dir"], dev["model_dir"])
        os.makedirs(dev_dir, exist_ok=True)

        profile = {
            "manufacturer": dev["manufacturer"],
            "model": dev["model"],
            "type": dev["type"],
            "year": dev["year"],
            "midi": {
                "channels": 16,
                "cc_map": dev["cc_map"]
            },
            "sysex": {
                "header": dev["sysex_header"],
                "device_id_byte": 2,
                "commands": {
                    "request_preset": dev["req_cmd"]
                }
            },
            "banks": []
        }

        presets_list = []
        for b_name, b_type, b_size, cat, names in dev["banks"]:
            profile["banks"].append({
                "name": b_name,
                "type": b_type,
                "size": b_size
            })

            for idx, p_name in enumerate(names):
                presets_list.append({
                    "number": idx + 1,
                    "name": p_name,
                    "bank": b_name,
                    "category": cat,
                    "tags": [dev["type"].split()[0].lower(), cat.lower(), dev["model"].lower().replace("-", "")],
                    "sysex_dump": make_sysex(dev["sysex_header"], idx)
                })

        with open(os.path.join(dev_dir, "profile.yaml"), "w") as f:
            yaml.dump(profile, f, sort_keys=False, default_flow_style=False)

        with open(os.path.join(dev_dir, "factory_presets.json"), "w") as f:
            json.dump(presets_list, f, indent=2)

        print(f"Created {dev['m_dir']}/{dev['model_dir']}: {dev['model']} ({len(presets_list)} presets)")

    print(f"\nWave 20 Build Complete! {len(DEVICES)} new flagships, analog synths & studio racks created.")

if __name__ == "__main__":
    build_all()
