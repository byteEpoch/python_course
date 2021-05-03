# Ejemplo de 3 en raya en python.
import random


def get_row():
    while True:
        try:
            row = int(input('Row number (1-3): '))
            if row < 1 or row > 3:
                print('Invalid row number.')
            else:
                break
        except ValueError:
            print('Invalid row number.')
    return row - 1


def get_col():
    while True:
        col = input('Column character (A-C): ')
        if col != 'A' and col != 'B' and col != 'C':
            print('Invalid column char')
        else:
            break
    return 0 if col == 'A' else 1 if col == 'B' else 2


def check_win(board, char):
    for i in board:
        for j in i:
            if j != char:
                break
        else:
            return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != char:
                break
        else:
            return True
    if board[0][0] == board[1][1] == board[2][2] == char or \
       board[2][2] == board[1][1] == board[0][0] == char:
        return True
    return False


def update_board(current_player, board):
    char = 'X' if current_player == 1 else 'O'
    while True:
        row, col = get_row(), get_col()
        if board[row][col] != '':
            print('Cheater! There is a token there! Try again.')
        else:
            break
    board[row][col] = char
    print()
    for line in board:
        print(line)
    print()
    return check_win(board, char)


def main():

    current_player = random.randint(1, 2)
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    for i in range(9):
        print('Player ' + str(current_player) + ' moves.')
        if update_board(current_player, board):
            print('Player ' + str(current_player) + ' wins !')
            break
        current_player = 2 if current_player == 1 else 1
    else:
        print('Draw!')


main()
