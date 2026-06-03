from modules import auth, crypto, history, utils, menu

def main():
    user = None

    while True:
        utils.clear()
        menu.menu()
        opcao = menu.option("Choose an option: ")

        if opcao == 1:
            utils.clear()
            auth.register_user()
            input("\nEnter to continue...")

        elif opcao == 2:
            utils.clear()
            user = auth.login_user()

            if user:
                crypto.crypto_menu(user)
            else:
                input("\nEnter to continue...")

        elif opcao == 3:
            utils.clear()
            print(utils.cor(utils.linha(50), 'cyan'))
            print(utils.cor("Goodbye.".center(50), 'cyan'))
            print(utils.cor(utils.linha(50), 'cyan'))
            break


if __name__ == "__main__":
    main()