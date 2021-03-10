# Ejercicios Clase 2 (09/03/2021)

## Ejercicio 1

Imprimir por pantalla todos los números primos entre 1 y 100.

## Ejercicio 2

Modificar el código de `src/class_2/rock_paper_scissors.py` para añadir la versión de lagarto y spock.
Podéis ver como funcionaría aquí: https://the-big-bang-theory.com/rock-paper-scissors-lizard-spock/

## Ejercicio 3

Hacer una versión simple del juego de black jack. El objetivo del juego es tener el número más cercano a 21 si pasarse,
y que la máquina no tenga un número más cercano al 21 que nosotros. Tendremos tener un dinero inicial y en cada partida debemos apostar
una cantidad entre 1 y el dinero que tengamos en ese momento. El jugador tendra como "carta" la suma de dos números aleatorios entre 1 y 10.
Después se le debe preguntar si desea sumar otro número, si es así se le sumara un nuevo número aleatorio y se le volverá a preguntar que si
quiere otro una y otra vez hasta que diga que no, o supere el número 21. Después la máquina hará lo mismo hasta que supere el número del jugador
o se pase de 21. Si el jugador no se ha pasado de 21 y la máquina no tiene un número más cercano a 21 que él, ganara el dinero de la apuesta,
que se le sumara al dinero que tenía, sino perdera y se le restará ese dinero. Después se le preguntará si desea jugar otra partida.
Este ciclo seguirá hasta que el jugador no desee seguir jugando o acabe en banca rota.
