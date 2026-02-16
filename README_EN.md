🚀 Python Backup Automation System
This project automates the compression and transfer of backups organized in a date-based directory structure (Year/Month/Day). It was designed to handle server logs or documents intelligently, ensuring efficiency and preventing duplicates.

🛠️ Requirements
Before starting, ensure you have:

Python 3.10 or higher: Download here - https://www.python.org/

Git: To clone the repository.

📦 Installation
Clone the repository:

Bash
git clone https://github.com/Wagner-MTF/sistema-backup-python.git
Enter the project folder:

Bash
cd sistema-backup-python
⚙️ Configuration
The system uses two JSON files for control:

1. config.json
Edit this file to define your source and destination paths. Note: On Windows, use double backslashes \\.

JSON
{
    "caminho_origem": "C:\\Path\\To\\Your\\Source",
    "caminho_destino": "Z:\\Your\\Backup\\Server",
    "limite_threads": 4
}
2. ultimo_backup.json
This file keeps track of the last processed date. To start from 2026-01-01, set it to the previous day:

JSON
{
    "ano": 2025,
    "mes": 12,
    "dia": 31
}
🚀 How to Use
Manual Mode
Run the script directly via terminal:

PowerShell
python main.py
Easy Access (Windows)
Double-click the backup.bat file in the project root. It will open the terminal, run the process, and keep the window open for you to check the results.

📊 Features
Multithreading: Compresses multiple subfolders simultaneously for maximum speed.

Automatic Date Skip: The system reads the current state and automatically moves to the next available day.

Logging System: Every operation generates a detailed log in the /logs folder for auditing.

Smart Hierarchy: Automatically navigates folders in Year > Month > Day format.