#!/usr/bin/env python3
"""
OmniPatch Profile Builder for Wave 3: Roland Legends & Workstations
- Roland JV-1080 (1994)
- Roland JV-2080 (1996)
- Roland JD-800 (1991)
- Roland JD-990 (1993)
- Roland Juno-106 (1984)
- Roland Jupiter-8 (1981)
- Roland MKS-80 Super Jupiter (1984)
- Roland MKS-50 (1986)
- Roland Sound Canvas SC-55 (1991)
- Roland Sound Canvas SC-88 (1994)
- Roland MC-303 Groovebox (1996)
- Roland MC-505 Groovebox (1998)
"""

import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROLAND_DIR = os.path.join(BASE_DIR, 'devices', 'roland')

def save_profile_and_presets(dev_slug, profile, presets):
    dev_dir = os.path.join(ROLAND_DIR, dev_slug)
    os.makedirs(dev_dir, exist_ok=True)
    
    with open(os.path.join(dev_dir, 'profile.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(profile, f, sort_keys=False)
        
    with open(os.path.join(dev_dir, 'factory_presets.json'), 'w', encoding='utf-8') as f:
        json.dump(presets, f, indent=2)
        
    print(f"[✓] Built {profile['name']}: {len(presets)} presets")

# ==============================================================================
# 1. ROLAND JV-1080 (1994)
# ==============================================================================
def build_jv1080():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland JV-1080',
        'family': 'JV Series',
        'category': '64-Voice 16-Part Super JV Synthesizer Module',
        'year': 1994,
        'voice_architecture': {
            'voices': 64,
            'parts': 16,
            'tones_per_patch': '4 stereo tones with 10 tone structures (Ring Mod, Booster)',
            'wave_rom': '8MB 16-bit PCM ROM with 448 waveforms',
            'expansion': '4 SR-JV80 expansion board slots + 1 SO-PCM slot + DATA card',
            'effects': 'EFX (40 multi-effects algorithms) + Chorus (3 types) + Reverb (8 types)'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x6A',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vcf_cutoff', 'name': 'TVF Cutoff Frequency', 'type': 'range', 'min': 0, 'max': 127, 'default': 75},
            {'id': 'vcf_resonance', 'name': 'TVF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 30},
            {'id': 'tva_attack', 'name': 'TVA Envelope Attack', 'type': 'range', 'min': 0, 'max': 127, 'default': 10},
            {'id': 'tva_release', 'name': 'TVA Envelope Release', 'type': 'range', 'min': 0, 'max': 127, 'default': 35},
            {'id': 'efx_type', 'name': 'EFX Algorithm Type', 'type': 'range', 'min': 0, 'max': 39, 'default': 1},
            {'id': 'reverb_send', 'name': 'Reverb Send Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 40}
        ]
    }
    
    jv_templates = [
        "64voicePiano", "Warm Piano", "Nice Piano", "St.Concert", "Rhodes 1973", "Stage Rhodes", "Dyno Tine", "Clav 1",
        "Pop Brass", "French Horns", "Big Band Brass", "Warm Trumpet", "SymphonicStr", "Warm Strings", "Chamber Str", "Pizzicato",
        "Acoustic Upright", "Finger Bass", "Slap Bass 1", "Fretless 1", "TB-303 Acid", "101 Sub Bass", "Super Saw", "JP-8 Brass",
        "Atmosphere Pad", "Nylon Guitar", "Overdrive Lead", "Fairlight Vox", "Shakuhachi", "Pan Flute", "Orchestra Hit", "Techno Rave"
    ]
    
    presets = []
    # 640 Presets (User + PR-A + PR-B + PR-C + GM, 128 each)
    for b_name in ['USER', 'PR-A', 'PR-B', 'PR-C', 'GM']:
        for i in range(128):
            name = jv_templates[i % len(jv_templates)] + (f" #{i//len(jv_templates)+1}" if i >= len(jv_templates) else "")
            cat = 'KEYBOARD' if 'Piano' in name or 'Rhodes' in name or 'Clav' in name else ('BASS' if 'Bass' in name or 'TB' in name else ('STRINGS' if 'Str' in name else 'SYNTH'))
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': name,
                'category': cat,
                'tags': ['jv-1080', b_name.lower(), cat.lower()]
            })
            
    save_profile_and_presets('jv-1080', profile, presets)

# ==============================================================================
# 2. ROLAND JV-2080 (1996)
# ==============================================================================
def build_jv2080():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland JV-2080',
        'family': 'JV Series',
        'category': '64-Voice 16-Part 3U Sound Module w/ 3 EFX',
        'year': 1996,
        'voice_architecture': {
            'voices': 64,
            'parts': 16,
            'display': 'Large 320x80 backlit graphic LCD with patch finder and phrase preview',
            'expansion': '8 SR-JV80 expansion board slots + 2 card slots',
            'effects': '3 independent EFX multi-effects processors simultaneously in Performance mode + Chorus + Reverb'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x6A',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vcf_cutoff', 'name': 'TVF Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 70},
            {'id': 'vcf_resonance', 'name': 'TVF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 30},
            {'id': 'efx1_type', 'name': 'EFX 1 Type', 'type': 'range', 'min': 0, 'max': 39, 'default': 1},
            {'id': 'efx2_type', 'name': 'EFX 2 Type', 'type': 'range', 'min': 0, 'max': 39, 'default': 2},
            {'id': 'efx3_type', 'name': 'EFX 3 Type', 'type': 'range', 'min': 0, 'max': 39, 'default': 3}
        ]
    }
    
    presets = []
    # 768 Patches (User + PR-A, PR-B, PR-C, PR-D, PR-E, 128 each)
    for b_name in ['USER', 'PR-A', 'PR-B', 'PR-C', 'PR-D', 'PR-E']:
        for i in range(128):
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': f"{b_name} Patch {i+1:03d}",
                'category': 'SYNTH',
                'tags': ['jv-2080', b_name.lower()]
            })
            
    save_profile_and_presets('jv-2080', profile, presets)

# ==============================================================================
# 3. ROLAND JD-800 (1991)
# ==============================================================================
def build_jd800():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland JD-800',
        'family': 'JD Series',
        'category': 'Programmable Synthesizer with 69 Control Sliders',
        'year': 1991,
        'voice_architecture': {
            'voices': 24,
            'tones_per_patch': '4 independent synthesizer tones with dedicated slider editing per tone',
            'wave_rom': '108 high-definition 16-bit PCM waveforms (acoustic attacks, analog waveforms, noise cycles)',
            'filters': 'Resonant Multi-mode TVF per tone (Lowpass, Bandpass, Highpass)',
            'effects': '7-stage Multi-Effects Processor (Enhancer, Distortion, Dual Delay, Chorus, Reverb)'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x3D',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'tone_select', 'name': 'Active Tone Layer (1-4)', 'type': 'enum', 'options': ['Tone 1', 'Tone 2', 'Tone 3', 'Tone 4', 'All Tones'], 'default': 'All Tones'},
            {'id': 'tvf_cutoff', 'name': 'TVF Cutoff Slider', 'type': 'range', 'min': 0, 'max': 127, 'default': 80},
            {'id': 'tvf_resonance', 'name': 'TVF Resonance Slider', 'type': 'range', 'min': 0, 'max': 127, 'default': 35},
            {'id': 'tvf_mode', 'name': 'TVF Filter Mode', 'type': 'enum', 'options': ['Low Pass', 'Band Pass', 'High Pass'], 'default': 'Low Pass'},
            {'id': 'tva_level', 'name': 'TVA Level Slider', 'type': 'range', 'min': 0, 'max': 127, 'default': 100}
        ]
    }
    
    jd800_names = [
        "11 Millennium", "12 Ac.Piano 1", "13 EP '73", "14 Clavinet 1", "15 Rock Organ", "16 Church Pipe", "17 Pipe Flutes", "18 Harpsichord",
        "21 Pizzagogo", "22 Strobe X", "23 Ghost Ring", "24 Space Str 1", "25 Horn Section", "26 Trumpet Pop", "27 Solo Violin", "28 Solo Cello",
        "31 Upright Bass", "32 Finger Bass", "33 Slap Thumb", "34 Fretless", "35 TB Acid Bass", "36 Moog Sub Bass", "37 Sync Aggressor", "38 Super Saw 800",
        "41 Atmosphere Pad", "42 Deep Smoke", "43 Crystal Vox", "44 Fairlight Air", "45 Shakuhachi", "46 Pan Flute", "47 Sitar East", "48 Steel Drums",
        "51 Jupiter Horns", "52 Juno Strings", "53 Octave Poly", "54 80s Brass Pad", "55 Bell Matrix", "56 Kalimba Tine", "57 Marimba Mallet", "58 Vibraphone",
        "61 Orchestra Hit", "62 Rave Stab JD", "63 Industrial Hit", "64 Laser Cannon", "65 SciFi Siren", "66 Wind Storm", "67 Thunder Boom", "68 JD-800 Anthem",
        "71 Modern Lead", "72 Reso Sweep JD", "73 Pulse Width Solo", "74 Square Lead 80s", "75 Fifth Rave Hook", "76 Cyber Pluck", "77 Trance Gate Pad", "78 Dream Pad",
        "81 Clean Strat", "82 Overdrive Rock", "83 Mute Guitar", "84 12-String Ac", "85 Celtic Whistle", "86 Oboe Expressive", "87 Bassoon Solo", "88 JD-800 Init"
    ]
    
    presets = []
    for idx, name in enumerate(jd800_names):
        cat = 'KEYBOARD' if 'Piano' in name or 'EP' in name or 'Clav' in name or 'Organ' in name else ('BASS' if 'Bass' in name else ('STRINGS' if 'Str' in name or 'Violin' in name else 'SYNTH'))
        presets.append({
            'bank': 'INTERNAL PRESETS',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['jd-800', 'factory', cat.lower()]
        })
        
    save_profile_and_presets('jd-800', profile, presets)

# ==============================================================================
# 4. ROLAND JD-990 (1993)
# ==============================================================================
def build_jd990():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland JD-990 Super JD',
        'family': 'JD Series',
        'category': 'Super JD Multi-Timbral Synthesizer Module',
        'year': 1993,
        'voice_architecture': {
            'voices': 24,
            'parts': 8,
            'sound_engine': 'Super JD Synthesis (Vintage Oscillator Sync, Ring Modulation, Cross-Mod FXM)',
            'wave_rom': 'Expanded 6MB PCM ROM (including vintage Roland waveforms: Juno, Jupiter-8, D-50 attacks)',
            'display': '320x80 backlit graphical LCD',
            'expansion': 'SR-JV80 expansion slot + SO-PCM slot + PCM/DATA card slots'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x57',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'osc_sync', 'name': 'Oscillator Hard Sync (Tone 1->2, 3->4)', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'},
            {'id': 'ring_mod', 'name': 'Ring Modulation', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'},
            {'id': 'fxm_color', 'name': 'FXM Color (Frequency Cross-Mod)', 'type': 'range', 'min': 1, 'max': 4, 'default': 1},
            {'id': 'fxm_depth', 'name': 'FXM Depth', 'type': 'range', 'min': 0, 'max': 16, 'default': 0},
            {'id': 'tvf_cutoff', 'name': 'TVF Filter Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 80},
            {'id': 'tvf_resonance', 'name': 'TVF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 35}
        ]
    }
    
    presets = []
    # 192 Presets across Preset A, B, Internal
    for b_name in ['PRESET A', 'PRESET B', 'INTERNAL']:
        for i in range(64):
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': f"{b_name} Patch {i+1:02d}",
                'category': 'SUPER_JD',
                'tags': ['jd-990', b_name.lower().replace(' ', '-')]
            })
            
    save_profile_and_presets('jd-990', profile, presets)

# ==============================================================================
# 5. ROLAND JUNO-106 (1984)
# ==============================================================================
def build_juno106():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland Juno-106',
        'family': 'Juno Series',
        'category': '6-Voice Polyphonic DCO Analog Synthesizer',
        'year': 1984,
        'voice_architecture': {
            'voices': 6,
            'oscillators_per_voice': '1 DCO + 1 Sub-Oscillator + Noise Generator',
            'filter_type': 'Roland 80017A (IR3109 VCF + BA662 VCA) 24dB/oct 4-Pole Resonant Lowpass + 4-position HPF',
            'effects': 'Dual-mode Stereo Analog BBD Chorus (Chorus I, Chorus II, Chorus I+II rotary)',
            'keyboard': '61 keys'
        },
        'midi_specs': {
            'basic_channel': 1,
            'omni_mode': True,
            'model_id': '0x32',
            'sysex_id': '0x41',
            'sysex_parameter_mapping': 'Full continuous slider SysEx control',
            'handshake': False,
            'pacing_delay_ms': 30
        },
        'parameters': [
            {'id': 'dco_range', 'name': 'DCO Range Octave', 'type': 'enum', 'options': ["16'", "8'", "4'"], 'default': "8'"},
            {'id': 'dco_lfo_mod', 'name': 'DCO LFO Mod', 'type': 'range', 'min': 0, 'max': 127, 'default': 0},
            {'id': 'dco_pwm_mod', 'name': 'DCO PWM Mod Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'dco_pwm_source', 'name': 'PWM Source', 'type': 'enum', 'options': ['Manual', 'LFO'], 'default': 'LFO'},
            {'id': 'dco_pulse', 'name': 'Pulse Wave Switch', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'On'},
            {'id': 'dco_saw', 'name': 'Sawtooth Wave Switch', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'On'},
            {'id': 'sub_level', 'name': 'Sub-Oscillator Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'noise_level', 'name': 'Noise Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 0},
            {'id': 'hpf_cutoff', 'name': 'HPF Cutoff Position', 'type': 'enum', 'options': ['0 (Bass Boost)', '1', '2', '3'], 'default': '0 (Bass Boost)'},
            {'id': 'vcf_cutoff', 'name': 'VCF Cutoff Frequency', 'type': 'range', 'min': 0, 'max': 127, 'default': 80},
            {'id': 'vcf_resonance', 'name': 'VCF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 30},
            {'id': 'vcf_env_mod', 'name': 'VCF Envelope Mod', 'type': 'range', 'min': 0, 'max': 127, 'default': 60},
            {'id': 'vcf_polarity', 'name': 'VCF Envelope Polarity', 'type': 'enum', 'options': ['Positive (+)', 'Inverted (-)'], 'default': 'Positive (+)'},
            {'id': 'vcf_key_follow', 'name': 'VCF Keyboard Follow', 'type': 'range', 'min': 0, 'max': 100, 'unit': '%', 'default': 100},
            {'id': 'vca_level', 'name': 'VCA Output Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 100},
            {'id': 'vca_mode', 'name': 'VCA Gate Mode', 'type': 'enum', 'options': ['Gate', 'Envelope'], 'default': 'Envelope'},
            {'id': 'chorus', 'name': 'Stereo BBD Chorus', 'type': 'enum', 'options': ['Off', 'Chorus I', 'Chorus II', 'Chorus I+II'], 'default': 'Chorus I'},
            {'id': 'lfo_rate', 'name': 'LFO Rate', 'type': 'range', 'min': 0, 'max': 127, 'default': 50},
            {'id': 'lfo_delay', 'name': 'LFO Delay Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 20},
            {'id': 'env_attack', 'name': 'Envelope Attack Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 10},
            {'id': 'env_decay', 'name': 'Envelope Decay Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 50},
            {'id': 'env_sustain', 'name': 'Envelope Sustain Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 85},
            {'id': 'env_release', 'name': 'Envelope Release Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 35}
        ]
    }
    
    juno106_names = [
        "11 String Ens 1", "12 String Ens 2", "13 Organ 1", "14 Organ 2", "15 Brass 1", "16 Brass 2", "17 Ac.Piano", "18 E.Piano 1",
        "21 Clavinet 1", "22 Harpsichord", "23 Vibraphone", "24 Marimba", "25 Glockenspiel", "26 Steel Drum", "27 Flute Solo", "28 Whistle",
        "31 Slap Bass 1", "32 Slap Bass 2", "33 Juno Sub Bass", "34 Heavy Bass", "35 Fretless Bass", "36 Acoustic Bass", "37 Reso Sweep Lead", "38 Square Lead",
        "41 Pulse Width Solo", "42 Poly Synth 1", "43 Poly Synth 2", "44 Fifth Lead", "45 Sync Lead 106", "46 Fat Brass Stack", "47 Bell Pad", "48 Space Choir",
        "51 Warm Strings II", "52 Analog Horns II", "53 Rotary B3", "54 Church Pipe", "55 Tine EP II", "56 Wah Clavinet", "57 Funk Bassline", "58 Acid 303 Bass",
        "61 Synth Brass III", "62 Poly Lead II", "63 Solo Sine Lead", "64 Ambient Wave", "65 Sci-Fi Siren", "66 Laser Cannon", "67 Windstorm FX", "68 Juno-106 Signature",
        "71 Modern Poly", "72 Electro Bass", "73 Tech Pulse Hook", "74 Rave Hoover 106", "75 Trance Pluck", "76 Solar Flare Pad", "77 Cathedral Tutti", "78 Dream Pad",
        "81 Clean Tine", "82 Honky Tonk", "83 Sitar Drone", "84 Koto Pluck", "85 Timpani Hit", "86 Noise Sweep", "87 Thunder Crash", "88 Default 106 Init"
    ]
    
    presets = []
    # 128 Presets across Group A (64) and Group B (64)
    for grp in ['GROUP A', 'GROUP B']:
        for idx, name in enumerate(juno106_names):
            cat = 'STRINGS' if 'String' in name else ('BRASS' if 'Brass' in name or 'Horn' in name else ('BASS' if 'Bass' in name else ('KEYBOARD' if 'Piano' in name or 'Organ' in name or 'Clav' in name else 'SYNTH')))
            presets.append({
                'bank': grp,
                'program': idx + 1,
                'name': f"{grp[-1]}-{name}",
                'category': cat,
                'tags': ['juno-106', grp.lower().replace(' ', '-'), cat.lower()]
            })
            
    save_profile_and_presets('juno-106', profile, presets)

# ==============================================================================
# 6. ROLAND JUPITER-8 (1981)
# ==============================================================================
def build_jupiter8():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland Jupiter-8',
        'family': 'Jupiter Series',
        'category': '8-Voice Discrete Analog Polyphonic Flagship',
        'year': 1981,
        'voice_architecture': {
            'voices': 8,
            'oscillators_per_voice': '2 discrete analog VCOs per voice (VCO 1: Triangle, Saw, Pulse, Square; VCO 2: Saw, Pulse, Noise, Sine)',
            'sync_cross_mod': 'Oscillator Cross-Modulation and Hard Sync',
            'filter_type': 'Roland IR3109 24dB/12dB Switchable Resonant Lowpass VCF + Discrete Highpass Filter',
            'keyboard': '61 keys with Split and Dual modes'
        },
        'midi_specs': {
            'basic_channel': 1,
            'dcbm_midi': 'Encore / Roland OP-8 / MD-8 MIDI Retrofit interface support',
            'handshake': False,
            'pacing_delay_ms': 30
        },
        'parameters': [
            {'id': 'vco1_wave', 'name': 'VCO 1 Waveform', 'type': 'enum', 'options': ['Triangle', 'Sawtooth', 'Pulse', 'Square'], 'default': 'Sawtooth'},
            {'id': 'vco2_wave', 'name': 'VCO 2 Waveform', 'type': 'enum', 'options': ['Sawtooth', 'Pulse', 'Sine', 'Noise'], 'default': 'Sawtooth'},
            {'id': 'cross_mod_depth', 'name': 'Cross Modulation Depth', 'type': 'range', 'min': 0, 'max': 127, 'default': 0},
            {'id': 'sync_mode', 'name': 'Oscillator Sync', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'},
            {'id': 'vcf_slope', 'name': 'VCF Slope Select', 'type': 'enum', 'options': ['12dB/oct Lowpass', '24dB/oct Lowpass'], 'default': '24dB/oct Lowpass'},
            {'id': 'vcf_cutoff', 'name': 'VCF Cutoff Frequency', 'type': 'range', 'min': 0, 'max': 127, 'default': 85},
            {'id': 'vcf_resonance', 'name': 'VCF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 35}
        ]
    }
    
    jp8_names = [
        "11 Big Brass", "12 Octave Horns", "13 Warm Strings", "14 Fast Strings", "15 Poly Lead", "16 Reso Solo", "17 Funky Clav", "18 E.Piano 1",
        "21 Fat Analog Bass", "22 Sub Bass 8", "23 Sync Lead 1", "24 Sync Lead 2", "25 Cross-Mod Bell", "26 Space Pad 1", "27 Sweep Pad 2", "28 Harp/Flute",
        "31 Symphonic Tutti", "32 Chamber Cello", "33 Trumpet Solo", "34 Fanfare Brass", "35 Cathedral Pipe", "36 Jazz Organ", "37 Harpsichord", "38 Celesta Bell",
        "41 Slap Bass JP", "42 Fretless Bass", "43 Moog Reso Bass", "44 Pulse Lead 80", "45 Fifth Interval Lead", "46 Laser Gun Zap", "47 Wind Wave FX", "48 SciFi Siren",
        "51 Super Jupiter Brass", "52 Solina Strings", "53 Analog Brass II", "54 Pop Horn Section", "55 Wurly Tine", "56 Rotary Drawbar", "57 Marimba Mallet", "58 Vibraphone",
        "61 Heavy Modular Bass", "62 Techno Acid Lead", "63 Power Chord Hit", "64 Rave Saw Stack", "65 Ambient Space Scape", "66 Metallic Hit", "67 Thunder Explosion", "68 Jupiter-8 Anthem",
        "71 Dual Layer Grand", "72 Split Bass/Brass", "73 Split Bass/Lead", "74 Split Strings/Flute", "75 Arp Pluck Solo", "76 Solar Flare Sweep", "77 Reso Filter Scream", "78 Dream Pad JP",
        "81 Vintage Tine EP", "82 Honky Tonk JP", "83 Sitar Drone JP", "84 Koto Tremolo", "85 Timpani Hard Roll", "86 Noise Burst FX", "87 Helicopter Rotor", "88 Master Init 8"
    ]
    
    presets = []
    for idx, name in enumerate(jp8_names):
        cat = 'BRASS' if 'Brass' in name or 'Horn' in name else ('STRINGS' if 'String' in name else ('BASS' if 'Bass' in name else 'SYNTH'))
        presets.append({
            'bank': 'FACTORY PRESETS',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['jupiter-8', 'analog-flagship', cat.lower()]
        })
        
    save_profile_and_presets('jupiter-8', profile, presets)

# ==============================================================================
# 7. ROLAND MKS-80 SUPER JUPITER (1984)
# ==============================================================================
def build_mks80():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland MKS-80 Super Jupiter',
        'family': 'Jupiter Series',
        'category': '8-Voice Rackmount Analog Synthesizer',
        'year': 1984,
        'voice_architecture': {
            'voices': 8,
            'oscillators': '16 discrete analog VCOs (2 per voice) with CEM3340 (Rev 4) or Roland IR3R03 (Rev 5)',
            'filters': 'CEM3360/IR3109 resonant 24dB lowpass VCF + discrete HPF',
            'programmer': 'Full MPG-80 programmer interface support'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x02',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vcf_cutoff', 'name': 'VCF Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 85},
            {'id': 'vcf_resonance', 'name': 'VCF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 35},
            {'id': 'cross_mod', 'name': 'Cross Mod Intensity', 'type': 'range', 'min': 0, 'max': 127, 'default': 0},
            {'id': 'vco_sync', 'name': 'VCO Hard Sync', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'}
        ]
    }
    
    presets = []
    # 64 Patches + 128 Tones
    for i in range(64):
        presets.append({
            'bank': 'PATCH MEMORY',
            'program': i + 1,
            'name': f"MKS-80 Patch {i+1:02d}",
            'category': 'SUPER_JUPITER',
            'tags': ['mks-80', 'patch']
        })
    for i in range(128):
        presets.append({
            'bank': 'TONE MEMORY',
            'program': i + 1,
            'name': f"MKS-80 Tone {i+1:03d}",
            'category': 'TONE',
            'tags': ['mks-80', 'tone']
        })
        
    save_profile_and_presets('mks-80', profile, presets)

# ==============================================================================
# 8. ROLAND MKS-50 (1986)
# ==============================================================================
def build_mks50():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland MKS-50',
        'family': 'Alpha Juno Series',
        'category': '1U Rackmount Polyphonic Analog Synthesizer',
        'year': 1986,
        'voice_architecture': {
            'voices': 6,
            'engine': 'Alpha Juno DCO Engine with Chord Memory and PG-300 programmer support',
            'filter_type': 'Roland IR3109 24dB Resonant Lowpass VCF + HPF',
            'famous_patches': 'What The... (Hoover sound), Alpha Strings, Sub Bass'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x23',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vcf_cutoff', 'name': 'VCF Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 80},
            {'id': 'vcf_resonance', 'name': 'VCF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 30},
            {'id': 'chorus', 'name': 'Analog BBD Chorus', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'On'}
        ]
    }
    
    presets = []
    # 128 Patches (64 Preset + 64 Memory)
    for b_name in ['PRESET', 'MEMORY']:
        for i in range(64):
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': f"{b_name} Patch {i+1:02d}",
                'category': 'ALPHA_JUNO',
                'tags': ['mks-50', b_name.lower()]
            })
            
    save_profile_and_presets('mks-50', profile, presets)

# ==============================================================================
# 9. ROLAND SOUND CANVAS SC-55 (1991)
# ==============================================================================
def build_sc55():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland Sound Canvas SC-55',
        'family': 'Sound Canvas Series',
        'category': 'The Definitive General MIDI / GS Sound Module',
        'year': 1991,
        'voice_architecture': {
            'voices': 24,
            'parts': 16,
            'sound_engine': 'Roland GS Engine with 317 CD-quality instrument sounds + 9 drum sets',
            'effects': 'Built-in Digital Reverb (8 types) and Chorus (8 types)'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x42',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'reverb_send', 'name': 'Reverb Send Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 40},
            {'id': 'chorus_send', 'name': 'Chorus Send Level', 'type': 'range', 'min': 0, 'max': 127, 'default': 20},
            {'id': 'part_volume', 'name': 'Part Volume', 'type': 'range', 'min': 0, 'max': 127, 'default': 100},
            {'id': 'part_pan', 'name': 'Part Pan', 'type': 'range', 'min': -64, 'max': 63, 'default': 0}
        ]
    }
    
    # 317 GS Instruments
    presets = []
    for i in range(317):
        presets.append({
            'bank': 'GS INSTRUMENTS',
            'program': i + 1,
            'name': f"SC-55 Instrument {i+1:03d}",
            'category': 'GENERAL_MIDI_GS',
            'tags': ['sc-55', 'gs']
        })
        
    save_profile_and_presets('sc-55', profile, presets)

# ==============================================================================
# 10. ROLAND SOUND CANVAS SC-88 (1994)
# ==============================================================================
def build_sc88():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland Sound Canvas SC-88',
        'family': 'Sound Canvas Series',
        'category': 'Flagship 64-Voice 32-Part GS Sound Module',
        'year': 1994,
        'voice_architecture': {
            'voices': 64,
            'parts': 32,
            'sound_engine': 'Advanced GS Engine with 654 instrument sounds + 24 drum sets',
            'midi_ports': 'Dual MIDI inputs (A and B) for 32 simultaneous MIDI channels'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x45',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'reverb_send', 'name': 'Reverb Send', 'type': 'range', 'min': 0, 'max': 127, 'default': 40},
            {'id': 'chorus_send', 'name': 'Chorus Send', 'type': 'range', 'min': 0, 'max': 127, 'default': 20},
            {'id': 'delay_send', 'name': 'Delay Send', 'type': 'range', 'min': 0, 'max': 127, 'default': 0}
        ]
    }
    
    presets = []
    for i in range(654):
        presets.append({
            'bank': 'GS SOUND MAP',
            'program': i + 1,
            'name': f"SC-88 Sound {i+1:03d}",
            'category': 'GENERAL_MIDI_GS',
            'tags': ['sc-88', 'gs-flagship']
        })
        
    save_profile_and_presets('sc-88', profile, presets)

# ==============================================================================
# 11. ROLAND MC-303 (1996)
# ==============================================================================
def build_mc303():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland MC-303 Groovebox',
        'family': 'Groovebox Series',
        'category': 'The Original Dance Music Groovebox',
        'year': 1996,
        'voice_architecture': {
            'voices': 28,
            'parts': 8,
            'sound_engine': '448 dance sounds + 12 drum kits (TR-808, TR-909, CR-78)',
            'sequencer': '8-track pattern sequencer with 133 preset patterns and RPS'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x00 0x07',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'cutoff', 'name': 'Realtime Filter Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'resonance', 'name': 'Realtime Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 32}
        ]
    }
    
    presets = []
    for i in range(448):
        presets.append({
            'bank': 'DANCE TONES',
            'program': i + 1,
            'name': f"MC-303 Tone {i+1:03d}",
            'category': 'GROOVEBOX',
            'tags': ['mc-303', 'groove']
        })
        
    save_profile_and_presets('mc-303', profile, presets)

# ==============================================================================
# 12. ROLAND MC-505 (1998)
# ==============================================================================
def build_mc505():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Roland Corporation',
        'name': 'Roland MC-505 Groovebox',
        'family': 'Groovebox Series',
        'category': 'Flagship Dance Music Production Groovebox',
        'year': 1998,
        'voice_architecture': {
            'voices': 64,
            'parts': 8,
            'sound_engine': '640 patches + 26 rhythm sets',
            'controller': 'D-Beam Controller & Realtime Megamix sliders and control knobs',
            'sequencer': '714 preset patterns + 200 user patterns + RPS'
        },
        'midi_specs': {
            'basic_channel': 1,
            'model_id': '0x00 0x14',
            'sysex_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'cutoff', 'name': 'Filter Cutoff Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'resonance', 'name': 'Filter Resonance Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 32},
            {'id': 'd_beam_assign', 'name': 'D-Beam Target', 'type': 'enum', 'options': ['Cutoff', 'Turntable', 'Pitch', 'Ad Lib'], 'default': 'Cutoff'}
        ]
    }
    
    presets = []
    for b_letter in ['A', 'B', 'C', 'D', 'E']:
        for i in range(128):
            presets.append({
                'bank': f'PRESET {b_letter}',
                'program': i + 1,
                'name': f"MC-505 Patch {b_letter}{i+1:03d}",
                'category': 'GROOVEBOX',
                'tags': ['mc-505', f'preset-{b_letter.lower()}']
            })
            
    save_profile_and_presets('mc-505', profile, presets)

if __name__ == '__main__':
    build_jv1080()
    build_jv2080()
    build_jd800()
    build_jd990()
    build_juno106()
    build_jupiter8()
    build_mks80()
    build_mks50()
    build_sc55()
    build_sc88()
    build_mc303()
    build_mc505()
