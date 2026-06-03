#Funções de uso dos arquivos de histórico, para salvar e ler as mensagens criptografadas e descriptografadas.

from modules import utils 
from time import sleep
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
LOG_FILE = BASE_DIR / 'data' / 'logs.json'


def load_logs():
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_logs(logs):
    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        json.dump(logs, file, indent=4, ensure_ascii=False)


def add_log(user, cipher, operation, input_text, output_text, key=None):
    logs = load_logs()

    new_log = {
        "user": user,
        "cipher": cipher,
        "operation": operation,
        "input": input_text,
        "output": output_text,
        "key": key
    }

    logs.append(new_log)
    save_logs(logs)

def show_logs():
    logs = load_logs()

    if not logs:
        print('Nenhum log encontrado.')
        return
    
    for log in logs:
        utils.linha(35)
        print(f'Usuário: {log["user"]}')
        print(f'Cifra: {log["cipher"]}')
        print(f'Operação: {log["operation"]}')
        print(f'Entrada de dados: {log["input"]}')
        print(f'Saída de dados: {log["output"]}')
        print(f'Chave: {log["key"]}')
