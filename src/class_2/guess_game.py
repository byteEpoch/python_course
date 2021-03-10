# Ejemplo de uso del while, if/elif/else, random.randint y sys.exit.
# Se trata de un juego de adivinación de un número aleatorio entre el 1 y el 100.
import random
import sys

guess_number = random.randint(1, 100)

while True:
    num = int(input('Dime un numbero del 1 al 100: '))

    if num < guess_number:
        print('El numero es mayor.')
    elif num > guess_number:
        print('El numero es menor.')
    else:
        print('Ganaste')
        sys.exit()
