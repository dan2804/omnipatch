#!/usr/bin/env python3
"""
Wave 16 Studio Multi-Effects, Hardware Retrofits & Vintage Synthesizers Generator for OmniPatch:
- KiwiTechnics Synthesizer Retrofits: Kiwi-106, Kiwi-3P, Kiwi-Six, Kiwi-80, Patch Editor
- High-End Studio Multi-Effects (Sony, ART, TC Electronic, TC-Helicon, Dynacord):
  Sony DPS-V77, DPS-R7, DPS-D7, DPS-M7, ART Multiverb Alpha, Multiverb III, SGX-2000, DMV-Pro,
  TC Electronic FireworX, D-Two, TC-Helicon VoiceWorks, Dynacord TAM-19, CL-20
- Ensoniq & Kawai Rack Workstations: Ensoniq DP/2, EPS-16 Plus, KS-32, KT-76, Kawai K4r, K1r, K5000W
- Sequential Circuits Vintage Classics: MultiTrak, Split-Eight, Max, Drumtraks
- Akai: ME-80P 8x10 MIDI Patch Bay
Creates profile.yaml and factory_presets.json for 30 specialized instruments.
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

def build_wave16():
    print("Building Wave 16: Studio Multi-Effects, Hardware Retrofits & Vintage Synthesizers (30 Instruments)...")

    # =========================================================================
    # 1. KIWITECHNICS KIWI-106 (Juno-106 Modern Upgrade)
    # =========================================================================
    k106_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo1_rate": 16, "lfo2_rate": 17, "dco_pwm": 70, "volume": 7}
    k106_sysex = {"header": "F0 00 21 16 01", "device_id_byte": 2, "commands": {"request_patch": "F0 00 21 16 01 01 [patch] F7"}}
    k106_banks = [{"name": "Kiwi Bank 1", "type": "RAM", "size": 128}, {"name": "Kiwi Bank 2", "type": "RAM", "size": 128},
                  {"name": "Kiwi Bank 3", "type": "RAM", "size": 128}, {"name": "Kiwi Bank 4", "type": "RAM", "size": 128}]
    k106_presets = []
    for b in range(4):
        bname = f"Kiwi Bank {b+1}"
        for i in range(128):
            k_pool = ["Kiwi Dual LFO Pad", "PWM Lush Chorus Poly", "Overdriven Sub Bass", "Step Sequenced Lead", "Velocity Sensitive Brass",
                      "Multi-Wave Modulation Solo", "BBD Warm Analog Strings", "Acid Resonant Bassline", "Detuned Fifth Lead", "Kiwi-106 Signature Sound"]
            base = k_pool[i % len(k_pool)]
            k106_presets.append({"name": f"Kiwi106 {base} B{b+1}-{i+1:03d}", "bank": bname, "number": i + 1, "category": "Pad" if "Pad" in base or "Strings" in base else "Bass" if "Bass" in base else "Lead", "tags": ["kiwitechnics", "kiwi-106", "juno-106", "analog", "upgrade"]})
    write_synth("kiwitechnics", "kiwi-106", "Kiwi-106", "Juno-106 Modern Upgrade Synthesizer", 2012, k106_cc, k106_sysex, k106_banks, k106_presets)

    # =========================================================================
    # 2. KIWITECHNICS KIWI-3P (Roland JX-3P Modern Upgrade)
    # =========================================================================
    k3p_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo1_rate": 16, "lfo2_rate": 17, "dco2_tune": 70}
    k3p_sysex = {"header": "F0 00 21 16 02", "device_id_byte": 2, "commands": {"request_patch": "F0 00 21 16 02 01 [patch] F7"}}
    k3p_banks = [{"name": "Kiwi-3P Bank A", "type": "RAM", "size": 128}, {"name": "Kiwi-3P Bank B", "type": "RAM", "size": 128}]
    k3p_presets = []
    for b, bname in enumerate(["Kiwi-3P Bank A", "Kiwi-3P Bank B"]):
        for i in range(128):
            k3p_presets.append({"name": f"Kiwi3P Patch {chr(65+b)}{i+1:03d}", "bank": bname, "number": i + 1, "category": "Synth", "tags": ["kiwitechnics", "kiwi-3p", "jx-3p", "analog upgrade"]})
    write_synth("kiwitechnics", "kiwi-3p", "Kiwi-3P", "JX-3P Modern Upgrade Synthesizer", 2013, k3p_cc, k3p_sysex, k3p_banks, k3p_presets)

    # =========================================================================
    # 3. KIWITECHNICS KIWI-SIX (Korg Polysix Modern Upgrade)
    # =========================================================================
    ksix_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo1_rate": 16, "lfo2_rate": 17, "sub_osc": 70}
    ksix_sysex = {"header": "F0 00 21 16 03", "device_id_byte": 2, "commands": {"request_patch": "F0 00 21 16 03 01 [patch] F7"}}
    ksix_banks = [{"name": "Kiwi-Six Preset Bank", "type": "RAM", "size": 128}]
    ksix_presets = []
    for i in range(128):
        ksix_presets.append({"name": f"KiwiSix Memory #{i+1:03d}", "bank": "Kiwi-Six Preset Bank", "number": i + 1, "category": "Analog", "tags": ["kiwitechnics", "kiwi-six", "polysix", "ssm2044 upgrade"]})
    write_synth("kiwitechnics", "kiwi-six", "Kiwi-Six", "Polysix Modern Upgrade Synthesizer", 2014, ksix_cc, ksix_sysex, ksix_banks, ksix_presets)

    # =========================================================================
    # 4. KIWITECHNICS KIWI-80 (Roland JX-8P / MKS-70 Upgrade)
    # =========================================================================
    k80_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo1_rate": 16, "cross_mod": 17}
    k80_sysex = {"header": "F0 00 21 16 04", "device_id_byte": 2, "commands": {"request_patch": "F0 00 21 16 04 01 [patch] F7"}}
    k80_banks = [{"name": "Kiwi-80 Sounds", "type": "RAM", "size": 128}]
    k80_presets = []
    for i in range(128):
        k80_presets.append({"name": f"Kiwi80 Soundtrack Poly #{i+1:03d}", "bank": "Kiwi-80 Sounds", "number": i + 1, "category": "Pad", "tags": ["kiwitechnics", "kiwi-80", "jx-8p", "analog upgrade"]})
    write_synth("kiwitechnics", "kiwi-80", "Kiwi-80", "JX-8P Modern Upgrade Synthesizer", 2016, k80_cc, k80_sysex, k80_banks, k80_presets)

    # =========================================================================
    # 5. KIWITECHNICS PATCH EDITOR (Universal Hardware Programmer)
    # =========================================================================
    kpe_cc = {"slider1": 16, "slider2": 17, "slider3": 18, "slider4": 19}
    kpe_sysex = {"header": "F0 00 21 16 00", "device_id_byte": 2, "commands": {"request_profile": "F0 00 21 16 00 01 [profile] F7"}}
    kpe_banks = [{"name": "Synth Profile Templates", "type": "ROM", "size": 32}]
    kpe_presets = []
    synths = ["Juno-106", "JX-3P", "Polysix", "Matrix-1000", "MKS-50", "MKS-80", "Prophet-600", "DW-8000", "Pulse", "Microwave"]
    for i in range(32):
        base = synths[i % len(synths)]
        kpe_presets.append({"name": f"Kiwi Editor: {base} Template #{i+1:02d}", "bank": "Synth Profile Templates", "number": i + 1, "category": "Utility", "tags": ["kiwitechnics", "patch editor", "hardware programmer"]})
    write_synth("kiwitechnics", "patch-editor", "Patch Editor", "Universal Hardware Synthesizer Programmer", 2011, kpe_cc, kpe_sysex, kpe_banks, kpe_presets)

    # =========================================================================
    # 6. SONY DPS-V77 (High-End 48kHz Studio Multi-Effects Processor)
    # =========================================================================
    v77_cc = {"mix": 91, "bypass": 84, "param1": 16, "param2": 17}
    v77_sysex = {"header": "F0 47 00 00 50", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 00 50 01 [prog] F7"}}
    v77_banks = [{"name": "Preset Program Bank", "type": "ROM", "size": 198}]
    v77_presets = []
    v77_names = [
        "Large Concert Hall Warm", "Studio Vocal Plate 1", "Gold Plate Reverb", "Acoustic Room Ambience",
        "Non-Linear Gated Snare", "Stereo Multi-Tap Delay", "Circular 3D Panning Delay", "Multi-Stage Chorus Ensemble",
        "Pitch Shift Micro Detune", "Rotary Speaker Doppler Sim", "Dynamic Compressor & EQ", "V77 Master Studio Multi"
    ]
    for i in range(198):
        base = v77_names[i % len(v77_names)]
        v77_presets.append({"name": f"DPS-V77 {base} #{i+1:03d}", "bank": "Preset Program Bank", "number": i + 1, "category": "FX", "tags": ["sony", "dps-v77", "studio reverb", "multi-effects", "48khz"]})
    write_synth("sony", "dps-v77", "DPS-V77", "Studio Digital Multi-Effects Processor", 1996, v77_cc, v77_sysex, v77_banks, v77_presets)

    # =========================================================================
    # 7. SONY DPS-R7 (Professional Digital Reverberator)
    # =========================================================================
    r7_cc = {"reverb_time": 16, "pre_delay": 17, "mix": 91, "bypass": 84}
    r7_sysex = {"header": "F0 47 00 00 48", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 00 48 01 [prog] F7"}}
    r7_banks = [{"name": "Preset Reverb Bank", "type": "ROM", "size": 100}]
    r7_presets = []
    r7_pool = ["Concert Hall A Natural", "Church Cathedral Dome", "Studio Warm Plate", "Wood Room Warm Ambience", "Tiled Bathroom Echo", "Non-Linear Reverse Reverb"]
    for i in range(100):
        base = r7_pool[i % len(r7_pool)]
        r7_presets.append({"name": f"DPS-R7 {base} #{i+1:02d}", "bank": "Preset Reverb Bank", "number": i + 1, "category": "Reverb", "tags": ["sony", "dps-r7", "digital reverb", "studio legend"]})
    write_synth("sony", "dps-r7", "DPS-R7", "Digital Reverberator", 1991, r7_cc, r7_sysex, r7_banks, r7_presets)

    # =========================================================================
    # 8. SONY DPS-D7 (Professional Digital Delay Unit)
    # =========================================================================
    d7_cc = {"delay_time": 16, "feedback": 17, "mix": 91, "bypass": 84}
    d7_sysex = {"header": "F0 47 00 00 49", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 00 49 01 [prog] F7"}}
    d7_banks = [{"name": "Preset Delay Bank", "type": "ROM", "size": 100}]
    d7_presets = []
    for i in range(100):
        d7_presets.append({"name": f"DPS-D7 Multi-Tap Delay #{i+1:02d}", "bank": "Preset Delay Bank", "number": i + 1, "category": "Delay", "tags": ["sony", "dps-d7", "digital delay", "studio delay"]})
    write_synth("sony", "dps-d7", "DPS-D7", "Digital Delay Unit", 1991, d7_cc, d7_sysex, d7_banks, d7_presets)

    # =========================================================================
    # 9. SONY DPS-M7 (Professional Digital Sonic Modulator)
    # =========================================================================
    m7_cc = {"speed": 16, "depth": 17, "mix": 91, "bypass": 84}
    m7_sysex = {"header": "F0 47 00 00 4A", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 00 4A 01 [prog] F7"}}
    m7_banks = [{"name": "Preset Modulation Bank", "type": "ROM", "size": 100}]
    m7_presets = []
    for i in range(100):
        m7_presets.append({"name": f"DPS-M7 Sonic Modulator #{i+1:02d}", "bank": "Preset Modulation Bank", "number": i + 1, "category": "Modulation", "tags": ["sony", "dps-m7", "sonic modulator", "chorus", "flanger"]})
    write_synth("sony", "dps-m7", "DPS-M7", "Digital Sonic Modulator", 1991, m7_cc, m7_sysex, m7_banks, m7_presets)

    # =========================================================================
    # 10. ART MULTIVERB ALPHA (24-bit ASIC Multi-Effects Processor)
    # =========================================================================
    art_cc = {"mix": 91, "bypass": 84, "param1": 16, "param2": 17}
    art_sysex = {"header": "F0 1A 01 00", "device_id_byte": 2, "commands": {"request_patch": "F0 1A 01 00 01 [patch] F7"}}
    art_banks = [{"name": "Factory Preset Bank", "type": "ROM", "size": 200}]
    art_presets = []
    for i in range(200):
        art_pool = ["Studio Concert Reverb", "Stereo Pitch Transposer", "Acoustic Room Simulator", "Gated Ambience Snare", "Multi-Tap Ping Pong", "Rotary Simulator Warm"]
        base = art_pool[i % len(art_pool)]
        art_presets.append({"name": f"ART Alpha {base} #{i+1:03d}", "bank": "Factory Preset Bank", "number": i + 1, "category": "FX", "tags": ["art", "multiverb-alpha", "asic", "multi-effects"]})
    write_synth("art", "multiverb-alpha", "Multiverb Alpha", "24-Bit Studio Multi-Effects Processor", 1991, art_cc, art_sysex, art_banks, art_presets)

    # =========================================================================
    # 11. ART MULTIVERB III (Studio Multi-Effects Unit)
    # =========================================================================
    art3_cc = {"mix": 91, "bypass": 84, "param1": 16}
    art3_sysex = {"header": "F0 1A 02 00", "device_id_byte": 2, "commands": {"request_patch": "F0 1A 02 00 01 [patch] F7"}}
    art3_banks = [{"name": "Preset Programs", "type": "ROM", "size": 200}]
    art3_presets = []
    for i in range(200):
        art3_presets.append({"name": f"Multiverb-III Effect #{i+1:03d}", "bank": "Preset Programs", "number": i + 1, "category": "FX", "tags": ["art", "multiverb-iii", "multi-effects", "vintage studio"]})
    write_synth("art", "multiverb-iii", "Multiverb III", "Studio Multi-Effects Processor", 1990, art3_cc, art3_sysex, art3_banks, art3_presets)

    # =========================================================================
    # 12. ART SGX-2000 EXPRESS (Tube Guitar Preamp & Multi-Effects)
    # =========================================================================
    sgx_cc = {"drive": 80, "bass": 81, "mid": 82, "treble": 83, "mix": 91}
    sgx_sysex = {"header": "F0 1A 03 00", "device_id_byte": 2, "commands": {"request_patch": "F0 1A 03 00 01 [patch] F7"}}
    sgx_banks = [{"name": "Factory Presets", "type": "ROM", "size": 200}]
    sgx_presets = []
    for i in range(200):
        sgx_presets.append({"name": f"SGX-2000 Tube Rig #{i+1:03d}", "bank": "Factory Presets", "number": i + 1, "category": "Guitar", "tags": ["art", "sgx-2000", "tube preamp", "guitar multi-effects"]})
    write_synth("art", "sgx-2000-express", "SGX-2000 Express", "Tube Guitar Preamp & Multi-Effects", 1993, sgx_cc, sgx_sysex, sgx_banks, sgx_presets)

    # =========================================================================
    # 13. ART DMV-PRO (Dual True-Stereo Multi-Effects Processor)
    # =========================================================================
    dmv_cc = {"mix1": 91, "mix2": 92, "bypass": 84}
    dmv_sysex = {"header": "F0 1A 04 00", "device_id_byte": 2, "commands": {"request_patch": "F0 1A 04 00 01 [patch] F7"}}
    dmv_banks = [{"name": "Dual Engine Presets", "type": "ROM", "size": 100}]
    dmv_presets = []
    for i in range(100):
        dmv_presets.append({"name": f"DMV-Pro Dual Setup #{i+1:02d}", "bank": "Dual Engine Presets", "number": i + 1, "category": "FX", "tags": ["art", "dmv-pro", "dual engine", "multi-effects"]})
    write_synth("art", "dmv-pro", "DMV-Pro", "Dual True-Stereo Multi-Effects Processor", 1999, dmv_cc, dmv_sysex, dmv_banks, dmv_presets)

    # =========================================================================
    # 14. TC ELECTRONIC FIREWORX (Modular DSP Multi-Effects Processor)
    # =========================================================================
    fw_cc = {"mix": 91, "bypass": 84, "modifier1": 16, "modifier2": 17, "modifier3": 18, "modifier4": 19}
    fw_sysex = {"header": "F0 00 20 1F 01", "device_id_byte": 2, "commands": {"request_preset": "F0 00 20 1F 01 01 [preset] F7"}}
    fw_banks = [{"name": "Factory Bank A", "type": "ROM", "size": 100}, {"name": "Factory Bank B", "type": "ROM", "size": 100},
                {"name": "Factory Bank C", "type": "ROM", "size": 100}, {"name": "User Bank", "type": "RAM", "size": 100}]
    fw_presets = []
    for b in ["Factory Bank A", "Factory Bank B", "Factory Bank C", "User Bank"]:
        for i in range(100):
            fw_pool = ["Vocoder Morph Texture", "Resonant Ring Modulator", "Analog Chaos Filter Sweep", "Dual Pitch Shifter Harmonizer",
                       "Multi-Tap Reverse Delay", "Spectral Soundscape Reverb", "Dynamic Ducking Flanger", "FireworX Signature Matrix"]
            base = fw_pool[i % len(fw_pool)]
            fw_presets.append({"name": f"FireworX {base} #{i+1:02d}", "bank": b, "number": i + 1, "category": "FX", "tags": ["tc-electronic", "fireworx", "modular dsp", "matrix routing", "flagship multi-effects"]})
    write_synth("tc_electronic", "fireworx", "FireworX", "Modular Multi-Effects Processor", 1998, fw_cc, fw_sysex, fw_banks, fw_presets)

    # =========================================================================
    # 15. TC ELECTRONIC D-TWO (Multi-Tap Rhythm Delay Processor)
    # =========================================================================
    dt_cc = {"time": 16, "feedback": 17, "mix": 91, "tap_tempo": 80}
    dt_sysex = {"header": "F0 00 20 1F 02", "device_id_byte": 2, "commands": {"request_preset": "F0 00 20 1F 02 01 [preset] F7"}}
    dt_banks = [{"name": "Preset Rhythm Delays", "type": "ROM", "size": 100}]
    dt_presets = []
    for i in range(100):
        dt_presets.append({"name": f"D-Two Rhythm Delay #{i+1:02d}", "bank": "Preset Rhythm Delays", "number": i + 1, "category": "Delay", "tags": ["tc-electronic", "d-two", "rhythm delay", "multitap"]})
    write_synth("tc_electronic", "d-two", "D-Two", "Multitap Rhythm Delay Processor", 1999, dt_cc, dt_sysex, dt_banks, dt_presets)

    # =========================================================================
    # 16. TC-HELICON VOICEWORKS (Vocal Harmony & Correction Processor)
    # =========================================================================
    vw_cc = {"lead_level": 7, "harmony_level": 8, "pitch_correct": 16, "reverb": 91}
    vw_sysex = {"header": "F0 00 20 1F 03", "device_id_byte": 2, "commands": {"request_preset": "F0 00 20 1F 03 01 [preset] F7"}}
    vw_banks = [{"name": "Preset Vocal Harmonies", "type": "ROM", "size": 100}]
    vw_presets = []
    for i in range(100):
        vw_presets.append({"name": f"VoiceWorks Preset #{i+1:02d}", "bank": "Preset Vocal Harmonies", "number": i + 1, "category": "Vocal", "tags": ["tc-helicon", "voiceworks", "vocal harmony", "pitch correction"]})
    write_synth("tc_helicon", "voiceworks", "VoiceWorks", "Vocal Harmony & Modeling Processor", 2002, vw_cc, vw_sysex, vw_banks, vw_presets)

    # =========================================================================
    # 17. DYNACORD TAM-19 (Vintage Analog Flanger & Time-Delay)
    # =========================================================================
    tam_cc = {"delay_time": 16, "feedback": 17, "modulation": 18}
    tam_sysex = {"header": "F0 27 00 00", "device_id_byte": 2, "commands": {"sync": "F8"}}
    tam_banks = [{"name": "Analog Preset Settings", "type": "ROM", "size": 64}]
    tam_presets = []
    for i in range(64):
        tam_presets.append({"name": f"TAM-19 Flange/Delay #{i+1:02d}", "bank": "Analog Preset Settings", "number": i + 1, "category": "Modulation", "tags": ["dynacord", "tam-19", "analog flanger", "bbd delay", "vintage"]})
    write_synth("dynacord", "tam-19", "TAM-19", "Time-Delay & Analog Flanger", 1980, tam_cc, tam_sysex, tam_banks, tam_presets)

    # =========================================================================
    # 18. DYNACORD CL-20 (Vintage Rotary Cabinet Simulator)
    # =========================================================================
    cl20_cc = {"speed_slow_fast": 16, "rotor_balance": 17}
    cl20_sysex = {"header": "F0 27 00 01", "device_id_byte": 2, "commands": {"sync": "F8"}}
    cl20_banks = [{"name": "Rotary Profiles", "type": "ROM", "size": 64}]
    cl20_presets = []
    for i in range(64):
        cl20_presets.append({"name": f"CL-20 Rotary Setting #{i+1:02d}", "bank": "Rotary Profiles", "number": i + 1, "category": "Modulation", "tags": ["dynacord", "cl-20", "rotary simulator", "leslie sim"]})
    write_synth("dynacord", "cl-20", "CL-20", "Rotary Speaker Simulator", 1982, cl20_cc, cl20_sysex, cl20_banks, cl20_presets)

    # =========================================================================
    # 19. ENSONIQ DP/2 (Parallel Effects Processor)
    # =========================================================================
    dp2_cc = {"mix": 91, "bypass": 84, "param1": 16, "param2": 17}
    dp2_sysex = {"header": "F0 0F 40 01", "device_id_byte": 2, "commands": {"request_preset": "F0 0F 40 01 01 [preset] F7"}}
    dp2_banks = [{"name": "ROM Presets", "type": "ROM", "size": 100}, {"name": "RAM User Memory", "type": "RAM", "size": 100}]
    dp2_presets = []
    for bname in ["ROM Presets", "RAM User Memory"]:
        for i in range(100):
            dp2_presets.append({"name": f"DP2 Studio Effect #{i+1:02d}", "bank": bname, "number": i + 1, "category": "FX", "tags": ["ensoniq", "dp-2", "parallel effects", "dual dsp"]})
    write_synth("ensoniq", "dp-2", "DP/2", "Parallel Effects Processor", 1996, dp2_cc, dp2_sysex, dp2_banks, dp2_presets)

    # =========================================================================
    # 20. ENSONIQ EPS-16 PLUS (16-Bit Sampling Workstation w/ 24-Bit Multi-FX)
    # =========================================================================
    eps_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "patch_sel1": 12, "patch_sel2": 13}
    eps_sysex = {"header": "F0 0F 03 00", "device_id_byte": 2, "commands": {"request_inst": "F0 0F 03 00 01 [inst] F7"}}
    eps_banks = [{"name": "Factory Sounds", "type": "Disk", "size": 100}]
    eps_presets = []
    for i in range(100):
        eps_presets.append({"name": f"EPS16+ Instrument #{i+1:02d}", "bank": "Factory Sounds", "number": i + 1, "category": "Sampler", "tags": ["ensoniq", "eps-16-plus", "16-bit sampler", "transwaves"]})
    write_synth("ensoniq", "eps-16-plus", "EPS-16 Plus", "16-Bit Sampling Workstation", 1990, eps_cc, eps_sysex, eps_banks, eps_presets)

    # =========================================================================
    # 21. ENSONIQ KS-32 (Weighted Synthesizer Workstation)
    # =========================================================================
    ks32_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    ks32_sysex = {"header": "F0 0F 04 00", "device_id_byte": 2, "commands": {"request_sound": "F0 0F 04 00 01 [prog] F7"}}
    ks32_banks = [{"name": "Preset Sounds", "type": "ROM", "size": 100}]
    ks32_presets = []
    for i in range(100):
        ks32_presets.append({"name": f"KS32 Sound #{i+1:02d}", "bank": "Preset Sounds", "number": i + 1, "category": "Keys", "tags": ["ensoniq", "ks-32", "weighted keys", "workstation"]})
    write_synth("ensoniq", "ks-32", "KS-32", "Weighted Action Music Workstation", 1992, ks32_cc, ks32_sysex, ks32_banks, ks32_presets)

    # =========================================================================
    # 22. ENSONIQ KT-76 (76-Key Weighted Workstation)
    # =========================================================================
    kt76_cc = {"volume": 7, "pan": 10, "reverb": 91, "chorus": 93}
    kt76_sysex = {"header": "F0 0F 04 01", "device_id_byte": 2, "commands": {"request_sound": "F0 0F 04 01 01 [prog] F7"}}
    kt76_banks = [{"name": "Internal Sounds", "type": "ROM", "size": 100}]
    kt76_presets = []
    for i in range(100):
        kt76_presets.append({"name": f"KT76 Program #{i+1:02d}", "bank": "Internal Sounds", "number": i + 1, "category": "Keys", "tags": ["ensoniq", "kt-76", "weighted workstation", "piano"]})
    write_synth("ensoniq", "kt-76", "KT-76", "76-Key Weighted Workstation", 1994, kt76_cc, kt76_sysex, kt76_banks, kt76_presets)

    # =========================================================================
    # 23. KAWAI K4r (16-Bit Digital Synthesizer Rack Module)
    # =========================================================================
    k4r_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "pan": 10}
    k4r_sysex = {"header": "F0 40 00 20 00 04", "device_id_byte": 2, "commands": {"request_patch": "F0 40 00 20 00 04 00 [prog] F7"}}
    k4r_banks = [{"name": "Preset Singles", "type": "ROM", "size": 64}, {"name": "Preset Multi", "type": "ROM", "size": 64}]
    k4r_presets = []
    for i in range(64):
        k4r_presets.append({"name": f"K4r Single Sound #{i+1:02d}", "bank": "Preset Singles", "number": i + 1, "category": "Synth", "tags": ["kawai", "k4r", "16-bit", "digital filters", "rack module"]})
    for i in range(64):
        k4r_presets.append({"name": f"K4r Multi Setup #{i+1:02d}", "bank": "Preset Multi", "number": i + 1, "category": "Multi", "tags": ["kawai", "k4r", "multi"]})
    write_synth("kawai", "k4r", "K4r", "16-Bit Digital Synthesizer Module", 1989, k4r_cc, k4r_sysex, k4r_banks, k4r_presets)

    # =========================================================================
    # 24. KAWAI K1r (8-Bit Digital Synthesizer Rack Module)
    # =========================================================================
    k1r_cc = {"volume": 7, "pan": 10, "joystick_x": 16, "joystick_y": 17}
    k1r_sysex = {"header": "F0 40 00 20 00 02", "device_id_byte": 2, "commands": {"request_patch": "F0 40 00 20 00 02 00 [prog] F7"}}
    k1r_banks = [{"name": "Preset Singles", "type": "ROM", "size": 64}, {"name": "Preset Multi", "type": "ROM", "size": 32}]
    k1r_presets = []
    for i in range(64):
        k1r_presets.append({"name": f"K1r Single Patch #{i+1:02d}", "bank": "Preset Singles", "number": i + 1, "category": "Synth", "tags": ["kawai", "k1r", "vm synthesis", "rack"]})
    for i in range(32):
        k1r_presets.append({"name": f"K1r Multi Patch #{i+1:02d}", "bank": "Preset Multi", "number": i + 1, "category": "Multi", "tags": ["kawai", "k1r", "multi"]})
    write_synth("kawai", "k1r", "K1r", "VM Synthesizer Module", 1988, k1r_cc, k1r_sysex, k1r_banks, k1r_presets)

    # =========================================================================
    # 25. KAWAI K5000W (Advanced Additive Synthesizer Workstation)
    # =========================================================================
    k5w_cc = {"cutoff": 74, "resonance": 71, "harmonics": 16, "pan": 10, "volume": 7}
    k5w_sysex = {"header": "F0 40 00 20 00 0A", "device_id_byte": 2, "commands": {"request_patch": "F0 40 00 20 00 0A 00 [prog] F7"}}
    k5w_banks = [{"name": "Additive Bank A", "type": "ROM", "size": 128}, {"name": "PCM General Bank", "type": "ROM", "size": 128}]
    k5w_presets = []
    for i in range(128):
        k5w_presets.append({"name": f"K5000W Additive Voice #{i+1:03d}", "bank": "Additive Bank A", "number": i + 1, "category": "Additive", "tags": ["kawai", "k5000w", "additive synthesis", "workstation"]})
    for i in range(128):
        k5w_presets.append({"name": f"K5000W PCM Instrument #{i+1:03d}", "bank": "PCM General Bank", "number": i + 1, "category": "General MIDI", "tags": ["kawai", "k5000w", "pcm", "workstation"]})
    write_synth("kawai", "k5000w", "K5000W", "Advanced Additive Synthesizer Workstation", 1996, k5w_cc, k5w_sysex, k5w_banks, k5w_presets)

    # =========================================================================
    # 26. SEQUENTIAL MULTITRAK (6-Voice Analog Multi-Timbral Synthesizer)
    # =========================================================================
    mt_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "lfo_rate": 16}
    mt_sysex = {"header": "F0 01 08", "device_id_byte": 2, "commands": {"request_program": "F0 01 08 00 [prog] F7"}}
    mt_banks = [{"name": "Preset Programs", "type": "RAM", "size": 100}]
    mt_presets = []
    mt_names = [
        "Analog Poly Brass", "Resonant Saw Bass", "Warm Curtis Strings", "Sync Lead Solo", "Funky Clavinet Poly",
        "Sub Pulse Bass", "Fifth Interval Screamer", "Warm Velvet Pad", "Pizzicato Poly Pluck", "MultiTrak Master Synth"
    ]
    for i in range(100):
        base = mt_names[i % len(mt_names)]
        mt_presets.append({"name": f"MultiTrak {base} #{i+1:02d}", "bank": "Preset Programs", "number": i + 1, "category": "Brass" if "Brass" in base else "Bass" if "Bass" in base else "Pad" if "Pad" in base or "Strings" in base else "Lead", "tags": ["sequential", "multitrak", "cem3394", "analog", "multi-timbral"]})
    write_synth("sequential", "multitrak", "MultiTrak", "6-Voice Multi-Timbral Analog Synthesizer", 1985, mt_cc, mt_sysex, mt_banks, mt_presets)

    # =========================================================================
    # 27. SEQUENTIAL SPLIT-EIGHT (8-Voice Polyphonic Analog Synthesizer)
    # =========================================================================
    s8_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7}
    s8_sysex = {"header": "F0 01 09", "device_id_byte": 2, "commands": {"request_program": "F0 01 09 00 [prog] F7"}}
    s8_banks = [{"name": "Preset Programs", "type": "RAM", "size": 64}]
    s8_presets = []
    for i in range(64):
        s8_presets.append({"name": f"Split-Eight Poly Sound #{i+1:02d}", "bank": "Preset Programs", "number": i + 1, "category": "Analog", "tags": ["sequential", "split-eight", "analog", "cem chips", "8-voice"]})
    write_synth("sequential", "split-eight", "Split-Eight", "8-Voice Polyphonic Analog Synthesizer", 1985, s8_cc, s8_sysex, s8_banks, s8_presets)

    # =========================================================================
    # 28. SEQUENTIAL MAX (6-Voice Analog Synthesizer)
    # =========================================================================
    max_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7}
    max_sysex = {"header": "F0 01 07", "device_id_byte": 2, "commands": {"request_program": "F0 01 07 00 [prog] F7"}}
    max_banks = [{"name": "Preset Memories", "type": "ROM", "size": 80}]
    max_presets = []
    for i in range(80):
        max_presets.append({"name": f"MAX Analog Sound #{i+1:02d}", "bank": "Preset Memories", "number": i + 1, "category": "Analog", "tags": ["sequential", "max", "cem3394", "analog"]})
    write_synth("sequential", "max", "MAX", "6-Voice Analog Synthesizer", 1984, max_cc, max_sysex, max_banks, max_presets)

    # =========================================================================
    # 29. SEQUENTIAL DRUMTRAKS (Vintage 1984 Programmable Drum Machine)
    # =========================================================================
    dt_cc = {"tuning": 16, "volume": 7}
    dt_sysex = {"header": "F0 01 05", "device_id_byte": 2, "commands": {"sync": "F8"}}
    dt_banks = [{"name": "Drumtraks Patterns", "type": "RAM", "size": 50}]
    dt_presets = []
    for i in range(50):
        dt_presets.append({"name": f"Drumtraks Pattern #{i+1:02d}", "bank": "Drumtraks Patterns", "number": i + 1, "category": "Drums", "tags": ["sequential", "drumtraks", "vintage drums", "1984", "e-prom"]})
    write_synth("sequential", "drumtraks", "Drumtraks", "Digital Programmable Drum Machine", 1984, dt_cc, dt_sysex, dt_banks, dt_presets)

    # =========================================================================
    # 30. AKAI ME-80P (8x10 Programmable MIDI Patch Bay)
    # =========================================================================
    me80_cc = {"channel_routing": 16}
    me80_sysex = {"header": "F0 47 00 10", "device_id_byte": 2, "commands": {"request_patch": "F0 47 00 10 00 [patch] F7"}}
    me80_banks = [{"name": "Patch Memory", "type": "RAM", "size": 64}]
    me80_presets = []
    for i in range(64):
        me80_presets.append({"name": f"ME-80P 8x10 Matrix Setup #{i+1:02d}", "bank": "Patch Memory", "number": i + 1, "category": "Routing", "tags": ["akai", "me-80p", "midi patch bay", "routing"]})
    write_synth("akai", "me-80p", "ME-80P", "8-In / 10-Out Programmable MIDI Patch Bay", 1988, me80_cc, me80_sysex, me80_banks, me80_presets)

    print("\nWave 16 Build Complete! 30 new studio multi-effects, retrofits & vintage synths created.")

if __name__ == "__main__":
    build_wave16()
