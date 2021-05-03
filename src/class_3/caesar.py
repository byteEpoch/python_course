# Método de cifrado César. Más info 👉🏻 https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar

def encrypt(text, offset):
    encrypted_text = ''
    for char in text:
        encrypted_text += chr(ord(char) + offset)
    return encrypted_text


def decrypt(text, offset):
    encrypted_text = ''
    for char in text:
        encrypted_text += chr(ord(char) - offset)
    return encrypted_text


def menu(text, offset):
    while True:
        print('+----------------+')
        print('| 1. Cifrar      |')
        print('| 2. Descifrar   |')
        print('+----------------+')
        option = input('Elige una opción: ')
        if option == '1':
            print(encrypt(text, offset))
        elif option == '2':
            print(decrypt(text, offset))
        else:
            print('Elige una opción valida.')


def main():
    text = input('Introduce el texto: ')
    offset = int(input('Introduce un número: '))
    menu(text, offset)

main()
