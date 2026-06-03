#Funções de login e cadastro dos usuários
from modules import utils 
from time import sleep
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

USERS_FILE = DATA_DIR / "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

def register_user():
    users = load_users()

    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor("REGISTER".center(50), "cyan"))
    print(utils.cor(utils.linha(50), 'cyan'))

    username = input(utils.cor("Username: ", 'yellow')).strip()
    password = input(utils.cor("Password: ", 'yellow')).strip()

    if not username or not password:
        print(utils.cor("✖ Fields cannot be empty.", "red"))
        return

    if len(username) < 3:
        print(utils.cor("✖ Username must have at least 3 characters.", "red"))
        return

    if len(password) < 4:
        print(utils.cor("✖ Password must have at least 4 characters.", "red"))
        return

    for user in users:
        if user["username"] == username:
            print(utils.cor("✖ User already exists.", "red"))
            return

    users.append({
        "username": username,
        "password": password
    })

    save_users(users)
    print(utils.cor("✔ Register successful!", "green"))

def login_user():
    users = load_users()
    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor("LOGIN".center(50), "cyan"))
    print(utils.cor(utils.linha(50), 'cyan'))
    username = input(utils.cor("Username: ", 'yellow')).strip()
    password = input(utils.cor("Password: ", 'yellow')).strip()

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(utils.cor("Login successful!", 'green'))
            return username

    print(utils.cor('Incorrect users or password.', 'red'))
    return None