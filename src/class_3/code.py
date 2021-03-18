# Para crear nuestras propias funciones se utiliza la palabra reservada def (define), seguido de un nombre, una lista de
# parámetros entre paréntesis y luego un bloque de código que debe ejecutar cuando se le llame.
# El nombre debe cumplir las mismas reglas que cualquier nombre de variable.
def hello():
    print('Hello, World!')
    print('My name is byte Epoch')
    print('I am 18 years old')

# Para llamar a la función lo hacemos igual que hemos visto con print, int o input. Solo hay que poner el nombre y unos
# paréntesis al final. Si la función tuviera parámetros, meteríamos los valores dentro del paréntesis.
hello()

# Para devolver valores de una función se utiliza la palabra reservada return. En este ejemplo tenemos una función
# que tienes 2 parámetros de entrada, a y b, y devuelve la suma de ambos.
def sum(a, b):
    return a + b

# Podemos usar esta función e imprimir el resultado en pantalla.
print(sum(2, 3))

# Si queremos definir parámetros opcionales se pondría un = y seguido el valor que tiene que tomar por defecto. En este
# caso, no es obligatorio pasarle valores para estos parámetros en la llamada a la función, al contrario que con los
# parámetros posicionales.
def math_operation(a, b, operation='sum', say='hello'):
    print(say)
    if operation == 'sum':
        return a + b
    elif operation == 'substract':
        return a - b


# Si queremos especificar qué valor va a qué parámetros, podemos hacerlo especificando el nombre = valor.
print(math_operation(b=2, a=3, operation='substract', say='goodbye'))

# Para recoger una lista variable de parámetros posicionales se haría poniendo un * como prefijo del nombre del
# parámetro. Normalmente se le llama args. Veremos como trabajar con estas listas de valores más adelante en el curso.
def sum(*args):
    print(args)

sum(1, 2, 3, 4, 5)


# Para recoger una lista variable de parámetros con nombre específico (keyword parameters) se haría poniendo **
# como prefijo del nombre del parámetro. Normalmente se le llama kwargs. Veremos como trabajar con estos diccionarios
# de valores más adelante en el curso.
def friend(**kwargs):
    print(kwargs)

friend(name='byte', last_name='epoch', age=18)

# Hay un tipo de valor especial, None, del tipo NoneType, que se usa para expresar la ausencia de valor.
a = None

# Si almacenamos la salida de una función que no devuelve nada, recibiremos un None.
b = hello()
print(b)


# Cuando creamos una función, creamos un nuevo ámbito (scope)para las variables. Esto significa que estos pueden ver
# todos los nombres definidos fuera de ellos, e.g dentro de my_number podemos ver la variable name. Por otro lado,
# el ámbito exterior no puede ver lo que hay en los más pequeños. En este ejemplo hemos definido num dentro de my_number
# y desde fuera no se puede ver esa variable.
name = 'eggs'


def my_number():
    num = 5
    print(name)
    return name

my_number()
# print(num) # ERROR: no ve esa variable desde este scope
print(name)


# Si dentro de un scope creamos un identificador que sea igual a otro nombre exterior ya definido, estaríamos
# enmascarando ese nombre, y cuando lo llamáramos haríamos referencia al que hemos creado nosotros y no al del scope
# exterior.
name = 'eggs'


def my_number():
    name = 'qwe'
    print(name)

my_number()
print(name)

# El scope más exterior, que es el que ocupa el fichero, se le llama global. Si queremos modificar una variable global,
# y no enmascararla como en el ejemplo exterior, se usa la palabra reservada global, para indicar que vamos a usar
# esa variable global. NO USAR.
name = 'eggs'


def my_number():
    global name
    name = 'qwe'
    print(name)

my_number()
print(name)

# Si nuestro código falla, devolverá una excepción y parara la ejecución en ese punto. Estas excepciones pueden ser
# tratadas. Ponemos el código que puede fallar dentro del try, y luego un except para capturarlo. Se pueden poner
# tantos excepts como se necesite y cuando ocurra una excepción se empezara a comprobar una except que encaje con el
# error en orden descendente hasta encontrar uno. Si ninguno encaja, la excepción no se capturara y se parará la
# ejecución del programa. A esto se le llama control de errores.
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error')
        return None
    except TypeError:
        return None
    except Exception:
        return 10


print(div(5, 3))
print(div(10, 2))
print(div(5, 0))
print(div(12, 3))
