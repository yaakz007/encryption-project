#Funções de uso dos arquivos de histórico, para salvar e ler as mensagens criptografadas e descriptografadas.

from modules import utils 
from time import sleep
from pathlib import Path
from datetime import datetime
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
        "key": key,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logs.append(new_log)
    save_logs(logs)

def show_logs():
    logs = load_logs()

    if not logs:
        print(utils.cor("No logs found.", "red"))
        return
    
    for log in logs:
        print(utils.cor(utils.linha(35), 'cyan'))
        print(utils.cor('User: ', 'magenta') + utils.cor(str(log["user"]), 'white'))
        print(utils.cor('Cipher: ', 'magenta') + utils.cor(str(log["cipher"]), 'white'))
        print(utils.cor('Operation: ', 'magenta') + utils.cor(str(log["operation"]), 'white'))
        print(utils.cor('Input: ', 'magenta') + utils.cor(str(log["input"]), 'white'))
        print(utils.cor('Output: ', 'magenta') + utils.cor(str(log["output"]), 'white'))
        print(utils.cor('Key: ', 'magenta') + utils.cor(str(log["key"]), 'white'))
        print(utils.cor('Date: ', 'magenta') + utils.cor(str(log.get("timestamp", "N/A")), 'white'))