from modules import auth, crypto, history, utils, menu

while True:
    #crypto.menu()

    opcao = menu.option('Digite sua opção: ')

    if opcao == 3:
        history.show_logs()