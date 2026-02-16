# 🚀 Sistema de Automação de Backup Python / Backup Automation System

[Português](#português) | [English](#english) | [Français](#français)

---

## Português

Este projeto automatiza a compactação e movimentação de backups organizados em estruturas de pastas por data (**Ano/Mês/Dia**). A versão atual permite que o usuário selecione manualmente um intervalo de dias (pastas numeradas) dentro de um mês específico.

### ⚙️ Configuração
1. **config.json**: Edite os caminhos de origem e destino (use `\\` para caminhos Windows).
   - `caminho_origem`: Onde ficam as pastas Ano/Mês/Dia.
   - `caminho_destino`: Onde os arquivos .zip serão salvos.

### 🚀 Como Usar
1. Execute o arquivo `executar_backup.bat`.
2. O sistema solicitará os seguintes dados:
   - **Ano** (ex: 2026)
   - **Mês** (ex: 1)
   - **Dia Inicial** (ex: 10)
   - **Dia Final** (ex: 20)
3. O sistema processará todas as pastas numeradas dentro desse intervalo.

---

## English

This project automates the compression and transfer of backups organized in date-based directory structures (**Year/Month/Day**). The current version allows users to manually select a range of days (numbered folders) within a specific month.

### ⚙️ Configuration
1. **config.json**: Set your source and destination paths (use `\\` for Windows).

### 🚀 How to Use
1. Run the `executar_backup.bat` file.
2. Enter the requested information:
   - **Year** (e.g., 2026)
   - **Month** (e.g., 1)
   - **Start Day** (e.g., 10)
   - **End Day** (e.g., 20)
3. The system will process all numbered folders within that range.

---

## Français

Ce projet automatise la compression et le transfert de sauvegardes organisées dans une structure de dossiers par date (**Année/Mois/Jour**). La version actuelle permet à l'utilisateur de sélectionner manuellement une plage de jours (dossiers numérotés) dans un mois spécifique.

### ⚙️ Configuration
1. **config.json** : Définissez vos chemins source et destination (utilisez `\\` pour Windows).

### 🚀 Utilisation
1. Lancez le fichier `executar_backup.bat`.
2. Saisissez les informations demandées :
   - **Année** (ex : 2026)
   - **Mois** (ex : 1)
   - **Jour de début** (ex : 10)
   - **Jour de fin** (ex : 20)
3. Le système traitera tous les dossiers numérotés dans cet intervalle.

---

📊 **Funcionalidades / Features**: Manual Range Selection | Multithreading | Error Logging