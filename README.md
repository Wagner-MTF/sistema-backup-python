# 🛡️ Sistema de Backup Automatizado (Multi-Modalidade)
> **Versão 3.0** | Backup inteligente com persistência de estado e logs segregados.

---

## 📋 Visão Geral
Este sistema automatiza o processo de compressão (ZIP) e movimentação de backups para as modalidades **CR**, **MG** e **CT**. Foi concebido para operar de forma autónoma, lembrando onde parou e organizando registos detalhados para cada setor.

---

## 🚀 Funcionalidades Principais

| Recurso | Descrição |
| :--- | :--- |
| **Persistência** | Utiliza o `estado_backup.json` para nunca repetir ou saltar um dia. |
| **Multi-Setor** | Processa caminhos independentes para CR, MG e CT. |
| **Logs Segregados** | Cada modalidade possui a sua própria pasta de histórico para auditoria rápida. |
| **Processamento Paralelo** | Usa *Threads* para comprimir múltiplas pastas simultaneamente. |

---

## 🛠️ Configuração do Ambiente

### 1. Estrutura do `config.json`
Certifique-se de que os caminhos utilizam barras duplas (`\\`).

```json
{
    "modalidades": {
        "CR": "E:\\DCM\\CR",
        "MG": "E:\\DCM\\MG",
        "CT": "E:\\DCM\\CT"
    },
    "caminho_destino": "C:\\Users\\User\\Documents\\BACKUP_FINAL",
    "limite_threads": 4
}

2. Agendamento no Windows
Para automação total, configure o Agendador de Tarefas:

Trigger: Diário (ex: 01:00 AM).

Ação: Iniciar um programa -> executar_backup.bat.

Diretório: No campo "Iniciar em", coloque C:\AutomacaoBackup.

📂 Organização de Logs
Os registos são salvos seguindo a estrutura:

Plaintext
logs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log

    Desenvolvido por: Wagner Matheus de Faria| Status: Estável ✅

    ---

### 🇺🇸 Versão em Inglês (`README_EN.md`)

```markdown
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

2. Windows Scheduling
For full automation, configure the Task Scheduler:

Trigger: Daily (e.g., 01:00 AM).

Action: Start a program -> executar_backup.bat.

Directory: In the "Start in" field, enter C:\AutomacaoBackup.


📂 Log Organization
Records are saved following this structure:

logs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log

    Developed by: Wagner MAtheus de Faria | Status: Stable ✅


    ---

### 🇫🇷 Versão em Francês (`README_FR.md`)

```markdown
# 🛡️ Système de Sauvegarde Automatisé (Multi-Modalité)
> **Version 3.0** | Sauvegarde intelligente avec persistance d'état et journaux séparés.

---

## 📋 Présentation Générale
Ce système automatise le processus de compression (ZIP) et le déplacement des sauvegardes pour les modalités **CR**, **MG** et **CT**. Il est conçu pour un fonctionnement autonome, mémorisant sa progression et organisant des registres détaillés pour chaque secteur.

---

## 🚀 Fonctionnalités Principales

| Fonctionnalité | Description |
| :--- | :--- |
| **Persistance** | Utilise `estado_backup.json` pour ne jamais répéter ou sauter un jour. |
| **Multi-Secteur** | Traite des chemins indépendants pour CR, MG et CT. |
| **Logs Séparés** | Chaque modalité possède son propre dossier d'historique pour un audit rapide. |
| **Traitement Parallèle** | Utilise des *Threads* para compresser plusieurs dossiers simultanément. |

---

## 🛠️ Configuration de l'Environnement

### 1. Structure du `config.json`
Assurez-vous que les chemins utilisent des doubles barres obliques inverses (`\\`).

```json
{
    "modalités": {
        "CR": "E:\\DCM\\CR",
        "MG": "E:\\DCM\\MG",
        "CT": "E:\\DCM\\CT"
    },
    "chemin_destination": "C:\\Users\\User\\Documents\\BACKUP_FINAL",
    "limite_threads": 4
}

2. Planification Windows
Pour une automatisation totale, configurez le Planificateur de tâches :

Déclencheur : Quotidien (ex : 01h00).

Action : Démarrer um programme -> executar_backup.bat.

Répertoire : Dans le champ "Commencer dans", saisissez C:\AutomacaoBackup.

📂 Organisation des Logs
Les enregistrements sont sauvegardés selon la structure suivante :

logs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log

    Développé par : Wagner Matheus de Faria| Statut : Stable ✅