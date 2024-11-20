#5.-programa que calcule el perímetro de un triángulo isósceles.
#El programa pedirá al usuario las entradas necesarias.
# # Obtener las longitudes de los lados ingresadas por  usuario
lado1 = float(input("Ingrese la longitud del primer lado igual: "))
lado2 = float(input("Ingrese la longitud del segundo lado igual: "))
base = float(input("Ingrese la longitud de la base: "))

# operacion para calcular el pedido
perimetro = lado1 + lado2 + base

# resultado
print(f"El perímetro del triángulo isósceles es: {perimetro}")

