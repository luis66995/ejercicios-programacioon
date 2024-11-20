#8.-programa que reciba un número e imprima la tabla de multiplicar de ese número del 2 al 10
#tablas de multiplicar
for numero in range(2, 11):
    print(f"Tabla de multiplicar del {numero}:")  # iterar el primer digito e imprimirlo
    # Iterar a través de multiplicadores del 1 al 10
    for i in range(1, 11):
        resultado = numero * i  # operacion
        print(f"{numero} x {i} = {resultado}")  # imprimir  multiplication
    print("\n")
