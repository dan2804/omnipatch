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

#[derive(Debug, Clone)]
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
            "CREATE TABLE IF NOT EXISTS patches (
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
    fn test_librarian_memory() {
        let db = LibrarianDb::open_in_memory().unwrap();
        let p = PatchRecord {
            id: 0,
            device_name: "Access Virus A".to_string(),
            bank_name: "Bank A".to_string(),
            patch_number: 1,
            patch_name: "Init Lead".to_string(),
            category: "Lead".to_string(),
            tags: vec!["trance".to_string(), "analog".to_string()],
            sysex_data: vec![0xF0, 0x00, 0x20, 0x33, 0xF7],
            rating: 5,
            notes: "Super fat saw lead".to_string(),
        };
        let id = db.insert_patch(&p).unwrap();
        assert_eq!(id, 1);

        let found = db.search(Some("Access Virus A"), Some("Lead")).unwrap();
        assert_eq!(found.len(), 1);
        assert_eq!(found[0].patch_name, "Init Lead");
        assert_eq!(db.total_patches().unwrap(), 1);
    }
}
