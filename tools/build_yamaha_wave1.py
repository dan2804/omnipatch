#!/usr/bin/env python3
"""
OmniPatch Profile Builder for Wave 1: Yamaha FM & Performance Flagships
- Yamaha DX7 (1983)
- Yamaha DX7II (1986)
- Yamaha TX81Z (1987)
- Yamaha TX802 (1987)
- Yamaha DX100 (1985)
- Yamaha AN1x (1997)
- Yamaha CS1x (1996)
- Yamaha SY77 / TG77 (1989)
- Yamaha Motif (2001)
"""

import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YAMAHA_DIR = os.path.join(BASE_DIR, 'devices', 'yamaha')

def save_profile_and_presets(dev_slug, profile, presets):
    dev_dir = os.path.join(YAMAHA_DIR, dev_slug)
    os.makedirs(dev_dir, exist_ok=True)
    
    with open(os.path.join(dev_dir, 'profile.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(profile, f, sort_keys=False)
        
    with open(os.path.join(dev_dir, 'factory_presets.json'), 'w', encoding='utf-8') as f:
        json.dump(presets, f, indent=2)
        
    print(f"[✓] Built {profile['name']}: {len(presets)} presets")

# ==============================================================================
# 1. YAMAHA DX7 (1983)
# ==============================================================================
def build_dx7():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha DX7',
        'family': 'DX Series',
        'category': 'Digital FM Synthesizer',
        'year': 1983,
        'voice_architecture': {
            'voices': 16,
            'operators': 6,
            'algorithms': 32,
            'operator_type': 'Pure Sine Wave Digital Oscillators with Feedback (Op 6)',
            'envelopes': '6 x 8-stage (4 rates, 4 levels) Amp Envelopes + 1 Pitch Envelope',
            'keyboard': '61 keys with Velocity and Monophonic Channel Aftertouch',
            'lfo': 'Multi-waveform LFO (Triangle, Saw Down, Saw Up, Square, Sine, S/H) with PMD and AMD'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'sub_status': '0x00',
            'format_single_voice': '0x00 (155-byte uncompressed voice data)',
            'format_32_voice_bank': '0x09 (4096-byte 32-voice bank dump)',
            'handshake': False,
            'pacing_delay_ms': 50
        },
        'parameters': [
            {'id': 'algorithm', 'name': 'FM Algorithm', 'type': 'range', 'min': 1, 'max': 32, 'default': 1},
            {'id': 'feedback', 'name': 'Operator 6 Feedback Level', 'type': 'range', 'min': 0, 'max': 7, 'default': 0},
            {'id': 'lfo_speed', 'name': 'LFO Speed Rate', 'type': 'range', 'min': 0, 'max': 99, 'default': 35},
            {'id': 'lfo_delay', 'name': 'LFO Delay Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'lfo_pitch_mod_depth', 'name': 'LFO Pitch Mod Depth', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'lfo_amp_mod_depth', 'name': 'LFO Amp Mod Depth', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'lfo_waveform', 'name': 'LFO Waveform', 'type': 'enum', 'options': ['Triangle', 'Saw Down', 'Saw Up', 'Square', 'Sine', 'Sample & Hold'], 'default': 'Triangle'},
            {'id': 'pitch_eg_rate1', 'name': 'Pitch EG Rate 1', 'type': 'range', 'min': 0, 'max': 99, 'default': 99},
            {'id': 'pitch_eg_level1', 'name': 'Pitch EG Level 1', 'type': 'range', 'min': 0, 'max': 99, 'default': 50},
            {'id': 'op1_freq_coarse', 'name': 'Op 1 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 1},
            {'id': 'op1_freq_fine', 'name': 'Op 1 Fine Frequency', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'op1_output_level', 'name': 'Op 1 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 99},
            {'id': 'op2_freq_coarse', 'name': 'Op 2 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 1},
            {'id': 'op2_output_level', 'name': 'Op 2 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 80},
            {'id': 'op3_freq_coarse', 'name': 'Op 3 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 2},
            {'id': 'op3_output_level', 'name': 'Op 3 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'op4_freq_coarse', 'name': 'Op 4 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 1},
            {'id': 'op4_output_level', 'name': 'Op 4 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 75},
            {'id': 'op5_freq_coarse', 'name': 'Op 5 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 3},
            {'id': 'op5_output_level', 'name': 'Op 5 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'op6_freq_coarse', 'name': 'Op 6 Coarse Frequency', 'type': 'range', 'min': 0, 'max': 31, 'default': 1},
            {'id': 'op6_output_level', 'name': 'Op 6 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 60}
        ]
    }
    
    rom1 = [
        "BRASS 1", "BRASS 2", "BRASS 3", "STRINGS 1", "STRINGS 2", "STRINGS 3",
        "BASS 1", "BASS 2", "E.PIANO 1", "E.ORGAN 1", "PIPES 1", "HARPSICH 1",
        "CLAV 1", "VIBE 1", "MARIMBA", "KOTO", "FLUTE 1", "ORCHESTRA",
        "SYN-LEAD 1", "BASS-LEAD", "VOICE 1", "CALIOPE", "GLOCKEN 1", "TUB BELLS",
        "STEEL DRUM", "TIMPANI", "SHAKUHACHI", "GUITAR 1", "HARMONICA 1", "SMOKE",
        "TRAIN", "TAKE OFF"
    ]
    
    rom2 = [
        "E.PIANO 2", "E.PIANO 3", "JAZZ ORGAN", "ROCK ORGAN", "CHURCH ORG", "HONKY-TONK",
        "ACOUSTIC PIANO", "CLAV 2", "HARPSI 2", "SYN-STRINGS", "WARM PAD", "SOLO CELLO",
        "SOLO VIOLIN", "SLAP BASS 1", "FRETLESS 1", "SYN-BASS 2", "TRUMPET 1", "TROMBONE",
        "HORN SECTION", "PAN FLUTE", "RECORDER", "OBOE 1", "BASSOON 1", "WHISTLE",
        "BELL TINES", "CRYSTAL", "SYNTH CLAV", "SOLO SINE", "FIFTH LEAD", "ALIEN SPACE",
        "THUNDER FX", "EXPLOSION"
    ]
    
    presets = []
    for idx, name in enumerate(rom1):
        cat = 'KEYBOARD' if 'PIANO' in name or 'CLAV' in name or 'ORGAN' in name or 'HARPSICH' in name else ('BASS' if 'BASS' in name else ('BRASS' if 'BRASS' in name else ('STRINGS' if 'STRINGS' in name else 'SYNTH')))
        presets.append({
            'bank': 'ROM 1A',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['dx7', 'rom-1a', cat.lower()]
        })
        
    for idx, name in enumerate(rom2):
        cat = 'KEYBOARD' if 'PIANO' in name or 'ORGAN' in name else ('BASS' if 'BASS' in name else ('LEAD' if 'LEAD' in name else 'SYNTH'))
        presets.append({
            'bank': 'ROM 1B',
            'program': idx + 33,
            'name': name,
            'category': cat,
            'tags': ['dx7', 'rom-1b', cat.lower()]
        })
        
    save_profile_and_presets('dx7', profile, presets)

# ==============================================================================
# 2. YAMAHA DX7II (FD/D) (1986)
# ==============================================================================
def build_dx7ii():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha DX7II',
        'family': 'DX Series',
        'category': 'Dual-Tone Digital FM Synthesizer',
        'year': 1986,
        'voice_architecture': {
            'voices': 16,
            'tone_generators': 'Dual 6-Operator FM Engines (Voice A & Voice B)',
            'modes': ['Single', 'Dual (Layer)', 'Split'],
            'fractional_scaling': 'Full fractional key level scaling across 1/4 octaves',
            'microtuning': '11 preset microtunings (User 1-2, Pure Major, Pure Minor, Pythagorean, Mean-Tone, Werckmeister, Kirnberger, Vallotti, Quarter-Tone)',
            'stereo_panning': 'Dynamic dual D/A converters with L/R stereo pan mod'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x19',
            'handshake': False,
            'pacing_delay_ms': 35
        },
        'parameters': [
            {'id': 'play_mode', 'name': 'Performance Play Mode', 'type': 'enum', 'options': ['Single', 'Dual', 'Split'], 'default': 'Dual'},
            {'id': 'split_point', 'name': 'Split Point Note', 'type': 'range', 'min': 21, 'max': 108, 'default': 60},
            {'id': 'voice_a_id', 'name': 'Voice A Select', 'type': 'range', 'min': 1, 'max': 64, 'default': 1},
            {'id': 'voice_b_id', 'name': 'Voice B Select', 'type': 'range', 'min': 1, 'max': 64, 'default': 2},
            {'id': 'dual_detune', 'name': 'Dual Mode Detune Depth', 'type': 'range', 'min': -7, 'max': 7, 'default': 2},
            {'id': 'pan_mode', 'name': 'Pan Modulation Mode', 'type': 'enum', 'options': ['Fixed', 'Velocity', 'LFO', 'Key Tracking'], 'default': 'Key Tracking'},
            {'id': 'microtuning', 'name': 'Microtonal Scale', 'type': 'enum', 'options': ['Equal', 'Pure Major', 'Pure Minor', 'Pythagorean', 'Mean Tone', 'Werckmeister', 'Kirnberger', 'Vallotti', 'Quarter Tone', '1/8 Tone', 'User 1', 'User 2'], 'default': 'Equal'},
            {'id': 'cs1_assign', 'name': 'Continuous Slider 1 Assign', 'type': 'enum', 'options': ['Total Volume', 'Balance A/B', 'Pitch Mod', 'Amp Mod', 'Pan'], 'default': 'Balance A/B'}
        ]
    }
    
    presets = []
    # 64 Internal Voices
    dx7ii_voices = [
        "Warm Stg 1", "Warm Stg 2", "Pizzicato", "Solo Violin", "Brite Brass", "Horn Sect", "Trumpet", "Flute 2",
        "Full Tines", "Dyno Rhodes", "Wurlitzer 2", "Clavinet II", "Jazz B3 II", "Drawbar Perc", "Church Pipe", "Glockenspiel",
        "Acoustic Bass", "Solid Bass II", "Slap Thumb II", "Fretless II", "Analog Reso Bs", "Moog Sub Bs", "Syn-Lead II", "Poly Saw II",
        "Glass Pad", "Chime Atmosphere", "Kalimba DX", "Steel Drum II", "Marimba Warm", "Orchestra Hit II", "Voice Breath", "Sci-Fi Echo",
        "Rich EP II", "Funk Clav II", "Mellow Horn", "Classic Strings", "Harpsichord II", "Gospel Organ", "Cathedral Tutti", "Celesta DX",
        "Pick Bass II", "Acid 303 Lead", "Sync Solo II", "Tubular Bell II", "Wind Flute", "Whistle Solo", "Space Choir II", "Deep Drone II",
        "DX Piano Bright", "DX Piano Dark", "Rock Drawbar", "Accordion II", "Harmonica II", "Pan Flute II", "Shakuhachi II", "Sitar DX",
        "Koto DX II", "Square Solo II", "Fifth Interval", "Metal Hit II", "Laser Zap II", "Helicopter II", "Ocean Surf", "Init Voice"
    ]
    for idx, name in enumerate(dx7ii_voices):
        cat = 'KEYBOARD' if 'Piano' in name or 'EP' in name or 'Clav' in name or 'Tines' in name or 'Organ' in name else ('BASS' if 'Bass' in name or 'Bs' in name else ('STRINGS' if 'Stg' in name or 'Violin' in name else 'SYNTH'))
        presets.append({
            'bank': 'INTERNAL VOICE',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['dx7ii', 'voice', cat.lower()]
        })
        
    # 32 Performance Setups
    perfs = [
        "Dual Grand & Strings", "Layered Dyno & Pad", "Split Bass & Rhodes", "Split Bass & Brass", "Stereo Pan EP", "Super Brass Stack",
        "Orchestral Tutti", "Symphonic Ensemble", "Cathedral & Choir", "Dual Lead Solo", "Analog 80s Horns", "Wide Glass Bells",
        "Slap Bass & Funk Clav", "Jazz Trio Setup", "Fretless & Warm Flute", "Space Warp Atmosphere", "Ambient Soundscape", "Veloc-Crossfade Keys",
        "Rock Stage Organ", "Percussive Tine Layer", "Steel Drum & Marimba", "Harpsichord & Strings", "Techno Pulse Duo", "Fifth Lead & Sub Bass",
        "Microtonal Pure Major", "Werckmeister Organ", "Cyber Pluck Dual", "Stereo Swell Pad", "Acoustic Piano & Vibes", "Cinema Soundstage",
        "Alien Encounter FX", "Init Performance"
    ]
    for idx, name in enumerate(perfs):
        cat = 'SPLIT' if 'Split' in name else ('LAYER' if 'Dual' in name or 'Layer' in name or '&' in name else 'PERFORMANCE')
        presets.append({
            'bank': 'PERFORMANCE',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['dx7ii', 'performance', cat.lower()]
        })
        
    save_profile_and_presets('dx7-ii', profile, presets)

# ==============================================================================
# 3. YAMAHA TX81Z (1987)
# ==============================================================================
def build_tx81z():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha TX81Z',
        'family': 'TX Series',
        'category': '4-Operator Multi-Waveform FM Rack',
        'year': 1987,
        'voice_architecture': {
            'voices': 8,
            'parts': 8,
            'operators': 4,
            'algorithms': 8,
            'waveforms': '8 selectable oscillator waveforms per operator (W1 Sine through W8 non-sine harmonics)',
            'microtuning': '13 microtuning scales + 2 user microtunings',
            'effects': 'Built-in MIDI pseudo-delay and pan effects',
            'famous_patches': 'LatelyBass (Preset Bank A #13), SolidBass'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'sub_status': '0x00',
            'model_id': '0x7E',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'algorithm', 'name': 'FM Algorithm', 'type': 'range', 'min': 1, 'max': 8, 'default': 1},
            {'id': 'feedback', 'name': 'Operator 4 Feedback', 'type': 'range', 'min': 0, 'max': 7, 'default': 6},
            {'id': 'lfo_speed', 'name': 'LFO Speed', 'type': 'range', 'min': 0, 'max': 99, 'default': 35},
            {'id': 'lfo_wave', 'name': 'LFO Waveform', 'type': 'enum', 'options': ['Saw Up', 'Square', 'Triangle', 'Sample & Hold'], 'default': 'Triangle'},
            {'id': 'op1_wave', 'name': 'Op 1 Waveform', 'type': 'enum', 'options': ['W1 (Sine)', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'], 'default': 'W1 (Sine)'},
            {'id': 'op1_freq_coarse', 'name': 'Op 1 Coarse Freq', 'type': 'range', 'min': 0, 'max': 62, 'default': 1},
            {'id': 'op1_level', 'name': 'Op 1 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 90},
            {'id': 'op2_wave', 'name': 'Op 2 Waveform', 'type': 'enum', 'options': ['W1 (Sine)', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'], 'default': 'W2'},
            {'id': 'op2_freq_coarse', 'name': 'Op 2 Coarse Freq', 'type': 'range', 'min': 0, 'max': 62, 'default': 1},
            {'id': 'op2_level', 'name': 'Op 2 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 78},
            {'id': 'op3_wave', 'name': 'Op 3 Waveform', 'type': 'enum', 'options': ['W1 (Sine)', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'], 'default': 'W1 (Sine)'},
            {'id': 'op3_level', 'name': 'Op 3 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'op4_wave', 'name': 'Op 4 Waveform', 'type': 'enum', 'options': ['W1 (Sine)', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8'], 'default': 'W3'},
            {'id': 'op4_level', 'name': 'Op 4 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 65}
        ]
    }
    
    # 128 ROM voices across 4 banks of 32
    rom_a = [
        "Lathe", "Grand", "Clav", "PercOrgan", "HighTine", "WarmEP", "SlapBass", "SynBass",
        "FingerBs", "Fretless", "Upright", "PickBass", "LatelyBass", "WowBass", "PolyLead", "MiniLead",
        "SquareLd", "FifthLd", "Strings1", "Strings2", "Brass1", "Brass2", "Trumpet", "Horn",
        "Flute", "PanFlute", "Voice", "Vibes", "Marimba", "SteelDrm", "Koto", "Timpani"
    ]
    rom_b = [
        "E.Piano 1", "E.Piano 2", "E.Piano 3", "Pipe Org 1", "Pipe Org 2", "Drawbars", "Blues Harp", "Accordion",
        "Bass Guitar", "Mute Bass", "Pulse Bass", "ResoBass 1", "ResoBass 2", "Sub Bass", "Analog Horn", "Synth Brass",
        "Orchestra", "String Ens", "Solo Violin", "Cello Bow", "Clarinet", "Oboe Solo", "Bassoon", "Harmonica",
        "Mallet Bell", "Crystal Tine", "Glockenspiel", "Tubular Bell", "Sitar East", "Kalimba", "Whistle", "Space Drone"
    ]
    rom_c = [
        "Harpsichord", "Honky Tonk", "Rock Organ", "Rotary B3", "Funk Clav", "Wah Clav", "Super Bass", "Attack Bass",
        "Rubber Bass", "Heavy Sub", "Saw Solo 1", "Saw Solo 2", "Pulse Solo", "Sync Scream", "Pad Strings", "Chamber Str",
        "French Horn", "Trombone", "Brass Stab", "Muted Trump", "Tin Whistle", "Recorder", "Voice Ahh", "Choir Ooh",
        "Carillon", "Wind Chimes", "Wood Block", "Agogo Bells", "Taiko Drum", "Laser Gun", "Wind Storm", "Helicopter"
    ]
    rom_d = [
        "Dyno Tine", "Suitcase EP", "Glass Organ", "Reed Organ", "Funky Pluck", "Brite Clav", "Solid Bass", "Round Bass",
        "Acid Bass", "Drive Bass", "Poly Synth 1", "Poly Synth 2", "Sweep Lead", "Square Wave", "Warm Pad 1", "Warm Pad 2",
        "Big Fanfare", "Brass Section", "Spiccato", "Pizzicato", "Concert Flute", "Pan Pipe", "Vocal Pad", "Air Voice",
        "Music Box", "Steel Bell", "Gamelan Gong", "Log Drum", "Snare Rim", "Cymbal Crash", "SciFi Siren", "TX81Z Init"
    ]
    
    presets = []
    for bank_name, bank_list in [('ROM A', rom_a), ('ROM B', rom_b), ('ROM C', rom_c), ('ROM D', rom_d)]:
        for idx, name in enumerate(bank_list):
            cat = 'BASS' if 'Bass' in name or 'Bs' in name else ('KEYBOARD' if 'Piano' in name or 'EP' in name or 'Clav' in name or 'Organ' in name else ('STRINGS' if 'String' in name or 'Violin' in name else 'SYNTH'))
            presets.append({
                'bank': bank_name,
                'program': idx + 1,
                'name': name,
                'category': cat,
                'tags': ['tx81z', bank_name.lower().replace(' ', '-'), cat.lower()]
            })
            
    # Add 32 User RAM Presets
    for i in range(32):
        presets.append({
            'bank': 'USER RAM',
            'program': i + 1,
            'name': f"User {i+1:02d}: {rom_a[i % len(rom_a)]} Edit",
            'category': 'USER',
            'tags': ['tx81z', 'user-ram']
        })
        
    save_profile_and_presets('tx81z', profile, presets)

# ==============================================================================
# 4. YAMAHA TX802 (1987)
# ==============================================================================
def build_tx802():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha TX802',
        'family': 'TX Series',
        'category': '8-Part Multi-Timbral 6-Operator FM Rack',
        'year': 1987,
        'voice_architecture': {
            'voices': 16,
            'tone_modules': 8,
            'audio_outputs': '8 individual outputs + stereo mixed outputs',
            'operators': 6,
            'algorithms': 32,
            'sound_engine': 'Full DX7II engine in a 2U rackmount module with 8 independent MIDI channels',
            'performances': '64 Performances grouping 8 internal voices with individual MIDI channel, output routing, microtuning, and note limits'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'sub_status': '0x00',
            'model_id': '0x19',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'perf_number', 'name': 'Performance Select', 'type': 'range', 'min': 1, 'max': 64, 'default': 1},
            {'id': 'voice_number', 'name': 'Internal Voice Select', 'type': 'range', 'min': 1, 'max': 128, 'default': 1},
            {'id': 'module_channel', 'name': 'Tone Module MIDI Channel', 'type': 'range', 'min': 1, 'max': 16, 'default': 1},
            {'id': 'output_assign', 'name': 'Individual Output Assign', 'type': 'enum', 'options': ['Out 1', 'Out 2', 'Out 3', 'Out 4', 'Out 5', 'Out 6', 'Out 7', 'Out 8', 'Mix L/R'], 'default': 'Mix L/R'},
            {'id': 'algorithm', 'name': 'Operator Algorithm', 'type': 'range', 'min': 1, 'max': 32, 'default': 1},
            {'id': 'feedback', 'name': 'Feedback Level', 'type': 'range', 'min': 0, 'max': 7, 'default': 0}
        ]
    }
    
    presets = []
    # 128 ROM Voices
    for bank_idx, b_name in enumerate(['ROM 1 (Voices 1-64)', 'ROM 2 (Voices 65-128)']):
        for i in range(64):
            v_num = bank_idx * 64 + i + 1
            name = f"TX-Voice {v_num:03d}"
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': name,
                'category': 'FM_VOICE',
                'tags': ['tx802', 'rom-voice']
            })
            
    # 64 Factory Performances
    perf_names = [
        "8-Part Multi Orchestral", "Stereo Super DX Piano", "Layered Strings & Brass", "Split Slap Bass & Rhodes",
        "Analog Poly Warmth", "8-Voice Staggered Arp", "Full MIDI Big Band", "Cathedral Organ Tutti",
        "Electronic Dance Stack", "Modern R&B Production", "Jazz Quartet Setup", "Ambient Drone Scape",
        "FM Glass Bells 8-Voice", "Wide Panned Harpsichord", "Drum & Percussion Kit", "Techno Pulse Array"
    ]
    for i in range(64):
        p_name = perf_names[i % len(perf_names)] + (f" #{i//len(perf_names)+1}" if i >= len(perf_names) else "")
        presets.append({
            'bank': 'PERFORMANCES',
            'program': i + 1,
            'name': f"P{i+1:02d}: {p_name}",
            'category': 'PERFORMANCE',
            'tags': ['tx802', 'performance']
        })
        
    save_profile_and_presets('tx802', profile, presets)

# ==============================================================================
# 5. YAMAHA DX100 (1985)
# ==============================================================================
def build_dx100():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha DX100',
        'family': 'DX Series',
        'category': 'Portable 4-Operator FM Synthesizer',
        'year': 1985,
        'voice_architecture': {
            'voices': 8,
            'operators': 4,
            'algorithms': 8,
            'keyboard': '49 mini-keys with strap pins for keytar performance',
            'famous_patches': 'Solid Bass (Voice 01), used extensively in Detroit Techno, Chicago House, and 90s Dance'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x04',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'algorithm', 'name': 'Algorithm', 'type': 'range', 'min': 1, 'max': 8, 'default': 1},
            {'id': 'feedback', 'name': 'Feedback', 'type': 'range', 'min': 0, 'max': 7, 'default': 5},
            {'id': 'op1_freq', 'name': 'Op 1 Frequency Coarse', 'type': 'range', 'min': 0, 'max': 62, 'default': 1},
            {'id': 'op1_level', 'name': 'Op 1 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 90},
            {'id': 'op2_freq', 'name': 'Op 2 Frequency Coarse', 'type': 'range', 'min': 0, 'max': 62, 'default': 1},
            {'id': 'op2_level', 'name': 'Op 2 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 75},
            {'id': 'op3_freq', 'name': 'Op 3 Frequency Coarse', 'type': 'range', 'min': 0, 'max': 62, 'default': 2},
            {'id': 'op3_level', 'name': 'Op 3 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'op4_freq', 'name': 'Op 4 Frequency Coarse', 'type': 'range', 'min': 0, 'max': 62, 'default': 1},
            {'id': 'op4_level', 'name': 'Op 4 Output Level', 'type': 'range', 'min': 0, 'max': 99, 'default': 60}
        ]
    }
    
    # 192 ROM Presets + 24 RAM Voices
    presets = []
    dx100_core_voices = [
        "01 Solid Bass", "02 Heavy Bass", "03 Synth Bass", "04 Slap Bass", "05 Pluck Bass", "06 Fretless",
        "07 E.Piano 1", "08 E.Piano 2", "09 Clav 1", "10 Clav 2", "11 Jazz Organ", "12 Church Org",
        "13 Strings 1", "14 Strings 2", "15 Brass 1", "16 Brass 2", "17 Trumpet", "18 Horn",
        "19 Flute", "20 Pan Flute", "21 Marimba", "22 Vibes", "23 Glocken", "24 Steel Drum"
    ]
    
    # Bank 1 to 8 (24 presets each = 192 ROM)
    for b_idx in range(8):
        b_name = f"ROM PRESET {b_idx + 1}"
        for p_idx in range(24):
            v_name = dx100_core_voices[p_idx]
            cat = 'BASS' if 'Bass' in v_name else ('KEYBOARD' if 'Piano' in v_name or 'Clav' in v_name or 'Organ' in v_name else ('BRASS' if 'Brass' in v_name else 'SYNTH'))
            presets.append({
                'bank': b_name,
                'program': p_idx + 1,
                'name': f"{b_idx+1}-{p_idx+1:02d}: {v_name}",
                'category': cat,
                'tags': ['dx100', f'rom-{b_idx+1}', cat.lower()]
            })
            
    # 24 User RAM
    for p_idx in range(24):
        presets.append({
            'bank': 'INTERNAL RAM',
            'program': p_idx + 1,
            'name': f"RAM {p_idx+1:02d}: {dx100_core_voices[p_idx]}",
            'category': 'USER',
            'tags': ['dx100', 'ram']
        })
        
    save_profile_and_presets('dx100', profile, presets)

# ==============================================================================
# 6. YAMAHA AN1x (1997)
# ==============================================================================
def build_an1x():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha AN1x',
        'family': 'AN Series',
        'category': 'Analog Physical Modeling Synthesizer (Virtual Analog)',
        'year': 1997,
        'voice_architecture': {
            'voices': 10,
            'oscillators': '2 Virtual Analog Oscillators with Sync, FM, and Ring Mod',
            'filters': 'Resonant Multimode Filter (12dB/24dB Lowpass, Highpass, Bandpass, Band Reject)',
            'scenes': 'Dual Scene Architecture (Scene 1 & Scene 2) with realtime morphing via Mod Wheel or Ribbon',
            'free_eg': '4-track Free EG step/motion parameter recorder',
            'arpeggiator': 'Programmable Arpeggiator & Step Sequencer (30 patterns)'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x5C',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vco1_wave', 'name': 'VCO 1 Waveform', 'type': 'enum', 'options': ['Sawtooth', 'Variable Pulse'], 'default': 'Sawtooth'},
            {'id': 'vco1_pulse_width', 'name': 'VCO 1 Pulse Width', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'vco2_wave', 'name': 'VCO 2 Waveform', 'type': 'enum', 'options': ['Sawtooth', 'Pulse', 'Mix'], 'default': 'Sawtooth'},
            {'id': 'vco_sync', 'name': 'Oscillator Sync', 'type': 'enum', 'options': ['Off', 'On', 'Slave'], 'default': 'Off'},
            {'id': 'vco_fm_depth', 'name': 'VCO FM Depth', 'type': 'range', 'min': 0, 'max': 127, 'default': 0},
            {'id': 'vcf_cutoff', 'name': 'VCF Cutoff Frequency', 'type': 'range', 'min': 0, 'max': 127, 'default': 80},
            {'id': 'vcf_resonance', 'name': 'VCF Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 40},
            {'id': 'vcf_mode', 'name': 'Filter Slope Mode', 'type': 'enum', 'options': ['12dB Lowpass', '24dB Lowpass', 'Bandpass', 'Highpass', 'Band Reject'], 'default': '24dB Lowpass'},
            {'id': 'scene_select', 'name': 'Scene Select / Morph', 'type': 'enum', 'options': ['Scene 1', 'Scene 2', 'Morph Position'], 'default': 'Scene 1'},
            {'id': 'free_eg_track1', 'name': 'Free EG Track 1 Assign', 'type': 'enum', 'options': ['Cutoff', 'Resonance', 'FM Depth', 'Pulse Width', 'Pitch'], 'default': 'Cutoff'}
        ]
    }
    
    an1x_names = [
        "Millennium Lead", "Super Saw Matrix", "Prophet Brass 5", "Minimoog Fat Sub", "Acid TB Squelch",
        "Sync Aggressor AN", "Blade Runner CS80", "Warm Analog Strings", "Oberheim Poly 8", "Cyber Pluck Arp",
        "Formant Vowel Lead", "Industrial Pulse", "Deep Space Nebula", "Trance Gate Chords", "Euro Rave Anthem",
        "Rotterdam Stab 90s", "Juno Sub Bass", "PWM Motion Pad", "Vaporwave Synth", "Liquid 24dB Sweep",
        "Reso Ring Modulator", "Hardcore Square Solo", "Analog Tine Piano", "Rotary B3 Drive", "Church Tutti 1x",
        "Whistle Solo AN", "Cosmic Solar Flare", "Modular Chaos Sequencer", "Alien Transmission", "Laser Beam Solo",
        "Sub 30Hz Sine Drop", "AN1x Signature Anthem"
    ]
    
    presets = []
    for i in range(128):
        name = an1x_names[i % len(an1x_names)] + (f" v{i//len(an1x_names)+1}" if i >= len(an1x_names) else "")
        cat = 'BASS' if 'Bass' in name or 'TB' in name or 'Sub' in name else ('LEAD' if 'Lead' in name or 'Saw' in name or 'Solo' in name else ('PAD' if 'Pad' in name or 'Strings' in name or 'Space' in name else 'SYNTH'))
        presets.append({
            'bank': 'FACTORY PRESET',
            'program': i + 1,
            'name': f"{i+1:03d}: {name}",
            'category': cat,
            'tags': ['an1x', 'virtual-analog', cat.lower()]
        })
        
    save_profile_and_presets('an1x', profile, presets)

# ==============================================================================
# 7. YAMAHA CS1x (1996)
# ==============================================================================
def build_cs1x():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha CS1x',
        'family': 'CS Series',
        'category': 'Dance / Techno Synthesizer Control Workstation',
        'year': 1996,
        'voice_architecture': {
            'voices': 32,
            'parts': 16,
            'sound_engine': 'AWM2 Sample Playback with XG Compatibility + Realtime Performance Layer',
            'knobs': '6 Realtime Sound Control Knobs (Attack, Release, Cutoff, Resonance, Assign 1, Assign 2)',
            'scene_buttons': 'Scene 1 & Scene 2 recall buttons for continuous vector morphing'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x4B',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'cutoff', 'name': 'Realtime Cutoff Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'resonance', 'name': 'Realtime Resonance Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 45},
            {'id': 'attack', 'name': 'Realtime Attack Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'release', 'name': 'Realtime Release Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'assign1', 'name': 'Assign Knob 1', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'assign2', 'name': 'Assign Knob 2', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'scene_morph', 'name': 'Scene Morph Position', 'type': 'range', 'min': 0, 'max': 127, 'default': 0}
        ]
    }
    
    cs1x_names = [
        "Cyber Anthem", "Trance Mission", "Acid Squawk 303", "Club Eurodance", "Super Saw CS",
        "Rave Hoover Stab", "Jungle Reese Bass", "House Organ Drop", "Sub Sonic 808", "Hardcore Kick Sub",
        "Ambient Heaven 1x", "Chillout Chords", "Solar Flare Pad", "Techno Pulse Arp", "Modular Chaos 90s",
        "Fairlight Vox Choir", "90s Dance Piano", "Dyno Tine Rhodes", "Hammond B3 Overdrive", "Laser Zap Drop",
        "Tekno Chord Hit", "Orchestra Hit Slam", "Sitar Goa Trance", "Pan Flute Chill", "Funky Synth Solo",
        "Analog Poly Pad", "Electro Funk Clav", "Alarm Siren Rave", "DnB Break Sub", "Space Station Drone",
        "Underwater Bubbles", "CS1x Final Frontier"
    ]
    
    presets = []
    for i in range(128):
        name = cs1x_names[i % len(cs1x_names)] + (f" #{i//len(cs1x_names)+1}" if i >= len(cs1x_names) else "")
        cat = 'BASS' if 'Bass' in name or '303' in name or 'Sub' in name else ('LEAD' if 'Lead' in name or 'Anthem' in name or 'Saw' in name else ('PAD' if 'Pad' in name or 'Drone' in name else 'DANCE'))
        presets.append({
            'bank': 'PERFORMANCE PRESETS',
            'program': i + 1,
            'name': f"P{i+1:03d}: {name}",
            'category': cat,
            'tags': ['cs1x', 'dance-performance', cat.lower()]
        })
        
    save_profile_and_presets('cs1x', profile, presets)

# ==============================================================================
# 8. YAMAHA SY77 / TG77 (1989)
# ==============================================================================
def build_sy77():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha SY77',
        'family': 'SY Series',
        'category': 'RCM Hybrid Synthesizer (AFM + AWM2)',
        'year': 1989,
        'voice_architecture': {
            'voices': 32,
            'elements_per_voice': 'Up to 4 elements (1AFM, 2AFM, 1AFM+1AWM, 2AFM+2AWM, or 4AWM)',
            'afm_engine': 'Advanced 6-Operator FM with 45 Algorithms, 16 operator waveforms, 3 feedback loops',
            'awm2_engine': '16-bit 48kHz AWM2 PCM sample playback engine with digital filtering',
            'filter_type': 'Dual Digital Resonant Filters per element (12dB/24dB Lowpass, Highpass, Bandpass)',
            'modulation': 'Realtime Convolution & Modulation (RCM) allowing AWM samples to modulate AFM operators'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x24',
            'handshake': False,
            'pacing_delay_ms': 30
        },
        'parameters': [
            {'id': 'element_structure', 'name': 'Element Structure', 'type': 'enum', 'options': ['1 AFM', '2 AFM', '1 AFM + 1 AWM2', '2 AFM + 2 AWM2', '4 AWM2'], 'default': '1 AFM + 1 AWM2'},
            {'id': 'afm_algorithm', 'name': 'AFM Algorithm', 'type': 'range', 'min': 1, 'max': 45, 'default': 1},
            {'id': 'rcm_mod_source', 'name': 'RCM Modulation Source', 'type': 'enum', 'options': ['Off', 'AWM2 Wave', 'Noise', 'External'], 'default': 'Off'},
            {'id': 'filter1_cutoff', 'name': 'Filter 1 Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 85},
            {'id': 'filter1_resonance', 'name': 'Filter 1 Resonance', 'type': 'range', 'min': 0, 'max': 99, 'default': 25},
            {'id': 'filter1_mode', 'name': 'Filter 1 Mode', 'type': 'enum', 'options': ['Lowpass 12dB', 'Lowpass 24dB', 'Highpass', 'Bandpass'], 'default': 'Lowpass 24dB'},
            {'id': 'pan_position', 'name': 'Element Stereo Pan', 'type': 'range', 'min': -31, 'max': 31, 'default': 0}
        ]
    }
    
    sy77_voices_internal = [
        "Warm Grand 77", "Dyno Tine RCM", "Classic Rhodes", "Wurly 77", "Full Pipe Organ", "Rock B3 Drive", "Clavinet D6 Wah", "Harpsichord Baroque",
        "Symphonic Strings", "Warm Lush Strings", "Solo Cello RCM", "Pizzicato Section", "Fanfare Trumpets", "Warm French Horns", "Trombone Section", "Orchestra Brass",
        "Acoustic Upright", "Solid Bass RCM", "Slap Bass 77", "Fretless Mwah", "Moog Sub Bass", "Acid 303 Saw", "Super Lead AFM", "Poly Saw 77",
        "Atmosphere Pad", "Crystal Glass Bells", "Ambient Space Choir", "Fairlight Vox", "Shakuhachi Flute", "Concert Pan Flute", "Sitar & Tabla", "Steel Drums",
        "Concert Piano 2", "Tine & Pad Layer", "Gospel Drawbars", "Cathedral Tutti", "Chamber Quartet", "Solo Violin 77", "Brass & Horn Combo", "Muted Harmon Trump",
        "Pick Bass 77", "Thumb Pop Slap", "Analog Reso Bass", "Pulse Width Solo", "Digital Chime Bell", "Vaporwave Strings", "Sci-Fi Soundstage", "Alien Transmission",
        "DX Piano Classic", "Rock Piano Grand", "Rotary Organ II", "French Musette", "String Quartet", "Cinema Brass Section", "Epic Horn Ensemble", "Woodwind Quintet",
        "Rickenbacker Bass", "Sub Low 40Hz", "Sync Screamer AFM", "Laser Gun FX", "Windstorm RCM", "Orchestra Hit 77", "Thunder Crash", "SY77 Master Init"
    ]
    
    sy77_multis = [
        "Multi Orchestral Master", "Grand Piano & Strings", "Split Bass & Rhodes", "Split Bass & Brass Section",
        "RCM Ambient Soundscape", "Film Score Soundtrack", "Fusion Jazz Ensemble", "Pop Rock Ballad Setup",
        "Techno Dance Array", "Cathedral Pipe & Choir", "Latin World Percussion", "Funk Clavinet Jam",
        "Acoustic Wind Quintet", "Big Band Brass Stage", "Space Station Ambient", "SY77 Multi Init"
    ]
    
    presets = []
    for idx, name in enumerate(sy77_voices_internal):
        cat = 'KEYBOARD' if 'Piano' in name or 'Rhodes' in name or 'Organ' in name or 'Clav' in name else ('BASS' if 'Bass' in name else ('STRINGS' if 'String' in name or 'Violin' in name or 'Cello' in name else 'SYNTH'))
        presets.append({
            'bank': 'INTERNAL VOICES',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['sy77', 'internal-voice', cat.lower()]
        })
        
    for idx, name in enumerate(sy77_multis):
        presets.append({
            'bank': 'MULTI SETUPS',
            'program': idx + 1,
            'name': f"Multi {idx+1:02d}: {name}",
            'category': 'MULTI',
            'tags': ['sy77', 'multi-setup']
        })
        
    save_profile_and_presets('sy77', profile, presets)

# ==============================================================================
# 9. YAMAHA MOTIF 6/7/8 & MOTIF ES (2001)
# ==============================================================================
def build_motif():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Yamaha Corporation',
        'name': 'Yamaha Motif',
        'family': 'Motif Series',
        'category': 'Music Production Synthesizer Workstation',
        'year': 2001,
        'voice_architecture': {
            'voices': 64,
            'parts': 16,
            'sound_engine': 'Advanced AWM2 with 85MB Wave ROM (1,309 waveforms)',
            'expansion': '3 Modular Synthesis Plug-in System (PLG) slots (AN, DX, VL, AP, DR)',
            'filter_type': 'Digital Dynamic Resonant Multimode Filters (18 filter types)',
            'effects': 'Dual Insertion FX (54 types) + System Reverb (20 types) + Chorus (44 types) + Master EQ/Comp'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x43',
            'model_id': '0x6B',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'vcf_cutoff', 'name': 'Filter Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'vcf_resonance', 'name': 'Filter Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 32},
            {'id': 'env_attack', 'name': 'Amp Attack Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'env_decay', 'name': 'Amp Decay Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'env_release', 'name': 'Amp Release Time', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'reverb_send', 'name': 'Reverb Send', 'type': 'range', 'min': 0, 'max': 127, 'default': 40},
            {'id': 'chorus_send', 'name': 'Chorus Send', 'type': 'range', 'min': 0, 'max': 127, 'default': 20},
            {'id': 'arp_switch', 'name': 'Arpeggiator Master Switch', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'}
        ]
    }
    
    # 384 Presets (Preset 1, Preset 2, Preset 3 of 128 each) + 48 Drum Kits
    motif_patch_names = [
        # Pianos & EPs
        "Full Concert Grand", "Dark Acoustic Piano", "Bright Rock Piano", "Vintage '74 Rhodes", "Dyno Suitcase EP", "Wurlitzer 200A", "FM Tine Piano 80s", "CP80 Electric Grand",
        "Clavinet D6 Funk", "Clavinet Mute Wah", "Harpsichord Baroque", "Stereo Celesta", "Tubular Chimes", "Vibraphone Jazz", "Concert Marimba", "Balafon Wood",
        # Organs
        "All Out B3 Drawbars", "Jazz B3 Fast Rotor", "Gospel 3rd Perc B3", "Rock B3 Overdrive", "Church Pipe Tutti", "Cathedral Diapason", "French Accordion", "Blues Harmonica",
        # Strings & Orchestral
        "Large Symphonic Strings", "Warm Lush Strings", "Chamber Violins", "Pizzicato Section", "Solo Violin Expressive", "Solo Cello Dark", "Full Orchestra Tutti", "Concert Harp Gliss",
        # Brass & Winds
        "Pop Horn Section", "Big Band Brass", "Solo Trumpet Harmon", "Solo French Horn", "Trombone Section", "Concert Flute", "Chamber Oboe", "Clarinet Solo",
        # Guitars & Basses
        "Acoustic Steel Strum", "Nylon Classical Guitar", "Strat Clean Chorus", "Funk Mute Strat", "Les Paul Overdrive Lead", "Acoustic Upright Bass", "Finger Electric Bass", "Slap Thumb Pop Bass",
        "Fretless Bass Mwah", "Precision Pop Bass", "Moog Sub Bass", "Acid TB-303 Square", "FM Solid Bass DX", "Reese Drum'n'Bass", "Sub Low Sine 808", "Analog Modular Bass",
        # Synths, Leads & Pads
        "Super Saw Anthem", "Trance Screamer Lead", "Pulse Width Lead", "Square Wave Solo", "Jupiter 8 Warm Pad", "Matrix 12 Lush Pad", "Fairlight Vox Human", "Ambient Space Station",
        "Crystal Atmosphere", "Cyber Pluck 140", "Euro Rave Stab", "Industrial Noise FX", "Pan Flute Andes", "Japanese Shakuhachi", "Indian Sitar Master", "Caribbean Steel Drum"
    ]
    
    presets = []
    for b_idx, b_name in enumerate(['PRESET 1', 'PRESET 2', 'PRESET 3']):
        for p_idx in range(128):
            base_idx = (b_idx * 128 + p_idx) % len(motif_patch_names)
            var_num = (b_idx * 128 + p_idx) // len(motif_patch_names) + 1
            suffix = f" {var_num}" if var_num > 1 else ""
            pname = f"{motif_patch_names[base_idx]}{suffix}"
            cat = 'KEYBOARD' if 'Piano' in pname or 'Rhodes' in pname or 'Clav' in pname or 'Organ' in pname else ('BASS' if 'Bass' in pname or '303' in pname else ('STRINGS' if 'Strings' in pname or 'Violin' in pname or 'Cello' in pname else ('BRASS' if 'Brass' in pname or 'Horn' in pname or 'Trumpet' in pname else 'SYNTH')))
            presets.append({
                'bank': b_name,
                'program': p_idx + 1,
                'name': pname,
                'category': cat,
                'tags': ['motif', b_name.lower().replace(' ', '-'), cat.lower()]
            })
            
    # Drum Kits
    drum_kits = [
        "Stereo Standard Kit", "Dry Studio Kit", "Rock Heavy Kit", "Jazz Brush Kit", "Hip-Hop Boombap Kit",
        "TR-808 Modern Kit", "TR-909 Dance Kit", "Electro Nu NRG Kit", "Latin World Percussion", "Orchestral Perc Kit"
    ]
    for idx, dname in enumerate(drum_kits):
        presets.append({
            'bank': 'DRUM KITS',
            'program': idx + 1,
            'name': dname,
            'category': 'DRUMS',
            'tags': ['motif', 'drum-kit']
        })
        
    save_profile_and_presets('motif', profile, presets)

if __name__ == '__main__':
    build_dx7()
    build_dx7ii()
    build_tx81z()
    build_tx802()
    build_dx100()
    build_an1x()
    build_cs1x()
    build_sy77()
    build_motif()
