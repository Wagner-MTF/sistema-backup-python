import os
import zipfile
import logging
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# 1. Carregar Configurações
def carregar_config():
    with open('config.json', 'r') as f:
        return json.load(f)

# 2. Configurar Logging
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(
    filename=f'logs/backup_{datetime.now().strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def zipar_e_mover(caminho_pasta, nome_zip, destino):
    try:
        caminho_final_zip = os.path.join(destino, f"{nome_zip}.zip")
        with zipfile.ZipFile(caminho_final_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for raiz, _, arquivos in os.walk(caminho_pasta):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    arcname = os.path.relpath(caminho_completo, caminho_pasta)
                    zipf.write(caminho_completo, arcname)
        logging.info(f"Sucesso: {nome_zip}")
        return True
    except Exception as e:
        logging.error(f"Erro em {nome_zip}: {str(e)}")
        return False

def executar_sistema():
    config = carregar_config()
    modalidades = config['modalidades']
    destino = config['caminho_destino']
    
    print("\n==========================================")
    print("      SISTEMA DE BACKUP POR MODALIDADE    ")
    print("==========================================")
    print("Opções: CR, MG, CT ou TODAS")
    escolha = input("👉 Escolha a modalidade: ").upper().strip()

    # Define quais caminhos serão processados
    pastas_para_processar = {}
    if escolha == "TODAS":
        pastas_para_processar = modalidades
    elif escolha in modalidades:
        pastas_para_processar = {escolha: modalidades[escolha]}
    else:
        print(f"❌ Opção '{escolha}' inválida!")
        return

    ano = input("📅 Digite o ANO (ex: 2026): ").strip()
    mes = input("📂 Digite o MÊS (ex: 1): ").strip()
    dia_inicio = int(input("🔢 Dia INICIAL: "))
    dia_fim = int(input("🔢 Dia FINAL: "))

    for mod, caminho_base in pastas_para_processar.items():
        print(f"\n--- 📁 Processando Modalidade: {mod} ---")
        
        for dia in range(dia_inicio, dia_fim + 1):
            # Monta o caminho garantindo que não haja espaços extras
            caminho_dia = os.path.join(caminho_base.strip(), str(ano), str(mes), str(dia))

            # Exibe o caminho para você conferir se está correto
            print(f"🔍 Tentando acessar: {caminho_dia}")

            if os.path.exists(caminho_dia):
                subpastas = [os.path.join(caminho_dia, f) for f in os.listdir(caminho_dia) 
                             if os.path.isdir(os.path.join(caminho_dia, f))]

                if subpastas:
                    print(f"✅ Dia {dia}: {len(subpastas)} pastas encontradas.")
                    with ThreadPoolExecutor(max_workers=config['limite_threads']) as executor:
                        for pasta in subpastas:
                            nome_zip = f"Backup_{mod}_{ano}_{mes}_{dia}_{os.path.basename(pasta)}"
                            executor.submit(zipar_e_mover, pasta, nome_zip, destino)
                else:
                    print(f"⚠️ Dia {dia}: Pasta encontrada, mas está vazia.")
            else:
                print(f"📂 Dia {dia}: Não encontrado. (Verifique se o caminho acima existe)")

    print("\n==========================================")
    print("      PROCESSO CONCLUÍDO COM SUCESSO!     ")
    print("==========================================\n")

if __name__ == "__main__":
    executar_sistema()