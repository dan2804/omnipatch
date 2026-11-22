pub mod commands;

pub use commands::*;

#[cfg(feature = "tauri-app")]
pub fn run() {
    tauri::Builder::default()
        .setup(|_app| {
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
