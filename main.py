from modules import auth, crypto, history, utils, menu

menu.menu()


while True:
    user = auth.login_user()

    if user:
        print(f'Seja bem vindo, {user}.')
    else:
        exit()

    opcao = menu.option('Digite sua opção: ')

    if opcao == 3:
        history.show_logs()