use std::collections::HashMap;
use std::fs;
use std::path::Path;
use thiserror::Error;

use crate::model::DeviceProfile;

#[derive(Error, Debug)]
pub enum ProfileError {
    #[error("I/O error reading device file: {0}")]
    Io(#[from] std::io::Error),
    #[error("YAML parse error in device profile '{path}': {source}")]
    Yaml {
        path: String,
        source: serde_yaml::Error,
    },
}

#[derive(Default)]
pub struct ProfileRegistry {
    pub profiles: HashMap<String, DeviceProfile>,
}

impl ProfileRegistry {
    pub fn new() -> Self {
        Self {
            profiles: HashMap::new(),
        }
    }

    /// Load a single .yaml device profile from path
    pub fn load_file<P: AsRef<Path>>(&mut self, path: P) -> Result<String, ProfileError> {
        let p = path.as_ref();
        let content = fs::read_to_string(p)?;
        let mut profile: DeviceProfile = serde_yaml::from_str(&content).map_err(|e| ProfileError::Yaml {
            path: p.display().to_string(),
            source: e,
        })?;

        // If factory_presets is empty, check for companion factory_presets.json in the same directory
        if profile.factory_presets.is_none() {
            if let Some(parent) = p.parent() {
                let presets_path = parent.join("factory_presets.json");
                if presets_path.is_file() {
                    if let Ok(json_str) = fs::read_to_string(&presets_path) {
                        if let Ok(banks) = serde_json::from_str(&json_str) {
                            profile.factory_presets = Some(banks);
                        }
                    }
                }
            }
        }

        let name = profile.name.clone();
        self.profiles.insert(name.clone(), profile);
        Ok(name)
    }

    /// Recursively load all .yaml files in a directory and any subdirectories
    pub fn load_dir<P: AsRef<Path>>(&mut self, dir: P) -> Result<usize, ProfileError> {
        let mut count = 0;
        self.load_dir_recursive(dir.as_ref(), &mut count)?;
        Ok(count)
    }

    fn load_dir_recursive(&mut self, dir: &Path, count: &mut usize) -> Result<(), ProfileError> {
        if dir.is_dir() {
            let mut entries: Vec<_> = fs::read_dir(dir)?.filter_map(|e| e.ok()).collect();
            entries.sort_by_key(|e| e.path());
            for entry in entries {
                let path = entry.path();
                if path.is_dir() {
                    self.load_dir_recursive(&path, count)?;
                } else if path.extension().and_then(|ext| ext.to_str()) == Some("yaml") {
                    match self.load_file(&path) {
                        Ok(_) => *count += 1,
                        Err(e) => {
                            log::warn!("Failed loading profile from {:?}: {}", path, e);
                        }
                    }
                }
            }
        }
        Ok(())
    }

    pub fn get(&self, name: &str) -> Option<&DeviceProfile> {
        self.profiles.get(name)
    }

    pub fn list(&self) -> Vec<&DeviceProfile> {
        self.profiles.values().collect()
    }

    pub fn all(&self) -> Vec<&DeviceProfile> {
        self.profiles.values().collect()
    }
}
