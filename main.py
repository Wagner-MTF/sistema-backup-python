import os
import zipfile
import logging
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

ESTADO_FILE = 'estado_backup.json'

def carregar_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def carregar_estado():
    if os.path.exists(ESTADO_FILE):
        with open(ESTADO_FILE, 'r') as f:
            return json.load(f)
    return {}

def salvar_estado(estado):
    with open(ESTADO_FILE, 'w') as f:
        json.dump(estado, f, indent=4)

def configurar_log(modalidade):
    pasta_log = os.path.join('logs', modalidade)
    if not os.path.exists(pasta_log): os.makedirs(pasta_log)
    
    log_file = os.path.join(pasta_log, f"backup_{datetime.now().strftime('%Y-%m')}.log")
    
    # Criar um logger específico para a modalidade
    logger = logging.getLogger(modalidade)
    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def zipar_e_mover(caminho_pasta, nome_zip, destino, logger):
    try:
        caminho_final_zip = os.path.join(destino, f"{nome_zip}.zip")
        with zipfile.ZipFile(caminho_final_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for raiz, _, arquivos in os.walk(caminho_pasta):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    arcname = os.path.relpath(caminho_completo, caminho_pasta)
                    zipf.write(caminho_completo, arcname)
        logger.info(f"Sucesso: {nome_zip}")
        return True
    except Exception as e:
        logger.error(f"Erro em {nome_zip}: {str(e)}")
        return False

def executar_sistema():
    config = carregar_config()
    estado = carregar_estado()
    modalidades = config['modalidades']
    destino = config['caminho_destino']
    
    print("\n[MODO AGENDAMENTO ATIVADO]")

    for mod, caminho_base in modalidades.items():
        logger = configurar_log(mod)
        print(f"\n--- Verificando Modalidade: {mod} ---")
        
        # Recupera onde parou ou começa de uma data padrão (ex: ontem)
        if mod in estado:
            ultima_data = datetime.strptime(estado[mod], "%Y-%m-%d")
            data_para_rodar = ultima_data + timedelta(days=1)
        else:
            # Se não tem histórico, tenta rodar o dia anterior ao de hoje
            data_para_rodar = datetime.now() - timedelta(days=1)

        ano, mes, dia = data_para_rodar.year, data_para_rodar.month, data_para_rodar.day
        caminho_dia = os.path.join(caminho_base, str(ano), str(mes), str(dia))

        print(f"🔍 Procurando pasta: {caminho_dia}")

        if os.path.exists(caminho_dia):
            subpastas = [os.path.join(caminho_dia, f) for f in os.listdir(caminho_dia) 
                         if os.path.isdir(os.path.join(caminho_dia, f))]

            if subpastas:
                print(f"🚀 {len(subpastas)} pastas encontradas para {mod}. Zipando...")
                with ThreadPoolExecutor(max_workers=config['limite_threads']) as executor:
                    for pasta in subpastas:
                        nome_zip = f"Backup_{mod}_{ano}_{mes}_{dia}_{os.path.basename(pasta)}"
                        executor.submit(zipar_e_mover, pasta, nome_zip, destino, logger)
                
                # Atualiza o estado apenas se a pasta existia e foi processada
                estado[mod] = data_para_rodar.strftime("%Y-%m-%d")
                print(f"✅ Backup de {mod} concluído e registrado.")
            else:
                print(f"⚠️ Pasta {dia} está vazia. Pulando registro de data.")
        else:
            print(f"📂 Pasta {dia} ainda não existe para {mod}. Nada a fazer.")

    salvar_estado(estado)
    print("\n--- Ciclo de Agendamento Finalizado ---")

if __name__ == "__main__":
    executar_sistema()