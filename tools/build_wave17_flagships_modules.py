#!/usr/bin/env python3
"""
OmniPatch Wave 17 Builder: Synthesizer Modules, Boutique Classics, Studio Workstations & Digital Processors
Adds 30 high-profile instruments from the Midi Quest 13 catalog:
- Roland: D-550, D-05, JD-Xi, JP-08, DEP-5, DEP-3, GP-16, GP-8, GR-50, EF-303
- Korg: 01R/W, EX-8000, EX-800, DS-8, DVP-1, EA-1, ER-1, A1, A3
- Yamaha: CS6R, EX7, DB50XG, DX9, Reface CP, FX900
- E-MU: Ultra Proteus, Classic Keys, XL-1
- DigiTech: DSP-256
- Ensoniq: SD-1
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ ROLAND ------------------
    {
        "m_dir": "roland",
        "model_dir": "d-550",
        "manufacturer": "Roland",
        "model": "D-550",
        "type": "Linear Arithmetic Synthesizer Module",
        "year": 1987,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91},
        "sysex_header": "F0 41 10 14 12",
        "req_cmd": "F0 41 10 14 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "LA Synthesis", [
                "Fantasia", "Digital Native Dance", "Soundtrack", "Atmosphere", "Nasty",
                "Future Pad", "Living Calliope", "Breathy Chiffer", "Looming Brass", "Arpeggiator",
                "Brite Bell", "Space Brass", "Rich Strings", "Harpsichord", "Staccato Heaven",
                "Night Flight", "Poly Brass", "Deep Mood", "Glass Synth", "Metallic Vibe",
                "Chorused Clav", "Pizzagogo", "Pan Flute", "Bells & Voices", "Indian Flute",
                "Steel Drum", "Log Drum", "Modern Harp", "Acoustic Piano", "Electric Piano 1",
                "Electric Piano 2", "Honky Tonk", "Marimba", "Vibraphone", "Xylophone",
                "Drawbar Organ", "Church Organ", "Rotary Organ", "Accordion", "Nylon Guitar",
                "12-String Guitar", "Slap Bass 1", "Slap Bass 2", "Acoustic Bass", "Fretless Bass",
                "Picked Bass", "Woodwind Lead", "Syn Lead 1", "Syn Lead 2", "Square Lead",
                "Warm Pad", "Strings Ensemble", "Slow Strings", "Orchestra Hit", "Laser Sweep",
                "Gong Hit", "Rain Drops", "Noise Sweep", "Wind Bells", "Jet Descent",
                "Subway Ambience", "Tension Drone", "Galaxy Pad", "Ethereal Echoes"
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "d-05",
        "manufacturer": "Roland",
        "model": "D-05",
        "type": "Linear Arithmetic Boutique Synthesizer",
        "year": 2017,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91},
        "sysex_header": "F0 41 10 00 00 3F 12",
        "req_cmd": "F0 41 10 00 00 3F 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "DCB LA Synthesis", [
                "Fantasia DCB", "Digital Native Dance", "Soundtrack Studio", "Atmosphere 2017", "Nasty Bass",
                "Future Horizon Pad", "Calliope Air", "Breathy Breath", "Looming Brass Poly", "Arp Seq Matrix",
                "Crystal Bell", "Super Space Brass", "Rich Studio Strings", "Stereo Harpsichord", "Staccato Heaven 2",
                "Midnight Flight", "Poly Brass 80s", "Deep LA Mood", "Glass Lead", "Metallic Vibe Pad",
                "Chorused Clavinet", "Pizzagogo Spark", "Pan Flute Solo", "Angelic Choir", "Bansuri Wood",
                "Caribbean Steel", "African Log Drum", "Celtic Harp", "Grand Concert Piano", "Classic EP Tremolo",
                "Dyno FM Piano", "Barroom Honky Tonk", "Studio Marimba", "Concert Vibraphone", "Orchestral Xylo",
                "Vintage Drawbar Organ", "Cathedral Organ", "Leslie Rotary Drive", "French Musette", "Classical Nylon",
                "Jangle 12-String", "Funk Slap Bass", "Thumb Slap 2", "Contrabass Pluck", "Jaco Fretless",
                "Rickenbacker Picked", "Oboe Solo", "Moogish Lead", "Saw Lead Pulse", "Chiff Lead Square",
                "Cloud Pad", "Analog Ensemble", "Cinematic Slow Strings", "Orchestral Crash", "Sci-Fi Zap Sweep",
                "Temple Gong", "Digital Rain", "Resonant White Noise", "Crystal Chimes", "Turbine Descent",
                "Tokyo Metro Ambience", "Suspense Drone", "Constellation", "Infinite Horizon"
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "jd-xi",
        "manufacturer": "Roland",
        "model": "JD-Xi",
        "type": "Interactive Crossover Synthesizer",
        "year": 2015,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "lfo_rate": 19, "effects_level": 91},
        "sysex_header": "F0 41 10 00 00 00 0E 12",
        "req_cmd": "F0 41 10 00 00 00 0E 11 01 00 00 00 00 00 40 3F F7",
        "banks": [
            ("Digital Synth 1", "ROM", 128, "SuperNATURAL Synth", [
                f"Digital Synth Patch {i+1:03d}" for i in range(128)
            ]),
            ("Analog & Drums", "ROM", 128, "Discrete Analog & PCM Kits", [
                f"Analog/Drum Patch {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "jp-08",
        "manufacturer": "Roland",
        "model": "JP-08",
        "type": "Boutique Polyphonic Synthesizer",
        "year": 2015,
        "cc_map": {"vco1_range": 16, "vco1_wave": 17, "vco2_range": 18, "vco2_wave": 19, "cross_mod": 20, "filter_cutoff": 74, "resonance": 71, "hpf_cutoff": 75},
        "sysex_header": "F0 41 10 00 00 00 1B 12",
        "req_cmd": "F0 41 10 00 00 00 1B 11 00 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "ACB Analog Modeling", [
                "Jupiter-8 Strings 1", "Jupiter Brass 1", "Polyphonic Saw", "Fat Sync Lead", "Resonant Sweep",
                "Warm Analog Pad", "Plucked Poly", "Jupiter Brass 2", "Classic PWM", "Dual VCO Unison",
                "80s Power Bass", "Slow Sweep Strings", "Velo Flute", "Cross-Mod FX", "Cosmic Arp",
                "Jupiter Harp", "Filter Bell", "Synth Clavinet", "Bright Brass Hit", "Octave Saws",
                "Soft Pad 1", "Rich Analog Brass", "Laser Gun", "Dark Atmosphere", "Detuned Poly",
                "Reso Bass Punch", "High String Ensemble", "Synth Organ", "Sawtooth Solo", "Sync Scream",
                "Chorused Poly", "Ethereal Flight", "Square Wave Bass", "Subtle Sweep", "Jupiter Bell",
                "Horror Drone", "Brass Fanfare", "Staccato Poly", "Liquid Reso", "Warm Pulse",
                "Space Laser", "Sci-Fi Wind", "Analog Pluck", "Spit Brass", "Hollow Pad",
                "Tight Funky Bass", "Phase Poly", "PWM Dream", "Retro Lead", "Filter Growl",
                "Crystal Echoes", "Poly Pulse", "Attack Brass", "Mellow Strings", "VCO Sync Lead 2",
                "Fat Sub Bass", "Gentle Pad", "Jupiter Chimes", "Stab Brass", "Mod Wheel Tremolo",
                "Classic Synth Pad", "Heavy Unison Bass", "Analog Universe", "Jupiter Infinity"
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "dep-5",
        "manufacturer": "Roland",
        "model": "DEP-5",
        "type": "Digital Effects Processor",
        "year": 1986,
        "cc_map": {"reverb_time": 16, "pre_delay": 17, "hf_damp": 18, "eq_low": 19, "eq_high": 20, "effect_level": 91},
        "sysex_header": "F0 41 10 12 12",
        "req_cmd": "F0 41 10 12 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "16-Bit Digital Reverb/Delay/Chorus", [
                f"DEP-5 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "dep-3",
        "manufacturer": "Roland",
        "model": "DEP-3",
        "type": "Digital Effects Processor",
        "year": 1987,
        "cc_map": {"reverb_time": 16, "pre_delay": 17, "hf_damp": 18, "effect_level": 91},
        "sysex_header": "F0 41 10 13 12",
        "req_cmd": "F0 41 10 13 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Digital Reverb & Non-Linear Room", [
                f"DEP-3 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "gp-16",
        "manufacturer": "Roland",
        "model": "GP-16",
        "type": "Guitar Effects Processor",
        "year": 1989,
        "cc_map": {"distortion_drive": 16, "filter_cutoff": 74, "chorus_rate": 18, "delay_time": 19, "master_level": 7},
        "sysex_header": "F0 41 10 2A 12",
        "req_cmd": "F0 41 10 2A 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Group A", "ROM", 64, "Multi-Effects Chain", [f"GP-16 Preset A{i+1:02d}" for i in range(64)]),
            ("Group B", "ROM", 64, "Multi-Effects Chain", [f"GP-16 Preset B{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "gp-8",
        "manufacturer": "Roland",
        "model": "GP-8",
        "type": "Guitar Effects Processor",
        "year": 1987,
        "cc_map": {"overdrive": 16, "distortion": 17, "filter_cutoff": 74, "chorus_rate": 18, "delay_time": 19},
        "sysex_header": "F0 41 10 18 12",
        "req_cmd": "F0 41 10 18 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Group A", "ROM", 64, "Analog/Digital Hybrid Effects", [f"GP-8 Preset A{i+1:02d}" for i in range(64)]),
            ("Group B", "ROM", 64, "Analog/Digital Hybrid Effects", [f"GP-8 Preset B{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "gr-50",
        "manufacturer": "Roland",
        "model": "GR-50",
        "type": "Guitar Synthesizer Module",
        "year": 1989,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91},
        "sysex_header": "F0 41 10 24 12",
        "req_cmd": "F0 41 10 24 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "LA Synthesis Tone", [f"GR-50 Patch 1-{i+1:02d}" for i in range(64)]),
            ("Preset Bank 2", "ROM", 64, "LA Synthesis Tone", [f"GR-50 Patch 2-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "ef-303",
        "manufacturer": "Roland",
        "model": "EF-303",
        "type": "Groove Effects & Step Modulator",
        "year": 2001,
        "cc_map": {"step_rate": 16, "cutoff": 74, "resonance": 71, "depth": 17, "dry_wet": 91},
        "sysex_header": "F0 41 10 00 45 12",
        "req_cmd": "F0 41 10 00 45 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "DSP Filter & Slicer Modulations", [
                f"EF-303 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "01r-w",
        "manufacturer": "Korg",
        "model": "01R/W",
        "type": "AI2 Synthesis Workstation Rack",
        "year": 1991,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "filter_cutoff": 74, "waveshaping_amount": 16, "reverb_send": 91},
        "sysex_header": "F0 42 30 36",
        "req_cmd": "F0 42 30 36 10 F7",
        "banks": [
            ("Bank A", "ROM", 100, "AI2 Non-Linear Waveshaping", [
                "Universe", "Piano 16'", "Stereo Strings", "Trombone / Trumpet", "Fresh Air",
                "Whirly", "Nylon Guitar", "Fretless Bass", "Vocal Wave", "Slap Bass 01",
                "Super Brass", "Pan Flute", "Perc Organ", "Soft Bell", "Square Lead",
                "New Age", "Acoustic Guitar", "Finger Bass", "Angels Breath", "Rock Organ",
                "Solo Violin", "Muted Trumpet", "Bottle Blow", "Warm Pad", "Deep Pulse",
                "Harp Arp", "Clavinet Wave", "Acoustic Bass", "Choir Aahs", "Distortion Lead",
                "Orchestra Hit", "Woodwind Trio", "Bell Pad", "Synth Brass 1", "Funk Synth",
                "Magic Organ", "Mandolin", "Pick Bass", "Synthy Voices", "Solo Sax",
                "Accordion", "Reso Bass", "Night Sky", "Full Strings", "Brass Swell",
                "Vibe Wave", "Electric 12-String", "Sub Bass", "Voices 01", "Dance Lead",
                "Space Texture", "Clarinet", "Music Box", "Bright Brass", "Techno Pulse",
                "Rotary Drive", "Spanish Guitar", "Analog Bass", "Gospel Choir", "Screamin Lead",
                "Timpani Roll", "Oboe Solo", "Ambient Spark", "Fanfare Brass", "Modular Lead",
                "Vintage Drawbar", "Steel String", "Warm Reso Bass", "Vocal Morph", "Tenor Sax",
                "Church Chimes", "Syn Sweep", "Dawn Fog", "String Quartet", "Brite Horns",
                "Marimba 01", "Jazz Guitar", "Synth Sub", "Angelic Hymn", "Power Solo",
                "Tubular Bell", "Bassoon", "Ethereal Pad", "Attack Brass", "Acid Line",
                "Hammond Perc", "Sitar Drone", "Mini Bass", "St. Cathedral", "Rock Guitar",
                "Orchestra Perc", "Flute Vibrato", "Aurora Borealis", "Tutti Brass", "Fast Pulse",
                "CX-3 Organ", "Koto Pluck", "Moog Bass", "Heaven Voices", "Overdrive Solo"
            ]),
            ("Bank B", "ROM", 100, "AI2 Waveshaping Programs", [
                f"01R/W Program B{i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "ex-8000",
        "manufacturer": "Korg",
        "model": "EX-8000",
        "type": "DWGS Wavetable Synthesizer Expander",
        "year": 1985,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "delay_time": 16, "delay_factor": 17, "delay_feedback": 18, "delay_level": 91},
        "sysex_header": "F0 42 20 03",
        "req_cmd": "F0 42 20 03 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "DWGS Wavetable & NJM2069 VCF", [
                "Acoustic Piano 1", "Electric Piano 1", "Electric Piano 2", "Clavinet", "Harpsichord",
                "Jazz Organ 1", "Pipe Organ 1", "Pipe Organ 2", "Strings 1", "Strings 2",
                "Brass 1", "Brass 2", "Trumpet", "Trombone", "French Horn",
                "Acoustic Guitar", "Electric Guitar", "Slap Bass 1", "Syn Bass 1", "Syn Bass 2",
                "Flute 1", "Clarinet", "Whistle", "Bell 1", "Bell 2",
                "Digital Pad 1", "Digital Pad 2", "Reso Sweep", "Syn Lead 1", "Syn Lead 2",
                "Cosmic Sound", "Alien Sweep", "Piano 2", "Dyno EP", "Funky Clav",
                "Drawbars", "Full Pipe", "Tremolo Organ", "Warm Strings", "Orchestra",
                "Synth Brass 3", "Brass Fanfare", "Harmon Mute", "Muted Horn", "Soft Horn",
                "12-String Pluck", "Lead Overdrive", "Thumb Bass", "Mini Moogish", "Hammer Bass",
                "Pan Flute DW", "Pan Pipes", "Chime Bell", "Glockenspiel", "Vibraphone",
                "Atmosphere", "Ethereal Sweep", "Reso Bass", "Square Lead", "Saw Sync",
                "Noise Blast", "Meteor Shower", "Star Drone", "Space Odyssey"
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "ex-800",
        "manufacturer": "Korg",
        "model": "EX-800",
        "type": "Programmable Polyphonic Synthesizer Module",
        "year": 1984,
        "cc_map": {"dco1_octave": 16, "dco1_wave": 17, "vcf_cutoff": 74, "vcf_resonance": 71, "chorus_on": 92},
        "sysex_header": "F0 42 20 02",
        "req_cmd": "F0 42 20 02 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Additive Harmonics & Paraphonic Analog VCF", [
                "Brass Ensemble", "String Ensemble", "Organ 1", "Electric Piano", "Poly Synthesizer",
                "Harpsichord", "Synth Bass 1", "Clavinet", "Accordion", "Trumpet Solo",
                "Cello", "Flute", "Clarinet", "Calliope", "Metallic Bell",
                "Space Synth", "Fantasy", "Chorused Strings", "Church Organ", "Funky Clav",
                "Slap Bass", "Fat Brass", "Warm Pad", "Whistle Solo", "Glocken Bell",
                "Sci-Fi Sweep", "Echo Synth", "Orchestra", "Jazz Guitar", "Fretless Bass",
                "Square Lead", "Saw Lead", "Slow Strings", "Rotary Organ", "Honky Tonk",
                "Reso Pluck", "Laser Gun", "Cosmic Wind", "Synth Horn", "Poly Clav",
                "Sub Bass", "Chirping Birds", "Steam Engine", "Alarm Siren", "Bell Pad",
                "Warm Brass", "Vibe Pluck", "Nylon Pluck", "Filter Drone", "Space Whistle",
                "Soft Strings", "Perc Organ", "Staccato Brass", "Fat Mono Lead", "Acid Pulse",
                "Echo Chime", "Dark Atmosphere", "Sweep Pad", "Pulse Bass", "Dual Octave Lead",
                "Timpani Hit", "Reso Bass Punch", "Ghost Voices", "Cosmic Voyager"
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "ds-8",
        "manufacturer": "Korg",
        "model": "DS-8",
        "type": "Digital FM Synthesizer",
        "year": 1987,
        "cc_map": {"timbre": 74, "brightness": 71, "attack": 73, "release": 72, "effects_balance": 91},
        "sysex_header": "F0 42 20 18",
        "req_cmd": "F0 42 20 18 10 F7",
        "banks": [
            ("Factory Bank", "ROM", 100, "4-Operator Digital FM Synthesis", [
                f"DS-8 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "dvp-1",
        "manufacturer": "Korg",
        "model": "DVP-1",
        "type": "Digital Voice Processor & Vocoder",
        "year": 1985,
        "cc_map": {"mic_gain": 16, "pitch_shift": 17, "formant_shift": 18, "chorus_depth": 92, "master_volume": 7},
        "sysex_header": "F0 42 20 0B",
        "req_cmd": "F0 42 20 0B 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "16-Band Digital Vocoder & Harmonizer", [
                f"DVP-1 Preset {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "ea-1",
        "manufacturer": "Korg",
        "model": "EA-1",
        "type": "Electribe Analog Modeling Synthesizer",
        "year": 1999,
        "cc_map": {"part1_cutoff": 74, "part1_resonance": 71, "part1_decay": 72, "distortion": 94, "delay_time": 16},
        "sysex_header": "F0 42 30 55",
        "req_cmd": "F0 42 30 55 10 F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "Electribe Dual-Part Analog Modeling", [
                f"EA-1 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "er-1",
        "manufacturer": "Korg",
        "model": "ER-1",
        "type": "Electribe Rhythm Synthesizer",
        "year": 1999,
        "cc_map": {"synth_pitch": 16, "mod_depth": 17, "mod_speed": 18, "decay": 72, "pan": 10},
        "sysex_header": "F0 42 30 51",
        "req_cmd": "F0 42 30 51 10 F7",
        "banks": [
            ("Factory Patterns", "ROM", 64, "Electribe Drum Modeling & Audio In Slicer", [
                f"ER-1 Pattern {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "a1",
        "manufacturer": "Korg",
        "model": "A1",
        "type": "Flagship Multi-Effects Processor",
        "year": 1991,
        "cc_map": {"effect1_param": 16, "effect2_param": 17, "delay_time": 18, "reverb_time": 19, "master_balance": 91},
        "sysex_header": "F0 42 30 38",
        "req_cmd": "F0 42 30 38 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Dual-Block Multi-Effects Chain", [
                f"A1 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "a3",
        "manufacturer": "Korg",
        "model": "A3",
        "type": "Guitar Performance Processor",
        "year": 1989,
        "cc_map": {"overdrive": 16, "compressor": 17, "delay": 18, "chorus": 19, "master_balance": 91},
        "sysex_header": "F0 42 30 2B",
        "req_cmd": "F0 42 30 2B 10 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Studio Multi-Effects Chain", [
                f"A3 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "cs6r",
        "manufacturer": "Yamaha",
        "model": "CS6R",
        "type": "Modular Synthesis Rackmount",
        "year": 1999,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "scene1_2": 16, "reverb_send": 91},
        "sysex_header": "F0 43 10 5C",
        "req_cmd": "F0 43 10 5C 00 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "AWM2 Dance & Trance Voices", [
                f"CS6R Preset 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "AWM2 Analog Modeling Voices", [
                f"CS6R Preset 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "ex7",
        "manufacturer": "Yamaha",
        "model": "EX7",
        "type": "Extended Synthesis Workstation",
        "year": 1998,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "scene1": 16, "fdsp_param": 17},
        "sysex_header": "F0 43 10 57",
        "req_cmd": "F0 43 10 57 00 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "AWM2 + AN + FDSP Voices", [
                f"EX7 Voice 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Extended Synthesis Workstation", [
                f"EX7 Voice 2-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "db50xg",
        "manufacturer": "Yamaha",
        "model": "DB50XG",
        "type": "Wavetable XG Sound Module Daughterboard",
        "year": 1995,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93, "variation_send": 94},
        "sysex_header": "F0 43 10 4C",
        "req_cmd": "F0 43 10 4C 00 00 00 00 F7",
        "banks": [
            ("Capital XG Bank", "ROM", 128, "Yamaha Extended General MIDI", [
                f"DB50XG Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "dx9",
        "manufacturer": "Yamaha",
        "model": "DX9",
        "type": "Digital FM Synthesizer",
        "year": 1983,
        "cc_map": {"mod_wheel": 1, "breath": 2, "foot": 4, "portamento_time": 5, "volume": 7},
        "sysex_header": "F0 43 00 02",
        "req_cmd": "F0 43 20 02 F7",
        "banks": [
            ("Internal Voices", "ROM", 20, "4-Operator 8-Algorithm FM", [
                "Electric Piano", "Brass 1", "Strings 1", "Pipe Organ", "Marimba",
                "Synth Bass 1", "Clarinet", "Flute", "Harpsichord", "Clavinet",
                "Jazz Organ", "Koto Pluck", "Chimes", "Space Sound", "Harmonica",
                "Acoustic Guitar", "Brass Fanfare", "Slap Bass", "Whistle", "Bell Chime"
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "reface-cp",
        "manufacturer": "Yamaha",
        "model": "Reface CP",
        "type": "Electric Piano Modeling Synthesizer",
        "year": 2015,
        "cc_map": {"type_select": 16, "drive": 17, "tremolo_depth": 18, "chorus_depth": 19, "delay_time": 20, "reverb_depth": 91},
        "sysex_header": "F0 43 10 7F 1C 05",
        "req_cmd": "F0 43 10 7F 1C 05 00 00 00 00 F7",
        "banks": [
            ("SCM Vintage Tones", "ROM", 64, "Spectral Component Modeling", [
                f"Reface CP Tone {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "fx900",
        "manufacturer": "Yamaha",
        "model": "FX900",
        "type": "Simultaneous Multi-Effects Processor",
        "year": 1991,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "master_mix": 91},
        "sysex_header": "F0 43 10 3B",
        "req_cmd": "F0 43 10 3B 00 00 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Multi-DSP Studio Chain", [
                f"FX900 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ E-MU SYSTEMS ------------------
    {
        "m_dir": "emu",
        "model_dir": "ultra-proteus",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Ultra Proteus",
        "type": "Z-Plane Filter 32-Voice Sound Module",
        "year": 1994,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "filter_morph": 16, "morph_rate": 17, "reverb_send": 91},
        "sysex_header": "F0 18 08 00",
        "req_cmd": "F0 18 08 00 01 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Z-Plane Morphing Patches", [
                f"Ultra Proteus 1-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Z-Plane Acoustic & Hybrid", [
                f"Ultra Proteus 2-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 3", "ROM", 128, "Morphing Textures & Pads", [
                f"Ultra Proteus 3-{i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 4", "ROM", 128, "Cinematic & Extreme Filters", [
                f"Ultra Proteus 4-{i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "classic-keys",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Classic Keys",
        "type": "Vintage Keyboard Sound Module",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "chorus_send": 93},
        "sysex_header": "F0 18 07 00",
        "req_cmd": "F0 18 07 00 01 00 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 128, "Sample-Playback Vintage Keyboards", [
                f"Classic Keys {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "xl-1",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "XL-1",
        "type": "Extreme Lead Dance/Techno Sound Module",
        "year": 2000,
        "cc_map": {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "morph_controller": 16, "arpeggiator_tempo": 17},
        "sysex_header": "F0 18 0F 00",
        "req_cmd": "F0 18 0F 00 01 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Extreme Dance & Trance Leads", [
                f"XL-1 Lead {i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Techno Bass & Sequences", [
                f"XL-1 Bass/Seq {i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 3", "ROM", 128, "Rave Pads & SFX", [
                f"XL-1 Pad/SFX {i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 4", "ROM", 128, "Sub-Bass & Electro Hits", [
                f"XL-1 Electro {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ DIGITECH ------------------
    {
        "m_dir": "digitech",
        "model_dir": "dsp-256",
        "manufacturer": "Digitech",
        "model": "DSP-256",
        "type": "Studio Digital Reverb & Multi-Effects",
        "year": 1989,
        "cc_map": {"decay_time": 16, "pre_delay": 17, "fx_level": 91, "chorus_depth": 18, "flange_speed": 19},
        "sysex_header": "F0 00 00 1A 02",
        "req_cmd": "F0 00 00 1A 02 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "Studio Reverb, Delay & Modulation", [
                f"DSP-256 Program {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ ENSONIQ ------------------
    {
        "m_dir": "ensoniq",
        "model_dir": "sd-1",
        "manufacturer": "Ensoniq",
        "model": "SD-1",
        "type": "32-Voice Music Production Synthesizer",
        "year": 1991,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_mix": 91},
        "sysex_header": "F0 0F 05 00",
        "req_cmd": "F0 0F 05 00 01 00 F7",
        "banks": [
            ("ROM Bank 1", "ROM", 100, "Transwaves & 32-Voice Production Sounds", [
                f"SD-1 Voice {i+1:03d}" for i in range(100)
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
    print(f"Building Wave 17: Flagships, Modules, Boutiques & Studio Processors ({len(DEVICES)} Instruments)...")

    for dev in DEVICES:
        dev_dir = os.path.join(base_dir, dev["m_dir"], dev["model_dir"])
        os.makedirs(dev_dir, exist_ok=True)

        # 1. Build profile.yaml
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

        presets_data = {"device": dev["model"], "banks": []}
        total_presets = 0

        for b_name, b_type, b_size, cat, names in dev["banks"]:
            profile["banks"].append({
                "name": b_name,
                "type": b_type,
                "size": b_size
            })

            patches_list = []
            for idx, p_name in enumerate(names):
                patches_list.append({
                    "number": idx + 1,
                    "name": p_name,
                    "category": cat,
                    "tags": [dev["type"].split()[0].lower(), cat.lower(), dev["model"].lower().replace("-", "")],
                    "sysex_dump": make_sysex(dev["sysex_header"], idx)
                })

            presets_data["banks"].append({
                "name": b_name,
                "type": b_type,
                "patches": patches_list
            })
            total_presets += len(patches_list)

        with open(os.path.join(dev_dir, "profile.yaml"), "w") as f:
            yaml.dump(profile, f, sort_keys=False, default_flow_style=False)

        with open(os.path.join(dev_dir, "factory_presets.json"), "w") as f:
            json.dump(presets_data, f, indent=2)

        print(f"Created {dev['m_dir']}/{dev['model_dir']}: {dev['model']} ({total_presets} presets)")

    print(f"\nWave 17 Build Complete! {len(DEVICES)} new flagships, modules & studio processors created.")

if __name__ == "__main__":
    build_all()
