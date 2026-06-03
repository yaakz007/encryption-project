#Funções de login e cadastro dos usuários
from modules import utils 
from time import sleep
from pathlib import Path
import json

USERS_FILE = Path("users.json")

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

    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username:
            print("Usuário já existe.")
            return
    
    users.append({
        "username": username,
        "password": password
    })

    save_users(users)
    print('Cadastro realizado com sucesso!')

def login_user():
    users = load_users() 

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for user in users:
        if user["Username"] == username and user["Password"] == password:
            print("Login realizado com sucesso!")
            return username
    
    print('Usuários ou senha incorretos.')
    return None