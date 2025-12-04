# EasySave — Backup Tool

EasySave is a backup application written in C#/.NET with a WPF interface and a clean MVVM architecture.  
It started as a school project, but I built it with production rules: clear separation, logging, safe operations, and predictable behavior.

[GitHub](https://github.com/ntino67/FISE_A3_SE_ENGEL_Axel)

---

## Features

- Multiple backup jobs (full, differential, custom)
- WPF interface with MVVM, data binding, view-model separation
- Job configuration with real-time validation
- Logging, progress tracking, and status persistence
- Encryption through an external CLI tool (CryptoSoft)
- Settings stored cleanly and reloadable

---

## Architecture

- **MVVM** for clean separation of UI and logic
- **Services** for I/O, encryption, scheduling
- **Models** for job definitions and state
- **ViewModels** connecting the UI to core logic

The structure was designed to scale without becoming tangled.

---

## Why this project matters

This project taught me to treat even small assignments like real products:

- UI patterns (MVVM, binding, commands)
- Maintaining a predictable and reproducible build
- Designing components that stay understandable months later
- Handling user input and external tooling safely

---

## Links

- [Back to Projects](/projects/)
