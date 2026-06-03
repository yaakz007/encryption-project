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