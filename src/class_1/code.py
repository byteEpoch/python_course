# Esto es un comentario

# enteros - int
my_int = 42

# reales - float
my_float = 3.14

# strings - str
my_str = 'string con comilla simple'
my_str_2 = "string con comilla doble"
my_str_3 = """string 
multilinea"""

"""Los strings
multilinea
pueden servir
para poner
comentarios de
varias líneas"""

# booleans - bool
my_bool_true = True
my_bool_false = False

# Imprimir por pantalla
print('Imprime cualquier cosa entre los parentesis')

# Operaciones aritméticas (int y floats)
print(3 + 4)  # Suma: 7
print(3 - 4)  # Resta: -1
print(3 * 4)  # Multiplicacion: 12
print(3 / 4)  # Divison: 0.75
print(3 // 4) # Divion entera: 0
print(3 % 4)  # Modulo: 3 
print(3 ** 4) # Potenciacion: 81
print(-3)     # Negativo: -3
print(+3)     # Positivo: 3

# Los parentesis cambian la precedencia de los operadores
print(3 / 4 * 5)   # 3.75
print(3 / (4 * 5)) # 0.15

# La lista de precedencia de los operadores la podeis ver aqui:
# https://docs.python.org/3/reference/expressions.html#operator-precedence
# La lista esta ordenada de menor a mayor. Contiene muchas mas cosas de las que hemos visto
# ahora, pero os puede servir si teneis dudas.

# Operaciones ariméticas (str)
print('Hello, ' + 'byteEpoch') # Hello, byteEpoch
print('spam' * 3)              # spamspamspam
print('na' * 8 + ' Batman')    # nananananananana Batman
# print('Un string ' + 5)      # ERROR: no se puede concatenar un str con algo que no sea un str

# Cambio/Cast de tipos
str(3)        # int a str
str(3.14)     # float a str
int('3')      # str a int
# int('3.14') # ERROR: no es un int
float('3')    # str a float
float('3.14') # str a float
bool(0)       # False
bool(42)      # True
bool(3.14)    # True
bool(0.0)     # False
bool('')      # False
bool(':)')    # True

# Declarar variables
# Reglas para los nombres:
# 1. Los nombres solo puedes contener caracteres alfanumericos y _
# 2. Las variables no pueden comenzar por numeros
# 3. Las variables no pueden tener espacios
# A parte de esto, las variables no pueden llamarse como algunas palabras
# os dejo un link con las palabras prohibidas: 
# https://docs.python.org/3/reference/lexical_analysis.html#keywords
# Por ultimo, las variables son case-senstive, no es lo mismo my_var que MY_VAR
# Ejemplos de nombres de variables:
my_var = 3
my_var_2 = 12
_my_other_var = 'papi'
_12 = 'Arthur'
MY_VAR = 'GREAT'
# Ejemplos de variables con nombres invalidos
# 12 = 'a' - Empieza por numero
# dollar$ = '$' - Continen algo que no es un caracter alfanumerico o _
# my var = 12 - Contiene espacios
# def = 2 - Palabra reservada

# Leer por teclado
my_value_from_keyboard = input()
my_value_from_keyboard_2 = input('Este texto sale por pantalla como el print: ')

# Longitud de un string
print(len('hola')) # 4

"""Primer programita en un string multilinea

print('Hello, world!')
print('What is your name?')
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
"""

# Operadores comparativos
# Estos operadores devuelven un bool - True o False, 0 o 1
# Igual a
my_num_1 = 7
my_num_2 = 7
print(my_num_1 == my_num_2) # True
# Distinto de
my_str1 = 'A'
my_str2 = 'a'
print(my_str1 != my_str2)   # True
# Mayor que
print(5 > 3)  # True
# Menor que
print(5 < 3)  # False
# Mayor o igual a
print(5 >= 3) # True
# Menor o igual a
print(5 <= 3) # True

# Operadores de asignacion
# Asignan lo que haya a la derecha del operador a la variable de la izquierda
# Asignacion normal
my_number = 3
print(my_number) # 3
# Asignacion con suma
# Suma lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number + 2
my_number += 2
print(my_number) # 5
# Asignacion con resta
# Resta lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number - 2
my_number -= 2
print(my_number) # 3
# Asignacion con multiplicacion
# Multiplica lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number * 2
my_number *= 2
print(my_number) # 6
# Asignacion con division
# Divide lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number / 2
my_number /= 2
print(my_number) # 3
# Asignacion con potenciacion
# Potencia lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number ** 2
my_number **= 2
print(my_number) # 9
# Asignacion con division entera
# Divide y descarta la parte decimal de lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number // 2
my_number //= 2
print(my_number) # 4
# Asignacion con modulo
# Obtiene el modulo de la division de lo que haya a la derecha a lo que ya hubiera a la izquierda
# Seria equivalente a my_number = my_number % 2
my_number %= 2
print(my_number) # 0

# OR
# Puerta logica que devuelve True si cualquiera de las dos partes es True.
# En cualquier otro caso devuelve False.
cobrar = False
dejar = False
print(cobrar or dejar) # 0 0 - False
cobrar = False
dejar = True
print(cobrar or dejar) # 0 1 - True
cobrar = True
dejar = False
print(cobrar or dejar) # 1 0 - True
cobrar = True
dejar = True
print(cobrar or dejar) # 1 1 - True

# AND
# Puerta logica que devuelve True si, y solo si, ambas partes son True.
# En cualquier otro caso devuelve False.
cobramos = False
soleado = False
print(cobramos and soleado) # 0 0 - False
cobramos = False
soleado = True
print(cobramos and soleado) # 0 1 - False
cobramos = True
soleado = False
print(cobramos and soleado) # 1 0 - False
cobramos = True
soleado = True
print(cobramos and soleado) # 1 1 - True

# NOT
# Puerta logica que devuelve la inversa, si es True, devuleve False, y si es False, devuleve True
inversa = True
print(not inversa) # False
inversa = False
print(not inversa) # True

# Estructura de control condicional - if
# Ejecuta el codigo que contiene si su condicion es True
# Para indicar que el codigo esta dentro del if se hace indentando el codigo
# Se puede indentar con cualquier numero de espacios o tabulador
# aunque lo recomendable es con 4 espacios.
# La mayoria de editores, sobre todo si son para python, transforman los 
# tabuladores en 4 espacios.
# La sintaxis seria:
# if CONDICION:
#     CODIGO
if cobramos and soleado:
    print('Party hard!')
# Si necesitamos tambien contemplar el caso contrario usamos else
# La sintaxis seria:
# if CONDICION:
#     CODIGO PARA CONDICION TRUE
# else:
#     CODIGO PARA CONDICION FALSE
if cobramos and soleado:
    print('Party hard!')
else:
    print('Boooring!')

# Happy Hacking! :)
