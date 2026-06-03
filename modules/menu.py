from modules import utils
def option(msg):
    while True:
        try:
            n = input(utils.cor(msg, 'cyan'))
            n = int(n)

            if n < 1 or n > 3:
                print(utils.cor('Opção inválida. Tente novamente.', 'red'))
            else:
                return n
            
        except ValueError:
            print(utils.cor('Digite um número válido.', 'red'))
        except KeyboardInterrupt:
            print(utils.cor('Usuário não informou os dados.', 'red'))
            exit()

def menu():
    print(utils.cor("═" * 80, "cyan"))

    print(utils.cor(wrap("CRIPTOGRAFIA"), "cyan"))

    print(utils.cor("═" * 80, "cyan"))

    print(utils.cor(wrap("1 - Register    2 - Login"), "yellow"))

    print(utils.cor("═" * 80, "cyan"))

    print(utils.cor(wrap("3 - Exit"), "red"))

    print(utils.cor("═" * 80, "cyan"))

def wrap(text, char="═", total=80):
    text = f" {text} "
    padding = total - len(text)

    left = padding // 2
    right = padding - left

    return char * left + text + char * right