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
    utils.clear()
    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor("ENCRYPT".center(50), 'cyan'))
    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor(menu.format_option("Caesar", "[1]"), 'yellow'))
    print(utils.cor(menu.format_option("Vigenère", "[2]"), 'yellow'))
    print(utils.cor(menu.format_option("ROT13", "[3]"), 'yellow'))
    print(utils.cor(utils.linha(50), 'cyan'))
    option = menu.option("Choose an option: ")
    utils.clear()

    text = input(utils.cor("Text: ", 'yellow'))

    if option == 1:
        key = int(input(utils.cor("Key (number): ", 'yellow')))
        result = caesar_encrypt(text, key)

        history.add_log(user, "caesar", "encrypt", text, result, key)
        print(result)

    elif option == 2:
        key = input(utils.cor("Key (text): ", 'yellow'))
        result = vigenere_encrypt(text, key)

        history.add_log(user, "vigenere", "encrypt", text, result, key)
        print(result)

    elif option == 3:
        result = rot13(text)

        history.add_log(user, "rot13", "encrypt", text, result)
        print(result)

    input(utils.cor("Enter...", 'cyan'))

def decrypt_menu(user):
    utils.clear()
    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor("DECRYPT".center(50), 'cyan'))
    print(utils.cor(utils.linha(50), 'cyan'))
    print(utils.cor(menu.format_option("Caesar", "[1]"), 'yellow'))
    print(utils.cor(menu.format_option("Vigenère", "[2]"), 'yellow'))
    print(utils.cor(menu.format_option("ROT13", "[3]"), 'yellow'))
    print(utils.cor(utils.linha(50), 'cyan'))
    option = menu.option("Choose an option: ")
    utils.clear()

    text = input(utils.cor("Text: ", 'yellow'))

    if option == 1:
        key = int(input(utils.cor("Key (number): ", 'yellow')))
        result = caesar_decrypt(text, key)

        history.add_log(user, "caesar", "decrypt", text, result, key)
        print(result)

    elif option == 2:
        key = input(utils.cor("Key (text): ", 'yellow'))
        result = vigenere_decrypt(text, key)

        history.add_log(user, "vigenere", "decrypt", text, result, key)
        print(result)

    elif option == 3:
        result = rot13(text)

        history.add_log(user, "rot13", "decrypt", text, result)
        print(result)

    input(utils.cor("Enter...", 'cyan'))

def crypto_menu(user):
    while True:
        utils.clear()
        print(utils.cor(utils.linha(50), 'cyan'))
        print(utils.cor("CRYPTO MENU".center(50), 'cyan'))
        print(utils.cor(utils.linha(50), 'cyan'))
        print(utils.cor(menu.format_option("Encrypt", "[1]"), 'yellow'))
        print(utils.cor(menu.format_option("Decrypt", "[2]" ), 'yellow'))
        print(utils.cor(menu.format_option("History", "[3]"), 'yellow'))
        print(utils.cor(menu.format_option("Back", "[4]" ), 'yellow'))
        print(utils.cor(utils.linha(50), 'cyan'))
        option = menu.option("Choose an option: ")

        if option == 1:
            utils.clear()
            encrypt_menu(user)

        elif option == 2:
            utils.clear()
            decrypt_menu(user)

        elif option == 3:
            history.show_logs()
            input(utils.cor("\nPress Enter to continue...", 'cyan'))

        elif option == 4:
            utils.clear()
            print(utils.cor("Returning...", "cyan"))
            break