#14.-programa en el cual el usuario debe adivinar un número entre 1 y 100. El número es generado aleatoriamente por el programa. El programa solo le dará 5 intentos al usuario para adivinar. Al final de los 5 intentos, el programa deberá mostrar el mensaje "PERDISTE" y mostrará cuál era el número correcto.

#i el usuario adivina en alguno de los 5 intentos, el programa debe mostrar el mensaje "GANASTE" y mostrará cuál es el número.

#Para efectos de diseño, supongamos que existe una función llamada "random(desde, hasta)" que genera un número entero aleatorio delimitado por los parámetros "desde" y "hasta", los cuales son números enteros.
import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("Tienes 5 intentos para adivinar un número entre 1 y 100.")

    while intentos < 5:
        intentos += 1
        try:
            numero_usuario = int(input(f"Intento {intentos}: Ingresa tu número: "))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
            continue

        if numero_usuario == numero_secreto:
            print(f"¡GANASTE! El número era {numero_secreto}. Lo adivinaste en {intentos} intentos.")
            return

        if numero_usuario < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

    print(f"PERDISTE. El número secreto era {numero_secreto}.")

# Iniciar el juego
adivina_el_numero()
