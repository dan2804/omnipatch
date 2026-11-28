#!/usr/bin/env python3
"""
Wave 14 Flagship Romplers, Sound Canvas Super-Modules & XG Synths Generator for OmniPatch:
- Roland Sound Canvas & JV/XP Flagships: SC-88 Pro, SC-8850, SC-8820, SD-35, SD-50, PMA-5, XP-30, XP-50, JV-1010, JV-880, JV-80
- Yamaha XG Tone Generators & Workstations: MU100, MU128, MU1000, MU2000, MU80, MU50, CS2x, Motif ES, Motif XF
- Korg AI2, Trinity & HI Synthesizers: X5D, X3, X2, 05R/W, NS5R, NX5R, TR-Rack, X50, MicroX, T3
Creates profile.yaml and factory_presets.json for 30 iconic instruments.
"""

import os
import json
import yaml

def write_synth(manufacturer, model_id, name, synth_type, year, midi_cc_map, sysex_spec, banks, presets):
    base_dir = os.path.join("devices", manufacturer, model_id)
    os.makedirs(base_dir, exist_ok=True)
    
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
        
    with open(os.path.join(base_dir, "factory_presets.json"), "w") as f:
        json.dump(presets, f, indent=2)
        
    print(f"Created {manufacturer}/{model_id}: {name} ({len(presets)} presets)")

def build_wave14():
    print("Building Wave 14: 90s Flagship Romplers, Sound Canvas Super-Modules & XG Synths (30 Instruments)...")

    # =========================================================================
    # 1. ROLAND SC-88 PRO (Sound Canvas Pro w/ Insertion Effects)
    # =========================================================================
    sc88p_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb": 91, "chorus": 93, "delay": 94, "filter_cutoff": 74, "resonance": 71}
    sc88p_sysex = {"header": "F0 41 10 42 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 42 11 [addr] [size] [chk] F7"}}
    sc88p_banks = [{"name": "SC-88 Pro Map", "type": "ROM", "size": 256}, {"name": "SC-88 Map", "type": "ROM", "size": 256}]
    sc88p_presets = []
    for b, bname in enumerate(["SC-88 Pro Map", "SC-88 Map"]):
        for i in range(256):
            pool = ["Piano 1 Pro", "Bright Piano Pro", "Dyno Rhodes Pro", "Jazz Organ Pro", "Full Strings Pro", "Warm Brass Pro",
                    "Acoustic Bass Pro", "Finger Bass Pro", "Slap Bass Pro", "Clean Strat Pro", "Overdrive Solo Pro", "Vocal Oohs Pro",
                    "Synth Saw Lead Pro", "Fifth Lead Pro", "Halo Pad Pro", "Sweep Pad Pro"]
            base = pool[i % len(pool)]
            sc88p_presets.append({"name": f"SC88Pro {base} #{i+1:03d}", "bank": bname, "number": i + 1, "category": "Keys" if "Piano" in base or "Organ" in base else "Bass" if "Bass" in base else "Lead" if "Lead" in base else "Pad", "tags": ["roland", "sc-88-pro", "sound canvas", "gs map", "insertion fx"]})
    write_synth("roland", "sc-88-pro", "SC-88 Pro", "Professional Sound Canvas Module", 1996, sc88p_cc, sc88p_sysex, sc88p_banks, sc88p_presets)

    # =========================================================================
    # 2. ROLAND SC-8850 (Flagship 128-Voice Sound Canvas)
    # =========================================================================
    sc8850_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "delay": 94, "filter_cutoff": 74, "resonance": 71}
    sc8850_sysex = {"header": "F0 41 10 00 27 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 27 11 [addr] [size] [chk] F7"}}
    sc8850_banks = [{"name": "SC-8850 Native Map", "type": "ROM", "size": 256}, {"name": "SC-8820 Map", "type": "ROM", "size": 128}]
    sc8850_presets = []
    for i in range(256):
        sc8850_presets.append({"name": f"SC8850 Flagship Sound #{i+1:03d}", "bank": "SC-8850 Native Map", "number": i + 1, "category": "Synth", "tags": ["roland", "sc-8850", "sound canvas", "128-voice", "flagship"]})
    for i in range(128):
        sc8850_presets.append({"name": f"SC8820 Compatible Patch #{i+1:03d}", "bank": "SC-8820 Map", "number": i + 1, "category": "General MIDI", "tags": ["roland", "sc-8820", "sound canvas", "gm2"]})
    write_synth("roland", "sc-8850", "SC-8850", "128-Voice Sound Canvas Flagship", 1999, sc8850_cc, sc8850_sysex, sc8850_banks, sc8850_presets)

    # =========================================================================
    # 3. ROLAND SC-8820 (Compact 64-Voice Sound Canvas USB)
    # =========================================================================
    sc8820_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "filter_cutoff": 74, "resonance": 71}
    sc8820_sysex = {"header": "F0 41 10 00 28 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 28 11 [addr] [size] [chk] F7"}}
    sc8820_banks = [{"name": "SC-8820 Preset Bank", "type": "ROM", "size": 256}]
    sc8820_presets = []
    for i in range(256):
        sc8820_presets.append({"name": f"SC8820 Tone #{i+1:03d}", "bank": "SC-8820 Preset Bank", "number": i + 1, "category": "General MIDI", "tags": ["roland", "sc-8820", "sound canvas", "usb"]})
    write_synth("roland", "sc-8820", "SC-8820", "64-Voice USB Sound Canvas Module", 1999, sc8820_cc, sc8820_sysex, sc8820_banks, sc8820_presets)

    # =========================================================================
    # 4. ROLAND SD-35 (MIDI Player Sound Canvas)
    # =========================================================================
    sd35_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    sd35_sysex = {"header": "F0 41 10 42 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 42 11 [addr] [size] [chk] F7"}}
    sd35_banks = [{"name": "Standard GS Bank", "type": "ROM", "size": 128}]
    sd35_presets = []
    for i in range(128):
        sd35_presets.append({"name": f"SD35 Canvas Instrument #{i+1:03d}", "bank": "Standard GS Bank", "number": i + 1, "category": "General MIDI", "tags": ["roland", "sd-35", "midi player", "sound canvas"]})
    write_synth("roland", "sd-35", "SD-35", "MIDI Player Sound Canvas", 1993, sd35_cc, sd35_sysex, sd35_banks, sd35_presets)

    # =========================================================================
    # 5. ROLAND SD-50 (Mobile Studio Canvas)
    # =========================================================================
    sd50_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "filter_cutoff": 74, "resonance": 71}
    sd50_sysex = {"header": "F0 41 10 00 00 48 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 00 00 48 11 [addr] [size] [chk] F7"}}
    sd50_banks = [{"name": "Solo Tones", "type": "ROM", "size": 128}, {"name": "Studio Canvas Bank", "type": "ROM", "size": 256}]
    sd50_presets = []
    for i in range(128):
        sd50_presets.append({"name": f"SD50 Solo Tone #{i+1:03d}", "bank": "Solo Tones", "number": i + 1, "category": "Solo", "tags": ["roland", "sd-50", "mobile canvas", "supernatural"]})
    for i in range(256):
        sd50_presets.append({"name": f"SD50 Studio Sound #{i+1:03d}", "bank": "Studio Canvas Bank", "number": i + 1, "category": "Synth", "tags": ["roland", "sd-50", "studio canvas", "gm2"]})
    write_synth("roland", "sd-50", "SD-50", "Mobile Studio Canvas Synthesizer", 2010, sd50_cc, sd50_sysex, sd50_banks, sd50_presets)

    # =========================================================================
    # 6. ROLAND PMA-5 (Personal Music Assistant)
    # =========================================================================
    pma_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    pma_sysex = {"header": "F0 41 10 42 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 42 11 [addr] [size] [chk] F7"}}
    pma_banks = [{"name": "PMA Tone Bank", "type": "ROM", "size": 128}]
    pma_presets = []
    for i in range(128):
        pma_presets.append({"name": f"PMA5 Sound #{i+1:03d}", "bank": "PMA Tone Bank", "number": i + 1, "category": "General MIDI", "tags": ["roland", "pma-5", "personal music assistant", "touch"]})
    write_synth("roland", "pma-5", "PMA-5", "Personal Music Assistant Sound Module", 1996, pma_cc, pma_sysex, pma_banks, pma_presets)

    # =========================================================================
    # 7. ROLAND XP-30 (64-Voice Expandable Synthesizer w/ 1,406 Patches)
    # =========================================================================
    xp30_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb": 91, "chorus": 93}
    xp30_sysex = {"header": "F0 41 10 6A 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 6A 11 [addr] [size] [chk] F7"}}
    xp30_banks = [{"name": "Preset Bank A", "type": "ROM", "size": 128}, {"name": "Preset Bank B", "type": "ROM", "size": 128},
                  {"name": "Session SR-JV", "type": "ROM", "size": 128}, {"name": "Techno SR-JV", "type": "ROM", "size": 128}]
    xp30_presets = []
    for bname in ["Preset Bank A", "Preset Bank B", "Session SR-JV", "Techno SR-JV"]:
        for i in range(128):
            xp_pool = ["Concert Grand XP", "Session Rhodes Mark V", "Techno Pulse Bass", "Warm Super JV Strings", "Saw Solo Screamer",
                       "Ambient Pad Evolution", "Stereo Acoustic Guitar", "Slap Bass Funk", "Section Horn Hits", "XP-30 Signature Poly"]
            base = xp_pool[i % len(xp_pool)]
            xp30_presets.append({"name": f"XP30 {base} #{i+1:03d}", "bank": bname, "number": i + 1, "category": "Keys" if "Piano" in base or "Rhodes" in base else "Bass" if "Bass" in base else "Pad" if "Strings" in base or "Pad" in base else "Lead", "tags": ["roland", "xp-30", "super jv", "64-voice", "session", "techno"]})
    write_synth("roland", "xp-30", "XP-30", "64-Voice Expandable Synthesizer", 1999, xp30_cc, xp30_sysex, xp30_banks, xp30_presets)

    # =========================================================================
    # 8. ROLAND XP-50 (Music Workstation)
    # =========================================================================
    xp50_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb": 91, "chorus": 93}
    xp50_sysex = {"header": "F0 41 10 6A 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 6A 11 [addr] [size] [chk] F7"}}
    xp50_banks = [{"name": "Internal Preset A", "type": "ROM", "size": 128}, {"name": "Internal Preset B", "type": "ROM", "size": 128}]
    xp50_presets = []
    for b in range(2):
        bname = f"Internal Preset {chr(65+b)}"
        for i in range(128):
            xp50_presets.append({"name": f"XP50 Sound {chr(65+b)}{i+1:03d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["roland", "xp-50", "workstation", "super jv"]})
    write_synth("roland", "xp-50", "XP-50", "64-Voice Music Workstation", 1995, xp50_cc, xp50_sysex, xp50_banks, xp50_presets)

    # =========================================================================
    # 9. ROLAND JV-1010 (64-Voice Synthesizer Module w/ Session Board)
    # =========================================================================
    jv1k_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "resonance": 71, "reverb": 91, "chorus": 93}
    jv1k_sysex = {"header": "F0 41 10 6A 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 6A 11 [addr] [size] [chk] F7"}}
    jv1k_banks = [{"name": "Preset Bank A-D", "type": "ROM", "size": 256}, {"name": "Session Expansion", "type": "ROM", "size": 256}]
    jv1k_presets = []
    for i in range(256):
        jv1k_presets.append({"name": f"JV1010 Core Sound #{i+1:03d}", "bank": "Preset Bank A-D", "number": i + 1, "category": "Synth", "tags": ["roland", "jv-1010", "half-rack", "super jv"]})
    for i in range(256):
        jv1k_presets.append({"name": f"JV1010 Session Sound #{i+1:03d}", "bank": "Session Expansion", "number": i + 1, "category": "Keys", "tags": ["roland", "jv-1010", "session card", "acoustic"]})
    write_synth("roland", "jv-1010", "JV-1010", "64-Voice Synthesizer Module w/ Session", 1999, jv1k_cc, jv1k_sysex, jv1k_banks, jv1k_presets)

    # =========================================================================
    # 10. ROLAND JV-880 (Multi-Timbral Synthesizer Module)
    # =========================================================================
    jv880_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    jv880_sysex = {"header": "F0 41 10 46 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 46 11 [addr] [size] [chk] F7"}}
    jv880_banks = [{"name": "Preset Bank A", "type": "ROM", "size": 64}, {"name": "Preset Bank B", "type": "ROM", "size": 64}]
    jv880_presets = []
    for b in range(2):
        bname = f"Preset Bank {chr(65+b)}"
        for i in range(64):
            jv880_presets.append({"name": f"JV880 Patch {chr(65+b)}{i+1:02d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["roland", "jv-880", "multi-timbral", "rack module"]})
    write_synth("roland", "jv-880", "JV-880", "Multi-Timbral Synthesizer Module", 1992, jv880_cc, jv880_sysex, jv880_banks, jv880_presets)

    # =========================================================================
    # 11. ROLAND JV-80 (Multi-Timbral Synthesizer Keyboard)
    # =========================================================================
    jv80_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "slider1": 16}
    jv80_sysex = {"header": "F0 41 10 46 12", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 46 11 [addr] [size] [chk] F7"}}
    jv80_banks = [{"name": "Preset Bank A", "type": "ROM", "size": 64}, {"name": "Preset Bank B", "type": "ROM", "size": 64}]
    jv80_presets = []
    for b in range(2):
        bname = f"Preset Bank {chr(65+b)}"
        for i in range(64):
            jv80_presets.append({"name": f"JV80 Sound {chr(65+b)}{i+1:02d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["roland", "jv-80", "synthesizer keyboard"]})
    write_synth("roland", "jv-80", "JV-80", "Multi-Timbral Synthesizer Keyboard", 1992, jv80_cc, jv80_sysex, jv80_banks, jv80_presets)

    # =========================================================================
    # 12. YAMAHA MU100 (64-Voice XG Tone Generator w/ Vocal Harmony)
    # =========================================================================
    mu100_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb": 91, "chorus": 93, "variation": 94, "cutoff": 74, "resonance": 71}
    mu100_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu100_banks = [{"name": "XG Normal Voices", "type": "ROM", "size": 256}, {"name": "XG SFX Voices", "type": "ROM", "size": 64}]
    mu100_presets = []
    for i in range(256):
        mu_pool = ["Grand Piano XG", "Dyno Rhodes XG", "Drawbar Organ XG", "Warm Nylon Guitar", "Overdriven Solo XG", "Acoustic Upright Bass",
                   "Slap Bass XG", "Symphonic Strings XG", "Brass Fanfare XG", "Analog Saw Lead", "Fifth Sweep Pad", "Voice Oohs XG"]
        base = mu_pool[i % len(mu_pool)]
        mu100_presets.append({"name": f"MU100 {base} #{i+1:03d}", "bank": "XG Normal Voices", "number": i + 1, "category": "General MIDI", "tags": ["yamaha", "mu100", "xg", "vocal harmony", "64-voice"]})
    for i in range(64):
        mu100_presets.append({"name": f"MU100 SFX Tone #{i+1:02d}", "bank": "XG SFX Voices", "number": i + 1, "category": "FX", "tags": ["yamaha", "mu100", "sfx"]})
    write_synth("yamaha", "mu100", "MU100", "64-Voice XG Tone Generator w/ VH", 1997, mu100_cc, mu100_sysex, mu100_banks, mu100_presets)

    # =========================================================================
    # 13. YAMAHA MU128 (128-Voice XG Tone Generator w/ 3 PLG Slots)
    # =========================================================================
    mu128_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "variation": 94, "cutoff": 74, "resonance": 71}
    mu128_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu128_banks = [{"name": "XG Native Bank 1", "type": "ROM", "size": 256}, {"name": "XG Native Bank 2", "type": "ROM", "size": 256}]
    mu128_presets = []
    for b in range(2):
        bname = f"XG Native Bank {b+1}"
        for i in range(256):
            mu128_presets.append({"name": f"MU128 Voice B{b+1}-{i+1:03d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["yamaha", "mu128", "xg", "128-voice", "plg slots"]})
    write_synth("yamaha", "mu128", "MU128", "128-Voice XG Tone Generator", 1998, mu128_cc, mu128_sysex, mu128_banks, mu128_presets)

    # =========================================================================
    # 14. YAMAHA MU1000 (Flagship Studio XG Tone Generator)
    # =========================================================================
    mu1k_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "variation": 94, "cutoff": 74, "resonance": 71}
    mu1k_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu1k_banks = [{"name": "MU1000 Studio Voices", "type": "ROM", "size": 256}, {"name": "MU1000 Acoustic Voices", "type": "ROM", "size": 256}]
    mu1k_presets = []
    for bname in ["MU1000 Studio Voices", "MU1000 Acoustic Voices"]:
        for i in range(256):
            mu1k_presets.append({"name": f"MU1000 {bname[:7]} #{i+1:03d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["yamaha", "mu1000", "flagship xg", "studio module"]})
    write_synth("yamaha", "mu1000", "MU1000", "Flagship Studio XG Tone Generator", 1999, mu1k_cc, mu1k_sysex, mu1k_banks, mu1k_presets)

    # =========================================================================
    # 15. YAMAHA MU2000 (Flagship Studio XG w/ Sampler)
    # =========================================================================
    mu2k_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "variation": 94, "cutoff": 74, "resonance": 71}
    mu2k_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu2k_banks = [{"name": "Flagship XG Bank", "type": "ROM", "size": 256}, {"name": "Sampled Voice Bank", "type": "RAM", "size": 128}]
    mu2k_presets = []
    for i in range(256):
        mu2k_presets.append({"name": f"MU2000 XG Voice #{i+1:03d}", "bank": "Flagship XG Bank", "number": i + 1, "category": "Synth", "tags": ["yamaha", "mu2000", "flagship", "sampler", "xg"]})
    for i in range(128):
        mu2k_presets.append({"name": f"MU2000 Sample Program #{i+1:03d}", "bank": "Sampled Voice Bank", "number": i + 1, "category": "Sampler", "tags": ["yamaha", "mu2000", "sampler"]})
    write_synth("yamaha", "mu2000", "MU2000", "Flagship Studio XG Synthesizer / Sampler", 2000, mu2k_cc, mu2k_sysex, mu2k_banks, mu2k_presets)

    # =========================================================================
    # 16. YAMAHA MU80 (Classic 64-Voice XG Module)
    # =========================================================================
    mu80_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "cutoff": 74, "resonance": 71}
    mu80_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu80_banks = [{"name": "MU80 Preset Voices", "type": "ROM", "size": 256}]
    mu80_presets = []
    for i in range(256):
        mu80_presets.append({"name": f"MU80 XG Sound #{i+1:03d}", "bank": "MU80 Preset Voices", "number": i + 1, "category": "General MIDI", "tags": ["yamaha", "mu80", "xg", "first xg module"]})
    write_synth("yamaha", "mu80", "MU80", "64-Voice XG Tone Generator", 1994, mu80_cc, mu80_sysex, mu80_banks, mu80_presets)

    # =========================================================================
    # 17. YAMAHA MU50 (Compact Half-Rack XG Sound Module)
    # =========================================================================
    mu50_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    mu50_sysex = {"header": "F0 43 10 4C", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 4C 00 [bank] [prog] F7"}}
    mu50_banks = [{"name": "MU50 Preset Voices", "type": "ROM", "size": 128}]
    mu50_presets = []
    for i in range(128):
        mu50_presets.append({"name": f"MU50 Voice #{i+1:03d}", "bank": "MU50 Preset Voices", "number": i + 1, "category": "General MIDI", "tags": ["yamaha", "mu50", "xg", "half-rack"]})
    write_synth("yamaha", "mu50", "MU50", "Compact XG Sound Module", 1995, mu50_cc, mu50_sysex, mu50_banks, mu50_presets)

    # =========================================================================
    # 18. YAMAHA CS2x (Dance Synthesizer w/ Arp & 64-Voice Poly)
    # =========================================================================
    cs2x_cc = {"cutoff": 74, "resonance": 71, "attack": 73, "decay": 72, "assign1": 16, "assign2": 17}
    cs2x_sysex = {"header": "F0 43 10 4B", "device_id_byte": 2, "commands": {"request_perf": "F0 43 10 4B 00 [perf] F7"}}
    cs2x_banks = [{"name": "Performance Bank", "type": "ROM", "size": 128}, {"name": "XG Synth Bank", "type": "ROM", "size": 128}]
    cs2x_presets = []
    for i in range(128):
        cs2_pool = ["Trance Energy Lead CS", "Fat Eurodance Saw", "Club Filtered Bass", "Hypnotic Arp Sequence", "Euphoric Pad Swell"]
        base = cs2_pool[i % len(cs2_pool)]
        cs2x_presets.append({"name": f"CS2X {base} #{i+1:03d}", "bank": "Performance Bank", "number": i + 1, "category": "Lead" if "Lead" in base else "Bass" if "Bass" in base else "Pad", "tags": ["yamaha", "cs2x", "dance synthesizer", "arpeggiator"]})
    for i in range(128):
        cs2x_presets.append({"name": f"CS2X XG Sound #{i+1:03d}", "bank": "XG Synth Bank", "number": i + 1, "category": "Synth", "tags": ["yamaha", "cs2x", "xg"]})
    write_synth("yamaha", "cs2x", "CS2x", "Dance Performance Synthesizer", 1998, cs2x_cc, cs2x_sysex, cs2x_banks, cs2x_presets)

    # =========================================================================
    # 19. YAMAHA MOTIF ES (Mega-Voice Workstation)
    # =========================================================================
    mes_cc = {"volume": 7, "pan": 10, "cutoff": 74, "resonance": 71, "knob1": 16, "knob2": 17}
    mes_sysex = {"header": "F0 43 10 7F 00", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 7F 00 00 [bank] [prog] F7"}}
    mes_banks = [{"name": f"Preset Bank {i+1}", "type": "ROM", "size": 128} for i in range(4)]
    mes_presets = []
    for b in range(4):
        bname = f"Preset Bank {b+1}"
        for i in range(128):
            mes_presets.append({"name": f"MotifES Voice B{b+1}-{i+1:03d}", "bank": bname, "number": i + 1, "category": "Workstation", "tags": ["yamaha", "motif-es", "mega voice", "workstation"]})
    write_synth("yamaha", "motif-es", "Motif ES", "128-Voice Mega-Voice Workstation", 2003, mes_cc, mes_sysex, mes_banks, mes_presets)

    # =========================================================================
    # 20. YAMAHA MOTIF XF (741MB Flagship Music Production Workstation)
    # =========================================================================
    mxf_cc = {"volume": 7, "pan": 10, "cutoff": 74, "resonance": 71, "slider1": 16, "slider2": 17}
    mxf_sysex = {"header": "F0 43 10 7F 12", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 7F 12 00 [bank] [prog] F7"}}
    mxf_banks = [{"name": f"Preset Bank {chr(65+b)}", "type": "ROM", "size": 128} for b in range(4)]
    mxf_presets = []
    for b in range(4):
        bname = f"Preset Bank {chr(65+b)}"
        for i in range(128):
            mxf_presets.append({"name": f"MotifXF Voice {chr(65+b)}{i+1:03d}", "bank": bname, "number": i + 1, "category": "Workstation", "tags": ["yamaha", "motif-xf", "flagship workstation", "flash expansion"]})
    write_synth("yamaha", "motif-xf", "Motif XF", "Music Production Synthesizer Workstation", 2010, mxf_cc, mxf_sysex, mxf_banks, mxf_presets)

    # =========================================================================
    # 21. KORG X5D (AI2 Synthesizer 64-Voice)
    # =========================================================================
    x5d_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "cutoff": 74}
    x5d_sysex = {"header": "F0 42 30 36", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 36 10 [prog] F7"}}
    x5d_banks = [{"name": "Preset Programs", "type": "ROM", "size": 100}, {"name": "Preset Combinations", "type": "ROM", "size": 100}]
    x5d_presets = []
    for i in range(100):
        x5d_presets.append({"name": f"X5D Program #{i+1:02d}", "bank": "Preset Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "x5d", "ai2", "64-voice"]})
        x5d_presets.append({"name": f"X5D Combo #{i+1:02d}", "bank": "Preset Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "x5d", "combination"]})
    write_synth("korg", "x5d", "X5D", "64-Voice AI2 Synthesizer", 1995, x5d_cc, x5d_sysex, x5d_banks, x5d_presets)

    # =========================================================================
    # 22. KORG X3 (AI2 Music Workstation)
    # =========================================================================
    x3_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    x3_sysex = {"header": "F0 42 30 35", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 35 10 [prog] F7"}}
    x3_banks = [{"name": "ROM Programs", "type": "ROM", "size": 100}, {"name": "ROM Combinations", "type": "ROM", "size": 100}]
    x3_presets = []
    for i in range(100):
        x3_presets.append({"name": f"X3 Program #{i+1:02d}", "bank": "ROM Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "x3", "ai2", "workstation"]})
        x3_presets.append({"name": f"X3 Combo #{i+1:02d}", "bank": "ROM Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "x3", "combination"]})
    write_synth("korg", "x3", "X3", "AI2 Music Workstation", 1993, x3_cc, x3_sysex, x3_banks, x3_presets)

    # =========================================================================
    # 23. KORG X2 (76-Key AI2 Music Workstation)
    # =========================================================================
    x2_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    x2_sysex = {"header": "F0 42 30 35", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 35 10 [prog] F7"}}
    x2_banks = [{"name": "ROM Programs", "type": "ROM", "size": 100}, {"name": "ROM Combinations", "type": "ROM", "size": 100}]
    x2_presets = []
    for i in range(100):
        x2_presets.append({"name": f"X2 Program #{i+1:02d}", "bank": "ROM Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "x2", "76-key", "ai2", "workstation"]})
        x2_presets.append({"name": f"X2 Combo #{i+1:02d}", "bank": "ROM Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "x2", "combination"]})
    write_synth("korg", "x2", "X2", "76-Key AI2 Music Workstation", 1994, x2_cc, x2_sysex, x2_banks, x2_presets)

    # =========================================================================
    # 24. KORG 05R/W (Compact Half-Rack AI2 Sound Module)
    # =========================================================================
    k05_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    k05_sysex = {"header": "F0 42 30 36", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 36 10 [prog] F7"}}
    k05_banks = [{"name": "Preset Programs", "type": "ROM", "size": 100}, {"name": "Preset Combinations", "type": "ROM", "size": 100}]
    k05_presets = []
    for i in range(100):
        k05_presets.append({"name": f"05RW Sound #{i+1:02d}", "bank": "Preset Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "05rw", "ai2", "half-rack"]})
        k05_presets.append({"name": f"05RW Combo #{i+1:02d}", "bank": "Preset Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "05rw", "combination"]})
    write_synth("korg", "05r-w", "05R/W", "Compact Half-Rack AI2 Sound Module", 1993, k05_cc, k05_sysex, k05_banks, k05_presets)

    # =========================================================================
    # 25. KORG NS5R (Half-Rack Sound Module w/ Graphic LCD)
    # =========================================================================
    ns5_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "cutoff": 74}
    ns5_sysex = {"header": "F0 42 30 4C", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 4C 10 [prog] F7"}}
    ns5_banks = [{"name": "AI2 Program Bank", "type": "ROM", "size": 128}, {"name": "GM/GS Sound Bank", "type": "ROM", "size": 128}]
    ns5_presets = []
    for i in range(128):
        ns5_presets.append({"name": f"NS5R Program #{i+1:03d}", "bank": "AI2 Program Bank", "number": i + 1, "category": "Synth", "tags": ["korg", "ns5r", "ai2", "graphic lcd"]})
    for i in range(128):
        ns5_presets.append({"name": f"NS5R GM/GS Tone #{i+1:03d}", "bank": "GM/GS Sound Bank", "number": i + 1, "category": "General MIDI", "tags": ["korg", "ns5r", "gm", "gs"]})
    write_synth("korg", "ns5r", "NS5R", "Sound Module with Graphic Display", 1997, ns5_cc, ns5_sysex, ns5_banks, ns5_presets)

    # =========================================================================
    # 26. KORG NX5R (Enhanced NS5R w/ Built-In Yamaha XG Daughterboard)
    # =========================================================================
    nx5_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93, "cutoff": 74}
    nx5_sysex = {"header": "F0 42 30 4C", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 4C 10 [prog] F7"}}
    nx5_banks = [{"name": "Korg AI2 Sounds", "type": "ROM", "size": 128}, {"name": "Yamaha XG Sounds", "type": "ROM", "size": 128}]
    nx5_presets = []
    for i in range(128):
        nx5_presets.append({"name": f"NX5R AI2 Sound #{i+1:03d}", "bank": "Korg AI2 Sounds", "number": i + 1, "category": "Synth", "tags": ["korg", "nx5r", "ai2"]})
    for i in range(128):
        nx5_presets.append({"name": f"NX5R XG Voice #{i+1:03d}", "bank": "Yamaha XG Sounds", "number": i + 1, "category": "General MIDI", "tags": ["korg", "nx5r", "yamaha xg daughterboard", "hybrid"]})
    write_synth("korg", "nx5r", "NX5R", "Synthesizer Module with Built-In XG Engine", 1998, nx5_cc, nx5_sysex, nx5_banks, nx5_presets)

    # =========================================================================
    # 27. KORG TR-RACK (Trinity 64-Voice Sound Module)
    # =========================================================================
    trr_cc = {"volume": 7, "pan": 10, "cutoff": 74, "resonance": 71, "reverb": 91, "chorus": 93}
    trr_sysex = {"header": "F0 42 30 3B", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 3B 10 [prog] F7"}}
    trr_banks = [{"name": "Bank A ACCESS", "type": "ROM", "size": 128}, {"name": "Bank B ACCESS", "type": "ROM", "size": 128},
                 {"name": "Bank C Multi", "type": "ROM", "size": 128}, {"name": "Bank D Multi", "type": "ROM", "size": 128}]
    trr_presets = []
    for b in ["Bank A ACCESS", "Bank B ACCESS", "Bank C Multi", "Bank D Multi"]:
        for i in range(128):
            tr_pool = ["Trinity Concert Grand", "Warm ACCESS Pad", "Stereo Poly Saw Lead", "Fat Reso Filter Bass", "Symphonic String Ensemble"]
            base = tr_pool[i % len(tr_pool)]
            trr_presets.append({"name": f"TR-Rack {base} #{i+1:03d}", "bank": b, "number": i + 1, "category": "Keys" if "Piano" in base else "Pad" if "Pad" in base or "String" in base else "Lead", "tags": ["korg", "tr-rack", "trinity", "access synthesis", "64-voice"]})
    write_synth("korg", "tr-rack", "TR-Rack", "64-Voice Trinity Sound Module", 1998, trr_cc, trr_sysex, trr_banks, trr_presets)

    # =========================================================================
    # 28. KORG X50 (Lightweight HI Synthesis Synthesizer)
    # =========================================================================
    x50_cc = {"volume": 7, "pan": 10, "cutoff": 74, "resonance": 71, "knob1": 16, "knob2": 17}
    x50_sysex = {"header": "F0 42 30 68", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 68 1C [prog] F7"}}
    x50_banks = [{"name": "HI Program Bank", "type": "ROM", "size": 128}, {"name": "HI Combination Bank", "type": "ROM", "size": 128}]
    x50_presets = []
    for i in range(128):
        x50_presets.append({"name": f"X50 HI Program #{i+1:03d}", "bank": "HI Program Bank", "number": i + 1, "category": "Synth", "tags": ["korg", "x50", "hi synthesis", "hyper integrated"]})
        x50_presets.append({"name": f"X50 HI Combo #{i+1:03d}", "bank": "HI Combination Bank", "number": i + 1, "category": "Multi", "tags": ["korg", "x50", "combination"]})
    write_synth("korg", "x50", "X50", "Lightweight Music Synthesizer", 2006, x50_cc, x50_sysex, x50_banks, x50_presets)

    # =========================================================================
    # 29. KORG MICROX (Compact HI Synthesizer)
    # =========================================================================
    mic_cc = {"volume": 7, "pan": 10, "cutoff": 74, "resonance": 71, "knob1": 16, "knob2": 17}
    mic_sysex = {"header": "F0 42 30 68", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 68 1C [prog] F7"}}
    mic_banks = [{"name": "MicroX Programs", "type": "ROM", "size": 128}, {"name": "MicroX Combinations", "type": "ROM", "size": 128}]
    mic_presets = []
    for i in range(128):
        mic_presets.append({"name": f"MicroX Program #{i+1:03d}", "bank": "MicroX Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "microx", "hi synthesis", "compact"]})
        mic_presets.append({"name": f"MicroX Combo #{i+1:03d}", "bank": "MicroX Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "microx", "combination"]})
    write_synth("korg", "microx", "microX", "Compact Music Synthesizer Module", 2006, mic_cc, mic_sysex, mic_banks, mic_presets)

    # =========================================================================
    # 30. KORG T3 (16-Track Workstation M1 Evolution)
    # =========================================================================
    t3_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    t3_sysex = {"header": "F0 42 30 26", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 26 10 [prog] F7"}}
    t3_banks = [{"name": "Internal Programs", "type": "ROM", "size": 100}, {"name": "Internal Combinations", "type": "ROM", "size": 100}]
    t3_presets = []
    for i in range(100):
        t3_pool = ["Concert Grand T3", "Lore Pad M1 Evolution", "Ooh/Aah Voice Swell", "Warm Analog Strings", "Slap Bass Workstation",
                   "Brass Fanfare T3", "Pan Flute Chiff", "Pole Bell Soundscape", "Percussive Organ B3", "T3 Signature Sound"]
        base = t3_pool[i % len(t3_pool)]
        t3_presets.append({"name": f"T3 {base} #{i+1:02d}", "bank": "Internal Programs", "number": i + 1, "category": "Keys" if "Piano" in base or "Organ" in base else "Pad" if "Pad" in base or "Strings" in base else "Lead", "tags": ["korg", "t3", "ai synthesis", "workstation", "m1 successor"]})
        t3_presets.append({"name": f"T3 Combo Layer #{i+1:02d}", "bank": "Internal Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "t3", "combination"]})
    write_synth("korg", "t3", "T3", "16-Track AI Music Workstation", 1989, t3_cc, t3_sysex, t3_banks, t3_presets)

    print("\nWave 14 Build Complete! 30 new flagship romplers and workstations created.")

if __name__ == "__main__":
    build_wave14()
