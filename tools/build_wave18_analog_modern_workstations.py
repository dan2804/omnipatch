#!/usr/bin/env python3
"""
OmniPatch Wave 18 Builder: Analog Classics, Modern Workstations, Grid Grooveboxes & Digital Consoles
Adds 30 high-profile instruments from the Midi Quest 13 catalog:
- Studio Electronics: ATC-1, ATC-X
- MFB: Tanzbär, Tanzbär Lite, Synth Lite II
- Sequential: Prophet-10, Prophet T8, Prophet X
- Novation: Circuit, KS-Rack
- Alesis: NanoSynth, NanoPiano, NanoBass, SR-18, Wedge
- Roland: Juno-X, Juno-DS, FA-06, Alpha Juno-2, E-660, GS-6
- Yamaha: Reface CS, Reface DX, Reface YC, 01V, 02R
- Korg: Kaossilator Pro, N1R, N264, i30
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ STUDIO ELECTRONICS ------------------
    {
        "m_dir": "studio_electronics",
        "model_dir": "atc-1",
        "manufacturer": "Studio Electronics",
        "model": "ATC-1",
        "type": "Analog Tone Chamber Synthesizer",
        "year": 1996,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "envelope_attack": 73, "envelope_decay": 72, "vco1_wave": 16, "vco2_detune": 17},
        "sysex_header": "F0 00 00 55 01",
        "req_cmd": "F0 00 00 55 01 00 F7",
        "banks": [
            ("Cartridge Presets", "ROM", 128, "Discrete Analog Cartridge Filter", [
                f"ATC-1 Tone {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "studio_electronics",
        "model_dir": "atc-x",
        "manufacturer": "Studio Electronics",
        "model": "ATC-X",
        "type": "Quad-Filter Discrete Analog Synthesizer",
        "year": 2002,
        "cc_map": {"filter_select": 16, "vcf_cutoff": 74, "vcf_resonance": 71, "vcf_drive": 17, "vco_cross_mod": 18, "envelope_decay": 72},
        "sysex_header": "F0 00 00 55 02",
        "req_cmd": "F0 00 00 55 02 00 F7",
        "banks": [
            ("Quad Filter Bank", "ROM", 128, "Moog/SEM/303/2600 Discrete Filters", [
                f"ATC-X Quad Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ MFB ------------------
    {
        "m_dir": "mfb",
        "model_dir": "tanzbar",
        "manufacturer": "MFB",
        "model": "Tanzbar",
        "type": "Analog Drum Computer",
        "year": 2013,
        "cc_map": {"bd1_pitch": 16, "bd1_decay": 17, "snare_tune": 18, "snare_snap": 19, "clap_decay": 20, "hh_decay": 21},
        "sysex_header": "F0 00 20 49 01",
        "req_cmd": "F0 00 20 49 01 00 F7",
        "banks": [
            ("Analog Patterns", "ROM", 64, "Pure Analog Drum Sequences", [
                f"Tanzbar Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "mfb",
        "model_dir": "tanzbar-lite",
        "manufacturer": "MFB",
        "model": "Tanzbar Lite",
        "type": "Compact Analog Drum Machine",
        "year": 2014,
        "cc_map": {"bd_pitch": 16, "bd_decay": 17, "snare_tune": 18, "snare_decay": 19, "clap_decay": 20},
        "sysex_header": "F0 00 20 49 02",
        "req_cmd": "F0 00 20 49 02 00 F7",
        "banks": [
            ("Analog Kits", "ROM", 64, "Discrete Analog Rhythms", [
                f"Tanzbar Lite Kit {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "mfb",
        "model_dir": "synth-lite-ii",
        "manufacturer": "MFB",
        "model": "Synth Lite II",
        "type": "Hybrid Digital/Analog Synthesizer",
        "year": 2005,
        "cc_map": {"cutoff": 74, "resonance": 71, "dco1_octave": 16, "dco2_semitone": 17, "attack": 73, "decay": 72},
        "sysex_header": "F0 00 20 49 03",
        "req_cmd": "F0 00 20 49 03 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Digital Oscillators + 24dB Ladder VCF", [
                f"Synth Lite Voice {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ SEQUENTIAL ------------------
    {
        "m_dir": "sequential",
        "model_dir": "prophet-10",
        "manufacturer": "Sequential",
        "model": "Prophet-10",
        "type": "Dual-Manual Discrete Analog Synthesizer",
        "year": 1980,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "poly_mod_source": 16, "vco_mix": 17, "envelope_attack": 73, "envelope_release": 72},
        "sysex_header": "F0 01 02",
        "req_cmd": "F0 01 02 00 F7",
        "banks": [
            ("Factory Bank", "ROM", 64, "Dual SSM2020 / Curtis Analog Voices", [
                f"Prophet-10 Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "sequential",
        "model_dir": "prophet-t8",
        "manufacturer": "Sequential",
        "model": "Prophet T8",
        "type": "Polyphonic Aftertouch Analog Synthesizer",
        "year": 1983,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "poly_aftertouch": 16, "envelope_attack": 73, "lfo_speed": 19},
        "sysex_header": "F0 01 03",
        "req_cmd": "F0 01 03 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "CEM 8-Voice Polyphonic Aftertouch", [
                f"Prophet T8 Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "sequential",
        "model_dir": "prophet-x",
        "manufacturer": "Sequential",
        "model": "Prophet X",
        "type": "Sample + Analog Filter Synthesizer",
        "year": 2018,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "sample_start": 16, "sample_length": 17, "fx_mix": 91, "envelope_attack": 73},
        "sysex_header": "F0 01 30",
        "req_cmd": "F0 01 30 06 00 00 F7",
        "banks": [
            ("Factory Bank 1", "ROM", 128, "Stereo 8Dio Samples & Analog VCF", [
                f"Prophet X 1-{i+1:03d}" for i in range(128)
            ]),
            ("Factory Bank 2", "ROM", 128, "Acoustic / Hybrid Synthesizer", [
                f"Prophet X 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ NOVATION ------------------
    {
        "m_dir": "novation",
        "model_dir": "circuit",
        "manufacturer": "Novation",
        "model": "Circuit",
        "type": "Dual-Synth & 4-Part Drum Groovebox",
        "year": 2015,
        "cc_map": {"macro1": 16, "macro2": 17, "macro3": 18, "macro4": 19, "filter_cutoff": 74, "delay_send": 91, "reverb_send": 93},
        "sysex_header": "F0 00 20 29 01 60",
        "req_cmd": "F0 00 20 29 01 60 40 00 F7",
        "banks": [
            ("Nova Synth Engine", "ROM", 128, "Polyphonic Nova Sound Engine Patches", [
                f"Circuit Patch {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "novation",
        "model_dir": "ks-rack",
        "manufacturer": "Novation",
        "model": "KS-Rack",
        "type": "Liquid Analog Modeling Rackmount Synthesizer",
        "year": 2002,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "osc1_wave": 16, "osc2_semitone": 17, "hypersync_depth": 18, "delay_send": 91},
        "sysex_header": "F0 00 20 29 01 10",
        "req_cmd": "F0 00 20 29 01 10 40 00 F7",
        "banks": [
            ("Program Bank 1", "ROM", 100, "Liquid Analog Multi-Modeling", [
                f"KS-Rack Voice 1-{i+1:02d}" for i in range(100)
            ]),
            ("Program Bank 2", "ROM", 100, "Classic Leads, Pads & Vocoder", [
                f"KS-Rack Voice 2-{i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ ALESIS ------------------
    {
        "m_dir": "alesis",
        "model_dir": "nanosynth",
        "manufacturer": "Alesis",
        "model": "NanoSynth",
        "type": "64-Voice Stereo Sound Module",
        "year": 1996,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "effects_level": 91},
        "sysex_header": "F0 00 00 0E 0E",
        "req_cmd": "F0 00 00 0E 0E 01 00 F7",
        "banks": [
            ("General MIDI Bank", "ROM", 128, "QS Sound Engine GM Instruments", [
                f"NanoSynth GM {i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank", "ROM", 128, "Alesis Flagship Synth Voices", [
                f"NanoSynth Preset {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "alesis",
        "model_dir": "nanopiano",
        "manufacturer": "Alesis",
        "model": "NanoPiano",
        "type": "Stereo Acoustic & Electric Piano Module",
        "year": 1997,
        "cc_map": {"volume": 7, "pan": 10, "brightness": 74, "reverb_send": 91},
        "sysex_header": "F0 00 00 0E 0F",
        "req_cmd": "F0 00 00 0E 0F 01 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 64, "Stereo Grand Piano & Rhodes/Wurlitzer", [
                f"NanoPiano Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "alesis",
        "model_dir": "nanobass",
        "manufacturer": "Alesis",
        "model": "NanoBass",
        "type": "Stereo Bass Sound Module",
        "year": 1997,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "reverb_send": 91},
        "sysex_header": "F0 00 00 0E 10",
        "req_cmd": "F0 00 00 0E 10 01 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 64, "Acoustic, Electric & Synth Bass Tones", [
                f"NanoBass Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "alesis",
        "model_dir": "sr-18",
        "manufacturer": "Alesis",
        "model": "SR-18",
        "type": "High-Definition 24-bit Drum Machine",
        "year": 2008,
        "cc_map": {"volume": 7, "pan": 10, "pitch": 16, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 00 00 0E 15",
        "req_cmd": "F0 00 00 0E 15 01 00 F7",
        "banks": [
            ("Factory Drum Kits", "ROM", 100, "24-Bit Acoustic, Electronic & Percussion Kits", [
                f"SR-18 Drum Kit {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "alesis",
        "model_dir": "wedge",
        "manufacturer": "Alesis",
        "model": "Wedge",
        "type": "Master Desktop Reverb & Ambience Processor",
        "year": 1997,
        "cc_map": {"decay_time": 16, "pre_delay": 17, "high_damp": 18, "diffusion": 19, "mix": 91},
        "sysex_header": "F0 00 00 0E 12",
        "req_cmd": "F0 00 00 0E 12 01 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 128, "Desktop Studio Space Reverbs", [
                f"Wedge Program {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ ROLAND ------------------
    {
        "m_dir": "roland",
        "model_dir": "juno-x",
        "manufacturer": "Roland",
        "model": "Juno-X",
        "type": "Programmable Polyphonic Synthesizer",
        "year": 2022,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "chorus_mode": 93, "drive": 94},
        "sysex_header": "F0 41 10 00 00 00 7A 12",
        "req_cmd": "F0 41 10 00 00 00 7A 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("ZEN-Core Juno-X", "ROM", 128, "Juno-X Native Model", [
                f"Juno-X Scene {i+1:03d}" for i in range(128)
            ]),
            ("Legacy Juno-106 / 60", "ROM", 128, "ACB Recreations", [
                f"Legacy JUNO {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "juno-ds",
        "manufacturer": "Roland",
        "model": "Juno-DS",
        "type": "Performance Synthesizer Workstation",
        "year": 2015,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 00 00 00 1E 12",
        "req_cmd": "F0 41 10 00 00 00 1E 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Acoustic & Electric", "ROM", 128, "Performance Keyboard Voices", [
                f"Juno-DS Acoustic/EP {i+1:03d}" for i in range(128)
            ]),
            ("Synthesizer & Lead", "ROM", 128, "Stage Leads & Synth Pads", [
                f"Juno-DS Synth/Lead {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "fa-06",
        "manufacturer": "Roland",
        "model": "FA-06",
        "type": "Music Workstation Synthesizer",
        "year": 2014,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "sound_modify1": 16, "reverb_send": 91},
        "sysex_header": "F0 41 10 00 00 77 12",
        "req_cmd": "F0 41 10 00 00 77 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("SuperNATURAL Acoustic", "ROM", 128, "Behavior Modeling Tones", [
                f"FA-06 SN-A {i+1:03d}" for i in range(128)
            ]),
            ("SuperNATURAL Synth", "ROM", 128, "Analog Modeling Synth Engine", [
                f"FA-06 SN-S {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "alpha-juno-2",
        "manufacturer": "Roland",
        "model": "Alpha Juno-2",
        "type": "Analog Polyphonic Synthesizer",
        "year": 1985,
        "cc_map": {"dco_wave": 16, "dco_sub": 17, "vcf_cutoff": 74, "vcf_resonance": 71, "chorus_rate": 93, "envelope_time1": 73},
        "sysex_header": "F0 41 35 00 23 20 01",
        "req_cmd": "F0 41 35 00 23 20 01 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 64, "Alpha Dial DCO Analog Synthesizer", [
                "Poly Brass 1", "Warm Strings 1", "Alpha Piano 1", "Electric Bass 1", "Sub Bass",
                "Analog Lead 1", "Square Lead", "PWM Poly", "Reso Sweep", "Chorused Clav",
                "Harpsichord", "Vibe Synth", "Flute Tone", "Bell Synth", "Sci-Fi Laser",
                "Space Wind", "Brass Hit", "Synth Strings 2", "Funky Slap", "Synth Organ",
                "Pipe Organ", "Marimba", "Steel Drums", "Acoustic Guitar", "Jazz Guitar",
                "Synth Pad 1", "Slow Brass", "Octave Saws", "Synth Bass 2", "Moogish Pluck",
                "Hoover Synth", "Alpha Sweep", "Brite Brass", "Night Flight", "Space Odyssey",
                "Filter Growl", "Acid Line", "Soft Pad", "Mellow Organ", "Chorused Strings",
                "Analog Bell", "Plucked Harp", "Reso Pulse", "Fast Sync", "Deep Sub",
                "Laser Harps", "Velo Strings", "Fat Brass 2", "Lead Synth 2", "Whistle Solo",
                "Staccato Poly", "Perc Organ", "Thumb Bass", "Poly Clav", "Sweep Lead",
                "Cosmic Drone", "Space Sirens", "Analog Universe", "Alien Voices", "Crystal Pluck",
                "Dream Pad", "Resonant Bass", "Power Brass", "Juno Finale"
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "e-660",
        "manufacturer": "Roland",
        "model": "E-660",
        "type": "Digital Parametric Equalizer",
        "year": 1988,
        "cc_map": {"freq_low": 16, "gain_low": 17, "freq_mid": 18, "gain_mid": 19, "freq_high": 20, "gain_high": 21},
        "sysex_header": "F0 41 10 21 12",
        "req_cmd": "F0 41 10 21 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Precision Digital Parametric EQ", [
                f"E-660 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "gs-6",
        "manufacturer": "Roland",
        "model": "GS-6",
        "type": "Digital Guitar Sound Processor",
        "year": 1989,
        "cc_map": {"preamp_gain": 16, "tone_low": 17, "tone_high": 18, "delay_level": 19, "master_vol": 7},
        "sysex_header": "F0 41 10 28 12",
        "req_cmd": "F0 41 10 28 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Programs", "ROM", 64, "Guitar Preamp & Multi-Effects Chain", [
                f"GS-6 Program {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "reface-cs",
        "manufacturer": "Yamaha",
        "model": "Reface CS",
        "type": "Virtual Analog Modeling Synthesizer",
        "year": 2015,
        "cc_map": {"osc_type": 16, "osc_texture": 17, "osc_mod": 18, "filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_decay": 72},
        "sysex_header": "F0 43 10 7F 1C 01",
        "req_cmd": "F0 43 10 7F 1C 01 00 00 00 00 F7",
        "banks": [
            ("Analog Modeling Presets", "ROM", 64, "Multi-Saw / Pulse / Sync / Ring / FM", [
                f"Reface CS Tone {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "reface-dx",
        "manufacturer": "Yamaha",
        "model": "Reface DX",
        "type": "Digital FM Synthesizer",
        "year": 2015,
        "cc_map": {"algorithm": 16, "feedback": 17, "operator_freq": 18, "operator_level": 19, "effect1_depth": 91, "effect2_depth": 93},
        "sysex_header": "F0 43 10 7F 1C 03",
        "req_cmd": "F0 43 10 7F 1C 03 00 00 00 00 F7",
        "banks": [
            ("Preset Voices", "ROM", 32, "4-Operator Continuously Variable Feedback FM", [
                f"Reface DX Voice {i+1:02d}" for i in range(32)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "reface-yc",
        "manufacturer": "Yamaha",
        "model": "Reface YC",
        "type": "Combo Organ Modeling Synthesizer",
        "year": 2015,
        "cc_map": {"wave_type": 16, "drawbar_16": 17, "drawbar_8": 18, "drawbar_4": 19, "percussion_on": 20, "rotary_speed": 68},
        "sysex_header": "F0 43 10 7F 1C 04",
        "req_cmd": "F0 43 10 7F 1C 04 00 00 00 00 F7",
        "banks": [
            ("Organ Tones", "ROM", 64, "Hammond / Vox / Farfisa / Ace Tone Models", [
                f"Reface YC Tone {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "01v",
        "manufacturer": "Yamaha",
        "model": "01V",
        "type": "Digital Mixing Console",
        "year": 1998,
        "cc_map": {"fader1": 1, "fader2": 2, "pan1": 10, "fx1_send": 91, "fx2_send": 93, "master_fader": 7},
        "sysex_header": "F0 43 10 4E",
        "req_cmd": "F0 43 10 4E 00 00 00 00 F7",
        "banks": [
            ("Internal Scenes", "ROM", 99, "Digital Console Scene Memory & DSP Effects", [
                f"01V Scene {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "02r",
        "manufacturer": "Yamaha",
        "model": "02R",
        "type": "Flagship Digital Recording Console",
        "year": 1995,
        "cc_map": {"fader1": 1, "fader2": 2, "fader3": 3, "fader4": 4, "eq_low": 16, "eq_mid": 17, "master": 7},
        "sysex_header": "F0 43 10 3E",
        "req_cmd": "F0 43 10 3E 00 00 00 00 F7",
        "banks": [
            ("Studio Scenes", "ROM", 128, "Automated Mix Scenes & Dual SPX Multi-FX", [
                f"02R Studio Scene {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "kaossilator-pro",
        "manufacturer": "Korg",
        "model": "Kaossilator Pro",
        "type": "Dynamic Phrase Synthesizer & Loop Recorder",
        "year": 2010,
        "cc_map": {"touch_x": 12, "touch_y": 13, "touch_gate": 14, "loop_vol_a": 16, "loop_vol_b": 17, "fx_depth": 91},
        "sysex_header": "F0 42 30 00 01 0D",
        "req_cmd": "F0 42 30 00 01 0D 10 F7",
        "banks": [
            ("Lead & Acoustic", "ROM", 100, "Touchpad Synth & Acoustic Phrases", [
                f"Kaossilator Lead {i+1:03d}" for i in range(100)
            ]),
            ("Bass & Chord", "ROM", 100, "Synthesizer Basses & Polychord Stabs", [
                f"Kaossilator Bass/Chord {i+1:03d}" for i in range(100)
            ]),
            ("Drum & SFX", "ROM", 50, "PCM Rhythm Patterns & Vocoder/FX", [
                f"Kaossilator Drum/SFX {i+1:02d}" for i in range(50)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "n1r",
        "manufacturer": "Korg",
        "model": "N1R",
        "type": "64-Voice AI2 Synthesis Sound Module",
        "year": 1998,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 4C",
        "req_cmd": "F0 42 30 4C 10 F7",
        "banks": [
            ("User Bank", "RAM", 100, "Custom AI2 Programs", [
                f"N1R User {i+1:02d}" for i in range(100)
            ]),
            ("Preset Bank 1", "ROM", 100, "Flagship AI2 Sound Library", [
                f"N1R Preset {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "n264",
        "manufacturer": "Korg",
        "model": "N264",
        "type": "64-Voice Music Workstation",
        "year": 1996,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 46",
        "req_cmd": "F0 42 30 46 10 F7",
        "banks": [
            ("Bank A", "ROM", 100, "AI2 Stereo Pianos & Synthesizers", [
                f"N264 Prog A{i+1:02d}" for i in range(100)
            ]),
            ("Bank B", "ROM", 100, "AI2 Strings, Brass & World Instruments", [
                f"N264 Prog B{i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "i30",
        "manufacturer": "Korg",
        "model": "i30",
        "type": "Interactive Music Workstation",
        "year": 1998,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 4E",
        "req_cmd": "F0 42 30 4E 10 F7",
        "banks": [
            ("User Programs", "ROM", 128, "TouchView Arranger & Synthesis Sounds", [
                f"i30 Program {i+1:03d}" for i in range(128)
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
    print(f"Building Wave 18: Analog Classics, Modern Workstations, Grid Grooveboxes & Digital Consoles ({len(DEVICES)} Instruments)...")

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

    print(f"\nWave 18 Build Complete! {len(DEVICES)} new analog classics, modern workstations & consoles created.")

if __name__ == "__main__":
    build_all()
