use anyhow::Result;
use clap::{Parser, Subcommand};
use colored::*;
use std::path::PathBuf;

use omnipatch_core::sysex::SysExMessage;
use omnipatch_librarian::{LibrarianDb, PatchRecord};
use omnipatch_midi::MidiManager;
use omnipatch_profile::ProfileRegistry;

#[derive(Parser)]
#[command(name = "omnipatch")]
#[command(about = "Modern Cross-Platform MIDI/SysEx Librarian & Patch Editor in Rust", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Inspect supported synthesizer profiles
    Devices {
        #[command(subcommand)]
        action: DevicesCommands,
    },
    /// MIDI Hardware Port management
    Midi {
        #[command(subcommand)]
        action: MidiCommands,
    },
    /// SysEx generation, testing, and debugging
    Sysex {
        #[command(subcommand)]
        action: SysexCommands,
    },
    /// Patch librarian and SQLite database
    Librarian {
        #[command(subcommand)]
        action: LibrarianCommands,
    },
}

#[derive(Subcommand)]
enum DevicesCommands {
    /// List all loaded synthesizer definition profiles
    List {
        #[arg(short, long, default_value = "devices")]
        dir: PathBuf,
    },
    /// Show detailed specifications and parameter count for a synth
    Show {
        name: String,
        #[arg(short, long, default_value = "devices")]
        dir: PathBuf,
    },
}

#[derive(Subcommand)]
enum MidiCommands {
    /// List available MIDI input and output ports
    Ports,
}

#[derive(Subcommand)]
enum SysexCommands {
    /// Format parameter change command for a synthesizer
    ParamEdit {
        device: String,
        param_id: String,
        value: i32,
    },
}

#[derive(Subcommand)]
enum LibrarianCommands {
    /// Import factory presets from a device profile into librarian DB
    ImportPresets {
        #[arg(short, long, default_value = "devices")]
        dir: PathBuf,
        #[arg(short = 'b', long, default_value = "omnipatch_library.db")]
        db: PathBuf,
    },
    /// Search librarian database
    Search {
        query: Option<String>,
        #[arg(short, long)]
        device: Option<String>,
        #[arg(short = 'b', long, default_value = "omnipatch_library.db")]
        db: PathBuf,
    },
}

fn main() -> Result<()> {
    env_logger::init();
    let cli = Cli::parse();

    match cli.command {
        Commands::Devices { action } => match action {
            DevicesCommands::List { dir } => {
                let mut registry = ProfileRegistry::new();
                let count = registry.load_dir(&dir)?;
                println!("{}", format!("=== OmniPatch Device Profiles ({} loaded) ===", count).cyan().bold());
                for prof in registry.list() {
                    println!(
                        "• {} [{}] - {} parameters",
                        prof.name.bright_green().bold(),
                        prof.manufacturer.bright_yellow(),
                        prof.parameters.len()
                    );
                }
            }
            DevicesCommands::Show { name, dir } => {
                let mut registry = ProfileRegistry::new();
                registry.load_dir(&dir)?;
                if let Some(prof) = registry.get(&name) {
                    println!("{}", format!("=== {} ===", prof.name).cyan().bold());
                    println!("Manufacturer: {}", prof.manufacturer);
                    println!("Category:     {}", prof.category);
                    if let Some(yr) = prof.release_year {
                        println!("Release Year: {}", yr);
                    }
                    if let Some(ref proto) = prof.control_protocol {
                        println!("Control Mode: {}", proto.bright_magenta());
                    }
                    println!("Parameters:   {}", prof.parameters.len());
                    println!("\nFirst 10 parameters:");
                    for (i, p) in prof.parameters.iter().take(10).enumerate() {
                        let addr = match (p.cc, p.index, p.param_id) {
                            (Some(cc), _, _) => format!("CC #{}", cc),
                            (_, Some(idx), _) => format!("Index {}", idx),
                            (_, _, Some(pid)) => format!("0x{:04X}", pid),
                            _ => "-".to_string(),
                        };
                        println!("  {:2}. {:<25} [{}]", i + 1, p.name.white(), addr.bright_yellow());
                    }
                } else {
                    eprintln!("Device '{}' not found.", name);
                }
            }
        },
        Commands::Midi { action } => match action {
            MidiCommands::Ports => {
                let mgr = MidiManager::new("OmniPatch");
                println!("{}", "=== MIDI Input Ports ===".cyan().bold());
                match mgr.list_input_ports() {
                    Ok(inputs) => {
                        if inputs.is_empty() {
                            println!("  (No hardware MIDI inputs detected)");
                        }
                        for (i, name) in inputs {
                            println!("  [{}] {}", i, name.bright_green());
                        }
                    }
                    Err(e) => eprintln!("Error querying MIDI inputs: {}", e),
                }

                println!("\n{}", "=== MIDI Output Ports ===".cyan().bold());
                match mgr.list_output_ports() {
                    Ok(outputs) => {
                        if outputs.is_empty() {
                            println!("  (No hardware MIDI outputs detected)");
                        }
                        for (i, name) in outputs {
                            println!("  [{}] {}", i, name.bright_green());
                        }
                    }
                    Err(e) => eprintln!("Error querying MIDI outputs: {}", e),
                }
            }
        },
        Commands::Sysex { action } => match action {
            SysexCommands::ParamEdit { device, param_id, value } => {
                println!("{}", format!("Generating parameter edit for {} -> {} = {}", device, param_id, value).cyan());
                if device.to_lowercase().contains("virus") {
                    // Virus A Single Edit Page A (0x70) or Page B (0x71)
                    let p_idx: u8 = param_id.parse().unwrap_or(34);
                    let val: u8 = (value as u8) & 0x7F;
                    let msg = SysExMessage::new_unchecked(vec![
                        0xF0, 0x00, 0x20, 0x33, 0x01, 0x10, 0x70, 0x40, p_idx, val, 0xF7,
                    ]);
                    println!("Raw SysEx:  {}", msg.to_hex_string().bright_yellow().bold());
                    println!("Parsed Msg: Manufacturer ID: Access Music (00 20 33)");
                } else if device.to_lowercase().contains("emax ii") || device.to_lowercase().contains("emax-ii") || device.to_lowercase().contains("emax2") {
                    // E-MU Emax II: F0 18 05 <dev> 01 <p_id> <v_lsb> <v_msb> F7
                    let pid: u8 = if param_id.starts_with("0x") {
                        u8::from_str_radix(&param_id[2..], 16).unwrap_or(0x82)
                    } else {
                        param_id.parse().unwrap_or(130)
                    };
                    let (v_lsb, v_msb) = omnipatch_core::checksum::emu::encode_14bit(value as u16);
                    let msg = SysExMessage::new_unchecked(vec![
                        0xF0, 0x18, 0x05, 0x00, 0x01, pid, v_lsb, v_msb, 0xF7,
                    ]);
                    println!("Raw SysEx:  {}", msg.to_hex_string().bright_yellow().bold());
                    println!("Parsed Msg: Manufacturer: E-mu Systems (18), Device: Emax II 16-Bit Stereo Sampler (05), Command: Parameter Edit (01)");
                } else if device.to_lowercase().contains("emax") {
                    // E-MU Emax: F0 18 02 <dev> 01 <p_id> <v_lsb> <v_msb> F7
                    let pid: u8 = if param_id.starts_with("0x") {
                        u8::from_str_radix(&param_id[2..], 16).unwrap_or(0x82)
                    } else {
                        param_id.parse().unwrap_or(130)
                    };
                    let (v_lsb, v_msb) = omnipatch_core::checksum::emu::encode_14bit(value as u16);
                    let msg = SysExMessage::new_unchecked(vec![
                        0xF0, 0x18, 0x02, 0x00, 0x01, pid, v_lsb, v_msb, 0xF7,
                    ]);
                    println!("Raw SysEx:  {}", msg.to_hex_string().bright_yellow().bold());
                    println!("Parsed Msg: Manufacturer: E-mu Systems (18), Device: Emax Sampler (02), Command: Parameter Edit (01)");
                } else if device.to_lowercase().contains("carnaval") {
                    // E-MU Carnaval: F0 18 0A <dev> 01 <p_lsb> <p_msb> <v_lsb> <v_msb> F7
                    let pid: u16 = if param_id.starts_with("0x") {
                        u16::from_str_radix(&param_id[2..], 16).unwrap_or(0x0001)
                    } else {
                        param_id.parse().unwrap_or(1)
                    };
                    let (p_lsb, p_msb) = omnipatch_core::checksum::emu::encode_14bit(pid);
                    let (v_lsb, v_msb) = omnipatch_core::checksum::emu::encode_14bit(value as u16);
                    let msg = SysExMessage::new_unchecked(vec![
                        0xF0, 0x18, 0x0A, 0x00, 0x01, p_lsb, p_msb, v_lsb, v_msb, 0xF7,
                    ]);
                    println!("Raw SysEx:  {}", msg.to_hex_string().bright_yellow().bold());
                    println!("Parsed Msg: Manufacturer: E-mu Systems (18), Device: Carnaval (0A), Command: Param Edit (01)");
                } else if device.to_lowercase().contains("audity") || device.to_lowercase().contains("b3") || device.to_lowercase().contains("b-3") || device.to_lowercase().contains("proteus") || device.to_lowercase().contains("xl-1") || device.to_lowercase().contains("xl1") || device.to_lowercase().contains("xtreme") || device.to_lowercase().contains("xl-7") || device.to_lowercase().contains("xl7") || device.to_lowercase().contains("command") {
                    let pid: u16 = if param_id.starts_with("0x") {
                        u16::from_str_radix(&param_id[2..], 16).unwrap_or(0x0180)
                    } else {
                        param_id.parse().unwrap_or(0x0180)
                    };
                    let (p_lsb, p_msb) = omnipatch_core::checksum::emu::encode_14bit(pid);
                    let (v_lsb, v_msb) = omnipatch_core::checksum::emu::encode_14bit(value as u16);
                    let msg = SysExMessage::new_unchecked(vec![
                        0xF0, 0x18, 0x0F, 0x00, 0x55, 0x01, 0x02, p_lsb, p_msb, v_lsb, v_msb, 0xF7,
                    ]);
                    println!("Raw SysEx:  {}", msg.to_hex_string().bright_yellow().bold());
                    println!("Parsed Msg: Manufacturer: E-mu Systems (18), Device: Proteus/Command Station Family (0F)");
                } else if device.to_lowercase().contains("ax60") {
                    let cc: u8 = param_id.parse().unwrap_or(74);
                    println!("AX60 (Tauntek): Real-time parameter transmitted via MIDI CC:");
                    println!("Raw MIDI:   {}", format!("B0 {:02X} {:02X}", cc, value & 0x7F).bright_yellow().bold());
                }
            }
        },
        Commands::Librarian { action } => match action {
            LibrarianCommands::ImportPresets { dir, db } => {
                let mut registry = ProfileRegistry::new();
                registry.load_dir(&dir)?;
                let librarian = LibrarianDb::open(&db)?;
                let mut total_imported = 0;

                for prof in registry.list() {
                    if let Some(ref banks) = prof.factory_presets {
                        for (bank_name, presets) in banks {
                            for (idx, p_entry) in presets.iter().enumerate() {
                                let record = PatchRecord {
                                    id: 0,
                                    device_name: prof.name.clone(),
                                    bank_name: bank_name.clone(),
                                    patch_number: idx as i32,
                                    patch_name: p_entry.display_name().to_string(),
                                    category: p_entry.category_name().unwrap_or("").to_string(),
                                    tags: vec![],
                                    sysex_data: vec![],
                                    rating: 0,
                                    notes: "Imported factory preset".to_string(),
                                };
                                librarian.insert_patch(&record)?;
                                total_imported += 1;
                            }
                        }
                    }
                }
                println!("{}", format!("Successfully imported {} presets into {}", total_imported, db.display()).bright_green().bold());
            }
            LibrarianCommands::Search { query, device, db } => {
                let librarian = LibrarianDb::open(&db)?;
                let results = librarian.search(device.as_deref(), query.as_deref())?;
                println!("{}", format!("Found {} matching patches in {}:", results.len(), db.display()).cyan().bold());
                for (i, p) in results.iter().take(25).enumerate() {
                    println!(
                        "  {:3}. [{}] {} / #{:03}: {}",
                        i + 1,
                        p.device_name.bright_green(),
                        p.bank_name.bright_yellow(),
                        p.patch_number,
                        p.patch_name.white().bold()
                    );
                }
                if results.len() > 25 {
                    println!("  ... and {} more patches", results.len() - 25);
                }
            }
        },
    }

    Ok(())
}
