# Función para comprobar si una palabra es un palíndromo, i.e. se lee igual de izquierda a derecha que de derecha a
# izquierda.

def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            print('Nope')
            break
    else:
        print('Yes!')


is_palindrome('1221')
is_palindrome('aba')
is_palindrome('abca')
is_palindrome('qwertytrewq')
is_palindrome('a')
is_palindrome('')
is_palindrome('123')
