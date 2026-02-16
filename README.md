🚀 Sistema de Automação de Backup Python
Este projeto automatiza a compactação e movimentação de backups organizados em estruturas de pastas por data (Ano/Mês/Dia). Ele foi desenvolvido para facilitar o arquivamento de logs ou documentos de servidores de forma inteligente, evitando duplicidade.

🛠️ Requisitos
Antes de começar, você precisará ter instalado:

Python 3.10 ou superior: Baixar aqui - https://www.python.org/

Git: Para clonar o repositório.

📦 Instalação
Clone o repositório:

Bash
git clone https://github.com/Wagner-MTF/sistema-backup-python.git
Acesse a pasta do projeto:

Bash
cd sistema-backup-python
⚙️ Configuração
O sistema utiliza dois arquivos JSON para controle:

1. config.json
Edite este arquivo para definir os caminhos de origem e destino. Nota: No Windows, use barras duplas \\.

JSON
{
    "caminho_origem": "C:\\Caminho\\Da\\Sua\\Origem",
    "caminho_destino": "Z:\\Seu\\Servidor\\De\\Backup",
    "limite_threads": 4
}
2. ultimo_backup.json
Este arquivo controla de qual data o sistema deve partir. Se quiser começar do dia 01/01/2026, configure-o com a data do dia anterior:

JSON
{
    "ano": 2025,
    "mes": 12,
    "dia": 31
}
🚀 Como Usar
Modo Manual
Você pode rodar o script diretamente pelo terminal:

PowerShell
python main.py
Modo Facilitado (Windows)
Basta dar dois cliques no arquivo backup.bat na raiz do projeto. Ele abrirá o terminal, executará o processo e manterá a janela aberta para você conferir os logs.

📊 Funcionalidades
Multithreading: Compacta várias subpastas simultaneamente para ganhar velocidade.

Pulo de Data Automático: O sistema lê o estado atual e pula para o próximo dia disponível.

Sistema de Logs: Cada operação gera um registro na pasta /logs para auditoria.

Estrutura Inteligente: Navega automaticamente em pastas no formato Ano > Mes > Dia.