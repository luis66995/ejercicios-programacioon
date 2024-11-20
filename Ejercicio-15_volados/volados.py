#15.-programa que juegue volados con el usuario. El juego tendrá 3 rondas.
"""Al inicio de cada ronda, la computadora realiza una apuesta aleatoria entre $20 y $100. Después el usuario deberá realizar su apuesta también con un límite entre $20 y $100.

A continuación, el jugador deberá elegir AGUILA o SOL. El programa lanza el volado e imprime el resultado (AGUILA o SOL) el jugador gana si adivinó el resultado, en caso contrario gana el CPU.

El ganador se lleva la cantidad de dinero que haya apostado su rival y este restará de su bolsa el dinero que perdió. Tanto el jugador como el CPU empiezan con una bolsa de $500.

Quien adivine más rondas gana. Al final de las 3 rondas, el programa debe imprimir quien es el ganador así como la cantidad de dinero tanto del jugador como del CPU."""

import random

def jugar_volados():
    jugador_dinero = 500
    cpu_dinero = 500
    jugador_victorias = 0
    cpu_victorias = 0

    for ronda in range(1, 4):
        print(f"\n--- Ronda {ronda} ---")

        # Apuesta del CPU
        cpu_apuesta = random.randint(20, 100)
        print(f"El CPU apuesta ${cpu_apuesta}")

        # Apuesta del jugador
        while True:
            try:
                jugador_apuesta = int(input("Ingresa tu apuesta (entre $20 y $100): "))
                if 20 <= jugador_apuesta <= 100 and jugador_apuesta <= jugador_dinero:
                    break
                else:
                    print("Apuesta inválida. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")

        # Elección del jugador
        while True:
            eleccion_jugador = input("Elige Águila (A) o Sol (S): ").upper()
            if eleccion_jugador in ("A", "S"):
                break
            else:
                print("Elección inválida. Ingresa A o S.")

        # Lanzar el volado
        resultado_volado = random.choice(["A", "S"])
        print(f"El resultado del volado es: {resultado_volado}")

        # Determinar el ganador
        if eleccion_jugador == resultado_volado:
            print("¡Ganaste la ronda!")
            jugador_dinero += cpu_apuesta
            cpu_dinero -= cpu_apuesta
            jugador_victorias += 1
        else:
            print("El CPU ganó la ronda.")
            cpu_dinero += jugador_apuesta
            jugador_dinero -= jugador_apuesta
            cpu_victorias += 1

        print(f"Dinero del jugador: ${jugador_dinero}")
        print(f"Dinero del CPU: ${cpu_dinero}")

    # Determinar el ganador final
    print("\n--- Resultados finales ---")
    if jugador_victorias > cpu_victorias:
        print("¡Felicidades! Ganaste el juego.")
    elif cpu_victorias > jugador_victorias:
        print("El CPU ganó el juego.")
    else:
        print("El juego terminó en empate.")

    print(f"Dinero final del jugador: ${jugador_dinero}")
    print(f"Dinero final del CPU: ${cpu_dinero}")

# Iniciar el juego
jugar_volados()
