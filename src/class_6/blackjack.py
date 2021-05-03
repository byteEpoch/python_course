# Implementación de un pequeño blackjack en python.
import json
import random
import os
import sys


def dump_money(money):
    with open('money.json', 'w') as f:
        f.write(json.dumps({'money': money}))


def load_money():
    try:
        with open('money.json') as f:
            return json.loads(f.read())['money']
    except FileNotFoundError:
        dump_money(100)
        return 100


def get_deck():
    deck = []
    for card_type in ('diamonds', 'clubs', 'hearts', 'spades'):
        for i in range(1, 14):
            if i == 1:
                card = 'A'
            elif i == 11:
                card = 'J'
            elif i == 12:
                card = 'Q'
            elif i == 13:
                card = 'K'
            else:
                card = i
            deck.append(f'{card} of {card_type}')
    random.shuffle(deck)
    return deck


def bet(money):
    while True:
        try:
            bet_money = int(input('Cuanto deseas apostar: '))
            if 0 >= bet_money or bet_money > money:
                print('Cantidad invalida.')
                print(f'Introduce un número entre 1 y {money}.')
            else:
                return bet_money
        except ValueError:
            print('Introduce un número.')


def check_cards(cards):
    amount = 0
    has_ace = False
    for card in cards:
        if card.startswith('A'):
            amount += 11
            has_ace = True
        elif card.startswith('J'):
            amount += 10
        elif card.startswith('Q'):
            amount += 10
        elif card.startswith('K'):
            amount += 10
        else:
            amount += int(card.split(' ')[0])
    if amount > 21 and has_ace:
        return amount - 10
    return amount


def play(money):
    bet_money = bet(money)
    deck = get_deck()
    player_cards = [random.choice(deck), random.choice(deck)]
    croupier_cards = [random.choice(deck), random.choice(deck)]
    print('Tus cartas son:')
    for card in player_cards:
        print(card)
    print('La primera carta del croupier es:')
    print(croupier_cards[0])
    while True:
        option = input('Deseas otra carta [s/n]: ')
        if option.lower() == 's':
            new_card = random.choice(deck)
            print(f'Has sacado {new_card}')
            player_cards.append(new_card)
            amount = check_cards(player_cards)
            if amount >= 21:
                break
        elif option.lower() == 'n':
            break
        else:
            print('Opción no valida.')
    player_amount = check_cards(player_cards)
    if player_amount > 21:
        print(f'Has perdido {bet_money} dolares.')
        return money - bet_money
    elif player_amount == 21:
        print(f'Has ganado {bet_money} dolares.')
    else:
        print('Las cartas del croupier son:')
        for card in croupier_cards:
            print(card)
        while player_amount > check_cards(croupier_cards) < 17:
            new_card = random.choice(deck)
            print(f'El croupier saca {new_card}')
            croupier_cards.append(new_card)
        croupier_amount = check_cards(croupier_cards)
        if player_amount == croupier_amount:
            print(f'Habéis empatado. Recuperas {bet_money} dolares.')
            return money
        elif player_amount > croupier_amount or croupier_amount > 21:
            print(f'Has ganado {bet_money} dolares.')
            return money + bet_money
        else:
            print(f'Has perdido {bet_money} dolares.')
            return money - bet_money


def print_menu():
    print('+------------+')
    print('| 1. Jugar   |')
    print('| 2. Saldo   |')
    print('| 3. Salir   |')
    print('+------------+')


def menu():
    money = load_money()
    while True:
        print_menu()
        option = input('Introduce una opción [1-3]: ')
        if option == '1':
            money = play(money)
        elif option == '2':
            print(f'Tienes {money} dolares.')
        elif option == '3':
            dump_money(money)
            sys.exit()
        else:
            print('Opción no valida.')
        if not money:
            print('Estas en banca rota.')
            os.remove('money.json')
            sys.exit()


def main():
    menu()


if __name__ == '__main__':
    main()
