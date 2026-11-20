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
        let profile: DeviceProfile = serde_yaml::from_str(&content).map_err(|e| ProfileError::Yaml {
            path: p.display().to_string(),
            source: e,
        })?;
        let name = profile.name.clone();
        self.profiles.insert(name.clone(), profile);
        Ok(name)
    }

    /// Load all .yaml files in a directory
    pub fn load_dir<P: AsRef<Path>>(&mut self, dir: P) -> Result<usize, ProfileError> {
        let mut count = 0;
        let p = dir.as_ref();
        if p.is_dir() {
            for entry in fs::read_dir(p)? {
                let entry = entry?;
                let path = entry.path();
                if path.extension().and_then(|ext| ext.to_str()) == Some("yaml") {
                    match self.load_file(&path) {
                        Ok(_) => count += 1,
                        Err(e) => {
                            log::warn!("Failed loading profile from {:?}: {}", path, e);
                        }
                    }
                }
            }
        }
        Ok(count)
    }

    pub fn get(&self, name: &str) -> Option<&DeviceProfile> {
        self.profiles.get(name)
    }

    pub fn list(&self) -> Vec<&DeviceProfile> {
        self.profiles.values().collect()
    }
}
