🛡️ Sistema de Backup Automatizado (Multi-Modalidade)Versão 3.0 | Backup inteligente com persistência de estado e logs segregados.📋 Visão GeralEste sistema automatiza o processo de compressão (ZIP) e movimentação de backups para as modalidades CR, MG e CT. Ele foi projetado para operar de forma autônoma, lembrando onde parou e organizando registros detalhados para cada setor.🚀 Funcionalidades PrincipaisRecursoDescriçãoPersistênciaUtiliza o estado_backup.json para nunca repetir ou pular um dia.Multi-SetorProcessa caminhos independentes para CR, MG e CT.Logs SegregadosCada modalidade possui sua própria pasta de histórico para auditoria rápida.Processamento ParaleloUsa Threads para comprimir múltiplas pastas simultaneamente.🛠️ Configuração do Ambiente1. Estrutura do config.jsonCertifique-se de que os caminhos utilizam barras duplas (\\).JSON{
    "modalidades": {
        "CR": "E:\\DCM\\CR",
        "MG": "E:\\DCM\\MG",
        "CT": "E:\\DCM\\CT"
    },
    "caminho_destino": "C:\\Users\\User\\Documents\\BACKUP_FINAL",
    "limite_threads": 4
}
2. Agendamento no WindowsPara automação total, configure o Agendador de Tarefas:Trigger: Diário (ex: 01:00 AM).Ação: Iniciar um programa -> executar_backup.bat.Diretório: No campo "Iniciar em", coloque C:\AutomacaoBackup.🌎 Idiomas / Languages / Langues🇧🇷 PortuguêsO sistema verifica o arquivo de estado. Se o último backup foi 2026-02-15, ele tentará processar 2026-02-16. Caso a pasta do dia ainda não exista, ele aguardará a próxima execução programada.🇺🇸 EnglishThe system checks the state file. If the last backup was 2026-02-15, it will automatically target 2026-02-16. If the folder for that day doesn't exist yet, it will skip and wait for the next scheduled run.🇫🇷 FrançaisLe système consulte le fichier d'état. Si la dernière sauvegarde était le 2026-02-15, il ciblera 2026-02-16. Si le dossier du jour n'existe pas encore, il attendra la prochaine exécution prévue.📂 Organização de LogsOs registros são salvos seguindo a estrutura:Plaintextlogs/
├── CR/
│   └── backup_2026-02.log
├── MG/
│   └── backup_2026-02.log
└── CT/
    └── backup_2026-02.log
Desenvolvido por: Wagner | Status: Estável ✅