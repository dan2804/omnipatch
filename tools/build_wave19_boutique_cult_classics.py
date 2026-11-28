#!/usr/bin/env python3
"""
OmniPatch Wave 19 Builder: Boutique Synths, Cult Modules, Studio Effects & Vintage Classics
Adds 30 high-profile instruments from the Midi Quest 13 catalog:
- Studiologic: Sledge
- Octave-Plateau: Voyetra-8
- Marion Systems: ProSynth
- Futuresonus: Parva
- Moog: Sirin
- Red Sound: Dark Star, Dark Star XP2
- Waldorf: Rocket, 4-Pole
- OTO Machines: Biscuit
- Meris: Enzo, Hedra
- MeeBlip: anode, triode, geode
- 1010music: Nanobox Fireball
- Yamaha: SPX1000, RX17, RY20
- Sony: DPS-V55
- DigiTech: Valve-FX, GSP-256, GSP-7
- Ensoniq: DP PRO
- TC Electronic: G-Sharp
- TC-Helicon: VoicePro, VoiceOne
- Kawai: R-100, Spectra
- Zoom: 9030
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ STUDIOLOGIC ------------------
    {
        "m_dir": "studiologic",
        "model_dir": "sledge",
        "manufacturer": "Studiologic",
        "model": "Sledge",
        "type": "Waldorf DSP Virtual Analog Synthesizer",
        "year": 2012,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_wave": 16, "osc2_semitone": 17, "osc3_detune": 18, "envelope_attack": 73, "envelope_release": 72, "lfo1_speed": 19},
        "sysex_header": "F0 00 20 2C 01",
        "req_cmd": "F0 00 20 2C 01 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "Waldorf Wavetable & Analog Modeling", [
                f"Sledge Sound {i+1:03d}" for i in range(128)
            ]),
            ("Preset Bank 2", "ROM", 128, "Polyphonic Leads, Pads & Sequences", [
                f"Sledge Sound {i+129:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ OCTAVE-PLATEAU ------------------
    {
        "m_dir": "octave_plateau",
        "model_dir": "voyetra-8",
        "manufacturer": "Octave-Plateau",
        "model": "Voyetra-8",
        "type": "8-Voice Polyphonic Analog Rack Synthesizer",
        "year": 1982,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "vco1_freq": 16, "vco2_detune": 17, "lfo_rate": 19, "envelope_attack": 73, "envelope_decay": 72},
        "sysex_header": "F0 1B 01",
        "req_cmd": "F0 1B 01 00 F7",
        "banks": [
            ("Factory Programs", "ROM", 100, "Curtis CEM Discrete Analog Voices", [
                f"Voyetra Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ MARION SYSTEMS ------------------
    {
        "m_dir": "marion_systems",
        "model_dir": "prosynth",
        "manufacturer": "Marion Systems",
        "model": "ProSynth",
        "type": "Tom Oberheim 8-Voice Analog Synthesizer",
        "year": 1995,
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco1_wave": 16, "dco2_interval": 17, "env1_attack": 73, "env1_decay": 72},
        "sysex_header": "F0 00 20 0A 01",
        "req_cmd": "F0 00 20 0A 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "High-Resolution Tom Oberheim Analog Engine", [
                f"ProSynth Patch {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ FUTURESONUS ------------------
    {
        "m_dir": "futuresonus",
        "model_dir": "parva",
        "manufacturer": "Futuresonus",
        "model": "Parva",
        "type": "8-Voice Polyphonic True Analog Synthesizer",
        "year": 2015,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_wave": 16, "osc2_tune": 17, "osc3_level": 18, "envelope_attack": 73},
        "sysex_header": "F0 00 21 2D 01",
        "req_cmd": "F0 00 21 2D 01 00 F7",
        "banks": [
            ("Preset Bank 1", "ROM", 128, "True Analog Polyphonic Voices", [
                f"Parva Poly Voice {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ MOOG ------------------
    {
        "m_dir": "moog",
        "model_dir": "sirin",
        "manufacturer": "Moog",
        "model": "Sirin",
        "type": "Analog Messenger of Joy Synthesizer",
        "year": 2019,
        "cc_map": {"filter_cutoff": 19, "resonance": 21, "vco2_freq": 20, "glide_rate": 5, "filter_env_amount": 27, "decay_time": 9},
        "sysex_header": "F0 04 08 24",
        "req_cmd": "F0 04 08 24 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "Taurus Bass & High-Register Analog Lead", [
                f"Sirin Preset {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ RED SOUND ------------------
    {
        "m_dir": "red_sound",
        "model_dir": "dark-star",
        "manufacturer": "Red Sound",
        "model": "Dark Star",
        "type": "Virtual Analog Synthesizer",
        "year": 1999,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_wave": 16, "osc2_detune": 17, "lfo1_speed": 18, "envelope_decay": 72},
        "sysex_header": "F0 00 20 3B 01",
        "req_cmd": "F0 00 20 3B 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Dual-Oscillator Virtual Analog", [
                f"Dark Star Program {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "red_sound",
        "model_dir": "dark-star-xp2",
        "manufacturer": "Red Sound",
        "model": "Dark Star XP2",
        "type": "Dual-DSP Virtual Analog Synthesizer",
        "year": 2001,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "osc1_wave": 16, "osc2_detune": 17, "joystick_x": 12, "joystick_y": 13},
        "sysex_header": "F0 00 20 3B 02",
        "req_cmd": "F0 00 20 3B 02 00 F7",
        "banks": [
            ("XP2 Factory Sounds", "ROM", 64, "Enhanced DSP Virtual Analog", [
                f"Dark Star XP2 {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ WALDORF ------------------
    {
        "m_dir": "waldorf",
        "model_dir": "rocket",
        "manufacturer": "Waldorf",
        "model": "Rocket",
        "type": "Paraphonic Synthesizer",
        "year": 2013,
        "cc_map": {"osc_wave": 16, "osc_tune": 17, "filter_cutoff": 74, "resonance": 71, "filter_boost": 18, "envelope_decay": 72},
        "sysex_header": "F0 3E 15 00",
        "req_cmd": "F0 3E 15 00 00 F7",
        "banks": [
            ("Factory Bank", "ROM", 64, "Multi-Saw / Pulse Paraphonic Synthesis", [
                f"Rocket Patch {i+1:02d}" for i in range(64)
            ])
        ]
    },
    {
        "m_dir": "waldorf",
        "model_dir": "4-pole",
        "manufacturer": "Waldorf",
        "model": "4-Pole",
        "type": "Analog Filter Module",
        "year": 1994,
        "cc_map": {"cutoff": 74, "resonance": 71, "filter_type": 16, "drive": 17, "lfo_speed": 18, "envelope_amount": 19},
        "sysex_header": "F0 3E 07 00",
        "req_cmd": "F0 3E 07 00 00 F7",
        "banks": [
            ("Filter Presets", "ROM", 64, "24dB Resonant Analog Filter & Drive", [
                f"4-Pole Filter {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ OTO MACHINES ------------------
    {
        "m_dir": "oto_machines",
        "model_dir": "biscuit",
        "manufacturer": "OTO Machines",
        "model": "Biscuit",
        "type": "8-Bit Effects Processor & Synthesizer",
        "year": 2010,
        "cc_map": {"drive": 16, "clock_freq": 17, "filter_cutoff": 74, "resonance": 71, "fx_type": 18, "dry_wet": 91},
        "sysex_header": "F0 00 20 73 01",
        "req_cmd": "F0 00 20 73 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "8-Bit Bit-Crusher, Wavefolder & Synth", [
                f"Biscuit Preset {i+1:02d}" for i in range(16)
            ])
        ]
    },

    # ------------------ MERIS ------------------
    {
        "m_dir": "meris",
        "model_dir": "enzo",
        "manufacturer": "Meris",
        "model": "Enzo",
        "type": "Multi-Voice Synthesizer Pedal",
        "year": 2018,
        "cc_map": {"pitch": 14, "filter_cutoff": 74, "resonance": 71, "filter_env": 16, "modulation": 17, "mix": 91},
        "sysex_header": "F0 00 21 3D 01",
        "req_cmd": "F0 00 21 3D 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "Multi-Voice Tracking Monophonic/Polyphonic Synth", [
                f"Enzo Synth Preset {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "meris",
        "model_dir": "hedra",
        "manufacturer": "Meris",
        "model": "Hedra",
        "type": "3-Voice Rhythmic Pitch Shifter",
        "year": 2019,
        "cc_map": {"key_scale": 14, "voice1_pitch": 16, "voice2_pitch": 17, "voice3_pitch": 18, "delay_time": 19, "mix": 91},
        "sysex_header": "F0 00 21 3D 02",
        "req_cmd": "F0 00 21 3D 02 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 16, "Micro-Tuned Diatonic Pitch Harmony", [
                f"Hedra Program {i+1:02d}" for i in range(16)
            ])
        ]
    },

    # ------------------ MEEBLIP ------------------
    {
        "m_dir": "meeblip",
        "model_dir": "anode",
        "manufacturer": "MeeBlip",
        "model": "anode",
        "type": "Bass Synthesizer",
        "year": 2013,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_decay": 72, "pulse_width": 16, "glide": 5},
        "sysex_header": "F0 00 20 6B 01",
        "req_cmd": "F0 00 20 6B 01 00 F7",
        "banks": [
            ("Factory Patches", "ROM", 16, "Digital Wavetable Oscillators + Twin-T Analog Filter", [
                f"anode Patch {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "meeblip",
        "model_dir": "triode",
        "manufacturer": "MeeBlip",
        "model": "triode",
        "type": "Monaural Synthesizer",
        "year": 2016,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_decay": 72, "osc_wave": 16, "sub_level": 17},
        "sysex_header": "F0 00 20 6B 02",
        "req_cmd": "F0 00 20 6B 02 00 F7",
        "banks": [
            ("Factory Patches", "ROM", 16, "3-Oscillator Digital Engine with Analog VCF", [
                f"triode Voice {i+1:02d}" for i in range(16)
            ])
        ]
    },
    {
        "m_dir": "meeblip",
        "model_dir": "geode",
        "manufacturer": "MeeBlip",
        "model": "geode",
        "type": "Digital/Analog Synthesizer",
        "year": 2019,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_decay": 72, "osc_morph": 16, "sub_octave": 17},
        "sysex_header": "F0 00 20 6B 03",
        "req_cmd": "F0 00 20 6B 03 00 F7",
        "banks": [
            ("Factory Patches", "ROM", 16, "Morphing Digital Wavetables with Analog Filter", [
                f"geode Voice {i+1:02d}" for i in range(16)
            ])
        ]
    },

    # ------------------ 1010MUSIC ------------------
    {
        "m_dir": "1010music",
        "model_dir": "nanobox-fireball",
        "manufacturer": "1010music",
        "model": "Nanobox Fireball",
        "type": "Polyphonic Wavetable Mini-Synthesizer",
        "year": 2022,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "wavetable_pos": 16, "warp": 17, "flanger_send": 91, "delay_send": 92},
        "sysex_header": "F0 00 21 44 01",
        "req_cmd": "F0 00 21 44 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "Dual Wavetable Polyphonic Voices", [
                f"Fireball Preset {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ YAMAHA ------------------
    {
        "m_dir": "yamaha",
        "model_dir": "spx1000",
        "manufacturer": "Yamaha",
        "model": "SPX1000",
        "type": "Professional Multi-Effects Processor",
        "year": 1988,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "mix": 91},
        "sysex_header": "F0 43 10 2E",
        "req_cmd": "F0 43 10 2E 00 00 00 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 99, "Classic Reverbs, Early Reflections & Pitch Shift", [
                f"SPX1000 Program {i+1:02d}" for i in range(99)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "rx17",
        "manufacturer": "Yamaha",
        "model": "RX17",
        "type": "Digital Rhythm Programmer",
        "year": 1987,
        "cc_map": {"volume": 7, "pan": 10, "accent_level": 16},
        "sysex_header": "F0 43 10 1C",
        "req_cmd": "F0 43 10 1C 00 00 F7",
        "banks": [
            ("Preset Patterns", "ROM", 24, "PCM Digital Rhythm Patterns", [
                f"RX17 Pattern {i+1:02d}" for i in range(24)
            ])
        ]
    },
    {
        "m_dir": "yamaha",
        "model_dir": "ry20",
        "manufacturer": "Yamaha",
        "model": "RY20",
        "type": "Programmable Rhythm Programmer",
        "year": 1994,
        "cc_map": {"volume": 7, "pan": 10, "pitch": 16, "decay": 17, "reverb_send": 91},
        "sysex_header": "F0 43 10 39",
        "req_cmd": "F0 43 10 39 00 00 F7",
        "banks": [
            ("Preset Drum Kits", "ROM", 50, "AWM Stereo Drum & Bass Kits", [
                f"RY20 Drum Kit {i+1:02d}" for i in range(50)
            ])
        ]
    },

    # ------------------ SONY ------------------
    {
        "m_dir": "sony",
        "model_dir": "dps-v55",
        "manufacturer": "Sony",
        "model": "DPS-V55",
        "type": "4-Channel Spatial Multi-Effects Processor",
        "year": 1998,
        "cc_map": {"param1": 16, "param2": 17, "param3": 18, "param4": 19, "master_balance": 91},
        "sysex_header": "F0 47 00 00 05",
        "req_cmd": "F0 47 00 00 05 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Surround Space Reverb & Modulation", [
                f"DPS-V55 Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ DIGITECH ------------------
    {
        "m_dir": "digitech",
        "model_dir": "valve-fx",
        "manufacturer": "Digitech",
        "model": "Valve-FX",
        "type": "Vacuum Tube Guitar Preamp & Multi-Effects",
        "year": 1995,
        "cc_map": {"tube_gain": 16, "bass": 17, "mid": 18, "treble": 19, "reverb_mix": 91},
        "sysex_header": "F0 00 00 1A 0A",
        "req_cmd": "F0 00 00 1A 0A 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "12AX7 Tube Preamp & S-DISC Processing", [
                f"Valve-FX Preset {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "digitech",
        "model_dir": "gsp-256",
        "manufacturer": "Digitech",
        "model": "GSP-256",
        "type": "Studio Guitar Multi-Effects Processor",
        "year": 1990,
        "cc_map": {"distortion_gain": 16, "delay_time": 17, "chorus_depth": 18, "mix": 91},
        "sysex_header": "F0 00 00 1A 06",
        "req_cmd": "F0 00 00 1A 06 01 00 F7",
        "banks": [
            ("Factory Programs", "ROM", 128, "24-Bit Digital Guitar Effects Chain", [
                f"GSP-256 Program {i+1:03d}" for i in range(128)
            ])
        ]
    },
    {
        "m_dir": "digitech",
        "model_dir": "gsp-7",
        "manufacturer": "Digitech",
        "model": "GSP-7",
        "type": "Guitar Effects Processor",
        "year": 1989,
        "cc_map": {"overdrive": 16, "delay_time": 17, "flanger_speed": 18, "fx_level": 91},
        "sysex_header": "F0 00 00 1A 04",
        "req_cmd": "F0 00 00 1A 04 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Studio Preamp & Multi-Effects", [
                f"GSP-7 Preset {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ ENSONIQ ------------------
    {
        "m_dir": "ensoniq",
        "model_dir": "dp-pro",
        "manufacturer": "Ensoniq",
        "model": "DP PRO",
        "type": "24-Bit Dual-Stereo Multi-Effects Processor",
        "year": 1998,
        "cc_map": {"fx_param1": 16, "fx_param2": 17, "fx_param3": 18, "master_wet": 91},
        "sysex_header": "F0 0F 06 00",
        "req_cmd": "F0 0F 06 00 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 128, "Dual 24-Bit ESP Multi-Effects Algorithms", [
                f"DP PRO Preset {i+1:03d}" for i in range(128)
            ])
        ]
    },

    # ------------------ TC ELECTRONIC ------------------
    {
        "m_dir": "tc_electronic",
        "model_dir": "g-sharp",
        "manufacturer": "Tc Electronic",
        "model": "G-Sharp",
        "type": "Guitar Effects Processor",
        "year": 2006,
        "cc_map": {"reverb_decay": 16, "reverb_color": 17, "fx_param": 18, "fx_mix": 91},
        "sysex_header": "F0 00 20 1F 09",
        "req_cmd": "F0 00 20 1F 09 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 99, "True Dual Engine Guitar Reverbs & Delays", [
                f"G-Sharp Preset {i+1:02d}" for i in range(99)
            ])
        ]
    },

    # ------------------ TC-HELICON ------------------
    {
        "m_dir": "tc_helicon",
        "model_dir": "voicepro",
        "manufacturer": "Tc Helicon",
        "model": "VoicePro",
        "type": "Flagship 8-Voice Vocal Processor",
        "year": 2005,
        "cc_map": {"harmony_level": 16, "lead_level": 17, "formant_shift": 18, "pitch_correct": 19, "reverb_level": 91},
        "sysex_header": "F0 00 20 1F 11",
        "req_cmd": "F0 00 20 1F 11 01 00 F7",
        "banks": [
            ("Studio Vocal Presets", "ROM", 100, "8-Voice Natural Pitch & Formant Modeling", [
                f"VoicePro Preset {i+1:02d}" for i in range(100)
            ])
        ]
    },
    {
        "m_dir": "tc_helicon",
        "model_dir": "voiceone",
        "manufacturer": "Tc Helicon",
        "model": "VoiceOne",
        "type": "Vocal Pitch Correction & Modeling Processor",
        "year": 2002,
        "cc_map": {"pitch_shift": 16, "formant": 17, "glottal": 18, "breath": 19, "mix": 91},
        "sysex_header": "F0 00 20 1F 0B",
        "req_cmd": "F0 00 20 1F 0B 01 00 F7",
        "banks": [
            ("Studio Presets", "ROM", 100, "PureFormance Vocal Modeling", [
                f"VoiceOne Program {i+1:02d}" for i in range(100)
            ])
        ]
    },

    # ------------------ KAWAI ------------------
    {
        "m_dir": "kawai",
        "model_dir": "r-100",
        "manufacturer": "Kawai",
        "model": "R-100",
        "type": "12-Bit Digital Drum Machine",
        "year": 1987,
        "cc_map": {"volume": 7, "pan": 10, "pitch": 16, "decay": 17},
        "sysex_header": "F0 40 00 10 00 07",
        "req_cmd": "F0 40 00 10 00 07 00 F7",
        "banks": [
            ("Factory Patterns", "ROM", 24, "Vintage 12-Bit Gritty Drum Patterns", [
                f"R-100 Pattern {i+1:02d}" for i in range(24)
            ])
        ]
    },
    {
        "m_dir": "kawai",
        "model_dir": "spectra",
        "manufacturer": "Kawai",
        "model": "Spectra",
        "type": "16-Bit Multi-Timbral Synthesizer",
        "year": 1990,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_release": 72, "reverb_send": 91},
        "sysex_header": "F0 40 00 10 00 0A",
        "req_cmd": "F0 40 00 10 00 0A 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 64, "16-Bit Digital Acoustic & Synth Tones", [
                f"Spectra Tone {i+1:02d}" for i in range(64)
            ])
        ]
    },

    # ------------------ ZOOM ------------------
    {
        "m_dir": "zoom",
        "model_dir": "9030",
        "manufacturer": "Zoom",
        "model": "9030",
        "type": "Advanced Guitar Multi-Effects Processor",
        "year": 1991,
        "cc_map": {"distortion_gain": 16, "delay_time": 17, "reverb_time": 18, "eq_mid": 19, "master_vol": 7},
        "sysex_header": "F0 52 00 10",
        "req_cmd": "F0 52 00 10 01 00 F7",
        "banks": [
            ("Factory Programs", "ROM", 99, "DSP High-Density Multi-Effects Chain", [
                f"Zoom 9030 Program {i+1:02d}" for i in range(99)
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
    print(f"Building Wave 19: Boutique Synths, Cult Modules & Studio Classics ({len(DEVICES)} Instruments)...")

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

    print(f"\nWave 19 Build Complete! {len(DEVICES)} new boutique synths, cult modules & studio classics created.")

if __name__ == "__main__":
    build_all()
