# Función que cuenta el número de apariciones de cada letra de un string.

from pprint import pprint


def count(string):
    characters = {}
    for char in string.lower():
        characters[char] = characters.setdefault(char, 0) + 1
    return characters


pprint(count('You don\'t get it! y'))
