use serde::{Deserialize, Serialize};
use std::path::Path;
use rusqlite::{params, Connection};
use thiserror::Error;

#[derive(Error, Debug)]
pub enum LibrarianError {
    #[error("Database error: {0}")]
    Sqlite(#[from] rusqlite::Error),
    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),
    #[error("Patch not found: id {0}")]
    NotFound(i64),
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PatchRecord {
    pub id: i64,
    pub device_name: String,
    pub bank_name: String,
    pub patch_number: i32,
    pub patch_name: String,
    pub category: String,
    pub tags: Vec<String>,
    pub sysex_data: Vec<u8>,
    pub rating: i32,
    pub notes: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DeviceRecord {
    pub id: i64,
    pub manufacturer: String,
    pub model: String,
    pub category: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BankRecord {
    pub id: i64,
    pub device_id: i64,
    pub name: String,
    pub bank_type: String, // "ROM", "RAM", "Cartridge", "User"
}

pub struct LibrarianDb {
    conn: Connection,
}

impl LibrarianDb {
    /// Initialize in-memory or on-disk SQLite database
    pub fn open<P: AsRef<Path>>(path: P) -> std::result::Result<Self, LibrarianError> {
        let conn = Connection::open(path)?;
        let mut db = Self { conn };
        db.init_schema()?;
        Ok(db)
    }

    pub fn open_in_memory() -> std::result::Result<Self, LibrarianError> {
        let conn = Connection::open_in_memory()?;
        let mut db = Self { conn };
        db.init_schema()?;
        Ok(db)
    }

    fn init_schema(&mut self) -> std::result::Result<(), LibrarianError> {
        self.conn.execute_batch(
            "PRAGMA foreign_keys = ON;

            -- Normalized Devices Table
            CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                manufacturer TEXT NOT NULL,
                model TEXT NOT NULL UNIQUE,
                category TEXT NOT NULL DEFAULT '',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            -- Normalized Banks Table
            CREATE TABLE IF NOT EXISTS banks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id INTEGER NOT NULL REFERENCES devices(id) ON DELETE CASCADE,
                name TEXT NOT NULL,
                bank_type TEXT NOT NULL DEFAULT 'RAM',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(device_id, name)
            );

            -- Patches Table
            CREATE TABLE IF NOT EXISTS patches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_name TEXT NOT NULL,
                bank_name TEXT NOT NULL,
                patch_number INTEGER NOT NULL,
                patch_name TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT '',
                tags TEXT NOT NULL DEFAULT '[]',
                sysex_data BLOB NOT NULL,
                rating INTEGER NOT NULL DEFAULT 0,
                notes TEXT NOT NULL DEFAULT '',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            CREATE INDEX IF NOT EXISTS idx_device_bank ON patches(device_name, bank_name);
            CREATE INDEX IF NOT EXISTS idx_patch_name ON patches(patch_name);
            CREATE INDEX IF NOT EXISTS idx_category ON patches(category);

            -- High-Performance FTS5 Full-Text Search Virtual Table
            CREATE VIRTUAL TABLE IF NOT EXISTS patches_fts USING fts5(
                patch_name,
                category,
                tags,
                notes,
                content='patches',
                content_rowid='id'
            );

            -- Triggers to keep FTS5 synchronized with patches table
            CREATE TRIGGER IF NOT EXISTS patches_ai AFTER INSERT ON patches BEGIN
                INSERT INTO patches_fts(rowid, patch_name, category, tags, notes)
                VALUES (new.id, new.patch_name, new.category, new.tags, new.notes);
            END;

            CREATE TRIGGER IF NOT EXISTS patches_ad AFTER DELETE ON patches BEGIN
                INSERT INTO patches_fts(patches_fts, rowid, patch_name, category, tags, notes)
                VALUES('delete', old.id, old.patch_name, old.category, old.tags, old.notes);
            END;

            CREATE TRIGGER IF NOT EXISTS patches_au AFTER UPDATE ON patches BEGIN
                INSERT INTO patches_fts(patches_fts, rowid, patch_name, category, tags, notes)
                VALUES('delete', old.id, old.patch_name, old.category, old.tags, old.notes);
                INSERT INTO patches_fts(rowid, patch_name, category, tags, notes)
                VALUES (new.id, new.patch_name, new.category, new.tags, new.notes);
            END;
            "
        )?;
        Ok(())
    }

    pub fn insert_patch(&self, patch: &PatchRecord) -> std::result::Result<i64, LibrarianError> {
        let tags_json = serde_json::to_string(&patch.tags)?;
        self.conn.execute(
            "INSERT INTO patches (device_name, bank_name, patch_number, patch_name, category, tags, sysex_data, rating, notes)
             VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9)",
            params![
                patch.device_name,
                patch.bank_name,
                patch.patch_number,
                patch.patch_name,
                patch.category,
                tags_json,
                patch.sysex_data,
                patch.rating,
                patch.notes
            ],
        )?;
        Ok(self.conn.last_insert_rowid())
    }

    /// Fast tokenized search across all fields using SQLite FTS5 engine
    pub fn search_fts(&self, query: &str) -> std::result::Result<Vec<PatchRecord>, LibrarianError> {
        let mut stmt = self.conn.prepare(
            "SELECT p.id, p.device_name, p.bank_name, p.patch_number, p.patch_name, p.category, p.tags, p.sysex_data, p.rating, p.notes
             FROM patches_fts f
             JOIN patches p ON p.id = f.rowid
             WHERE patches_fts MATCH :query
             ORDER BY rank"
        )?;

        let formatted_query = if query.contains(' ') || query.contains('*') {
            query.to_string()
        } else {
            format!("{}*", query) // Prefix match for real-time typeahead
        };

        let rows = stmt.query_map(params![formatted_query], |row| {
            let tags_str: String = row.get(6)?;
            let tags: Vec<String> = serde_json::from_str(&tags_str).unwrap_or_default();
            Ok(PatchRecord {
                id: row.get(0)?,
                device_name: row.get(1)?,
                bank_name: row.get(2)?,
                patch_number: row.get(3)?,
                patch_name: row.get(4)?,
                category: row.get(5)?,
                tags,
                sysex_data: row.get(7)?,
                rating: row.get(8)?,
                notes: row.get(9)?,
            })
        })?;

        let mut results = Vec::new();
        for r in rows {
            results.push(r?);
        }
        Ok(results)
    }

    /// Standard filtered search by device name and/or keyword query
    pub fn search(&self, device: Option<&str>, query: Option<&str>) -> std::result::Result<Vec<PatchRecord>, LibrarianError> {
        let mut sql = "SELECT id, device_name, bank_name, patch_number, patch_name, category, tags, sysex_data, rating, notes FROM patches WHERE 1=1".to_string();
        if device.is_some() {
            sql.push_str(" AND device_name = :device");
        }
        if query.is_some() {
            sql.push_str(" AND (patch_name LIKE :query OR category LIKE :query OR tags LIKE :query)");
        }
        sql.push_str(" ORDER BY device_name, bank_name, patch_number ASC");

        let mut stmt = self.conn.prepare(&sql)?;
        let query_param = query.map(|q| format!("%{}%", q));
        
        let mut named_params: Vec<(&str, &dyn rusqlite::ToSql)> = Vec::new();
        if let Some(ref dev) = device {
            named_params.push((":device", dev));
        }
        if let Some(ref q) = query_param {
            named_params.push((":query", q));
        }

        let rows = stmt.query_map(named_params.as_slice(), |row| {
            let tags_str: String = row.get(6)?;
            let tags: Vec<String> = serde_json::from_str(&tags_str).unwrap_or_default();
            Ok(PatchRecord {
                id: row.get(0)?,
                device_name: row.get(1)?,
                bank_name: row.get(2)?,
                patch_number: row.get(3)?,
                patch_name: row.get(4)?,
                category: row.get(5)?,
                tags,
                sysex_data: row.get(7)?,
                rating: row.get(8)?,
                notes: row.get(9)?,
            })
        })?;

        let mut results = Vec::new();
        for r in rows {
            results.push(r?);
        }
        Ok(results)
    }

    pub fn total_patches(&self) -> std::result::Result<usize, LibrarianError> {
        let count: i64 = self.conn.query_row("SELECT COUNT(*) FROM patches", [], |row| row.get(0))?;
        Ok(count as usize)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_librarian_memory_and_fts5() {
        let db = LibrarianDb::open_in_memory().unwrap();
        let p1 = PatchRecord {
            id: 0,
            device_name: "Access Virus A".to_string(),
            bank_name: "Bank A".to_string(),
            patch_number: 1,
            patch_name: "HyperSaw Lead".to_string(),
            category: "Lead".to_string(),
            tags: vec!["trance".to_string(), "analog".to_string(), "rave".to_string()],
            sysex_data: vec![0xF0, 0x00, 0x20, 0x33, 0xF7],
            rating: 5,
            notes: "Classic super-saw trance pluck lead".to_string(),
        };
        let p2 = PatchRecord {
            id: 0,
            device_name: "Casio CZ-1".to_string(),
            bank_name: "Preset Bank A".to_string(),
            patch_number: 1,
            patch_name: "Warm Brass Ensemble".to_string(),
            category: "Brass".to_string(),
            tags: vec!["phase-distortion".to_string(), "warm".to_string()],
            sysex_data: vec![0xF0, 0x44, 0x00, 0x00, 0x70, 0xF7],
            rating: 4,
            notes: "Iconic 16 DCO brass ensemble with stereo chorus".to_string(),
        };

        db.insert_patch(&p1).unwrap();
        db.insert_patch(&p2).unwrap();

        assert_eq!(db.total_patches().unwrap(), 2);

        // Test standard search
        let found = db.search(Some("Access Virus A"), Some("Lead")).unwrap();
        assert_eq!(found.len(), 1);
        assert_eq!(found[0].patch_name, "HyperSaw Lead");

        // Test FTS5 instant search across patch names
        let fts_lead = db.search_fts("HyperSaw").unwrap();
        assert_eq!(fts_lead.len(), 1);
        assert_eq!(fts_lead[0].patch_name, "HyperSaw Lead");

        // Test FTS5 instant search across notes
        let fts_chorus = db.search_fts("chorus").unwrap();
        assert_eq!(fts_chorus.len(), 1);
        assert_eq!(fts_chorus[0].device_name, "Casio CZ-1");

        // Test FTS5 instant search across tags
        let fts_trance = db.search_fts("trance").unwrap();
        assert_eq!(fts_trance.len(), 1);
    }
}
