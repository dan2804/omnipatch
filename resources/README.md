# OmniPatch Hardware Ingestion Resources

This folder is the designated inbox for user-supplied synthesizer manuals, MIDI implementation charts, factory preset documentation, and raw SysEx dumps.

---

## Directory Layout

```
resources/
├── manuals/         <- Drop synthesizer PDF user guides and service manuals here
├── presets/         <- Drop preset lists, patch sheet scans, or text exports here
└── sysex_dumps/     <- Drop raw .syx factory bank dumps or test packets here
```

---

## Recommended Naming Conventions

To help the automated ingestion pipeline (`tools/pdf_to_profile.py`) accurately categorize incoming hardware:

- **PDF Manuals:** `<manufacturer>_<model>_manual.pdf`  
  *Examples:*
  - `resources/manuals/roland_d50_manual.pdf`
  - `resources/manuals/yamaha_dx7_service_manual.pdf`
  - `resources/manuals/korg_m1_midi_impl.pdf`
  - `resources/manuals/waldorf_microwave_manual.pdf`
  - `resources/manuals/nord_lead_2_manual.pdf`

- **Factory Presets / Patch Sheets:** `<manufacturer>_<model>_presets.txt` (or `.json`, `.csv`)
- **Raw SysEx Bank Dumps:** `<manufacturer>_<model>_bank_<name>.syx`

---

## Automated Ingestion Pipeline

Once you place PDF manuals in `resources/manuals/`, you can tell Antigravity to ingest them, or run the built-in parser manually:

```bash
# Scan a PDF for MIDI Implementation Charts, SysEx tables, and preset lists
python3 tools/pdf_to_profile.py resources/manuals/roland_d50_manual.pdf --scan-midi

# Extract structured text to inspect parameter definitions
python3 tools/pdf_to_profile.py resources/manuals/roland_d50_manual.pdf --extract-text resources/manuals/roland_d50_extracted.txt
```

The system will parse:
1. **Manufacturer & Model Details** (Device ID, Model ID, Release Year, Architecture).
2. **MIDI Implementation Chart** (Channels, Polyphony, CC mappings, Program Change banks).
3. **SysEx Specification Table** (Parameter IDs, offsets, data bit lengths, ranges, and checksum formats).
4. **Factory Preset ROM Lists** (Preset names, categories, bank indices).
5. Output draft profiles directly into `devices/<manufacturer>/<model>/`.
