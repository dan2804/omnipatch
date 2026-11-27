# OmniPatch Hardware Ingestion Resources

This folder is the designated repository for synthesizer manuals, MIDI implementation charts, factory preset documentation, and raw SysEx dumps.

---

## Directory Layout

```
resources/
├── manuals/         <- [INBOX] Drop new synthesizer PDF user guides and manuals here
├── presets/         <- [INBOX] Drop new preset lists, text dumps, or patch sheets here
├── sysex_dumps/     <- [INBOX] Drop new raw .syx factory bank dumps or test packets here
└── processed/       <- [ARCHIVE] Reference files that have already been ingested into devices/
    ├── manuals/     <- Ingested PDF manuals and parameter tables
    └── sysex_dumps/ <- Ingested .syx bank dumps
```

---

## Ingestion Workflow

1. **Drop new files** into `resources/manuals/` or `resources/sysex_dumps/`.
2. Run or trigger ingestion via `tools/pdf_to_profile.py` or dedicated manufacturer builders.
3. Once processed, reference files are moved into `resources/processed/` so your inbox stays clean and ready for the next batch of gear!
