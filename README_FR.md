🚀 Système d'Automatisation de Sauvegarde Python
Ce projet automatise la compression et le transfert de sauvegardes organisées dans une structure de dossiers par date (Année/Mois/Jour). Il a été conçu pour gérer intelligemment l'archivage des journaux (logs) ou des documents de serveur, garantissant l'efficacité et évitant les doublons.

🛠️ Prérequis
Avant de commencer, assurez-vous d'avoir installé :

Python 3.10 ou supérieur : Télécharger ici - https://www.python.org/

Git : Pour cloner le dépôt.

📦 Installation
Clonez le dépôt :

Bash
git clone https://github.com/Wagner-MTF/sistema-backup-python.git
Accédez au dossier du projet :

Bash
cd sistema-backup-python
⚙️ Configuration
Le système utilise deux fichiers JSON pour le contrôle :

1. config.json
Modifiez ce fichier pour définir vos chemins source et destination. Note : Sur Windows, utilisez des doubles barres obliques \\.

JSON
{
    "caminho_origem": "C:\\Chemin\\De\\Votre\\Source",
    "caminho_destino": "Z:\\Votre\\Serveur\\De\\Sauvegarde",
    "limite_threads": 4
}
2. ultimo_backup.json
Ce fichier assure le suivi de la dernière date traitée. Pour commencer à partir du 01/01/2026, configurez-le avec la date du jour précédent :

JSON
{
    "ano": 2025,
    "mes": 12,
    "dia": 31
}
🚀 Utilisation
Mode Manuel
Exécutez le script directement via le terminal :

PowerShell
python main.py
Accès Facilité (Windows)
Double-cliquez sur le fichier backup.bat à la racine du projet. Cela ouvrira le terminal, lancera le processus et gardera la fenêtre ouverte pour que vous puissiez vérifier les résultats.

📊 Fonctionnalités
Multithreading : Compresse plusieurs sous-dossiers simultanément pour une vitesse maximale.

Saut de Date Automatique : Le système lit l'état actuel et passe automatiquement au jour suivant disponible.

Système de Logs : Chaque opération génère un registre détaillé dans le dossier /logs pour l'audit.

Hiérarchie Intelligente : Navigue automatiquement dans les dossiers au format Année > Mois > Jour.