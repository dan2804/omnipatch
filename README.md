# OmniPatch

> **Universal Cross-Platform MIDI/SysEx Librarian & Synthesizer Patch Editor in Rust**  
> Inspired by Sound Quest's **Midi Quest 13**, crafted with an authentic **Windows 8 Metro UI Modern Studio** experience.  
> Fully compatible with **Windows, macOS, Linux, FreeBSD, and OpenBSD**.

OmniPatch is a high-performance, modular patch librarian and hardware editor written in Rust. It combines a clean, typography-driven **Windows 8 Modern UI** (flat design, zero neon glow, 90-degree geometry, live tiles, collapsible manufacturer menus) with deep hardware-tailored sound engines for 27 legendary vintage analog, virtual analog, phase distortion, and digital rackmount synthesizers.

![OmniPatch Windows 8 Metro UI Studio Hub](assets/screenshots/studio_hub.png)

---

## Key Features

- **Authentic Windows 8 Metro UI Studio:**
  - **Collapsible Manufacturer Menus:** Sidebar hierarchy cleanly grouping instruments under **E-MU Systems**, **Casio Computer Co.**, **Access Music**, and **Akai Professional**, featuring quick `EXP` (Expand All) and `COL` (Collapse All) toggles and auto-reveal on search.
  - **Live Tile Start Screen:** Horizontal Windows 8 panoramic start board with live parameter readouts, family grouping, and quick launch tiles.
  - **Universal Patch Librarian:** Instant cross-synth searching and filtering, live auditioning, and real-time SysEx hexadecimal packet telemetry inspector.
  - **Interactive 2D Filter & Vector Curve Canvas:** Real-time log-frequency response visualization with interactive cutoff and resonance control.
  - **Low-Latency Web Audio Engine:** Reactive auditioning soundboard tiles and interactive synthesizer engines with real-time waveform generation.
- **Cross-Platform Rust Core:** High-performance, memory-safe engine running natively across desktop platforms using `midir` and `rusqlite`.
- **Declarative Device Profiles (`.yaml`):** Adding support for a new synthesizer requires zero Rust recompilation—simply drop a YAML definition file and JSON preset dump into `devices/`.
- **Hardware-Safe Pacing & Buffer Throttling:** Configurable inter-byte and inter-block millisecond delays designed specifically to prevent UART buffer overflows on vintage 8-bit and 16-bit microcontrollers (e.g. Motorola 68000, 6809, and Intel 8031).
- **Embedded SQLite Librarian (`rusqlite`):** High-speed local patch database indexing binary `.syx` blobs, categories, bank indices, ROM IDs, and user tags with instant full-text search.
- **Automated Manual Ingestion Pipeline:** Built-in PDF extraction and NLP utility scans manufacturer service manuals, extracts MIDI Implementation Charts and SysEx specification tables, and generates structured profiles.

---

## Supported Synthesizers (228 Production Profiles)

OmniPatch ships with 228 comprehensive device profiles across 39 legendary synthesizer manufacturers:

| Synthesizer | Manufacturer | Architecture | Parameters | Presets | SysEx ID / Details |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **OSC OSCar** | Oxford Synthesiser Co. | Additive / Analog Synthesizer Masterpiece | 5 | 36 | `0x00 0x00 0x2F` · Chris Huggett additive waveforms, dual 12dB filters with separation & drive |
| **Cheetah MS6** | Cheetah Marketing | 6-Voice Multitimbral Analog Module | 5 | 64 | `0x24` · Dual DCOs per voice, CEM3396 analog VCF chips, multitimbral |
| **Crumar Bit One / 99 / 01** | Crumar | Polyphonic Analog Synthesizer | 5 | 75 | `0x27` · Dual DCOs, CEM3328 resonant analog lowpass VCF, Italian warmth |
| **Siel Opera 6 / DK600** | Siel | 6-Voice Polyphonic Analog Synthesizer | 4 | 95 | `0x21` · Dual DCOs, SSM2044 24dB resonant analog filters, Italian poly |
| **UDO Audio Super 6 / Gemini** | UDO Audio | Binaural 12-Voice Polyphonic Synthesizer | 6 | 128 | `0x00 0x21 0x4B` · Binaural stereo spatial spread, FPGA DDS oscillators, SSI2144 VCF |
| **Black Corp Deckard's Dream** | Black Corporation | 8-Voice Polyphonic Analog Synthesizer | 5 | 256 | `0x00 0x21 0x3F` · Dual discrete analog voice cards inspired by the Yamaha CS-80 |
| **Pioneer DJ / DSI Toraiz AS-1** | Pioneer DJ | Monophonic Analog Synthesizer | 6 | 495 | `0x01` (ID `0x2F`) · Discrete analog Prophet-6 single-voice architecture, 5 banks |
| **Pioneer DJ / DSI Toraiz SP-16**| Pioneer DJ | Professional Sampler & Step Sequencer | 3 | 128 | `0x01` (ID `0x2E`) · Dave Smith discrete Prophet-6 analog lowpass and highpass filters |
| **TC Electronic 2290** | TC Electronic | Dynamic Digital Delay + Multi-FX | 5 | 100 | `0x00 0x20 0x1F` · The definitive studio dynamic delay processor, ducking, chorus |
| **Strymon BigSky** | Strymon | Multidimensional Reverb Processor | 6 | 300 | `0x00 0x01 0x55` · Cloud, Shimmer, Bloom, Chorale, Magneto, Reflections, 150 banks |
| **Strymon TimeLine** | Strymon | Multidimensional Delay Processor | 7 | 300 | `0x00 0x01 0x55` · dTape, dBucket, Ice shimmer delay, Dual, Pattern, Lo-Fi, 150 banks |
| **Eventide Rose / PitchFactor** | Eventide | Modulated Delay & Pitch Processor | 6 | 100 | `0x1C` (ID `0x05`) · Analog-digital hybrid modulated delay, pitch shifting, reverse |
| **Korg Mono/Poly MP-4** | Korg | 4-VCO Analog Synthesizer | 7 | 64 | `0x42` (ID `0x00`) · 4 discrete VCOs, cycling arpeggiator, SSM2044 resonant filter |
| **Korg Polysix PS-6** | Korg | 6-Voice Polyphonic Analog Synthesizer | 5 | 64 | `0x42` (ID `0x02`) · Discrete analog VCOs, SSM2044 VCF, built-in BBD ensemble chorus |
| **Korg Poly-800** | Korg | Programmable Polyphonic Synthesizer | 5 | 64 | `0x42` (ID `0x06`) · 8 DCOs paraphonic, Digital Envelope Generators (DEG), portable |
| **Waldorf Quantum / Iridium** | Waldorf Music | Flagship Hybrid Synthesizer | 5 | 1,000 | `0x3E` (ID `0x16`) · 5 synthesis engines: Wavetable, Particle, Resonator, Kernel FM |
| **Waldorf Kyra** | Waldorf Music | 128-Voice FPGA Virtual Analog | 5 | 1,024 | `0x3E` (ID `0x17`) · 128 voices, 8 parts, 32x oversampled audio, Hypersaw, 8 banks |
| **Waldorf M** | Waldorf Music | Wavetable Synth w/ Analog Filters | 5 | 512 | `0x3E` (ID `0x18`) · Microwave I/II heritage, SSI2144 24dB analog VCF, 4 banks |
| **Moog One (8/16 Voice)** | Moog Music | Flagship Polyphonic Analog Synthesizer | 8 | 1,024 | `0x04` (ID `0x07`) · Tri-timbral, 3 VCOs per voice, dual filters (SVF + ladder), Eventide FX |
| **Moog Matriarch** | Moog Music | 4-Voice Paraphonic Semi-Modular | 5 | 64 | `0x04` (ID `0x08`) · 4-voice paraphony, dual stereo ladder filters, stereo analog BBD delay |
| **Moog Grandmother** | Moog Music | Semi-Modular Analog Synthesizer | 4 | 64 | `0x04` (ID `0x09`) · Built-in real spring reverb tank, dual analog oscillators, sequencer |
| **Sequential Take 5** | Sequential Circuits | 5-Voice Polyphonic Analog Synthesizer | 5 | 256 | `0x01` (ID `0x34`) · Dual analog VCOs, 4-pole Prophet-5 resonant lowpass filter, Vintage knob |
| **Sequential Trigon-6** | Sequential Circuits | 6-Voice 3-VCO Analog Synthesizer | 7 | 500 | `0x01` (ID `0x35`) · 3 discrete VCOs per voice, switchable 2/4-pole ladder filter, 5 banks |
| **Arturia PolyBrute** | Arturia | 6-Voice Analog Morphing Synthesizer | 8 | 768 | `0x00 0x20 0x6B` · Seamless A/B sound morphing, dual filters (Steiner + Ladder), Morphée |
| **Arturia MatrixBrute** | Arturia | Flagship Analog Monophonic Synth | 5 | 256 | `0x00 0x20 0x6B` · 16x16 modulation matrix, 3 analog VCOs, Steiner + Ladder filters |
| **Arturia MicroFreak** | Arturia | Algorithmic Hybrid Synthesizer | 6 | 384 | `0x00 0x20 0x6B` · Mutable Instruments Plaits engines, analog filter, touch keyboard |
| **Arturia MiniBrute 2 / 2S** | Arturia | Semi-Modular Analog Synthesizer | 5 | 64 | `0x00 0x20 0x6B` · 48-point CV/Gate patchbay, Steiner-Parker filter, Brute Factor |
| **Elektron Digitakt** | Elektron | 8-Voice Drum Computer & Sampler | 5 | 128 | `0x00 0x20 0x3C` · 8 audio tracks, parameter locks, multi-mode filter, overdrive |
| **Elektron Digitone** | Elektron | 8-Voice Polyphonic Digital FM | 5 | 256 | `0x00 0x20 0x3C` · 4-operator FM engine, subtractive resonant filter, overdrive, 2 banks |
| **Elektron Syntakt** | Elektron | 12-Track Drum Computer & Synthesizer | 5 | 128 | `0x00 0x20 0x3C` · 8 digital + 4 analog drum/synth machines, analog drive/filter block |
| **Elektron Analog Four / Rytm** | Elektron | 4-Voice Discrete Analog Synthesizer | 5 | 256 | `0x00 0x20 0x3C` · 4 discrete analog voices, dual analog filters, analog overdrive, 2 banks |
| **Roland TB-303 Bass Line** | Roland Corporation | Definitive Acid Synthesizer & Sequencer | 6 | 64 | `0x41` · Diode ladder filter, resonant slide/accent, 4 pattern groups |
| **Roland TR-808 Rhythm Composer**| Roland Corporation | Analog Rhythm Composer Flagship | 5 | 64 | `0x41` · Bridged-T resonant kick, snappy snare, claps, congas, cowbell |
| **Roland TR-909 Rhythm Composer**| Roland Corporation | Analog/Sample Hybrid Rhythm Composer | 5 | 96 | `0x41` · Punchy analog kick/snare + 6-bit sampled cymbals/hats, 6 banks |
| **Roland TR-707 / TR-727** | Roland Corporation | Digital Rhythm Composer | 2 | 64 | `0x41` · Classic 80s Chicago house digital drums, 4 pattern banks |
| **Roland SH-101** | Roland Corporation | Monophonic Analog Synthesizer | 5 | 64 | `0x41` · CEM3340 VCO, IR3109 cascade VCF, red/blue/grey classic |
| **Roland System-8** | Roland Corporation | Plug-Out Synthesizer Flagship | 5 | 512 | `0x41` · ACB modeling, Jupiter-8, Juno-106, JX-3P plug-outs, 8 banks |
| **Roland SE-02** | Roland Corporation | Analog Synthesizer Module | 6 | 384 | `0x41` · 3 discrete analog VCOs, ladder filter, Studio Electronics colab |
| **Roland Integra-7** | Roland Corporation | SuperNATURAL Sound Module Flagship | 5 | 2,048 | `0x41` · 16 SuperNATURAL banks, all 12 SRX expansion boards built-in |
| **Yamaha CS-80** | Yamaha Corporation | 8-Voice Polyphonic Analog Synthesizer | 5 | 48 | `0x43` · Dual 8-voice signal paths, polyphonic aftertouch, ribbon, Vangelis |
| **Yamaha FS1R** | Yamaha Corporation | 8-Op Formant Shaping Synthesizer | 6 | 1,408 | `0x43` (ID `0x5E`) · 8-operator FM + 8 unvoiced formants, Fseq, 12 banks |
| **Yamaha SY99** | Yamaha Corporation | Advanced RCM Hybrid Music Workstation | 3 | 144 | `0x43` (ID `0x2C`) · AFM 6-operator FM + AWM2 sample RAM, dual filters |
| **Yamaha EX5 / EX7** | Yamaha Corporation | Extended Synthesis Flagship Workstation | 5 | 256 | `0x43` (ID `0x4C`) · AWM2, AN virtual analog, VL physical modeling, FDSP |
| **Yamaha VL1 / VL70-m** | Yamaha Corporation | Virtual Acoustic Physical Modeling | 4 | 128 | `0x43` (ID `0x3C`) · Acoustic waveguide modeling of woodwinds, brass, strings |
| **Korg Kronos / Nautilus** | Korg | 9-Engine Music Workstation Flagship | 5 | 1,536 | `0x42` (ID `0x68`) · SGX-2, EP-1, CX-3, MS-20EX, Polysix, AL-1, MOD-7, STR-1 |
| **Korg minilogue xd** | Korg | 4-Voice Hybrid Analog Synthesizer | 6 | 500 | `0x42` (ID `0x51`) · 2 analog VCOs + Multi-Engine (VPM/User), 5 banks |
| **Korg prologue 8 / 16** | Korg | Polyphonic Analog Synthesizer Flagship | 6 | 500 | `0x42` (ID `0x4B`) · Discrete analog VCOs + digital Multi Engine, 5 banks |
| **Korg opsix** | Korg | Altered FM Synthesizer | 8 | 500 | `0x42` (ID `0x59`) · 6-operator matrix faders/knobs, 40 operator algorithms |
| **Korg wavestate** | Korg | Wave Sequencing Synthesizer | 6 | 500 | `0x42` (ID `0x57`) · Wave Sequencing 2.0, Lanes (Sample, Timing, Pitch, Shape) |
| **Korg modwave** | Korg | Wavetable Synthesizer | 5 | 500 | `0x42` (ID `0x5A`) · Wavetables, Kaoss Physics, Motion Sequencing 2.0, 5 banks |
| **Korg KingKORG** | Korg | eXpanded Modeling Technology Synthesizer | 5 | 300 | `0x42` (ID `0x32`) · XMT modeling, vacuum tube overdrive, vintage filter models |
| **Peavey DPM 3 / DPM V3** | Peavey | Digital Phase Modulation Synthesizer | 3 | 100 | `0x1B` (ID `0x00`) · 16-bit PCM synthesis, dual resonant digital filters |
| **Peavey Spectrum Series** | Peavey | 1U Classic Sound Module (Bass/Synth/Organ)| 3 | 200 | `0x1B` (ID `0x01`) · Dedicated classic bass, synth, and organ sound modules |
| **Dreadbox Typhon** | Dreadbox | Analog Monophonic Synth w/ Sinevibes | 6 | 128 | `0x00 0x21 0x44` · Pure analog signal path with Sinevibes digital stereo FX |
| **Dreadbox Erebus** | Dreadbox | Paraphonic Analog Synthesizer | 4 | 64 | `0x00 0x21 0x44` · Dual analog VCOs, 2-pole lowpass filter, lo-fi delay |
| **Kurzweil K2000 / K2000R** | Kurzweil | V.A.S.T. Workstation Synthesizer | 5 | 200 | `0x07` (ID `0x00`) · Variable Architecture Synthesis Technology, 31 algorithms, DSP |
| **Kurzweil K2500 / K2500R** | Kurzweil | 48-Voice V.A.S.T. Production Synthesizer | 5 | 300 | `0x07` (ID `0x00`) · KDFX studio effects, 48 voices, 200 programs + 100 setups |
| **Kurzweil K2600 / K2600R** | Kurzweil | Triple Modular Processing V.A.S.T. Flagship | 5 | 300 | `0x07` (ID `0x00`) · Triple Modular processing, 8 sliders, dual ribbon controllers |
| **Eventide H3000 Ultra-Harmonizer**| Eventide | Studio Pitch Harmonizer & Multi-Effects | 5 | 1,000 | `0x1C` (ID `0x01`) · MicroPitch (Steve Vai), diatonic shift, dual shift, 1,000 programs |
| **Eventide DSP4000** | Eventide | Modular Multi-Effects Processor | 5 | 500 | `0x1C` (ID `0x02`) · Modular algorithmic architecture, pitch shifting, reverbs |
| **Eventide Eclipse** | Eventide | 24-Bit Dual-Engine Effects Processor | 4 | 500 | `0x1C` (ID `0x03`) · 24-bit 96kHz dual DSP engines, classic Eventide algorithms |
| **Eventide Space & TimeFactor** | Eventide | Flagship Studio Stomp / Processor | 6 | 100 | `0x1C` (ID `0x04`) · Blackhole, Shimmer, MangledVerb, Dual Delay, Band Delay |
| **Lexicon PCM70** | Lexicon | Digital Effects Processor | 3 | 100 | `0x06` (ID `0x01`) · Concert Hall, Rich Plate, Tiled Room, Resonant Chords |
| **Lexicon PCM80** | Lexicon | Dual-DSP Digital Effects Processor | 4 | 200 | `0x06` (ID `0x04`) · Dual DSP, spatial reverb, stereo multi-tap delay |
| **Lexicon PCM90** | Lexicon | Dedicated Digital Reverberator | 4 | 250 | `0x06` (ID `0x05`) · Reference studio reverberator, 5 banks of halls, plates, rooms |
| **Lexicon LXP-1 / LXP-5** | Lexicon | Compact Digital Reverb & Effects Module | 3 | 128 | `0x06` (ID `0x02`) · Compact 16-bit studio reverbs and pitch delays |
| **Lexicon MPX-1** | Lexicon | Multiple Processor FX Synthesizer | 3 | 200 | `0x06` (ID `0x06`) · Dedicated reverb DSP + multi-effects DSP, 200 programs |
| **Modal Argon8** | Modal Electronics | 8-Voice Wavetable Synthesizer | 5 | 500 | `0x00 0x21 0x27` · 32 high-res wavetables, 16-step morphing seq, 5 banks |
| **Modal Cobalt8** | Modal Electronics | 8-Voice Extended Virtual Analog | 5 | 500 | `0x00 0x21 0x27` · 34 complex analog algorithms, 4-pole morphing filter, 5 banks |
| **Modal Skulpt / CraftSynth** | Modal Electronics | Compact Virtual Analog / Wavetable | 4 | 128 | `0x00 0x21 0x27` · 4-voice portable virtual analog & wavetable synth |
| **Modal 002** | Modal Electronics | 12-Voice Hybrid Polyphonic Synthesizer | 5 | 500 | `0x00 0x21 0x27` · NCO digital oscillators, discrete transistor ladder filter, 5 banks |
| **JoMoX XBase 09 / AirBase 99** | JoMoX | Real Analog Drum Synthesizer | 6 | 128 | `0x33` (ID `0x01`) · Real discrete analog kick and snare circuits + sampled hats |
| **Doepfer MS-404 / Dark Energy**| Doepfer | Analog Monophonic Synthesizer Module | 5 | 64 | `0x00 0x20 0x20` · Discrete transistor ladder 24dB filter, 2 LFOs, CV/Gate |
| **DigiTech GSP 2101** | DigiTech | Dual Tube Guitar Preamp & Multi-FX | 4 | 200 | `0x00 0x00 0x1A` · Dual 12AX7 vacuum tubes, S-DISC processing, 200 programs |
| **DigiTech Studio Quad / TSR-24**| DigiTech | 4-In 4-Out Digital Multi-Effects | 3 | 200 | `0x00 0x00 0x1A` · 4 discrete audio channels, flexible multi-FX routing |
| **Alesis Andromeda A6** | Alesis | 16-Voice Discrete Analog Monster | 8 | 384 | `0x00 0x00 0x0E` · Discrete VCOs, dual filters (Moog ladder + SEM), ribbon |
| **Alesis Ion** | Alesis | High-Resolution Virtual Analog Synthesizer | 5 | 512 | `0x00 0x00 0x0E` · 17 filter models, 3 continuous mod wheels, 8 banks |
| **Alesis Micron** | Alesis | Compact Virtual Analog Synthesizer | 5 | 500 | `0x00 0x00 0x0E` · Ion sound engine, step seq, rhythm patterns, vocoder |
| **Alesis QS6 / QS7 / QS8 / QSR**| Alesis | 64-Voice Expandable Synthesizer | 5 | 640 | `0x00 0x00 0x0E` · 16MB sound ROM, PCMCIA card expansion, 5 banks |
| **Alesis QuadraSynth / Plus** | Alesis | 64-Voice Master Synthesizer | 5 | 512 | `0x00 0x00 0x0E` · 64-voice polyphony, Plus Piano soundset, 4 banks |
| **Alesis D4 / DM5** | Alesis | High-Sample-Rate Drum Sound Module | 3 | 500 | `0x00 0x00 0x0E` · 500 punchy 16-bit acoustic and electronic drum sounds |
| **Alesis HR-16 / HR-16B** | Alesis | 16-Bit Digital Drum Machine | 2 | 98 | `0x00 0x00 0x0E` · 49 authentic 16-bit drum sounds & rhythm patterns |
| **Alesis Quadraverb / Quadraverb 2**| Alesis | 20-Bit Digital Multi-Effects Processor | 4 | 100 | `0x00 0x00 0x0E` · Reverb, delay, pitch, EQ, 100 studio presets |
| **Kawai K5000S / R / W** | Kawai | Advanced Additive Synthesizer Flagship | 4 | 320 | `0x40` (ID `0x0A`) · 128 additive harmonics, Formant Filter (128 bandpass) |
| **Kawai K1 / K1m / K1r** | Kawai | VM Vector Synthesizer | 3 | 96 | `0x40` (ID `0x01`) · Vector joystick, 256 16-bit PCM waveforms, single & multi |
| **Kawai K4 / K4r** | Kawai | Digital Synthesizer w/ Resonant Filter | 4 | 128 | `0x40` (ID `0x04`) · Resonant digital lowpass/highpass filters, 16-bit PCM |
| **Kawai K5** | Kawai | Digital Additive Synthesizer | 3 | 96 | `0x40` (ID `0x02`) · 126 harmonic additive synthesis, single & multi setups |
| **Kawai XD-5** | Kawai | Percussion Synthesizer Module | 3 | 80 | `0x40` (ID `0x06`) · 16-bit PCM percussion synthesis with resonant filters |
| **Access Virus TI / TI2 / Snow** | Access Music | Dual-DSP Flagship Synthesizer | 5 | 2,048 | `0x00 0x20 0x33` · Dual DSP, Total Integration, hypersaw, wavetable synthesis |
| **Access Virus C / Indigo 2** | Access Music | 32-Voice Virtual Analog Synthesizer | 6 | 1,024 | `0x00 0x20 0x33` · 32 voices, 3-band EQ per part, Moog filter model, 8 banks |
| **Access Virus B / Indigo** | Access Music | Virtual Analog Synthesizer | 6 | 512 | `0x00 0x20 0x33` · 24 voices, DSP56303, 3 oscs + sub, 4 banks A-D |
| **ASM Hydrasynth (All Models)** | ASM | Wavemorphing Synthesizer Flagship | 5 | 640 | `0x00 0x21 0x3D` · Wavemorphing, Mutators (FM, WaveStack), Poly-Aftertouch |
| **Quasimidi Rave-O-Lution 309** | Quasimidi | Dance & Techno Groove Synthesizer | 4 | 99 | `0x3F` (ID `0x00`) · TB-303 and TR-808/909 emulations, real-time knobs |
| **Quasimidi Sirius** | Quasimidi | Dance Keyboard Workstation & Vocoder | 4 | 384 | `0x3F` (ID `0x02`) · 7-band vocoder, 11-track pattern sequencer, 288 presets |
| **Quasimidi Polymorph** | Quasimidi | 4-Part Virtual Analog Synthesizer | 4 | 128 | `0x3F` (ID `0x04`) · 4-part modular virtual analog rack, 16-step sequencer |
| **Quasimidi Technox** | Quasimidi | 16-Part Techno Sound Module | 3 | 256 | `0x3F` (ID `0x01`) · 16 multitimbral parts dedicated to electronic dance music |
| **Behringer Deepmind 12 / 12D** | Behringer | 12-Voice Polyphonic Analog Synthesizer | 6 | 1,024 | `0x00 0x20 0x32` · 12 analog voices, dual DCOs, 4 Klark Teknik FX, 8 banks |
| **Behringer PRO-800** | Behringer | 8-Voice Dual-VCO Polyphonic Analog | 5 | 400 | `0x00 0x20 0x32` · 8 voices, dual VCOs, Prophet 600 clone with GliGli mods |
| **Studio Electronics SE-1 / SE-1X**| Studio Electronics | Discrete 3-VCO Analog Synthesizer | 6 | 396 | `0x00 0x01 0x25` · 3 discrete analog VCOs, Moog 24dB + Oberheim 12dB SEM |
| **Oberheim Matrix-1000** | Oberheim | 6-Voice 1U Analog Synthesizer | 5 | 1,000 | `0x10` (ID `0x06`) · 1,000 matrix modulation patches, CEM3396 analog VCF |
| **Oberheim Matrix-6 / 6R** | Oberheim | Polyphonic Analog Synthesizer | 5 | 100 | `0x10` (ID `0x06`) · 100 memory patches, matrix modulation, CEM3396 |
| **Oberheim Matrix-12 / Xpander** | Oberheim | Flagship Multi-Mode Analog Synthesizer | 5 | 100 | `0x10` (ID `0x02`) · 15-mode state-variable filter, CEM3374 discrete VCOs |
| **Oberheim OB-8** | Oberheim | 8-Voice Polyphonic Analog Synthesizer | 5 | 120 | `0x10` (ID `0x01`) · Page 2 extended modulation, Curtis analog VCOs/VCFs |
| **Oberheim OB-X8** | Oberheim | 8-Voice Pure Analog Synthesizer | 6 | 160 | `0x01` (ID `0x32`) · Pure discrete VCOs, classic OB-X, OB-Xa & OB-8 filters |
| **Moog Minimoog Voyager** | Moog Music | Flagship Analog Monophonic Synthesizer | 12 | 896 | `0x04` (ID `0x01`) · Bob Moog continuous dual ladder filters, 3D touch surface, 7 banks |
| **Moog Sub 37 / Subsequent 37** | Moog Music | Paraphonic Analog Synthesizer | 12 | 256 | `0x04` (ID `0x05`) · Duo-paraphonic, MultiDrive grit, looping envelopes, 16 banks |
| **Moog Sub Phatty** | Moog Music | Analog Monophonic Synthesizer | 6 | 16 | `0x04` (ID `0x04`) · 25 keys, sub-oscillator, multidrive, 4 banks x 4 buttons |
| **Moog Little Phatty / Slim Phatty**| Moog Music | Analog Monophonic Synthesizer | 6 | 100 | `0x04` (ID `0x02`) · Real analog ladder filter, overload circuit, Bob Moog design |
| **Moog Minitaur / Sirin** | Moog Music | Analog Bass Synthesizer | 7 | 128 | `0x04` (ID `0x03`) · Legendary Taurus bass pedals sound engine, 8 banks |
| **Clavia Nord Lead 1 / Rack** | Clavia Nord | Virtual Analog Synthesizer (1995) | 6 | 139 | `0x33` (ID `0x04`) · The original virtual analog pioneer, pitch stick, morph |
| **Clavia Nord Lead 2 / Rack 2** | Clavia Nord | 16-Voice Virtual Analog Synthesizer | 5 | 396 | `0x33` (ID `0x04`) · 16 voices, 4-part multitimbral, FM synthesis, 4 banks |
| **Clavia Nord Lead 2X / Rack 2X**| Clavia Nord | 20-Voice Virtual Analog Synthesizer | 5 | 792 | `0x33` (ID `0x04`) · 20 voices, 24-bit 96kHz DACs, 4 program & 4 perf banks |
| **Clavia Nord Lead 3 / Rack 3** | Clavia Nord | Advanced Subtractive & FM Synthesizer | 5 | 1,024 | `0x33` (ID `0x06`) · Endless rotary LED encoders, 24-voice polyphony, 8 banks |
| **Clavia Nord Lead 4 / Rack 4** | Clavia Nord | Performance Virtual Analog Synthesizer | 5 | 396 | `0x33` (ID `0x08`) · Wavetables, ladder filter emulations, crush FX, 4 banks |
| **Novation Bass Station II** | Novation | Pure Analog Monophonic Synthesizer | 5 | 128 | `0x00 0x20 0x29` · Dual analog oscs, sub-osc, classic & acid filters, distortion |
| **Novation Supernova II / Supernova**| Novation | Flagship Virtual Analog Synthesizer | 6 | 512 | `0x00 0x20 0x29` · 8-part multitimbral, 42-band vocoder, 56 simultaneous FX, 4 banks |
| **Novation Nova / Nova II** | Novation | Desktop Virtual Analog Synthesizer | 6 | 256 | `0x00 0x20 0x29` · Desktop compact VA engine, polyphonic vocoder, 2 banks |
| **Novation K-Station / KS-4 / KS-5**| Novation | Liquid Analog Modeling Synthesizer | 5 | 200 | `0x00 0x20 0x29` · Liquid analog engine, hypersaw, 100 progs + 100 combis |
| **Novation Peak / Summit** | Novation | Flagship Hybrid Synthesizer | 6 | 512 | `0x00 0x20 0x29` · Oxford FPGA new-oxford oscs, analog multimode VCF, 4 banks |
| **Ensoniq ESQ-1 / ESQ-M** | Ensoniq | Digital Wave Synth w/ Curtis Analog VCF | 5 | 120 | `0x0F` (ID `0x02`) · 3 digital oscs, CEM3379 analog VCF, 40 internal + 80 cart |
| **Ensoniq SQ-80** | Ensoniq | Cross Wave Synthesizer | 5 | 120 | `0x0F` (ID `0x03`) · Cross-wave synthesis, CEM3379 analog filter, poly aftertouch |
| **Ensoniq VFX / VFX-SD** | Ensoniq | Transwave Synthesizer Workstation | 5 | 120 | `0x0F` (ID `0x05`) · Dynamic Transwave synthesis, patch select buttons, dual 24-bit FX |
| **Ensoniq TS-10 / TS-12** | Ensoniq | Performance Workstation w/ Hyper-Wave | 5 | 120 | `0x0F` (ID `0x08`) · Hyper-Wave wave sequencing, 32 voices, 73 dynamic effects |
| **Ensoniq MR Rack / MR-61** | Ensoniq | 64-Voice Synthesizer Module | 5 | 473 | `0x0F` (ID `0x0A`) · 16-bit 44.1kHz wave ROM, 64 voices, Idea Pad, 5 sound banks |
| **Waldorf Blofeld** | Waldorf Music | Desktop / Keyboard Wavetable & VA | 9 | 1,024 | `0x3E` (ID `0x13`) · 3 oscs, dual multi-mode & comb filters, 8 banks A-H |
| **Waldorf Microwave I** | Waldorf Music | Hybrid Wavetable Synth w/ Curtis Analog VCF | 8 | 64 | `0x3E` (ID `0x00`) · CEM3389 24dB VCF/VCA, wavetables 1-30, Bank A & B |
| **Waldorf Microwave II / XT** | Waldorf Music | DSP Wavetable Powerhouse Synth | 8 | 256 | `0x3E` (ID `0x0E`) · Digital multi-mode filters, speech synthesis, Bank A & B |
| **Waldorf Pulse / Pulse Plus** | Waldorf Music | Monophonic 3-VCO Analog Monster | 8 | 100 | `0x3E` (ID `0x07`) · 3 analog VCOs, 24dB cascade VCF, 40 ROM + 60 RAM |
| **Waldorf Pulse 2** | Waldorf Music | Analog Mono / Paraphonic Synthesizer | 9 | 500 | `0x3E` (ID `0x14`) · 3 analog oscillators, 8-voice paraphonic chords, drive |
| **Waldorf Q / Q Rack / Q+** | Waldorf Music | Flagship Virtual Analog Synthesizer | 10 | 300 | `0x3E` (ID `0x0F`) · 3 oscs, dual multi-mode filters, comb filter, vocoder |
| **Waldorf Streichfett** | Waldorf Music | Dedicated String & Choir Synthesizer | 8 | 12 | `0x3E` (ID `0x15`) · Solina/Crumar string ensemble, choir, animate/reverb FX |
| **Sequential Prophet-5** | Sequential Circuits | Definitive 5-Voice Analog Polysynth | 12 | 200 | `0x01` (ID `0x02`) · SSM/Curtis analog VCOs/VCFs, Poly-Mod, Cars Sync II |
| **Sequential Prophet 600** | Sequential Circuits | First Commercial MIDI Synthesizer | 6 | 100 | `0x01` (ID `0x02`) · Dual VCO CEM3340, CEM3372 filter/VCA, patches 00-99 |
| **Sequential Prophet VS** | Sequential Circuits | Vector Synthesis Digital/Analog Hybrid | 7 | 100 | `0x01` (ID `0x0A`) · 4 digital oscs, vector joystick, Curtis CEM3379 analog VCF |
| **Sequential Six-Trak** | Sequential Circuits | 6-Voice Multitimbral Analog Synthesizer | 4 | 100 | `0x01` (ID `0x05`) · 6 voices CEM3394 synth-on-a-chip, 100 memory patches |
| **DSI Prophet '08 / Rev2** | Dave Smith Instruments | 8/16-Voice Modern Analog Polysynth | 10 | 256 | `0x01` (ID `0x23`) · Curtis analog DCOs & 2/4-pole lowpass VCF, 2 factory banks |
| **DSI Prophet-6** | Dave Smith Instruments | Discrete Polyphonic Analog Synthesizer | 9 | 500 | `0x01` (ID `0x2D`) · Pure discrete VCOs/VCFs, Poly Mod, dual digital FX, 5 banks |
| **DSI / Oberheim OB-6** | Dave Smith Instruments | Polyphonic Analog Synth w/ SEM Filter | 8 | 500 | `0x01` (ID `0x2E`) · Tom Oberheim SEM multi-mode continuous filter, 5 banks |
| **DSI Prophet 12** | Dave Smith Instruments | 12-Voice Flagship Hybrid Synthesizer | 9 | 396 | `0x01` (ID `0x26`) · Digital wavetables, Character FX (Girth/Air/Hack), analog VCF |
| **DSI Evolver** | Dave Smith Instruments | Hybrid Analog/Digital Synthesizer | 7 | 384 | `0x01` (ID `0x20`) · Dual analog + dual digital oscs, 4x16 step seq, feedback |
| **DSI Mopho / Tetra** | Dave Smith Instruments | Analog Monophonic / Polyphonic Synth | 7 | 384 | `0x01` (ID `0x25`) · Curtis 4-pole lowpass, sub-oscillators, analog feedback |
| **DSI Pro 2 / Pro 3** | Dave Smith Instruments | Flagship Paraphonic Hybrid Synthesizer | 8 | 396 | `0x01` (ID `0x2B`) · Dual analog filters (Prophet + SEM), 4-track sequencer, CV I/O |
| **Roland JV-1080** | Roland Corporation | 64-Voice 16-Part Super JV Module | 6 | 640 | `0x6A` · 4 SR-JV80 slots, 40 EFX, User + PR-A/B/C + GM |
| **Roland JV-2080** | Roland Corporation | 64-Voice 3U Module with 3 EFX | 5 | 768 | `0x6A` · 8 SR-JV80 slots, 320x80 LCD, 3 simultaneous EFX |
| **Roland JD-800** | Roland Corporation | Programmable Synth w/ 69 Control Sliders | 5 | 64 | `0x3D` · 4 tone layers, multi-mode TVF, Pizzagogo & Strobe X |
| **Roland JD-990** | Roland Corporation | Super JD Multi-Timbral Module | 6 | 192 | `0x57` · Hard sync, ring mod, FXM, vintage Roland waves, 320x80 LCD |
| **Roland Juno-106** | Roland Corporation | 6-Voice DCO Analog Polyphonic Synth | 23 | 128 | `0x32` · IR3109 VCF, BBD chorus, continuous slider SysEx control |
| **Roland Jupiter-8** | Roland Corporation | 8-Voice Discrete Analog Polyphonic | 7 | 64 | `0x41` · Discrete VCOs, cross-mod, sync, switchable 12/24dB VCF |
| **Roland MKS-80** | Roland Corporation | Super Jupiter 8-Voice Rackmount Analog | 4 | 192 | `0x02` · MPG-80 programmer, 16 analog VCOs, 64 patches + 128 tones |
| **Roland MKS-50** | Roland Corporation | 1U Alpha Juno Polyphonic Analog Rack | 3 | 128 | `0x23` · IR3109 VCF, BBD chorus, chord memory, PG-300 mapping |
| **Roland Sound Canvas SC-55** | Roland Corporation | Definitive General MIDI / GS Module | 4 | 317 | `0x42` (GS) · 317 GS instruments + 9 drum sets, digital reverb/chorus |
| **Roland Sound Canvas SC-88** | Roland Corporation | Flagship 64-Voice 32-Part GS Module | 3 | 654 | `0x45` (GS) · 654 GS sounds, dual MIDI inputs (32 parts), 24 drum kits |
| **Roland MC-303** | Roland Corporation | The Original Dance Music Groovebox | 2 | 448 | `0x00 0x07` · 448 dance tones, TR-808/909 kits, 8-track sequencer |
| **Roland MC-505** | Roland Corporation | Flagship Dance Production Groovebox | 3 | 640 | `0x00 0x14` · 640 patches, 26 rhythm kits, D-Beam, Megamix sliders |
| **Korg M1** | Korg | AI Synthesis Music Workstation Flagship | 10 | 150 | `0x42` (ID `0x19`) · Universe, Piano 16' (house piano staple), 100 Progs + Combis |
| **Korg Wavestation** | Korg | Vector Synthesis & Wave Sequencing | 6 | 205 | `0x42` (ID `0x28`) · 2-axis vector joystick, dynamic rhythmic wave sequencing, Ski Jam |
| **Korg 01/W** | Korg | AI2 Synthesis Workstation w/ Waveshaping | 5 | 400 | `0x42` (ID `0x36`) · 60 waveshaping tables, 200 Programs + 200 Combinations |
| **Korg Trinity** | Korg | ACCESS Synthesis Workstation TouchView | 4 | 675 | `0x42` (ID `0x3B`) · 24MB PCM ROM, 320x240 TouchView LCD, Ribbon, Bank A/B/M |
| **Korg Triton** | Korg | HI Synthesis Workstation & Sampler | 5 | 1,040 | `0x42` (ID `0x50`) · 512 Programs + 512 Combis, dual poly arps, 16 drum kits |
| **Korg MS2000** | Korg | DSP Virtual Analog Synthesizer & Vocoder | 5 | 128 | `0x42` (ID `0x58`) · 71 DWGS waveforms, 3-track 16-step Motion Sequencer, 16-band Vocoder |
| **Korg microKORG** | Korg | Compact Modeling Synthesizer / Vocoder | 5 | 128 | `0x42` (ID `0x58`) · Genre select dial, 8-band vocoder w/ gooseneck mic, DWGS waves |
| **Korg Prophecy** | Korg | MOSS Solo Physical Modeling Synthesizer | 4 | 128 | `0x42` (ID `0x41`) · Monophonic acoustic modeling, ribbon controller, Prodigy rave lead |
| **Korg Z1** | Korg | 12-Voice Polyphonic MOSS Modeling Synth | 5 | 288 | `0x42` (ID `0x46`) · 13 oscillator algorithms, X-Y touchpad, dual poly arpeggiator |
| **Korg DW-8000** | Korg | Hybrid DWGS Synth w/ Analog NJM2069 VCF | 5 | 64 | `0x42` (ID `0x03`) · 16 sampled waveforms, 24dB resonant analog VCF, digital delay |
| **Yamaha DX7** | Yamaha Corporation | 16-Voice 6-Operator Digital FM Flagship | 22 | 64 | `0x43` · 32 algorithms, 6 EGs, pure sine operators, E.Piano 1 & Bass 1 |
| **Yamaha DX7II (FD/D)** | Yamaha Corporation | Dual 6-Op FM Synth w/ Fractional Scaling | 8 | 96 | `0x43` (ID `0x19`) · Dual/Split/Single, microtuning, stereo panning |
| **Yamaha TX81Z** | Yamaha Corporation | 8-Voice 4-Op Multi-Waveform FM Rack | 14 | 160 | `0x43` (ID `0x7E`) · 8 waveforms (W1-W8), LatelyBass, 8-part multi |
| **Yamaha TX802** | Yamaha Corporation | 8-Part 6-Op FM Rack (8x DX7II) | 6 | 192 | `0x43` (ID `0x19`) · 8 discrete audio outputs, 64 performances |
| **Yamaha DX100** | Yamaha Corporation | Portable 4-Operator FM Performance Synth | 10 | 216 | `0x43` (ID `0x04`) · Solid Bass (Voice 01), strap pins, 192 ROM sounds |
| **Yamaha AN1x** | Yamaha Corporation | 10-Voice Analog Physical Modeling (VA) | 10 | 128 | `0x43` (ID `0x5C`) · Dual scene morphing, 4-track Free EG motion recorder |
| **Yamaha CS1x** | Yamaha Corporation | Dance/Techno Performance Synthesizer | 7 | 128 | `0x43` (ID `0x4B`) · Realtime analog-style knobs, Scene 1/2 vector morph |
| **Yamaha SY77 / TG77** | Yamaha Corporation | RCM Hybrid Synthesizer (AFM + AWM2) | 7 | 80 | `0x43` (ID `0x24`) · 6-op 45-algo AFM modulated by 16-bit AWM2 PCM |
| **Yamaha Motif** | Yamaha Corporation | 64-Voice AWM2 Production Workstation | 8 | 394 | `0x43` (ID `0x6B`) · 85MB Wave ROM, PLG expansion, Dual Insert FX |
| **Roland JX-3P** | Roland Corporation | 6-Voice DCO Analog Polyphonic Synth | 28 | 64 | `0x41` · IR3109 VCF, BBD chorus, 128-step poly sequencer, PG-200 |
| **Roland JX-8P** | Roland Corporation | 6-Voice DCO Analog Synth w/ PG-800 | 36 | 64 | `0x06` · Sync/Metal cross-mod, dual envelopes, touch sensitivity |
| **Roland JX-10 Super JX** | Roland Corporation | 12-Voice Flagship Dual DCO Analog | 10 | 164 | `0x0A` · Dual tone layers, Chase Play delay, 64 patches + 100 tones |
| **Roland JX-305** | Roland Corporation | 64-Voice Groove Keyboard Workstation | 8 | 666 | `0x00 0x14` · MC-505 sound engine, 5 banks x 128 patches, 26 rhythm kits |
| **Roland JP-8000** | Roland Corporation | 8-Voice Analog Modeling (Super Saw VA) | 23 | 85 | `0x3F` · Motion Control, Ribbon, RPS, Ribbon & Feedback Osc |
| **Roland JP-8080** | Roland Corporation | 10-Voice VA Rack with 12-Band Vocoder | 25 | 284 | `0x4A` · External Audio Input, 12-band Vocoder, Voice Modulator |
| **Roland SH-01 GAIA** | Roland Corporation | Triple-Stacked Virtual Analog Synth | 11 | 64 | `0x00 0x00 0x41` · 3 complete virtual analog synth engines in parallel |
| **Roland JD-XA** | Roland Corporation | Advanced Analog/Digital Crossover Synth | 8 | 64 | `0x00 0x00 0x00 0x09` · 4-voice discrete analog + 64-voice digital SuperNATURAL |
| **Roland JW-50** | Roland Corporation | Music Workstation (GS Sound Canvas) | 3 | 128 | `0x42` (GS) · 16-track sequencer, SMF compatibility, 128 GS sounds |
| **Roland JX-1** | Roland Corporation | Performance Synthesizer | 4 | 64 | `0x2F` · Instant front-panel slider editing, Dual/Split/Layer |
| **Roland FANTOM Modern** | Roland Corporation | Flagship ZEN-Core / V-Piano / ACB Synthesizer | 5 | 2,104 | `0x00 0x00 0x00 0x64` · Stereo analog filter, scenes, Zenology |
| **Roland FANTOM-0** | Roland Corporation | Lightweight ZEN-Core & SuperNATURAL Synth | 3 | 2,098 | `0x00 0x00 0x00 0x76` · 16 zones, USB audio interface, 06/07/08 |
| **Roland Fantom-G** | Roland Corporation | SuperNATURAL 128-Voice Flagship Workstation | 4 | 1,190 | `0x00 0x00 0x24` · ARX expansion slots, 8.5" color LCD, G6/G7/G8 |
| **Roland Fantom-X** | Roland Corporation | 128-Voice Sampling Workstation & 1U Rack | 8 | 1,471 | `0x00 0x6B` · Color LCD, 8-track audio, 4x SRX slots, X6/X7/X8/XR |
| **Roland Fantom-S** | Roland Corporation | Sampling Workstation Keyboard (S / S88) | 3 | 997 | `0x00 0x5B` · Skip-Back sampling, 16 dynamic pads, SRX expansion |
| **Roland XV-5080** | Roland Corporation | 128-Voice Flagship 32-Part Synth/Sampler | 49 | 1,263 | `0x00 0x10` · 8 SR-JV80 + 4 SRX slots, 4 stereo tones, 1,083 waves |
| **Roland XV-3080** | Roland Corporation | 128-Voice 16-Part 2U Synth Module | 49 | 1,065 | `0x00 0x10` · 6 SR-JV80 + 2 SRX slots, 1,083 PCM waves |
| **Roland XV-5050** | Roland Corporation | 64-Voice 16-Part 1U Module (COSM) | 49 | 598 | `0x00 0x10` · COSM effects processors, 2 SRX slots, USB MIDI |
| **Roland XP-80 / XP-60** | Roland Corporation | 64-Voice Workstation Keyboard | 9 | 363 | `0x6A` · 4 SR-JV80 slots, MRC Pro sequencer, authentic PCM waves |
| **Roland D-50** | Roland Corporation | 16-Voice Linear Arithmetic (LA) Flagship | 26 | 64 | `0x14` · 4 partials, ring mod, reverb/chorus/EQ, Fantasia & Soundtrack |
| **Roland D-20** | Roland Corporation | Multi-Timbral LA Keyboard Workstation | 7 | 128 | `0x16` · 8 parts + rhythm, built-in FDD disk drive & sequencer |
| **Roland D-70** | Roland Corporation | Super LA 76-Key Synthesizer & Controller | 11 | 64 | `0x32` · 4 tones, Differential Loop Modulation (DLM), 28MB ROM |
| **Roland D-110** | Roland Corporation | Multi-Timbral LA Synthesis Module | 8 | 128 | `0x16` · 8 individual outputs, 13 partial structures, D-50 heritage |
| **Roland Alpha Juno-1 / 2** | Roland Corporation | 6-Voice Polyphonic Analog (DCO) | 23 | 64 | `0x23` · IR3109 VCF, BBD chorus, Hoover "What The..." sound |
| **Roland D2** | Roland Corporation | Desktop Groovebox with D-Field Controller | 4 | 640 | `0x00 0x34` · MC-505 sound engine, 5 banks x 128 patches, Megamix |
| **Roland DJ-70** | Roland Corporation | Sampling Keyboard with Scratch Dial | 2 | 64 | `0x4B` · 37 keys, scratch jog dial, load-while-play sampler |
| **Roland EG-101** | Roland Corporation | Advanced Groove Keyboard with D-Beam | 2 | 128 | `0x00 0x1B` · Phrase sampler, D-Beam controller, synth presets |
| **Roland W-30** | Roland Corporation | 12-Bit Sampling Music Workstation | 7 | 57 | `0x2B` · 30kHz/15kHz 12-bit sampler, SCSI/HD support, 16 tracks |
| **Access Virus A** | Access Music GmbH | Virtual Analog (DSP56303) | 17 | 256 | `0x10` (16) · Multi-page SysEx (Pages A, B, C), 256-byte dumps |
| **Akai AX60** | Akai Professional | 6-Voice CEM3394 Analog | 23 | 64 | Tauntek CC mapping (CC 14–74), 3,445B Bank SysEx, Sampler input |
| **Casio CZ-1** | Casio Computer Co. | 16-DCO Phase Distortion | 26 | 64 | `0x03` · Dual Line detune, Velocity & Aftertouch sensitivity |
| **Casio CZ-101** | Casio Computer Co. | 8-DCO Portable Phase Distortion | 22 | 32 | `0x01` · Cosine phase distortion, 8-stage DCO/DCW/DCA envelopes |
| **Casio CZ-1000** | Casio Computer Co. | Full-Size 8-DCO Phase Distortion | 22 | 32 | `0x02` · Membrane button styling, 8-stage envelopes, SysEx `0x44` |
| **Casio CZ-230S** | Casio Computer Co. | Phase Distortion + PCM Rhythm | 11 | 104 | `0x04` · 100 preset PD voices + 4 User RAM, onboard speaker |
| **Casio CZ-3000** | Casio Computer Co. | 16-DCO Full-Size Synthesizer | 23 | 64 | `0x05` · Dual line layering, stereo chorus, 8-stage pitch/wave/amp |
| **Casio CZ-5000** | Casio Computer Co. | Flagship PD Workstation | 25 | 64 | `0x06` · Built-in 8-track sequencer, 16 DCOs, dual line stack |
| **E-MU Audity 2000** | E-mu Systems, Inc. | 64-Voice Modular Rack | 53 | 640 | `0x0C` · 4 sub-editors (MultiMode, Presets, Arp, FX), 16 arpeggiators |
| **E-MU B-3** | E-mu Systems, Inc. | 64-Voice Tonewheel Organ | 25 | 384 | `0x0E` · 9 Hammond drawbars, Leslie 122 rotary cabinet, percussion |
| **E-MU Carnaval** | E-mu Systems, Inc. | 32-Voice Latin/World Module | 24 | 640 | `0x08` · BEATS drum machine, X-Factor polyrhythmic groove crossfade |
| **E-MU Emax** | E-mu Systems, Inc. | 12-Bit Analog VCF Sampler | 24 | 72 | `0x00` · SSM2047 24dB/oct resonant analog filters, dual AHDSR, MIDI SDS |
| **E-MU Emax II** | E-mu Systems, Inc. | 16-Bit Stereo Workstation | 24 | 80 | `0x00` · 32-voice stereo sampling, digital 4-pole VCF, Spectrum Interpolation |
| **E-MU Orbit 9090** | E-mu Systems, Inc. | 32-Voice Dance Planet Rack | 7 | 640 | `0x01` · 1996 Golden yellow chassis, Beats mode, 32 digital filters |
| **E-MU Orbit-3** | E-mu Systems, Inc. | 128-Voice Super Dance Module | 7 | 1,024 | `0x11` (17) · Dual 32MB Beat Garden & Techno Yard ROMs, 50 Z-Plane filters |
| **E-MU Planet Earth** | E-mu Systems, Inc. | 64-Voice World Expedition | 7 | 1,024 | `0x06` · Oceanic teal chassis, 32MB World ROM, SuperBEATS engine |
| **E-MU Planet Phatt** | E-mu Systems, Inc. | 32-Voice Hip-Hop / Swing System | 7 | 640 | `0x01` · Magenta anodized chassis, 32 digital filters, BEATS swing grooves |
| **E-MU Proteus 1000** | E-mu Systems, Inc. | 64-Voice 1U Sound Module | 7 | 1,024 | `0x0C` (12) · 30th Anniversary edition, blue trapezoid LCD, 32MB Composer ROM |
| **E-MU Proteus 2000** | E-mu Systems, Inc. | 128-Voice Flagship Module | 8 | 1,024 | `0x04` · 4 ROM slots, 128 voices, 50 Z-Plane filters, 24 mod cords |
| **E-MU Proteus 2500** | E-mu Systems, Inc. | 128-Voice Command Station | 8 | 1,024 | `0x0A` (10) · Desktop console, 16 velocity pads, 16 knobs, 16-track sequencer |
| **E-MU SP-1200** | E-mu Systems, Inc. | 12-Bit 26.04kHz Drum Sampler | 12 | 100 | `0x01` · SSM2044 4-pole discrete analog dynamic filters, 8 multi-pitch sliders |
| **E-MU Vintage Keys** | E-mu Systems, Inc. | 32-Voice Vintage Module (1993) | 10 | 512 | `0x01` · 1U matte steel, 11x5 cyan dot matrix, 8 classic keyboard engines |
| **E-MU Vintage Pro** | E-mu Systems, Inc. | 128-Voice Vintage Workstation | 10 | 1,024 | `0x16` (22) · Two-tone pewter faceplate, 64MB Vintage Collection ROM |
| **E-MU Virtuoso 2000** | E-mu Systems, Inc. | 128-Voice Virtual Orchestra | 10 | 1,024 | `0x08` · 64MB Orchestral Sessions Vol 1 & 2 ROMs, continuous navy wave line |
| **E-MU XK-6** | E-mu Systems, Inc. | 61-Key Dance Performance Synth | 10 | 1,024 | `0x12` (18) · 61 synth-action keys, SuperBEATS interactive engine |
| **E-MU XL-7** | E-mu Systems, Inc. | 128-Voice Command Station | 18 | 1,024 | `0x0E` (14) · Electric yellow desktop tabletop, 16 pads, 16 rotary knobs |
| **E-MU Xtreme Lead-1** | E-mu Systems, Inc. | 64-Voice Dance & Techno Rack | 14 | 1,024 | `0x07` · Electric yellow 1U rack, 50 Z-Plane filters, 16-track SuperBEATS |

---

## Workspace Architecture

```
omnipatch/
├── assets/                   # Hardware faceplate images, vector reference diagrams, icons
│   └── screenshots/          # High-resolution hardware editor & studio screenshots
├── crates/                   # High-performance modular Rust crates
│   ├── omnipatch-cli/        # CLI binary commands, SysEx testing, database utilities
│   ├── omnipatch-core/       # Core types, error handling, parameter schemas
│   ├── omnipatch-librarian/  # SQLite local database storage, indexing, search engine
│   ├── omnipatch-midi/       # midir low-latency packet pacing, hardware throttling
│   ├── omnipatch-profile/    # YAML parser, parameter mapping, validation engine
│   └── omnipatch-sysex/      # Checksum calculators (Roland, E-MU, Casio, Waldorf)
├── devices/                  # 228 Declarative YAML hardware profiles & factory presets
│   ├── access/               # Access Music (Virus A, B, C, TI, TI2, Indigo, Snow)
│   ├── akai/                 # Akai Professional (AX60)
│   ├── alesis/               # Alesis (Andromeda A6, Ion, Micron, QS Series, QuadraSynth, D4/DM5, HR-16)
│   ├── arturia/              # Arturia (PolyBrute, MatrixBrute, MicroFreak, MiniBrute 2)
│   ├── asm/                  # Ashun Sound Machines (Hydrasynth Desktop, Deluxe, Explorer, Keyboard)
│   ├── behringer/            # Behringer (Deepmind 12, Deepmind 12D, PRO-800)
│   ├── black_corporation/    # Black Corporation (Deckard's Dream, Kijimi)
│   ├── casio/                # Casio Computer Co. (CZ-1, CZ-101, CZ-1000, CZ-230S, CZ-3000, CZ-5000)
│   ├── cheetah/              # Cheetah Marketing (MS6)
│   ├── clavia/               # Clavia Nord (Nord Lead 1, 2, 2X, 3, 4, Nord Rack)
│   ├── crumar/               # Crumar (Bit One, Bit 99, Bit 01)
│   ├── digitech/             # DigiTech (GSP 2101 Tube Preamp, Studio Quad / TSR-24)
│   ├── doepfer/              # Doepfer (MS-404, Dark Energy)
│   ├── dreadbox/             # Dreadbox (Typhon, Erebus)
│   ├── elektron/             # Elektron (Digitakt, Digitone, Syntakt, Analog Four / Rytm)
│   ├── emu/                  # E-MU Systems (Orbit-3, Proteus family, SP-1200, Emax, Vintage, etc.)
│   ├── ensoniq/              # Ensoniq (ESQ-1, SQ-80, VFX, TS-10, MR Rack)
│   ├── eventide/             # Eventide (H3000, DSP4000, Eclipse, Space, TimeFactor, Rose)
│   ├── jomox/                # JoMoX (XBase 09, AirBase 99)
│   ├── kawai/                # Kawai (K1, K4, K5, K5000 Additive Flagship, XD-5)
│   ├── korg/                 # Korg (Kronos, minilogue xd, prologue, opsix, wavestate, Mono/Poly, Polysix, Poly-800)
│   ├── kurzweil/             # Kurzweil (K2000, K2500, K2600 V.A.S.T. Workstations)
│   ├── lexicon/              # Lexicon (PCM70, PCM80, PCM90, LXP-1/5, MPX-1)
│   ├── modal/                # Modal Electronics (Argon8, Cobalt8, Skulpt, Modal 002)
│   ├── moog/                 # Moog Music (Moog One, Minimoog Voyager, Sub 37, Matriarch, Grandmother, Minitaur)
│   ├── novation/             # Novation (Bass Station II, Supernova II, Nova, K-Station, Peak)
│   ├── oberheim/             # Oberheim (Matrix-1000, Matrix-6, Matrix-12/Xpander, OB-8, OB-X8)
│   ├── oscar/                # Oxford Synthesiser Company (OSCar)
│   ├── peavey/               # Peavey (DPM 3, Spectrum Series)
│   ├── pioneer_dj/           # Pioneer DJ / Dave Smith (Toraiz AS-1, Toraiz SP-16)
│   ├── quasimidi/            # Quasimidi (Rave-O-Lution 309, Sirius, Polymorph, Technox)
│   ├── roland/               # Roland Corporation (TB-303, TR-808, TR-909, SH-101, Integra-7, System-8, JV, JD, Juno)
│   ├── sequential/           # Sequential & DSI (Prophet-5, Prophet-6, OB-6, Trigon-6, Take 5, Evolver, P12, Mopho)
│   ├── siel/                 # Siel (Opera 6, DK600)
│   ├── strymon/              # Strymon (BigSky, TimeLine)
│   ├── studio_electronics/   # Studio Electronics (SE-1, SE-1X)
│   ├── tc_electronic/        # TC Electronic (2290 Dynamic Delay)
│   ├── udo_audio/            # UDO Audio (Super 6, Super Gemini)
│   ├── waldorf/              # Waldorf Music (Quantum, Iridium, Kyra, M, Blofeld, Microwave, Pulse, Q, Streichfett)
│   └── yamaha/               # Yamaha Corporation (CS-80, FS1R, SY99, EX5, VL1, DX7, DX7II, TX81Z, Motif)
├── preview/                  # Web Audio interactive studio prototypes & hardware editors
│   ├── index.html            # Main Entry: Universal Windows 8 Metro UI Studio Hub (All 27 Synths)
│   ├── metro_studio.html     # Universal Windows 8 Metro UI Studio (Collapsible Menus, Live Tiles)
│   ├── orbit_3_metro.html    # Standalone authentic Metro UI editor for E-MU Orbit-3
│   ├── index_legacy_hybrid.html # Archived backup of legacy skeuomorphic/hybrid rack hub
│   └── *.html                # Dedicated hardware-specific vintage rackface editors
└── tools/                    # Automated PDF manual ingestion tool (Python)
```

---

## Quick Start

### 1. Launching the Interactive Metro Studio

The full 27-instrument Metro Studio can be run locally in any browser with zero installation:

```bash
# Start a local static file server
cd omnipatch
python3 -m http.server 8080

# Open in your web browser:
# http://localhost:8080/preview/index.html
# or
# http://localhost:8080/preview/metro_studio.html
```

#### Metro Studio Features Available Immediately:
- **Collapsible Sidebar:** Expand and collapse hardware brands (E-MU, Casio, Access Music, Akai) or use the `EXP` / `COL` quick buttons.
- **Top Bar Panoramic Navigation:** Switch between **Synth Editor**, **Start Screen**, **Universal Librarian**, and **MIDI Engine & Specs**.
- **Interactive Audio Playback:** Click any preset or soundboard tile to audition real-time synthesis powered by the Web Audio API.
- **SysEx Telemetry:** Inspect live 7-bit MIDI SysEx packet streams and download `.syx` patch dumps directly from the browser.

---

### 2. Building the Rust CLI & Core Engine

```bash
# Clone the repository
git clone https://github.com/dan2804/omnipatch.git
cd omnipatch

# Build the release binaries
cargo build --release

# Run unit tests across all crates
cargo test
```

### 3. CLI Commands & Librarian Usage

```bash
# List all 27 loaded synth profiles
./target/release/omnipatch devices list --dir devices/

# Inspect specific synth parameters
./target/release/omnipatch devices show "Casio CZ-1" --dir devices/
./target/release/omnipatch devices show "E-MU Orbit-3" --dir devices/
./target/release/omnipatch devices show "Access Virus A" --dir devices/

# Generate bit-perfect SysEx parameter edit
./target/release/omnipatch sysex param-edit "cz1" "dco1_wave" 2
./target/release/omnipatch sysex param-edit "orbit3" "cutoff" 105
./target/release/omnipatch sysex param-edit "virus-a" "filter1_cutoff" 88

# Import all factory presets into local SQLite librarian
./target/release/omnipatch librarian import-presets --dir devices/ -b library.db

# Search patches by name, bank, or category
./target/release/omnipatch librarian search "Acid" -b library.db
./target/release/omnipatch librarian search "Strings" -b library.db
./target/release/omnipatch librarian search "Reso" -b library.db
```

---

## Hardware Editor Previews

| Synthesizer | Preview File | Architecture Highlights |
| :--- | :--- | :--- |
| **Universal Metro Studio** | [`preview/index.html`](preview/index.html) | Complete Windows 8 Modern Studio with all 27 synths & collapsible brand menus |
| **E-MU Orbit-3 (Metro UI)** | [`preview/orbit_3_metro.html`](preview/orbit_3_metro.html) | Standalone Windows 8 Metro UI editor, 8 live soundboard tiles, 2D Z-Plane curve |
| **Casio CZ-1** | [`preview/casio_cz_1.html`](preview/casio_cz_1.html) | Flagship 16-DCO Phase Distortion, dual line detuning, velocity/aftertouch |
| **Casio CZ-101 / CZ-1000** | [`preview/casio_cz_101.html`](preview/casio_cz_101.html) | Portable & membrane-keypad PD classics, 8-stage DCO/DCW/DCA envelope engines |
| **Casio CZ-230S** | [`preview/casio_cz_230s.html`](preview/casio_cz_230s.html) | Phase distortion preset soundboard and onboard PCM drum rhythm groove accompaniment |
| **Casio CZ-3000 / CZ-5000** | [`preview/casio_cz_5000.html`](preview/casio_cz_5000.html) | 16-DCO dual line stack, stereo chorus, built-in 8-track hardware sequencer |
| **Access Virus A** | [`preview/virus_a.html`](preview/virus_a.html) | Red anodized chassis, dual resonant serial/parallel filters with saturation drive |
| **Akai AX60** | [`preview/ax60.html`](preview/ax60.html) | Curtis CEM3394 analog sliders, Tauntek CC mapping, stereo BBD chorus |
| **E-MU Proteus 1000 / 2000** | [`preview/proteus_1000.html`](preview/proteus_1000.html) | 30th Anniversary trapezoid LCD, 32MB Composer ROM, 50 Z-Plane filters |
| **E-MU SP-1200** | [`preview/sp1200.html`](preview/sp1200.html) | 12-bit linear 26.04kHz sampler, discrete SSM2044 analog filters, 8-pad decay matrix |
| **E-MU Emax & Emax II** | [`preview/emax.html`](preview/emax.html) | SSM2047 analog VCF vs 16-bit digital processing, spectrum interpolation |
| **E-MU Planet Earth & Phatt** | [`preview/planet_earth.html`](preview/planet_earth.html) | Oceanic teal & magenta anodized 1U racks, World Expedition & Swing System BEATS |
| **E-MU XL-7 & XK-6** | [`preview/xl7.html`](preview/xl7.html) | Desktop tabletop command station & 61-key performance keyboard with SuperBEATS |

---

## License

Open-source under MIT or Apache 2.0.
