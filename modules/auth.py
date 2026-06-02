#Funções de login e cadastro dos usuários
from modules import utils 
from time import sleep


def auth():
    utils.linha(50)
    print(utils.cor('Bem-vindo ao sistema de criptografia!','cyan'))
    print(utils.cor('Faça login ou cadastre-se para começar a usar o programa.','cyan'))
    utils.linha(50)
    print(utils.cor('1 - Fazer login','yellow'))
    print(utils.cor('2 - Cadastro','yellow'))
    utils.linha(50)
    escolha = input(utils.cor('Escolha uma opção: ','green'))
    while escolha not in ['1', '2']:
        print(utils.cor('Opção inválida. Tente novamente.','red'))
        escolha = input(utils.cor('Escolha uma opção: ','green'))
    if escolha == '1':
        login()
    else:
        cadastro()

def login():
    utils.linha(50)
    print(utils.cor('Faça login para acessar o sistema.','cyan'))
    utils.linha(50)
    username = input(utils.cor('Username: ','green'))
    password = input(utils.cor('Password: ','green'))
    print(utils.cor('Login bem-sucedido!','green'))
    sleep(2)

def cadastro():
    utils.linha(50)
    print(utils.cor('Faça seu cadastro para acessar o sistema.','cyan'))
    utils.linha(50)
    username = input(utils.cor('Escolha um username: ','green'))
    password = input(utils.cor('Escolha uma password: ','green'))
    print(utils.cor('Cadastro bem-sucedido! Faça login para acessar o sistema.','green'))
    sleep(2)