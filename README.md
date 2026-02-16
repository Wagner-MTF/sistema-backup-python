# 🚀 Sistema de Automação de Backup Python / Backup Automation System

[Português](#português) | [English](#english) | [Français](#français)

---

## Português

Este projeto automatiza a compactação e movimentação de backups organizados em estruturas de pastas por data (**Ano/Mês/Dia**). Ele foi desenvolvido para facilitar o arquivamento de logs ou documentos de servidores de forma inteligente, evitando duplicidade.

### 🛠️ Requisitos
* **Python 3.10 ou superior**: [Baixar aqui](https://www.python.org/)
* **Git**: Para clonar o repositório.

### ⚙️ Configuração
1. **config.json**: Edite os caminhos de origem e destino (use `\\`).
2. **ultimo_backup.json**: Define a data de partida (coloque a data do dia anterior ao desejado).

### 🚀 Como Usar
* **Modo Facilitado**: Dê dois cliques no arquivo `executar_backup.bat`.
* **Modo Manual**: Execute `python main.py` no terminal.

---

## English

This project automates the compression and transfer of backups organized in date-based directory structures (**Year/Month/Day**).

### 🛠️ Requirements
* **Python 3.10+**
* **Git**

### ⚙️ Configuration
1. **config.json**: Set your source and destination paths.
2. **ultimo_backup.json**: Set the starting point date.

### 🚀 How to Use
* **Easy Mode**: Double-click the `executar_backup.bat` file.
* **Manual Mode**: Run `python main.py` in the terminal.

---

## Français

Ce projet automatise la compression et le transfert de sauvegardes organisées dans une structure de dossiers par date (**Année/Mois/Jour**).

### 🛠️ Prérequis
* **Python 3.10+**
* **Git**

### ⚙️ Configuration
1. **config.json** : Définissez vos chemins source et destination.
2. **ultimo_backup.json** : Définissez la date de début.

### 🚀 Utilisation
* **Mode Facile** : Double-cliquez sur le fichier `executar_backup.bat`.
* **Mode Manuel** : Exécutez `python main.py` dans le terminal.

---

📊 **Funcionalidades / Features**: Multithreading | Auto Date Skip | Logging System