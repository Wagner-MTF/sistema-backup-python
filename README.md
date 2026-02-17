[🇧🇷 Português](README.md) | [🇺🇸 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

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

```

2. Agendamento no Windows
Para automação total, configure o Agendador de Tarefas:

Trigger: Diário (ex: 01:00 AM).

Ação: Iniciar um programa -> executar_backup.bat.

Diretório: No campo "Iniciar em", coloque C:\AutomacaoBackup.

📂 Organização de Logs
Os registos são salvos seguindo a estrutura:

logs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log

Desenvolvido por: Wagner Matheus de Faria | Status: Estável ✅