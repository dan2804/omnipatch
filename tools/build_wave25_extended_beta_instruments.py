#!/usr/bin/env python3
"""
OmniPatch Wave 25 Builder: Extended Studio Beta Instruments Wave
Ingests the 17 instruments from the extended hardware beta list:
- Behringer: Virtualizer (DSP1000 Pro Multi-Effects)
- Ensoniq: ASR-X (Advanced Sampler / Resonant Filter Workstation)
- Korg: Kross (EDS-i Music Workstation)
- Lexicon: 300L (LARC-Controlled Studio Reverb)
- Quasimidi: Raven (Dance & Techno Keyboard Workstation)
- Roland: A-90 (88-Key PA-4 Weighted Master Controller)
- Boss: DR-202 Dr. Groove (Groovebox & Drum Machine)
- Boss: GT-5 (COSM Guitar Multi-Effects)
- Boss: GX-700 (COSM Studio Guitar Preamp)
- Roland: FC-200 (MIDI Foot Controller)
- Roland: S-220 (12-Bit Digital Sampler Rack)
- Roland: TB-03 (Boutique Bass Line Synthesizer)
- Roland: TD-6 (V-Drums Percussion Sound Module)
- Roland: TD-8 (COSM V-Drums Brain)
- TC Electronic: Finalizer (Studio Mastering Processor)
- TC Electronic: TC 1128 (Programmable 28-Band Graphic Equalizer)
- Waldorf: Zarenbourg (Physical Modeling Stage Piano)
"""

import os
import json
import yaml

DEVICES = [
    # ------------------ BEHRINGER ------------------
    {
        "m_dir": "behringer",
        "model_dir": "virtualizer",
        "manufacturer": "Behringer",
        "model": "Virtualizer Pro",
        "type": "Digital Multi-Effects Processor",
        "year": 1998,
        "cc_map": {"edit_1": 16, "edit_2": 17, "edit_3": 18, "mix": 91, "eq_high": 19, "eq_low": 20},
        "sysex_header": "F0 00 20 32 02",
        "req_cmd": "F0 00 20 32 02 01 00 F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "Studio Reverbs, Delays & Modulation Algorithms", [f"Virtualizer {i+1:03d}" for i in range(100)])
        ]
    },

    # ------------------ ENSONIQ ------------------
    {
        "m_dir": "ensoniq",
        "model_dir": "asr-x",
        "manufacturer": "Ensoniq",
        "model": "ASR-X",
        "type": "Advanced Resonant Filter Sampler & Production Station",
        "year": 1997,
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "attack": 73, "release": 72, "fx_amount": 91},
        "sysex_header": "F0 0F 03 04",
        "req_cmd": "F0 0F 03 04 01 00 F7",
        "banks": [
            ("Internal Sounds", "ROM", 128, "Resonant Filtered Hip-Hop & Techno Sampler Presets", [f"ASR-X Sound {i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ KORG ------------------
    {
        "m_dir": "korg",
        "model_dir": "kross",
        "manufacturer": "Korg",
        "model": "Kross",
        "type": "EDS-i Mobile Music Workstation",
        "year": 2013,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "eg_intensity": 79, "eg_release": 72, "knob_1": 16, "knob_2": 17},
        "sysex_header": "F0 42 30 00 01 23",
        "req_cmd": "F0 42 30 00 01 23 10 00 00 F7",
        "banks": [
            ("Bank A Programs", "ROM", 128, "Pianos, Guitars & Orchestral Presets", [f"Kross Prog A-{i+1:03d}" for i in range(128)]),
            ("Bank B Programs", "ROM", 128, "EDM Synths, Basses & Motion Leads", [f"Kross Prog B-{i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ LEXICON ------------------
    {
        "m_dir": "lexicon",
        "model_dir": "300l",
        "manufacturer": "Lexicon",
        "model": "Lexicon 300L",
        "type": "LARC-Controlled Studio Digital Effects System",
        "year": 1991,
        "cc_map": {"decay_time": 16, "predelay": 17, "rolloff": 18, "size": 19, "diffusion": 20, "mix": 91},
        "sysex_header": "F0 06 03",
        "req_cmd": "F0 06 03 01 00 F7",
        "banks": [
            ("Preset Programs", "ROM", 100, "Classic Lexicon Hall, Plate & Random Ambience", [f"Lexicon 300L {i+1:03d}" for i in range(100)])
        ]
    },

    # ------------------ QUASIMIDI ------------------
    {
        "m_dir": "quasimidi",
        "model_dir": "raven",
        "manufacturer": "Quasimidi",
        "model": "Raven",
        "type": "Dance & Techno Master Synthesizer Keyboard",
        "year": 1995,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "envelope_attack": 73, "envelope_decay": 72, "reverb": 91, "chorus": 93},
        "sysex_header": "F0 3F 00 01",
        "req_cmd": "F0 3F 00 01 01 00 F7",
        "banks": [
            ("Preset Bank", "ROM", 128, "Aggressive Rave, Hardcore & Trance Soundset", [f"Raven Sound {i+1:03d}" for i in range(128)])
        ]
    },

    # ------------------ ROLAND & BOSS ------------------
    {
        "m_dir": "roland",
        "model_dir": "a-90",
        "manufacturer": "Roland",
        "model": "A-90",
        "type": "88-Key PA-4 Weighted Master Controller",
        "year": 1996,
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "bender": 1, "aftertouch": 3},
        "sysex_header": "F0 41 10 7A 12",
        "req_cmd": "F0 41 10 7A 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Master Performances", "RAM", 64, "4-Zone Master Stage Performance Setups", [f"A-90 Setup {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "boss",
        "model_dir": "dr-202",
        "manufacturer": "Boss",
        "model": "DR-202 Dr. Groove",
        "type": "Groovebox Drum Machine & Bass Synthesizer",
        "year": 1998,
        "cc_map": {"filter_cutoff": 74, "resonance": 71, "decay": 72, "reverb_level": 91, "flanger_level": 93},
        "sysex_header": "F0 41 10 00 08 12",
        "req_cmd": "F0 41 10 00 08 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Styles", "ROM", 128, "Hip-Hop, Jungle, Drum&Bass & Acid Patterns", [f"DR-202 Style {i+1:03d}" for i in range(128)])
        ]
    },
    {
        "m_dir": "boss",
        "model_dir": "gt-5",
        "manufacturer": "Boss",
        "model": "GT-5",
        "type": "COSM Guitar Effects Processor",
        "year": 1996,
        "cc_map": {"preamp_gain": 16, "bass": 17, "middle": 18, "treble": 19, "delay_level": 91, "chorus_level": 93},
        "sysex_header": "F0 41 10 7B 12",
        "req_cmd": "F0 41 10 7B 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Preset Patches", "ROM", 100, "COSM Vintage & Modern Guitar Amp Models", [f"GT-5 Patch {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "boss",
        "model_dir": "gx-700",
        "manufacturer": "Boss",
        "model": "GX-700",
        "type": "COSM Studio Guitar Preamp & Multi-Effects",
        "year": 1996,
        "cc_map": {"drive": 16, "master": 17, "bass": 18, "middle": 19, "treble": 20, "delay_send": 91},
        "sysex_header": "F0 41 10 76 12",
        "req_cmd": "F0 41 10 76 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Presets", "ROM", 100, "1U Rackmount Studio Guitar Tones", [f"GX-700 Preset {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "fc-200",
        "manufacturer": "Roland",
        "model": "FC-200",
        "type": "MIDI Foot Controller",
        "year": 1995,
        "cc_map": {"expression_pedal": 7, "control_pedal": 80},
        "sysex_header": "F0 41 10 65 12",
        "req_cmd": "F0 41 10 65 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Patch Bank", "RAM", 32, "Stage MIDI Routing Presets", [f"FC-200 Setup {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "s-220",
        "manufacturer": "Roland",
        "model": "S-220",
        "type": "12-Bit Digital Sampler Rack",
        "year": 1987,
        "cc_map": {"tvf_cutoff": 74, "resonance": 71, "volume": 7},
        "sysex_header": "F0 41 10 18 12",
        "req_cmd": "F0 41 10 18 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Factory Sounds", "ROM", 32, "12-Bit Studio Sampler Presets", [f"S-220 Sound {i+1:02d}" for i in range(32)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "tb-03",
        "manufacturer": "Roland",
        "model": "TB-03",
        "type": "ACB Boutique Bass Line Synthesizer",
        "year": 2016,
        "cc_map": {"tuning": 16, "cutoff": 74, "resonance": 71, "env_mod": 12, "decay": 72, "accent": 17, "overdrive": 18, "delay_time": 19},
        "sysex_header": "F0 41 10 00 00 00 12",
        "req_cmd": "F0 41 10 00 00 00 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Pattern Bank", "RAM", 64, "ACB Authentic Acid & Techno Patterns", [f"TB-03 Pattern {i+1:02d}" for i in range(64)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "td-6",
        "manufacturer": "Roland",
        "model": "TD-6",
        "type": "V-Drums Percussion Sound Module",
        "year": 2001,
        "cc_map": {"pitch": 16, "decay": 17, "pan": 10, "reverb_level": 91},
        "sysex_header": "F0 41 10 00 3F 12",
        "req_cmd": "F0 41 10 00 3F 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("Drum Kits", "ROM", 99, "Dynamic V-Drums Percussion Kits", [f"TD-6 Kit {i+1:02d}" for i in range(99)])
        ]
    },
    {
        "m_dir": "roland",
        "model_dir": "td-8",
        "manufacturer": "Roland",
        "model": "TD-8",
        "type": "COSM V-Drums Percussion Sound Module",
        "year": 1999,
        "cc_map": {"shell_depth": 16, "tuning": 17, "muffling": 18, "reverb_send": 91},
        "sysex_header": "F0 41 10 00 16 12",
        "req_cmd": "F0 41 10 00 16 11 00 00 00 00 01 00 7F F7",
        "banks": [
            ("COSM Preset Kits", "ROM", 64, "COSM Modeled Drum Sets", [f"TD-8 Kit {i+1:02d}" for i in range(64)])
        ]
    },

    # ------------------ TC ELECTRONIC ------------------
    {
        "m_dir": "tc_electronic",
        "model_dir": "finalizer",
        "manufacturer": "TC Electronic",
        "model": "Finalizer",
        "type": "Studio Mastering & Dynamics Processor",
        "year": 1996,
        "cc_map": {"compressor_thresh": 16, "limiter_thresh": 17, "eq_low": 18, "eq_mid": 19, "eq_high": 20, "output_gain": 7},
        "sysex_header": "F0 00 20 1F 01",
        "req_cmd": "F0 00 20 1F 01 01 00 F7",
        "banks": [
            ("Mastering Presets", "ROM", 100, "Multiband Compressor, Limiter & Stereo Normalizers", [f"Finalizer Preset {i+1:02d}" for i in range(100)])
        ]
    },
    {
        "m_dir": "tc_electronic",
        "model_dir": "tc1128",
        "manufacturer": "TC Electronic",
        "model": "TC 1128",
        "type": "Programmable 28-Band Graphic Equalizer",
        "year": 1988,
        "cc_map": {f"band_{i+1}": i+16 for i in range(16)},
        "sysex_header": "F0 00 20 1F 02",
        "req_cmd": "F0 00 20 1F 02 01 00 F7",
        "banks": [
            ("EQ Memories", "RAM", 100, "Studio Room Tuning & Precision Acoustic Curves", [f"TC1128 Curve {i+1:02d}" for i in range(100)])
        ]
    },

    # ------------------ WALDORF ------------------
    {
        "m_dir": "waldorf",
        "model_dir": "zarenbourg",
        "manufacturer": "Waldorf",
        "model": "Zarenbourg",
        "type": "Physical Modeling Stage Piano",
        "year": 2011,
        "cc_map": {"volume": 7, "bass": 16, "mid": 17, "treble": 18, "tremolo_speed": 19, "tremolo_depth": 20, "chorus_depth": 93, "reverb_depth": 91},
        "sysex_header": "F0 3E 15 00",
        "req_cmd": "F0 3E 15 00 01 00 F7",
        "banks": [
            ("Physical Modeled Pianos", "ROM", 32, "Rhodes, Wurlitzer, Clavinet & CP-70 Physical Models", [f"Zarenbourg Preset {i+1:02d}" for i in range(32)])
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

    print(f"\nWave 25 Build Complete! {len(DEVICES)} extended hardware beta instruments created.")

if __name__ == "__main__":
    build_all()
