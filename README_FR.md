---

### 3️⃣ Arquivo: `README_FR.md` (Francês)
```markdown
[🇧🇷 Português](README.md) | [🇺🇸 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

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
| **Traitement Parallèle** | Utilise des *Threads* pour compresser plusieurs dossiers simultanément. |

---
**Développé par :** Wagner Matheus de Faria | **Statut :** Stable ✅