# Ejemplo de uso de todo lo visto en esta clase.
# Se trata de un juego de piedra, papel o tijera.
import random

wins = 0
looses = 0

for i in range(5):

    while True:
        action = input('[R]ock, [P]aper, [S]cissors: ')
        if action != 'R' and action != 'P' and action != 'S':
            print('Esa no es una opcion valida.')
        else:
            break

    enemy_action_number = random.randint(1, 3)
    if enemy_action_number == 1:
        print('La maquina elige piedra')
        enemy_action = 'R'
    elif enemy_action_number == 2:
        print('La maquina elige papel')
        enemy_action = 'P'
    else:
        print('La maquina elige tijeras')
        enemy_action = 'S'

    if action == enemy_action:
        print('Has empatado!')
    elif action == 'R' and enemy_action == 'S':
        print('Has ganado!')
        wins += 1
    elif action == 'S' and enemy_action == 'P':
        print('Has ganado!')
        wins += 1
    elif action == 'P' and enemy_action == 'R':
        print('Has ganado!')
        wins += 1
    else:
        print('Has perdido :(')
        looses += 1

if wins > looses:
    print('Has ganado la guerra')
elif wins == looses:
    print('Habeis empatado')
else:
    print('Has perdido la guerra')
