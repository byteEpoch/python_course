import random
import sys


def roll_a_dice():
    try:
        num = int(input('Introduce un número: '))
        return random.randint(1, num)
    except ValueError:
        return None


def roll_n_dices():
    try:
        times = int(input('Introduce el número de dados: '))
        for i in range(times):
            num = int(input('Introduce un número: '))
            print(random.randint(1, num))
    except ValueError:
        print('Error')


def pifia():
    print(1)


def menu():
    while True:
        option = input('''Introduce una opción:
        1. Lanzar un dado
        2. Lanzar múltiples dados
        3. Auto-pifia
        4. Salir
        -> ''')
        if option != '1' and option != '2' and option != '3' and option != '4':
            print('Opción invalida')
        else:
            return option


def main():
    while True:
        option = menu()
        if option == '1':
            print(roll_a_dice())
        elif option == '2':
            roll_n_dices()
        elif option == '3':
            pifia()
        elif option == '4':
            print('Hasta la próxima partida!')
            sys.exit()

main()
