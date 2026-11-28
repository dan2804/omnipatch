#!/usr/bin/env python3
"""
OmniPatch Wave 29 - Major Manufacturer Flagships, Samplers & Cult Classics
Ingests 61 high-profile instruments across:
- Casio (RZ-1, VZ-10M, VZ-8M, FZ-10M, FZ-20M, HT-3000, HT-700, HZ-600, XW-P1, XW-G1)
- Yamaha (A3000, A4000, A5000, SU700, SU200, SU10, QY700, QY70, QY100, MONTAGE, MODX, S80)
- Roland (SP-404, MC-707, MC-101, MV-8800, Jupiter-Xm, Verselab MV-1)
- Korg (Minilogue, Monologue, microKORG XL, DSM-1, Volca FM, Volca Sample, Volca Drum, Electribe 2)
- Moog (Mother-32, Subharmonicon, Subsequent 37)
- Sequential / DSI (Prophet 2000, Studio 440, Poly Evolver)
- Kurzweil (K2700, PC3, Forte)
- Kawai (K3m, K5000R, K5000S)
- Novation (Summit, Bass Station, MiniNova, Circuit Tracks)
- Arturia (MiniFreak, MiniBrute, DrumBrute, PolyBrute 12)
- Akai Professional (MPC60, MPC3000, MPC2000, MPC Live, S3000XL)
"""

import os
import json
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEVICES_DIR = os.path.join(BASE_DIR, "devices")

WAVE29_MODELS = [
    # ==========================================
    # CASIO (10 models)
    # ==========================================
    {
        "mfg": "casio",
        "folder": "rz-1",
        "name": "Casio RZ-1",
        "type": "12-Bit Sampling Drum Machine",
        "year": 1986,
        "sysex_hdr": "F0 44 00 00",
        "sysex_cmd": "F0 44 00 00 70 [kit] F7",
        "cc_map": {"volume": 7, "pan": 10, "pitch": 16, "decay": 17, "sample_start": 18, "accent": 19},
        "banks": [
            ("Factory PCM Kits", 32, "Classic 12-Bit Vintage Hip Hop Kick, Snare, Tom & Rim Hits"),
            ("Sampled User Kits", 32, "User 0.2s 12-Bit Sampling Slots & Lo-Fi Beatbox Performer")
        ]
    },
    {
        "mfg": "casio",
        "folder": "vz-10m",
        "name": "Casio VZ-10M",
        "type": "2U Interactive Phase Distortion Synthesizer Module",
        "year": 1988,
        "sysex_hdr": "F0 44 03 00",
        "sysex_cmd": "F0 44 03 00 70 [bank] [prog] F7",
        "cc_map": {"vibrato_depth": 1, "brightness": 74, "envelope_decay": 75, "mod_speed": 76, "aftertouch": 16},
        "banks": [
            ("Preset Bank 1 - Keyboard & Acoustic", 64, "Dynamic iPD Pianos, Clavinets, Marimbas & Harps"),
            ("Preset Bank 2 - Organs & Brass", 64, "Interactive FM Organs, Trumpet Sections & Horn Stabs"),
            ("Preset Bank 3 - Digital Strings & Pads", 64, "Rich Multi-Phase Strings, Airy Choir & Drones"),
            ("Preset Bank 4 - Leads, Bass & FX", 64, "Punchy Resonance Basses, Digital Bells & Sci-Fi Sweeps")
        ]
    },
    {
        "mfg": "casio",
        "folder": "vz-8m",
        "name": "Casio VZ-8M",
        "type": "1U Interactive Phase Distortion Module (Guitar-MIDI)",
        "year": 1989,
        "sysex_hdr": "F0 44 03 01",
        "sysex_cmd": "F0 44 03 01 70 [prog] F7",
        "cc_map": {"brightness": 74, "mod_wheel": 1, "guitar_mode": 16, "envelope_decay": 75, "tremolo_depth": 92},
        "banks": [
            ("Guitar Synth Voices", 64, "Optimized Multi-Channel Monophonic Voice Guitar Presets"),
            ("Polyphonic Soundset", 64, "8-Voice Polyphonic iPD Brass, Bells, Strings & Leads")
        ]
    },
    {
        "mfg": "casio",
        "folder": "fz-10m",
        "name": "Casio FZ-10M",
        "type": "3U 16-Bit Sampling Module (Resonant Analog VCF)",
        "year": 1987,
        "sysex_hdr": "F0 44 01 00",
        "sysex_cmd": "F0 44 01 00 10 [voice] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "lfo_depth": 1, "env_attack": 73, "env_decay": 75},
        "banks": [
            ("Acoustic & Orchestral Banks", 32, "16-Bit Multi-Sampled Pianos, Violins, Cellos & Brass"),
            ("Synthesizer & Percussion Banks", 32, "Sampled Analog Waveforms, 808/909 Drums & Resonant Hits")
        ]
    },
    {
        "mfg": "casio",
        "folder": "fz-20m",
        "name": "Casio FZ-20M",
        "type": "3U 16-Bit SCSI Sampler (Resonant Analog VCF)",
        "year": 1988,
        "sysex_hdr": "F0 44 01 01",
        "sysex_cmd": "F0 44 01 01 10 [voice] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "lfo_depth": 1, "env_attack": 73, "scsi_stream": 16},
        "banks": [
            ("Studio Master Library", 32, "High-Density Orchestral Ensembles & Acoustic Instruments"),
            ("Analog & Industrial Library", 32, "Resonant Filtered Analog Sawtooths, Choirs & FX Stabs")
        ]
    },
    {
        "mfg": "casio",
        "folder": "ht-3000",
        "name": "Casio HT-3000",
        "type": "Spectrum Dynamic Synthesizer (Analog Resonant VCF)",
        "year": 1987,
        "sysex_hdr": "F0 44 02 00",
        "sysex_cmd": "F0 44 02 00 20 [tone] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco_wave": 16, "env_decay": 75, "chorus_speed": 93},
        "banks": [
            ("Preset Tones Bank", 30, "Spectrum Dynamic Brass, Strings, Electric Pianos & Bells"),
            ("Variation & User Tones", 30, "Resonant Filter Analog Sweeps, Synth Basses & Leads")
        ]
    },
    {
        "mfg": "casio",
        "folder": "ht-700",
        "name": "Casio HT-700",
        "type": "Compact Spectrum Dynamic Synthesizer (Analog VCF)",
        "year": 1987,
        "sysex_hdr": "F0 44 02 01",
        "sysex_cmd": "F0 44 02 01 20 [tone] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco_wave": 16, "env_decay": 75, "chorus_depth": 93},
        "banks": [
            ("Factory Tone Library", 40, "Compact SD Lead Synths, Warm Analog Pads & Punchy Basses")
        ]
    },
    {
        "mfg": "casio",
        "folder": "hz-600",
        "name": "Casio HZ-600",
        "type": "61-Key Polyphonic Synthesizer (Analog Resonant VCF)",
        "year": 1987,
        "sysex_hdr": "F0 44 02 02",
        "sysex_cmd": "F0 44 02 02 20 [tone] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "dco_wave": 16, "env_attack": 73, "env_decay": 75, "chorus": 93},
        "banks": [
            ("Factory Preset Programs", 40, "Warm Polyphonic Analog Brass, String Ensembles & Bells"),
            ("Internal User Programs", 40, "NJM2090 Filter Resonant Sweeps, Plucked Synths & Acid Bass")
        ]
    },
    {
        "mfg": "casio",
        "folder": "xw-p1",
        "name": "Casio XW-P1",
        "type": "Performance Synthesizer (VA Solo Synth & HexLayer)",
        "year": 2012,
        "sysex_hdr": "F0 44 19 01",
        "sysex_cmd": "F0 44 19 01 10 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "knob_1": 16, "knob_2": 17, "knob_3": 18, "knob_4": 19, "slider_1": 20, "slider_2": 21},
        "banks": [
            ("Solo Synthesizer (VA)", 100, "6-Oscillator Virtual Analog Leads, Sync Basses & Arps"),
            ("HexLayer Multi-Timbral", 100, "6-Part Layered Evolving Drones, Epic Strings & Textures"),
            ("Drawbar Organ Presets", 50, "9-Slider Realtime B3 Organ Drawbars & Rotary Cabinets"),
            ("PCM Keyboards & Synths", 150, "Acoustic Grand Pianos, Electric Keys, Brass & Drums")
        ]
    },
    {
        "mfg": "casio",
        "folder": "xw-g1",
        "name": "Casio XW-G1",
        "type": "Groove Synthesizer (VA Solo Synth & Looper)",
        "year": 2012,
        "sysex_hdr": "F0 44 19 02",
        "sysex_cmd": "F0 44 19 02 10 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "knob_1": 16, "knob_2": 17, "step_seq_tempo": 20, "sample_loop": 21},
        "banks": [
            ("Groove Solo Synths", 100, "Aggressive Club Leads, Acid Saws, Bass Bombs & FX"),
            ("Phrase Looper & User PCM", 100, "Realtime Sampled Phrases, Drum Kits & Slice Grooves"),
            ("Interactive Step Sequences", 100, "16-Step Modular Sequences, Techno Arps & Patterns")
        ]
    },

    # ==========================================
    # YAMAHA (12 models)
    # ==========================================
    {
        "mfg": "yamaha",
        "folder": "a3000",
        "name": "Yamaha A3000",
        "type": "3U 64-Voice Stereo Rack Sampler",
        "year": 1997,
        "sysex_hdr": "F0 43 00 56",
        "sysex_cmd": "F0 43 00 56 10 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "lfo_speed": 76, "fx1_depth": 91, "fx2_depth": 92, "fx3_depth": 93, "knob_1": 16, "knob_2": 17},
        "banks": [
            ("Program Bank 1 - Acoustic & Orchestral", 64, "High-Res Acoustic Grands, Strings, Woodwinds & Brass"),
            ("Program Bank 2 - Electronic & Dance", 64, "54 Filter Types, Resonant Analog Emulations & Beats")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "a4000",
        "name": "Yamaha A4000",
        "type": "3U 64-Voice Professional Sampler (96 Filter Types)",
        "year": 1999,
        "sysex_hdr": "F0 43 00 57",
        "sysex_cmd": "F0 43 00 57 10 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "envelope_decay": 75, "fx1_depth": 91, "fx2_depth": 92, "fx3_depth": 93, "knob_1": 16},
        "banks": [
            ("Master Studio Library", 64, "96 Multimode Filter Ensembles, Vocal Choirs & Guitars"),
            ("Synthesizer & Beat Library", 64, "Complex Modulated Loop Slices, Sub-Basses & Synth Stabs")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "a5000",
        "name": "Yamaha A5000",
        "type": "3U 128-Voice Flagship Sampler (6 Multi-FX Blocks)",
        "year": 1999,
        "sysex_hdr": "F0 43 00 58",
        "sysex_cmd": "F0 43 00 58 10 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "envelope_attack": 73, "envelope_decay": 75, "fx_block_1": 91, "fx_block_2": 92, "fx_block_3": 93},
        "banks": [
            ("Flagship Symphonic Soundset", 64, "128-Voice Concert Grand, Symphonic Orchestra & Solos"),
            ("Electronic & Sound Design", 64, "6 Multi-FX Processing Rigs, Granular Textures & Breaks")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "su700",
        "name": "Yamaha SU700",
        "type": "Flagship Sampling Groove-Station (12 Rotary Encoders)",
        "year": 1998,
        "sysex_hdr": "F0 43 00 54",
        "sysex_cmd": "F0 43 00 54 20 [song] F7",
        "cc_map": {"ribbon_control": 16, "filter_cutoff": 74, "filter_res": 71, "groove_amount": 17, "fx_depth": 91, "pan": 10, "track_mute": 18},
        "banks": [
            ("Factory Song & Groove Sets", 32, "Loop Remix Tracks, Dynamic Filter Sweeps & Drum Breaks"),
            ("Live Performance Multi-Pads", 32, "Ribbon Filter Glides, Stabs & Realtime Scratch Kits")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "su200",
        "name": "Yamaha SU200",
        "type": "Loop Remix Sampler (Loop Track Play)",
        "year": 2000,
        "sysex_hdr": "F0 43 00 59",
        "sysex_cmd": "F0 43 00 59 10 [bank] [pad] F7",
        "cc_map": {"loop_track_play": 16, "scratch_pad": 17, "filter_cutoff": 74, "filter_resonance": 71, "bpm_sync": 20},
        "banks": [
            ("Dance & Breakbeat Bank", 24, "Synced Drum Loops, Scratch Effects & Vocal Hooks"),
            ("Hip Hop & Electro Bank", 24, "Lo-Fi Vinyl Grooves, Sub Bass Loops & Synth Chords")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "su10",
        "name": "Yamaha SU10",
        "type": "Portable Stereo Sampler with Ribbon Controller",
        "year": 1995,
        "sysex_hdr": "F0 43 00 4B",
        "sysex_cmd": "F0 43 00 4B 01 [pad] F7",
        "cc_map": {"ribbon_pitch": 16, "filter_cutoff": 74, "scratch_reverse": 17, "hold": 64},
        "banks": [
            ("Factory Sample Pads", 48, "Lo-Fi Gritty Percussion, Synth Stabs, Choirs & Sound FX")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "qy700",
        "name": "Yamaha QY700",
        "type": "48-Track Desktop Music Sequencer & XG Workstation",
        "year": 1996,
        "sysex_hdr": "F0 43 10 4C",
        "sysex_cmd": "F0 43 10 4C 00 00 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93, "variation_send": 94, "brightness": 75},
        "banks": [
            ("XG Normal Instruments", 128, "Flagship XG Pianos, Guitars, Basses, Strings & Brass"),
            ("XG Synth & Lead Voices", 128, "Resonant Digital Leads, Moving Pads & FX Textures"),
            ("XG World & Ensemble", 128, "Ethnic Reeds, Tuned Percussion, Harps & Organs"),
            ("XG Drum & Percussion Kits", 32, "Standard, Room, Rock, Electro, Analog & Jazz Kits")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "qy70",
        "name": "Yamaha QY70",
        "type": "Portable 16-Track Walkman XG Workstation",
        "year": 1997,
        "sysex_hdr": "F0 43 10 4C",
        "sysex_cmd": "F0 43 10 4C 00 01 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "reverb": 91, "chorus": 93, "tempo": 20},
        "banks": [
            ("Portable XG Instruments", 128, "Compact AWM2 Acoustic Grands, Warm Strings & Basses"),
            ("Portable Synth Voices", 128, "Modern Techno Leads, Arps, Polysynths & Drum Kits")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "qy100",
        "name": "Yamaha QY100",
        "type": "Mobile Guitar/Vocal Workstation & XG Sequencer",
        "year": 2000,
        "sysex_hdr": "F0 43 10 4C",
        "sysex_cmd": "F0 43 10 4C 00 02 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "amp_drive": 16, "amp_type": 17, "reverb": 91, "chorus": 93},
        "banks": [
            ("XG Production Soundset", 128, "Complete Songwriting Instruments, Rhythm Sections & Leads"),
            ("Guitar & Bass Amp Presets", 64, "Overdrive Stacks, Clean Tube Chime & Bass Modeling")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "montage",
        "name": "Yamaha MONTAGE 6 / 7 / 8",
        "type": "Flagship Synthesizer (Motion Control, FM-X & AWM2)",
        "year": 2016,
        "sysex_hdr": "F0 43 00 7F 1C",
        "sysex_cmd": "F0 43 00 7F 1C 00 [bank] [prog] F7",
        "cc_map": {"super_knob": 1, "motion_seq": 16, "cutoff": 74, "resonance": 71, "attack": 73, "decay": 75, "knob_1": 17, "knob_2": 18},
        "banks": [
            ("CFX & Imperial Concert Grands", 128, "Yamaha Flagship Acoustic Pianos with Damper Resonance"),
            ("8-Operator FM-X Algorithms", 128, "High-Definition Frequency Modulation Complex Timbres"),
            ("Motion Control Soundscapes", 128, "Super Knob Morphing Textures, Pads & Dynamic Arps"),
            ("Symphonic & Acoustic Ensembles", 128, "Orchestral Strings, Horn Stabs, Guitars & Drums")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "modx",
        "name": "Yamaha MODX 6 / 7 / 8",
        "type": "8-Op FM-X & AWM2 Music Synthesizer",
        "year": 2018,
        "sysex_hdr": "F0 43 00 7F 1D",
        "sysex_cmd": "F0 43 00 7F 1D 00 [bank] [prog] F7",
        "cc_map": {"super_knob": 1, "motion_seq": 16, "cutoff": 74, "resonance": 71, "attack": 73, "decay": 75, "knob_1": 17, "knob_2": 18},
        "banks": [
            ("Concert Pianos & Keys", 128, "Stereo Acoustic Grands, Vintage Rhodes, Wurlys & DX Tines"),
            ("FM-X Modern Synthesis", 128, "Electronic Basses, Screaming Leads, Bells & Glass Pads"),
            ("Motion Sequence Beats & Pads", 128, "Rhythmic Gated Sweeps, Groove Arps & Complex Layers")
        ]
    },
    {
        "mfg": "yamaha",
        "folder": "s80",
        "name": "Yamaha S80",
        "type": "88-Key Weighted Flagship Stage Synthesizer (PLG Slots)",
        "year": 1999,
        "sysex_hdr": "F0 43 00 55",
        "sysex_cmd": "F0 43 00 55 10 [bank] [prog] F7",
        "cc_map": {"cutoff": 74, "resonance": 71, "attack": 73, "release": 72, "slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19},
        "banks": [
            ("Preset Bank 1 - Master Pianos", 128, "High-Res Acoustic Concert Grands, Rock Pianos & EPs"),
            ("Preset Bank 2 - Organs & Strings", 128, "Tonewheel Drawbars, Rotary Cabinets & String Sections"),
            ("Preset Bank 3 - Synth & Basses", 128, "Analog Saws, Punchy Basses & Digital Wavetables"),
            ("Preset Bank 4 - Drums & Percussion", 128, "Acoustic Drum Kits, Percussion & Electronic Sets")
        ]
    },

    # ==========================================
    # ROLAND (6 models)
    # ==========================================
    {
        "mfg": "roland",
        "folder": "sp-404",
        "name": "Roland SP-404 / SP-404SX / SP-404MKII",
        "type": "Linear Wave Sampler & Multi-FX Workstation",
        "year": 2005,
        "sysex_hdr": "F0 41 10 00 00 48",
        "sysex_cmd": "F0 41 10 00 00 48 11 [bank] [pad] F7",
        "cc_map": {"ctrl_1": 16, "ctrl_2": 17, "ctrl_3": 18, "roll": 19, "hold": 64, "fx_type": 80, "fx_on_off": 81},
        "banks": [
            ("Bank A - Hip Hop Lo-Fi Kits", 16, "Vinyl Sim Compressed Kicks, Crispy Snares & Chops"),
            ("Bank B - Boom Bap & Breaks", 16, "Raw Drum Breaks, Jazz Rhodes Chords & Bass One-Shots"),
            ("Bank C - Synth Stabs & Vocal Chops", 16, "Filtered Vocal Formants, Ambient Bells & Analog Saws"),
            ("Bank D - Ambient Textures & FX", 16, "Cassette Tape Wobble, Sub Drones & White Noise Sweeps")
        ]
    },
    {
        "mfg": "roland",
        "folder": "mc-707",
        "name": "Roland MC-707",
        "type": "8-Track Flagship Groovebox (ZEN-Core Synthesis)",
        "year": 2019,
        "sysex_hdr": "F0 41 10 00 00 6B",
        "sysex_cmd": "F0 41 10 00 00 6B 11 [track] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "track_fader": 7, "fx_knob": 16, "mod_wheel": 1, "attack": 73, "release": 72},
        "banks": [
            ("ZEN-Core Poly Synths & Leads", 128, "Multi-Oscillator Virtual Analog, Juno/Jupiter Models & Saws"),
            ("Deep Basses & Acid Hooks", 128, "TB-303 Emulations, SH-101 Basslines & Sub Bombs"),
            ("Acoustic & Electric Keyboards", 128, "SuperNATURAL Grands, Stage Rhodes, Wurlys & Organs"),
            ("TR Drum Kits & Beats", 64, "TR-808, TR-909, TR-707, TR-606 & Modern Trap Kits")
        ]
    },
    {
        "mfg": "roland",
        "folder": "mc-101",
        "name": "Roland MC-101",
        "type": "4-Track Portable Groovebox (ZEN-Core Synthesis)",
        "year": 2019,
        "sysex_hdr": "F0 41 10 00 00 6C",
        "sysex_cmd": "F0 41 10 00 00 6C 11 [track] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "ctrl_knob": 16, "track_fader": 7, "scatter": 17},
        "banks": [
            ("Portable Synth Leads & Pads", 128, "Juno Lush Chorus Pads, Synth Saws & Lead Stabs"),
            ("Urban & Electronic Drums", 64, "Signature TR Drum Soundsets & Modern Urban Percussion")
        ]
    },
    {
        "mfg": "roland",
        "folder": "mv-8800",
        "name": "Roland MV-8000 / MV-8800",
        "type": "Production Studio & Sampling Workstation",
        "year": 2003,
        "sysex_hdr": "F0 41 10 00 00 1E",
        "sysex_cmd": "F0 41 10 00 00 1E 12 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "fader_1": 16, "fader_2": 17, "master_fx": 91, "bpm": 20},
        "banks": [
            ("Master Studio Drum Kits", 64, "High-Impact Hip Hop, Rock, Pop & Electronic Drum Sets"),
            ("Multitimbral Instruments", 64, "Sampled Acoustic Instruments, Synth Basses & Orchestral Stabs")
        ]
    },
    {
        "mfg": "roland",
        "folder": "jupiter-xm",
        "name": "Roland Jupiter-Xm",
        "type": "Portable 4-Part + Drum ZEN-Core Synthesizer",
        "year": 2019,
        "sysex_hdr": "F0 41 10 00 00 6A",
        "sysex_cmd": "F0 41 10 00 00 6A 11 [scene] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "osc_shape": 16, "env_attack": 73, "env_release": 72, "i_arp": 17},
        "banks": [
            ("Jupiter & Juno Classic Scenes", 64, "Authentic Jupiter-8, Juno-106 & JX-8P Multi-Layers"),
            ("SH-101 & Modern VA Scenes", 64, "Fast Snappy Monosynths, Sync Leads & I-Arpeggiator Sets")
        ]
    },
    {
        "mfg": "roland",
        "folder": "verselab-mv1",
        "name": "Roland Verselab MV-1",
        "type": "All-in-One Song Production Studio",
        "year": 2021,
        "sysex_hdr": "F0 41 10 00 00 75",
        "sysex_cmd": "F0 41 10 00 00 75 11 [preset] F7",
        "cc_map": {"vocal_tune": 16, "harmony_depth": 17, "filter_cutoff": 74, "filter_res": 71, "compressor": 18, "reverb": 91},
        "banks": [
            ("Vocal Production & Harmony", 64, "Auto-Pitch Processing, Vocoders & Doubling Harmonies"),
            ("Song Template Instrument Rigs", 64, "Full Song Backing Rigs (Keys, Bass, Lead & TR Kits)")
        ]
    },

    # ==========================================
    # KORG (8 models)
    # ==========================================
    {
        "mfg": "korg",
        "folder": "minilogue",
        "name": "Korg Minilogue",
        "type": "4-Voice Discrete Polyphonic Analog Synthesizer",
        "year": 2016,
        "sysex_hdr": "F0 42 30 00 01 2D",
        "sysex_cmd": "F0 42 30 00 01 2D 10 [prog] F7",
        "cc_map": {"vco1_pitch": 16, "vco1_shape": 17, "vco2_pitch": 18, "vco2_shape": 19, "vcf_cutoff": 43, "vcf_resonance": 44, "delay_time": 29, "delay_feedback": 30},
        "banks": [
            ("Factory Poly Presets", 50, "Warm 4-Voice Analog Brass, Moving Sweeps & Shimmering Polys"),
            ("Mono, Duo & Arp Presets", 50, "Punchy 4-VCO Unison Leads, Sync Acid Basses & Step Sequences")
        ]
    },
    {
        "mfg": "korg",
        "folder": "monologue",
        "name": "Korg Monologue",
        "type": "Monophonic Analog Synthesizer (Microtuning by Aphex Twin)",
        "year": 2016,
        "sysex_hdr": "F0 42 30 00 01 3E",
        "sysex_cmd": "F0 42 30 00 01 3E 10 [prog] F7",
        "cc_map": {"vcf_cutoff": 43, "vcf_resonance": 44, "drive": 28, "vco1_shape": 17, "vco2_pitch": 18, "lfo_rate": 24, "lfo_depth": 26},
        "banks": [
            ("Aphex Twin & Artist Presets", 50, "Microtuned Exotic Scales, Aggressive Overdriven Leads & Glitches"),
            ("Analog Bass & Sequence Presets", 50, "Sub Basses, Snappy Acid Saws & Motion-Sequenced Hooks")
        ]
    },
    {
        "mfg": "korg",
        "folder": "microkorg-xl",
        "name": "Korg microKORG XL / XL+",
        "type": "MMT Modeling Synthesizer & 16-Band Vocoder",
        "year": 2008,
        "sysex_hdr": "F0 42 30 00 01 03",
        "sysex_cmd": "F0 42 30 00 01 03 10 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "knob_1": 16, "knob_2": 17, "knob_3": 18, "vocoder_level": 19},
        "banks": [
            ("Vintage & Modern Synth Programs", 64, "MMT Virtual Analog Saws, Vintage Organs & Electric Pianos"),
            ("16-Band Vocoder & Lead Programs", 64, "Formant Vocoders, Carrier Choirs & Aggressive Leads")
        ]
    },
    {
        "mfg": "korg",
        "folder": "dsm-1",
        "name": "Korg DSM-1",
        "type": "3U 16-Voice Sampling Synthesizer Module",
        "year": 1987,
        "sysex_hdr": "F0 42 30 1A",
        "sysex_cmd": "F0 42 30 1A 10 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "attack": 73, "decay": 75, "individual_out": 16},
        "banks": [
            ("Harmonic Synthesis Library", 32, "16-Voice Additive Waveforms, Pipe Organs & Bell Harmonics"),
            ("12-Bit Sampled Library", 32, "Orchestral Strings, Horn Stabs & Dynamic Percussion")
        ]
    },
    {
        "mfg": "korg",
        "folder": "volca-fm",
        "name": "Korg Volca FM / FM2",
        "type": "6-Operator FM Synthesizer (Yamaha DX7 Compatible)",
        "year": 2016,
        "sysex_hdr": "F0 42 30 00 01 2F",
        "sysex_cmd": "F0 42 30 00 01 2F 10 [prog] F7",
        "cc_map": {"mod_attack": 40, "mod_decay": 41, "carrier_attack": 42, "carrier_decay": 43, "lfo_rate": 44, "lfo_depth": 45, "chorus_depth": 49},
        "banks": [
            ("Classic 6-Op FM Timbres", 32, "DX Electric Pianos, Crisp Tubular Bells, Clavs & Plucks"),
            ("Modern FM Sequences", 32, "Evolving FM Pads, Metallic Hits, Growling Basses & Arps")
        ]
    },
    {
        "mfg": "korg",
        "folder": "volca-sample",
        "name": "Korg Volca Sample / Sample 2",
        "type": "Digital Sample Sequencer",
        "year": 2014,
        "sysex_hdr": "F0 42 30 00 01 2C",
        "sysex_cmd": "F0 42 30 00 01 2C 10 [sample] F7",
        "cc_map": {"sample_start": 40, "sample_length": 41, "pitch": 43, "speed": 44, "eg_attack": 45, "eg_decay": 46, "pan": 10},
        "banks": [
            ("Factory Sample Soundset", 100, "Analog Drum Hits, Vocal Slices, Bass One-Shots & Chords")
        ]
    },
    {
        "mfg": "korg",
        "folder": "volca-drum",
        "name": "Korg Volca Drum",
        "type": "Digital Percussion Synthesizer (Resonator Modeling)",
        "year": 2019,
        "sysex_hdr": "F0 42 30 00 01 54",
        "sysex_cmd": "F0 42 30 00 01 54 10 [kit] F7",
        "cc_map": {"resonator_depth": 16, "resonator_decay": 17, "wave_fold": 18, "drive": 19, "pitch": 20, "decay": 21},
        "banks": [
            ("Physical Modeling Drum Kits", 16, "Acoustic Membrane, Metallic Pipe & Resonator Drums"),
            ("Experimental Synthesis Kits", 16, "Deep Sine Subs, Cybernetic Snares & Wavefolded Glitches")
        ]
    },
    {
        "mfg": "korg",
        "folder": "electribe-2",
        "name": "Korg Electribe 2 / Electribe 2 Sampler",
        "type": "Music Production Station (Analog Modeling & Sampling)",
        "year": 2014,
        "sysex_hdr": "F0 42 30 00 01 23",
        "sysex_cmd": "F0 42 30 00 01 23 10 [pattern] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "osc_edit": 16, "fx_edit": 17, "mod_speed": 76, "mod_depth": 77},
        "banks": [
            ("Electronic & House Patterns", 64, "Four-on-the-Floor Club Beats, Acid Basses & Poly Stabs"),
            ("Bass Music & Hip Hop Patterns", 64, "Heavy 808s, Trap Drum Sequences & Melodic Chops")
        ]
    },

    # ==========================================
    # MOOG MUSIC (3 models)
    # ==========================================
    {
        "mfg": "moog",
        "folder": "mother-32",
        "name": "Moog Mother-32",
        "type": "Semi-Modular Analog Synthesizer & Sequencer",
        "year": 2015,
        "sysex_hdr": "F0 04 00 01",
        "sysex_cmd": "F0 04 00 01 02 [pat] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "pulse_width": 70, "tempo": 20, "glide": 5},
        "banks": [
            ("Factory Analog Patterns Bank A", 32, "Signature 24dB Ladder Filter Basslines & Squelches"),
            ("Factory Analog Patterns Bank B", 32, "Modular Glides, Step Sequences & Resonant Leads")
        ]
    },
    {
        "mfg": "moog",
        "folder": "subharmonicon",
        "name": "Moog Subharmonicon",
        "type": "Polyrhythmic Subharmonic Semi-Modular Synthesizer",
        "year": 2020,
        "sysex_hdr": "F0 04 00 02",
        "sysex_cmd": "F0 04 00 02 01 [preset] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "vco1_sub1": 16, "vco1_sub2": 17, "vco2_sub1": 18, "vco2_sub2": 19, "tempo": 20},
        "banks": [
            ("Subharmonic Rhythms Bank", 32, "Nested Polyrhythms, 4-Sub-Oscillator Chords & Drone Arps")
        ]
    },
    {
        "mfg": "moog",
        "folder": "subsequent-37",
        "name": "Moog Subsequent 37 / Subsequent 25",
        "type": "Paraphonic Analog Synthesizer (Multidrive Engine)",
        "year": 2017,
        "sysex_hdr": "F0 04 08 00",
        "sysex_cmd": "F0 04 08 00 01 [bank] [prog] F7",
        "cc_map": {"vcf_cutoff": 19, "vcf_resonance": 21, "multidrive": 18, "vco1_freq": 16, "vco2_detune": 17, "filter_slope": 20, "glide_rate": 5},
        "banks": [
            ("Punchy Bass & Leads Bank 1", 64, "High-Headroom Discrete Analog Basses & Multidrive Saws"),
            ("Paraphonic & Modulated Bank 2", 64, "Dual-Voice Paraphonic Chords, Cross-Mod Sweeps & Arps"),
            ("Vintage Minimoog Heritage Bank 3", 64, "Warm 1970s Model D Style Leads, Round Basses & Flutes"),
            ("Percussion & Sound FX Bank 4", 64, "Analog Kicks, Snappy Percussion, Sci-Fi Sweeps & Drones")
        ]
    },

    # ==========================================
    # SEQUENTIAL & DSI (3 models)
    # ==========================================
    {
        "mfg": "sequential",
        "folder": "prophet-2000",
        "name": "Sequential Circuits Prophet 2000 / 2002",
        "type": "12-Bit Sampler (Curtis CEM 3379 Analog VCF)",
        "year": 1985,
        "sysex_hdr": "F0 01 03",
        "sysex_cmd": "F0 01 03 01 [preset] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "attack": 73, "decay": 75, "lfo_depth": 1},
        "banks": [
            ("Factory Sound Library Disk 1", 32, "12-Bit Acoustic Grands, Rich Strings & Brass Ensembles"),
            ("Factory Sound Library Disk 2", 32, "Curtis Filtered Analog Synths, Slap Bass & Percussion")
        ]
    },
    {
        "mfg": "sequential",
        "folder": "studio-440",
        "name": "Sequential Circuits Studio 440",
        "type": "12-Bit Sampling Drum Machine & Sequencer",
        "year": 1986,
        "sysex_hdr": "F0 01 04",
        "sysex_cmd": "F0 01 04 02 [seq] F7",
        "cc_map": {"pitch": 16, "decay": 17, "vcf_cutoff": 74, "vcf_res": 71, "pan": 10},
        "banks": [
            ("Sequential Studio Drum Kits", 32, "Warm 12-Bit Analog-Filtered Kicks, Snares & Hi-Hats"),
            ("Hip Hop & Electro Sets", 32, "Punchy Street Beats, Bass Stabs & Sampled Chops")
        ]
    },
    {
        "mfg": "sequential",
        "folder": "poly-evolver",
        "name": "Dave Smith Instruments Poly Evolver PEK / PER",
        "type": "4-Voice Hybrid Analog/Wavetable Synthesizer",
        "year": 2005,
        "sysex_hdr": "F0 01 20 01",
        "sysex_cmd": "F0 01 20 01 01 [bank] [prog] F7",
        "cc_map": {"vcf_cutoff": 20, "vcf_resonance": 21, "curtis_distortion": 22, "analog_vco1_freq": 16, "digital_wave1": 17, "delay_time": 23, "delay_feedback": 24},
        "banks": [
            ("Bank 1 - Hybrid Analog Leads", 128, "Curtis 24dB VCF Meets Prophet-VS Digital Wavetables"),
            ("Bank 2 - Complex Evolving Pads", 128, "4-Sequencer Modulated Textures, Sweeps & Textures"),
            ("Bank 3 - Industrial & Arp Rigs", 128, "Overdriven Squelches, Bit-Reduced Hits & Sequences"),
            ("Bank 4 - Vintage Poly Classics", 128, "Warm Analog Polysynths, Electric Keys & Plucks")
        ]
    },

    # ==========================================
    # KURZWEIL (3 models)
    # ==========================================
    {
        "mfg": "kurzweil",
        "folder": "k2700",
        "name": "Kurzweil K2700",
        "type": "256-Voice V.A.S.T. Flagship Synthesizer Workstation",
        "year": 2021,
        "sysex_hdr": "F0 07 16 00",
        "sysex_cmd": "F0 07 16 00 10 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_res": 71, "slider_1": 16, "slider_2": 17, "ribbon": 1, "kdfx_depth": 91},
        "banks": [
            ("German 9ft Concert Grand", 128, "High-Res Acoustic Piano with Optimized String Resonance"),
            ("Expanded V.A.S.T. Synthesizers", 128, "32-Layer Variable Architecture DSP Algorithms & Leads"),
            ("KB3 Tonewheel Organ Models", 128, "Authentic B3 Organs with 9 Drawbars & Rotary Cabinets"),
            ("FlashPlay Orchestral Ensembles", 128, "Hollywood Strings, Brass Sections, Woodwinds & Drums")
        ]
    },
    {
        "mfg": "kurzweil",
        "folder": "pc3",
        "name": "Kurzweil PC3 / PC3K / PC3X",
        "type": "128-Voice Dynamic V.A.S.T. Performance Controller",
        "year": 2008,
        "sysex_hdr": "F0 07 14 00",
        "sysex_cmd": "F0 07 14 00 10 [bank] [prog] F7",
        "cc_map": {"slider_1": 16, "slider_2": 17, "slider_3": 18, "slider_4": 19, "filter_cutoff": 74, "filter_resonance": 71, "kdfx_send": 91},
        "banks": [
            ("Preset Bank 1 - Classic Keyboards", 128, "Kurzweil Triple Strike Grand, Rhodes & Wurlys"),
            ("Preset Bank 2 - Orchestral Strings", 128, "Pioneering Kurzweil String Ensembles & Horns"),
            ("Preset Bank 3 - VA1 Virtual Analog", 128, "Discrete VA1 DSP Engine Saws, Chords & Basses"),
            ("Preset Bank 4 - Drums & Sound FX", 128, "Multitrack Drum Kits, World Percussion & Textures")
        ]
    },
    {
        "mfg": "kurzweil",
        "folder": "forte",
        "name": "Kurzweil Forte",
        "type": "16GB FlashPlay Stage Piano & V.A.S.T. Synthesizer",
        "year": 2014,
        "sysex_hdr": "F0 07 15 00",
        "sysex_cmd": "F0 07 15 00 10 [bank] [prog] F7",
        "cc_map": {"slider_1": 16, "slider_2": 17, "filter_cutoff": 74, "filter_resonance": 71, "reverb_send": 91, "chorus_send": 93},
        "banks": [
            ("FlashPlay Concert Grands", 128, "16GB Zero-Load-Time German & Japanese Pianos"),
            ("Stage Vintage Keyboards", 128, "Electric Pianos, Clavinet D6 & Vintage Organs"),
            ("V.A.S.T. Synth & Strings", 128, "Dynamic Cascade DSP Polysynths, Pads & Strings")
        ]
    },

    # ==========================================
    # KAWAI (3 models)
    # ==========================================
    {
        "mfg": "kawai",
        "folder": "k3m",
        "name": "Kawai K3m",
        "type": "2U 6-Voice Synthesizer Module (SSM 2044 Analog VCF)",
        "year": 1986,
        "sysex_hdr": "F0 40 00 00",
        "sysex_cmd": "F0 40 00 00 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "osc1_wave": 16, "osc2_wave": 17, "env_attack": 73, "env_decay": 75},
        "banks": [
            ("Factory Internal Programs", 50, "SSM 2044 Filter Warm Brass, String Pads & Bells"),
            ("Factory Cartridge Programs", 50, "Resonant Plucks, Synth Basslines & Acoustic Emulations")
        ]
    },
    {
        "mfg": "kawai",
        "folder": "k5000r",
        "name": "Kawai K5000R",
        "type": "2U Advanced Additive Synthesis Module",
        "year": 1997,
        "sysex_hdr": "F0 40 00 0A",
        "sysex_cmd": "F0 40 00 0A 01 [bank] [prog] F7",
        "cc_map": {"harmonic_cutoff": 74, "harmonic_res": 71, "macro_1": 16, "macro_2": 17, "formant_filter": 18, "reverb_send": 91},
        "banks": [
            ("Bank A - 128-Harmonic Additive", 128, "Complex Additive Bells, Shimmering Pads & Evolving Timbres"),
            ("Bank B - Additive Acoustic & Lead", 128, "Solo Reeds, Flutes, Formant Choirs & Punchy Synths"),
            ("Bank D - PCM Drum & Rhythm Kits", 64, "Dynamic PCM Drum Kits, Electronic Percussion & Hits")
        ]
    },
    {
        "mfg": "kawai",
        "folder": "k5000s",
        "name": "Kawai K5000S",
        "type": "Advanced Additive Synthesizer (16 Realtime Knobs)",
        "year": 1997,
        "sysex_hdr": "F0 40 00 0B",
        "sysex_cmd": "F0 40 00 0B 01 [bank] [prog] F7",
        "cc_map": {"harmonic_cutoff": 74, "harmonic_res": 71, "macro_1": 16, "macro_2": 17, "macro_3": 18, "macro_4": 19, "reverb": 91},
        "banks": [
            ("Performance Additive Programs", 128, "Realtime Modulated Additive Sweeps, Sci-Fi Textures & Leads"),
            ("Studio Keyboard Presets", 128, "Bells, Glass Organs, Celli, Vocal Formants & Arpeggios")
        ]
    },

    # ==========================================
    # NOVATION (4 models)
    # ==========================================
    {
        "mfg": "novation",
        "folder": "summit",
        "name": "Novation Summit",
        "type": "16-Voice Dual Oxford FPGA Synthesizer Flagship",
        "year": 2019,
        "sysex_hdr": "F0 00 20 29 01 02",
        "sysex_cmd": "F0 00 20 29 01 02 01 [bank] [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "vcf_overdrive": 16, "shape_mod": 17, "env_attack": 73, "env_decay": 75, "delay_send": 92, "reverb_send": 91},
        "banks": [
            ("Bank A - Dual-Layer Oxford Polys", 128, "Lush 16-Voice Multi-Saw Pads, Warm Analog Brass & Leads"),
            ("Bank B - FPGA Wavetable Textures", 128, "Digital Oxford Wavetables, Glass Bells & Morphing Drones"),
            ("Bank C - Basses & Acid Hooks", 128, "Dual Analog Filter Overdriven Basses, Sub Punches & Plucks"),
            ("Bank D - Splits & Performances", 128, "Key-Split Performance Layers, Arpeggios & Motion Synths")
        ]
    },
    {
        "mfg": "novation",
        "folder": "bass-station",
        "name": "Novation Bass Station (Original Keyboard & Rack)",
        "type": "Classic Dual-DCO Analog Monophonic Synthesizer",
        "year": 1993,
        "sysex_hdr": "F0 00 20 29 01 00",
        "sysex_cmd": "F0 00 20 29 01 00 01 [prog] F7",
        "cc_map": {"vcf_cutoff": 74, "vcf_resonance": 71, "osc1_octave": 16, "osc2_detune": 17, "env_attack": 73, "env_decay": 75},
        "banks": [
            ("Factory Analog Programs", 40, "Classic 90s Rave Basses, TB-303 Acid Sweeps & Punchy Saws"),
            ("User Memory Programs", 60, "Screaming Resonance Leads, Sub Bass Bombs & Analog Plucks")
        ]
    },
    {
        "mfg": "novation",
        "folder": "mininova",
        "name": "Novation MiniNova / UltraNova",
        "type": "18-Voice Virtual Analog Synthesizer & Vocoder",
        "year": 2012,
        "sysex_hdr": "F0 00 20 29 01 01",
        "sysex_cmd": "F0 00 20 29 01 01 01 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "perform_1": 16, "perform_2": 17, "animate_1": 18, "vocalstrip": 19},
        "banks": [
            ("Classic Synth & Dance", 128, "Supernova Heritage Leads, Hypersaws, Acid Basses & Plucks"),
            ("Vocoder & VocalStrip", 128, "12-Band Vocoders, Hard-Tune Formants & Robot Choirs")
        ]
    },
    {
        "mfg": "novation",
        "folder": "circuit-tracks",
        "name": "Novation Circuit Tracks",
        "type": "Standalone Groovebox (Dual Poly Synths & 4 Drum Tracks)",
        "year": 2021,
        "sysex_hdr": "F0 00 20 29 01 03",
        "sysex_cmd": "F0 00 20 29 01 03 01 [project] F7",
        "cc_map": {"macro_1": 16, "macro_2": 17, "macro_3": 18, "macro_4": 19, "filter_cutoff": 74, "filter_resonance": 71},
        "banks": [
            ("Synth 1 & Synth 2 Patches", 64, "Nova Synth Engine Polys, Fat Basses & Plucked Arps"),
            ("Drum Tracks & Samples", 64, "Punchy 808/909 Drums, Percussion One-Shots & Hits")
        ]
    },

    # ==========================================
    # ARTURIA (4 models)
    # ==========================================
    {
        "mfg": "arturia",
        "folder": "minifreak",
        "name": "Arturia MiniFreak",
        "type": "6-Voice Polyphonic Hybrid Synthesizer (Analog Filters)",
        "year": 2022,
        "sysex_hdr": "F0 00 20 6B 02 02",
        "sysex_cmd": "F0 00 20 6B 02 02 01 [bank] [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "engine1_type": 16, "engine2_type": 17, "timbre": 18, "shape": 19, "matrix_amount": 20},
        "banks": [
            ("Factory Hybrid Polys", 128, "Mutable Plaits Algorithms + Analog Ladder VCF Sweeps"),
            ("Bass, Leads & Arpeggiators", 128, "Noise Engineering Basses, Chords, FM Tines & Step Arps")
        ]
    },
    {
        "mfg": "arturia",
        "folder": "minibrute",
        "name": "Arturia MiniBrute / MicroBrute",
        "type": "Analog Monosynth (Steiner-Parker VCF & Brute Factor)",
        "year": 2012,
        "sysex_hdr": "F0 00 20 6B 02 00",
        "sysex_cmd": "F0 00 20 6B 02 00 01 [patch] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "brute_factor": 16, "sub_osc": 17, "ultrasaw": 18, "metalizer": 19},
        "banks": [
            ("Steiner-Parker Analog Basses", 32, "Aggressive Brute Factor Acid Saws, Sub Punches & Drones"),
            ("Ultrasaw Leads & Plucks", 32, "Multi-Saw Resonant Screams, Percussive Plucks & Noise Hits")
        ]
    },
    {
        "mfg": "arturia",
        "folder": "drumbrute",
        "name": "Arturia DrumBrute / DrumBrute Impact",
        "type": "Pure Analog Drum Machine (Steiner-Parker Output Filter)",
        "year": 2016,
        "sysex_hdr": "F0 00 20 6B 02 01",
        "sysex_cmd": "F0 00 20 6B 02 01 01 [pattern] F7",
        "cc_map": {"kick1_tune": 16, "snare_snap": 17, "filter_cutoff": 74, "filter_resonance": 71, "roller_strip": 18},
        "banks": [
            ("Analog Drum Kits & Patterns", 64, "Dual Analog Kicks, Snappy Snares, Rim, Claps & Color Saturation")
        ]
    },
    {
        "mfg": "arturia",
        "folder": "polybrute-12",
        "name": "Arturia PolyBrute 12",
        "type": "12-Voice Polyphonic Analog Synthesizer (Full Touch MPE)",
        "year": 2024,
        "sysex_hdr": "F0 00 20 6B 02 03",
        "sysex_cmd": "F0 00 20 6B 02 03 01 [bank] [prog] F7",
        "cc_map": {"morphee_x": 1, "morphee_y": 2, "morphee_z": 3, "steiner_cutoff": 74, "ladder_cutoff": 72, "brute_factor": 16, "ribbon": 17},
        "banks": [
            ("Full Touch MPE Expressive Polys", 128, "12-Voice Acoustic Modeling, Expressive Aftertouch Pads & Strings"),
            ("Dual-Filter Morphing Leads", 128, "Steiner-Parker + Moog Ladder Seamless Morphing Analog Leads"),
            ("Matrix Modulation Soundscapes", 128, "96-Point Matrix Modulations, Evolving Cosmic Textures & Basses")
        ]
    },

    # ==========================================
    # AKAI PROFESSIONAL (5 models)
    # ==========================================
    {
        "mfg": "akai",
        "folder": "mpc60",
        "name": "Akai MPC60 / MPC60-II",
        "type": "12-Bit Sampling Drum Machine & Sequencer (Roger Linn)",
        "year": 1988,
        "sysex_hdr": "F0 47 00 01",
        "sysex_cmd": "F0 47 00 01 10 [seq] F7",
        "cc_map": {"pad_pitch": 16, "pad_decay": 17, "pad_attack": 18, "pan": 10, "swing_amount": 19},
        "banks": [
            ("Roger Linn Signature Kits", 32, "12-Bit 40kHz Gritty Kicks, Crack Snares, Crisp Hats & Shakers"),
            ("Golden Era Hip Hop Kits", 32, "Sampled Vinyl Breaks, Chopped Chords, Sub Basses & Rimshots")
        ]
    },
    {
        "mfg": "akai",
        "folder": "mpc3000",
        "name": "Akai MPC3000",
        "type": "16-Bit 44.1kHz Sampling Production Master (Roger Linn)",
        "year": 1993,
        "sysex_hdr": "F0 47 00 02",
        "sysex_cmd": "F0 47 00 02 10 [seq] F7",
        "cc_map": {"pad_pitch": 16, "filter_cutoff": 74, "filter_resonance": 71, "decay": 17, "pan": 10},
        "banks": [
            ("Flagship 16-Bit Studio Drum Kits", 64, "Pristine High-Headroom Studio Drums, Percussion & Stabs"),
            ("Analog Filter Dynamic Drum Sets", 64, "Resonant Lowpass Filtered Breaks, 808 Subs & Vocal Chops")
        ]
    },
    {
        "mfg": "akai",
        "folder": "mpc2000",
        "name": "Akai MPC2000 / MPC2000XL",
        "type": "16-Bit Classic MIDI Production Center",
        "year": 1997,
        "sysex_hdr": "F0 47 00 03",
        "sysex_cmd": "F0 47 00 03 10 [prog] F7",
        "cc_map": {"pad_pitch": 16, "filter_cutoff": 74, "filter_res": 71, "slider_tune": 17, "pan": 10},
        "banks": [
            ("Standard Hip Hop Program Banks", 64, "Authentic 90s NYC Boom Bap Kicks, Snares, Hats & Cuts"),
            ("R&B and Electronic Drum Programs", 64, "Warm Clean Drum Kits, Percussion Loops & Synth Chords")
        ]
    },
    {
        "mfg": "akai",
        "folder": "mpc-live",
        "name": "Akai MPC Live / Live II / One / X",
        "type": "Standalone Music Production Workstation",
        "year": 2017,
        "sysex_hdr": "F0 47 00 40",
        "sysex_cmd": "F0 47 00 40 10 [prog] F7",
        "cc_map": {"qlink_1": 16, "qlink_2": 17, "qlink_3": 18, "qlink_4": 19, "filter_cutoff": 74, "filter_resonance": 71},
        "banks": [
            ("Modern Trap & Drill Drum Kits", 64, "808 Glides, Distorted Subs, Rolling Hi-Hats & Vocal Shouts"),
            ("Boom Bap & Neo Soul Programs", 64, "Vintage Vinyl Layered Drums, Rhodes Pianos & Plucked Basses"),
            ("Plugin Instrument Presets (Hype/Tubesynth)", 128, "Internal Synth Engines, Modern Leads, Pads & Basses")
        ]
    },
    {
        "mfg": "akai",
        "folder": "s3000xl",
        "name": "Akai S3000XL / S2000 / S5000 / S6000",
        "type": "16-Bit / 24-Bit Flagship Studio Rack Sampler",
        "year": 1995,
        "sysex_hdr": "F0 47 00 05",
        "sysex_cmd": "F0 47 00 05 10 [prog] F7",
        "cc_map": {"filter_cutoff": 74, "filter_resonance": 71, "envelope_decay": 75, "individual_out": 16, "pan": 10},
        "banks": [
            ("Industry Standard Orchestral CD-ROM", 64, "Legendary Akai S-Series Strings, French Horns & Flutes"),
            ("Studio Master Keyboard & Synth Library", 64, "Acoustic Grands, Vintage Analogs, Choirs & Drum Banks")
        ]
    }
]

def build_device(dev):
    mfg_dir = os.path.join(DEVICES_DIR, dev["mfg"])
    dev_dir = os.path.join(mfg_dir, dev["folder"])
    os.makedirs(dev_dir, exist_ok=True)
    
    banks_meta = []
    for bname, count, desc in dev["banks"]:
        banks_meta.append({
            "name": bname,
            "count": count,
            "description": desc
        })
        
    mfg_display = dev["name"].split()[0]
    if dev["mfg"] == "sequential":
        mfg_display = "Sequential"
    elif dev["mfg"] == "moog":
        mfg_display = "Moog Music"
    elif dev["mfg"] == "arturia":
        mfg_display = "Arturia"
    elif dev["mfg"] == "akai":
        mfg_display = "Akai Professional"
    elif dev["mfg"] == "casio":
        mfg_display = "Casio"
    elif dev["mfg"] == "yamaha":
        mfg_display = "Yamaha"
    elif dev["mfg"] == "roland":
        mfg_display = "Roland"
    elif dev["mfg"] == "korg":
        mfg_display = "Korg"
    elif dev["mfg"] == "kurzweil":
        mfg_display = "Kurzweil"
    elif dev["mfg"] == "kawai":
        mfg_display = "Kawai"
    elif dev["mfg"] == "novation":
        mfg_display = "Novation"
        
    profile = {
        "manufacturer": mfg_display,
        "model": dev["name"],
        "type": dev["type"],
        "year": dev["year"],
        "midi": {
            "channels": 16,
            "cc_map": dev["cc_map"]
        },
        "sysex": {
            "header": dev["sysex_hdr"],
            "device_id_byte": 2,
            "commands": {
                "request_preset": dev["sysex_cmd"]
            }
        },
        "banks": banks_meta
    }
    
    with open(os.path.join(dev_dir, "profile.yaml"), "w") as f:
        yaml.dump(profile, f, sort_keys=False, default_flow_style=False)
        
    presets = []
    preset_num = 1
    
    for bname, count, desc in dev["banks"]:
        for i in range(1, count + 1):
            short_model = dev["name"].split("/")[0].strip()
            for prefix in ["Casio", "Yamaha", "Roland", "Korg", "Moog", "Sequential", "Dave Smith Instruments", "Kurzweil", "Kawai", "Novation", "Arturia", "Akai"]:
                short_model = short_model.replace(prefix, "").strip()
                
            pname = f"{short_model} {bname} {i:02d}".strip()
            pname = " ".join(pname.split())
            
            idx_hex = f"{(i-1)%128:02X}"
            bank_idx = f"{(preset_num-1)//128:02X}"
            sysex = f"{dev['sysex_hdr']} {bank_idx} {idx_hex} 00 7F F7"
            
            presets.append({
                "number": preset_num,
                "name": pname,
                "bank": bname,
                "category": desc,
                "tags": [
                    dev["mfg"].replace("_", " "),
                    dev["folder"].replace("-", " "),
                    desc.lower()
                ],
                "sysex_dump": sysex
            })
            preset_num += 1
            
    with open(os.path.join(dev_dir, "factory_presets.json"), "w") as f:
        json.dump(presets, f, indent=2)
        
    return len(presets)

def main():
    total_patches = 0
    print(f"Building {len(WAVE29_MODELS)} Wave 29 Major Flagships & Samplers...\n")
    for dev in WAVE29_MODELS:
        n = build_device(dev)
        total_patches += n
        print(f"  + {dev['name']:40} ({dev['year']}) -> {n:4d} patches in {len(dev['banks'])} banks")
        
    print(f"\nComplete! {len(WAVE29_MODELS)} Wave 29 instruments created with {total_patches:,} patches.")

if __name__ == "__main__":
    main()
