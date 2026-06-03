from modules import utils

def option(msg):
    while True:
        try:
            n = input(utils.cor(msg, 'cyan'))
            n = int(n)

            if n < 1 or n > 4:
                print(utils.cor('Invalid option, try again.', 'red'))
            else:
                return n

        except ValueError:
            print(utils.cor('Enter a valid number.', 'red'))
        except KeyboardInterrupt:
            print(utils.cor('User did not provide the data.', 'red'))
            exit()


def format_option(text, number, total=50, fill="."):
    text = f"{text}"
    number = f"{number}"

    space = total - len(text) - len(number)

    return text + (fill * space) + number


def menu():
    print(utils.cor("═" * 50, "cyan"))
    print(utils.cor(wrap("ENCRYPTION"), "cyan"))
    print(utils.cor("═" * 50, "cyan"))

    print(utils.cor(format_option("Register", "[1]"), "yellow"))
    print(utils.cor(format_option("Login", "[2]"), "yellow"))
    print(utils.cor(format_option("Exit", "[3]"), "yellow"))

    print(utils.cor("═" * 50, "cyan"))


def wrap(text, char="═", total=50):
    text = f" {text} "
    padding = total - len(text)

    left = padding // 2
    right = padding - left

    return char * left + text + char * right