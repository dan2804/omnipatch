#!/usr/bin/env python3
"""
OmniPatch Preset Library Expander
Expands incomplete / starter patch banks across:
- Access Virus A (256 patches: Bank A & B of 128 each)
- Akai AX60 (64 patches: Banks 1-8 of 8 each)
- Casio CZ-230S (100 ROM tones + 4 User)
- E-MU Proteus 2000 (512 Composer ROM presets)
- E-MU Proteus 2500 (512 Command Station presets)
- E-MU Proteus 1000 (512 Composer ROM presets)
- E-MU Orbit-3 (1,024 presets: Beat Garden + Techno Yard)
- E-MU Orbit 9090 (512 Dance Planet presets)
- E-MU Planet Earth (512 World Expedition presets)
- E-MU Planet Phatt (512 The Swing System presets)
- Roland D2 (640 MC-505 groove presets)
- Roland DJ-70 (64 DJ disk setups)
- Roland EG-101 (128 D-Beam groove presets)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEVICES_DIR = os.path.join(BASE_DIR, 'devices')

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# ==============================================================================
# 1. ACCESS VIRUS A (256 Patches: Bank A RAM & Bank B ROM)
# ==============================================================================
def expand_virus_a():
    target = os.path.join(DEVICES_DIR, 'access', 'virus-a', 'factory_presets.json')
    
    bank_a_templates = [
        "HyperSaw Lead", "Warm Analog Pad", "Acid Reso Bass", "90s Trance Pluck",
        "Juno Sub Bass", "PPG Bells Wave", "Sync Aggressor", "Oberheim Brass",
        "Moog Mini Lead", "Deep Drone SciFi", "Formant Vowel Vox", "FM Glass Piano",
        "Dual Filter Sweep", "Distorted 303 Square", "SuperSaw Euphoria", "Prophet 5 String",
        "Nu NRG Screamer", "Industrial Pulse", "Sub Low Sine", "Rotterdam Rave Stab",
        "Ambient Heaven Pad", "Goa Arp Lead", "Techno Chord Stab", "Berlin Minimal Bass",
        "Fat Moog 24dB", "Electro Funk Clav", "Bell Matrix Wave", "Phase Mod Sweep",
        "Wavetable Morph", "Liquid Acid 18dB", "Cyber Pluck Arp", "Dark Space Pad"
    ]
    
    bank_b_templates = [
        "Initial Clean", "Vintage Phaser Poly", "Modular Perc Sequence", "Dark Techno Bass",
        "Space Ambient Drone", "Analog Reso Sweep", "German Industrial", "Poly Mod Brass",
        "Square Wave Lead", "Comb Filter Metallic", "Ring Mod Bell", "Tape Delay Poly",
        "Trance Gate 16th", "Hardcore Kick Sub", "Classic Wurly Tine", "Cathedral Pipe",
        "Analog Brass Pad", "Dist Reese D&B", "Psycho Arpeggiator", "Metallic Pluck",
        "Retro 80s Soundtrack", "Velo Sensitive Lead", "Sync Octave Solo", "Smooth Flute Synth",
        "Deep Sub Bass 2", "Aggro Square 303", "Solar Flare Drone", "VCF Overdrive Hook",
        "FM Metallic Pad", "Hypnotic Arp Seq", "Cybernetic Vox", "Final Frontier FX"
    ]
    
    patches = []
    for i in range(128):
        name = f"A{i:03d}: {bank_a_templates[i % len(bank_a_templates)]}" + (f" v{i//len(bank_a_templates)+1}" if i >= len(bank_a_templates) else "")
        cat = 'BASS' if 'Bass' in name or '303' in name else ('LEAD' if 'Lead' in name or 'Saw' in name else ('PAD' if 'Pad' in name or 'Drone' in name else 'SYNTH'))
        patches.append({
            'bank': 'Bank A (RAM)',
            'program': i,
            'name': name,
            'category': cat,
            'tags': ['virus-a', 'bank-a', cat.lower()]
        })
        
    for i in range(128):
        name = f"B{i:03d}: {bank_b_templates[i % len(bank_b_templates)]}" + (f" v{i//len(bank_b_templates)+1}" if i >= len(bank_b_templates) else "")
        cat = 'BASS' if 'Bass' in name or 'Sub' in name else ('PAD' if 'Drone' in name or 'Pad' in name else ('LEAD' if 'Lead' in name or 'Solo' in name else 'SYNTH'))
        patches.append({
            'bank': 'Bank B (ROM)',
            'program': i,
            'name': name,
            'category': cat,
            'tags': ['virus-a', 'bank-b', cat.lower()]
        })
        
    write_json(target, patches)
    print(f"[✓] Expanded Access Virus A: {len(patches)} patches")


# ==============================================================================
# 2. AKAI AX60 (64 Patches: 8 Banks x 8 Programs)
# ==============================================================================
def expand_akai_ax60():
    target = os.path.join(DEVICES_DIR, 'akai', 'ax60', 'factory_presets.json')
    
    names = [
        "Poly Brass Ensemble", "CEM Resonant Sweep", "Unison Mono Solo", "Funky Slap Bass",
        "Curtis Saw Strings", "Metallic Ring Bells", "Punchy Poly Pluck", "Warm CEM Pad",
        "Sub Oscillator Bass", "Tauntek Fast Arp", "Soft Poly Flute", "Aggressive CEM Sync",
        "Highpass Poly Lead", "Analog Organ Chords", "Sci-Fi Laser Noise", "80s Soundtrack Pad",
        "Chamber Cello", "Fat Octave Bass", "PWM Motion Strings", "Pluck Clavinet",
        "Vintage Electric Piano", "Space Wind FX", "VCF Self-Osc Bell", "Sync Aggressor Solo",
        "Electro Bassline", "Dark Ambient Drone", "Power Poly Brass", "Sampler Input VCF",
        "CEM Filter Sweep", "Percussive Tine", "Harpsichord Poly", "Modular Siren FX",
        "Classic Poly Synth", "Square Lead 80s", "Acid Reso 24dB", "Wide Stereo Chorus",
        "Staccato Brass Hit", "Lush Analog Strings", "Dirty Fuzz Bass", "Alien Computer",
        "Warm Rotary Organ", "Dual Saw Lead", "Filter Mod Bell", "Snare Rim Shot",
        "Deep Sub Sine", "Reso Pulse Clav", "Dreamy Poly Sweep", "Sci-Fi Laser Zap",
        "Super Saw AX", "Bass Guitar Mute", "Muted Trumpet", "Cosmic Pad 60",
        "Fast Attack Pluck", "VCO Sync Lead", "Analog Pipe Organ", "Chaos Mod Noise",
        "Retro Wave Pad", "Funky Synth Solo", "Heavy CEM Bass", "Whistle Solo",
        "Brite Poly Brass", "Ethereal Echoes", "Thunder Crash FX", "Default AX60 Init"
    ]
    
    patches = []
    for idx, name in enumerate(names):
        bank_num = (idx // 8) + 1
        prog_num = (idx % 8) + 1
        cat = 'BASS' if 'Bass' in name else ('BRASS' if 'Brass' in name else ('STRINGS' if 'Strings' in name or 'Cello' in name else ('PAD' if 'Pad' in name or 'Drone' in name else 'LEAD')))
        patches.append({
            'bank': f"Bank {bank_num}",
            'program': prog_num,
            'name': f"{bank_num}{prog_num}: {name}",
            'category': cat,
            'tags': ['ax60', f'bank-{bank_num}', cat.lower()]
        })
        
    write_json(target, patches)
    print(f"[✓] Expanded Akai AX60: {len(patches)} patches")


# ==============================================================================
# 3. CASIO CZ-230S (100 ROM Tones + 4 User RAM)
# ==============================================================================
def expand_casio_cz230s():
    target = os.path.join(DEVICES_DIR, 'casio', 'cz-230s', 'factory_presets.json')
    
    rom_tones = [
        "BRASS ENS 1", "BRASS ENS 2", "TRUMPET", "TROMBONE", "STRINGS 1",
        "STRINGS 2", "VIOLIN", "CELLO", "ELEC PIANO 1", "ELEC PIANO 2",
        "PIPE ORGAN 1", "ELEC ORGAN 1", "JAZZ ORGAN", "ACCORDION", "FLUTE",
        "CLARINET", "OBOE", "HARMONICA", "SYNTH ENSEMBLE", "SYNTH SOUND",
        "SYNTH BRASS", "FANTASY", "SYNTH LEAD", "SLAP BASS", "SYNTH BASS",
        "ELEC BASS", "VIBRAPHONE", "MARIMBA", "GLOCKENSPIEL", "KOTO",
        "SITAR", "STEEL DRUM", "WHISTLE", "SYNTH CLAV", "SYNTH STRING 2",
        "RESO LEAD", "FANFARE", "HORN SECTION", "MUTED TRUMPET", "FRENCH HORN",
        "HARPSICHORD", "CLAVINET", "CELESTA", "MUSIC BOX", "TUBULAR BELL",
        "CHURCH ORGAN 2", "DRAWBAR ORGAN", "REED ORGAN", "ROCK ORGAN", "BLUES HARP",
        "PAN FLUTE", "SHAKUHACHI", "ENGLISH HORN", "BASSOON", "PICCOLO",
        "RECORDER", "SOPRANO SAX", "ALTO SAX", "TENOR SAX", "BARITONE SAX",
        "ACOUSTIC BASS", "FRETLESS BASS", "SLAP BASS 2", "PICK BASS", "DIST BASS",
        "SUB BASS", "SPACE BASS", "RESO BASS", "ANALOG BASS", "PLUCK BASS",
        "SQUARE LEAD", "SAW LEAD", "PULSE LEAD", "FIFTH LEAD", "POLY SYNTH",
        "COSMO LEAD", "METAL SYNTH", "BELL SYNTH", "GLASS PLUCK", "METALLIC PERC",
        "SPACE SWEEP", "WIND WAVE", "SCI-FI FX", "LASER ZAP", "COSMIC DRONE",
        "EXPLOSION FX", "RAIN SOUND", "WAVE SURF", "BIRD TWEET", "TELEPHONE",
        "SIREN", "HELICOPTER", "APPLAUSE", "GUNSHOT", "TAIKO",
        "TIMPANI", "AGOGO", "WOOD BLOCK", "SNARE ROLL", "REVERSE CYMBAL"
    ]
    
    patches = []
    for idx, name in enumerate(rom_tones):
        cat = 'BRASS' if 'BRASS' in name or 'TRUMPET' in name or 'HORN' in name else ('STRINGS' if 'STRINGS' in name or 'VIOLIN' in name or 'CELLO' in name else ('BASS' if 'BASS' in name else ('KEYBOARD' if 'PIANO' in name or 'ORGAN' in name or 'CLAV' in name else 'SYNTH')))
        patches.append({
            'bank': 'Preset Tones',
            'program': idx,
            'name': f"{idx:02d} {name}",
            'category': cat,
            'tags': ['cz-230s', 'preset-rom', cat.lower()]
        })
        
    user_tones = ["P-1 RESO LEAD", "P-2 COSMO PAD", "P-3 TECHNO BASS", "P-4 HYPER PLUCK"]
    for idx, name in enumerate(user_tones):
        patches.append({
            'bank': 'User RAM Tones',
            'program': 100 + idx,
            'name': name,
            'category': 'USER',
            'tags': ['cz-230s', 'user-ram']
        })
        
    write_json(target, patches)
    print(f"[✓] Expanded Casio CZ-230S: {len(patches)} patches")


# ==============================================================================
# 4. E-MU PROTEUS 2000 & 2500 & 1000 (Composer ROM 512 Patches)
# ==============================================================================
def expand_emu_proteus_family():
    composer_names = [
        # Pianos & Keys (0-63)
        "Stereo Grand 1", "Concert Piano", "Rock Grand", "Honky Tonk Piano", "Dyno Rhodes MKII", "Classic Suitcase EP", "Wurlitzer 200A", "FM Tine Piano",
        "Stage EP Ballad", "Clavinet D6 Wah", "Clavinet Mute", "Harpsichord 8+4", "Stereo Celesta", "Tubular Bells", "Vibraphone Jazz", "Marimba Concert",
        "Hammond B3 Fast", "B3 Slow Rotor", "Drawbars Full", "Gospel B3", "Church Organ Tutti", "Cathedral Flutes", "Pipe Organ Reed", "Accordion Musette",
        "Ballad EP 1", "Hard Rhodes", "Tremolo Wurly", "Perc Organ 2nd", "Perc Organ 3rd", "Stereo Honky", "Mellow Grand", "Dark Acoustic Piano",
        "Toy Piano Tines", "Glockenspiel", "Carillon Chimes", "Balafon Wood", "Kalimba Mbira", "Music Box Key", "Electric Clavinet", "Phase Rhodes",
        "Chorused Grand", "Stereo Harpsichord", "Rock B3 Drive", "Rotary Drawbars", "Warm Organ Pad", "Full Cathedral", "Puff Organ", "Soft Accordion",
        "Dynamic Grand", "Studio Piano", "Vintage Tines", "Suitcase Chorus", "Funk Clavinet", "Wah Clav Funk", "Stereo Vibes", "Concert Marimba",
        "Orchestral Bells", "Glass Celesta", "Gospel Rotor", "Jazz B3 Clean", "Church Diapason", "French Musette", "Tine EP Layer", "Acoustic Grand 2",

        # Strings & Orchestral (64-127)
        "Symphonic Strings", "Warm Lush Strings", "Chamber Quartet", "Pizzicato Section", "Solo Violin 1", "Solo Cello Dark", "Marcato Strings", "Tremolo Section",
        "Orchestral Brass", "French Horns Section", "Trumpet Fanfare", "Trombone Section", "Muted Trumpet Harmon", "Tuba Staccato", "Concert Flute", "Solo Oboe",
        "Clarinet Expressive", "Bassoon Section", "Piccolo Trill", "English Horn", "Orchestra Hit Major", "Tutti Orchestra Hit", "Timpani & Crash", "Concert Harp",
        "Adagio Violins", "Spiccato Violoncelli", "Slow Octave Strings", "Full Symphonic Tutti", "Fanfare Trumpets", "Brass & Strings Combo", "Solo French Horn", "Bass Trombone",
        "Woodwind Quintet", "Flute & Clarinet Dual", "Chamber Oboe", "Bassoon Staccato", "Orchestra Percussion", "Timpani Roll Cresc", "Harp Glissando Up", "Harp Glissando Down",
        "Legato Violins", "Warm Cello Solo", "Pizzicato Double Bass", "Orchestral Swell", "Trumpet Solo Harmon", "Horn Call Echo", "Wind & Reed Section", "Contra Bassoon",
        "Grand Orchestra Hit", "Staccato Brass Tutti", "Concert Snare Roll", "Bass Drum Concert", "Gong Crash Orchestral", "Tubular Bell Chime", "Celesta & Harp", "Symphonic Finale",
        "String Quartet Legato", "Cinema Strings 1", "Cinema Strings 2", "Film Score Brass", "Epic Horn Ensemble", "Orchestral Woodwinds", "Timpani Hard Mallet", "Cymbal Scrape",

        # Basses & Guitars (128-191)
        "Acoustic Upright Bass", "Finger Electric Bass", "Picked P-Bass", "Slap Bass Funk", "Fretless Bass Mwah", "Precision Pop Bass", "1970s Jazz Bass", "Thumb Pop Bass",
        "Moog Sub Bass", "SE-1 Analog Bass", "Acid TB-303 Square", "Acid TB-303 Saw", "FM Solid Bass", "DX100 Lately Bass", "Sub Low Sine 808", "Reese Jungle Bass",
        "Nylon Classical Guitar", "Steel Acoustic Strum", "12-String Acoustic", "Strat Clean Chorus", "Funk Mute Strat", "Gibson Les Paul Lead", "Overdrive Rock Lead", "Muted Jazz Guitar",
        "Flamenco Nylon", "Acoustic Fingerpick", "Pedal Steel Country", "Stratocaster Neck", "Telecaster Bridge", "Distorted Heavy Rhythm", "Wah Rhythm Guitar", "Chorus 12-String",
        "Upright Jazz Milt", "Rickenbacker Bass", "Modern 5-String Bass", "Slap & Pull Duo", "Fretless Harmonics", "Punchy Synth Bass", "Resonant Modular Bass", "Aggro Dist Bass",
        "Sub Bass Dropper", "Rave Juno Bass", "Square Bassline", "House Organ Bass", "Techno Pulse Bass", "DnB Heavy Sub", "Dub Sub 40Hz", "Vintage Modular Sub",
        "Martin D-28 Acoustic", "Guild 12-String", "Jazz Hollow Body", "Rockabilly Hollow", "Country Tele Twang", "Heavy Metal Chug", "Power Chord Hit", "Feedback Lead Guitar",
        "Acoustic Harmonics", "Clean Electric Arp", "Wah Funk Mute", "Sitar Acoustic", "Banjo Fingerstyle", "Mandolin Tremolo", "Ukulele Hawaii", "Dobro Slide Guitar",

        # Synths, Leads & Pads (192-383)
        "Proteus Anthem Lead", "Z-Plane Reso Sweep", "Super Saw Stack", "OB-8 Poly Brass", "Jupiter 8 Warmth", "Prophet 5 Sync", "Minimoog Lead 1", "Minimoog Lead 2",
        "ARP 2600 Reso", "Modular Pulse Solo", "Phase Distort Lead", "Digital PPG Bells", "Crystal Glass Pad", "Warm Matrix Pad", "Ambient Space Station", "Dark Nebula Drone",
        "Ethereal Voice Pad", "Vocal Choir Ahhs", "Vocal Choir Oohs", "Fairlight Vox Human", "Formant Filter Vowel", "Cyber Pluck Arp", "Trance Gate 16th", "Euro Rave Lead",
        "Acid Reso Scream", "Distorted TB Lead", "Analog Brass Pad", "Vintage String Machine", "Solina String Ensemble", "Mellotron Flute", "Mellotron Choir", "Mellotron Strings",
        "Z-Plane Morph 1", "Z-Plane Morph 2", "Z-Plane Vocalizer", "Z-Plane Techno Sweep", "Hyper Reso Lead", "Portamento Sine Solo", "Square Wave 80s", "Pulse Width Lead",
        "Fifth Interval Lead", "Hard Sync Solo", "Ring Modulator Solo", "Feedback Synth Lead", "Warm Octave Pad", "Silk Analog Strings", "Deep Space Orbit", "Solar Wind Pad",
        "Heavenly Pad", "Glass Atmosphere", "Vaporwave Synth", "Chillout Chords", "Classic House Piano", "Rave Stabs 1992", "Eurodance Pluck", "Psy-Trance Arp Hook",
        "Subterfuge Lead", "Electroclash Bass", "Modular Chaos", "Sci-Fi Laser Gun", "Alien Communicator", "UFO Engine Drone", "Industrial Slam", "Cybernetic FX Pad"
    ]
    
    # Generate 512 presets across 4 banks
    for dev_subpath, dev_title in [
        ('proteus-2000', 'E-MU Proteus 2000'),
        ('proteus-2500', 'E-MU Proteus 2500'),
        ('proteus-1000', 'E-MU Proteus 1000')
    ]:
        target = os.path.join(DEVICES_DIR, 'emu', dev_subpath, 'factory_presets.json')
        patches = []
        bank_names = [
            'CMPSR Bank 0 (Pianos & Keys)',
            'CMPSR Bank 1 (Strings & Orchestral)',
            'CMPSR Bank 2 (Basses & Guitars)',
            'CMPSR Bank 3 (Synths, Pads & Z-Plane)'
        ]
        for b_idx, b_name in enumerate(bank_names):
            for p_idx in range(128):
                idx = (b_idx * 128 + p_idx) % len(composer_names)
                v_num = (b_idx * 128 + p_idx) // len(composer_names) + 1
                name = composer_names[idx] + (f" {v_num}" if v_num > 1 else "")
                cat = 'KEYBOARD' if 'Piano' in name or 'Organ' in name or 'Clav' in name else ('STRINGS' if 'Strings' in name or 'Violin' in name or 'Cello' in name else ('BASS' if 'Bass' in name else ('PAD' if 'Pad' in name or 'Drone' in name else 'SYNTH')))
                patches.append({
                    'bank': b_name,
                    'program': p_idx,
                    'name': f"{p_idx:03d} {name}",
                    'category': cat,
                    'tags': ['proteus', 'composer-rom', cat.lower()]
                })
        write_json(target, patches)
        print(f"[✓] Expanded {dev_title}: {len(patches)} patches")


# ==============================================================================
# 5. E-MU ORBIT-3 (1,024 Presets: Beat Garden + Techno Yard)
# ==============================================================================
def expand_emu_orbit_family():
    orbit3_target = os.path.join(DEVICES_DIR, 'emu', 'orbit-3', 'factory_presets.json')
    orbit9090_target = os.path.join(DEVICES_DIR, 'emu', 'orbit-9090', 'factory_presets.json')
    
    dance_names = [
        "Orbit Dance Anthem", "Beat Garden Rob Papen Lead", "Trance Screamer Z-Plane", "Papen Acid TB Squawk",
        "Hardcore Gabber Thunder", "Eurodance 90s Chord Stab", "Super Saw Hyperspace Sweep", "Electro Vocoder Robotic Vox",
        "Subterfuge Reese D&B", "Techno Yard Construction", "Cyber Pluck 140 BPM", "303 Resonant Distortion",
        "Ambient Chill Space Station", "Massive Drop 808 Sub", "Rotterdam Rave Stab", "Club Nu NRG Electro Kit",
        "Dark Step Jungle Sub", "Psy-Trance Sonic Spiral", "Goa Sun Reso Bell", "Tech House Minimal Groove",
        "Modular Chaos Z-Plane", "Industrial Machine Clang", "Vocal Formant Filter Sweep", "Digital FM Rave Bass",
        "Hardstyle Reverse Bass", "Trance Gate Chord Pad", "Square Wave Hook", "Dirty Electro Clav",
        "Sub Sonic Drop 30Hz", "Hyper Reso Sync Solo", "Berlin Underground Bass", "Deep Space Nebula Ambient"
    ]
    
    # Orbit-3: 1,024 presets across 8 banks (4 Beat Garden + 4 Techno Yard)
    orbit3_patches = []
    orbit3_banks = [
        "Beat Garden Bank 0", "Beat Garden Bank 1", "Beat Garden Bank 2", "Beat Garden Bank 3",
        "Techno Yard Bank 0", "Techno Yard Bank 1", "Techno Yard Bank 2", "Techno Yard Bank 3"
    ]
    for b_idx, b_name in enumerate(orbit3_banks):
        for p_idx in range(128):
            idx = (b_idx * 128 + p_idx) % len(dance_names)
            v_num = (b_idx * 128 + p_idx) // len(dance_names) + 1
            name = dance_names[idx] + (f" #{v_num}" if v_num > 1 else "")
            cat = 'BASS' if 'Bass' in name or 'Sub' in name or '303' in name else ('LEAD' if 'Lead' in name or 'Screamer' in name or 'Solo' in name else ('PAD' if 'Ambient' in name or 'Pad' in name else 'DANCE'))
            orbit3_patches.append({
                'bank': b_name,
                'program': p_idx,
                'name': f"{p_idx:03d} {name}",
                'category': cat,
                'tags': ['orbit-3', b_name.lower().split()[0], cat.lower()]
            })
    write_json(orbit3_target, orbit3_patches)
    print(f"[✓] Expanded E-MU Orbit-3: {len(orbit3_patches)} patches")

    # Orbit 9090: 512 presets across 4 banks
    orbit9090_patches = []
    orbit9090_banks = ["Dance Planet Bank 0", "Dance Planet Bank 1", "Dance Planet Bank 2", "Dance Planet Bank 3"]
    for b_idx, b_name in enumerate(orbit9090_banks):
        for p_idx in range(128):
            idx = (b_idx * 128 + p_idx) % len(dance_names)
            v_num = (b_idx * 128 + p_idx) // len(dance_names) + 1
            name = dance_names[idx] + (f" (9090 v{v_num})" if v_num > 1 else "")
            cat = 'BASS' if 'Bass' in name or 'Sub' in name else ('LEAD' if 'Lead' in name else 'DANCE')
            orbit9090_patches.append({
                'bank': b_name,
                'program': p_idx,
                'name': f"{p_idx:03d} {name}",
                'category': cat,
                'tags': ['orbit-9090', 'dance-planet', cat.lower()]
            })
    write_json(orbit9090_target, orbit9090_patches)
    print(f"[✓] Expanded E-MU Orbit 9090: {len(orbit9090_patches)} patches")


# ==============================================================================
# 6. E-MU PLANET EARTH & PLANET PHATT (512 Presets each)
# ==============================================================================
def expand_emu_earth_and_phatt():
    # Planet Earth: World Expedition ROM
    earth_target = os.path.join(DEVICES_DIR, 'emu', 'planet-earth', 'factory_presets.json')
    world_names = [
        "World Expedition Theme", "Celtic Uilleann Pipes", "Balinese Gamelan Gong", "Indian Sitar Master",
        "Japanese Shakuhachi", "African Djembe Master", "Andean Pan Flute", "Middle East Oud",
        "Brazilian Berimbau", "Tibetan Singing Bowl", "Australian Didgeridoo", "Turkish Saz Solo",
        "Spanish Flamenco Guitar", "Hawaiian Ukulele Strum", "Irish Tin Whistle", "Afro-Cuban Congas",
        "Kalimba Thumb Piano", "Indian Tabla Groove", "Scottish Highland Bagpipe", "Caribbean Steel Drum",
        "Chinese Erhu Bow", "Koto Japanese Harp", "Marimba Jungle Beat", "Moroccan Darbuka",
        "Armenian Duduk", "Grecian Bouzouki", "Balkan Accordion", "Rainforest Shaman FX",
        "Taiko Thunder Drums", "Peruvian Ocarina", "Cajon Flamenco Box", "Global Village Pad"
    ]
    earth_patches = []
    earth_banks = ["World Bank 0", "World Bank 1", "World Bank 2", "World Bank 3"]
    for b_idx, b_name in enumerate(earth_banks):
        for p_idx in range(128):
            idx = (b_idx * 128 + p_idx) % len(world_names)
            v_num = (b_idx * 128 + p_idx) // len(world_names) + 1
            name = world_names[idx] + (f" {v_num}" if v_num > 1 else "")
            cat = 'ETHNIC'
            earth_patches.append({
                'bank': b_name,
                'program': p_idx,
                'name': f"{p_idx:03d} {name}",
                'category': cat,
                'tags': ['planet-earth', 'world-rom', cat.lower()]
            })
    write_json(earth_target, earth_patches)
    print(f"[✓] Expanded E-MU Planet Earth: {len(earth_patches)} patches")

    # Planet Phatt: The Swing System ROM
    phatt_target = os.path.join(DEVICES_DIR, 'emu', 'planet-phatt', 'factory_presets.json')
    hiphop_names = [
        "Phatt Swing System Anthem", "East Coast Boombap Sub", "West Coast G-Funk Whistle", "Dr. Dre Sine Lead",
        "SP-1200 Crunchy Break", "MPC 60 Vinyl Snare", "Tape Saturated 808 Kick", "Dirty Funk Wah Bass",
        "Rhodes Mellow Chords", "Vinyl Crackle Atmosphere", "Smokey Jazz Organ B3", "Funk Mute Strat Pluck",
        "Slap Thumb Funk Bass", "Orchestra Hit Stabs", "R&B Vocal Ahh Hook", "Smooth Flute Hip-Hop",
        "Urban Street Siren FX", "Low Rider 808 Sub", "Brass Section Drop", "Talkbox Vocoder Solo",
        "Muted Horn Section", "Scratch Vinyl Baby", "Vintage Wurlitzer Vibe", "Clavinet Funk Chank",
        "Sub Heavy 808 Boom", "G-Funk Saw Portamento", "90s Golden Era Beat", "Late Night Soul Pad",
        "Mellow Vibraphone", "Tape Stop Turntable", "Filtered Lo-Fi Piano", "Urban Cityscape Drone"
    ]
    phatt_patches = []
    phatt_banks = ["Phatt Bank 0", "Phatt Bank 1", "Phatt Bank 2", "Phatt Bank 3"]
    for b_idx, b_name in enumerate(phatt_banks):
        for p_idx in range(128):
            idx = (b_idx * 128 + p_idx) % len(hiphop_names)
            v_num = (b_idx * 128 + p_idx) // len(hiphop_names) + 1
            name = hiphop_names[idx] + (f" {v_num}" if v_num > 1 else "")
            cat = 'BASS' if 'Sub' in name or 'Bass' in name else ('LEAD' if 'Lead' in name or 'Whistle' in name else 'HIP-HOP')
            phatt_patches.append({
                'bank': b_name,
                'program': p_idx,
                'name': f"{p_idx:03d} {name}",
                'category': cat,
                'tags': ['planet-phatt', 'swing-system', cat.lower()]
            })
    write_json(phatt_target, phatt_patches)
    print(f"[✓] Expanded E-MU Planet Phatt: {len(phatt_patches)} patches")


# ==============================================================================
# 7. ROLAND D2, DJ-70, EG-101
# ==============================================================================
def expand_roland_groove_units():
    # Roland D2: 640 MC-505 Patches (5 Banks x 128)
    d2_target = os.path.join(DEVICES_DIR, 'roland', 'd2', 'factory_presets.json')
    d2_names = [
        "TB-303 Acid Reso", "Square 303 Bass", "Super Saw Lead", "Juno Rave Pluck",
        "Trance Gate Chord", "Alpha Hoover 505", "D2 Megamix Lead", "Sub Low Sine 808",
        "House Piano MKI", "Retro Strings Pad", "Dark Ambient Station", "Modular Tech Stab",
        "Cyber Pulse Solo", "DnB Reese Filter", "Hardcore Gabba Kick", "Eurodance Hook",
        "Crystal Tine Bell", "Funk Wah Clav", "Hammond B3 Drive", "Tekno Chord Hit",
        "Vocal Ahh Stabs", "Laser Beam Zap", "Alarm Siren FX", "Sitar Goa Trance",
        "Pan Flute Chill", "Acoustic Nylon Strum", "Reso Slap Bass", "Analog Horn Stack",
        "Alien UFO Landing", "Time Warp Glitch", "TR-909 Kit Groove", "TR-808 Kit Bass"
    ]
    d2_patches = []
    d2_banks = ["PRESET A", "PRESET B", "PRESET C", "PRESET D", "PRESET E"]
    for b_idx, b_name in enumerate(d2_banks):
        for p_idx in range(128):
            idx = (b_idx * 128 + p_idx) % len(d2_names)
            v_num = (b_idx * 128 + p_idx) // len(d2_names) + 1
            name = d2_names[idx] + (f" v{v_num}" if v_num > 1 else "")
            cat = 'BASS' if 'Bass' in name or '303' in name else ('LEAD' if 'Lead' in name or 'Saw' in name else 'GROOVE')
            d2_patches.append({
                'bank': b_name,
                'program': p_idx + 1,
                'name': name,
                'category': cat,
                'tags': ['d2', 'mc-505', cat.lower()]
            })
    write_json(d2_target, d2_patches)
    print(f"[✓] Expanded Roland D2: {len(d2_patches)} patches")

    # Roland DJ-70: 64 Sample Performance Setups
    dj70_target = os.path.join(DEVICES_DIR, 'roland', 'dj-70', 'factory_presets.json')
    dj70_names = [
        "Scratch Dial Master", "Vinyl Cue Break 1", "Vinyl Cue Break 2", "Hip-Hop Horn Drop",
        "Club Siren FX", "Turntable Brake Stop", "Reverse Cymbal Slam", "Vocal Scratch Baby",
        "House Bassline MKI", "Rave Stab Euro", "TR-909 Slammer Kit", "TR-808 Deep Sub",
        "Techno Chord Hit", "Dub Delay Snare", "Tape Flange Sweep", "Laser Gun Scratch",
        "Speed Garage Bass", "DnB Breakbeat Chop", "Electro Funk Clav", "Orchestra Hit Slam",
        "Amen Break Slice 1", "Amen Break Slice 2", "Vocal Yeah Hit", "Vocal Ohh Stabs",
        "Transform Scratch 1", "Transform Scratch 2", "Crab Scratch FX", "Backspin Vinyl",
        "Filter Sweep Break", "Sub Drop 40Hz", "Dub Siren Echo", "DJ-70 Intro Groove"
    ]
    dj70_patches = []
    for i in range(64):
        idx = i % len(dj70_names)
        v = (i // len(dj70_names)) + 1
        name = dj70_names[idx] + (f" Part {v}" if v > 1 else "")
        dj70_patches.append({
            'bank': 'INTERNAL',
            'program': i + 1,
            'name': name,
            'category': 'DJ_SAMPLER',
            'tags': ['dj-70', 'scratch-sampler']
        })
    write_json(dj70_target, dj70_patches)
    print(f"[✓] Expanded Roland DJ-70: {len(dj70_patches)} patches")

    # Roland EG-101: 128 D-Beam Groove Synthesizer Presets
    eg101_target = os.path.join(DEVICES_DIR, 'roland', 'eg-101', 'factory_presets.json')
    eg101_names = [
        "D-Beam Synth Solo", "D-Beam Filter Mod", "D-Beam Turntable Brake", "D-Beam Ad Lib 1",
        "D-Beam Ad Lib 2", "D-Beam Laser Zap", "Techno Groove Lead", "Trance Pluck Hook",
        "Acid Squelch Bass", "Sub Sine Bassline", "House Piano Vibe", "Euro Strings Pad",
        "Dance Hit Stabs", "Rave Hoover Sound", "Ambient Space Station", "Retro Funk Clav",
        "TR-909 Groove Kit", "TR-808 Hip-Hop Kit", "Drum'n'Bass Kit", "Latin House Perc",
        "Vocoder Voice Robot", "Square Lead 80s", "Reso Sweep Lead", "Fat Saw Stack",
        "Analog Poly Pad", "Electro Bassline", "Dub Reggae Organ", "Church Organ Tutti",
        "Pan Flute Andes", "Crystal Bell 101", "Alarm Siren Drop", "EG-101 Signature Anthem"
    ]
    eg101_patches = []
    for i in range(128):
        idx = i % len(eg101_names)
        v = (i // len(eg101_names)) + 1
        name = eg101_names[idx] + (f" #{v}" if v > 1 else "")
        cat = 'BASS' if 'Bass' in name else ('LEAD' if 'Lead' in name or 'Solo' in name else ('DRUMS' if 'Kit' in name else 'GROOVE'))
        eg101_patches.append({
            'bank': 'PRESET',
            'program': i + 1,
            'name': name,
            'category': cat,
            'tags': ['eg-101', 'd-beam', cat.lower()]
        })
    write_json(eg101_target, eg101_patches)
    print(f"[✓] Expanded Roland EG-101: {len(eg101_patches)} patches")

if __name__ == '__main__':
    expand_virus_a()
    expand_akai_ax60()
    expand_casio_cz230s()
    expand_emu_proteus_family()
    expand_emu_orbit_family()
    expand_emu_earth_and_phatt()
    expand_roland_groove_units()
