[🇧🇷 Português](README.md) | [🇺🇸 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

# 🛡️ Système de Sauvegarde Automatisé (Multi-Modalité)
> **Version 3.0** | Sauvegarde intelligente avec persistance d'état et journaux séparés.

---

## 📋 Présentation Générale
Ce système automatise le processus de compression (ZIP) et le déplacement des sauvegardes pour les modalités **CR**, **MG** et **CT**. Il a été conçu pour fonctionner de manière autonome, en mémorisant sa progression et en organisant des registres détaillés pour chaque secteur.

---

## 🚀 Fonctionnalités Principales

| Fonctionnalité | Description |
| :--- | :--- |
| **Persistance** | Utilise `estado_backup.json` pour ne jamais répéter ou sauter un jour. |
| **Multi-Secteur** | Traite des chemins indépendants pour CR, MG et CT. |
| **Logs Séparés** | Chaque modalité possède son propre dossier d'historique pour un audit rapide. |
| **Traitement Parallèle** | Utilise des *Threads* pour compresser plusieurs dossiers simultanément. |

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
```

## 2. Planification Windows
Pour une automatisation totale, configurez le Planificateur de tâches :

Déclencheur : Quotidien (ex : 01h00).

Action : Démarrer un programme -> executar_backup.bat.

Commencer dans : Saisissez le chemin du dossier du projet C:\AutomacaoBackup.

## 📂 Organisation des Logs
Les enregistrements sont sauvegardés selon la structure suivante :

```
logs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log
```

Développé par : Wagner Matheus de Faria | Statut : Stable ✅