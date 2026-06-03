from modules import auth, crypto, history, utils, menu

while True:
    menu.menu()
    opcao = menu.option("Escolha: ")

    if opcao == 1:
        utils.clear()
        auth.register_user()
        input("\nEnter to continue...")

    elif opcao == 2:
        utils.clear()
        user = auth.login_user()
        input("\nEnter to continue...")

    elif opcao == 3:
        break