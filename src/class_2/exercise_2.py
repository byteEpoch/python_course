import random

wins = 0
looses = 0

for i in range(5):

    while True:
        action = input('[R]ock, [P]aper, [S]cissors, [L]izard, Spoc[K]: ')
        if action != 'R' and action != 'P' and action != 'S' and action != 'L' and action != 'K':
            print('Esa no es una opcion valida.')
        else:
            break

    enemy_action_number = random.randint(1, 5)
    if enemy_action_number == 1:
        print('La maquina elige piedra')
        enemy_action = 'R'
    elif enemy_action_number == 2:
        print('La maquina elige papel')
        enemy_action = 'P'
    elif enemy_action_number == 3:
        print('La maquina elige tijeras')
        enemy_action = 'S'
    elif enemy_action_number == 4:
        print('La maquina elige lagarto')
        enemy_action = 'L'
    else:
        print('La maquina elige spock')
        enemy_action = 'K'

    if action == enemy_action:
        print('Has empatado!')
    elif action == 'R' and (enemy_action == 'S' or enemy_action == 'L'):
        print('Has ganado!')
        wins += 1
    elif action == 'S' and (enemy_action == 'P' or enemy_action == 'L'):
        print('Has ganado!')
        wins += 1
    elif action == 'P' and (enemy_action == 'R' or enemy_action == 'K'):
        print('Has ganado!')
        wins += 1
    elif action == 'L' and (enemy_action == 'P' or enemy_action == 'K'):
        print('Has ganado!')
        wins += 1
    elif action == 'K' and (enemy_action == 'R' or enemy_action == 'S'):
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
