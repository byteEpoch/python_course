import random
import sys

money = 100

while money:
    while True:
        bet = int(input('Cuanto deseas apostar: '))
        if 1 <= bet <= money:
            break
        print('Cantidad invalida. Por favor, introduzca un número entre 1 y ' + str(money))
        
    player_cards = random.randint(1, 10) + random.randint(1, 10)
    print('Tienes ' + str(player_cards))
    while True:
        more_cards = input('Desea otra carta? [y/n]: ')
        if more_cards == 'y':
            player_cards += random.randint(1, 10)
            print('Tienes ' + str(player_cards))
            if player_cards > 21:
                break
        elif more_cards == 'n':
            break
        else:
            print('Opción invalida. Por favor, introduzca y o n.')

    if player_cards > 21:
        print('Has perdido.')
        money -= bet
    else:
        machine_cards = random.randint(1, 10) + random.randint(1, 10)
        while True:
            if machine_cards < player_cards:
                machine_cards += random.randint(1, 10)
            else:
                break
        print('La máquina tiene ' + str(machine_cards))
        if machine_cards > 21:
            print('Has ganado')
            money += bet
        else:
            print('Has perdido')
            money -= bet

    while True:
        more_cards = input('Desea otra partida? [y/n]: ')
        if more_cards == 'y':
            if not money:
                print('No tienes dinero para seguir jugando.')
            break
        elif more_cards == 'n':
            print('Te llevas ' + str(money))
            sys.exit()
        else:
            print('Opción invalida. Por favor, introduzca y o n.')
