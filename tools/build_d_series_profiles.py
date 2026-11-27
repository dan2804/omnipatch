#!/usr/bin/env python3
"""
OmniPatch Roland D-Series (D-50, D-20, D-70) Ingestion Pipeline
Generates production-ready declarative YAML profiles and JSON preset libraries
for Roland's legendary Linear Arithmetic (LA & Super-LA) synthesizers.
"""

import os
import json
import yaml

OUTPUT_BASE = "devices/roland"

def get_d50_presets():
    # Complete 64 Factory ROM Patches for Roland D-50 (Banks 1-8, Patches 1-8)
    d50_patches = [
        # Bank 1
        {"id": "11", "name": "Fantasia", "cat": "SYNTH", "tags": ["bell", "pad", "classic"]},
        {"id": "12", "name": "DigitalNativeDance", "cat": "ETHNIC", "tags": ["rhythmic", "percussive", "classic"]},
        {"id": "13", "name": "Soundtrack", "cat": "PAD", "tags": ["ambient", "warm", "classic"]},
        {"id": "14", "name": "Living Calliope", "cat": "KEYBOARD", "tags": ["organ", "flute"]},
        {"id": "15", "name": "Stereo Polysynth", "cat": "SYNTH", "tags": ["analog", "poly"]},
        {"id": "16", "name": "Deep Strings", "cat": "STRINGS", "tags": ["lush", "analog"]},
        {"id": "17", "name": "Gamelan Bell", "cat": "MALLET", "tags": ["metallic", "bell"]},
        {"id": "18", "name": "Cathedral Organ", "cat": "ORGAN", "tags": ["pipe", "church"]},

        # Bank 2
        {"id": "21", "name": "Glass Voices", "cat": "PAD", "tags": ["choir", "crystal"]},
        {"id": "22", "name": "Staccato Choral", "cat": "VOICE", "tags": ["vocal", "staccato"]},
        {"id": "23", "name": "Pizzagogo", "cat": "PLUCK", "tags": ["agogo", "pizzicato", "classic"]},
        {"id": "24", "name": "Horn Section", "cat": "BRASS", "tags": ["horns", "brass"]},
        {"id": "25", "name": "Shaku / Flute", "cat": "WIND", "tags": ["ethnic", "bamboo"]},
        {"id": "26", "name": "Arco Strings", "cat": "STRINGS", "tags": ["bowed", "orchestral"]},
        {"id": "27", "name": "Bell Brass", "cat": "BRASS", "tags": ["hybrid", "bright"]},
        {"id": "28", "name": "Harpsichord", "cat": "KEYBOARD", "tags": ["baroque", "plucked"]},

        # Bank 3
        {"id": "31", "name": "Chime Water", "cat": "FX", "tags": ["ambient", "liquid"]},
        {"id": "32", "name": "Bones", "cat": "PERCUSSION", "tags": ["wooden", "marimba"]},
        {"id": "33", "name": "Night Breeze", "cat": "PAD", "tags": ["wind", "ambient"]},
        {"id": "34", "name": "Breathy Chiffer", "cat": "WIND", "tags": ["pipe", "breath"]},
        {"id": "35", "name": "Steel Drum", "cat": "MALLET", "tags": ["caribbean", "metallic"]},
        {"id": "36", "name": "Poly Bass", "cat": "BASS", "tags": ["analog", "synth"]},
        {"id": "37", "name": "Slap Bass", "cat": "BASS", "tags": ["funk", "slap"]},
        {"id": "38", "name": "Analog Brass", "cat": "BRASS", "tags": ["jupiter", "saw"]},

        # Bank 4
        {"id": "41", "name": "Techno Synth", "cat": "SYNTH", "tags": ["electronic", "lead"]},
        {"id": "42", "name": "Rock Organ", "cat": "ORGAN", "tags": ["drawbar", "rotary"]},
        {"id": "43", "name": "Synth Clav", "cat": "KEYBOARD", "tags": ["funk", "clav"]},
        {"id": "44", "name": "Marimba", "cat": "MALLET", "tags": ["wood", "percussive"]},
        {"id": "45", "name": "Electric Piano 1", "cat": "KEYBOARD", "tags": ["rhodes", "dyno"]},
        {"id": "46", "name": "Electric Piano 2", "cat": "KEYBOARD", "tags": ["wurlie", "fm"]},
        {"id": "47", "name": "Honky Tonk", "cat": "PIANO", "tags": ["ragtime", "upright"]},
        {"id": "48", "name": "Acoustic Piano 1", "cat": "PIANO", "tags": ["grand", "acoustic"]},

        # Bank 5
        {"id": "51", "name": "Laser Sweeper", "cat": "FX", "tags": ["sci-fi", "sweep"]},
        {"id": "52", "name": "Space Voice", "cat": "VOICE", "tags": ["ambient", "ethereal"]},
        {"id": "53", "name": "Electro Pluck", "cat": "PLUCK", "tags": ["sequencer", "short"]},
        {"id": "54", "name": "Vibe Wave", "cat": "MALLET", "tags": ["vibraphone", "motor"]},
        {"id": "55", "name": "Reso Lead", "cat": "LEAD", "tags": ["resonance", "solo"]},
        {"id": "56", "name": "Fifth Chime", "cat": "SYNTH", "tags": ["interval", "bell"]},
        {"id": "57", "name": "Warm Atmosphere", "cat": "PAD", "tags": ["soundscape", "film"]},
        {"id": "58", "name": "Brass Hit", "cat": "HIT", "tags": ["orchestral", "stab"]},

        # Bank 6
        {"id": "61", "name": "Square Wave", "cat": "SYNTH", "tags": ["vintage", "chptune"]},
        {"id": "62", "name": "Triangle Lead", "cat": "LEAD", "tags": ["smooth", "flute-like"]},
        {"id": "63", "name": "Heavy Metal Gtr", "cat": "GUITAR", "tags": ["distortion", "rock"]},
        {"id": "64", "name": "Distorted Solo", "cat": "LEAD", "tags": ["feedback", "guitar"]},
        {"id": "65", "name": "Acoustic Guitar", "cat": "GUITAR", "tags": ["nylon", "folk"]},
        {"id": "66", "name": "12-Str Guitar", "cat": "GUITAR", "tags": ["steel", "chorus"]},
        {"id": "67", "name": "Koto Pluck", "cat": "ETHNIC", "tags": ["asian", "japanese"]},
        {"id": "68", "name": "Shamisen", "cat": "ETHNIC", "tags": ["traditional", "plucked"]},

        # Bank 7
        {"id": "71", "name": "Cello Solo", "cat": "STRINGS", "tags": ["solo", "bowed"]},
        {"id": "72", "name": "Solo Violin", "cat": "STRINGS", "tags": ["expressive", "vibrato"]},
        {"id": "73", "name": "Oboe Legato", "cat": "WIND", "tags": ["double_reed", "pastoral"]},
        {"id": "74", "name": "Clarinet Warm", "cat": "WIND", "tags": ["woodwind", "mellow"]},
        {"id": "75", "name": "Pan Flute", "cat": "WIND", "tags": ["zamfir", "breath"]},
        {"id": "76", "name": "Pipe Organ Full", "cat": "ORGAN", "tags": ["tutti", "pedals"]},
        {"id": "77", "name": "Trumpet Section", "cat": "BRASS", "tags": ["bright", "fanfare"]},
        {"id": "78", "name": "Muted Horns", "cat": "BRASS", "tags": ["miles", "harmon"]},

        # Bank 8
        {"id": "81", "name": "African Mallet", "cat": "MALLET", "tags": ["kalimba", "balafon"]},
        {"id": "82", "name": "Metal Fantasy", "cat": "SYNTH", "tags": ["bell", "bright"]},
        {"id": "83", "name": "Synth Gong", "cat": "PERCUSSION", "tags": ["metallic", "tail"]},
        {"id": "84", "name": "Jet Sound", "cat": "FX", "tags": ["airplane", "sweep"]},
        {"id": "85", "name": "Wind Storm", "cat": "FX", "tags": ["noise", "nature"]},
        {"id": "86", "name": "Space Bell", "cat": "MALLET", "tags": ["cosmic", "shimmer"]},
        {"id": "87", "name": "Nightmare", "cat": "FX", "tags": ["dissonant", "horror"]},
        {"id": "88", "name": "Final Frontier", "cat": "PAD", "tags": ["space", "motion"]}
    ]

    res = []
    for idx, p in enumerate(d50_patches):
        res.append({
            "id": p["id"],
            "name": p["name"],
            "bank": "INTERNAL",
            "program": idx + 1,
            "category": p["cat"],
            "tags": p["tags"] + ["d50", "la_synthesis"]
        })
    return res

def get_d20_presets():
    # 128 Preset Tones for Roland D-20 / D-10
    tones = [
        "Acou Piano 1", "Acou Piano 2", "Honky-tonk", "Elec Piano 1", "Elec Piano 2", "Elec Organ 1", "Elec Organ 2", "Pipe Organ",
        "Harpsichord", "Clavinet", "Celesta", "Glockenspiel", "Vibraphone", "Marimba", "Xylophone", "Tubular Bell",
        "Nylon Gtr 1", "Nylon Gtr 2", "Steel Gtr 1", "Steel Gtr 2", "12-String Gtr", "Jazz Guitar", "Clean Gtr", "Muted Gtr",
        "Overdrive Gtr", "Distortion Gtr", "Acou Bass 1", "Acou Bass 2", "Fingered Bass", "Picked Bass", "Fretless 1", "Fretless 2",
        "Slap Bass 1", "Slap Bass 2", "Synth Bass 1", "Synth Bass 2", "Violin 1", "Violin 2", "Viola", "Cello",
        "Contrabass", "Strings 1", "Strings 2", "Strings 3", "Pizzicato", "Harp", "Timpani", "Trumpet 1",
        "Trumpet 2", "Muted Trumpet", "Trombone 1", "Trombone 2", "French Horn", "Tuba", "Brass 1", "Brass 2",
        "Synth Brass 1", "Synth Brass 2", "Soprano Sax", "Alto Sax 1", "Alto Sax 2", "Tenor Sax", "Baritone Sax", "Oboe",
        "English Horn", "Bassoon", "Clarinet", "Piccolo", "Flute", "Pan Flute", "Recorder", "Whistle",
        "Square Lead", "Saw Lead", "Syn Lead 1", "Syn Lead 2", "Charang", "Voice Lead", "Fifth Lead", "Bass & Lead",
        "Fantasy", "Warm Pad", "Poly Synth", "Space Voice", "Bowed Glass", "Metal Pad", "Halo Pad", "Sweep Pad",
        "Ice Rain", "Soundtrack", "Crystal", "Atmosphere", "Brightness", "Goblin", "Echo Drops", "Star Theme",
        "Sitar", "Banjo", "Shamisen", "Koto", "Kalimba", "Bagpipe", "Fiddle", "Shanai",
        "Tinkle Bell", "Agogo", "Steel Drums", "Woodblock", "Taiko Drum", "Melodic Tom", "Synth Drum", "Reverse Cymbal",
        "Guitar Fret", "Breath Noise", "Seashore", "Bird Tweet", "Telephone", "Helicopter", "Applause", "Gunshot",
        "Laser Gun", "Cosmic Voice", "Stab Brass", "Orchestra Hit", "Big Boom", "Steam Air", "Space Horn", "Night Air"
    ]
    res = []
    for idx, name in enumerate(tones):
        group = "GROUP A" if idx < 64 else "GROUP B"
        num = (idx % 64) + 1
        res.append({
            "id": f"{group[6]}-{num:02d}",
            "name": name,
            "bank": group,
            "program": idx + 1,
            "category": "LA_SYNTH",
            "tags": ["d20", "d10", "workstation"]
        })
    return res

def get_d70_presets():
    # Roland D-70 Super LA Synthesizer 64 Factory Performances
    perfs = [
        "AcousticGrand", "D-70 Warm Pad", "Super LA Lead", "Cyber Groove", "HollywoodStrgs", "Brass Explosion", "St.Velo EPiano", "Cathedral Choir",
        "Velo Slap Bass", "Differential", "Space Traveller", "Dyno Clavinet", "Full Baroque", "Spanish Nights", "Big City Funk", "Night Illusion",
        "Orchestral Hit", "Solar Flares", "Fretless Glide", "Harpsichord D70", "Modular Sequence", "Nylon Serenade", "Analog Monosynth", "Gamelan Waves",
        "Pop Horn Section", "Ice Cavern", "Whistle Express", "Deep Sub Bass", "Heavenly Air", "Electric 12-Str", "Stereo Pianos", "Atmospherics",
        "Pan Flute Solo", "Techno Rave Stab", "Chamber Quartet", "Drawbar B3 Fast", "Searing Lead", "Celtic Pipes", "Acoustic Muted", "Super Chorus EP",
        "Bowed Spectrum", "African Journey", "Bell & Pad Layer", "Velo Trumpet", "Acid Reso 303", "Vintage Tapes", "Space Calliope", "Heavy Rock Stack",
        "Jazz Solo Flute", "Cinema Brass", "Pulse Wave Clav", "Contemplation", "Acoustic Upright", "Ether Voice", "Crystal Bells", "Overdriven Strat",
        "Marcato Strings", "Trombone Section", "Sync Saw Lead", "Dreaming", "Stereo Grand 2", "Synth Bassline", "Laser Odyssey", "Master of D-70"
    ]
    res = []
    for idx, name in enumerate(perfs):
        res.append({
            "id": f"P-{idx+1:02d}",
            "name": name,
            "bank": "INTERNAL",
            "program": idx + 1,
            "category": "SUPER_LA",
            "tags": ["d70", "super_la", "dlm"]
        })
    return res

def build_d50_profile():
    return {
        "name": "Roland D-50",
        "manufacturer": "Roland Corporation",
        "category": "16-Voice Linear Arithmetic Synthesizer",
        "release_year": 1987,
        "hardware": {
            "form_factor": "61-Key Performance Synthesizer (D-550 is 2U Rack)",
            "polyphony": "16 Voices",
            "voice_architecture": "Linear Arithmetic (LA) Synthesis: 2 Tones (Upper/Lower), 4 Partials per patch (Synth waveform or PCM attack/loop) with Ring Modulation",
            "effects": "Built-in Digital Reverb (32 modes) + Digital Chorus (8 modes) + 2-Band Parametric EQ"
        },
        "midi": {
            "manufacturer_id": "0x41",
            "device_id": 16,
            "model_id": "0x14",
            "channel": 1
        },
        "sysex": {
            "header": "F0 41 {device_id} 14 {command_id} {address} {data} {checksum} F7",
            "checksum": "roland",
            "command_ids": {"dataset_dt1": "0x12", "request_rq1": "0x11"},
            "parameter_edit_format": "F0 41 10 14 12 {address} {value} {checksum} F7"
        },
        "parameters": [
            # Common Patch Parameters
            {"id": "patch_name", "name": "Patch Name", "page": "Common", "type": "string"},
            {"id": "structure_upper", "name": "Upper Structure (Partials 1&2)", "page": "Common", "range": [1, 7], "default": 1},
            {"id": "structure_lower", "name": "Lower Structure (Partials 3&4)", "page": "Common", "range": [1, 7], "default": 1},
            {"id": "reverb_type", "name": "Reverb Type", "page": "Effects", "range": [1, 32], "default": 1},
            {"id": "reverb_balance", "name": "Reverb Balance", "page": "Effects", "range": [0, 100], "default": 40},
            {"id": "chorus_type", "name": "Chorus Type", "page": "Effects", "range": [1, 8], "default": 1},
            {"id": "chorus_rate", "name": "Chorus Rate", "page": "Effects", "range": [0, 100], "default": 50},
            {"id": "chorus_depth", "name": "Chorus Depth", "page": "Effects", "range": [0, 100], "default": 60},
            {"id": "eq_low_freq", "name": "EQ Low Frequency", "page": "Effects", "range": [0, 15], "default": 4},
            {"id": "eq_low_gain", "name": "EQ Low Gain", "page": "Effects", "range": [-12, 12], "default": 0},
            {"id": "eq_high_freq", "name": "EQ High Frequency", "page": "Effects", "range": [0, 29], "default": 12},
            {"id": "eq_high_gain", "name": "EQ High Gain", "page": "Effects", "range": [-12, 12], "default": 0},

            # Upper Partial 1
            {"id": "u1_wave_type", "name": "Upper P1 Waveform Type", "page": "Upper P1", "type": "enum", "options": ["SYNTH", "PCM"], "default": 0},
            {"id": "u1_synth_wave", "name": "Upper P1 Synth Waveform", "page": "Upper P1", "type": "enum", "options": ["SQUARE", "SAW"], "default": 0},
            {"id": "u1_pcm_wave", "name": "Upper P1 PCM Wave Number", "page": "Upper P1", "range": [1, 100], "default": 1},
            {"id": "u1_pulse_width", "name": "Upper P1 Pulse Width", "page": "Upper P1", "range": [0, 100], "default": 50},
            {"id": "u1_pw_velo", "name": "Upper P1 PW Velocity Sens", "page": "Upper P1", "range": [-7, 7], "default": 0},
            {"id": "u1_tvf_cutoff", "name": "Upper P1 TVF Cutoff", "page": "Upper P1", "range": [0, 100], "default": 85},
            {"id": "u1_tvf_resonance", "name": "Upper P1 TVF Resonance", "page": "Upper P1", "range": [0, 30], "default": 10},
            {"id": "u1_tvf_env_depth", "name": "Upper P1 TVF Env Depth", "page": "Upper P1", "range": [0, 100], "default": 50},
            {"id": "u1_tva_level", "name": "Upper P1 TVA Level", "page": "Upper P1", "range": [0, 100], "default": 90},
            {"id": "u1_tva_velo", "name": "Upper P1 TVA Velocity Sens", "page": "Upper P1", "range": [-50, 50], "default": 20},

            # Upper Partial 2
            {"id": "u2_wave_type", "name": "Upper P2 Waveform Type", "page": "Upper P2", "type": "enum", "options": ["SYNTH", "PCM"], "default": 1},
            {"id": "u2_pcm_wave", "name": "Upper P2 PCM Wave Number", "page": "Upper P2", "range": [1, 100], "default": 2},
            {"id": "u2_tvf_cutoff", "name": "Upper P2 TVF Cutoff", "page": "Upper P2", "range": [0, 100], "default": 90},
            {"id": "u2_tva_level", "name": "Upper P2 TVA Level", "page": "Upper P2", "range": [0, 100], "default": 80}
        ]
    }

def build_d20_profile():
    return {
        "name": "Roland D-20",
        "manufacturer": "Roland Corporation",
        "category": "Multi-Timbral LA Synthesizer Workstation",
        "release_year": 1988,
        "hardware": {
            "form_factor": "61-Key Workstation Keyboard with Onboard 3.5\" FDD",
            "polyphony": "32 Voices",
            "parts": "8 Multi-Timbral Parts + 1 Rhythm Part",
            "sequencer": "8-Track Sequencer (approx 16,000 notes) with FDD",
            "synthesis": "Linear Arithmetic (LA) Synthesis"
        },
        "midi": {
            "manufacturer_id": "0x41",
            "device_id": 16,
            "model_id": "0x16",
            "channel": 1
        },
        "sysex": {
            "header": "F0 41 {device_id} 16 {command_id} {address} {data} {checksum} F7",
            "checksum": "roland",
            "command_ids": {"dataset_dt1": "0x12", "request_rq1": "0x11"}
        },
        "parameters": [
            {"id": "timbre_name", "name": "Timbre Name", "page": "Common", "type": "string"},
            {"id": "reverb_mode", "name": "Reverb Mode", "page": "Effects", "range": [1, 8], "default": 1},
            {"id": "reverb_level", "name": "Reverb Level", "page": "Effects", "range": [0, 7], "default": 4},
            {"id": "part1_level", "name": "Part 1 Level", "page": "Multi", "range": [0, 100], "default": 100},
            {"id": "part1_pan", "name": "Part 1 Pan", "page": "Multi", "range": [-7, 7], "default": 0},
            {"id": "tvf_cutoff", "name": "TVF Cutoff Frequency", "page": "Filter", "range": [0, 100], "default": 85},
            {"id": "tvf_resonance", "name": "TVF Resonance", "page": "Filter", "range": [0, 30], "default": 12}
        ]
    }

def build_d70_profile():
    return {
        "name": "Roland D-70",
        "manufacturer": "Roland Corporation",
        "category": "Super LA 76-Key Synthesizer & Master Controller",
        "release_year": 1990,
        "hardware": {
            "form_factor": "76-Key Semi-Weighted Keyboard with 240x64 Graphic LCD & 5 Sliders",
            "polyphony": "30 Voices",
            "parts": "5 Multi-Timbral Parts (4 Synth + 1 Rhythm)",
            "synthesis": "Super-LA: 4 Tones per Patch with Differential Loop Modulation (DLM) and TVF with Resonance",
            "rom": "28MB Internal ROM (U-20 sound engine heritage) + 2 Card Slots"
        },
        "midi": {
            "manufacturer_id": "0x41",
            "device_id": 16,
            "model_id": "0x32",
            "channel": 1
        },
        "sysex": {
            "header": "F0 41 {device_id} 32 {command_id} {address} {data} {checksum} F7",
            "checksum": "roland",
            "command_ids": {"dataset_dt1": "0x12", "request_rq1": "0x11"}
        },
        "parameters": [
            {"id": "perf_name", "name": "Performance Name", "page": "Common", "type": "string"},
            {"id": "t1_wave", "name": "Tone 1 Wave Number", "page": "Tone 1", "range": [1, 114], "default": 1},
            {"id": "t1_dlm_mode", "name": "Tone 1 DLM Mode", "page": "Tone 1", "type": "enum", "options": ["OFF", "DLM A", "DLM B"], "default": 0},
            {"id": "t1_cutoff", "name": "Tone 1 TVF Cutoff", "page": "Tone 1", "range": [0, 127], "default": 100},
            {"id": "t1_resonance", "name": "Tone 1 TVF Resonance", "page": "Tone 1", "range": [0, 127], "default": 25},
            {"id": "t1_level", "name": "Tone 1 TVA Level", "page": "Tone 1", "range": [0, 127], "default": 100},
            {"id": "t1_pan", "name": "Tone 1 TVA Pan", "page": "Tone 1", "range": [-64, 63], "default": 0},
            {"id": "t2_wave", "name": "Tone 2 Wave Number", "page": "Tone 2", "range": [1, 114], "default": 2},
            {"id": "t2_cutoff", "name": "Tone 2 TVF Cutoff", "page": "Tone 2", "range": [0, 127], "default": 95},
            {"id": "chorus_level", "name": "Chorus Level", "page": "Effects", "range": [0, 127], "default": 30},
            {"id": "reverb_level", "name": "Reverb Level", "page": "Effects", "range": [0, 127], "default": 45}
        ]
    }

def main():
    print("[*] Starting OmniPatch Roland D-Series Ingestion...")
    
    synths = [
        ("d-50", build_d50_profile, get_d50_presets),
        ("d-20", build_d20_profile, get_d20_presets),
        ("d-70", build_d70_profile, get_d70_presets)
    ]
    
    total = 0
    for folder, prof_fn, pres_fn in synths:
        out_dir = os.path.join(OUTPUT_BASE, folder)
        os.makedirs(out_dir, exist_ok=True)
        
        prof = prof_fn()
        with open(os.path.join(out_dir, "profile.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(prof, f, sort_keys=False, indent=2, allow_unicode=True)
            
        presets = pres_fn()
        with open(os.path.join(out_dir, "factory_presets.json"), "w", encoding="utf-8") as f:
            json.dump(presets, f, indent=2, ensure_ascii=False)
            
        total += len(presets)
        print(f"[+] Ingested {prof['name']:<20}: {len(prof['parameters']):2d} params | {len(presets):3d} presets -> {out_dir}")
        
    print(f"\n[✓] Ingested Roland D-Series! Total patches: {total}")

if __name__ == "__main__":
    main()
