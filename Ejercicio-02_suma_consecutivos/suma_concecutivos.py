#2.-programa que reciba un número entre 1 y 50 y devuelva la suma de los números consecutivos del 1 hasta ese número.
n = int(input("Ingrese un numero entre 1 y 50:  "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los números consecutivos desde 1 hasta", n, "es:", suma)
