#!/usr/bin/env python3
"""
OmniPatch SQLite Librarian Database Seeder
Builds and populates omnipatch_library.db with all 34 synthesizers and 3,700+ presets,
creating normalized devices, banks, patches, and high-performance FTS5 full-text search indexes.
"""

import os
import json
import yaml
import sqlite3

DB_PATH = "omnipatch_library.db"
DEVICES_DIR = "devices"

SCHEMA = """
PRAGMA foreign_keys = ON;

-- Clean start if re-seeding
DROP TABLE IF EXISTS patches_fts;
DROP TABLE IF EXISTS patches;
DROP TABLE IF EXISTS banks;
DROP TABLE IF EXISTS devices;

-- Normalized Devices Table
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer TEXT NOT NULL,
    model TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL DEFAULT '',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Normalized Banks Table
CREATE TABLE banks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id INTEGER NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    bank_type TEXT NOT NULL DEFAULT 'ROM',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(device_id, name)
);

-- Patches Table
CREATE TABLE patches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT NOT NULL,
    bank_name TEXT NOT NULL,
    patch_number INTEGER NOT NULL,
    patch_name TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT '',
    tags TEXT NOT NULL DEFAULT '[]',
    sysex_data BLOB NOT NULL DEFAULT X'',
    rating INTEGER NOT NULL DEFAULT 0,
    notes TEXT NOT NULL DEFAULT '',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_device_bank ON patches(device_name, bank_name);
CREATE INDEX idx_patch_name ON patches(patch_name);
CREATE INDEX idx_category ON patches(category);

-- High-Performance FTS5 Full-Text Search Virtual Table
CREATE VIRTUAL TABLE patches_fts USING fts5(
    patch_name,
    category,
    tags,
    notes,
    content='patches',
    content_rowid='id'
);

-- Triggers to keep FTS5 synchronized with patches table
CREATE TRIGGER patches_ai AFTER INSERT ON patches BEGIN
    INSERT INTO patches_fts(rowid, patch_name, category, tags, notes)
    VALUES (new.id, new.patch_name, new.category, new.tags, new.notes);
END;

CREATE TRIGGER patches_ad AFTER DELETE ON patches BEGIN
    INSERT INTO patches_fts(patches_fts, rowid, patch_name, category, tags, notes)
    VALUES('delete', old.id, old.patch_name, old.category, old.tags, old.notes);
END;

CREATE TRIGGER patches_au AFTER UPDATE ON patches BEGIN
    INSERT INTO patches_fts(patches_fts, rowid, patch_name, category, tags, notes)
    VALUES('delete', old.id, old.patch_name, old.category, old.tags, old.notes);
    INSERT INTO patches_fts(rowid, patch_name, category, tags, notes)
    VALUES (new.id, new.patch_name, new.category, new.tags, new.notes);
END;
"""

def seed_database():
    print(f"[*] Initializing OmniPatch SQLite Librarian at '{DB_PATH}'...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(SCHEMA)

    total_devices = 0
    total_banks = 0
    total_patches = 0

    for root, dirs, files in os.walk(DEVICES_DIR):
        if 'profile.yaml' in files and 'factory_presets.json' in files:
            prof_path = os.path.join(root, 'profile.yaml')
            presets_path = os.path.join(root, 'factory_presets.json')

            with open(prof_path, 'r', encoding='utf-8') as f:
                prof = yaml.safe_load(f) or {}
            with open(presets_path, 'r', encoding='utf-8') as f:
                presets = json.load(f) or []

            dev_name = prof.get('model') or prof.get('name') or os.path.basename(root)
            manufacturer = prof.get('manufacturer', 'Unknown')
            category = prof.get('type') or prof.get('category') or 'Synthesizer'

            # Insert Device
            cursor.execute(
                "INSERT INTO devices (manufacturer, model, category) VALUES (?, ?, ?)",
                (manufacturer, dev_name, category)
            )
            device_id = cursor.lastrowid
            total_devices += 1

            # Normalize presets into a unified flat list of patch dicts
            patch_list = []
            if isinstance(presets, dict):
                if "banks" in presets and isinstance(presets["banks"], list):
                    for b in presets["banks"]:
                        b_name = b.get("name", "Factory ROM")
                        patches_in_bank = b.get("patches", [])
                        for item_idx, item in enumerate(patches_in_bank):
                            if isinstance(item, dict):
                                patch_list.append({
                                    'name': item.get('name', f'Preset #{item_idx+1}'),
                                    'bank': item.get('bank', b_name),
                                    'program': item.get('number', item.get('program', item_idx + 1)),
                                    'category': item.get('category', ''),
                                    'tags': item.get('tags', [])
                                })
                else:
                    for bank_title, items in presets.items():
                        if isinstance(items, list):
                            for item_idx, item in enumerate(items):
                                if isinstance(item, dict):
                                    patch_list.append({
                                        'name': item.get('name', f'Preset #{item_idx+1}'),
                                        'bank': item.get('bank', bank_title),
                                        'program': item.get('program', item.get('number', item_idx + 1)),
                                        'category': item.get('category', ''),
                                        'tags': item.get('tags', [])
                                    })
                                elif isinstance(item, str):
                                    name = item.strip()
                                    num = item_idx + 1
                                    if ':' in item:
                                        prefix, rest = item.split(':', 1)
                                        name = rest.strip()
                                    patch_list.append({
                                        'name': name,
                                        'bank': bank_title,
                                        'program': num,
                                        'category': 'SYNTH',
                                        'tags': []
                                    })
            elif isinstance(presets, list):
                for idx, p in enumerate(presets):
                    if isinstance(p, dict):
                        patch_list.append({
                            'name': p.get('name', f'Preset #{idx+1}'),
                            'bank': p.get('bank', 'Factory ROM'),
                            'program': p.get('program', p.get('number', idx + 1)),
                            'category': p.get('category', ''),
                            'tags': p.get('tags', [])
                        })
                    else:
                        patch_list.append({
                            'name': str(p),
                            'bank': 'Factory ROM',
                            'program': idx + 1,
                            'category': 'SYNTH',
                            'tags': []
                        })

            # Discover all distinct banks in this device
            bank_map = {}
            for p in patch_list:
                b_name = p['bank']
                if b_name not in bank_map:
                    cursor.execute(
                        "INSERT OR IGNORE INTO banks (device_id, name, bank_type) VALUES (?, ?, ?)",
                        (device_id, b_name, 'ROM')
                    )
                    cursor.execute("SELECT id FROM banks WHERE device_id = ? AND name = ?", (device_id, b_name))
                    b_id = cursor.fetchone()[0]
                    bank_map[b_name] = b_id
                    total_banks += 1

            # Insert Patches
            for p in patch_list:
                p_name = p['name']
                b_name = p['bank']
                p_num = p['program']
                cat = p['category']
                tags = json.dumps(p['tags'])
                notes = f"Factory preset for {dev_name}"

                cursor.execute(
                    """INSERT INTO patches 
                       (device_name, bank_name, patch_number, patch_name, category, tags, sysex_data, rating, notes)
                       VALUES (?, ?, ?, ?, ?, ?, X'', 0, ?)""",
                    (dev_name, b_name, p_num, p_name, cat, tags, notes)
                )
                total_patches += 1

    conn.commit()
    conn.close()

    print(f"\n[✓] Database Seeding Complete!")
    print(f"    • Devices: {total_devices}")
    print(f"    • Banks:   {total_banks}")
    print(f"    • Patches: {total_patches:,} indexed in SQLite & FTS5")

if __name__ == "__main__":
    seed_database()
