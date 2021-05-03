# Importamos el modulo copy
import copy
# Importamos el modulo random
import random

# Las listas en python nos permiten almacenar n valores en una sola variable.
# En este caso estamos creando una lista de 5 valores numéricos.
my_list = [1, 2, 3, 4, 5]

# Para acceder a los valores, ya sea para modificarlos, o bien para usarlos para otra operación, se haría usando
# corchetes y luego el índice a acceder. Los índices empiezan a contarse desde el 0. Por lo que el 1 en nuestra lista
# anterior se obtendría de la siguiente forma.
print(my_list[0])

# Lo elementos de una lista también pueden ser accedidos empezando desde el final usando números negativos, empezando
# por el -1. Para acceder, por ejemplo, al 4 de nuestra lista se haría de esta manera.
print(my_list[-4])

# Si intentamos acceder a una posición que no existe nos dara un error del tipo IndexError
# my_list[10]  # ERROR

# Para obtener el tamaño de nuestra lista podemos utilizar la función len
print(len(my_list))  # Esta línea imprimiría un 5

# Podemos seleccionar un rango dentro de nuestra lista indicando desde donde hasta donde queremos obtenerlo. Para ello
# ponemos los dos indices separados por :, e.g. my_list[1:4]. El número de inicio es inclusivo, y el de fin exclusivo.
# En este ejemplo obtendríamos una lista con los números de los índice 1, 2 y 3.
print(my_list[1:4])  # Esta línea imprimiría [2, 3, 4]

# Cuando hacemos rangos en una lista, no da un error de índices cuando nos pasamos del tamaño máximo, simplemente
# cogería valores hasta que no pudiera más.
print(my_list[1:10000])  # Esto funcionaría perfectamente

# Para obtener un rango desde el inicio, en vez de poner el 0, podemos omitirlo.
print(my_list[:3])  # Esta línea imprimiría [1, 2, 3]

# Lo mismo para el final.
print(my_list[1:])  # Esta línea imprimiría [2, 3, 4, 5]

# También podemos obtener los rangos salteados, utilizando un 3er valores que indica cada cuanto obtener un número. Por
# ejemplo para obtener todos los números pares, podríamos decirle que cogiera desde el indice 1 hasta el final
# de 2 en 2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

# La listas pueden sumarse. El resultado sería una nueva lista con los elementos de los primera lista, seguidos de los
# de la segunda.
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
print(even_numbers + odd_numbers)  # Esta línea imprimiría [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

# Las listas también pueden multiplicarse por un número entero, devolviendo una nueva lista con todos los elementos de
# la lista multiplicada, tantas veces como el número usado.
print(['spam'] * 3)  # Esta línea devolvería [spam, spam, spam]

# Podemos eliminar elementos de una lista usando la palabra del.
fruits = ['banana', 'orange', 'melon']
del fruits[1]
print(fruits)  # Esta línea devolvería ['banana', 'melon']

# Las listas pueden tener elementos de distintos tipos.
my_extrange_list = [None, True, 'hola', 0]

# Aquí tenemos un ejemplo de uso en el que añadimos de forma iterativa el nombre de 6 gatos a una lista.
def cat_madam():
    cats = []
    for i in range(6):
        cat_name = input('Introduce el nombre del gato: ')
        cats += [cat_name]
    return cats


cat_names = cat_madam()
print(cat_names)


# Aquí imprimimos cada uno de los nombres de la lista de gatos en una línea nueva.
for cat_name in cat_names:
    print(cat_name)


# También podemos usar un range de la longitud de la lista para acceder a sus elementos.
for i in range(len(cat_names)):
    print('El gato ' + str(i + 1) + ' se llama ' + cat_names[i])


# La función enumerate hace lo mismo que los dos ejemplos anteriores. Nos devuelve el índice y a la vez el valor, en
# dos variables diferentes.
for i, v in enumerate(cat_names):
    print('El gato ' + str(i + 1) + ' se llama ' + v)


# Podemos comprobar si un elemento pertenece a una lista usando la palabra reservada in.
print('guantes' in  cat_names)


# Si importamos el modulo random, podemos usar la función choice que nos devuelve un elemento aleatorio de una lista.
print('Mi gato favorito es ' + random.choice(cat_names))


# La función shuffle del modulo random ordena los elementos de una lista de forma aleatoria. NOTA: esta función no
# devuelve nada, cambia la lista in situ.
random.shuffle(cat_names)

for i, v in enumerate(cat_names):
    print('El gato ' + str(i + 1) + ' se llama ' + v)

# Podemos añadir elementos a una lista de dos formas. La primera ya la hemos visto:
my_list = [1, 2, 3, 4, 5]
my_list += [6]
print(my_list)

# La otra es usando el método append de la lista.
my_list.append(10)
print(my_list)

# Para eliminar elementos por valor en vez de por índice, podemos usar el método remove. Solo elimina la primera
# aparición de ese valor, por lo que, si lo tenemos más de una vez en nuestra lista, solo se eliminaría el primero, y
# dejaría los demás tal y como están.
fruits = ['banana', 'orange', 'melon', 'cherry', 'orange']
fruits.remove('orange')
print(fruits)  # Esta línea devolvería ['banana', 'melon', 'cherry', 'orange']

# Para añadir un valor en un posión concreta podriamos usar el método insert, pasandole en primer lugar la posición
# donde queremos que vaya, y en segundo, el valor que queremos añadir.
fruits.insert(1, 'orange')
print(fruits)  # Esta línea devolvería ['banana', 'orange', 'melon', 'cherry', 'orange']

# Podemos obtener el primer índice donde aparece un valor usando el método index.
print(fruits.index('melon'))  # Esta línea devolvería un 2

# Podemos ordenar los elementos de una lista con el método sort. Este método también funciona in situ.
unordered_numbers = [2, 1, 20, 3, 56, 12, 100]
print(unordered_numbers)
unordered_numbers.sort()
print(unordered_numbers)

# Por último, podemos invertir el orden de los elementos de una lista con el método reverse.
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Esta línea devolvería [5, 4, 3, 2, 1]

# Tenéis más info sobre todos estos métodos aquí https://docs.python.org/3/tutorial/datastructures.html

# En los lenguajes de programación en general los valores pueden ser mutables o inmutables. Esto quiere decir que
# la variable se modifica directamente en memoria o no. En el caso de las listas, al añadir un elemento nuevo por
# ejemplo, estamos modificando directamente el valor en memoria, por lo que las listas son mutables.
# Podemos ver la posición de memoria donde está almacenado un valor usando la función id.
num = 5
print(id(5))

# Podemos ver esto en acción en este ejemplo.
a = [1]
print(a)
print(id(a))
a.append(2)
print(a)
print(id(a))  # El id de la variables es el mismo que tenía previamente.

# Podemos crear listas inmutables de elementos a través de las tuplas. Son exactamente igual que las listas pero no se
# pueden modificar. Para crear una tupla, escribimos sus valores entre paréntesis.
my_tuple = (1, 2, 3, 4, 5)

# Para crear una tupla de un elemento ponemos el valor entre paréntesis con una , al final.
my_tuple_2 = (1, )

# Accedemos a sus elementos de las misma forma que con las listas.
print(my_tuple[3])

# Podemos transformar listas en tuplas con la función tuple.
print(tuple([1, 2, 3]))

# Y también tuplas en listas con la función list.
print(list((1, 2, 3)))

# Si intentamos modificar un valor de una tupla, nos dara un error del tipo TypeError, indicando que las tuplas no
# soportan la asignación de valores.
# my_tuple[2] = 16  # ERROR

my_list = [1, 2]


def movify_list(a_list):
    aux = copy.copy(a_list)
    aux.append(3)
    return aux


print(my_list)
a = movify_list(my_list)
print(my_list)
print(a)


def my_function(a = []):
    a.append(1)
    print(a)


my_function()
my_function()
my_function()


def my_fibonacci_dummy():
    return 5, 8


num1, num2 = my_fibonacci_dummy()
print(num1)
print(num2)


def sum(*nums):
    a = 0
    for num in nums:
        a += num
    print(a)


sum(1, 2, 3, 4, 5)
