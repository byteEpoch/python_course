import math
import sys


def sum():
    try:
        a = int(input('Introduce el primer número: '))
        b = int(input('Introduce el segundo número: '))
        print(a + b)
    except ValueError:
        print('Error fatal de cálculo')


def sub():
    try:
        a = int(input('Introduce el primer número: '))
        b = int(input('Introduce el segundo número: '))
        print(a - b)
    except ValueError:
        print('Error fatal de cálculo')


def mult():
    try:
        a = int(input('Introduce el primer número: '))
        b = int(input('Introduce el segundo número: '))
        print(a * b)
    except ValueError:
        print('Error fatal de cálculo')


def div():
    try:
        a = int(input('Introduce el primer número: '))
        b = int(input('Introduce el segundo número: '))
        print(a / b)
    except ValueError:
        print('Error fatal de cálculo')


def mod():
    try:
        a = int(input('Introduce el primer número: '))
        b = int(input('Introduce el segundo número: '))
        print(a % b)
    except ValueError:
        print('Error fatal de cálculo')


def sqrt():
    try:
        a = int(input('Introduce el número: '))
        print(math.sqrt(a))
    except ValueError:
        print('Error fatal de cálculo')


def advanced_options():
    while True:
        option = input('''
        Introduce una opción:
        1. Raíz cuadrada
        2. Atras
        -> ''')
        if option != '1' and option != '2':
            print('Opción invalida')
        else:
            return option


def menu():
    while True:
        option = input('''
        Introduce una opción:
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Modulo
        6. Opciones avanzadas
        7. Salir
        -> ''')
        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6'\
                and option != '7':
            print('Opción invalida')
        else:
            return option


def main():
    while True:
        option = menu()
        if option == '1':
            sum()
        elif option == '2':
            sub()
        elif option == '3':
            mult()
        elif option == '4':
            div()
        elif option == '5':
            mod()
        elif option == '6':
            sub_option = advanced_options()
            if sub_option == '1':
                sqrt()
            elif sub_option == '2':
                pass
        elif option == '7':
            print('Hasta la próxima partida!')
            sys.exit()

main()
