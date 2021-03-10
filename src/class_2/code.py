# Los imports deben ir en la parte superior del fichero.
# Con ellos podemos utilizar paquetes extra de codigo en nuestros programas.
# Podéis ver todas las funciones que trae python por defecto en:
# https://docs.python.org/3/library/functions.html
# Y las librerias standard que podemos importar en:
# https://docs.python.org/3/library/index.html
# Random trae funcionalidad para trabajar con aleatoriedad. Más info en:
# https://docs.python.org/3/library/random.html
# Sys trae funcionalidades para trabajar con el sistema. Más info en:
# https://docs.python.org/3/library/sys.html
import random
import sys
# Con la forma from paquete import elemento podemos importar algo especifico de un paquete
# from random import randint

# Si escribimos un str dentro de un input nos permite mostrar el texto en pantalla justo antes
# de recoger lo que nos escriban por teclado.
num1 = int(input('Dime el primer numero: '))
num2 = int(input('Dime el segundo numero: '))
num3 = int(input('Dime el tercer numero: '))

# Elif nos permite añadir casos extra a nuestros if.
if num3 < num1 > num2:
    print('El primer numero es el mayor')
elif num2 > num3:
    print('El segundo es el mayor')
else:
    print('El tercero es el mayor')

num1 = int(input('Dime el primer numero: '))
num2 = int(input('Dime el segundo numero: '))
operacion = input('Dime la operacion m, d, s, r: ')

if operacion == 'm':
    print('El resultado de la multiplicacion es :' + str(num1 * num2))
elif operacion == 'd':
    print('El resultado de la division es :' + str(num1 / num2))
elif operacion == 's':
    print('El resultado de la suma es :' + str(num1 + num2))
elif operacion == 'r':
    print('El resultado de la resta es :' + str(num1 - num2))
else:
    print('Operacion no soportada')

# While nos permite ejecutar un código una y otra vez mientras las condición evaluada sea cierta.
# Esto permite ejecutar un bucle de 0 a n veces.
number = 5
while number:
    print(number)
    number -= 1

guess_number = 13
num = int(input('Introduce un numero: '))

while num != guess_number:
    num = int(input('Casi intentalo de nuevo. Dime otro numero: '))

print('Lo adivinaste')

# Usando un while True y la sentencia break al final, nos permite ejecutar un while de 1 a n veces.
# break rompe el flujo actual. Usar solo si es completamente necesario.
# continue nos permite no seguir ejecutando el codigo de un bucle y pasar a la siguiente iteración, 
# i.e volver a comprobar la condición y si se evalua como True empezar desde la primera linea del
# código del bucle. NO USAR.
guess_number = 13

while True:
    num = int(input('Introduce un numero: '))
    # continue: NO USAR
    if num == guess_number:
        break

print('Lo adivinaste')

# For nos permite ejecutar un bucle un número finito de veces. Por cada valor de la derecha, se asigna a la
# variable de la izquierda y ejecuta el contenido. Tantas veces como datos haya en la lista de la derecha.
# range nos devuelve un rango de numeros. Hay 3 formas de utilizarlo:
# La priemra es solo indicando el numero de veces final que debe alcalnzar. Empezando por 0 y llegando a ese
# numero - 1
for i in range(5):
    print(i)

# La segunda opción es indicandole desde que numero empezar (incluido) y hasta que numero (excluido)
for i in range(1, 6):
    print(i)

# Por último podemos decirle un tercer numero que indica cuanto debe ir aumentando en cada paso del bucle.
# En este ejemplo podriamos obtener todos los números pares.
for i in range(2, 101, 2):
    print(i)

# Python utiliza como set de carateres el standard unicode 16 (utf-16). Podéis ver una tabla completa de 
# correspondencias aquí:
# https://www.fileformat.info/info/charset/UTF-16/list.htm
# con la función ord podemos obtener el int asociado a un caracter. https://docs.python.org/3/library/functions.html#ord
# con la función chr podemos obtener el caracter asociado a un int. https://docs.python.org/3/library/functions.html#chr
for i in range(ord('A'), ord('Z')):
    print(chr(i))

# Con la función randint del paquete random podemos obtener un numero entero aleatorio entre 2 números, ambos incluidos.
guess_number = random.randint(1, 20)

while True:
    num = int(input('Introduce un numero: '))
    if num == guess_number:
        # Con la función exit del paquete sys podemos parar la ejecución de un programa.
        sys.exit()

# Al usar sys.exit este código no se ejecutaría.
print('Lo adivinaste')
