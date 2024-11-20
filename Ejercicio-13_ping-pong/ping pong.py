#13.-programa que imprima los números del 1 al 100, pero aplicando las siguientes reglas.
"""Regla 1: Cuando el número sea divisible entre 3, en vez del número debe escribir "ping"
Regla 2: Cuando el número sea divisible entre 5, en vez del número debe escribir "pong"
Regla 3: Cuando el número   sea divisible entre 3 y también divisible entre 5, en vez del número debe escribir "ping-pong"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("ping-pong")
    elif i % 3 == 0:
        print("ping")
    elif i % 5 == 0:
        print("pong")
    else:
        print(i)
