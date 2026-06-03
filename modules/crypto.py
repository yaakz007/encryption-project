#Funções principais de criptografia e descriptografia. César, Vigenère e rot13.
from modules import utils, history, menu
from time import sleep

def caesar_encrypt(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in text:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            new_index = (index + key) % 26

            if letter.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += letter
    
    return result

def caesar_decrypt(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in text:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            new_index = (index - key) % 26

            if letter.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += letter

    return result

def rot13(text):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in text:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            new_index = (index + 13) % 26

            if letter.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += letter

    return result

def vigenere_encrypt(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    key_index = 0

    for letter in text:
        if letter.lower() in alphabet:
            text_index = alphabet.index(letter.lower())
            shift = alphabet.index(key[key_index % len(key)])

            new_index = (text_index + shift) % 26

            if letter.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]

            key_index += 1
        else:
            result += letter

    return result

def vigenere_decrypt(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    key_index = 0

    for letter in text:
        if letter.lower() in alphabet:
            text_index = alphabet.index(letter.lower())
            shift = alphabet.index(key[key_index % len(key)])

            new_index = (text_index - shift) % 26

            if letter.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]

            key_index += 1
        else:
            result += letter

    return result

def encrypt_menu(user):
    print("1 - Caesar")
    print("2 - Vigenère")
    print("3 - ROT13")

    option = menu.option("Choose: ")

    text = input("Text: ")

    if option == 1:
        key = int(input("Key: "))
        result = caesar_encrypt(text, key)

        history.add_log(user, "caesar", "encrypt", text, result, key)
        print(result)

    elif option == 2:
        key = input("Key: ")
        result = vigenere_encrypt(text, key)

        history.add_log(user, "vigenere", "encrypt", text, result, key)
        print(result)

    elif option == 3:
        result = rot13(text)

        history.add_log(user, "rot13", "encrypt", text, result)
        print(result)

    input("Enter...")

def decrypt_menu(user):
    print("1 - Caesar")
    print("2 - Vigenère")
    print("3 - ROT13")

    option = menu.option("Choose: ")

    text = input("Text: ")

    if option == 1:
        key = int(input("Key: "))
        result = caesar_decrypt(text, key)

        history.add_log(user, "caesar", "decrypt", text, result, key)
        print(result)

    elif option == 2:
        key = input("Key: ")
        result = vigenere_decrypt(text, key)

        history.add_log(user, "vigenere", "decrypt", text, result, key)
        print(result)

    elif option == 3:
        result = rot13(text)

        history.add_log(user, "rot13", "decrypt", text, result)
        print(result)

    input("Enter...")

def crypto_menu(user):
    while True:
        utils.clear()

        print(utils.cor("1 - Encrypt", 'yellow'))
        print(utils.cor("2 - Decrypt", 'yellow'))
        print(utils.cor("3 - History", 'yellow'))
        print(utils.cor("4 - Back", 'yellow'))

        option = menu.option("Choose: ")

        if option == 1:
            encrypt_menu(user)

        elif option == 2:
            decrypt_menu(user)

        elif option == 3:
            history.show_logs()

        elif option == 4:
            break