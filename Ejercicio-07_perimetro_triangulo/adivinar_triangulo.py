#7.-programa que calcule el perímetro de un triángulo.El programa preguntará al usuario el tipo de triángulo
#(equilátero, isósceles o escaleno) y le pedirá las entradas necesarias para realizar el cálculo necesario.
tipo_triangulo = input("Ingrese el tipo de triángulo (equilátero, isósceles o escaleno): ")

# Calcular el perimetro dependiendo de la entrada del ususario
if tipo_triangulo == "equilátero":
    lado = float(input("Ingrese la longitud del lado: "))
    perimetro = lado * 3
elif tipo_triangulo == "isosceles":
    lado1 = float(input("Ingrese la longitud del primer lado igual: "))
    lado2 = float(input("Ingrese la longitud del segundo lado igual: "))
    base = float(input("Ingrese la longitud de la base: "))
    perimetro = lado1 + lado2 + base
elif tipo_triangulo == "escaleno":
    ladoa = float(input("Ingrese la longitud del lado a: "))
    ladob = float(input("Ingrese la longitud del lado b: "))
    ladoc = float(input("Ingrese la longitud del lado c: "))
    perimetro = ladoa + ladob + ladoc
else:
    print("Tipo de triángulo inválido.")
    perimetro = None  # Asignar None si el tipo de triángulo es inválido
if perimetro is not None:
    print(f"El perímetro del triángulo es: {perimetro}")
