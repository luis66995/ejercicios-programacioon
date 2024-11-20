#3._programa que reciba como entrada un monto en dólares (USD) y devuelva la cantidad equivalente en pesos mexicanos (MXN)
dolar=19.68
peso= 1.00
cantidad = int(input("Ingrese la cantidad a convertir en dolares :"))
cantidad_pesos=( dolar*cantidad)

print(f"total de dinero en pesos es: {cantidad_pesos}")
