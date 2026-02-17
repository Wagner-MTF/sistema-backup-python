---

### 2️⃣ Arquivo: `README_EN.md` (Inglês)
```markdown
[🇧🇷 Português](README.md) | [🇺🇸 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

# 🛡️ Automated Backup System (Multi-Modality)
> **Version 3.0** | Intelligent backup with state persistence and segregated logs.

---

## 📋 Overview
This system automates the compression (ZIP) and relocation of backups for **CR**, **MG**, and **CT** modalities. It is designed for autonomous operation, remembering its last progress and maintaining detailed records for each sector.

---

## 🚀 Key Features

| Feature | Description |
| :--- | :--- |
| **Persistence** | Uses `estado_backup.json` to never repeat or skip a day. |
| **Multi-Sector** | Processes independent paths for CR, MG, and CT. |
| **Segregated Logs** | Each modality has its own history folder for quick auditing. |
| **Parallel Processing** | Uses *Threads* to compress multiple folders simultaneously. |

---

## 🛠️ Environment Setup

### 1. `config.json` Structure
Ensure that file paths use double backslashes (`\\`).

```json
{
    "modalities": {
        "CR": "E:\\DCM\\CR",
        "MG": "E:\\DCM\\MG",
        "CT": "E:\\DCM\\CT"
    },
    "destination_path": "C:\\Users\\User\\Documents\\BACKUP_FINAL",
    "thread_limit": 4
}

Developed by: Wagner Matheus de Faria | Status: Stable ✅