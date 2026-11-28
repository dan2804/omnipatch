#!/usr/bin/env python3
"""
OmniPatch Wave 28 - Studio Flagships, Vintage Icons & Modern Analog Workstations
Ingests 33 high-profile instruments across:
- Elektron (Machinedrum, Monomachine, Octatrack, Analog Rytm, Analog Keys)
- Ensoniq (Fizmo, Mirage, Halo)
- E-MU Systems (Mo'Phatt, MP-7 Command Station, PK-6, MK-6, Procussion)
- Waldorf (Micro Q, Microwave II, STVC)
- Alesis (Fusion 6HD/8HD, S4 QuadraSynth Rack, QS6, QS7, QS8, QS6.1, QS7.1, QS8.1, QSR)
- Crumar (Bit One, Bit 01, Bit 99)
- Studio Electronics (Omega 8, CODE 8)
- Historical Giants (NED Synclavier II, Digital Keyboards Synergy)
- Akai Professional (VX90, Timbre Wolf, Rhythm Wolf)
"""

import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEVICES_DIR = os.path.join(BASE_DIR, "devices")

WAVE28_MODELS = [
    # ==========================================
    # ELEKTRON
    # ==========================================
    {
        "mfg": "elektron",
        "folder": "machinedrum",
        "name": "Elektron Machinedrum SPS-1 / SPS-1UW",
        "type": "16-Track Digital Drum Synthesizer",
        "year": 2001,
        "sysex_hdr": "F0 00 20 3C 02",
        "sysex_cmd": "F0 00 20 3C 02 52 [kit] F7",
        "cc_map": {"pitch": 16, "decay": 17, "filter_freq": 18, "filter_res": 19, "lfo_speed": 20, "lfo_depth": 21, "delay_send": 22, "reverb_send": 23},
        "banks": [
            ("TRX Electronic Kits", 32, "Roland TR-808/909 Emulation & Modern Analog Models"),
            ("EFM FM Percussion", 32, "Feedback FM Metallic Percussion & Experimental Bells"),
            ("E12 Sampled Beats", 32, "Vintage 12-Bit Gritty Drum Machine Sample Kits"),
            ("P-I Physical Acoustic", 32, "Physical Modeling Snares, Toms, Bells & Resonators")
        ]
    },
    {
        "mfg": "elektron",
        "folder": "monomachine",
        "name": "Elektron Monomachine SFX-6 / SFX-60",
        "type": "6-Track Multi-Engine Synthesizer",
        "year": 2004,
        "sysex_hdr": "F0 00 20 3C 03",
        "sysex_cmd": "F0 00 20 3C 03 53 [kit] F7",
        "cc_map": {"pitch": 16, "cutoff": 17, "resonance": 18, "attack": 19, "decay": 20, "lfo_depth": 21, "delay_time": 22, "delay_feedback": 23},
        "banks": [
            ("SuperWave Lead & Bass", 32, "Multi-Saw Subtractive Leads, Acid Basses & Plucks"),
            ("SID 6581 Chiptune", 32, "Commodore 64 MOS SID Sound Chip Emulation Kits"),
            ("DigiPRO Wavetable", 32, "12-Bit Digital Waveforms & User PCM Tables"),
            ("FM+ Algorithms", 32, "4-Operator Frequency Modulation Experimental Timbres")
        ]
    },
    {
        "mfg": "elektron",
        "folder": "octatrack",
        "name": "Elektron Octatrack DPS-1",
        "type": "8-Track Dynamic Performance Sampler",
        "year": 2010,
        "sysex_hdr": "F0 00 20 3C 07",
        "sysex_cmd": "F0 00 20 3C 07 50 [part] F7",
        "cc_map": {"crossfader": 48, "pitch": 16, "playback_rate": 17, "filter_cutoff": 18, "filter_res": 19, "amp_vol": 20, "reverb_send": 21, "delay_send": 22},
        "banks": [
            ("Live Remix Projects", 32, "Realtime Time-Stretching & Granular Loop Remixes"),
            ("Stereo Beat Production", 32, "Multitrack Drum Loops & One-Shot Slice Sets"),
            ("Stem Deconstruction", 32, "Vocal Chop, Bassline & Synth Phrase Processing"),
            ("Ambient Soundscapes", 32, "Granular Tape Shifting & Generative Spatial Drones")
        ]
    },
    {
        "mfg": "elektron",
        "folder": "analog-rytm",
        "name": "Elektron Analog Rytm",
        "type": "8-Voice Hybrid Analog Drum Machine & Sampler",
        "year": 2014,
        "sysex_hdr": "F0 00 20 3C 08",
        "sysex_cmd": "F0 00 20 3C 08 51 [kit] F7",
        "cc_map": {"synth_tune": 16, "synth_decay": 17, "analog_overdrive": 18, "vcf_cutoff": 19, "vcf_res": 20, "sample_tune": 21, "delay_send": 22, "reverb_send": 23},
        "banks": [
            ("Analog Bass Drums & Snares", 32, "Deep Sub Kicks, Dual-VCO Snares & Analog Claps"),
            ("Hybrid Drum Kits", 32, "Combined Analog Voice + Digital Sample Layered Percussion"),
            ("Overdriven Industrial Beats", 32, "Saturated Master Distortion & Compressor Hits"),
            ("Melodic Percussion & Chords", 32, "Tuned Analog Toms, Metallic Hats & Cymbal Prones")
        ]
    },
    {
        "mfg": "elektron",
        "folder": "analog-keys",
        "name": "Elektron Analog Keys",
        "type": "4-Voice Discrete Analog Synthesizer Keyboard",
        "year": 2014,
        "sysex_hdr": "F0 00 20 3C 06",
        "sysex_cmd": "F0 00 20 3C 06 50 [patch] F7",
        "cc_map": {"osc1_tune": 16, "osc2_tune": 17, "vcf_cutoff": 74, "vcf_res": 71, "overdrive": 18, "env_attack": 73, "env_decay": 75, "joystick_x": 1},
        "banks": [
            ("Polyphonic Leads & Pads", 32, "4-Voice Warm Analog Polysynths & Lush Moving Sweeps"),
            ("Punchy Analog Basses", 32, "Dual Sub-Oscillator Basses & Acid Squelches"),
            ("Split & Multitimbral Rigs", 32, "Key-Split Performance Setups & 4-Voice Stacks"),
            ("FX & Analog Soundscapes", 32, "Cross-Modulated Drones, Resonant Sweeps & Noise Hits")
        ]
    },

    # ==========================================
    # ENSONIQ
    # ==========================================
    {
        "mfg": "ensoniq",
        "folder": "fizmo",
        "name": "Ensoniq Fizmo",
        "type": "Realtime Transwave Polyphonic Synthesizer",
        "year": 1998,
        "sysex_hdr": "F0 0F 07",
        "sysex_cmd": "F0 0F 07 01 [preset] F7",
        "cc_map": {"wave_mod": 16, "f_knob_1": 17, "f_knob_2": 18, "f_knob_3": 19, "f_knob_4": 20, "filter_cutoff": 74, "filter_res": 71, "fx_depth": 91},
        "banks": [
            ("Factory Presets Bank A", 64, "Dynamic Transwave Pads, Textures & Morphing Leads"),
            ("Factory Presets Bank B", 64, "Complex Motion Synths, Rhythmic Sweeps & Vocals")
        ]
    },
    {
        "mfg": "ensoniq",
        "folder": "mirage",
        "name": "Ensoniq Mirage DSK / DMS",
        "type": "8-Bit Sampling Synthesizer (CEM 3328 VCF)",
        "year": 1984,
        "sysex_hdr": "F0 0F 01",
        "sysex_cmd": "F0 0F 01 00 [param] [val] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_res": 71, "env_attack": 73, "env_decay": 75, "pitch_bend": 1, "lfo_depth": 77},
        "banks": [
            ("Factory Diskette Soundbank 1", 32, "8-Bit Acoustic Grands, Electric Pianos & Harpsichords"),
            ("Factory Diskette Soundbank 2", 32, "Vintage Strings, Choir Ahs, Brass Hits & Orchestral Stabs"),
            ("Factory Diskette Soundbank 3", 32, "Sampled Analog Synths, Slap Basses & Electronic Percussion")
        ]
    },
    {
        "mfg": "ensoniq",
        "folder": "halo",
        "name": "Ensoniq Halo",
        "type": "64-Voice Keyboard Workstation (Transwave ROM)",
        "year": 2002,
        "sysex_hdr": "F0 0F 08",
        "sysex_cmd": "F0 0F 08 00 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "env_attack": 73, "env_release": 72, "chorus_send": 93, "reverb_send": 91},
        "banks": [
            ("Preset Bank 1 - Keys & Organs", 128, "Stereo Acoustic Pianos, Rhodes, Wurlys & B3 Tonewheels"),
            ("Preset Bank 2 - Strings & Brass", 128, "Orchestral String Sections, Brass Ensembles & Solo Reeds"),
            ("Preset Bank 3 - Transwave Synths", 128, "Dynamic Transwave Morphing Leads, Sweeps & Pads"),
            ("Preset Bank 4 - Drums & FX", 128, "Urban & Pop Drum Kits, Sound FX & Acoustic Percussion")
        ]
    },

    # ==========================================
    # E-MU SYSTEMS
    # ==========================================
    {
        "mfg": "emu",
        "folder": "mo-phatt",
        "name": "E-MU Mo'Phatt",
        "type": "Urban Dance & Hip Hop Sound Module",
        "year": 2000,
        "sysex_hdr": "F0 18 0F",
        "sysex_cmd": "F0 18 0F 55 01 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "attack": 73, "decay": 75, "controller_a": 21, "controller_b": 22, "controller_c": 23, "controller_d": 24},
        "banks": [
            ("User Bank 0", 128, "User Editable Hip Hop & R&B Custom Patches"),
            ("Preset Bank 1 - Basses & Beats", 128, "Sub-Bass Bombs, 808 Booms & Gritty Hip Hop Drum Kits"),
            ("Preset Bank 2 - Keys & Leads", 128, "Lo-Fi Pianos, Vinyl Rhodes, Portamento Leads & Whistles"),
            ("Preset Bank 3 - Hits & Stabs", 128, "Brass Horn Sections, DJ Scratches, Vocal Hits & Chords")
        ]
    },
    {
        "mfg": "emu",
        "folder": "mp-7",
        "name": "E-MU MP-7 Command Station",
        "type": "Hip Hop Desktop Synthesizer & Sequencer",
        "year": 2001,
        "sysex_hdr": "F0 18 0F",
        "sysex_cmd": "F0 18 0F 55 03 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "attack": 73, "decay": 75, "knob_1": 21, "knob_2": 22, "knob_3": 23, "knob_4": 24},
        "banks": [
            ("User Bank 0", 128, "User Rhythm Kits & Master Command Sequences"),
            ("Preset Bank 1 - Urban Beats", 128, "East Coast Boom Bap & Dirty South Trap Drum Sets"),
            ("Preset Bank 2 - Synth Grooves", 128, "Synth Stabs, G-Funk Saws, Sub Waves & Acid Hooks"),
            ("Preset Bank 3 - Street Instruments", 128, "Guitars, Electric Pianos, Strings & Brass Ensembles")
        ]
    },
    {
        "mfg": "emu",
        "folder": "pk-6",
        "name": "E-MU PK-6 Proteus Keys",
        "type": "64-Voice Keyboard Workstation (Proteus 2000 ROM)",
        "year": 2001,
        "sysex_hdr": "F0 18 0F",
        "sysex_cmd": "F0 18 0F 55 04 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "attack": 73, "release": 72, "knob_1": 21, "knob_2": 22, "knob_3": 23, "knob_4": 24},
        "banks": [
            ("User Bank", 128, "User Performance Programs & Multitimbral Setups"),
            ("Preset Bank 1 - Keyboards & Acoustic", 128, "Grand Pianos, Rhodes, Clavs, Organs & Acoustic Guitars"),
            ("Preset Bank 2 - Orchestral & Woodwinds", 128, "Solo Flutes, Cellos, Brass Ensembles & String Sections"),
            ("Preset Bank 3 - Synths & Pads", 128, "Analog Brass, Poly Sweeps, Vocal Choirs & Synth Textures")
        ]
    },
    {
        "mfg": "emu",
        "folder": "mk-6",
        "name": "E-MU MK-6 Mo'Phatt Keys",
        "type": "64-Voice Hip Hop Synthesizer Keyboard",
        "year": 2001,
        "sysex_hdr": "F0 18 0F",
        "sysex_cmd": "F0 18 0F 55 05 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "attack": 73, "release": 72, "knob_1": 21, "knob_2": 22, "knob_3": 23, "knob_4": 24},
        "banks": [
            ("User Bank", 128, "User Urban Production Performance Patches"),
            ("Preset Bank 1 - Urban Bass & Drums", 128, "808 Sub-Bass, 909 Kick Stabs, Hip Hop Snares & Hats"),
            ("Preset Bank 2 - Urban Keys & Melodies", 128, "Rhodes Mark V, Wurly, Whistle Leads & G-Funk Portas"),
            ("Preset Bank 3 - Hits, Brass & Cuts", 128, "Orchestra Hits, Turntable Scratches & Horn Sections")
        ]
    },
    {
        "mfg": "emu",
        "folder": "procussion",
        "name": "E-MU Procussion",
        "type": "32-Voice 1U Percussion Sound Module",
        "year": 1991,
        "sysex_hdr": "F0 18 06",
        "sysex_cmd": "F0 18 06 01 [kit] F7",
        "cc_map": {"pitch": 16, "pitch_env": 17, "decay": 75, "filter_cutoff": 74, "velocity_response": 20, "pan": 10},
        "banks": [
            ("Factory Kits Bank 1", 64, "Acoustic Rock, Jazz, Funk & Studio Drum Kits"),
            ("Factory Kits Bank 2", 64, "Latin, World, Orchestral & Electronic Percussion Kits")
        ]
    },

    # ==========================================
    # WALDORF
    # ==========================================
    {
        "mfg": "waldorf",
        "folder": "micro-q",
        "name": "Waldorf Micro Q",
        "type": "25-Voice Virtual Analog Rack Synthesizer",
        "year": 2000,
        "sysex_hdr": "F0 3E 0E",
        "sysex_cmd": "F0 3E 0E 00 00 [bank] [prog] F7",
        "cc_map": {"cutoff_1": 74, "resonance_1": 71, "cutoff_2": 72, "pulse_width": 70, "lfo_1_speed": 76, "lfo_1_depth": 77, "env_attack": 73, "env_decay": 75},
        "banks": [
            ("Bank A - Leads & Basses", 100, "Aggressive VA Saws, Sub Basses & Acid Resonance Leads"),
            ("Bank B - Pads & Polys", 100, "Lush Wavetable Sweeps, Moving Strings & Shimmering Pads"),
            ("Bank C - Arps & Sequences", 100, "Sync'd Step Arpeggiations, Drum Kits & Sound FX")
        ]
    },
    {
        "mfg": "waldorf",
        "folder": "microwave-2",
        "name": "Waldorf Microwave II",
        "type": "DSP Wavetable Synthesizer Module",
        "year": 1997,
        "sysex_hdr": "F0 3E 0E",
        "sysex_cmd": "F0 3E 0E 00 01 [bank] [prog] F7",
        "cc_map": {"wavetable": 70, "wave_position": 71, "filter_cutoff": 74, "filter_res": 72, "env_decay": 75, "env_attack": 73, "lfo_speed": 76},
        "banks": [
            ("Bank A - Classic Wavetable", 128, "Resonant Digital Sweeps, Bell Tines & PPG Heritage Tables"),
            ("Bank B - Modern DSP Textures", 128, "Complex Algorithmic Modulations, Evolving Drones & Leads")
        ]
    },
    {
        "mfg": "waldorf",
        "folder": "stvc",
        "name": "Waldorf STVC",
        "type": "String Synthesizer & 16-Band Vocoder Keyboard",
        "year": 2019,
        "sysex_hdr": "F0 3E 15",
        "sysex_cmd": "F0 3E 15 00 01 [prog] F7",
        "cc_map": {"registration": 70, "ensemble_rate": 71, "solo_cutoff": 74, "solo_resonance": 72, "vocoder_carrier": 75, "reverb_send": 91, "chorus_send": 93},
        "banks": [
            ("String Machine Presets", 64, "Lush 70s Solina Ensembles, Brass Strings & Velvet Pads"),
            ("16-Band Vocoder & Solo", 64, "Robotic Formant Vocoders, Carrier Choirs & Solo Leads")
        ]
    },

    # ==========================================
    # ALESIS
    # ==========================================
    {
        "mfg": "alesis",
        "folder": "fusion",
        "name": "Alesis Fusion 6HD / 8HD",
        "type": "Multi-Engine Workstation (VA, FM, Sample, Physical)",
        "year": 2005,
        "sysex_hdr": "F0 00 00 0E 15",
        "sysex_cmd": "F0 00 00 0E 15 01 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "mod_wheel": 1, "knob_1": 16, "knob_2": 17, "knob_3": 18, "knob_4": 19, "reverb_send": 91},
        "banks": [
            ("Preset Bank A - Holy Grail Piano & Keys", 128, "Grand Pianos, Rhodes, Wurlitzers & Organs"),
            ("Preset Bank B - Synthesizer VA & FM", 128, "Virtual Analog Leads, 6-Op FM Timbres & Basses"),
            ("Preset Bank C - Physical Modeling & World", 128, "Wind, Reed, Plucked String & Acoustic Resonators"),
            ("Preset Bank D - Drums & Complex Arps", 128, "Multitrack Drum Kits, Motion Pads & Step Sequences")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "s4",
        "name": "Alesis S4 Sound Module",
        "type": "64-Voice 1U Rackmount QuadraSynth",
        "year": 1993,
        "sysex_hdr": "F0 00 00 0E 0A",
        "sysex_cmd": "F0 00 00 0E 0A 01 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16, "controller_b": 17},
        "banks": [
            ("User Bank", 128, "User Editable Multi-Timbral Programs"),
            ("Preset Bank 1 - Pianos & Keys", 128, "Acoustic Grand, Harpsichords, Electric Pianos & Organs"),
            ("Preset Bank 2 - Orchestral & Strings", 128, "String Ensembles, Solo Violins, French Horns & Brass"),
            ("Preset Bank 3 - Synths, Pads & Drums", 128, "Analog Saws, Ambient Sweeps, Drums & FX Hits")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs6",
        "name": "Alesis QS6",
        "type": "64-Voice 61-Key Synthesizer",
        "year": 1996,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Flagship Pianos, Organs & Classic Keyboards"),
            ("Preset Bank 2", 128, "Orchestral Strings, Woodwinds & Brass Ensembles"),
            ("Preset Bank 3", 128, "Vintage Analog Leads, Pads & Modular Textures"),
            ("Preset Bank 4", 128, "Rhythm Kits, Ethnic Instruments & Sound Effects")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs7",
        "name": "Alesis QS7",
        "type": "64-Voice 76-Key Semi-Weighted Synthesizer",
        "year": 1996,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Concert Grands, Stage Rhodes & Tonewheel Organs"),
            ("Preset Bank 2", 128, "Strings, Orchestral Woodwinds & Brass Sections"),
            ("Preset Bank 3", 128, "Modern Electronic Leads, Basses & Evolving Sweeps"),
            ("Preset Bank 4", 128, "Studio Drum Kits, Percussion & Ambient Effects")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs8",
        "name": "Alesis QS8",
        "type": "64-Voice 88-Key Hammer Action Synthesizer",
        "year": 1996,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Concert Grand Pianos & Classic Stage Keyboards"),
            ("Preset Bank 2", 128, "Symphonic Strings, Solo Reeds & Horn Sections"),
            ("Preset Bank 3", 128, "Polyphonic Synth Sweeps, Warm Pads & Basses"),
            ("Preset Bank 4", 128, "World Percussion, Drum Kits & Cinematic Textures")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs6-1",
        "name": "Alesis QS6.1",
        "type": "64-Voice 61-Key Synthesizer (Enhanced Sliders & LCD)",
        "year": 1999,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Enhanced Acoustic Grands & Stage Rhodes"),
            ("Preset Bank 2", 128, "Lush Ensembles, Solo Violins & Brass Stacks"),
            ("Preset Bank 3", 128, "Contemporary Pop & Electronica Synth Leads"),
            ("Preset Bank 4", 128, "Alesis Signature Rhythm Kits & Sound Effects")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs7-1",
        "name": "Alesis QS7.1",
        "type": "64-Voice 76-Key Synthesizer (Enhanced Sliders & LCD)",
        "year": 1999,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Concert Acoustic Grands & Electric Pianos"),
            ("Preset Bank 2", 128, "Cinematic Strings, Woodwinds & French Horns"),
            ("Preset Bank 3", 128, "Analog Modular Emulations & Modern Synths"),
            ("Preset Bank 4", 128, "Studio Acoustic & Electronic Drum Kits")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qs8-1",
        "name": "Alesis QS8.1",
        "type": "64-Voice 88-Key Hammer Action Workstation",
        "year": 1999,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91},
        "banks": [
            ("User Bank", 128, "User Programmable Patches"),
            ("Preset Bank 1", 128, "Master Grand Pianos, Wurlys & B3 Drawbars"),
            ("Preset Bank 2", 128, "Full Symphonic Orchestra & Choral Ensembles"),
            ("Preset Bank 3", 128, "Fat Analog Basses, Lead Synths & Pads"),
            ("Preset Bank 4", 128, "Alesis Drum Kits, Grooves & Soundscapes")
        ]
    },
    {
        "mfg": "alesis",
        "folder": "qsr",
        "name": "Alesis QSR",
        "type": "64-Voice 1U Rackmount Synthesizer Module",
        "year": 1996,
        "sysex_hdr": "F0 00 00 0E 0E",
        "sysex_cmd": "F0 00 00 0E 0E 05 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "controller_a": 16},
        "banks": [
            ("User Bank", 128, "User Editable Multi-Timbral Setups"),
            ("Preset Bank 1", 128, "QS Acoustic Grands, Rhodes & Organ Drawbars"),
            ("Preset Bank 2", 128, "Orchestral Strings, Horns & Solo Instruments"),
            ("Preset Bank 3", 128, "Analog Synth Leads, Resonant Sweeps & Pads"),
            ("Preset Bank 4", 128, "General Percussion, Kits & Special FX")
        ]
    },

    # ==========================================
    # CRUMAR
    # ==========================================
    {
        "mfg": "crumar",
        "folder": "bit-one",
        "name": "Crumar Bit One",
        "type": "6-Voice Polyphonic Analog Synthesizer (SSM Filters)",
        "year": 1984,
        "sysex_hdr": "F0 27 00",
        "sysex_cmd": "F0 27 00 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco1_shape": 20, "dco2_shape": 21, "env_decay": 75, "env_release": 72},
        "banks": [
            ("Factory Programs", 63, "Classic Italian Analog Brass, Rich Strings & Resonant Basses")
        ]
    },
    {
        "mfg": "crumar",
        "folder": "bit-01",
        "name": "Crumar Bit 01",
        "type": "6-Voice Rackmount Analog Synthesizer",
        "year": 1985,
        "sysex_hdr": "F0 27 00",
        "sysex_cmd": "F0 27 00 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco1_shape": 20, "dco2_shape": 21, "env_decay": 75, "env_release": 72},
        "banks": [
            ("Factory Programs", 63, "Analog Rack Polys, Plucked Clavs, Sweeps & Basslines")
        ]
    },
    {
        "mfg": "crumar",
        "folder": "bit-99",
        "name": "Crumar Bit 99",
        "type": "6-Voice Analog Synthesizer (Velocity Sensitive & Splits)",
        "year": 1985,
        "sysex_hdr": "F0 27 00",
        "sysex_cmd": "F0 27 00 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco_detune": 22, "env_attack": 73, "env_decay": 75, "velocity_mod": 23},
        "banks": [
            ("Factory Programs", 75, "Dynamic Velocity Analog Keys, Layered Pads & Synth Basses")
        ]
    },

    # ==========================================
    # STUDIO ELECTRONICS
    # ==========================================
    {
        "mfg": "studio_electronics",
        "folder": "omega-8",
        "name": "Studio Electronics Omega 8",
        "type": "8-Voice Discrete Multi-Filter Analog Synthesizer",
        "year": 2000,
        "sysex_hdr": "F0 00 01 27 08",
        "sysex_cmd": "F0 00 01 27 08 01 [prog] F7",
        "cc_map": {"osc1_freq": 16, "osc2_detune": 17, "vcf_cutoff": 74, "vcf_resonance": 71, "vcf_env_decay": 75, "filter_type": 70, "glide_rate": 5},
        "banks": [
            ("Moog Ladder Voice Bank", 64, "Warm 24dB Minimoog Style Leads, Round Basses & Poly Stabs"),
            ("Oberheim SEM Voice Bank", 64, "Lush 12dB State Variable Sweeps, Airy Brass & Polys")
        ]
    },
    {
        "mfg": "studio_electronics",
        "folder": "code-8",
        "name": "Studio Electronics CODE 8",
        "type": "8-Voice Analog Synthesizer (Discrete Overdrive & Filters)",
        "year": 2008,
        "sysex_hdr": "F0 00 01 27 09",
        "sysex_cmd": "F0 00 01 27 09 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "drive_level": 70, "filter_select": 72, "env_attack": 73, "env_decay": 75, "lfo_rate": 76},
        "banks": [
            ("Discrete Saturated Polys", 64, "Overdriven Analog Poly Leads, Huge Unison Stabs & Pads"),
            ("Modular Filter Architectures", 64, "Multi-Filter Roland TB/ARP 2600 Emulations & Deep Drones")
        ]
    },

    # ==========================================
    # HISTORICAL GIANTS
    # ==========================================
    {
        "mfg": "ned",
        "folder": "synclavier-ii",
        "name": "New England Digital Synclavier II",
        "type": "Digital Additive & FM Synthesis Workstation",
        "year": 1980,
        "sysex_hdr": "F0 00 00 1B",
        "sysex_cmd": "F0 00 00 1B 01 [timbre] F7",
        "cc_map": {"timbral_volume": 7, "harmonic_decay": 75, "mod_index": 1, "fm_depth": 71, "lfo_rate": 76, "brightness": 74},
        "banks": [
            ("Timbre Bank 1 - Iconic Additive Timbres", 64, "Famous Michael Jackson / Frank Zappa Bells, Chimes & Hits"),
            ("Timbre Bank 2 - FM Strings & Brass", 64, "Crisp Digital FM Guitars, Plucks, Brass & Sci-Fi Effects")
        ]
    },
    {
        "mfg": "digital_keyboards",
        "folder": "synergy",
        "name": "Digital Keyboards Synergy",
        "type": "32-Oscillator Additive & FM Synthesizer",
        "year": 1982,
        "sysex_hdr": "F0 2B 01",
        "sysex_cmd": "F0 2B 01 02 [cart] [prog] F7",
        "cc_map": {"brightness": 74, "envelope_speed": 75, "vibrato_depth": 1, "chorus_rate": 76, "master_volume": 7},
        "banks": [
            ("Wendy Carlos Cartridge 1", 24, "Microtonal Tunings, Acoustic Orchestral Resonators & Bells"),
            ("Wendy Carlos Cartridge 2", 24, "Harmonic Flutes, Harps, Reed Instruments & Solo Horns"),
            ("Factory Cartridge A", 24, "Dynamic Additive Organs, Polyphonic Keys & Electric Basses"),
            ("Factory Cartridge B", 24, "Futuristic Sweeps, Space Chimes, Brass Stabs & Percussion")
        ]
    },

    # ==========================================
    # AKAI PROFESSIONAL
    # ==========================================
    {
        "mfg": "akai",
        "folder": "vx90",
        "name": "Akai VX90",
        "type": "6-Voice Analog Synthesizer Module (CEM 3394)",
        "year": 1986,
        "sysex_hdr": "F0 47 00 14",
        "sysex_cmd": "F0 47 00 14 01 [prog] F7",
        "cc_map": {"vco_freq": 16, "pulse_width": 70, "vcf_cutoff": 74, "vcf_resonance": 71, "vcf_env_depth": 72, "vca_decay": 75},
        "banks": [
            ("Factory Programs Bank", 100, "Vintage CEM Analog Poly Leads, Fat Brass, Basses & FX")
        ]
    },
    {
        "mfg": "akai",
        "folder": "timbre-wolf",
        "name": "Akai Timbre Wolf",
        "type": "4-Voice Discrete Analog Synthesizer",
        "year": 2014,
        "sysex_hdr": "F0 47 00 32",
        "sysex_cmd": "F0 47 00 32 01 [pattern] F7",
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "env_amount": 72, "decay": 75, "tuning": 16, "voice_mode": 70},
        "banks": [
            ("Factory Analog Presets & Patterns", 64, "4-Voice Poly Sequences, Unison Acid Basses & Round Leads")
        ]
    },
    {
        "mfg": "akai",
        "folder": "rhythm-wolf",
        "name": "Akai Rhythm Wolf",
        "type": "Analog Drum Machine & Bass Synthesizer",
        "year": 2014,
        "sysex_hdr": "F0 47 00 31",
        "sysex_cmd": "F0 47 00 31 01 [kit] F7",
        "cc_map": {"bass_cutoff": 74, "bass_resonance": 71, "howl_overdrive": 70, "snare_tune": 17, "kick_tune": 16, "hat_decay": 75},
        "banks": [
            ("Factory Drum Kits & Sequences", 64, "Analog Bass Drums, Snappy Snares, Open/Closed Hats & Howl Bass")
        ]
    }
]

def build_device(dev):
    mfg_dir = os.path.join(DEVICES_DIR, dev["mfg"])
    dev_dir = os.path.join(mfg_dir, dev["folder"])
    os.makedirs(dev_dir, exist_ok=True)
    
    banks_meta = []
    for bname, count, desc in dev["banks"]:
        banks_meta.append({
            "name": bname,
            "count": count,
            "description": desc
        })
        
    profile = {
        "manufacturer": dev["name"].split()[0] if not dev["mfg"] in ["studio_electronics", "digital_keyboards", "ned"] else ("Studio Electronics" if dev["mfg"] == "studio_electronics" else ("Digital Keyboards" if dev["mfg"] == "digital_keyboards" else "New England Digital")),
        "model": dev["name"],
        "type": dev["type"],
        "year": dev["year"],
        "midi": {
            "channels": 16,
            "cc_map": dev["cc_map"]
        },
        "sysex": {
            "header": dev["sysex_hdr"],
            "device_id_byte": 2,
            "commands": {
                "request_preset": dev["sysex_cmd"]
            }
        },
        "banks": banks_meta
    }
    
    with open(os.path.join(dev_dir, "profile.yaml"), "w") as f:
        yaml.dump(profile, f, sort_keys=False, default_flow_style=False)
        
    presets = []
    preset_num = 1
    
    for bname, count, desc in dev["banks"]:
        for i in range(1, count + 1):
            short_model = dev["name"].split("/")[0].strip()
            for prefix in ["Elektron", "Ensoniq", "E-MU", "Waldorf", "Alesis", "Crumar", "Studio Electronics", "New England Digital", "Digital Keyboards", "Akai"]:
                short_model = short_model.replace(prefix, "").strip()
                
            pname = f"{short_model} {bname} {i:02d}".strip()
            pname = " ".join(pname.split())
            
            idx_hex = f"{(i-1)%128:02X}"
            bank_idx = f"{(preset_num-1)//128:02X}"
            sysex = f"{dev['sysex_hdr']} {bank_idx} {idx_hex} 00 7F F7"
            
            presets.append({
                "number": preset_num,
                "name": pname,
                "bank": bname,
                "category": desc,
                "tags": [
                    dev["mfg"].replace("_", " "),
                    dev["folder"].replace("-", " "),
                    desc.lower()
                ],
                "sysex_dump": sysex
            })
            preset_num += 1
            
    with open(os.path.join(dev_dir, "factory_presets.json"), "w") as f:
        json.dump(presets, f, indent=2)
        
    return len(presets)

def main():
    total_patches = 0
    print(f"Building {len(WAVE28_MODELS)} Wave 28 Instruments...\n")
    for dev in WAVE28_MODELS:
        n = build_device(dev)
        total_patches += n
        print(f"  + {dev['name']:36} ({dev['year']}) -> {n:4d} patches in {len(dev['banks'])} banks")
        
    print(f"\nComplete! {len(WAVE28_MODELS)} Wave 28 instruments created with {total_patches:,} patches.")

if __name__ == "__main__":
    main()
