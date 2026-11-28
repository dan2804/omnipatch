#!/usr/bin/env python3
"""
OmniPatch Wave 22 Builder: Flagships, Workstations, Samplers & Studio Racks
Adds 40 high-profile instruments from the Midi Quest 13 catalog:
- Roland: RS-5, RS-9, XP-10, XP-60, XV-88, JV-1000, VK-7, TR-6S, S-550, S-770, U-110, V-Synth XT
- Yamaha: SY55, TG55, TG100, TG300, YS100, YS200, SPX900, SW1000XG, P-100
- Korg: Nautilus, OASYS, TR-61, Volca Kick, SG-ProX, T1, T2, A4-Guitar
- E-MU Systems: Proteus FX, Proteus/1 XR, Proteus/2 XR, Sound Engine
- Ensoniq: KT-88, TS-12
- DigiTech: DSP-128, GSP-5, RP-10
- Access Music: Virus Indigo, Virus KB
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ ROLAND ------------------
    {
        "m_dir": "roland",
        "model_dir": "rs-5",
        "manufacturer": "Roland",
        "model": "RS-5",
        "type": "64-Voice Synthesizer",
        "year": 2001,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "reverb_send": 91, "chorus_send": 93, "pan": 10},
        "sysex_header": "F0 41 10 00 3D 12",
        "req_cmd": "F0 41 10 00 3D 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("User Bank", "RAM", 128, "User Performance Presets", [f"RS-5 User {i+1:03d}" for i in range(128)]),
            ("Preset Bank A", "ROM", 128, "Acoustic & Electric Keyboards", [f"RS-5 Preset {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "rs-9",
        "manufacturer": "Roland",
        "model": "RS-9",
        "type": "88-Key 64-Voice Synthesizer",
        "year": 2001,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "reverb_send": 91, "chorus_send": 93, "pan": 10},
        "sysex_header": "F0 41 10 00 3E 12",
        "req_cmd": "F0 41 10 00 3E 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("User Bank", "RAM", 128, "Weighted Stage Performance", [f"RS-9 Stage {i+1:03d}" for i in range(128)]),
            ("Preset Bank A", "ROM", 128, "Grand Pianos & Orchestral", [f"RS-9 Acoustic {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "xp-10",
        "manufacturer": "Roland",
        "model": "XP-10",
        "type": "Multitimbral Synthesizer",
        "year": 1995,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "reverb_level": 91, "chorus_level": 93, "portamento_time": 5},
        "sysex_header": "F0 41 10 77 12",
        "req_cmd": "F0 41 10 77 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank A", "ROM", 128, "Acoustic & Synth Tones", [f"XP-10 Tone A-{i+1:03d}" for i in range(128)]),
            ("Preset Bank B", "ROM", 128, "Pads & Textures", [f"XP-10 Tone B-{i+1:03d}" for i in range(128)]),
            ("User Bank", "RAM", 128, "User Performance Combinations", [f"XP-10 User {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "xp-60",
        "manufacturer": "Roland",
        "model": "XP-60",
        "type": "64-Voice Music Workstation",
        "year": 1998,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "efx_ctrl1": 12, "efx_ctrl2": 13, "mod_wheel": 1},
        "sysex_header": "F0 41 10 6A 12",
        "req_cmd": "F0 41 10 6A 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("User Patches", "RAM", 128, "User Custom Creations", [f"XP-60 User {i+1:03d}" for i in range(128)]),
            ("Preset Bank A", "ROM", 128, "Pop & Contemporary Instruments", [f"XP-60 Preset A-{i+1:03d}" for i in range(128)]),
            ("Preset Bank B", "ROM", 128, "Orchestral & Acoustic Realism", [f"XP-60 Preset B-{i+1:03d}" for i in range(128)]),
            ("Preset Bank C", "ROM", 128, "Vintage Synth Classics & Pads", [f"XP-60 Preset C-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "xv-88",
        "manufacturer": "Roland",
        "model": "XV-88",
        "type": "128-Voice Flagship Synthesizer",
        "year": 2000,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "matrix_ctrl1": 16, "matrix_ctrl2": 17, "matrix_ctrl3": 18, "matrix_ctrl4": 19},
        "sysex_header": "F0 41 10 00 10 12",
        "req_cmd": "F0 41 10 00 10 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("User Bank", "RAM", 128, "Custom XV-88 Programs", [f"XV-88 User {i+1:03d}" for i in range(128)]),
            ("Preset Bank A", "ROM", 128, "Concert Grand Pianos", [f"XV-88 Concert {i+1:03d}" for i in range(128)]),
            ("Preset Bank B", "ROM", 128, "Electric Pianos & Clavs", [f"XV-88 Keys {i+1:03d}" for i in range(128)]),
            ("Preset Bank C", "ROM", 128, "Lush Strings & Orchestral", [f"XV-88 Strings {i+1:03d}" for i in range(128)]),
            ("Preset Bank D", "ROM", 128, "Analog Brass & Solos", [f"XV-88 Brass {i+1:03d}" for i in range(128)]),
            ("Preset Bank E", "ROM", 128, "Wavetable & Synth Textures", [f"XV-88 Wavetable {i+1:03d}" for i in range(128)]),
            ("Preset Bank F", "ROM", 128, "Bass & Lead Synths", [f"XV-88 Lead {i+1:03d}" for i in range(128)]),
            ("Preset Bank G", "ROM", 128, "Pads & Soundscapes", [f"XV-88 Pad {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "jv-1000",
        "manufacturer": "Roland",
        "model": "JV-1000",
        "type": "76-Key Music Workstation",
        "year": 1993,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "tvf_envelope": 73, "tva_release": 72, "reverb_level": 91, "chorus_level": 93},
        "sysex_header": "F0 41 10 46 12",
        "req_cmd": "F0 41 10 46 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank A", "ROM", 64, "Super JV Acoustic Realism", [f"JV-1000 Acoustic {i+1:02d}" for i in range(64)]),
            ("Preset Bank B", "ROM", 64, "Warm Synthesizer Pads & Sweeps", [f"JV-1000 Pad {i+1:02d}" for i in range(64)]),
            ("Internal Bank", "RAM", 64, "Internal Production Performances", [f"JV-1000 Internal {i+1:02d}" for i in range(64)]),
            ("User Bank", "RAM", 64, "Custom Master Patches", [f"JV-1000 User {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "vk-7",
        "manufacturer": "Roland",
        "model": "VK-7",
        "type": "Virtual ToneWheel Combo Organ",
        "year": 1997,
        "cc_map": {"drawbar_16": 12, "drawbar_8": 13, "drawbar_4": 14, "drawbar_2": 15, "rotary_speed": 68, "overdrive_level": 16, "vibrato_chorus": 17},
        "sysex_header": "F0 41 10 00 07 12",
        "req_cmd": "F0 41 10 00 07 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Bank 1", "ROM", 32, "Classic Gospel & Rock B3 Drawbars", [f"VK-7 Organ {i+1:02d}" for i in range(32)]),
            ("Preset Bank 2", "ROM", 32, "Jazz, Theater & Percussive Organs", [f"VK-7 Jazz {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "tr-6s",
        "manufacturer": "Roland",
        "model": "TR-6S",
        "type": "6-Track Rhythm Performer",
        "year": 2020,
        "cc_map": {"tune_bd": 20, "decay_bd": 21, "ctrl_bd": 22, "tune_sd": 24, "decay_sd": 25, "ctrl_sd": 26, "master_fx": 19},
        "sysex_header": "F0 41 10 00 00 6C 12",
        "req_cmd": "F0 41 10 00 00 6C 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Patterns", "ROM", 64, "ACB Vintage Kits & FM Patterns", [f"TR-6S Kit {i+1:02d}" for i in range(64)]),
            ("User Patterns", "RAM", 64, "User Rhythm Kits & Motion Patterns", [f"TR-6S User {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "s-550",
        "manufacturer": "Roland",
        "model": "S-550",
        "type": "12-Bit Studio Digital Sampler",
        "year": 1987,
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "pan": 10},
        "sysex_header": "F0 41 10 17 12",
        "req_cmd": "F0 41 10 17 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Library Disk A", "ROM", 32, "Acoustic Instruments & Percussion", [f"S-550 Disk A-{i+1:02d}" for i in range(32)]),
            ("Factory Library Disk B", "ROM", 32, "Orchestral Strings & Brass", [f"S-550 Disk B-{i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "s-770",
        "manufacturer": "Roland",
        "model": "S-770",
        "type": "24-Bit DSP 16-Bit Sampler Flagship",
        "year": 1990,
        "cc_map": {"tvf_cutoff": 74, "tvf_resonance": 71, "tva_volume": 7, "panpot": 10, "reverb_send": 91},
        "sysex_header": "F0 41 10 34 12",
        "req_cmd": "F0 41 10 34 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Master Library Bank 1", "ROM", 64, "High-Definition Grand Pianos & Strings", [f"S-770 Master 1-{i+1:02d}" for i in range(64)]),
            ("Master Library Bank 2", "ROM", 64, "Analog Synthesis & Cinematic Textures", [f"S-770 Master 2-{i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "u-110",
        "manufacturer": "Roland",
        "model": "U-110",
        "type": "PCM Sound Module",
        "year": 1988,
        "cc_map": {"level": 7, "pan": 10, "chorus_depth": 93, "detune": 94},
        "sysex_header": "F0 41 10 23 12",
        "req_cmd": "F0 41 10 23 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Tones", "ROM", 64, "Internal PCM Acoustic & Synthesizer Tones", [f"U-110 Tone {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "v-synth-xt",
        "manufacturer": "Roland",
        "model": "V-Synth XT",
        "type": "Rack Elastic Audio & Dual VC Workstation",
        "year": 2005,
        "cc_map": {"time_trip_pad_x": 12, "time_trip_pad_y": 13, "filter_cutoff": 74, "resonance": 71, "cosm1_p1": 16, "cosm2_p1": 17, "fx_level": 91},
        "sysex_header": "F0 41 10 00 1E 12",
        "req_cmd": "F0 41 10 00 1E 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Internal Bank 1", "RAM", 128, "VariPhrase Vocal & Sound FX", [f"V-Synth XT Patch 1-{i+1:03d}" for i in range(128)]),
            ("Internal Bank 2", "RAM", 128, "Analog Modeling Leads & Sweeps", [f"V-Synth XT Patch 2-{i+1:03d}" for i in range(128)]),
            ("VC-1 D-50 Bank", "ROM", 128, "Full Authentic D-50 Synthesizer Cards", [f"VC-1 D-50 Tone {i+1:03d}" for i in range(128)]),
            ("VC-2 Vocal Designer", "ROM", 128, "Advanced Vocoder & Choir Modeling", [f"VC-2 Vocal Tone {i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "sy55",
        "manufacturer": "Yamaha",
        "model": "SY55",
        "type": "AWM2 Music Synthesizer",
        "year": 1990,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "eg_attack": 73, "eg_release": 72, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 43 10 2E",
        "req_cmd": "F0 43 20 2E 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "AWM2 Acoustic & Synth Voices", [f"SY55 Voice {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tg55",
        "manufacturer": "Yamaha",
        "model": "TG55",
        "type": "AWM2 Tone Generator Module",
        "year": 1990,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "eg_attack": 73, "eg_release": 72, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 43 10 2E",
        "req_cmd": "F0 43 20 2E 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 64, "AWM2 Rack Studio Voices", [f"TG55 Voice {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tg100",
        "manufacturer": "Yamaha",
        "model": "TG100",
        "type": "General MIDI Tone Generator",
        "year": 1992,
        "cc_map": {"volume": 7, "pan": 10, "expression": 11, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 27",
        "req_cmd": "F0 43 20 27 00 00 00 F7",
        "banks": [
            ("General MIDI Bank", "ROM", 128, "Standard 128 GM Instruments", [f"TG100 GM {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "tg300",
        "manufacturer": "Yamaha",
        "model": "TG300",
        "type": "General MIDI & GS Tone Generator",
        "year": 1993,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 2B",
        "req_cmd": "F0 43 20 2B 00 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Enhanced GM/GS Instruments", [f"TG300 Instrument {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "ys100",
        "manufacturer": "Yamaha",
        "model": "YS100",
        "type": "4-Operator FM Digital Synthesizer",
        "year": 1988,
        "cc_map": {"volume": 7, "modulation": 1, "sustain": 64, "portamento": 65},
        "sysex_header": "F0 43 10 24",
        "req_cmd": "F0 43 20 24 00 00 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 100, "Easy Edit 4-Operator FM Voices", [f"YS100 Preset {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "ys200",
        "manufacturer": "Yamaha",
        "model": "YS200",
        "type": "4-Operator FM Digital Workstation",
        "year": 1988,
        "cc_map": {"volume": 7, "modulation": 1, "sustain": 64, "portamento": 65},
        "sysex_header": "F0 43 10 24",
        "req_cmd": "F0 43 20 24 00 00 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 100, "4-Operator FM Workstation Voices", [f"YS200 Preset {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "spx900",
        "manufacturer": "Yamaha",
        "model": "SPX900",
        "type": "Professional Multi-Effects Processor",
        "year": 1988,
        "cc_map": {"input_level": 7, "balance": 10, "param_1": 16, "param_2": 17, "param_3": 18, "bypass": 80},
        "sysex_header": "F0 43 10 2C",
        "req_cmd": "F0 43 20 2C 00 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Studio Digital Reverb & Modulations", [f"SPX900 Program {i+1:02d}" for i in range(99)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "sw1000xg",
        "manufacturer": "Yamaha",
        "model": "SW1000XG",
        "type": "PCI Hardware XG Synthesizer",
        "year": 1998,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack_time": 73, "release_time": 72, "variation_send": 94, "reverb_send": 91, "chorus_send": 93},
        "sysex_header": "F0 43 10 4C",
        "req_cmd": "F0 43 10 4C 00 00 00 F7",
        "banks": [
            ("XG Normal Bank 1", "ROM", 128, "Studio Quality XG Acoustic & Synth Voices", [f"SW1000XG Normal {i+1:03d}" for i in range(128)]),
            ("XG Normal Bank 2", "ROM", 128, "Expanded Studio Synthesis & SFX", [f"SW1000XG Synth {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "p-100",
        "manufacturer": "Yamaha",
        "model": "P-100",
        "type": "AWM Stage Piano",
        "year": 1994,
        "cc_map": {"volume": 7, "damper": 64, "sostenuto": 66, "soft": 67, "reverb_depth": 91, "chorus_depth": 93},
        "sysex_header": "F0 43 10 3E",
        "req_cmd": "F0 43 20 3E 00 00 00 F7",
        "banks": [
            ("Preset Voices", "ROM", 32, "Acoustic Grand Pianos & Clavinets", [f"P-100 Voice {i+1:02d}" for i in range(32)])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "nautilus",
        "manufacturer": "Korg",
        "model": "Nautilus",
        "type": "9-Engine Music Workstation",
        "year": 2020,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "dynamics_knob": 16, "tone_knob": 17, "user_knob_1": 18, "user_knob_2": 19, "rt_control": 20},
        "sysex_header": "F0 42 30 00 01 1D",
        "req_cmd": "F0 42 30 00 01 1D 10 00 00 F7",
        "banks": [
            ("HD-1 High Definition Bank", "ROM", 128, "High-Res Acoustic & Orchestral Presets", [f"Nautilus HD-1 {i+1:03d}" for i in range(128)]),
            ("EXi Synthesis Engines Bank", "ROM", 128, "AL-1, MS-20, Polysix & MOD-7 Algorithms", [f"Nautilus EXi {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "oasys",
        "manufacturer": "Korg",
        "model": "OASYS",
        "type": "Open Architecture Synthesis Studio",
        "year": 2005,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "vector_joystick_x": 16, "vector_joystick_y": 17, "karma_slider_1": 18, "karma_slider_2": 19, "karma_slider_3": 20},
        "sysex_header": "F0 42 30 73",
        "req_cmd": "F0 42 30 73 10 00 00 F7",
        "banks": [
            ("HD-1 PCM Programs", "ROM", 128, "Uncompressed PCM Pianos & Acoustic Waves", [f"OASYS HD-1 {i+1:03d}" for i in range(128)]),
            ("AL-1 VA & CX-3 Organs", "ROM", 128, "Analog Modeling & Tonewheel Organ Algorithms", [f"OASYS Synth {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "tr-61",
        "manufacturer": "Korg",
        "model": "TR-61",
        "type": "HI Synthesis Music Workstation",
        "year": 2006,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "eg_intensity": 79, "eg_release": 72, "knob_a": 16, "knob_b": 17, "knob_c": 18, "knob_d": 19},
        "sysex_header": "F0 42 30 76",
        "req_cmd": "F0 42 30 76 10 00 00 F7",
        "banks": [
            ("Bank A Programs", "ROM", 128, "Pianos, Keyboards & Guitars", [f"TR-61 Program A-{i+1:03d}" for i in range(128)]),
            ("Bank B Programs", "ROM", 128, "Synths, Pads & Leads", [f"TR-61 Program B-{i+1:03d}" for i in range(128)]),
            ("Bank C Programs", "ROM", 128, "Orchestral Brass, Strings & Winds", [f"TR-61 Program C-{i+1:03d}" for i in range(128)]),
            ("Bank D Programs", "ROM", 128, "Drums, Percussion & SFX", [f"TR-61 Program D-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "volca-kick",
        "manufacturer": "Korg",
        "model": "Volca Kick",
        "type": "Analog Kick Generator",
        "year": 2016,
        "cc_map": {"pitch": 40, "bend_reverse": 41, "bend_time": 42, "pulse_colour": 43, "pulse_level": 44, "attack": 45, "decay": 46, "tone": 47, "resonator": 48},
        "sysex_header": "F0 42 30 00 01 43",
        "req_cmd": "F0 42 30 00 01 43 10 00 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "MS-20 Resonator Kicks & Subs", [f"Volca Kick Pattern {i+1:02d}" for i in range(16)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "sg-prox",
        "manufacturer": "Korg",
        "model": "SG-ProX",
        "type": "Stage Piano and Master Controller",
        "year": 1997,
        "cc_map": {"volume": 7, "pan": 10, "reverb_depth": 91, "effect_depth": 93, "slider_1": 16, "slider_2": 17},
        "sysex_header": "F0 42 30 50",
        "req_cmd": "F0 42 30 50 10 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 32, "Concert Pianos & Electric Pianos", [f"SG-ProX Piano {i+1:02d}" for i in range(32)]),
            ("Preset Bank 2", "ROM", 32, "Clavs, Organs & String Layers", [f"SG-ProX Layer {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "t1",
        "manufacturer": "Korg",
        "model": "T1",
        "type": "88-Key AI Synthesis Music Workstation",
        "year": 1989,
        "cc_map": {"vdf_cutoff": 74, "vdf_mg_depth": 1, "vda_attack": 73, "vda_release": 72, "effect1_balance": 91, "effect2_balance": 93},
        "sysex_header": "F0 42 30 30",
        "req_cmd": "F0 42 30 30 10 00 00 F7",
        "banks": [
            ("Program Bank A", "ROM", 100, "88-Key Weighted Grand Pianos & Workstation Programs", [f"T1 Program A-{i+1:02d}" for i in range(100)]),
            ("Program Bank B", "ROM", 100, "Synthesizer Sweeps, Bells & Orchestral Ensembles", [f"T1 Program B-{i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "t2",
        "manufacturer": "Korg",
        "model": "T2",
        "type": "76-Key AI Synthesis Music Workstation",
        "year": 1989,
        "cc_map": {"vdf_cutoff": 74, "vdf_mg_depth": 1, "vda_attack": 73, "vda_release": 72, "effect1_balance": 91, "effect2_balance": 93},
        "sysex_header": "F0 42 30 30",
        "req_cmd": "F0 42 30 30 10 00 00 F7",
        "banks": [
            ("Program Bank A", "ROM", 100, "76-Key Workstation AI Programs", [f"T2 Program A-{i+1:02d}" for i in range(100)]),
            ("Program Bank B", "ROM", 100, "Acoustic Instruments & Split Performances", [f"T2 Program B-{i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "korg",
        "model_dir": "a4-guitar",
        "manufacturer": "Korg",
        "model": "A4 Guitar",
        "type": "Guitar Multi-Effects Processor",
        "year": 1993,
        "cc_map": {"drive": 16, "tone": 17, "level": 18, "mod_speed": 19, "mod_depth": 20, "delay_time": 21, "delay_level": 22},
        "sysex_header": "F0 42 30 42",
        "req_cmd": "F0 42 30 42 10 00 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 30, "Classic Overdrives, Tube Leads & Rock Amps", [f"A4 Guitar Rock {i+1:02d}" for i in range(30)]),
            ("Preset Bank 2", "ROM", 30, "Clean Chorused & Ambient Stereo Delays", [f"A4 Guitar Ambient {i+1:02d}" for i in range(30)])
        ]
    },

    # ------------------ E-MU SYSTEMS ------------------
    {
        "m_dir": "emu",
        "model_dir": "proteus-fx",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Proteus FX",
        "type": "Sound Module with Dual Effects",
        "year": 1994,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack": 73, "release": 72, "fx_a_amount": 91, "fx_b_amount": 93, "controller_a": 16},
        "sysex_header": "F0 18 04",
        "req_cmd": "F0 18 04 00 01 00 00 F7",
        "banks": [
            ("RAM Bank 0", "RAM", 128, "User FX Programs", [f"Proteus FX User {i+1:03d}" for i in range(128)]),
            ("ROM Bank 1", "ROM", 128, "Pop & Rock Collection", [f"Proteus FX Pop {i+1:03d}" for i in range(128)]),
            ("ROM Bank 2", "ROM", 128, "Orchestral & Acoustic Collection", [f"Proteus FX Orch {i+1:03d}" for i in range(128)]),
            ("ROM Bank 3", "ROM", 128, "Synthesizer & World Collection", [f"Proteus FX Synth {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "proteus-1-xr",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Proteus/1 XR",
        "type": "Expanded 384-Preset Sound Module",
        "year": 1990,
        "cc_map": {"controller_a": 16, "controller_b": 17, "controller_c": 18, "controller_d": 19, "volume": 7, "pan": 10},
        "sysex_header": "F0 18 04",
        "req_cmd": "F0 18 04 00 01 00 00 F7",
        "banks": [
            ("User Bank", "RAM", 128, "User Custom Patches", [f"Proteus/1 XR User {i+1:03d}" for i in range(128)]),
            ("Preset Bank 1", "ROM", 128, "Pop/Rock Standard Programs", [f"Proteus/1 XR Preset 1-{i+1:03d}" for i in range(128)]),
            ("Preset Bank 2", "ROM", 128, "Expanded Factory Library", [f"Proteus/1 XR Preset 2-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "proteus-2-xr",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Proteus/2 XR",
        "type": "Expanded Orchestral Sound Module",
        "year": 1991,
        "cc_map": {"controller_a": 16, "controller_b": 17, "controller_c": 18, "controller_d": 19, "volume": 7, "pan": 10},
        "sysex_header": "F0 18 04",
        "req_cmd": "F0 18 04 00 01 00 00 F7",
        "banks": [
            ("User Bank", "RAM", 128, "User Orchestral Setups", [f"Proteus/2 XR User {i+1:03d}" for i in range(128)]),
            ("Preset Bank 1", "ROM", 128, "Solo Strings, Brass & Woodwinds", [f"Proteus/2 XR Orch 1-{i+1:03d}" for i in range(128)]),
            ("Preset Bank 2", "ROM", 128, "Ensembles, Percussion & Concert Harp", [f"Proteus/2 XR Orch 2-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "emu",
        "model_dir": "sound-engine",
        "manufacturer": "E-mu Systems, Inc.",
        "model": "Sound Engine",
        "type": "General MIDI Sound Module",
        "year": 1993,
        "cc_map": {"volume": 7, "pan": 10, "reverb_send": 91, "chorus_send": 93, "expression": 11},
        "sysex_header": "F0 18 05",
        "req_cmd": "F0 18 05 00 01 00 00 F7",
        "banks": [
            ("General MIDI Presets", "ROM", 128, "High Quality E-MU General MIDI Library", [f"Sound Engine GM {i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ ENSONIQ ------------------
    {
        "m_dir": "ensoniq",
        "model_dir": "kt-88",
        "manufacturer": "Ensoniq",
        "model": "KT-88",
        "type": "88-Key 64-Voice Production Workstation",
        "year": 1994,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "attack": 73, "decay": 72, "fx_mix": 91, "mod_wheel": 1},
        "sysex_header": "F0 0F 03 00",
        "req_cmd": "F0 0F 03 00 01 00 F7",
        "banks": [
            ("ROM Bank 1", "ROM", 80, "Acoustic Piano & Solo Instruments", [f"KT-88 Voice 1-{i+1:02d}" for i in range(80)]),
            ("ROM Bank 2", "ROM", 80, "Synth Pads, Organs & Percussion", [f"KT-88 Voice 2-{i+1:02d}" for i in range(80)])
        ]
    },
    {
        "m_dir": "ensoniq",
        "model_dir": "ts-12",
        "manufacturer": "Ensoniq",
        "model": "TS-12",
        "type": "76-Key Transwave Synthesizer Workstation",
        "year": 1993,
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "mod_source": 1, "timbre": 70, "fx_dry_wet": 91},
        "sysex_header": "F0 0F 03 02",
        "req_cmd": "F0 0F 03 02 01 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 60, "Transwave Dynamic Synthesis Programs", [f"TS-12 Program 1-{i+1:02d}" for i in range(60)]),
            ("Preset Bank 2", "ROM", 60, "Hyper-Wave & Multi-Sampled Acoustic Sets", [f"TS-12 Program 2-{i+1:02d}" for i in range(60)])
        ]
    },

    # ------------------ DIGITECH ------------------
    {
        "m_dir": "digitech",
        "model_dir": "dsp-128",
        "manufacturer": "DigiTech",
        "model": "DSP-128",
        "type": "Digital Multi-Effects Processor",
        "year": 1987,
        "cc_map": {"decay_time": 16, "predelay": 17, "damping": 18, "mix": 91},
        "sysex_header": "F0 00 00 1B 01",
        "req_cmd": "F0 00 00 1B 01 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "Studio Digital Reverbs, Delays & Chorus", [f"DSP-128 Preset {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "digitech",
        "model_dir": "gsp-5",
        "manufacturer": "DigiTech",
        "model": "GSP-5",
        "type": "Guitar Multi-Effects Preamp",
        "year": 1989,
        "cc_map": {"distortion_gain": 16, "overdrive": 17, "eq_bass": 18, "eq_treble": 19, "delay_time": 20, "reverb_level": 91},
        "sysex_header": "F0 00 00 1B 02",
        "req_cmd": "F0 00 00 1B 02 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Classic Guitar Preamp & Multi-Effects", [f"GSP-5 Program {i+1:02d}" for i in range(99)])
        ]
    },
    {
        "m_dir": "digitech",
        "model_dir": "rp-10",
        "manufacturer": "DigiTech",
        "model": "RP-10",
        "type": "Guitar Effects Floor Controller",
        "year": 1994,
        "cc_map": {"exp_pedal_1": 1, "exp_pedal_2": 2, "gain": 16, "delay_level": 91, "chorus_level": 93},
        "sysex_header": "F0 00 00 1B 06",
        "req_cmd": "F0 00 00 1B 06 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "Stage Performance Multi-Effects", [f"RP-10 Patch {i+1:02d}" for i in range(99)])
        ]
    },

    # ------------------ ACCESS MUSIC ------------------
    {
        "m_dir": "access",
        "model_dir": "virus-indigo",
        "manufacturer": "Access",
        "model": "Virus Indigo",
        "type": "Virtual Analog 37-Key Synthesizer",
        "year": 2000,
        "cc_map": {"filter_cutoff": 40, "resonance": 41, "osc1_shape": 33, "osc2_semitone": 35, "lfo1_rate": 20, "filter_env_decay": 46},
        "sysex_header": "F0 00 20 33 01 10",
        "req_cmd": "F0 00 20 33 01 10 10 00 00 F7",
        "banks": [
            ("Bank A", "RAM", 128, "Designer Leads & Screaming Analog Acid", [f"Indigo A-{i+1:03d}" for i in range(128)]),
            ("Bank B", "RAM", 128, "Hyper-Resonant Basses & Trance Pads", [f"Indigo B-{i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "access",
        "model_dir": "virus-kb",
        "manufacturer": "Access",
        "model": "Virus KB",
        "type": "61-Key Virtual Analog Synthesizer",
        "year": 1999,
        "cc_map": {"filter_cutoff": 40, "resonance": 41, "osc1_shape": 33, "osc2_semitone": 35, "lfo1_rate": 20, "filter_env_decay": 46},
        "sysex_header": "F0 00 20 33 01 10",
        "req_cmd": "F0 00 20 33 01 10 10 00 00 F7",
        "banks": [
            ("Bank A", "RAM", 128, "Virus KB Performance Programs", [f"Virus KB A-{i+1:03d}" for i in range(128)]),
            ("Bank B", "RAM", 128, "Classic Virus Analog Modeling", [f"Virus KB B-{i+1:03d}" for i in range(128)])
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

    print(f"\nWave 22 Build Complete! {len(DEVICES)} new flagships, workstations, samplers & racks created.")

if __name__ == "__main__":
    build_all()
