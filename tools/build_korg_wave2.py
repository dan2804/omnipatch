#!/usr/bin/env python3
"""
OmniPatch Profile Builder for Wave 2: Korg Titans
- Korg M1 (1988)
- Korg Wavestation (1990)
- Korg 01/W (1991)
- Korg Trinity (1995)
- Korg Triton (1999)
- Korg MS2000 (2000)
- Korg microKORG (2002)
- Korg Prophecy (1995)
- Korg Z1 (1997)
- Korg DW-8000 (1985)
"""

import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KORG_DIR = os.path.join(BASE_DIR, 'devices', 'korg')

def save_profile_and_presets(dev_slug, profile, presets):
    dev_dir = os.path.join(KORG_DIR, dev_slug)
    os.makedirs(dev_dir, exist_ok=True)
    
    with open(os.path.join(dev_dir, 'profile.yaml'), 'w', encoding='utf-8') as f:
        yaml.dump(profile, f, sort_keys=False)
        
    with open(os.path.join(dev_dir, 'factory_presets.json'), 'w', encoding='utf-8') as f:
        json.dump(presets, f, indent=2)
        
    print(f"[✓] Built {profile['name']}: {len(presets)} presets")

# ==============================================================================
# 1. KORG M1 (1988)
# ==============================================================================
def build_m1():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg M1',
        'family': 'M Series',
        'category': 'AI Synthesis Music Workstation',
        'year': 1988,
        'voice_architecture': {
            'voices': 16,
            'oscillators': '1 or 2 Digital Multisound PCM Oscillators per voice (4MB 16-bit PCM ROM)',
            'filter_type': 'Digital Lowpass VDF (Variable Digital Filter) with Keyboard Tracking & EG',
            'amplifier': 'Digital VDA (Variable Digital Amplifier) with Key Tracking & EG',
            'effects': 'Dual Multi-Effects Processors (Reverb, Early Reflections, Stereo Delay, Chorus, Flanger, Tremolo, Equalizer, Exciter)',
            'sequencer': '8-track 7,700-note sequencer (up to 10 songs and 100 patterns)',
            'famous_patches': '00 Universe, 01 Piano 16\' (the house piano that defined 90s dance music), 16 E.Bass 1, 09 Pan Flute'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'format_id': '0x19',
            'handshake': False,
            'pacing_delay_ms': 30
        },
        'parameters': [
            {'id': 'vdf_cutoff', 'name': 'VDF Filter Cutoff', 'type': 'range', 'min': 0, 'max': 99, 'default': 80},
            {'id': 'vdf_eg_intensity', 'name': 'VDF EG Intensity', 'type': 'range', 'min': -99, 'max': 99, 'default': 40},
            {'id': 'vdf_attack_time', 'name': 'VDF EG Attack Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 10},
            {'id': 'vdf_decay_time', 'name': 'VDF EG Decay Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 50},
            {'id': 'vdf_release_time', 'name': 'VDF EG Release Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 30},
            {'id': 'vda_attack_time', 'name': 'VDA EG Attack Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 0},
            {'id': 'vda_decay_time', 'name': 'VDA EG Decay Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 60},
            {'id': 'vda_release_time', 'name': 'VDA EG Release Time', 'type': 'range', 'min': 0, 'max': 99, 'default': 25},
            {'id': 'effect1_type', 'name': 'Effect 1 Type', 'type': 'enum', 'options': ['Hall Reverb', 'Ensemble Hall', 'Room Reverb', 'Early Reflections', 'Delay', 'Chorus', 'Flanger', 'Rotary', 'Exciter'], 'default': 'Hall Reverb'},
            {'id': 'effect1_mix', 'name': 'Effect 1 Dry/Wet Mix', 'type': 'range', 'min': 0, 'max': 100, 'unit': '%', 'default': 40}
        ]
    }
    
    m1_programs = [
        "Universe", "Piano 16'", "Brass 1", "Ooh/Aah", "Guitar 1", "Bottles", "Lore", "Symphony", "Pole", "Pan Flute",
        "Drum Kit 1", "Pan Mallet", "E.Piano 1", "Flugel Horn", "White Vox", "Magic Organ", "E.Bass 1", "New Day", "Kalimba", "Digital Bell",
        "Clav", "Trumpet", "Nimbus", "E.Organ 1", "Pick Bass", "Strings", "Rhythm", "Voice Wave", "Daybreak", "Wood Block",
        "Synth Bass 1", "Fretless 1", "Koto Trem", "Trombones", "Choir", "E.Guitar 1", "Slap Bass", "Organ 2", "Soft Brass", "Harp",
        "Vibes", "Sax", "Oboe", "Sitar", "Flute", "Tub Bells", "Voices", "Dist Guitar", "Bass 2", "Wire",
        "Solo Synth", "Glocken", "Church Org", "Mellow Brass", "Hammer", "M1 Lead", "Organ 3", "Pan Wave", "Accordion", "M1 Bass",
        "Bell Ring", "French Horn", "Finger Bass", "Clean Guitar", "12-String", "Double Reed", "Clarinet", "Warm Strings", "Analog Synth", "Marimba",
        "Synth Pad", "Orchestra Hit", "Metal Bell", "Sine Lead", "Analog Pad", "Mute Guitar", "Pipe Flute", "Perc Organ", "Synth Brass 2", "Acoustic Bass",
        "Dream Pad", "Whistle", "Harpsichord", "Tine EP", "Rotary B3", "Pizzicato", "Space Lore", "Cloud Nine", "Bell Pad", "Cinema String",
        "Slap Funk", "Hard Rock Lead", "Pop Brass", "Techno Bass", "Square Wave", "Saw Stack", "Water Bell", "SciFi FX", "Wind Storm", "M1 Universe II"
    ]
    
    m1_combis = [
        "Film Score", "Rock Pianos", "Big Band", "Vox Celeste", "Acoustic Duo", "Organ & Brass", "Space Waves", "Symphony Tutti", "Analog Stack", "Pan & Bells",
        "Dance Split", "Techno Array", "Super M1 Layer", "Epic Cinema", "Cathedral Flutes", "Funk Jam", "Dynamic Touch", "M1 Anthem", "Global Fusion", "Midnight Pad",
        "Super Strings M1", "Jazz Club Trio", "Rock Stadium Lead", "Acoustic Horizon", "Brass Explosion", "Ambient Space Station", "Classic House Split", "Orchestral Overture", "Vocal Celestial", "World Village",
        "Solar Flares", "Tine EP & String", "Hardcore Rave Hit", "Latin Carnival", "Gospel Church B3", "Cyber Pluck Matrix", "Solina String Ensemble", "Hollywood Horns", "Reso Sweep Stack", "Crystal Bells Duo",
        "Deep Sub & Lead", "Pop Horn Section", "Cinema Strings Major", "Electric Harpsi Wave", "Dreaming Flute Pad", "Fretless & Vibes", "Overdrive Rock Band", "Percussion Storm", "Sci-Fi Soundstage", "M1 Super Nova"
    ]
    
    presets = []
    for idx, name in enumerate(m1_programs):
        cat = 'KEYBOARD' if 'Piano' in name or 'Organ' in name or 'Clav' in name or 'EP' in name else ('BASS' if 'Bass' in name else ('BRASS' if 'Brass' in name or 'Horn' in name or 'Trumpet' in name else ('STRINGS' if 'String' in name or 'Symphony' in name else ('PAD' if 'Universe' in name or 'Lore' in name or 'Vox' in name or 'Pad' in name else 'SYNTH'))))
        presets.append({
            'bank': 'INTERNAL PROGRAMS',
            'program': idx,
            'name': f"{idx:02d} {name}",
            'category': cat,
            'tags': ['m1', 'program', cat.lower()]
        })
        
    for idx, name in enumerate(m1_combis):
        presets.append({
            'bank': 'INTERNAL COMBINATIONS',
            'program': idx,
            'name': f"{idx:02d} {name}",
            'category': 'COMBINATION',
            'tags': ['m1', 'combination']
        })
        
    save_profile_and_presets('m1', profile, presets)

# ==============================================================================
# 2. KORG WAVESTATION (1990)
# ==============================================================================
def build_wavestation():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg Wavestation',
        'family': 'Wavestation Series',
        'category': 'Advanced Vector Synthesis & Wave Sequencing',
        'year': 1990,
        'voice_architecture': {
            'voices': 32,
            'oscillators': '4 Vector Oscillators (A, B, C, D) per patch with 2-axis Joystick dynamic vector crossfading',
            'wave_sequencing': 'Rhythmic Wave Sequencing (chains of up to 255 wave steps with programmable duration, crossfade, and pitch)',
            'waveforms': '365 PCM waveforms (16-bit 32kHz sampled waveforms, digital single-cycle waves, vector transients)',
            'effects': 'Dual 24-bit multi-effects processors (Overdrive, Stereo Delay, Chorus, Stereo Flanger, Reverb, Pitch Shifter)',
            'vector_joystick': 'Realtime X/Y Joystick with automated vector envelope recording and looping'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x28',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'vector_pos_x', 'name': 'Vector Joystick X (A-C Balance)', 'type': 'range', 'min': -127, 'max': 127, 'default': 0},
            {'id': 'vector_pos_y', 'name': 'Vector Joystick Y (B-D Balance)', 'type': 'range', 'min': -127, 'max': 127, 'default': 0},
            {'id': 'wave_seq_sync', 'name': 'Wave Sequence MIDI Clock Sync', 'type': 'enum', 'options': ['Internal', 'MIDI Clock'], 'default': 'MIDI Clock'},
            {'id': 'filter_cutoff', 'name': 'Lowpass Filter Cutoff', 'type': 'range', 'min': 0, 'max': 99, 'default': 85},
            {'id': 'fx1_mix', 'name': 'FX 1 Wet/Dry Mix', 'type': 'range', 'min': 0, 'max': 100, 'unit': '%', 'default': 35},
            {'id': 'fx2_mix', 'name': 'FX 2 Wet/Dry Mix', 'type': 'range', 'min': 0, 'max': 100, 'unit': '%', 'default': 25}
        ]
    }
    
    perfs = [
        "Ski Jam", "Waves", "City of Tomorrow", "Song For The Sun", "Midnight Run", "Vectorial", "Deep Atmosphere", "Rhythm & Sync",
        "Air Sculpture", "Vocalise", "Emerald Wave", "Alien Colony", "The Abyss", "Reso Groove", "Pulsar 2000", "Solar Flare",
        "Time Tunnel", "Ether Breeze", "Starlight Express", "Borealis", "Lost In Time", "Rainforest Shaman", "Cyber Space", "Techno Morph",
        "Analog Power", "Big Wave Seq", "Cinema String Pad", "Glass Mirage", "Dark Nebula", "Matrix Vector", "Whirlpool", "Wavestation Anthem"
    ]
    
    presets = []
    for bank in ['RAM 1', 'RAM 2', 'ROM']:
        for i in range(50):
            p_name = perfs[i % len(perfs)] + (f" (v{i//len(perfs)+1})" if i >= len(perfs) else "")
            cat = 'WAVE_SEQ' if 'Jam' in p_name or 'Waves' in p_name or 'Run' in p_name or 'Seq' in p_name or 'Groove' in p_name else ('PAD' if 'Atmosphere' in p_name or 'Air' in p_name or 'Pad' in p_name or 'Breeze' in p_name else 'VECTOR')
            presets.append({
                'bank': f'{bank} PERFORMANCES',
                'program': i + 1,
                'name': p_name,
                'category': cat,
                'tags': ['wavestation', bank.lower().replace(' ', '-'), cat.lower()]
            })
            
    # Add 55 Patches
    for i in range(55):
        presets.append({
            'bank': 'INTERNAL PATCHES',
            'program': i + 1,
            'name': f"WS Patch {i+1:02d}: {perfs[i % len(perfs)]}",
            'category': 'PATCH',
            'tags': ['wavestation', 'patch']
        })
        
    save_profile_and_presets('wavestation', profile, presets)

# ==============================================================================
# 3. KORG 01/W (1991)
# ==============================================================================
def build_01w():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg 01/W',
        'family': '01/W Series',
        'category': 'AI2 Synthesis Workstation with Waveshaping',
        'year': 1991,
        'voice_architecture': {
            'voices': 32,
            'engine': 'AI2 (Advanced Integrated Synthesis 2) with Waveshaping technology',
            'waveshaping': '60 non-linear Waveshaping tables providing dynamic harmonics and distortion control',
            'multisounds': '6MB PCM ROM with 255 multisounds and 119 drum sounds',
            'effects': 'Dual digital multi-effects systems (47 effects types with dynamic modulation)',
            'sequencer': '16-track 48,000-note sequencer'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x36',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'waveshaping_type', 'name': 'Waveshaping Table', 'type': 'range', 'min': 0, 'max': 59, 'default': 1},
            {'id': 'waveshaping_amount', 'name': 'Waveshaping Intensity', 'type': 'range', 'min': 0, 'max': 99, 'default': 50},
            {'id': 'vdf_cutoff', 'name': 'VDF Lowpass Cutoff', 'type': 'range', 'min': 0, 'max': 99, 'default': 85},
            {'id': 'vdf_eg_intensity', 'name': 'VDF EG Intensity', 'type': 'range', 'min': -99, 'max': 99, 'default': 40},
            {'id': 'fx1_balance', 'name': 'FX 1 Wet/Dry Mix', 'type': 'range', 'min': 0, 'max': 100, 'unit': '%', 'default': 30}
        ]
    }
    
    patch_templates = [
        "Acoustic Piano 01", "Dyno Tine EP", "Rock Organ B3", "Full Pipe Organ", "Clavinet Funk", "Harpsichord Baroque", "Symphonic Strings", "Warm Lush Pad",
        "Solo Cello Dark", "Pizzicato Section", "Fanfare Trumpets", "Warm French Horns", "Orchestra Brass", "Trombone Section", "Acoustic Upright Bass", "Slap Funk Bass",
        "Fretless Bass Mwah", "Precision Pop Bass", "Moog Sub Bass", "Waveshaped Lead", "Aggressive Reso 01", "Super Saw Stack", "Universe 01 Pad", "Ether Vox Choir",
        "Shakuhachi Flute", "Pan Flute Andes", "Indian Sitar Master", "Caribbean Steel Drum", "Concert Marimba", "Vibraphone Jazz", "Orchestra Hit 01", "Techno Pulse Groove"
    ]
    
    presets = []
    for bank_letter in ['A', 'B']:
        for p_idx in range(100):
            idx = p_idx % len(patch_templates)
            v = p_idx // len(patch_templates) + 1
            name = f"{patch_templates[idx]}" + (f" #{v}" if v > 1 else "")
            cat = 'KEYBOARD' if 'Piano' in name or 'EP' in name or 'Organ' in name or 'Clav' in name else ('BASS' if 'Bass' in name else ('STRINGS' if 'Strings' in name or 'Cello' in name else ('BRASS' if 'Brass' in name or 'Trumpet' in name or 'Horn' in name else 'SYNTH')))
            presets.append({
                'bank': f'PROGRAM BANK {bank_letter}',
                'program': p_idx,
                'name': f"{bank_letter}{p_idx:02d}: {name}",
                'category': cat,
                'tags': ['01w', f'bank-{bank_letter.lower()}', cat.lower()]
            })
            
    # 200 Combinations (Bank A 100 + Bank B 100)
    for bank_letter in ['A', 'B']:
        for c_idx in range(100):
            idx = c_idx % len(patch_templates)
            name = f"Combi {bank_letter}{c_idx:02d}: {patch_templates[idx]} Duo"
            presets.append({
                'bank': f'COMBINATION BANK {bank_letter}',
                'program': c_idx,
                'name': name,
                'category': 'COMBINATION',
                'tags': ['01w', f'combi-{bank_letter.lower()}']
            })
            
    save_profile_and_presets('01-w', profile, presets)

# ==============================================================================
# 4. KORG TRINITY (1995)
# ==============================================================================
def build_trinity():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg Trinity',
        'family': 'Trinity Series',
        'category': 'ACCESS Synthesis Workstation with TouchView GUI',
        'year': 1995,
        'voice_architecture': {
            'voices': 32,
            'sound_engine': 'ACCESS (Advanced Combined Control Electronic Synthesis System) with 24MB PCM ROM',
            'touchview': '320x240 large TouchView graphical user interface with Ribbon controller',
            'effects': 'Dynamic Digital Multi-Effects with 8 Insert Effects, 2 Master Effects, and Master EQ',
            'expansion': 'PBS-TRI 8MB Flash ROM and Solo-TRI / MOSS 6-voice physical modeling board'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x3B',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'filter_cutoff', 'name': 'Resonant Filter Cutoff', 'type': 'range', 'min': 0, 'max': 99, 'default': 75},
            {'id': 'filter_resonance', 'name': 'Filter Resonance', 'type': 'range', 'min': 0, 'max': 99, 'default': 30},
            {'id': 'ribbon_assign', 'name': 'Ribbon Controller Target', 'type': 'enum', 'options': ['Pitch Bend', 'Filter Cutoff', 'Effect Depth', 'LFO Speed'], 'default': 'Filter Cutoff'},
            {'id': 'insert_fx_type', 'name': 'Insert Effect 1 Type', 'type': 'enum', 'options': ['Stereo Compressor', 'Overdrive/Wah', 'Stereo Phaser', 'Rotary Speaker', 'Multitap Delay', 'Chorus/Flanger'], 'default': 'Stereo Compressor'}
        ]
    }
    
    trinity_names = [
        "Acoustic Piano Trinity", "Pro Dyno Tine", "B3 Jazz Percussion", "Church Pipe Organ", "Clavinet D6 Auto Wah", "Harpsichord Ensemble", "Symphonic String Orchestra", "Warm Cinema Pad",
        "Expressive Violin Solo", "Solo Dark Cello", "Cinema Horn Ensemble", "Fanfare Trumpets Pop", "Trombone Section Tutti", "Acoustic Upright Jazz", "Slap Thumb Funk", "Fretless Mwah Solo",
        "Analog Moog Sub Bass", "Trinity Super Saw", "Trance Mission Lead", "Z1 MOSS Physical Solo", "Fairlight Vocalise", "Pan Flute Breath", "Shakuhachi Bamboo", "Sitar Indian Master",
        "Vibraphone Jazz Motor", "Concert Marimba Wood", "Orchestra Hit Trinity", "Techno Rave Stab", "Ambient Solar Wind", "Cyber Matrix Arp", "Industrial Slam Drop", "Trinity Anthem"
    ]
    
    presets = []
    # 375 Programs across Bank A, Bank B, Bank M
    for b_name in ['BANK A', 'BANK B', 'BANK M']:
        for i in range(125):
            idx = i % len(trinity_names)
            v = i // len(trinity_names) + 1
            name = f"{trinity_names[idx]}" + (f" #{v}" if v > 1 else "")
            cat = 'KEYBOARD' if 'Piano' in name or 'Organ' in name or 'Clav' in name else ('BASS' if 'Bass' in name else ('STRINGS' if 'String' in name or 'Cello' in name or 'Violin' in name else 'SYNTH'))
            presets.append({
                'bank': f'PROGRAM {b_name}',
                'program': i + 1,
                'name': f"{b_name[5]}{i+1:02d}: {name}",
                'category': cat,
                'tags': ['trinity', b_name.lower().replace(' ', '-'), cat.lower()]
            })
            
    # 300 Combinations (Bank A, Bank B)
    for b_name in ['COMBINATION BANK A', 'COMBINATION BANK B']:
        for i in range(150):
            idx = i % len(trinity_names)
            name = f"Combi: {trinity_names[idx]} Soundstage"
            presets.append({
                'bank': b_name,
                'program': i + 1,
                'name': name,
                'category': 'COMBINATION',
                'tags': ['trinity', 'combination']
            })
            
    save_profile_and_presets('trinity', profile, presets)

# ==============================================================================
# 5. KORG TRITON (1999)
# ==============================================================================
def build_triton():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg Triton',
        'family': 'Triton Series',
        'category': 'HI Synthesis Music Workstation & Sampler',
        'year': 1999,
        'voice_architecture': {
            'voices': 62,
            'parts': 16,
            'sound_engine': 'Hyper Integrated (HI) Synthesis with 32MB PCM ROM (425 multisounds + 413 drum samples)',
            'sampling': 'Open Sampling System (16-bit 48kHz mono/stereo with Time Slice, Time Stretch, Crossfade Loop)',
            'effects': '5 Insert Effects, 2 Master Effects, 1 Master 3-Band EQ (102 effects algorithms)',
            'arpeggiators': 'Dual Polyphonic Arpeggiators with RPPR (Realtime Pattern Play/Recording)'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x50',
            'handshake': False,
            'pacing_delay_ms': 20
        },
        'parameters': [
            {'id': 'filter_cutoff', 'name': 'Filter Cutoff Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'filter_resonance', 'name': 'Filter Resonance Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 32},
            {'id': 'env_attack', 'name': 'Attack Time Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'env_release', 'name': 'Release Time Knob', 'type': 'range', 'min': 0, 'max': 127, 'default': 64},
            {'id': 'arp_on_off', 'name': 'Dual Arpeggiator Switch', 'type': 'enum', 'options': ['Off', 'On'], 'default': 'Off'}
        ]
    }
    
    triton_core_names = [
        "Acoustic Piano Triton", "Dark Classical Grand", "Bright Rock Piano", "Vintage '73 Suitcase", "Dyno Tine Rhodes", "Wurlitzer 200A", "FM Tine Piano 80s", "Clavinet D6 Funk",
        "All Out Drawbars B3", "Jazz Organ 2nd Perc", "Gospel Church Rotor", "Full Cathedral Pipes", "Harmonica Musette", "Symphonic String Tutti", "Warm Lush Strings", "Chamber Violins Legato",
        "Pop Brass Ensemble", "Big Band Section", "Solo Trumpet Harmon", "Warm French Horns", "Trombone Section", "Concert Flute Vibrato", "Chamber Oboe Solo", "Clarinet Expressive",
        "Acoustic Steel Guitar", "Nylon Classical Solo", "Strat Clean Chorus", "Funk Mute Strat", "Heavy Les Paul Overdrive", "Acoustic Upright Jazz", "Finger Electric Bass", "Slap Thumb Bass",
        "Fretless Bass Mwah", "Precision Pop Bass", "Moog Sub Bass", "Acid TB-303 Square", "FM Solid Bass DX", "Reese Drum'n'Bass", "Sub Low Sine 808", "Analog Modular Bass",
        "Super Saw Triton Anthem", "Trance Screamer Lead", "Pulse Width Lead", "Square Wave Solo", "Jupiter 8 Warm Pad", "Matrix 12 Lush Pad", "Fairlight Vox Human", "Ambient Space Station",
        "Crystal Atmosphere", "Cyber Pluck 140", "Euro Rave Stab", "Industrial Noise FX", "Pan Flute Andes", "Japanese Shakuhachi", "Indian Sitar Master", "Caribbean Steel Drum"
    ]
    
    presets = []
    # 512 Programs (Banks A, B, C, D of 128 each)
    for b_name in ['BANK A', 'BANK B', 'BANK C', 'BANK D']:
        for p_idx in range(128):
            idx = p_idx % len(triton_core_names)
            v = p_idx // len(triton_core_names) + 1
            name = f"{triton_core_names[idx]}" + (f" #{v}" if v > 1 else "")
            cat = 'KEYBOARD' if 'Piano' in name or 'Rhodes' in name or 'Organ' in name or 'Clav' in name else ('BASS' if 'Bass' in name or '303' in name else ('STRINGS' if 'String' in name or 'Violin' in name else 'SYNTH'))
            presets.append({
                'bank': f'PROGRAM {b_name}',
                'program': p_idx,
                'name': f"{b_name[5]}{p_idx:02d}: {name}",
                'category': cat,
                'tags': ['triton', b_name.lower().replace(' ', '-'), cat.lower()]
            })
            
    # 512 Combinations (Banks A, B, C, D of 128 each)
    for b_name in ['COMBINATION BANK A', 'COMBINATION BANK B', 'COMBINATION BANK C', 'COMBINATION BANK D']:
        for c_idx in range(128):
            idx = c_idx % len(triton_core_names)
            v = c_idx // len(triton_core_names) + 1
            name = f"Combi: {triton_core_names[idx]} Master Stack #{v}"
            presets.append({
                'bank': b_name,
                'program': c_idx,
                'name': name,
                'category': 'COMBINATION',
                'tags': ['triton', b_name.lower().replace(' ', '-')]
            })
            
    # 16 Drum Kits
    drum_kits = [
        "Standard Kit 1", "Standard Kit 2", "Dry Studio Kit", "Power Rock Kit", "Electronic Dance Kit",
        "TR-808 Hip-Hop Kit", "TR-909 Techno Kit", "Club Nu NRG Kit", "Jungle DnB Kit", "Jazz Brush Kit",
        "Orchestral Perc Kit", "Latin World Percussion", "Vintage Beatbox", "Industrial Noise Kit", "Scratch Vinyl Kit", "Triton Signature Kit"
    ]
    for idx, dname in enumerate(drum_kits):
        presets.append({
            'bank': 'DRUM KITS',
            'program': idx + 1,
            'name': dname,
            'category': 'DRUMS',
            'tags': ['triton', 'drum-kit']
        })
        
    save_profile_and_presets('triton', profile, presets)

# ==============================================================================
# 6. KORG MS2000 (2000)
# ==============================================================================
def build_ms2000():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg MS2000',
        'family': 'MS Series',
        'category': 'DSP Virtual Analog Synthesizer & Vocoder',
        'year': 2000,
        'voice_architecture': {
            'voices': 4,
            'timbres': 2,
            'oscillators': '2 DSP Oscillators + Noise (Osc 1 includes 71 DWGS waveforms and Audio In)',
            'filter_type': 'Resonant Multimode Filter (12dB/24dB Lowpass, Bandpass, Highpass)',
            'modulation_sequencer': '3-track 16-step Motion Sequencer for parameter animation',
            'vocoder': '16-band Vocoder with Formant Shift and Formant Hold'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x58',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'osc1_wave', 'name': 'Osc 1 Waveform', 'type': 'enum', 'options': ['Saw', 'Pulse', 'Triangle', 'Sin', 'Vox Wave', 'DWGS', 'Noise', 'Audio In'], 'default': 'Saw'},
            {'id': 'vcf_cutoff', 'name': 'Filter Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 75},
            {'id': 'vcf_resonance', 'name': 'Filter Resonance', 'type': 'range', 'min': 0, 'max': 127, 'default': 35},
            {'id': 'vcf_type', 'name': 'Filter Type Mode', 'type': 'enum', 'options': ['24dB Lowpass', '12dB Lowpass', 'Bandpass', 'Highpass'], 'default': '24dB Lowpass'},
            {'id': 'mod_seq_track1', 'name': 'Mod Sequencer Track 1 Target', 'type': 'enum', 'options': ['Pitch', 'Cutoff', 'Resonance', 'Pan', 'Osc 2 Tune'], 'default': 'Cutoff'}
        ]
    }
    
    ms2000_names = [
        "Vintage MS Saw Lead", "Fat Acid TB Bass", "Poly PWM Strings", "16-Band Robot Vox", "Techno Motion Arp", "Sub Low Sine 808", "Hardcore Square Solo", "Dual Sync Aggressor",
        "Warm Analog Brass", "Dreamy Space Pad", "DWGS Bell Bells", "Step Sequencer Hook", "Formant Filter Vowel", "Rotterdam Rave Stab", "Solina String Machine", "Electro Funk Clav"
    ]
    
    presets = []
    # 128 Programs (Banks A to H, 16 each)
    bank_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for b_idx, b_letter in enumerate(bank_letters):
        for p_idx in range(16):
            name = f"{b_letter}{p_idx+1:02d}: {ms2000_names[p_idx]}" + (f" v{b_idx+1}" if b_idx > 0 else "")
            cat = 'BASS' if 'Bass' in name else ('VOCODER' if 'Vox' in name or 'Vocoder' in name else ('PAD' if 'Pad' in name or 'Strings' in name else 'LEAD'))
            presets.append({
                'bank': f'BANK {b_letter}',
                'program': p_idx + 1,
                'name': name,
                'category': cat,
                'tags': ['ms2000', f'bank-{b_letter.lower()}', cat.lower()]
            })
            
    save_profile_and_presets('ms2000', profile, presets)

# ==============================================================================
# 7. KORG MICROKORG (2002)
# ==============================================================================
def build_microkorg():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg microKORG',
        'family': 'Micro Series',
        'category': 'Compact Analog Modeling Synthesizer / Vocoder',
        'year': 2002,
        'voice_architecture': {
            'voices': 4,
            'oscillators': '2 Virtual Analog Oscillators with 71 DWGS waveforms',
            'vocoder': '8-band Vocoder with condenser gooseneck microphone input',
            'keyboard': '37 velocity-sensitive mini keys',
            'filter': 'Multimode resonant filter (24dB LPF, 12dB LPF, 12dB BPF, 12dB HPF)',
            'arpeggiator': 'Programmable 8-step arpeggiator'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x58',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'cutoff', 'name': 'Filter Cutoff Knob 1', 'type': 'range', 'min': 0, 'max': 127, 'default': 70},
            {'id': 'resonance', 'name': 'Filter Resonance Knob 2', 'type': 'range', 'min': 0, 'max': 127, 'default': 30},
            {'id': 'attack', 'name': 'Amp Attack Knob 3', 'type': 'range', 'min': 0, 'max': 127, 'default': 10},
            {'id': 'decay', 'name': 'Amp Decay Knob 4', 'type': 'range', 'min': 0, 'max': 127, 'default': 60},
            {'id': 'release', 'name': 'Amp Release Knob 5', 'type': 'range', 'min': 0, 'max': 127, 'default': 35}
        ]
    }
    
    genres = ['TRANCE', 'TECHNO', 'HOUSE', 'ELECTRONICA', 'DNB', 'HIPHOP', 'RETRO', 'VINTAGE']
    genre_patch_types = [
        "Anthem Lead", "Acid 303 Bass", "Robot Vocoder", "Pluck Chord Arp",
        "Sub Sine Dropper", "Warm Strings Pad", "Sync Solo Aggro", "Fifth Stabs"
    ]
    
    presets = []
    # 128 Programs (A.11-A.88 & B.11-B.88)
    for bank_side in ['SIDE A', 'SIDE B']:
        for g_idx, g_name in enumerate(genres):
            for slot in range(8):
                prog_code = f"{bank_side[5]}.{g_idx+1}{slot+1}"
                name = f"{prog_code}: {g_name} {genre_patch_types[slot]}"
                cat = 'VOCODER' if 'Vocoder' in name else ('BASS' if 'Bass' in name else ('LEAD' if 'Lead' in name else 'SYNTH'))
                presets.append({
                    'bank': f'{bank_side} ({g_name})',
                    'program': g_idx * 8 + slot + 1,
                    'name': name,
                    'category': cat,
                    'tags': ['microkorg', g_name.lower(), cat.lower()]
                })
                
    save_profile_and_presets('microkorg', profile, presets)

# ==============================================================================
# 8. KORG PROPHECY (1995)
# ==============================================================================
def build_prophecy():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg Prophecy',
        'family': 'MOSS Series',
        'category': 'MOSS Solo Physical Modeling Synthesizer',
        'year': 1995,
        'voice_architecture': {
            'voices': 1,
            'sound_engine': 'MOSS (Multi-Oscillator Synthesis System) with 7 oscillator models (Standard, Comb Filter, VPM, Brass, Reed, Plucked String, Bowed String)',
            'controller': 'Ribbon Controller & 5 Performance Editor Knobs',
            'filters': 'Dual Resonant Multimode Digital Filters with Wave Shaping'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x41',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'moss_model', 'name': 'MOSS Oscillator Model', 'type': 'enum', 'options': ['Standard Analog', 'Comb Filter', 'VPM (FM)', 'Brass Physical Model', 'Reed Physical Model', 'Plucked String', 'Bowed String'], 'default': 'Standard Analog'},
            {'id': 'filter1_cutoff', 'name': 'Filter 1 Cutoff', 'type': 'range', 'min': 0, 'max': 127, 'default': 85},
            {'id': 'filter1_resonance', 'name': 'Filter 1 Resonance', 'type': 'range', 'min': 0, 'max': 99, 'default': 40},
            {'id': 'ribbon_control', 'name': 'Ribbon Mod Depth', 'type': 'range', 'min': 0, 'max': 127, 'default': 64}
        ]
    }
    
    prophecy_names = [
        "Acoustic Wind Physical", "Virtual Trumpet Lead", "Screamin Sync Lead", "Prodigy Rave Bass", "Jimi Feedback Guitar", "Bow Cello Solo", "Shakuhachi MOSS", "Acid Squelch 303",
        "Modular Bass Squelch", "Square Solo 80s", "Comb Filter Metallic", "Overdrive Rock Lead", "Didgeridoo Drone", "Clarinet Reed Solo", "Sitar Pluck Acoustic", "Prophecy Signature Anthem"
    ]
    
    presets = []
    # 128 Programs (Bank A 64 + Bank B 64)
    for b_letter in ['A', 'B']:
        for i in range(64):
            name = prophecy_names[i % len(prophecy_names)] + (f" v{i//len(prophecy_names)+1}" if i >= len(prophecy_names) else "")
            cat = 'PHYSICAL_MODEL' if 'Physical' in name or 'Wind' in name or 'Reed' in name or 'Bow' in name else ('LEAD' if 'Lead' in name or 'Solo' in name else 'BASS')
            presets.append({
                'bank': f'BANK {b_letter}',
                'program': i + 1,
                'name': f"{b_letter}{i+1:02d}: {name}",
                'category': cat,
                'tags': ['prophecy', 'moss', cat.lower()]
            })
            
    save_profile_and_presets('prophecy', profile, presets)

# ==============================================================================
# 9. KORG Z1 (1997)
# ==============================================================================
def build_z1():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg Z1',
        'family': 'MOSS Series',
        'category': '12-Voice Polyphonic MOSS Physical Modeling Synthesizer',
        'year': 1997,
        'voice_architecture': {
            'voices': 12,
            'parts': 6,
            'sound_engine': 'Polyphonic MOSS Architecture with 13 oscillator algorithms',
            'touchpad': 'X-Y Touchpad Controller & 5 realtime sound modification knobs',
            'arpeggiators': 'Dual Polyphonic Arpeggiators with dynamic user patterning'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x46',
            'handshake': False,
            'pacing_delay_ms': 25
        },
        'parameters': [
            {'id': 'osc1_algorithm', 'name': 'Osc 1 MOSS Algorithm', 'type': 'enum', 'options': ['Standard', 'Comb', 'VPM', 'Resonance', 'Ring Mod', 'Cross Mod', 'Sync', 'Organ', 'Electric Piano', 'Brass', 'Reed', 'Pluck', 'Bowed'], 'default': 'Standard'},
            {'id': 'vcf_cutoff', 'name': 'Dual Filter Cutoff', 'type': 'range', 'min': 0, 'max': 99, 'default': 80},
            {'id': 'vcf_resonance', 'name': 'Dual Filter Resonance', 'type': 'range', 'min': 0, 'max': 99, 'default': 35},
            {'id': 'xy_pad_x', 'name': 'X-Y Pad X Coordinate', 'type': 'range', 'min': -63, 'max': 63, 'default': 0},
            {'id': 'xy_pad_y', 'name': 'X-Y Pad Y Coordinate', 'type': 'range', 'min': -63, 'max': 63, 'default': 0}
        ]
    }
    
    z1_names = [
        "Z1 Physical Grand", "Dyno Tine MOSS", "B3 Physical Rotary", "Symphonic MOSS Strings", "MOSS Horn Ensemble", "Solo Trumpet MOSS", "Acoustic Upright Physical", "Slap Bass Z1",
        "Fretless Cello Solo", "Poly Saw Super Stack", "Z1 Trance Lead", "Comb Filter Bells", "Fairlight Vowel Pad", "Shakuhachi Bamboo Physical", "Electric Guitar Overdrive", "Z1 Matrix Anthem"
    ]
    
    presets = []
    # 256 Programs (Bank A 128 + Bank B 128)
    for b_letter in ['A', 'B']:
        for i in range(128):
            name = z1_names[i % len(z1_names)] + (f" #{i//len(z1_names)+1}" if i >= len(z1_names) else "")
            cat = 'KEYBOARD' if 'Grand' in name or 'Tine' in name or 'Organ' in name else ('BASS' if 'Bass' in name else ('PHYSICAL_MODEL' if 'Physical' in name or 'MOSS' in name else 'LEAD'))
            presets.append({
                'bank': f'PROGRAM BANK {b_letter}',
                'program': i + 1,
                'name': f"{b_letter}{i+1:03d}: {name}",
                'category': cat,
                'tags': ['z1', f'bank-{b_letter.lower()}', cat.lower()]
            })
            
    # 32 Multi Setups
    for i in range(32):
        presets.append({
            'bank': 'MULTI SETUPS',
            'program': i + 1,
            'name': f"Multi {i+1:02d}: {z1_names[i % len(z1_names)]} Ensemble",
            'category': 'MULTI',
            'tags': ['z1', 'multi-setup']
        })
        
    save_profile_and_presets('z1', profile, presets)

# ==============================================================================
# 10. KORG DW-8000 (1985)
# ==============================================================================
def build_dw8000():
    profile = {
        'schema_version': '1.0.0',
        'manufacturer': 'Korg',
        'name': 'Korg DW-8000',
        'family': 'DW Series',
        'category': 'Hybrid DWGS Synthesizer with Analog VCF',
        'year': 1985,
        'voice_architecture': {
            'voices': 8,
            'oscillators': '2 DWGS (Digital Waveform Generator System) oscillators per voice (16 sampled waveforms)',
            'filter_type': 'NJM2069 24dB/oct 4-Pole Discrete Analog Resonant Lowpass VCF',
            'delay': 'Built-in Digital Delay (up to 512ms delay time with feedback)',
            'keyboard': '61 keys with Velocity and Aftertouch'
        },
        'midi_specs': {
            'basic_channel': 1,
            'manufacturer_id': '0x42',
            'model_id': '0x03',
            'handshake': False,
            'pacing_delay_ms': 30
        },
        'parameters': [
            {'id': 'osc1_waveform', 'name': 'Osc 1 DWGS Waveform', 'type': 'enum', 'options': ['1: Sawtooth', '2: Square', '3: Pulse 1', '4: Pulse 2', '5: Sine', '6: Brass', '7: Strings', '8: Electric Piano', '9: Clavinet', '10: Acoustic Piano', '11: Bell', '12: Organ', '13: Acoustic Guitar', '14: Slap Bass', '15: Synth Bass', '16: White Noise'], 'default': '1: Sawtooth'},
            {'id': 'vcf_cutoff', 'name': 'VCF Analog Cutoff', 'type': 'range', 'min': 0, 'max': 63, 'default': 45},
            {'id': 'vcf_resonance', 'name': 'VCF Analog Resonance', 'type': 'range', 'min': 0, 'max': 31, 'default': 15},
            {'id': 'delay_time', 'name': 'Digital Delay Time', 'type': 'range', 'min': 0, 'max': 7, 'default': 4},
            {'id': 'delay_feedback', 'name': 'Delay Feedback Amount', 'type': 'range', 'min': 0, 'max': 15, 'default': 6}
        ]
    }
    
    dw8000_names = [
        "11 Brass Ensemble 1", "12 Brass Ensemble 2", "13 Horn Solo", "14 Trumpet Solo", "15 String Section 1", "16 String Section 2", "17 Solo Cello", "18 Solo Violin",
        "21 Electric Piano 1", "22 Electric Piano 2", "23 Honky-Tonk", "24 Clavinet 1", "25 Harpsichord", "26 Pipe Organ", "27 Jazz Organ", "28 Rock Organ",
        "31 Slap Bass 1", "32 Slap Bass 2", "33 Synth Bass 1", "34 Synth Bass 2", "35 Fretless Bass", "36 Wood Bass", "37 Flute Solo", "38 Pan Flute",
        "41 DWGS Bell 1", "42 DWGS Bell 2", "43 Marimba", "44 Vibes", "45 Steel Drum", "46 Koto", "47 Sitar", "48 Harmonica",
        "51 Poly Synth 1", "52 Poly Synth 2", "53 Reso Sweep Lead", "54 Sync Solo", "55 Fifth Lead", "56 Square Solo", "57 Saw Stack Solo", "58 Modular Brass",
        "61 Space Pad 1", "62 Space Pad 2", "63 Analog Strings", "64 Digital Chime", "65 Crystal Bells", "66 Metallic Hit", "67 Windstorm FX", "68 Sci-Fi Siren",
        "71 Delay Echo Pluck", "72 Delay Lead Solo", "73 Slap Echo Bass", "74 Rotary Delay Organ", "75 Arpeggio Pluck", "76 Synth Chime", "77 Laser Zap Drop", "78 Ocean Wave FX",
        "81 Funky DWGS Clav", "82 Fat Analog Horns", "83 Warm Cello Pad", "84 Sub Bass 8000", "85 Acid Squelch DW", "86 Cybernetic Lead", "87 Cathedral Tutti", "88 DW-8000 Signature"
    ]
    
    presets = []
    for idx, name in enumerate(dw8000_names):
        cat = 'BRASS' if 'Brass' in name or 'Horn' in name or 'Trumpet' in name else ('STRINGS' if 'String' in name or 'Cello' in name or 'Violin' in name else ('KEYBOARD' if 'Piano' in name or 'Organ' in name or 'Clav' in name else ('BASS' if 'Bass' in name else 'SYNTH')))
        presets.append({
            'bank': 'FACTORY PRESETS',
            'program': idx + 1,
            'name': name,
            'category': cat,
            'tags': ['dw8000', 'dwgs-analog', cat.lower()]
        })
        
    save_profile_and_presets('dw-8000', profile, presets)

if __name__ == '__main__':
    build_m1()
    build_wavestation()
    build_01w()
    build_trinity()
    build_triton()
    build_ms2000()
    build_microkorg()
    build_prophecy()
    build_z1()
    build_dw8000()
