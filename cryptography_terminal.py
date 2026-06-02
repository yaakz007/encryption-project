program = input('Deseja iniciar o programa? S/N: ').upper()
if program == 'S':
    login = input('Olá, usuário, tudo bem? Deseja fazer login na sua conta ou se cadastrar em nosso sistema?\n1 - Fazer login\n2 - Cadastro\n')
    
    if login == '2':
        user = input('Nome de usuário: ')
        passw = input('Senha: ')
        with open("users.txt", "a") as file:
            file.write(f'{user},{passw}\n')
    
    elif login == '1':
        with open("users.txt", "r") as file:
            linhas = file.readlines()
        logado = False
        while not logado:
            log = input('Usuário: ')
            passw_log = input('Senha: ')
            for linha in linhas:
                user1, passw1 = linha.strip().split(",")
                if log == user1 and passw_log == passw1:
                    logado = True
                    break
            if not logado:
                error = input('Login ou senha incorretos! Deseja tentar novamente? S/N ').upper()
                if error != 'S':
                    break

        if logado:
            print(f'Login bem-sucedido! Seja bem-vindo {log}!')
            action = input(f'O que você deseja fazer agora {log}?\n1 - Criptografia\n2 - Descriptografia\n3 - Histórico\n')

            if action == "1":
                cifra = input('Qual das opções de criptografia?\n1 - Cifra de César\n2 - Cifra de Vigenère\n3 - ROT13\n')

                if cifra == "1":
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem para criptografar (César): ')
                        key = int(input('Chave: '))
                        encrypted = ""
                        alfabeto = "abcdefghijklmnopqrstuvwxyz"
                        for letra in message:
                            if letra.lower() in alfabeto:
                                indice = alfabeto.index(letra.lower())
                                new_indice = (indice + key) % 26
                                encrypted += alfabeto[new_indice].upper() if letra.isupper() else alfabeto[new_indice]
                            else:
                                encrypted += letra
                        print(f'Criptografado: {encrypted}')
                        with open(f"{log}_cifra_de_cesar_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'{message} | Chave: {key} | Criptografado: {encrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

                elif cifra == "2":
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem para criptografar (Vigenère): ')
                        key = input('Chave: ')
                        encrypted = ""
                        alfabeto = "abcdefghijklmnopqrstuvwxyz"
                        j = 0
                        key_expanded = ""
                        for letra in message:
                            key_expanded += key[j % len(key)] if letra.lower() in alfabeto else letra
                            if letra.lower() in alfabeto:
                                j += 1
                        for letra, k in zip(message, key_expanded):
                            if letra.lower() in alfabeto:
                                indice_letra = alfabeto.index(letra.lower())
                                indice_chave = alfabeto.index(k.lower())
                                new_indice = (indice_letra + indice_chave) % 26
                                encrypted += alfabeto[new_indice].upper() if letra.isupper() else alfabeto[new_indice]
                            else:
                                encrypted += letra
                        print(f'Criptografado: {encrypted}')
                        with open(f"{log}_cifra_de_vigenere_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'{message} | Chave: {key} | Criptografado: {encrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

                elif cifra == "3":
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem para criptografar (ROT13): ')
                        encrypted = ""
                        alfabeto = "abcdefghijklmnopqrstuvwxyz"
                        for letra in message:
                            if letra.lower() in alfabeto:
                                indice = alfabeto.index(letra.lower())
                                new_indice = (indice + 13) % 26
                                encrypted += alfabeto[new_indice].upper() if letra.isupper() else alfabeto[new_indice]
                            else:
                                encrypted += letra
                        print(f'Criptografado: {encrypted}')
                        with open(f"{log}_cifra_rot13_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'{message} | Criptografado: {encrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

            elif action == "2":
                de_cifra = input('Qual cifra para descriptografar?\n1 - Cifra de César\n2 - Cifra de Vigenère\n3 - ROT13\n')

                if de_cifra == "1":
                    def de_cesar(texto, chave):
                        resultado = ""
                        for letra in texto:
                            if letra.isalpha():
                                base = ord('A') if letra.isupper() else ord('a')
                                resultado += chr((ord(letra) - base - chave) % 26 + base)
                            else:
                                resultado += letra
                        return resultado
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem a descriptografar (César): ')
                        key = int(input('Chave: '))
                        decrypted = de_cesar(message, key)
                        print(f'Descriptografado: {decrypted}')
                        with open(f"{log}_cifra_de_cesar_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'Descriptografado: {message} | Chave: {key} | Resultado: {decrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

                elif de_cifra == "2":
                    def de_vigenere(texto, key):
                        resultado = ""
                        alfabeto = "abcdefghijklmnopqrstuvwxyz"
                        j = 0
                        key_expanded = ""
                        for letra in texto:
                            key_expanded += key[j % len(key)] if letra.lower() in alfabeto else letra
                            if letra.lower() in alfabeto:
                                j += 1
                        for letra, k in zip(texto, key_expanded):
                            if letra.lower() in alfabeto:
                                indice_letra = alfabeto.index(letra.lower())
                                indice_chave = alfabeto.index(k.lower())
                                new_indice = (indice_letra - indice_chave) % 26
                                resultado += alfabeto[new_indice].upper() if letra.isupper() else alfabeto[new_indice]
                            else:
                                resultado += letra
                        return resultado
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem a descriptografar (Vigenère): ')
                        key = input('Chave: ')
                        decrypted = de_vigenere(message, key)
                        print(f'Descriptografado: {decrypted}')
                        with open(f"{log}_cifra_de_vigenere_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'Descriptografado: {message} | Chave: {key} | Resultado: {decrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

                elif de_cifra == "3":
                    def de_rot13(texto):
                        resultado = ""
                        alfabeto = "abcdefghijklmnopqrstuvwxyz"
                        for letra in texto:
                            if letra.lower() in alfabeto:
                                indice = alfabeto.index(letra.lower())
                                new_indice = (indice + 13) % 26
                                resultado += alfabeto[new_indice].upper() if letra.isupper() else alfabeto[new_indice]
                            else:
                                resultado += letra
                        return resultado
                    continuar = "S"
                    while continuar.upper() == "S":
                        message = input('Mensagem a descriptografar (ROT13): ')
                        decrypted = de_rot13(message)
                        print(f'Descriptografado: {decrypted}')
                        with open(f"{log}_cifra_rot13_logs.txt", "a", encoding="utf-8") as file:
                            file.write(f'Descriptografado: {message} | Resultado: {decrypted}\n')
                        continuar = input('Deseja continuar? S/N: ')

            elif action == "3":
                tipo = input('Qual histórico deseja ver?\n1 - Cifra de César\n2 - Cifra de Vigenère\n3 - ROT13\n')
                if tipo == "1":
                    with open(f"{log}_cifra_de_cesar_logs.txt", "r", encoding="utf-8") as file:
                        print(file.read())
                elif tipo == "2":
                    with open(f"{log}_cifra_de_vigenere_logs.txt", "r", encoding="utf-8") as file:
                        print(file.read())
                elif tipo == "3":
                    with open(f"{log}_cifra_rot13_logs.txt", "r", encoding="utf-8") as file:
                        print(file.read())