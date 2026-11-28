#!/usr/bin/env python3
"""
OmniPatch Wave 23 Builder: Retrofits, Cult Classics, Controllers & Studio Systems
Adds 46 instruments, retrofits, and processors from the hardware synthesizer catalog:
- Tubbutec: Juno-66, SH-1oh1
- Vecoven: Super JX 4.x
- Encore: OB-Xa
- Europa: Jupiter 6
- KiwiTechnics: Kiwi-1000, Kiwi-8P, Kiwi-SuperJX
- Yamaha: VL7 V2, S70XS, WF192XG
- Creative Labs: Wave Blaster
- OTO Machines: Der OTO
- Hohner: HS-2
- Kawai: XS-1, RV-4
- E-MU Systems: Launch Pad
- Fender: B-DEC 30
- Dynacord: Add-One
- Roland: SRV-3030, TD-7, TD-5, SPD-11, SPD-8, Pro-E, RAP-10, SC-50, SCC-1, VC-1
- Korg: A4-Bass, i4S, i5S, TR-76
- DigiTech: GFX-1
- Line 6: Floor POD Plus, Guitar POD V.2
- Vintage Revolution: PedalPro
- Doepfer: Drehbank, Pocket C, Pocket D
- Peavey: PC-1600, PC-1600x
- Kenton: Control Freak
- Akai: DP88
- Oberheim: Cyclone
- JLCooper: Synapse
- Quasimidi: Turbo-Volcon
- Access Music: Virus Rack XL
- Novation: KS4
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ HARDWARE RETROFITS ------------------
    {
        "m_dir": "tubbutec",
        "model_dir": "juno-66",
        "manufacturer": "Tubbutec",
        "model": "Juno-66",
        "type": "Hardware MIDI Retrofit for Roland Juno-6 / 60",
        "year": 2014,
        "cc_map": {"filter_cutoff": 74, "portamento_time": 5, "lfo_rate": 19, "dco_detune": 94, "bender": 1, "chord_memory": 85},
        "sysex_header": "F0 00 21 23 01",
        "req_cmd": "F0 00 21 23 01 01 00 F7",
        "banks": [
            ("Preset Bank", "RAM", 64, "Juno-60 Enhanced Retrofit Patches", [f"Juno-66 Patch {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "tubbutec",
        "model_dir": "sh-1oh1",
        "manufacturer": "Tubbutec",
        "model": "SH-1oh1",
        "type": "Hardware MIDI & Sequencer Retrofit for Roland SH-101",
        "year": 2015,
        "cc_map": {"filter_cutoff": 74, "accent": 16, "envelope_decay": 72, "lfo_rate": 19, "seq_clock": 86},
        "sysex_header": "F0 00 21 23 02",
        "req_cmd": "F0 00 21 23 02 01 00 F7",
        "banks": [
            ("Sequence Bank", "RAM", 64, "SH-101 Enhanced Motion Sequences", [f"SH-1oh1 Seq {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "vecoven",
        "model_dir": "super-jx",
        "manufacturer": "Vecoven",
        "model": "Super JX 4.x",
        "type": "Advanced PWM & Engine Upgrade for Roland JX-10 / MKS-70",
        "year": 2013,
        "cc_map": {"dco1_freq": 16, "dco2_freq": 17, "pwm_depth": 18, "vcf_cutoff": 74, "vcf_res": 71, "env_attack": 73, "env_decay": 72},
        "sysex_header": "F0 41 36 00 24 20",
        "req_cmd": "F0 41 36 00 24 10 00 00 F7",
        "banks": [
            ("Vecoven Flash Bank", "RAM", 100, "Super JX PWM & Dynamic Modulation Presets", [f"Vecoven Patch {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "encore",
        "model_dir": "ob-xa",
        "manufacturer": "Encore Electronics",
        "model": "Encore OB-Xa",
        "type": "120-Patch MIDI Retrofit for Oberheim OB-Xa",
        "year": 1999,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "lfo_speed": 19, "filter_env_amt": 16},
        "sysex_header": "F0 00 20 1A 01",
        "req_cmd": "F0 00 20 1A 01 01 00 F7",
        "banks": [
            ("Encore Bank A", "RAM", 60, "Classic OB-Xa Big Analog Brass & Pads", [f"Encore OB-Xa A-{i+1:02d}" for i in range(60)]),
            ("Encore Bank B", "RAM", 60, "Sync Leads & Matrix Resonant Sweeps", [f"Encore OB-Xa B-{i+1:02d}" for i in range(60)])
        ]
    },
    {
        "m_dir": "europa",
        "model_dir": "jupiter-6",
        "manufacturer": "Europa",
        "model": "Europa Jupiter 6",
        "type": "Full Engine & Arp MIDI Upgrade for Roland Jupiter-6",
        "year": 2007,
        "cc_map": {"vco1_range": 16, "vco2_range": 17, "cross_mod": 18, "vcf_cutoff": 74, "vcf_res": 71, "arp_clock": 85},
        "sysex_header": "F0 41 10 06 12",
        "req_cmd": "F0 41 10 06 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Europa Presets", "RAM", 96, "Jupiter-6 Discrete Dual-VCO Analog Programs", [f"Europa JP-6 {i+1:02d}" for i in range(96)])
        ]
    },
    {
        "m_dir": "kiwitechnics",
        "model_dir": "kiwi-1000",
        "manufacturer": "KiwiTechnics",
        "model": "Kiwi-1000",
        "type": "Hardware Engine Upgrade for Oberheim Matrix-1000",
        "year": 2017,
        "cc_map": {"dco1_freq": 16, "dco2_freq": 17, "vcf_cutoff": 74, "vcf_res": 71, "lfo1_rate": 19, "env1_attack": 73},
        "sysex_header": "F0 00 21 02 05",
        "req_cmd": "F0 00 21 02 05 01 00 F7",
        "banks": [
            ("Flash Bank 1", "RAM", 128, "Kiwi Matrix Analog Polyphonic", [f"Kiwi-1000 1-{i+1:03d}" for i in range(128)]),
            ("Flash Bank 2", "RAM", 128, "Dynamic Filter Sweeps & Sequences", [f"Kiwi-1000 2-{i+1:03d}" for i in range(128)]),
            ("Flash Bank 3", "RAM", 128, "Classic Oberheim Matrix Tones", [f"Kiwi-1000 3-{i+1:03d}" for i in range(128)]),
            ("Flash Bank 4", "RAM", 128, "Ambient Soundscapes & Arps", [f"Kiwi-1000 4-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "kiwitechnics",
        "model_dir": "kiwi-8p",
        "manufacturer": "KiwiTechnics",
        "model": "Kiwi-8P",
        "type": "Hardware Engine Upgrade for Roland JX-8P",
        "year": 2016,
        "cc_map": {"dco1_wave": 16, "dco2_wave": 17, "vcf_cutoff": 74, "vcf_res": 71, "lfo_rate": 19, "env1_attack": 73},
        "sysex_header": "F0 00 21 02 03",
        "req_cmd": "F0 00 21 02 03 01 00 F7",
        "banks": [
            ("Preset Bank 1", "RAM", 128, "Kiwi JX Analog Leads & Pads", [f"Kiwi-8P 1-{i+1:03d}" for i in range(128)]),
            ("Preset Bank 2", "RAM", 128, "Fast Poly Sequences & Basses", [f"Kiwi-8P 2-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "kiwitechnics",
        "model_dir": "kiwi-superjx",
        "manufacturer": "KiwiTechnics",
        "model": "Kiwi-SuperJX",
        "type": "Hardware Engine Upgrade for Roland JX-10 / MKS-70",
        "year": 2018,
        "cc_map": {"dco1_wave": 16, "dco2_wave": 17, "vcf_cutoff": 74, "vcf_res": 71, "lfo1_rate": 19, "env1_attack": 73},
        "sysex_header": "F0 00 21 02 04",
        "req_cmd": "F0 00 21 02 04 01 00 F7",
        "banks": [
            ("Kiwi SuperJX Bank 1", "RAM", 128, "12-Voice Dual DCO Warm Strings", [f"Kiwi SuperJX 1-{i+1:03d}" for i in range(128)]),
            ("Kiwi SuperJX Bank 2", "RAM", 128, "Analog Brass & Solos", [f"Kiwi SuperJX 2-{i+1:03d}" for i in range(128)]),
            ("Kiwi SuperJX Bank 3", "RAM", 128, "Deep Polyphonic Basses", [f"Kiwi SuperJX 3-{i+1:03d}" for i in range(128)]),
            ("Kiwi SuperJX Bank 4", "RAM", 128, "Motion Arpeggiations & Sweeps", [f"Kiwi SuperJX 4-{i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ SYNTHESIZERS & SOUND MODULES ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "vl7-v2",
        "manufacturer": "Yamaha",
        "model": "VL7 V2",
        "type": "Single-Element Virtual Acoustic Physical Modeling Synthesizer",
        "year": 1994,
        "cc_map": {"pressure": 2, "embouchure": 13, "tonguing": 14, "growl": 15, "throat": 16, "harmonics": 17, "damping": 18},
        "sysex_header": "F0 43 10 3B",
        "req_cmd": "F0 43 20 3B 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "Physical Wind, Reed & Brass Modeling", [f"VL7 Voice 1-{i+1:02d}" for i in range(64)]),
            ("Preset Bank 2", "ROM", 64, "Acoustic String & Hybrid Resonant Models", [f"VL7 Voice 2-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "s70xs",
        "manufacturer": "Yamaha",
        "model": "S70XS",
        "type": "76-Key Balanced Hammer Stage Synthesizer",
        "year": 2009,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack": 73, "release": 72, "assign1": 16, "assign2": 17, "slider1": 18},
        "sysex_header": "F0 43 10 7F 0D",
        "req_cmd": "F0 43 10 7F 0D 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Natural S6 Grand Piano & Stage EPs", [f"S70XS Piano {i+1:03d}" for i in range(128)]),
            ("Preset Bank 2", "ROM", 128, "Motif XS Synthesis & Orchestral", [f"S70XS Motif {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "wf192xg",
        "manufacturer": "Yamaha",
        "model": "WF192XG",
        "type": "PCI Hardware XG Wavetable Soundcard Synthesizer",
        "year": 1997,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93, "variation_send": 94},
        "sysex_header": "F0 43 10 4C",
        "req_cmd": "F0 43 10 4C 00 00 00 F7",
        "banks": [
            ("XG Wavetable Bank", "ROM", 128, "Hardware PCI XG Instrument Collection", [f"WF192XG Sound {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "creative",
        "model_dir": "wave-blaster",
        "manufacturer": "Creative Labs",
        "model": "Wave Blaster",
        "type": "General MIDI Wavetable Daughterboard",
        "year": 1992,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 18 01",
        "req_cmd": "F0 18 01 00 01 00 F7",
        "banks": [
            ("General MIDI Presets", "ROM", 128, "Classic E-MU Proteus GM Sample ROM", [f"Wave Blaster GM {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "oto_machines",
        "model_dir": "der-oto",
        "manufacturer": "OTO Machines",
        "model": "Der OTO",
        "type": "All-Analog Monophonic Desktop Synthesizer",
        "year": 2012,
        "cc_map": {"cutoff": 74, "resonance": 71, "env_attack": 73, "env_decay": 72, "vco_shape": 16, "sub_osc": 17},
        "sysex_header": "F0 00 20 7B 01",
        "req_cmd": "F0 00 20 7B 01 01 00 F7",
        "banks": [
            ("Preset Memory", "RAM", 32, "Gritty Analog Basses, Leads & Percussion", [f"Der OTO Patch {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "hohner",
        "model_dir": "hs-2",
        "manufacturer": "Hohner",
        "model": "HS-2",
        "type": "16-Bit Digital Sampling Synthesizer",
        "year": 1988,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "level": 7, "pan": 10},
        "sysex_header": "F0 27 01 00",
        "req_cmd": "F0 27 01 00 01 00 F7",
        "banks": [
            ("Factory Library Bank", "ROM", 64, "16-Bit Resonant VCF Sampler Presets", [f"HS-2 Voice {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "kawai",
        "model_dir": "xs-1",
        "manufacturer": "Kawai",
        "model": "XS-1",
        "type": "Half-Rack General MIDI Sound Module",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 40 10 00 00",
        "req_cmd": "F0 40 10 00 00 01 F7",
        "banks": [
            ("GM Presets", "ROM", 128, "16-Bit PCM General MIDI Acoustic & Synth Instruments", [f"XS-1 Instrument {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "kawai",
        "model_dir": "rv-4",
        "manufacturer": "Kawai",
        "model": "RV-4",
        "type": "4-Channel 20-Bit Digital Multi-Processor",
        "year": 1996,
        "cc_map": {"mix": 91, "reverb_time": 16, "predelay": 17, "damping": 18, "er_level": 19},
        "sysex_header": "F0 40 10 00 04",
        "req_cmd": "F0 40 10 00 04 01 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Quad Independent Studio Reverb & Effects", [f"RV-4 Program {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "launch-pad",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Launch Pad",
        "type": "MIDI Controller & Performance Interface",
        "year": 1996,
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "data_wheel": 6},
        "sysex_header": "F0 18 06",
        "req_cmd": "F0 18 06 00 01 00 F7",
        "banks": [
            ("Factory Templates", "RAM", 64, "E-MU Synthesizer & Sampler Remote Maps", [f"Launch Pad Template {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "fender",
        "model_dir": "b-dec-30",
        "manufacturer": "Fender",
        "model": "B-DEC 30",
        "type": "Bass Digital Entertainment Center",
        "year": 2005,
        "cc_map": {"drive": 16, "bass": 17, "middle": 18, "treble": 19, "fx_level": 91},
        "sysex_header": "F0 00 01 38 02",
        "req_cmd": "F0 00 01 38 02 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 50, "Bass Amp Modeling & Backing Groove Styles", [f"B-DEC Style {i+1:02d}" for i in range(50)])
        ]
    },
    {
        "m_dir": "dynacord",
        "model_dir": "add-one",
        "manufacturer": "Dynacord",
        "model": "Add-One",
        "type": "Advanced Digital Drums with Analog CEM Filters",
        "year": 1986,
        "cc_map": {"tune": 16, "decay": 17, "vcf_cutoff": 74, "vcf_res": 71, "bend": 18, "pan": 10},
        "sysex_header": "F0 00 01 22 01",
        "req_cmd": "F0 00 01 22 01 01 00 F7",
        "banks": [
            ("Drum Kits Bank 1", "ROM", 64, "Dynamic 12-Bit Analog Filtered Kits", [f"Add-One Kit 1-{i+1:02d}" for i in range(64)]),
            ("Drum Kits Bank 2", "ROM", 64, "Electronic Punch & Industrial Percussion", [f"Add-One Kit 2-{i+1:02d}" for i in range(64)])
        ]
    },

    # ------------------ ROLAND STUDIO & PERCUSSION ------------------
    {
        "m_dir": "roland",
        "model_dir": "srv-3030",
        "manufacturer": "Roland",
        "model": "SRV-3030",
        "type": "24-Bit 3D Spatial Digital Reverb Processor",
        "year": 1999,
        "cc_map": {"rev_time": 16, "pre_delay": 17, "density": 18, "rss_azimuth": 19, "rss_elevation": 20, "mix_balance": 91},
        "sysex_header": "F0 41 10 00 13 12",
        "req_cmd": "F0 41 10 00 13 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank", "ROM", 100, "High-Density RSS 3D Reverb Spaces & Plates", [f"SRV-3030 Space {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "td-7",
        "manufacturer": "Roland",
        "model": "TD-7",
        "type": "Electronic Percussion Sound Module",
        "year": 1992,
        "cc_map": {"pitch": 16, "decay": 17, "reverb_level": 91, "chorus_level": 93, "flange": 94},
        "sysex_header": "F0 41 10 4E 12",
        "req_cmd": "F0 41 10 4E 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Kits", "ROM", 32, "Acoustic, Rock & Electronic Percussion Kits", [f"TD-7 Kit {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "td-5",
        "manufacturer": "Roland",
        "model": "TD-5",
        "type": "V-Drums Percussion Brain",
        "year": 1994,
        "cc_map": {"tune": 16, "pan": 10, "reverb_send": 91},
        "sysex_header": "F0 41 10 63 12",
        "req_cmd": "F0 41 10 63 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Kits", "ROM", 32, "Classic TD-5 Studio & Stage Kits", [f"TD-5 Kit {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "spd-11",
        "manufacturer": "Roland",
        "model": "SPD-11",
        "type": "Total Percussion Pad",
        "year": 1993,
        "cc_map": {"pitch": 16, "decay": 17, "reverb_level": 91, "pan": 10},
        "sysex_header": "F0 41 10 54 12",
        "req_cmd": "F0 41 10 54 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Patches", "ROM", 64, "Electronic Multi-Pad Percussion Kits", [f"SPD-11 Patch {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "spd-8",
        "manufacturer": "Roland",
        "model": "SPD-8",
        "type": "Total Percussion Controller",
        "year": 1990,
        "cc_map": {"pitch": 16, "decay": 17, "pan": 10},
        "sysex_header": "F0 41 10 39 12",
        "req_cmd": "F0 41 10 39 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Patches", "ROM", 32, "Percussion Controller Sound Sets", [f"SPD-8 Patch {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "pro-e",
        "manufacturer": "Roland",
        "model": "Pro-E",
        "type": "Intelligent Arranger Module",
        "year": 1988,
        "cc_map": {"volume": 7, "pan": 10, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 2B 12",
        "req_cmd": "F0 41 10 2B 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Music Styles", "ROM", 64, "Interactive Music Accompaniment Styles", [f"Pro-E Style {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "rap-10",
        "manufacturer": "Roland",
        "model": "RAP-10",
        "type": "Roland Audio Production Soundcard",
        "year": 1993,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "reverb_level": 91, "chorus_level": 93},
        "sysex_header": "F0 41 10 42 12",
        "req_cmd": "F0 41 10 42 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("General MIDI Bank", "ROM", 128, "DSP Enhanced General MIDI Presets", [f"RAP-10 GM {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "sc-50",
        "manufacturer": "Roland",
        "model": "SC-50",
        "type": "Sound Canvas General MIDI / GS Module",
        "year": 1993,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 42 12",
        "req_cmd": "F0 41 10 42 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("GS Capital Tones", "ROM", 128, "Roland GS Acoustic & Synth Voices", [f"SC-50 Tone {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "scc-1",
        "manufacturer": "Roland",
        "model": "SCC-1",
        "type": "GS Sound Canvas ISA Synthesizer Card",
        "year": 1992,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 41 10 42 12",
        "req_cmd": "F0 41 10 42 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("GS Presets", "ROM", 128, "Hardware ISA Sound Canvas Tones", [f"SCC-1 Preset {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "vc-1",
        "manufacturer": "Roland",
        "model": "VC-1",
        "type": "D-50 V-Card for V-Synth & VariOS",
        "year": 2004,
        "cc_map": {"tvf_cutoff": 74, "tvf_resonance": 71, "lfo_rate": 19, "chase_play": 80, "reverb_balance": 91},
        "sysex_header": "F0 41 10 14 12",
        "req_cmd": "F0 41 10 14 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("D-50 Factory Bank", "ROM", 64, "Original Authentic Roland D-50 Presets", [f"VC-1 D-50 Sound {i+1:02d}" for i in range(64)])
        ]
    },

    # ------------------ KORG ARRANGERS & WORKSTATIONS ------------------
    {
        "m_dir": "korg",
        "model_dir": "a4-bass",
        "manufacturer": "Korg",
        "model": "A4 Bass",
        "type": "Bass Multi-Effects Processor",
        "year": 1993,
        "cc_map": {"drive": 16, "tone": 17, "level": 18, "compressor": 19, "chorus_depth": 93, "delay_time": 20},
        "sysex_header": "F0 42 30 43",
        "req_cmd": "F0 42 30 43 10 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 30, "Punchy Funk, Slap & Tube Overdrive", [f"A4 Bass Funk {i+1:02d}" for i in range(30)]),
            ("Preset Bank 2", "ROM", 30, "Smooth Chorused & Synth Bass Models", [f"A4 Bass Synth {i+1:02d}" for i in range(30)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "i4s",
        "manufacturer": "Korg",
        "model": "i4S",
        "type": "Interactive Music Workstation",
        "year": 1994,
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 42 30 3E",
        "req_cmd": "F0 42 30 3E 10 00 00 F7",
        "banks": [
            ("Bank A Programs", "ROM", 64, "Interactive AI2 Arranger Programs", [f"i4S Program A-{i+1:02d}" for i in range(64)]),
            ("Bank B Programs", "ROM", 64, "Orchestral & Synth Solo Leads", [f"i4S Program B-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "i5s",
        "manufacturer": "Korg",
        "model": "i5S",
        "type": "Interactive Music Workstation",
        "year": 1996,
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 42 30 4B",
        "req_cmd": "F0 42 30 4B 10 00 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 128, "Expanded AI2 Arranger Sound Collection", [f"i5S Program {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "tr-76",
        "manufacturer": "Korg",
        "model": "TR-76",
        "type": "76-Key HI Synthesis Music Workstation",
        "year": 2006,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "eg_intensity": 79, "eg_release": 72, "knob_a": 16, "knob_b": 17},
        "sysex_header": "F0 42 30 76",
        "req_cmd": "F0 42 30 76 10 00 00 F7",
        "banks": [
            ("Bank A Programs", "ROM", 128, "HI Workstation 76-Key Programs", [f"TR-76 Program A-{i+1:03d}" for i in range(128)]),
            ("Bank B Programs", "ROM", 128, "Synthesizer & Cinematic Ensembles", [f"TR-76 Program B-{i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ GUITAR & FLOOR PROCESSORS ------------------
    {
        "m_dir": "digitech",
        "model_dir": "gfx-1",
        "manufacturer": "DigiTech",
        "model": "GFX-1",
        "type": "Twin Tube Guitar Processor",
        "year": 1995,
        "cc_map": {"gain": 16, "master": 17, "bass": 18, "mid": 19, "treble": 20, "mix": 91},
        "sysex_header": "F0 00 00 1B 07",
        "req_cmd": "F0 00 00 1B 07 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Dual 12AX7 Vacuum Tube Guitar Tones", [f"GFX-1 Tone {i+1:02d}" for i in range(99)])
        ]
    },
    {
        "m_dir": "line6",
        "model_dir": "floor-pod-plus",
        "manufacturer": "Line 6",
        "model": "Floor POD Plus",
        "type": "Floor Amp Modeling & Multi-Effects",
        "year": 2007,
        "cc_map": {"drive": 16, "bass": 17, "mid": 18, "treble": 19, "delay_level": 91, "mod_speed": 1},
        "sysex_header": "F0 00 01 0C 05",
        "req_cmd": "F0 00 01 0C 05 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 124, "Studio Amp Modeling & Stompbox Presets", [f"Floor POD Plus {i+1:03d}" for i in range(124)])
        ]
    },
    {
        "m_dir": "line6",
        "model_dir": "guitar-pod-v2",
        "manufacturer": "Line 6",
        "model": "POD (V.2)",
        "type": "Digital Guitar Amp Modeler",
        "year": 2000,
        "cc_map": {"drive": 16, "bass": 17, "mid": 18, "treble": 19, "chan_vol": 7, "reverb": 91},
        "sysex_header": "F0 00 01 0C 01",
        "req_cmd": "F0 00 01 0C 01 01 00 F7",
        "banks": [
            ("Factory Channel Bank", "ROM", 36, "Classic POD 2.0 Amp Modeling Presets", [f"POD V2 Preset {i+1:02d}" for i in range(36)])
        ]
    },
    {
        "m_dir": "vintagerevolution",
        "model_dir": "pedalpro",
        "manufacturer": "Vintage Revolution",
        "model": "PedalPro",
        "type": "True Analog Programmable Multi-Effects System",
        "year": 2011,
        "cc_map": {"preamp_gain": 16, "analog_chorus": 93, "analog_delay": 91, "phaser_depth": 17, "tremolo_depth": 18},
        "sysex_header": "F0 00 20 7C 01",
        "req_cmd": "F0 00 20 7C 01 01 00 F7",
        "banks": [
            ("Factory Presets", "RAM", 64, "Pure Analog Guitar Signal Path Presets", [f"PedalPro Preset {i+1:02d}" for i in range(64)])
        ]
    },

    # ------------------ CONTROLLERS & PATCHBAYS ------------------
    {
        "m_dir": "doepfer",
        "model_dir": "drehbank",
        "manufacturer": "Doepfer",
        "model": "Drehbank",
        "type": "64-Knob MIDI Rotary Controller Console",
        "year": 1998,
        "cc_map": {f"knob_{i+1}": i+1 for i in range(32)},
        "sysex_header": "F0 00 20 20 61",
        "req_cmd": "F0 00 20 20 61 01 00 F7",
        "banks": [
            ("Bank Presets", "RAM", 8, "Drehbank 64-Parameter Synth Control Maps", [f"Drehbank Map {i+1:02d}" for i in range(8)])
        ]
    },
    {
        "m_dir": "doepfer",
        "model_dir": "pocket-c",
        "manufacturer": "Doepfer",
        "model": "Pocket C",
        "type": "Pocket MIDI Rotary Controller",
        "year": 2000,
        "cc_map": {f"knob_{i+1}": i+1 for i in range(16)},
        "sysex_header": "F0 00 20 20 62",
        "req_cmd": "F0 00 20 20 62 01 00 F7",
        "banks": [
            ("Control Templates", "RAM", 16, "Pocket Control Profiles", [f"Pocket C Preset {i+1:02d}" for i in range(16)])
        ]
    },
    {
        "m_dir": "doepfer",
        "model_dir": "pocket-d",
        "manufacturer": "Doepfer",
        "model": "Pocket D",
        "type": "Pocket MIDI Fader Controller",
        "year": 2000,
        "cc_map": {f"fader_{i+1}": i+1 for i in range(16)},
        "sysex_header": "F0 00 20 20 63",
        "req_cmd": "F0 00 20 20 63 01 00 F7",
        "banks": [
            ("Fader Templates", "RAM", 16, "Pocket Drawbar & Fader Profiles", [f"Pocket D Preset {i+1:02d}" for i in range(16)])
        ]
    },
    {
        "m_dir": "peavey",
        "model_dir": "pc-1600",
        "manufacturer": "Peavey",
        "model": "PC-1600",
        "type": "Studio MIDI Fader Controller",
        "year": 1993,
        "cc_map": {f"fader_{i+1}": i+1 for i in range(16)},
        "sysex_header": "F0 00 00 1B 40",
        "req_cmd": "F0 00 00 1B 40 01 00 F7",
        "banks": [
            ("Preset Setups", "RAM", 50, "Hardware Synth SysEx & CC Fader Maps", [f"PC-1600 Setup {i+1:02d}" for i in range(50)])
        ]
    },
    {
        "m_dir": "peavey",
        "model_dir": "pc-1600x",
        "manufacturer": "Peavey",
        "model": "PC-1600x",
        "type": "High-Resolution Studio MIDI Fader Controller",
        "year": 1995,
        "cc_map": {f"fader_{i+1}": i+1 for i in range(16)},
        "sysex_header": "F0 00 00 1B 41",
        "req_cmd": "F0 00 00 1B 41 01 00 F7",
        "banks": [
            ("Preset Setups", "RAM", 50, "Studio Synthesizer Fader Maps", [f"PC-1600x Setup {i+1:02d}" for i in range(50)])
        ]
    },
    {
        "m_dir": "kenton",
        "model_dir": "control-freak",
        "manufacturer": "Kenton Electronics",
        "model": "Control Freak",
        "type": "Studio Fader MIDI Controller",
        "year": 1998,
        "cc_map": {f"slider_{i+1}": i+1 for i in range(16)},
        "sysex_header": "F0 00 20 13 01",
        "req_cmd": "F0 00 20 13 01 01 00 F7",
        "banks": [
            ("Profiles Bank", "RAM", 64, "Vintage Analog & Digital Hardware Maps", [f"Control Freak Profile {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "akai",
        "model_dir": "dp88",
        "manufacturer": "Akai Professional",
        "model": "DP88",
        "type": "Digital Audio Matrix Patchbay",
        "year": 1991,
        "cc_map": {"routing_preset": 32, "master_level": 7},
        "sysex_header": "F0 47 00 38",
        "req_cmd": "F0 47 00 38 01 00 F7",
        "banks": [
            ("Routing Memories", "RAM", 32, "Studio Audio Routing Configurations", [f"DP88 Route {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "oberheim",
        "model_dir": "cyclone",
        "manufacturer": "Oberheim",
        "model": "Cyclone",
        "type": "Interactive MIDI Arpeggiator & Performance Sequencer",
        "year": 1988,
        "cc_map": {"tempo": 16, "gate_time": 17, "velocity": 18, "mode": 19},
        "sysex_header": "F0 10 03 01",
        "req_cmd": "F0 10 03 01 01 00 F7",
        "banks": [
            ("Arp Setups", "RAM", 64, "Algorithmic Arpeggiations & Patterns", [f"Cyclone Setup {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "jlcooper",
        "model_dir": "synapse",
        "manufacturer": "JLCooper Electronics",
        "model": "Synapse",
        "type": "16x20 Studio MIDI Routing Matrix",
        "year": 1989,
        "cc_map": {"patch_select": 32},
        "sysex_header": "F0 15 01",
        "req_cmd": "F0 15 01 01 00 F7",
        "banks": [
            ("Patch Memories", "RAM", 64, "Studio MIDI Routing Configurations", [f"Synapse Setup {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "quasimidi",
        "model_dir": "turbo-volcon",
        "manufacturer": "Quasimidi",
        "model": "Turbo-Volcon",
        "type": "Synthesizer Programmer & Dynamic Controller",
        "year": 1996,
        "cc_map": {"cutoff": 74, "resonance": 71, "envelope": 73, "lfo": 19},
        "sysex_header": "F0 3F 00 03",
        "req_cmd": "F0 3F 00 03 01 00 F7",
        "banks": [
            ("Programmer Maps", "RAM", 32, "Quasimidi Sound Engine Mappings", [f"Turbo-Volcon Map {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "access",
        "model_dir": "virus-rack-xl",
        "manufacturer": "Access",
        "model": "Virus Rack XL",
        "type": "Dual-DSP Virtual Analog Rack Synthesizer",
        "year": 2002,
        "cc_map": {"filter_cutoff": 40, "resonance": 41, "osc1_shape": 33, "osc2_semitone": 35, "lfo1_rate": 20, "filter_env_decay": 46},
        "sysex_header": "F0 00 20 33 01 11",
        "req_cmd": "F0 00 20 33 01 11 10 00 00 F7",
        "banks": [
            ("Bank A", "RAM", 128, "Virus C-Series Trance Leads & Basses", [f"Rack XL A-{i+1:03d}" for i in range(128)]),
            ("Bank B", "RAM", 128, "Hypersaw Pads & Dual-Filter Sweeps", [f"Rack XL B-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "novation",
        "model_dir": "ks4",
        "manufacturer": "Novation",
        "model": "KS4",
        "type": "49-Key Liquid Analog Synthesizer",
        "year": 2002,
        "cc_map": {"filter_cutoff": 105, "resonance": 106, "osc1_semitone": 40, "osc2_semitone": 47, "lfo1_speed": 82, "env_attack": 73},
        "sysex_header": "F0 00 20 29 01 32",
        "req_cmd": "F0 00 20 29 01 32 01 00 F7",
        "banks": [
            ("Program Bank 1", "RAM", 100, "Liquid Virtual Analog Leads & Basses", [f"KS4 Program 1-{i+1:02d}" for i in range(100)]),
            ("Program Bank 2", "RAM", 100, "Hypersync Arpeggiators & Lush Vocoders", [f"KS4 Program 2-{i+1:02d}" for i in range(100)])
        ]
    }
]

def make_sysex(header: str, idx: int) -> str:
    h = header.strip()
    return f"{h} {idx:02X} 00 00 7F F7"

def build_all():
    base_dir = "devices"
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

    print(f"\nWave 23 Build Complete! {len(DEVICES)} new retrofits, cult classics & systems created.")

if __name__ == "__main__":
    build_all()
