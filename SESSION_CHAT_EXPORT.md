# OmniPatch & E-MU Hardware Synthesizers: Complete Chat & Session Export
**Date / Timestamp:** 2026-11-23T03:30:00-08:00  
**Repository:** [https://github.com/dan2804/omnipatch](https://github.com/dan2804/omnipatch)  
**Branch:** `main` (Latest commit: `2046a1c`)  
**Context:** Multi-device skeuomorphic Web Audio hardware synthesizers & Midi Quest 13 SysEx integration hub.

---

## 1. Executive Summary & Purpose
This document provides a complete, exportable record of the pair-programming and design sessions focused on engineering pixel-perfect, skeuomorphic, interactive Web Audio hardware emulations and Midi Quest 13 editors for classic E-MU Systems rack synthesizers.

This export is structured to allow immediate continuation in any local development environment (e.g. Cursor, VS Code, Cline, Roo Code, Aider, Claude Code, or local terminal).

---

## 2. Chronological Conversation Log & User Requests

### Request 1: E-MU Proteus 1000
- **User Prompt:**
  ```text
  proteus 1000
  https://www.emumania.net/wp-content/uploads/e-mu-proteus-1000-lrg-tx.jpg
  https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFSrSEVPVtAMZZ3RkVx6z-1QQHRWBdO6bacoqQaU1bE8Z_mrRPTivP6tl3&s=10
  https://i.ebayimg.com/images/g/NRkAAOSwi~Vn3NKl/s-l1200.jpg
  https://squest.com/Products/MidiQuest13/Instruments/E-MUProteus1000/index.html
  ```
- **Actions Taken:** Built the complete `preview/proteus_1000.html` with slate/charcoal metallic faceplate, Composer 32MB sound ROM, 10 Midi Quest 13 SysEx component editors, and Web Audio synthesizer.

### Requests 2..4: Alignment & Spacing Refinements (Proteus 1000)
- **User Feedback 1:** *"can we just check spacing and alignment, etc"*
- **User Feedback 2:** *"still some slight misalignment...around the demo text and brackets and on the left hand side where the button is to select A, B , C, etc isn't central to the button"*
- **User Feedback 3:** *"nearly there...the demos bracket is overlapping the buttons and should be a fraction lower"*
- **Actions Taken:**
  - Shifted the Controller Mode button (`A-D`, `E-H`, `I-L`) to be vertically and horizontally centered with its indicators.
  - Redrew the `DEMOS` bracket in SVG with dedicated clearance between the `MASTER` / `EDIT` buttons and the middle dividing line.
  - Tuned the equidistant spacing across all 5 knobs.

### Request 5: E-MU Planet Phatt
- **User Prompt:**
  ```text
  https://www.emumania.net/wp-content/uploads/e-mu-planet-phatt-lrg-tx.jpg
  https://www.vintagesynth.com/sites/default/files/2017-05/emu_planet_phatt.jpg
  https://squest.com/Products/MidiQuest13/Instruments/E-MUPlanetPhatt/index.html
  Planet Phatt
  ```
- **Actions Taken:** Created `preview/planet_phatt.html` with metallic magenta anodized 1U faceplate, hip-hop/urban dance soundboard (Funky Drummer, 808 Sub, Moog Bass, Scratch), BEATS swing groove engine, and Midi Quest 13 component editors.

### Requests 6..7: E-MU Planet Earth & Knob Alignment
- **User Prompt:**
  ```text
  EMU Planet Earth
  https://www.emumania.net/wp-content/uploads/e-mu-planet-earth-larg-tx.jpg
  https://www.emumania.net/wp-content/uploads/e-mu-planet-earth-sml.png
  https://squest.com/Products/MidiQuest13/Instruments/E-MUPlanetEarth/index.html
  ```
- **User Feedback:** *"this looks amaziing however the knobs aren't quite in line with the arches on the left hand side ....if the knobs and their respective text could be aligned properly that would be great"*
- **Actions Taken:**
  - Built `preview/planet_earth.html` with authentic Oceanic Teal metallic chassis.
  - Fixed knob alignment: Aligned all 5 knobs (`VOLUME`, `A/E/I`, `B/F/J`, `C/G/K`, `D/H/L`) with uniform 58px column pitch.
  - Positioned the semi-circular stamped arch relief collars (`A 21 21`) directly concentric over Knobs 1..4.
  - Positioned the red parameter LEDs at the top-right (2 o'clock) of each collar.

### Requests 8..10: E-MU Orbit-3 Layout & Vector Diagram
- **User Prompt 1:**
  ```text
  emu orbit-3
  https://squest.com/Products/MidiQuest13/Instruments/E-MUPlanetEarth/index.html
  https://www.emumania.net/wp-content/uploads/e-mu-orbit-3-lrg-tx.jpg
  https://www.vintagesynth.com/sites/default/files/2017-05/emu_orbit3.jpg
  https://squest.com/Products/MidiQuest13/Instruments/E-MUOrbit3/index.html
  ```
- **User Prompt 2:** User provided official vector manual layout diagram:
  - File: `Screenshot_2026-11-22_at_23.38.55.png` (1024x124)
- **User Feedback:** *"best one yet...i think some of your alignments are a fraction off...the line through the middle isn't perfect and the two logos are slightly wrong"*
- **User Follow-up:** *"please use this image in colour https://www.emumania.net/wp-content/uploads/e-mu-orbit-3-sml.png and the uploaded image for the layout"*
- **Actions Taken:**
  - **Color Palette:** Sourced directly from `orbit-3-sml.png`:
    - Chassis: Electric canary/lemon yellow gradient (`#fff212` to `#ffea00` and `#dca000`).
    - Center Bezel: Dark matte charcoal (`#18191c`).
    - LCD Backlight: Glowing emerald green (`#026635` to `#01381c`) with `#79f7a4` matrix font.
  - **Middle Dividing Line:**
    - Exits right slant of center trapezoid bezel at $(x=740, y=60)$.
    - Traverses across the 4 button columns with a subtle $1.8^\circ$ downward slope.
    - Passes cleanly **below** the `DEMOS` bracket and text.
    - Terminates cleanly at the left rim of the circular DATA wheel housing at $(x=962, y=65)$.
    - Resumes on the right of the DATA wheel at $(x=1038, y=66)$, intersects the black round `POWER` pushbutton $(x=1052\text{ to }1076)$, and continues to the right rack ear $(x=1105, y=73)$.
  - **Center `Orbit-3` Logo:**
    - Replaced serif font with bold techno-industrial sans in crisp white (`#ffffff`).
    - Slicing through the capital `O` is a vivid fiery crimson-red orbit ring (`#dc2626` / `#ef4444`) tilted at $-32^\circ$.
  - **Far Right `≡ E-MU` Emblem:**
    - Replaced vertical stacked bars with the official horizontal E-MU mark: 3 horizontal black bars on the left (`≡`) followed by bold black `E-MU` text on the right (`≡ E-MU`).
  - **Pushbuttons & Hardware Controls:**
    - `<` and `>` cursor buttons equipped with recessed well collars and white indicator arrows.
    - Re-ordered right controls into authentic hardware hierarchy: Button Matrix $\rightarrow$ DATA Wheel $\rightarrow$ Right Sub-cluster (`≡ E-MU` on top, `POWER` switch in middle, `/ MIDI` activity LED + `POWER` silkscreen on bottom).

---

## 3. Architecture & File Manifest

### Previews Directory (`preview/`)
| File | Instrument | Key Features |
| :--- | :--- | :--- |
| `orbit_3.html` | E-MU Orbit-3 (Model 9093) | Electric Neon Yellow, Techno/Dance Soundboard, SuperBEATS, 10 Midi Quest Editors |
| `planet_earth.html` | E-MU Planet Earth (Model 9094) | Oceanic Teal, World Expedition Soundboard, 10 Midi Quest Editors |
| `planet_phatt.html` | E-MU Planet Phatt (Model 9091) | Metallic Magenta, Urban Dance / Hip Hop Soundboard, BEATS Swing Engine |
| `proteus_1000.html` | E-MU Proteus 1000 (Model 9090) | Slate Anodized, Composer 32MB Soundboard, 10 Midi Quest Editors |
| `audity_2000.html` | E-MU Audity 2000 | Deep Indigo 16-Arp Dance Synth, 10 Midi Quest Editors |
| `emu_b3.html` | E-MU B-3 (Model 9092) | Authentic B3 Organ Tonewheel & Leslie Emulation |
| `carnaval.html` | E-MU Carnaval | Latin Dance / Salsa percussion modules |
| `vintage_keys.html` | E-MU Vintage Keys (Classic) | 1993 Classic Vintage Keys 1U Faceplate |
| `vintage_pro.html` | E-MU Vintage PRO | 2002 128-Voice Classic Keys Module |
| `virtuoso_2000.html` | E-MU Virtuoso 2000 | Orchestral Module with unbroken curved swoosh line |
| `xl1.html` | E-MU XL-1 | Turbo Dance module with techno lead soundboard |
| `xl7.html` | E-MU XL-7 | Command Station desktop groovebox emulation |
| `xk6.html` | E-MU XK-6 | 61-Key Synth faceplate & interactive engine |
| `virus_a.html` | Access Virus A | Red 12-knob Virtual Analog synthesizer |
| `ax60.html` | Akai AX60 | Analog Polyphonic 6-Voice Synthesizer |
| `hardware_themed_preview.html` | Theme Switcher | Interactive multi-rack testing suite |
| `skeuomorphic_studio.html` | Studio Rack View | Full rack-stack studio visualization |
| `index.html` | OmniPatch Studio Hub | Complete Metro Synth Quest visual synthesizer manager |

### Assets & Screenshots (`assets/screenshots/`)
- `orbit_3.png`, `emu_orbit_3.png` — Exact high-resolution renders of the perfected Orbit-3 1U panel.
- `planet_earth.png`, `emu_planet_earth.png` — Renders of the Oceanic Teal Planet Earth panel.
- `planet_phatt.png`, `emu_planet_phatt.png` — Renders of the Metallic Magenta Planet Phatt panel.
- `proteus_1000.png`, `emu_proteus_1000.png` — Renders of the Proteus 1000 panel.

---

## 4. How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/dan2804/omnipatch.git
cd omnipatch
```

### 2. Launch Local Web Server
You can serve the interactive previews using any simple local HTTP server:

**Using Python 3:**
```bash
python3 -m http.server 8080
```
Then open in your browser:
- Orbit-3: [http://localhost:8080/preview/orbit_3.html](http://localhost:8080/preview/orbit_3.html)
- Planet Earth: [http://localhost:8080/preview/planet_earth.html](http://localhost:8080/preview/planet_earth.html)
- Planet Phatt: [http://localhost:8080/preview/planet_phatt.html](http://localhost:8080/preview/planet_phatt.html)
- Proteus 1000: [http://localhost:8080/preview/proteus_1000.html](http://localhost:8080/preview/proteus_1000.html)
- Studio Hub: [http://localhost:8080/preview/index.html](http://localhost:8080/preview/index.html)

**Using Node.js / npx:**
```bash
npx serve .
```

### 3. Resuming with a Local AI Assistant (Cursor / Claude Code / Cline / Aider)
When starting your local AI session, provide this document (`SESSION_CHAT_EXPORT.md`) or summarize:
> "We are continuing work on the OmniPatch repository (`https://github.com/dan2804/omnipatch`). The codebase contains authentic skeuomorphic HTML/Tailwind/Web Audio hardware previews and Midi Quest 13 SysEx editors for classic E-MU synths (Orbit-3, Planet Earth, Planet Phatt, Proteus 1000, etc.). All layout specifications, SVG contour paths, and color systems are documented in `SESSION_CHAT_EXPORT.md`."
