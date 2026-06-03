#Cores e outras funções de utilidade geral para o projeto
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def cor(msg, nome_cor, fundo=None):
    cores = {
        "red": "\033[31m",
        "green": "\033[32m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "white": "\033[37m",
        "black": "\033[30m",
        "cyan": "\033[36m",
        "magenta": "\033[35m",
        "orange": "\033[38;5;214m",
        "pink": "\033[38;5;213m",
        "purple": "\033[38;5;129m",
        "gray": "\033[90m",
        "light_red": "\033[91m",
        "light_green": "\033[92m",
        "light_yellow": "\033[93m",
        "light_blue": "\033[94m",
        "light_magenta": "\033[95m",
        "light_cyan": "\033[96m",
    }

    fundos = {
        "red": "\033[41m",
        "green": "\033[42m",
        "blue": "\033[44m",
        "yellow": "\033[43m",
        "white": "\033[47m",
        "black": "\033[40m",
        "cyan": "\033[46m",
        "magenta": "\033[45m",
        "orange": "\033[48;5;214m",
        "pink": "\033[48;5;213m",
        "purple": "\033[48;5;129m",
        "gray": "\033[100m",
        "light_red": "\033[101m",
        "light_green": "\033[102m",
        "light_yellow": "\033[103m",
        "light_blue": "\033[104m",
        "light_magenta": "\033[105m",
        "light_cyan": "\033[106m",
    }

    RESET = "\033[0m"

    codigo = cores.get(nome_cor.lower(), "")
    codigo_fundo = fundos.get(fundo.lower(), "") if fundo else ""

    return (codigo_fundo + codigo + str(msg) + RESET)

def linha(tam):
    return '=' * tam