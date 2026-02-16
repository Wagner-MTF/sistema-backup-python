import os
import zipfile
import logging
import json
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# 1. Carregar Configurações
with open('config.json', 'r') as f:
    config = json.load(f)

ORIGEM = config['caminho_origem']
DESTINO = config['caminho_destino']
ESTADO_FILE = 'ultimo_backup.json'

# 2. Configurar Logging
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(
    filename=f'logs/backup_{datetime.now().strftime("%Y-%m-%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def carregar_proxima_data():
    if os.path.exists(ESTADO_FILE):
        with open(ESTADO_FILE, 'r') as f:
            dados = json.load(f)
            data_str = f"{dados['ano']}-{dados['mes']}-{dados['dia']}"
            data_dt = datetime.strptime(data_str, "%Y-%m-%d") + timedelta(days=1)
            return data_dt
    # Se não existir histórico, começa de uma data inicial (ajuste aqui se precisar)
    return datetime(2026, 1, 14) 

def salvar_estado(data_dt):
    with open(ESTADO_FILE, 'w') as f:
        json.dump({
            "ano": data_dt.year,
            "mes": data_dt.month,
            "dia": data_dt.day,
            "data_completa": data_dt.strftime("%Y-%m-%d")
        }, f)

def zipar_e_mover(caminho_pasta, nome_zip):
    try:
        caminho_final_zip = os.path.join(DESTINO, f"{nome_zip}.zip")
        with zipfile.ZipFile(caminho_final_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for raiz, _, arquivos in os.walk(caminho_pasta):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    arcname = os.path.relpath(caminho_completo, caminho_pasta)
                    zipf.write(caminho_completo, arcname)
        return True
    except Exception as e:
        logging.error(f"Erro em {nome_zip}: {str(e)}")
        return False

def executar_sistema():
    data_alvo = carregar_proxima_data()
    
    # Monta o caminho: ORIGEM / ANO / MES / DIA
    # Exemplo: Teste_Origem/2026/1/15
    pasta_do_dia = os.path.join(ORIGEM, str(data_alvo.year), str(data_alvo.month), str(data_alvo.day))

    print(f"Tentando acessar: {pasta_do_dia}")

    if os.path.exists(pasta_do_dia):
        subpastas = [os.path.join(pasta_do_dia, f) for f in os.listdir(pasta_do_dia) 
                     if os.path.isdir(os.path.join(pasta_do_dia, f))]

        if subpastas:
            print(f"Fazendo backup de {len(subpastas)} pastas do dia {data_alvo.strftime('%d/%m/%Y')}...")
            
            with ThreadPoolExecutor(max_workers=config['limite_threads']) as executor:
                for pasta in subpastas:
                    nome_arquivo = f"Backup_{data_alvo.year}_{data_alvo.month}_{data_alvo.day}_{os.path.basename(pasta)}"
                    executor.submit(zipar_e_mover, pasta, nome_arquivo)
            print("Sucesso!")
        else:
            print("Pasta do dia encontrada, mas está vazia.")

        # ESTA LINHA DEVE FICAR AQUI (Fora do if subpastas e fora do else)
        # Ela garante que o dia seja salvo de qualquer jeito se a pasta existir
        salvar_estado(data_alvo)
        logging.info(f"Processamento do dia {data_alvo.strftime('%Y-%m-%d')} concluído.")

    else:
        print(f"A pasta do dia {data_alvo.day} ainda não existe no caminho especificado.")

if __name__ == "__main__":
    executar_sistema()