#!/usr/bin/env python3
"""
Wave 12 Vintage Samplers, Vector Synthesizers & Digital Classics Generator for OmniPatch:
- Casio: VZ-1 (iPD flagship), HT-6000 (SD analog VCF), FZ-1 (16-bit sampler)
- Akai: AX80 (hybrid analog), VX600 (CEM/SSM matrix analog), AX73 (CEM analog), S950 (12-bit sampler), S1000 (16-bit sampler)
- Korg: Radias (MMT synth), M3 (HD-1 KARMA workstation), 03R/W (AI2 module), 707 (FM synth), DSS-1 (analog filter sampler), DW-6000 (DCO analog filter), Poly-61 (analog DCO)
- Roland: JD-08 (Boutique JD-800), JU-06A (Boutique Juno-60/106), JX-08 (Boutique JX-8P), U-20 (RS-PCM), CM-32L (LA sound canvas module)
- Yamaha: CS6x (AWM2/PLG dance synth), SY85 (AWM2 workstation), TG33 (Vector synth), FB-01 (4-op FM), V50 (4-op FM workstation)
- E-MU: Morpheus (14-pole Z-plane), Audity 2000 (64-voice digital), Orbit (Dance Planet 9090)
- Ensoniq: DP/4 (4-unit parallel multi-effects), ASR-10 (Advanced Sampling Recorder)
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

def build_wave12():
    print("Building Wave 12: Casio VZ/HT/FZ, Akai AX/VX/S-Series, Korg Radias/M3/DSS/707, Roland Boutiques/U-20/CM-32L, Yamaha CS6x/SY85/TG33/FB-01/V50, E-MU Morpheus/Audity/Orbit, Ensoniq DP-4/ASR-10...")

    # =========================================================================
    # 1. CASIO VZ-1 (Interactive Phase Distortion iPD Flagship)
    # =========================================================================
    vz1_cc = {"volume": 7, "pan": 10, "expression": 11, "mod_wheel": 1, "sustain": 64, "aftertouch_depth": 70, "slider1": 16}
    vz1_sysex = {"header": "F0 44 03 00", "device_id_byte": 2, "commands": {"request_patch": "F0 44 03 00 70 [prog] F7"}}
    vz1_banks = [{"name": "Internal Normal", "type": "Normal", "size": 64}, {"name": "Operation Memory", "type": "Multi", "size": 64}]
    vz1_presets = []
    vz1_names = [
        "Acoustic Piano 1", "Honky Tonk Piano", "E-Piano 1 (Dyno)", "E-Piano 2 (FM Bell)", "Clavichord", "Harpsichord",
        "Pipe Organ 1", "Jazz Organ B3", "Accordion", "Nylon Guitar", "Steel Guitar", "12-String Guitar", "Jazz Guitar",
        "Overdrive Guitar", "Slap Bass 1", "Fretless Bass", "Wood Bass", "Synth Bass 1", "Synth Bass 2", "Violin Solo",
        "Cello Solo", "String Ensemble 1", "String Ensemble 2", "Warm Strings", "Pizzicato Strings", "Trumpet 1",
        "Mute Trumpet", "Trombone", "French Horn", "Brass Ensemble 1", "Brass Ensemble 2", "Synth Brass 1", "Flute",
        "Clarinet", "Oboe", "Bassoon", "Pan Flute", "Shakuhachi", "Whistle", "Square Lead", "Saw Lead", "Sync Lead",
        "Digital Sweep", "Reso Sweep", "Metallic Pad", "Atmosphere Pad", "Cosmic Bell", "Marimba", "Vibraphone",
        "Glockenspiel", "Tubular Bell", "Steel Drum", "Koto", "Sitar", "Kalimba", "Timpani", "Snare Drum", "Bass Drum",
        "Hi-Hat/Ride", "Fantasy Voice", "Glass Chime", "Space Drone", "Wind FX", "Laser Perc"
    ]
    for i, name in enumerate(vz1_names):
        cat = "Keys" if "Piano" in name or "Clav" in name or "Organ" in name else "Bass" if "Bass" in name else "Strings" if "String" in name or "Violin" in name else "Brass" if "Trumpet" in name or "Brass" in name else "Lead" if "Lead" in name else "Pad"
        vz1_presets.append({"name": f"VZ {name}", "bank": "Internal Normal", "number": i + 1, "category": cat, "tags": ["casio", "ipd", "interactive phase distortion", "vintage"]})
    for i in range(64):
        vz1_presets.append({"name": f"VZ Operation Combo {i+1:02d}", "bank": "Operation Memory", "number": i + 1, "category": "Multi", "tags": ["casio", "ipd", "combination", "layer"]})
    write_synth("casio", "vz-1", "VZ-1 / VZ-10M", "Interactive Phase Distortion Synthesizer", 1988, vz1_cc, vz1_sysex, vz1_banks, vz1_presets)

    # =========================================================================
    # 2. CASIO HT-6000 (Spectrum Dynamic Synth w/ 8 Analog NJM2090 Resonant VCFs)
    # =========================================================================
    ht_cc = {"filter_cutoff": 74, "filter_resonance": 71, "dca_decay": 72, "mod_depth": 1, "volume": 7}
    ht_sysex = {"header": "F0 44 02 00", "device_id_byte": 2, "commands": {"request_tone": "F0 44 02 00 00 [tone] F7"}}
    ht_banks = [{"name": "Preset Sounds", "type": "ROM", "size": 30}, {"name": "Lower Tones", "type": "ROM", "size": 34}]
    ht_presets = []
    ht_names = [
        "SD Piano 1", "SD Honky Tonk", "Electric Piano 1", "Harpsichord 1", "Pipe Organ", "Electronic Organ",
        "Accordion 1", "Vibraphone", "Marimba", "Acoustic Guitar", "Koto", "SD Strings 1", "Warm Strings",
        "Violin", "Cello", "Trumpet", "Trombone", "Brass Ensemble 1", "Synth Brass", "Flute", "Clarinet",
        "Oboe", "Harmonica", "Whistle", "Synthesizer Lead", "Cosmic Sound", "Metallic Sound", "Analog Bass",
        "Slap Bass", "Synth Bass 1"
    ]
    for i, name in enumerate(ht_names):
        ht_presets.append({"name": f"HT6K {name}", "bank": "Preset Sounds", "number": i + 1, "category": "Keys" if "Piano" in name else "Bass" if "Bass" in name else "Brass" if "Brass" in name else "Synth", "tags": ["casio", "analog filter", "njm2090", "spectrum dynamic"]})
    for i in range(34):
        ht_presets.append({"name": f"HT6K Lower Bass/Comp {i+1:02d}", "bank": "Lower Tones", "number": i + 1, "category": "Bass", "tags": ["casio", "accompaniment", "bass"]})
    write_synth("casio", "ht-6000", "HT-6000", "Polyphonic SD Synthesizer with Analog VCF", 1987, ht_cc, ht_sysex, ht_banks, ht_presets)

    # =========================================================================
    # 3. CASIO FZ-1 (16-bit Sampling Synthesizer with Resonant Digital Filters)
    # =========================================================================
    fz_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "pan": 10, "mod_wheel": 1}
    fz_sysex = {"header": "F0 44 04 00", "device_id_byte": 2, "commands": {"request_voice": "F0 44 04 00 01 [voice] F7"}}
    fz_banks = [{"name": "Factory Bank A", "type": "ROM/Disk", "size": 32}, {"name": "Factory Bank B", "type": "ROM/Disk", "size": 32}]
    fz_presets = []
    fz_names = [
        "Concert Grand 1", "Studio Grand", "CP-80 Electric", "DX Fender Rhodes", "Dyno Rhodes", "Wurlitzer 200A",
        "Hammond B3 Rock", "Church Pipe Organ", "Nylon Classical", "Stratocaster Clean", "Telecaster Crunch",
        "Precision Finger Bass", "Fretless Bass Solo", "Moog Minibass", "Analog Reso Bass", "Symphonic Strings 1",
        "Pizzicato Ensemble", "Solo Cello Agitato", "Solo Violin Vibrato", "Section French Horns", "Tight Brass Stabs",
        "Orchestral Trumpet", "Tenor Saxophone", "Concert Flute", "Panpipe Chiff", "Square Wave Waveform",
        "Sawtooth Harmonic Wave", "Resonant Sweep Pad", "Digital Bell Choir", "Tubular Bells Chime", "Orchestra Hit Slam", "Industrial Metal Clang"
    ]
    for i, name in enumerate(fz_names):
        fz_presets.append({"name": f"FZ1 {name}", "bank": "Factory Bank A", "number": i + 1, "category": "Sampler", "tags": ["casio", "16-bit", "sampling", "resonant filter"]})
        fz_presets.append({"name": f"FZ1 Studio {name}", "bank": "Factory Bank B", "number": i + 1, "category": "Sampler", "tags": ["casio", "16-bit", "sampling", "sound library"]})
    write_synth("casio", "fz-1", "FZ-1 / FZ-10M", "16-bit Sampling Synthesizer", 1987, fz_cc, fz_sysex, fz_banks, fz_presets)

    # =========================================================================
    # 4. AKAI AX80 (8-Voice Dual-Curtis CEM Analog Polyphonic Synthesizer)
    # =========================================================================
    ax80_cc = {"filter_cutoff": 74, "filter_resonance": 71, "lfo_depth": 1, "volume": 7, "env_attack": 73, "env_release": 72}
    ax80_sysex = {"header": "F0 47 00 00", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 00 40 [prog] F7"}}
    ax80_banks = [{"name": "Preset Programs", "type": "ROM", "size": 64}]
    ax80_presets = []
    ax80_names = [
        "Electric Grand Piano", "Honky Tonk Piano", "Clavinet D6", "Pipe Organ Full", "Rotary Jazz Organ",
        "Funky Slap Bass", "Growl Bass CEM", "Reso Sweep Bass", "Sub Pulse Bass", "Punchy Electro Bass",
        "Strings Ensemble Slow", "Strings Ensemble Fast", "Warm Analog Strings", "Solo Violin Vibrato",
        "Poly Brass Section", "Bright Horn Fanfare", "Synth Brass 80s", "Power Synth Brass",
        "Sync Lead Screamer", "Sawtooth Soloist", "Square PWM Lead", "Guitar-Like Solo", "Fifth Interval Lead",
        "Analog Flute", "Whistle Solo", "Resonant Filter Sweep", "Cosmic Space FX", "Metallic Bell Chime",
        "Warm Poly Pad", "Matrix Sweep Pad", "Harpsichord Poly", "Soft Velvet Poly",
        "Punch Clav Synth", "Organ Percussive", "Brite Electric Piano", "Chorus Rhodes", "Vintage String Orchestra",
        "Spit Brass 1", "Moog-ish Saw Bass", "Heavy Punch Bass", "Funk Clavinet", "Warm Mellow Pad",
        "Bright Sync Mod", "Glissando Lead", "Alien Wind Effect", "Laser Attack FX", "Polyphonic Arp Sound",
        "Vibraphone Perc", "Marimba Sound", "Glockenspiel Poly", "Church Bell Toll", "Stereo Poly Sweep",
        "Fat PWM Strings", "Octave Brass Hit", "Sawtooth Poly Chord", "Dual VCO Lead", "Filtered Pulse Clav",
        "Reso Bubble FX", "Detuned Fifth Lead", "High Velocity Brass", "Sub Octave Bassline", "LFO Sweep Texture",
        "Sci-Fi Computer Noise", "AX80 Signature Poly"
    ]
    for i, name in enumerate(ax80_names):
        cat = "Bass" if "Bass" in name else "Brass" if "Brass" in name or "Horn" in name else "Strings" if "Strings" in name or "Violin" in name else "Lead" if "Lead" in name or "Solo" in name else "Pad" if "Pad" in name or "Warm" in name else "Keys"
        ax80_presets.append({"name": f"AX80 {name}", "bank": "Preset Programs", "number": i + 1, "category": cat, "tags": ["akai", "ax80", "analog", "cem3372", "vco"]})
    write_synth("akai", "ax80", "AX80", "8-Voice Polyphonic Analog Synthesizer", 1984, ax80_cc, ax80_sysex, ax80_banks, ax80_presets)

    # =========================================================================
    # 5. AKAI VX600 (6-Voice Matrix Analog Synthesizer w/ CEM3374 & SSM2044)
    # =========================================================================
    vx6_cc = {"filter_cutoff": 74, "filter_resonance": 71, "mod_wheel": 1, "aftertouch": 2, "volume": 7, "expression": 11}
    vx6_sysex = {"header": "F0 47 00 24", "device_id_byte": 2, "commands": {"request_patch": "F0 47 00 24 40 [patch] F7"}}
    vx6_banks = [{"name": "Factory Sounds", "type": "ROM/RAM", "size": 100}]
    vx6_presets = []
    for i in range(100):
        names_pool = ["SSM Filter Lead", "CEM Fat Saw Brass", "Oberheim Poly String", "Matrix Reso Sweep", "Analog Wind Horn",
                      "Sub Pulse Punch Bass", "Sync Detune Screamer", "Warm SSM Velvet Pad", "Dynamic Aftertouch Pluck", "Wind Controller EWI Solo"]
        base = names_pool[i % len(names_pool)]
        vx6_presets.append({"name": f"VX600 {base} #{i+1:02d}", "bank": "Factory Sounds", "number": i + 1, "category": "Lead" if "Lead" in base or "Solo" in base else "Bass" if "Bass" in base else "Pad", "tags": ["akai", "vx600", "ssm2044", "cem3374", "matrix analog"]})
    write_synth("akai", "vx600", "VX600", "6-Voice Matrix Analog Synthesizer", 1988, vx6_cc, vx6_sysex, vx6_banks, vx6_presets)

    # =========================================================================
    # 6. AKAI AX73 / VX90 (6-Voice Analog Synthesizer w/ CEM3394)
    # =========================================================================
    ax73_cc = {"filter_cutoff": 74, "filter_resonance": 71, "vco_pwm": 70, "volume": 7, "lfo_depth": 1}
    ax73_sysex = {"header": "F0 47 00 13", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 13 40 [prog] F7"}}
    ax73_banks = [{"name": "Factory Memory", "type": "RAM", "size": 100}]
    ax73_presets = []
    for i in range(100):
        pnames = ["Fat CEM Brass", "Warm Analog Strings", "Deep Sawtooth Bass", "Resonant Filter Pluck", "Punchy PWM Poly",
                  "Sync Modulation Lead", "Octave Synth Solo", "Velvet Dark Pad", "Percussive Clavinet", "Sci-Fi Noise Sweep"]
        base = pnames[i % len(pnames)]
        ax73_presets.append({"name": f"AX73 {base} #{i+1:02d}", "bank": "Factory Memory", "number": i + 1, "category": "Brass" if "Brass" in base else "Bass" if "Bass" in base else "Pad" if "Pad" in base or "Strings" in base else "Lead", "tags": ["akai", "ax73", "vx90", "cem3394", "analog"]})
    write_synth("akai", "ax73", "AX73 / VX90", "6-Voice Analog Synthesizer", 1986, ax73_cc, ax73_sysex, ax73_banks, ax73_presets)

    # =========================================================================
    # 7. AKAI S950 (12-bit Studio Sampler with Variable Rate & Timestretch)
    # =========================================================================
    s950_cc = {"volume": 7, "pan": 10, "filter_cutoff": 74, "mod_wheel": 1, "pitch_bend": 0}
    s950_sysex = {"header": "F0 47 00 20", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 20 01 [prog] F7"}}
    s950_banks = [{"name": "Standard Library", "type": "Disk", "size": 64}]
    s950_presets = []
    s950_names = [
        "950 Classic Hip Hop Kick", "950 Gritty Snare", "Crisp 12-Bit Hi-Hats", "LinnDrum Studio Kit",
        "Acoustic Upright Bass", "Slap Funk Bass 12-Bit", "Moog Rogue Sub Bass", "TR-808 Boomy Kick",
        "Fender Rhodes Mark I", "Wurlitzer 200 Vintage", "Stereo Grand Piano 12B", "B3 Jazz Percussive Organ",
        "S950 Timestretched Vocal Hook", "Amen Break Sliced Kit", "Funky Drummer Loop Slices", "Soul Horn Hits",
        "Symphonic Cello Section", "Staccato Violin Plucks", "Analog Synthesizer Saw Pad", "Warm Reso Filter Sweep",
        "Flute Mellotron Sample", "Dub Siren FX Drop", "Industrial Metal Clank", "Reverse Cymbal Wash",
        "Slap Tongue Sax Hit", "Electric Jazz Guitar Chords", "Orchestra Hit Stabs", "Dark Ambient Sub Drone",
        "Sci-Fi Timestretch Drone", "Boom Bap Percussion Multi", "Vinyl Crackle Vinyl Loop", "80s Pop Brass Chords",
        "Deep 808 Sine Bass", "Jungle Timestretched Vocal", "Funk Finger Bass", "Electro Clap Multi",
        "Reggae Skank Guitar", "Latin Percussion Shakers", "Conga Tumba Bongo Set", "Steel Pan Caribbean",
        "Marimba Wooden Pluck", "Tubular Bell Tolling", "Glockenspiel Studio", "Vibraphone Motor On",
        "Vintage Accordion Squeeze", "Tenor Sax Solo Breath", "Mute Trumpet Miles Style", "Trombone Fall Hit",
        "Orchestral Timpani Roll", "Stadium Rock Tom Kit", "Electronic Gate Snare", "Filtered White Noise Rise",
        "Laser Zap FX Drop", "Subharmonic Earth Shake", "Space Chamber Reverb Tail", "Choir Aahs Sample",
        "Choir Oohs Mellotron", "Female Vocal Breath", "Dancefloor Piano Stabs", "House Organ Bassline",
        "Analog Pulse Lead 950", "Square Wave Chiptune", "Downsampled 8-Bit Lo-Fi", "S950 Ultimate Master Kit"
    ]
    for i, name in enumerate(s950_names):
        cat = "Drums" if "Kit" in name or "Snare" in name or "Kick" in name or "Break" in name or "Perc" in name else "Bass" if "Bass" in name else "Keys" if "Piano" in name or "Rhodes" in name or "Organ" in name else "FX" if "FX" in name or "Drone" in name else "Sampler"
        s950_presets.append({"name": f"S950 {name}", "bank": "Standard Library", "number": i + 1, "category": cat, "tags": ["akai", "s950", "12-bit", "sampler", "hip hop", "timestretch"]})
    write_synth("akai", "s950", "S950", "12-Bit Professional MIDI Sampler", 1988, s950_cc, s950_sysex, s950_banks, s950_presets)

    # =========================================================================
    # 8. AKAI S1000 (Industry Standard 16-bit Stereo Sampler)
    # =========================================================================
    s1k_cc = {"volume": 7, "pan": 10, "expression": 11, "filter_cutoff": 74, "filter_resonance": 71}
    s1k_sysex = {"header": "F0 47 00 28", "device_id_byte": 2, "commands": {"request_program": "F0 47 00 28 01 [prog] F7"}}
    s1k_banks = [{"name": "Factory Sound Bank", "type": "ROM/Disk", "size": 100}]
    s1k_presets = []
    for i in range(100):
        base_names = ["Stereo Concert Grand", "Pop Studio Drums Multi", "Slap & Finger Bass Split", "Full String Orchestra",
                      "Section Horns Stabs", "Dyno Rhodes Electric Piano", "Choir Boys & Female Voices", "Warm Analog Saw Swell",
                      "Electric Clean Stratocaster", "Acoustic Nylon Guitar Plucks"]
        name = f"S1000 {base_names[i % len(base_names)]} {i//10 + 1}"
        s1k_presets.append({"name": name, "bank": "Factory Sound Bank", "number": i + 1, "category": "Sampler", "tags": ["akai", "s1000", "16-bit", "stereo sampler", "industry standard"]})
    write_synth("akai", "s1000", "S1000", "16-Bit Stereo Digital Sampler", 1988, s1k_cc, s1k_sysex, s1k_banks, s1k_presets)

    # =========================================================================
    # 9. KORG RADIAS (MMT Multi Modeling Technology Synthesizer & Vocoder)
    # =========================================================================
    radias_cc = {"filter_cutoff": 74, "filter_resonance": 71, "drive": 80, "osc1_ctrl1": 14, "osc1_ctrl2": 15, "pan": 10, "volume": 7}
    radias_sysex = {"header": "F0 42 30 72", "device_id_byte": 2, "commands": {"request_program": "F0 42 30 72 10 [bank] [prog] F7"}}
    radias_banks = [{"name": f"Bank {chr(65+b)}", "type": "RAM", "size": 16} for b in range(16)]
    radias_presets = []
    preset_counter = 1
    for b in range(16):
        bname = f"Bank {chr(65+b)}"
        for p in range(16):
            rnames = ["MMT SuperSaw Lead", "Formant Vocal Vocoder", "VPM Cross Mod Poly", "Analog Sub Kick Bass", "Comb Filtered Pluck",
                      "Step Sequencer Groove", "Vintage 24dB Moog Saw", "Reso Pulse Sync Solo", "Modulated Drone Pad", "Virtual Motion Arp",
                      "Drum PCM Electro Kit", "Drive Distortion Screamer", "Warm Poly String Brass", "BPM Delay Atmosphere", "Chirp Bell Ring Mod", "Radias Flagship Poly"]
            name = f"RAD {rnames[p]} {chr(65+b)}{p+1:02d}"
            radias_presets.append({"name": name, "bank": bname, "number": p + 1, "category": "Lead" if "Lead" in name or "Solo" in name else "Pad" if "Pad" in name or "String" in name else "Bass" if "Bass" in name else "Synth", "tags": ["korg", "radias", "mmt", "virtual analog", "vocoder"]})
            preset_counter += 1
    write_synth("korg", "radias", "Radias", "MMT Multi Modeling Synthesizer / Vocoder", 2006, radias_cc, radias_sysex, radias_banks, radias_presets)

    # =========================================================================
    # 10. KORG M3 (HD-1 High Definition Synthesizer Workstation w/ KARMA 2.0)
    # =========================================================================
    m3_cc = {"filter_cutoff": 74, "filter_resonance": 71, "karma_sw": 22, "slider1": 16, "slider2": 17, "volume": 7, "pan": 10}
    m3_sysex = {"header": "F0 42 30 68", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 68 1C [bank] [prog] F7"}}
    m3_banks = [{"name": f"Bank {chr(65+b)}", "type": "HD-1 Programs", "size": 128} for b in range(4)]
    m3_presets = []
    for b in range(4):
        bname = f"Bank {chr(65+b)}"
        for p in range(128):
            m3_names_pool = ["M3 Concert Grand Piano", "KARMA Motion Arp Groove", "HD-1 Multi-Osc Poly Pad", "Deep Nu-Age Acoustic Bass",
                             "Symphonic Brass Ensemble", "Vintage Tremolo Rhodes", "Distortion Solo Lead", "Ethnic World Sitar Pad",
                             "Punchy Electronic Beat Kit", "Vocal Morph Choir Swell", "Sweet Soprano Sax Lead", "Staccato String Run",
                             "Warm 4-Pole Analog Poly", "Ambient Soundscape Waves", "Tubular Bell Chime Hit", "Resonant Step Techno Bass"]
            base = m3_names_pool[p % len(m3_names_pool)]
            m3_presets.append({"name": f"M3 {base} {chr(65+b)}{p+1:03d}", "bank": bname, "number": p + 1, "category": "Keys" if "Piano" in base or "Rhodes" in base else "Bass" if "Bass" in base else "Pad" if "Pad" in base or "Waves" in base else "Lead" if "Lead" in base else "KARMA", "tags": ["korg", "m3", "hd-1", "karma", "workstation"]})
    write_synth("korg", "m3", "M3", "Expanded HD-1 Workstation with KARMA 2.0", 2007, m3_cc, m3_sysex, m3_banks, m3_presets)

    # =========================================================================
    # 11. KORG 03R/W (AI2 Synthesis Multi-Timbral Module)
    # =========================================================================
    k03_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_depth": 91, "chorus_depth": 93, "filter_cutoff": 74}
    k03_sysex = {"header": "F0 42 30 36", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 36 10 [bank] [prog] F7"}}
    k03_banks = [{"name": "ROM Programs", "type": "ROM", "size": 100}, {"name": "ROM Combinations", "type": "ROM", "size": 100}]
    k03_presets = []
    for i in range(100):
        k03_presets.append({"name": f"03RW Program {i+1:02d}", "bank": "ROM Programs", "number": i + 1, "category": "Synth", "tags": ["korg", "03rw", "ai2", "rompler"]})
        k03_presets.append({"name": f"03RW Combo {i+1:02d}", "bank": "ROM Combinations", "number": i + 1, "category": "Multi", "tags": ["korg", "03rw", "ai2", "combination"]})
    write_synth("korg", "03r-w", "03R/W", "AI2 Synthesis Sound Module", 1992, k03_cc, k03_sysex, k03_banks, k03_presets)

    # =========================================================================
    # 12. KORG 707 (4-Operator FM Synthesizer with Performance Sliders)
    # =========================================================================
    k707_cc = {"filter_cutoff": 74, "filter_resonance": 71, "mod_wheel": 1, "volume": 7, "slider1": 16}
    k707_sysex = {"header": "F0 42 30 19", "device_id_byte": 2, "commands": {"request_voice": "F0 42 30 19 10 [voice] F7"}}
    k707_banks = [{"name": "Internal Voice Bank", "type": "RAM", "size": 100}]
    k707_presets = []
    for i in range(100):
        fm_pool = ["Solid FM Bass", "Bell Electric Piano", "Punchy Clavinet", "FM Brass Section", "Warm FM Strings",
                   "Harpsichord Crisp", "Jazz Organ Perc", "Metallic Chime Pad", "Sync Screamer FM", "Glass Marimba"]
        base = fm_pool[i % len(fm_pool)]
        k707_presets.append({"name": f"707 {base} {i+1:02d}", "bank": "Internal Voice Bank", "number": i + 1, "category": "Bass" if "Bass" in base else "Keys" if "Piano" in base or "Organ" in base else "Lead" if "Screamer" in base else "Pad", "tags": ["korg", "707", "ds-8", "fm synthesis", "4-op"]})
    write_synth("korg", "707", "707 / DS-8", "4-Operator FM Performance Synthesizer", 1987, k707_cc, k707_sysex, k707_banks, k707_presets)

    # =========================================================================
    # 13. KORG DSS-1 (12-bit Sampling Synthesizer with Resonant NJM2069 Filters)
    # =========================================================================
    dss_cc = {"filter_cutoff": 74, "filter_resonance": 71, "eg_attack": 73, "eg_decay": 75, "volume": 7}
    dss_sysex = {"header": "F0 42 30 0B", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 0B 10 [prog] F7"}}
    dss_banks = [{"name": f"System Bank {chr(65+b)}", "type": "Disk", "size": 32} for b in range(4)]
    dss_presets = []
    for b in range(4):
        bname = f"System Bank {chr(65+b)}"
        for p in range(32):
            dss_pool = ["Concert Grand DSS", "Warm NJM2069 Analog Strings", "Draw Wave Harmonic Bell", "Punchy 12-Bit Slap Bass",
                        "Resonant Analog Filter Sweep", "Stereo Brass Ensemble", "Acoustic Nylon Guitar", "Mellotron Flute Chiff",
                        "Fat Dual Delay Poly Lead", "Sync Mod Drone Texture"]
            base = dss_pool[p % len(dss_pool)]
            dss_presets.append({"name": f"DSS1 {base} {chr(65+b)}{p+1:02d}", "bank": bname, "number": p + 1, "category": "Sampler", "tags": ["korg", "dss-1", "12-bit", "njm2069", "analog filter", "additive"]})
    write_synth("korg", "dss-1", "DSS-1 / DSM-1", "12-Bit Sampling Synthesizer with Analog Filters", 1986, dss_cc, dss_sysex, dss_banks, dss_presets)

    # =========================================================================
    # 14. KORG DW-6000 (Digital Waveform Synthesizer with NJM2069 VCF)
    # =========================================================================
    dw6_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "chorus_depth": 93}
    dw6_sysex = {"header": "F0 42 30 04", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 04 10 [prog] F7"}}
    dw6_banks = [{"name": "Preset Programs", "type": "RAM", "size": 64}]
    dw6_presets = []
    dw6_names = [
        "Acoustic Piano 1", "Honky Tonk Piano", "Electric Piano DW", "Clavinet DCO", "Pipe Organ Full", "Jazz Organ B3",
        "Accordion Sound", "Harpsichord Poly", "Vibraphone Perc", "Marimba Sound", "Acoustic Guitar", "Electric Guitar",
        "Upright Wood Bass", "Slap Funk Bass", "Synthesizer Reso Bass", "Warm Poly Strings 1", "Slow Attack Strings",
        "Violin Vibrato", "Cello Ensemble", "Trumpet Fanfare", "Trombone Section", "French Horn Poly", "Analog Synth Brass 1",
        "Punchy Horn Stabs", "Concert Flute", "Clarinet Solo", "Pan Flute Breath", "Oboe Soloist", "Harmonica Chime",
        "Whistle Solo", "Resonant Sweep Lead", "Dual Osc Fat Solo", "Fifth Interval Lead", "Cosmic Space Bell",
        "Metallic Texture", "Digital Chime Pad", "Warm Velvet Pad", "Plucked Harp Poly", "Percussive Clav Sound",
        "Octave Lead Screamer", "Sub Octave Pulse Bass", "Detuned Poly Saw", "Chorus Electric Piano", "Cathedral Organ",
        "Rock Organ Distortion", "Classic DW Brass", "Spit Brass Hit", "Orchestra Hit Chord", "Staccato Pluck Poly",
        "Sci-Fi Laser Gun", "Alien Wind Ambience", "Bubble Filter Sweep", "Analog Clav Solo", "Mellow Woodwind",
        "Bright Poly Synth", "Square Lead Vintage", "PWM Slow Strings", "Punchy Disco Bass", "Low Sub Drone",
        "Digital Bells Sparkle", "Crystal Glasses Pad", "Tubular Bells Toll", "White Noise Jet Sweep", "DW6000 Master Signature"
    ]
    for i, name in enumerate(dw6_names):
        cat = "Keys" if "Piano" in name or "Organ" in name or "Clav" in name else "Bass" if "Bass" in name else "Strings" if "Strings" in name or "Violin" in name else "Brass" if "Brass" in name or "Horn" in name else "Lead" if "Lead" in name or "Solo" in name else "Pad"
        dw6_presets.append({"name": f"DW6K {name}", "bank": "Preset Programs", "number": i + 1, "category": cat, "tags": ["korg", "dw-6000", "dwgs", "analog filter", "njm2069"]})
    write_synth("korg", "dw-6000", "DW-6000", "Digital Waveform Synthesizer with Analog Filters", 1985, dw6_cc, dw6_sysex, dw6_banks, dw6_presets)

    # =========================================================================
    # 15. KORG POLY-61 (Polyphonic Analog DCO Synthesizer)
    # =========================================================================
    p61_cc = {"filter_cutoff": 74, "filter_resonance": 71, "dco2_tune": 70, "volume": 7, "arp_rate": 14}
    p61_sysex = {"header": "F0 42 30 01", "device_id_byte": 2, "commands": {"request_prog": "F0 42 30 01 10 [prog] F7"}}
    p61_banks = [{"name": "Preset Memories", "type": "RAM", "size": 64}]
    p61_presets = []
    p61_names = [
        "Poly-61 Brass Ensemble", "Punchy 80s Horns", "Reso Synth Brass", "Warm Analog Strings 1", "Fast Attack Strings",
        "Polyphonic Pipe Organ", "Classic Rock Organ", "Electric Piano Tone", "Funky Clavinet Poly", "Harpsichord Crisp",
        "Deep Resonant Bass", "Sub Octave DCO Bass", "Punchy Slap Bass", "Analog Lead Solo 1", "Sawtooth Sync Lead",
        "Dual DCO Detune Poly", "Fifth Interval Synth", "Warm Velvet Pad", "High Pass Sweep", "Arpeggiator Pluck Tone",
        "Percussive Bell Synth", "Vibraphone Analog", "Marimba Sound", "Acoustic Guitar Pluck", "Space Wind Sound",
        "Sci-Fi Computer Blips", "Laser Attack Sound", "Analog Drone Texture", "Soft Flute Voice", "Clarinet Analog",
        "Mellow Reed Poly", "Bright Polysynth Saw", "Chorused Poly Sound", "Detuned Octave Poly", "Resonant Sweep Pad",
        "Analog Clav Slap", "Punchy Chord Stab", "Electro Bassline 1", "Square Wave Bass", "Funky Mini Lead",
        "Screaming DCO Solo", "Vintage Poly Chord", "Bright Bell Poly", "Analog Music Box", "Metallic Tinkle",
        "Filter Modulation FX", "Helicopter Noise FX", "Alien Invader Sound", "Cosmic Pad Swell", "Dark Gothic Organ",
        "Accordion Squeeze", "Tremolo Electric Piano", "Slow Filter Sweep Pad", "Punchy Dance Brass", "Fast Staccato Poly",
        "Dual Oscillator Saw Solo", "Sub Bass Heavy", "Funky DCO Pluck", "Sweet Analog Pad", "Space Shuttle Launch",
        "White Noise Surf", "Synthesizer Siren", "Random Filter Sample & Hold", "Poly-61 Ultimate Memory"
    ]
    for i, name in enumerate(p61_names):
        cat = "Brass" if "Brass" in name or "Horn" in name else "Strings" if "Strings" in name else "Bass" if "Bass" in name else "Keys" if "Organ" in name or "Piano" in name or "Clav" in name else "Lead" if "Lead" in name or "Solo" in name else "Pad"
        p61_presets.append({"name": f"P61 {name}", "bank": "Preset Memories", "number": i + 1, "category": cat, "tags": ["korg", "poly-61", "dco", "analog", "vintage"]})
    write_synth("korg", "poly-61", "Poly-61", "6-Voice Programmable Polyphonic Synthesizer", 1982, p61_cc, p61_sysex, p61_banks, p61_presets)

    # =========================================================================
    # 16. ROLAND JD-08 (Boutique 4-Part Multi-Timbral JD-800 Recreation)
    # =========================================================================
    jd08_cc = {"filter_cutoff": 74, "filter_resonance": 71, "tvf_env_depth": 77, "pan": 10, "volume": 7, "reverb_level": 91}
    jd08_sysex = {"header": "F0 41 10 00 00 64", "device_id_byte": 3, "commands": {"request_patch": "F0 41 10 00 00 64 11 [addr] [size] [chk] F7"}}
    jd08_banks = [{"name": "Bank A Original", "type": "ROM", "size": 64}, {"name": "Bank B Expanded", "type": "ROM", "size": 64}]
    jd08_presets = []
    jd800_names = [
        "Millennium Pad", "Crystal Rhodes", "Deep Forest Pad", "Wicked Lead", "Analog Brass 1", "Stereo Poly Saw",
        "Guit-Arp Pluck", "Heavenly Voices", "Vortex Sweep", "Acoustic Grand JD", "Warm Reso Bass", "Chamber Strings",
        "Nylon Air Guitar", "Industrial Metal Perc", "Solo Oboe Vibrato", "Digital Cathedral Organ", "Cyber Pulse Lead",
        "Space Wind Drone", "Polyphonic Bells", "Bell Choir Swell", "Funk Slap Minibass", "Spit Brass Fanfare",
        "Glassy Electric Piano", "Vintage Clavinet Funk", "Alien Communication", "Mellotron Flute Chime",
        "Dancefloor Techno Stabs", "Resonant Sweep Bass", "Velocity Poly Chords", "Ethereal Pad Atmosphere",
        "Fifth Interval Screamer", "Submarine Sonar Ping"
    ]
    for i in range(64):
        base = jd800_names[i % len(jd800_names)]
        jd08_presets.append({"name": f"JD08 {base} A{i+1:02d}", "bank": "Bank A Original", "number": i + 1, "category": "Pad" if "Pad" in base or "Atmosphere" in base else "Keys" if "Piano" in base or "Rhodes" in base else "Lead" if "Lead" in base else "Bass", "tags": ["roland", "jd-08", "jd-800", "boutique", "4-part"]})
    for i in range(64):
        base = jd800_names[i % len(jd800_names)]
        jd08_presets.append({"name": f"JD08 Modern {base} B{i+1:02d}", "bank": "Bank B Expanded", "number": i + 1, "category": "Synth", "tags": ["roland", "jd-08", "boutique", "expanded"]})
    write_synth("roland", "jd-08", "JD-08", "Boutique 4-Part Linear Synthesizer", 2021, jd08_cc, jd08_sysex, jd08_banks, jd08_presets)

    # =========================================================================
    # 17. ROLAND JU-06A (Boutique Juno-60 + Juno-106 Recreation)
    # =========================================================================
    ju_cc = {"filter_cutoff": 74, "filter_resonance": 71, "chorus_mode": 93, "sub_osc_level": 70, "volume": 7, "hpf_cutoff": 75}
    ju_sysex = {"header": "F0 41 10 00 00 5E", "device_id_byte": 3, "commands": {"request_patch": "F0 41 10 00 00 5E 11 [addr] [size] [chk] F7"}}
    ju_banks = [{"name": "Juno-60 Mode", "type": "Preset", "size": 32}, {"name": "Juno-106 Mode", "type": "Preset", "size": 32}]
    ju_presets = []
    juno60_names = [
        "J60 Brass Section 1", "J60 Warm Strings 1", "J60 Fat Analog Bass", "J60 Chorus Electric Piano",
        "J60 Polyphonic Pluck", "J60 Resonance Lead Solo", "J60 Church Pipe Organ", "J60 Space Arp Pattern",
        "J60 Sub Pulse Bass", "J60 Lush Filter Pad", "J60 Bright Horns", "J60 Slow Attack Strings",
        "J60 Funky Clavinet", "J60 Whistle Soloist", "J60 Bell Chimes Analog", "J60 Cosmic Wind Sweep",
        "J60 PWM Lush Pad", "J60 Sawtooth Lead", "J60 Acid Bass Filter", "J60 Polyphonic Harpsichord",
        "J60 Jazz Organ Rotary", "J60 Vibraphone Tone", "J60 High Pass Reso Sweep", "J60 Detuned Fifth Poly",
        "J60 Square Lead Vintage", "J60 Heavy Sub Bass", "J60 Dream Voices Pad", "J60 Fast Staccato Horn",
        "J60 Octave Lead Punch", "J60 White Noise Waves", "J60 Arpeggio Clock Dance", "J60 Ultimate Polyphonic"
    ]
    for i, name in enumerate(juno60_names):
        ju_presets.append({"name": f"JU06A {name}", "bank": "Juno-60 Mode", "number": i + 1, "category": "Strings" if "Strings" in name or "Pad" in name else "Brass" if "Brass" in name or "Horn" in name else "Bass" if "Bass" in name else "Keys", "tags": ["roland", "ju-06a", "juno-60", "chorus", "boutique"]})
    juno106_names = [
        "J106 Warm Strings I", "J106 Brass Section II", "J106 Sub Bass 106", "J106 Solid Bass Punch",
        "J106 Chorus Rhodes Poly", "J106 Octave Solo Lead", "J106 Soft Flute Pad", "J106 Poly Clavinet",
        "J106 Pipe Organ II", "J106 Resonant Pluck Arp", "J106 Lush Chorused Pad", "J106 Synth Brass Hits",
        "J106 Electro Funk Bass", "J106 Fast Pulse Lead", "J106 Glass Bell Tone", "J106 Space Jet Sound",
        "J106 Deep Moog-ish Bass", "J106 Cathedral Organ", "J106 Pizzicato Strings", "J106 Polyphonic Saw Lead",
        "J106 Ambient Filter Drone", "J106 Mellow Velvet Pad", "J106 Brass Fanfare", "J106 Detuned Lead Solo",
        "J106 Analog Accordion", "J106 High Resonance Zap", "J106 Slow String Swell", "J106 House Music Bass",
        "J106 Techno Chord Stab", "J106 Sci-Fi Computer Laser", "J106 Subharmonic Rumble", "J106 Juno-106 Master Sound"
    ]
    for i, name in enumerate(juno106_names):
        ju_presets.append({"name": f"JU06A {name}", "bank": "Juno-106 Mode", "number": i + 1, "category": "Strings" if "Strings" in name or "Pad" in name else "Bass" if "Bass" in name else "Brass" if "Brass" in name else "Lead", "tags": ["roland", "ju-06a", "juno-106", "chorus", "boutique"]})
    write_synth("roland", "ju-06a", "JU-06A", "Boutique Juno-60 / Juno-106 Synthesizer", 2019, ju_cc, ju_sysex, ju_banks, ju_presets)

    # =========================================================================
    # 18. ROLAND JX-08 (Boutique JX-8P Recreation w/ PG-800 Integration)
    # =========================================================================
    jx_cc = {"filter_cutoff": 74, "filter_resonance": 71, "dco2_tune": 70, "volume": 7, "cross_mod": 14}
    jx_sysex = {"header": "F0 41 10 00 00 65", "device_id_byte": 3, "commands": {"request_patch": "F0 41 10 00 00 65 11 [addr] [size] [chk] F7"}}
    jx_banks = [{"name": "Preset Bank 1", "type": "ROM", "size": 32}, {"name": "Preset Bank 2", "type": "ROM", "size": 32}]
    jx_presets = []
    jx8p_names = [
        "Soundtrack Pad", "Warm Analog Strings", "Poly Brass Section", "Voices & Choir Swell", "Sync Lead Solo",
        "Electric Piano 1", "Clavinet Poly Funk", "Jazz Organ Rotary", "Upright Wood Bass", "Synth Bass Punch",
        "Vibraphone Perc", "Marimba Sound", "Acoustic Nylon Guitar", "Resonant Sweep Pad", "Metallic Chime Bell",
        "Cross-Mod SFX Alien", "Pizzicato Poly Pluck", "French Horn Ensemble", "Solo Trumpet Fanfare", "Flute Analog",
        "Oboe Vibrato Solo", "Violin Soloist", "Harpsichord Baroque", "Pipe Organ Cathedral", "Slow Sweep Strings",
        "Fat DCO Saw Brass", "Sync Modulation Lead", "Sub Octave Pulse Bass", "Lush Chorused Rhodes", "Space Wind Drone",
        "Percussive Glockenspiel", "JX-8P Master Signature"
    ]
    for i, name in enumerate(jx8p_names):
        jx_presets.append({"name": f"JX08 {name}", "bank": "Preset Bank 1", "number": i + 1, "category": "Pad" if "Pad" in name or "Soundtrack" in name else "Strings" if "Strings" in name else "Brass" if "Brass" in name else "Keys", "tags": ["roland", "jx-08", "jx-8p", "pg-800", "soundtrack pad"]})
        jx_presets.append({"name": f"JX08 Modern {name}", "bank": "Preset Bank 2", "number": i + 1, "category": "Synth", "tags": ["roland", "jx-08", "boutique", "analog"]})
    write_synth("roland", "jx-08", "JX-08", "Boutique Sound Generator (JX-8P)", 2021, jx_cc, jx_sysex, jx_banks, jx_presets)

    # =========================================================================
    # 19. ROLAND U-20 / U-220 (RS-PCM Sound Canvas Synthesizer Module)
    # =========================================================================
    u20_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_level": 91, "chorus_level": 93}
    u20_sysex = {"header": "F0 41 10 2B", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 2B 11 [addr] [size] [chk] F7"}}
    u20_banks = [{"name": "Preset Patches", "type": "ROM", "size": 64}, {"name": "Preset Timbres", "type": "ROM", "size": 64}]
    u20_presets = []
    u20_names = [
        "Acoustic Piano 1", "Honky Tonk Piano", "Electric Piano 1", "Harpsichord Poly", "Clavinet Funk", "Pipe Organ Full",
        "Jazz Organ B3", "Accordion Squeeze", "Vibraphone Perc", "Marimba Pluck", "Acoustic Guitar Steel", "Nylon Guitar Solo",
        "12-String Guitar", "Clean Electric Guitar", "Overdrive Guitar", "Acoustic Wood Bass", "Fretless Bass Solo", "Slap Bass 1",
        "Synth Bass RS", "Symphonic Strings", "Slow Strings Swell", "Pizzicato Strings", "Solo Violin", "Solo Cello",
        "Trumpet Section", "Solo Trumpet Mute", "Trombone Ensemble", "French Horns Section", "Brass Fanfare Stabs", "Synth Brass 1",
        "Concert Flute", "Pan Flute Chiff", "Shakuhachi Breath", "Oboe Vibrato", "Clarinet Solo", "Bassoon Low",
        "Harmonica Blues", "Whistle Soloist", "Square Lead Vintage", "Sawtooth Solo Lead", "Fat Poly Synth", "Warm RS-PCM Pad",
        "Digital Bell Choir", "Crystal Pad Swell", "Soundtrack Atmosphere", "Space Drone Texture", "Tubular Bells Toll", "Glockenspiel Studio",
        "Timpani Roll Hit", "Steel Drum Island", "Sitar Indian", "Koto Japanese", "Kalimba African", "Taiko Drum Slam",
        "Standard Drum Kit", "Electronic Dance Kit", "Brush Jazz Kit", "Orchestra Percussion", "Synth Percussion Clank", "RS-PCM Wind Sweep",
        "Laser Attack FX", "Alien Computer Tone", "Sub Heavy Rumble", "U-20 Master Canvas"
    ]
    for i, name in enumerate(u20_names):
        cat = "Keys" if "Piano" in name or "Organ" in name or "Clav" in name else "Bass" if "Bass" in name else "Strings" if "Strings" in name or "Violin" in name else "Brass" if "Brass" in name or "Trumpet" in name else "Pad" if "Pad" in name or "Soundtrack" in name else "Drums" if "Kit" in name or "Drum" in name else "Synth"
        u20_presets.append({"name": f"U20 {name}", "bank": "Preset Patches", "number": i + 1, "category": cat, "tags": ["roland", "u-20", "u-220", "rs-pcm", "rompler"]})
        u20_presets.append({"name": f"U20 Timbre {name}", "bank": "Preset Timbres", "number": i + 1, "category": cat, "tags": ["roland", "u-20", "timbre", "rs-pcm"]})
    write_synth("roland", "u-20", "U-20 / U-220", "RS-PCM Multi-Timbral Synthesizer", 1989, u20_cc, u20_sysex, u20_banks, u20_presets)

    # =========================================================================
    # 20. ROLAND CM-32L (Classic Computer Music LA Sound Module / MT-32 Expansion)
    # =========================================================================
    cm_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_level": 91}
    cm_sysex = {"header": "F0 41 10 16", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 16 11 [addr] [size] [chk] F7"}}
    cm_banks = [{"name": "LA Sound Bank", "type": "ROM", "size": 128}]
    cm_presets = []
    la_names = [
        "Acoustic Piano 1", "Acoustic Piano 2", "Acoustic Piano 3", "Electric Piano 1", "Electric Piano 2", "Electric Piano 3",
        "Electric Piano 4", "Honky Tonk Piano", "Electric Organ 1", "Electric Organ 2", "Electric Organ 3", "Electric Organ 4",
        "Pipe Organ 1", "Pipe Organ 2", "Pipe Organ 3", "Accordion", "Harpsichord 1", "Harpsichord 2", "Harpsichord 3",
        "Clavinet 1", "Clavinet 2", "Clavinet 3", "Celesta 1", "Celesta 2", "Syn Brass 1", "Syn Brass 2", "Syn Brass 3", "Syn Brass 4",
        "Syn Bass 1", "Syn Bass 2", "Syn Bass 3", "Syn Bass 4", "Acoustic Bass 1", "Acoustic Bass 2", "Electric Bass 1", "Electric Bass 2",
        "Slap Bass 1", "Slap Bass 2", "Fretless Bass 1", "Fretless Bass 2", "Flute 1", "Flute 2", "Piccolo 1", "Piccolo 2",
        "Recorder", "Pan Flute", "Sax 1", "Sax 2", "Sax 3", "Sax 4", "Clarinet 1", "Clarinet 2", "Oboe", "English Horn",
        "Bassoon", "Harmonica", "Trumpet 1", "Trumpet 2", "Mute Trumpet 1", "Mute Trumpet 2", "Trombone 1", "Trombone 2",
        "French Horn 1", "French Horn 2", "Tuba", "Brass Section 1", "Brass Section 2", "Vibe 1", "Vibe 2", "Syn Mallet",
        "Windbell", "Glockenspiel", "Tubular Bell", "Xylophone", "Marimba", "Koto", "Sho", "Shakuhachi", "Whistle 1", "Whistle 2",
        "Bottleblow", "Breathpipe", "Strings 1", "Strings 2", "Strings 3", "Strings 4", "Pizzicato Strings", "Violin 1", "Violin 2",
        "Cello 1", "Cello 2", "Contrabass", "Harp 1", "Harp 2", "Sitar", "Acoustic Guitar 1", "Acoustic Guitar 2", "Electric Guitar 1",
        "Electric Guitar 2", "Slap Guitar", "Jazz Guitar", "Fantasy Pad", "Syn Voice", "Chorale", "Nightmare FX", "Laser Gun FX",
        "Explosion Sound", "Siren Alarm", "Jet Engine", "Helicopter Sound", "Wind Storm", "Gunshot Sound", "Dog Bark", "Bird Tweet",
        "Telephone Ring", "Punch Hit", "Heartbeat Sound", "Footstep Sound", "Applause Cheer", "Door Creak", "Scratch Disc",
        "Wind Chime Sound", "Bubble Pop", "Water Drops", "Rain Storm", "Thunder Crack", "Train Horn", "Car Crash", "CM-32L Master Sound"
    ]
    for i, name in enumerate(la_names):
        cat = "FX" if "FX" in name or "Sound" in name or "Engine" in name or "Crash" in name or "Storm" in name else "Keys" if "Piano" in name or "Organ" in name else "Bass" if "Bass" in name else "Strings" if "Strings" in name or "Violin" in name else "Brass" if "Brass" in name or "Trumpet" in name else "Synth"
        cm_presets.append({"name": f"CM32L {name}", "bank": "LA Sound Bank", "number": i + 1, "category": cat, "tags": ["roland", "cm-32l", "la synthesis", "dos games", "sierra", "mt-32"]})
    write_synth("roland", "cm-32l", "CM-32L", "Linear Arithmetic Sound Module for PC/Games", 1989, cm_cc, cm_sysex, cm_banks, cm_presets)

    # =========================================================================
    # 21. YAMAHA CS6x / CS6R (64-Voice AWM2 + Modular Synthesis Plug-in System)
    # =========================================================================
    cs6_cc = {"filter_cutoff": 74, "filter_resonance": 71, "scene1": 16, "scene2": 17, "volume": 7, "pan": 10, "assign1": 18, "assign2": 19}
    cs6_sysex = {"header": "F0 43 10 5F", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 5F 00 [bank] [prog] F7"}}
    cs6_banks = [{"name": "Internal Voice Bank 1", "type": "ROM", "size": 128}, {"name": "Internal Voice Bank 2", "type": "ROM", "size": 128}]
    cs6_presets = []
    for b in range(2):
        bname = f"Internal Voice Bank {b+1}"
        for p in range(128):
            cs6_pool = ["Trance Energy Lead", "Fat Dance Bass AWM2", "Filtered Tech Poly", "Euphoric String Swell", "Acid Resonance Sweep",
                        "Club Stabs Stereo", "Analog Power Saw", "Hypnotic Arp Sequence", "Vocal Morph Choir", "Ambient Soundscape CS",
                        "Sub Attack Bassline", "Modern Hardstyle Pluck", "BPM Delay Synth", "Punchy Electro Kick Lead", "Stereo Phaser Pad", "CS6x Flagship Voice"]
            base = cs6_pool[p % len(cs6_pool)]
            cs6_presets.append({"name": f"CS6X {base} #{p+1:03d}", "bank": bname, "number": p + 1, "category": "Lead" if "Lead" in base else "Bass" if "Bass" in base else "Pad" if "Pad" in base or "Swell" in base else "Synth", "tags": ["yamaha", "cs6x", "cs6r", "awm2", "dance", "techno", "plg"]})
    write_synth("yamaha", "cs6x", "CS6x / CS6R", "64-Voice AWM2 Dance Synthesizer", 1999, cs6_cc, cs6_sysex, cs6_banks, cs6_presets)

    # =========================================================================
    # 22. YAMAHA SY85 (Advanced AWM2 Music Workstation w/ Resonant Filters)
    # =========================================================================
    sy85_cc = {"filter_cutoff": 74, "filter_resonance": 71, "slider1": 16, "slider2": 17, "slider3": 18, "slider4": 19, "volume": 7}
    sy85_sysex = {"header": "F0 43 10 3B", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 3B 00 [bank] [prog] F7"}}
    sy85_banks = [{"name": f"Internal Bank {chr(65+b)}", "type": "ROM", "size": 64} for b in range(4)]
    sy85_presets = []
    for b in range(4):
        bname = f"Internal Bank {chr(65+b)}"
        for p in range(64):
            sy_pool = ["Concert Grand SY", "Fat Reso Filter Saw", "Warm AWM2 Strings", "Dynamic Slap Bass", "Poly Brass Horns",
                       "Vintage Rhodes Mark V", "Solo Saxophone Breathy", "Digital Chime Bell Pad", "Acid Synth Bassline", "Symphonic Ensemble"]
            base = sy_pool[p % len(sy_pool)]
            sy85_presets.append({"name": f"SY85 {base} {chr(65+b)}{p+1:02d}", "bank": bname, "number": p + 1, "category": "Keys" if "Grand" in base or "Rhodes" in base else "Bass" if "Bass" in base else "Strings" if "Strings" in base else "Brass" if "Brass" in base else "Synth", "tags": ["yamaha", "sy85", "awm2", "workstation", "resonant filters"]})
    write_synth("yamaha", "sy85", "SY85", "Advanced AWM2 Music Synthesizer Workstation", 1992, sy85_cc, sy85_sysex, sy85_banks, sy85_presets)

    # =========================================================================
    # 23. YAMAHA TG33 / SY22 (Vector Synthesis Tone Generator)
    # =========================================================================
    tg33_cc = {"vector_x": 16, "vector_y": 17, "volume": 7, "pan": 10, "reverb_depth": 91}
    tg33_sysex = {"header": "F0 43 10 2E", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 2E 00 [bank] [prog] F7"}}
    tg33_banks = [{"name": "Preset Voice Bank 1", "type": "ROM", "size": 64}, {"name": "Preset Voice Bank 2", "type": "ROM", "size": 64}, {"name": "Multi Memory", "type": "Multi", "size": 64}]
    tg33_presets = []
    for b in range(2):
        bname = f"Preset Voice Bank {b+1}"
        for p in range(64):
            vec_pool = ["Vector Motion Morph", "FM + AWM Dynamic Lead", "Cosmic Vector Pad", "Deep Pulse Hybrid Bass", "Crystal Vector Bell",
                        "Alien Space Texture", "Warm E-Piano Vector", "Analog Saw Motion Sweep", "Ethnic World Flute Morph", "Orchestral Vector Swell"]
            base = vec_pool[p % len(vec_pool)]
            tg33_presets.append({"name": f"TG33 {base} #{p+1:02d}", "bank": bname, "number": p + 1, "category": "Pad" if "Pad" in base or "Swell" in base else "Lead" if "Lead" in base else "Bass" if "Bass" in base else "Synth", "tags": ["yamaha", "tg33", "sy22", "vector synthesis", "fm+awm"]})
    for m in range(64):
        tg33_presets.append({"name": f"TG33 Multi Combination {m+1:02d}", "bank": "Multi Memory", "number": m + 1, "category": "Multi", "tags": ["yamaha", "tg33", "multi", "layer"]})
    write_synth("yamaha", "tg33", "TG33 / SY22", "Vector Synthesis Tone Generator", 1990, tg33_cc, tg33_sysex, tg33_banks, tg33_presets)

    # =========================================================================
    # 24. YAMAHA FB-01 (4-Operator FM Sound Generator)
    # =========================================================================
    fb01_cc = {"volume": 7, "pan": 10, "mod_wheel": 1, "pitch_bend": 0}
    fb01_sysex = {"header": "F0 43 75 00", "device_id_byte": 2, "commands": {"request_voice": "F0 43 75 00 20 [bank] [voice] F7"}}
    fb01_banks = [{"name": f"ROM Bank {b+1}", "type": "ROM", "size": 48} for b in range(5)]
    fb01_presets = []
    for b in range(5):
        bname = f"ROM Bank {b+1}"
        for p in range(48):
            fb_pool = ["Solid 4-Op Bass", "E-Piano FM Bell", "Crisp Clavinet 4-Op", "FM Brass Fanfare", "Warm FM Strings",
                       "Jazz Organ B3 FM", "Glockenspiel Bell", "Harmonica Blues FM", "Reso Synth Sweep", "Sci-Fi Space FX"]
            base = fb_pool[p % len(fb_pool)]
            fb01_presets.append({"name": f"FB01 {base} B{b+1}-{p+1:02d}", "bank": bname, "number": p + 1, "category": "Bass" if "Bass" in base else "Keys" if "Piano" in base or "Organ" in base else "Lead" if "Sweep" in base else "Synth", "tags": ["yamaha", "fb-01", "4-op", "fm synthesis", "vintage"]})
    write_synth("yamaha", "fb-01", "FB-01", "4-Operator FM Sound Generator Module", 1986, fb01_cc, fb01_sysex, fb01_banks, fb01_presets)

    # =========================================================================
    # 25. YAMAHA V50 (All-in-One 4-Operator FM Workstation w/ Drum Machine)
    # =========================================================================
    v50_cc = {"volume": 7, "pan": 10, "mod_wheel": 1, "breath_ctrl": 2, "sustain": 64}
    v50_sysex = {"header": "F0 43 10 27", "device_id_byte": 2, "commands": {"request_voice": "F0 43 10 27 00 [voice] F7"}}
    v50_banks = [{"name": "Preset Internal Voices", "type": "ROM", "size": 100}]
    v50_presets = []
    for i in range(100):
        v50_pool = ["Lately Bass 4-Op", "DX7 E-Piano Warm", "Super Clavinet V50", "Full Brass Ensemble", "Symphonic Strings 4-Op",
                    "Hammond B3 Rotary", "Slap Bass Funky", "Sync Soloist Lead", "Cosmic Crystal Pad", "Punchy Drum PCM Kit"]
        base = v50_pool[i % len(v50_pool)]
        v50_presets.append({"name": f"V50 {base} #{i+1:02d}", "bank": "Preset Internal Voices", "number": i + 1, "category": "Bass" if "Bass" in base else "Keys" if "Piano" in base or "Organ" in base else "Brass" if "Brass" in base else "Pad" if "Pad" in base or "Strings" in base else "Lead", "tags": ["yamaha", "v50", "4-op", "fm workstation", "drum machine"]})
    write_synth("yamaha", "v50", "V50", "4-Operator FM Workstation Synthesizer", 1989, v50_cc, v50_sysex, v50_banks, v50_presets)

    # =========================================================================
    # 26. KAWAI K3 / K3M (6-Voice Hybrid Synthesizer w/ SSM2044 Analog VCF)
    # =========================================================================
    k3_cc = {"filter_cutoff": 74, "filter_resonance": 71, "volume": 7, "dco_wave": 70, "chorus": 93}
    k3_sysex = {"header": "F0 40 00 00 00 01", "device_id_byte": 2, "commands": {"request_patch": "F0 40 00 00 00 01 00 [prog] F7"}}
    k3_banks = [{"name": "Internal Memory", "type": "RAM", "size": 50}]
    k3_presets = []
    k3_names = [
        "Acoustic Grand K3", "Electric Piano 1", "Honky Tonk Piano", "Clavinet DCO", "Pipe Organ Full", "Jazz Organ B3",
        "Acoustic Guitar", "Electric Guitar Jazz", "Upright Wood Bass", "Slap Bass Funky", "Resonant SSM Saw Bass",
        "Polyphonic Warm Strings", "Slow Attack Strings", "Solo Violin Vibrato", "Cello Ensemble", "Trumpet Fanfare",
        "Trombone Section", "French Horns", "Analog Synth Brass 1", "Fat Reso Horn Stabs", "Concert Flute", "Pan Flute Chiff",
        "Clarinet Solo", "Oboe Vibrato", "Harmonica Blues", "Whistle Soloist", "Square Lead Vintage", "Saw Solo Screamer",
        "SSM Filter Sweep Lead", "Detuned Poly Saw", "Warm Velvet Pad", "High Pass Sweep", "Percussive Bell Synth",
        "Vibraphone Analog", "Marimba Sound", "Digital Chime Bell", "Glass Marimba", "Cosmic Space Wind", "Sci-Fi Computer Noise",
        "Laser Attack FX", "Alien Drone Swell", "Sub Octave Pulse Bass", "Fifth Interval Lead", "Sync Modulation Solo",
        "Arpeggio Pluck Tone", "Harpsichord Poly", "Accordion Squeeze", "Tremolo Electric Piano", "Chorus Mellow Poly", "K3 Master Sound"
    ]
    for i, name in enumerate(k3_names):
        cat = "Keys" if "Piano" in name or "Organ" in name or "Clav" in name else "Bass" if "Bass" in name else "Strings" if "Strings" in name or "Violin" in name else "Brass" if "Brass" in name or "Horn" in name else "Lead" if "Lead" in name or "Solo" in name else "Pad"
        k3_presets.append({"name": f"K3 {name}", "bank": "Internal Memory", "number": i + 1, "category": cat, "tags": ["kawai", "k3", "k3m", "ssm2044", "hybrid", "analog filter"]})
    write_synth("kawai", "k3", "K3 / K3m", "6-Voice Hybrid Synthesizer with SSM2044 Filter", 1986, k3_cc, k3_sysex, k3_banks, k3_presets)

    # =========================================================================
    # 27. KAWAI K11 (General MIDI & Multi-Timbral Synthesizer Module)
    # =========================================================================
    k11_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_level": 91, "chorus_level": 93}
    k11_sysex = {"header": "F0 40 00 20 00 07", "device_id_byte": 2, "commands": {"request_patch": "F0 40 00 20 00 07 00 [prog] F7"}}
    k11_banks = [{"name": "GM Preset Bank", "type": "ROM", "size": 128}, {"name": "Synth Section Bank", "type": "ROM", "size": 64}]
    k11_presets = []
    for i in range(128):
        k11_presets.append({"name": f"K11 GM Patch #{i+1:03d}", "bank": "GM Preset Bank", "number": i + 1, "category": "General MIDI", "tags": ["kawai", "k11", "gm", "sound canvas"]})
    for i in range(64):
        k11_presets.append({"name": f"K11 Synth Lead/Pad #{i+1:02d}", "bank": "Synth Section Bank", "number": i + 1, "category": "Synth", "tags": ["kawai", "k11", "synth", "pad", "lead"]})
    write_synth("kawai", "k11", "K11 / GMega", "Multi-Timbral GM Synthesizer Module", 1993, k11_cc, k11_sysex, k11_banks, k11_presets)

    # =========================================================================
    # 28. ROLAND D-10 (Linear Arithmetic Multi-Timbral Synthesizer)
    # =========================================================================
    d10_cc = {"volume": 7, "pan": 10, "expression": 11, "reverb_level": 91}
    d10_sysex = {"header": "F0 41 10 16", "device_id_byte": 2, "commands": {"request_patch": "F0 41 10 16 11 [addr] [size] [chk] F7"}}
    d10_banks = [{"name": "Preset Bank 1", "type": "ROM", "size": 64}, {"name": "Preset Bank 2", "type": "ROM", "size": 64}]
    d10_presets = []
    d10_names = [
        "Acoustic Piano 1", "Honky Tonk Piano", "Electric Piano 1", "Harpsichord Poly", "Clavinet Funk", "Pipe Organ Full",
        "Jazz Organ B3", "Accordion Squeeze", "Vibraphone Perc", "Marimba Pluck", "Acoustic Guitar Steel", "Nylon Guitar Solo",
        "12-String Guitar", "Clean Electric Guitar", "Overdrive Guitar", "Acoustic Wood Bass", "Fretless Bass Solo", "Slap Bass 1",
        "Synth Bass LA", "Symphonic Strings", "Slow Strings Swell", "Pizzicato Strings", "Solo Violin", "Solo Cello",
        "Trumpet Section", "Solo Trumpet Mute", "Trombone Ensemble", "French Horns Section", "Brass Fanfare Stabs", "Synth Brass 1",
        "Concert Flute", "Pan Flute Chiff", "Shakuhachi Breath", "Oboe Vibrato", "Clarinet Solo", "Bassoon Low",
        "Harmonica Blues", "Whistle Soloist", "Square Lead Vintage", "Sawtooth Solo Lead", "Fat Poly Synth", "Warm LA Pad",
        "Digital Bell Choir", "Crystal Pad Swell", "Soundtrack Atmosphere", "Space Drone Texture", "Tubular Bells Toll", "Glockenspiel Studio",
        "Timpani Roll Hit", "Steel Drum Island", "Sitar Indian", "Koto Japanese", "Kalimba African", "Taiko Drum Slam",
        "Standard Drum Kit", "Electronic Dance Kit", "Brush Jazz Kit", "Orchestra Percussion", "Synth Percussion Clank", "LA Wind Sweep",
        "Laser Attack FX", "Alien Computer Tone", "Sub Heavy Rumble", "D-10 Master Canvas"
    ]
    for i, name in enumerate(d10_names):
        cat = "Keys" if "Piano" in name or "Organ" in name or "Clav" in name else "Bass" if "Bass" in name else "Strings" if "Strings" in name or "Violin" in name else "Brass" if "Brass" in name or "Trumpet" in name else "Pad" if "Pad" in name or "Soundtrack" in name else "Drums" if "Kit" in name or "Drum" in name else "Synth"
        d10_presets.append({"name": f"D10 {name}", "bank": "Preset Bank 1", "number": i + 1, "category": cat, "tags": ["roland", "d-10", "la synthesis", "linear arithmetic"]})
        d10_presets.append({"name": f"D10 Modern {name}", "bank": "Preset Bank 2", "number": i + 1, "category": cat, "tags": ["roland", "d-10", "la synthesis", "patch"]})
    write_synth("roland", "d-10", "D-10", "Linear Arithmetic Multi-Timbral Synthesizer", 1988, d10_cc, d10_sysex, d10_banks, d10_presets)

    # =========================================================================
    # 29. ENSONIQ DP/4 (Legendary 4-Unit Parallel Multi-Effects Processor)
    # =========================================================================
    dp4_cc = {"fx_bypass": 84, "mix_dry_wet": 91, "param_1": 16, "param_2": 17, "param_3": 18, "param_4": 19}
    dp4_sysex = {"header": "F0 0F 40 00", "device_id_byte": 2, "commands": {"request_preset": "F0 0F 40 00 01 [preset] F7"}}
    dp4_banks = [{"name": "1-Unit Algorithms", "type": "ROM", "size": 100}, {"name": "2-Unit Algorithms", "type": "ROM", "size": 100},
                 {"name": "4-Unit Configurations", "type": "ROM", "size": 100}, {"name": "User Memory", "type": "RAM", "size": 100}]
    dp4_presets = []
    for b, bname in enumerate(["1-Unit Algorithms", "2-Unit Algorithms", "4-Unit Configurations", "User Memory"]):
        for p in range(100):
            fx_pool = ["Large Concert Hall Reverb", "Plate Reverb Warm Studio", "Stereo Ping-Pong Delay", "8-Voice Chorus Ensemble",
                       "Rotary Speaker Simulator", "Phaser 12-Stage Sweep", "Flanger Jet Aero", "Pitch Shifter Micro Detune",
                       "Guitar Amp & Speaker 4x12", "Parametric EQ Studio 4", "Vocal De-Esser & Compressor", "Resonant 4-Pole Lowpass Filter",
                       "Gated Reverb 80s Snare", "Reverse Reverb Dreamscape", "Multi-Tap Rhythm Delay", "DP/4 Master Multi-Rack"]
            base = fx_pool[p % len(fx_pool)]
            dp4_presets.append({"name": f"DP4 {base} #{p+1:02d}", "bank": bname, "number": p + 1, "category": "FX", "tags": ["ensoniq", "dp-4", "multi-effects", "parallel processing", "studio legend"]})
    write_synth("ensoniq", "dp-4", "DP/4 / DP/4+", "Parallel Multi-Effects Processor", 1992, dp4_cc, dp4_sysex, dp4_banks, dp4_presets)

    # =========================================================================
    # 30. ENSONIQ ASR-10 (Advanced Sampling Recorder Workstation)
    # =========================================================================
    asr_cc = {"volume": 7, "pan": 10, "mod_wheel": 1, "filter_cutoff": 74, "patch_select_1": 12, "patch_select_2": 13}
    asr_sysex = {"header": "F0 0F 05 00", "device_id_byte": 2, "commands": {"request_inst": "F0 0F 05 00 01 [inst] F7"}}
    asr_banks = [{"name": "Factory Instruments Bank", "type": "ROM/Disk", "size": 100}]
    asr_presets = []
    for i in range(100):
        asr_pool = ["Concert Grand Piano ASR", "Stereo Drum Kit Hip Hop", "Analog Sawtooth Poly Transwave", "Warm Upright Acoustic Bass",
                    "Symphonic Cello Section", "Section Trumpets & Horns", "Vintage Electric Rhodes", "Transwave Resonant Sweep",
                    "Mellotron Flute Vintage", "Stereo Guitar Strum & Pluck"]
        base = asr_pool[i % len(asr_pool)]
        asr_presets.append({"name": f"ASR10 {base} #{i+1:02d}", "bank": "Factory Instruments Bank", "number": i + 1, "category": "Sampler", "tags": ["ensoniq", "asr-10", "sampler", "transwave", "workstation", "hip hop"]})
    write_synth("ensoniq", "asr-10", "ASR-10", "Advanced Sampling Recorder Workstation", 1992, asr_cc, asr_sysex, asr_banks, asr_presets)

    print("\nWave 12 Build Complete! 30 new instruments ready for librarian indexing.")

if __name__ == "__main__":
    build_wave12()
