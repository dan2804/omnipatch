#!/usr/bin/env python3
"""
OmniPatch Wave 21 Builder: Flagships, Advanced FM Vectors, Samplers & Volcas
Adds 30 high-profile instruments from the Midi Quest 13 catalog:
- Roland: V-Synth GT, SH-32, SH-01A, TR-08, TR-09, TR-06, VP-03, S-760, SRV-2000, U-220, XV-2020
- Yamaha: TG77, TG500, SY22, SY35, TX7, TX816, TX16W, SPX990, W7
- Korg: Volca Keys, Volca Bass, Volca Beats, Volca Nubass, SDD-3300, SG-Rack
- Ensoniq: ZR-76
- DigiTech: TSR-12, Legend II
- Clavia: Nord Rack 2X
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ ROLAND ------------------
    {
        "m_dir": "roland",
        "model_dir": "v-synth-gt",
        "manufacturer": "Roland",
        "model": "V-Synth GT",
        "type": "Dual-Core Elastic Audio Synthesizer",
        "year": 2007,
        "cc_map": {"time_trip_pad_x": 12, "time_trip_pad_y": 13, "filter_cutoff": 74, "resonance": 71, "ap_formant": 16, "cosm1_param": 17, "effects_level": 91},
        "sysex_header": "F0 41 10 00 00 24 12",
        "req_cmd": "F0 41 10 00 00 24 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "VariPhrase & AP-Synthesis Leads", [
                f"V-Synth GT Patch 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Vocal Designer & Elastic Audio Textures", [
                f"V-Synth GT Patch 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "sh-32",
        "manufacturer": "Roland",
        "model": "SH-32",
        "type": "Wave Acceleration Synthesizer",
        "year": 2001,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "osc1_wave": 16, "osc2_tune": 17, "filter_type": 18},
        "sysex_header": "F0 41 10 00 48 12",
        "req_cmd": "F0 41 10 00 48 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "Wave Acceleration Leads & Basses", [f"SH-32 Sound 1-{i+1:02d}" for i in range(64)]),
            ("Preset Bank 2", "ROM", 64, "Arpeggiator Patterns & Pads", [f"SH-32 Sound 2-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "sh-01a",
        "manufacturer": "Roland",
        "model": "SH-01A",
        "type": "Boutique Synthesizer Module",
        "year": 2017,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "env_attack": 73, "env_decay": 72, "mod_rate": 19, "sub_osc": 16},
        "sysex_header": "F0 41 10 00 00 00 40 12",
        "req_cmd": "F0 41 10 00 00 00 40 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "ACB SH-101 Analog Polyphonic Modeling", [
                f"SH-01A Patch {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "tr-08",
        "manufacturer": "Roland",
        "model": "TR-08",
        "type": "Boutique Rhythm Composer",
        "year": 2017,
        "cc_map": {"bd_tune": 20, "bd_tone": 21, "bd_decay": 22, "sd_tone": 23, "sd_snappy": 24, "sd_decay": 25, "ch_decay": 26},
        "sysex_header": "F0 41 10 00 00 00 3C 12",
        "req_cmd": "F0 41 10 00 00 00 3C 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "ACB TR-808 Discrete Analog Modeling", [
                f"TR-08 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "tr-09",
        "manufacturer": "Roland",
        "model": "TR-09",
        "type": "Boutique Rhythm Composer",
        "year": 2016,
        "cc_map": {"bd_tune": 20, "bd_attack": 21, "bd_decay": 22, "sd_tune": 23, "sd_snappy": 24, "sd_decay": 25, "ch_decay": 26},
        "sysex_header": "F0 41 10 00 00 00 2F 12",
        "req_cmd": "F0 41 10 00 00 00 2F 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "ACB TR-909 Discrete Analog & PCM", [
                f"TR-09 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "tr-06",
        "manufacturer": "Roland",
        "model": "TR-06",
        "type": "Boutique Drumatix",
        "year": 2020,
        "cc_map": {"bd_tune": 20, "bd_decay": 21, "sd_tune": 22, "sd_snappy": 23, "cymbal_decay": 24, "drive": 94},
        "sysex_header": "F0 41 10 00 00 00 6D 12",
        "req_cmd": "F0 41 10 00 00 00 6D 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "ACB TR-606 Drumatix Modeling", [
                f"TR-06 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "vp-03",
        "manufacturer": "Roland",
        "model": "VP-03",
        "type": "Boutique Vocoder Plus Module",
        "year": 2016,
        "cc_map": {"balance": 16, "tone": 17, "vocoder_level": 18, "strings_level": 19, "voice_level": 20, "attack": 73},
        "sysex_header": "F0 41 10 00 00 00 2E 12",
        "req_cmd": "F0 41 10 00 00 00 2E 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "ACB VP-330 Vocoder & Strings Ensemble", [
                f"VP-03 Preset {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "s-760",
        "manufacturer": "Roland",
        "model": "S-760",
        "type": "16-Bit Digital Sampler Rack",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "sample_start": 16, "envelope_release": 72},
        "sysex_header": "F0 41 10 56 12",
        "req_cmd": "F0 41 10 56 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Performance Bank", "ROM", 128, "Advanced 16-Bit Resonant Filter Sampling", [
                f"S-760 Performance {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "srv-2000",
        "manufacturer": "Roland",
        "model": "SRV-2000",
        "type": "16-Bit Digital Reverb Processor",
        "year": 1985,
        "cc_map": {"reverb_time": 16, "pre_delay": 17, "hf_damp": 18, "eq_low": 19, "eq_high": 20, "dry_wet": 91},
        "sysex_header": "F0 41 10 0B 12",
        "req_cmd": "F0 41 10 0B 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Programs", "ROM", 64, "Pioneering 16-Bit Studio Digital Reverb", [
                f"SRV-2000 Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "u-220",
        "manufacturer": "Roland",
        "model": "U-220",
        "type": "RS-PCM Synthesizer Module",
        "year": 1989,
        "cc_map": {"volume": 7, "pan": 10, "reverb_level": 91, "chorus_level": 93, "detune": 16, "attack": 73},
        "sysex_header": "F0 41 10 2B 12",
        "req_cmd": "F0 41 10 2B 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "RS-PCM Acoustic & Hybrid Voices", [f"U-220 Timbre 1-{i+1:02d}" for i in range(64)]),
            ("Preset Bank 2", "ROM", 64, "RS-PCM Orchestral & Synth Tones", [f"U-220 Timbre 2-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "xv-2020",
        "manufacturer": "Roland",
        "model": "XV-2020",
        "type": "64-Voice Synthesizer Module",
        "year": 2002,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 00 59 12",
        "req_cmd": "F0 41 10 00 59 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank A", "ROM", 128, "XV 64MB Waveform Library", [f"XV-2020 Patch A{i+1:03d}" for i in range(128)]),
            ("Preset Bank B", "ROM", 128, "XV Flagship Acoustic & Synth", [f"XV-2020 Patch B{i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "tg77",
        "manufacturer": "Yamaha",
        "model": "TG77",
        "type": "AFM + AWM2 Advanced Synthesizer Rack",
        "year": 1990,
        "cc_map": {"afm_cutoff": 74, "resonance": 71, "mod_wheel": 1, "pan": 10, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 34",
        "req_cmd": "F0 43 10 34 00 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "6-Operator AFM + 16-Bit AWM2 Realtime Convolution", [
                f"TG77 Voice 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Hybrid Digital Vector Waves", [
                f"TG77 Voice 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tg500",
        "manufacturer": "Yamaha",
        "model": "TG500",
        "type": "64-Voice 16-Part AWM2 Tone Generator",
        "year": 1992,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 3C",
        "req_cmd": "F0 43 10 3C 00 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Dual SY85 Engine Advanced AWM2", [
                f"TG500 Voice 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Multi-Timbral Performance Patches", [
                f"TG500 Voice 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "sy22",
        "manufacturer": "Yamaha",
        "model": "SY22",
        "type": "Vector Dynamic Synthesizer",
        "year": 1990,
        "cc_map": {"vector_x": 16, "vector_y": 17, "filter_cutoff": 74, "detune": 18, "effect_balance": 91},
        "sysex_header": "F0 43 10 30",
        "req_cmd": "F0 43 10 30 00 00 F7",
        "banks": [
            ("Internal Voices", "ROM", 128, "Dynamic Vector Mixing of 2-Op FM and 12-Bit AWM", [
                f"SY22 Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "sy35",
        "manufacturer": "Yamaha",
        "model": "SY35",
        "type": "Expanded Vector Synthesis Workstation",
        "year": 1992,
        "cc_map": {"vector_x": 16, "vector_y": 17, "filter_cutoff": 74, "detune": 18, "effect_balance": 91},
        "sysex_header": "F0 43 10 3D",
        "req_cmd": "F0 43 10 3D 00 00 F7",
        "banks": [
            ("Internal Voices", "ROM", 128, "Expanded 16-Bit Vector Synthesis", [
                f"SY35 Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tx7",
        "manufacturer": "Yamaha",
        "model": "TX7",
        "type": "Desktop FM Tone Generator",
        "year": 1985,
        "cc_map": {"volume": 7, "mod_wheel": 1, "breath": 2, "foot": 4, "portamento": 5},
        "sysex_header": "F0 43 00 00",
        "req_cmd": "F0 43 20 00 F7",
        "banks": [
            ("Factory Voices", "ROM", 32, "Pure 6-Operator 32-Algorithm DX7 Synthesis", [
                "Brass 1", "Brass 2", "Brass 3", "Strings 1", "Strings 2",
                "Strings 3", "Bass 1", "Bass 2", "E.Piano 1", "E.Piano 2",
                "Guitar 1", "Guitar 2", "Clav 1", "Clav 2", "Harpsichord 1",
                "Harpsichord 2", "Organ 1", "Organ 2", "Organ 3", "Flute 1",
                "Flute 2", "Orchestra", "Syn-Lead 1", "Syn-Lead 2", "Voices 1",
                "Voices 2", "Marimba", "Vibe", "Steel Drum", "Timpani",
                "Take-off", "Master Tune"
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tx816",
        "manufacturer": "Yamaha",
        "model": "TX816",
        "type": "Octal FM Tone Generator Rack",
        "year": 1984,
        "cc_map": {"volume": 7, "pan": 10, "mod_wheel": 1, "breath": 2, "expression": 11},
        "sysex_header": "F0 43 10 00",
        "req_cmd": "F0 43 10 00 01 00 F7",
        "banks": [
            ("Octal Layer Bank 1", "ROM", 128, "8x DX7 Engine Massive FM Layers", [
                f"TX816 Multi {i+1:03d}" for i in range(128)
            ]),
            ("Octal Layer Bank 2", "ROM", 128, "Orchestral & Polyphonic Walls of Sound", [
                f"TX816 Multi {i+129:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tx16w",
        "manufacturer": "Yamaha",
        "model": "TX16W",
        "type": "12-Bit Stereo Digital Sampler Rack",
        "year": 1987,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "sample_loop": 16, "envelope_attack": 73, "envelope_release": 72},
        "sysex_header": "F0 43 10 22",
        "req_cmd": "F0 43 10 22 00 00 F7",
        "banks": [
            ("Factory Performances", "ROM", 64, "12-Bit Digital Sampling & Dynamic VCF", [
                f"TX16W Performance {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "spx990",
        "manufacturer": "Yamaha",
        "model": "SPX990",
        "type": "20-Bit Professional Multi-Effects Processor",
        "year": 1993,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "mix": 91},
        "sysex_header": "F0 43 10 3E",
        "req_cmd": "F0 43 10 3E 00 00 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "20-Bit Reverb, Multi-Tap Delay & Pitch Shifting", [
                f"SPX990 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "w7",
        "manufacturer": "Yamaha",
        "model": "W7",
        "type": "16-Track AWM2 Advanced Workstation",
        "year": 1994,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 43",
        "req_cmd": "F0 43 10 43 00 00 00 00 F7",
        "banks": [
            ("Preset Voices", "ROM", 128, "Advanced AWM2 8MB Wave ROM Library", [
                f"W7 Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "volca-keys",
        "manufacturer": "Korg",
        "model": "Volca Keys",
        "type": "Analogue Loop Synthesizer",
        "year": 2013,
        "cc_map": {"voice_mode": 40, "octave": 41, "detune": 42, "vcf_cutoff": 44, "vcf_eg_int": 45, "delay_time": 46, "delay_feedback": 47},
        "sysex_header": "F0 42 30 00 01 2D",
        "req_cmd": "F0 42 30 00 01 2D 10 F7",
        "banks": [
            ("Pattern Memory", "ROM", 16, "3-Voice Analogue Mini-Polyphonic", [
                f"Volca Keys Pattern {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "volca-bass",
        "manufacturer": "Korg",
        "model": "Volca Bass",
        "type": "Analogue Bass Machine",
        "year": 2013,
        "cc_map": {"slide_time": 40, "lfo_rate": 41, "lfo_int": 42, "vco_pitch1": 43, "vco_pitch2": 44, "vcf_cutoff": 46, "vcf_resonance": 47},
        "sysex_header": "F0 42 30 00 01 2C",
        "req_cmd": "F0 42 30 00 01 2C 10 F7",
        "banks": [
            ("Pattern Memory", "ROM", 16, "Triple-Oscillator Analogue Acid Bass", [
                f"Volca Bass Pattern {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "volca-beats",
        "manufacturer": "Korg",
        "model": "Volca Beats",
        "type": "Analogue Rhythm Machine",
        "year": 2013,
        "cc_map": {"kick_click": 40, "kick_pitch": 41, "kick_decay": 42, "snare_snappy": 43, "snare_pitch": 44, "snare_decay": 45, "tom_decay": 46, "hat_grain": 49},
        "sysex_header": "F0 42 30 00 01 2B",
        "req_cmd": "F0 42 30 00 01 2B 10 F7",
        "banks": [
            ("Pattern Memory", "ROM", 16, "Analogue Drums + Lo-Fi PCM Percussion", [
                f"Volca Beats Pattern {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "volca-nubass",
        "manufacturer": "Korg",
        "model": "Volca Nubass",
        "type": "Vacuum Tube Acid Bass Synthesizer",
        "year": 2019,
        "cc_map": {"vcf_cutoff": 44, "vcf_resonance": 45, "vcf_eg_int": 46, "drive": 47, "tone": 48, "accent": 49},
        "sysex_header": "F0 42 30 00 01 54",
        "req_cmd": "F0 42 30 00 01 54 10 F7",
        "banks": [
            ("Pattern Memory", "ROM", 16, "Nutube Dual-Triode Oscillator & Sub-Oscillator", [
                f"Volca Nubass Pattern {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "sdd-3300",
        "manufacturer": "Korg",
        "model": "SDD-3300",
        "type": "Triple Digital Delay Processor",
        "year": 1986,
        "cc_map": {"delay1_time": 16, "delay1_feedback": 17, "delay2_time": 18, "delay3_time": 19, "master_mix": 91},
        "sysex_header": "F0 42 20 0E",
        "req_cmd": "F0 42 20 0E 10 F7",
        "banks": [
            ("Preset Programs", "ROM", 64, "Three Independent High-End Digital Delays", [
                f"SDD-3300 Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "sg-rack",
        "manufacturer": "Korg",
        "model": "SG-Rack",
        "type": "Stage Piano Sound Module",
        "year": 1997,
        "cc_map": {"volume": 7, "pan": 10, "brightness": 74, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 42 30 4B",
        "req_cmd": "F0 42 30 4B 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Stereo Concert Grand & Vintage Tines", [
                f"SG-Rack Program {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ ENSONIQ ------------------
    {
        "m_dir": "ensoniq",
        "model_dir": "zr-76",
        "manufacturer": "Ensoniq",
        "model": "ZR-76",
        "type": "Music Workstation Synthesizer",
        "year": 1998,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 0F 07 00",
        "req_cmd": "F0 0F 07 00 01 00 F7",
        "banks": [
            ("SoundFinder Bank 1", "ROM", 128, "William Coakley Perfect Piano & Drums", [
                f"ZR-76 Sound 1-{i+1:03d}" for i in range(128)
            ]),
            ("SoundFinder Bank 2", "ROM", 128, "Full Palette Workstation Sounds", [
                f"ZR-76 Sound 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ DIGITECH ------------------
    {
        "m_dir": "digitech",
        "model_dir": "tsr-12",
        "manufacturer": "Digitech",
        "model": "TSR-12",
        "type": "24-Bit True Stereo Digital Reverb & Effects",
        "year": 1994,
        "cc_map": {"decay_time": 16, "pre_delay": 17, "fx_level": 91, "chorus_depth": 18, "flange_speed": 19},
        "sysex_header": "F0 00 00 1A 08",
        "req_cmd": "F0 00 00 1A 08 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "True Stereo S-DISC Processing", [
                f"TSR-12 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "digitech",
        "model_dir": "legend-ii",
        "manufacturer": "Digitech",
        "model": "Legend II",
        "type": "Studio Guitar Preamp & Multi-Effects",
        "year": 1993,
        "cc_map": {"gain": 16, "bass": 17, "mid": 18, "treble": 19, "delay_time": 20, "mix": 91},
        "sysex_header": "F0 00 00 1A 07",
        "req_cmd": "F0 00 00 1A 07 01 00 F7",
        "banks": [
            ("Factory Programs", "ROM", 128, "Guitar Preamp & Digital Reverb/Pitch Multi-FX", [
                f"Legend II Program {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ CLAVIA ------------------
    {
        "m_dir": "clavia",
        "model_dir": "nord-rack-2x",
        "manufacturer": "Clavia",
        "model": "Nord Rack 2X",
        "type": "20-Voice Virtual Analog Rack Synthesizer",
        "year": 2003,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_wave": 16, "osc2_semitone": 17, "osc2_wave": 18, "envelope_attack": 73, "envelope_decay": 72},
        "sysex_header": "F0 33 04",
        "req_cmd": "F0 33 04 06 00 00 F7",
        "banks": [
            ("Bank 1", "ROM", 100, "20-Voice Expanded Virtual Analog", [
                f"Nord Rack 2X Sound {i+1:02d}" for i in range(100)
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
    print(f"Building Wave 21: Flagships, Advanced FM Vectors, Samplers & Volcas ({len(DEVICES)} Instruments)...")

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

    print(f"\nWave 21 Build Complete! {len(DEVICES)} new flagships, vectors, samplers & volcas created.")

if __name__ == "__main__":
    build_all()
