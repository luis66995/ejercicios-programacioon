#9.-teorema de la desigualdad de un triángulo. Si tenemos tres segmentos de cualquier longitud,
# no siempre se puede construir un triángulo con ellos.
#Elabora un programa que reciba la longitud de 3 segmentos y determine si con ellos es posible formar un triángulo.
# obtener datos por el usuario
a = float(input("Ingrese la longitud del primer segmento: "))
b = float(input("Ingrese la longitud del segundo segmento: "))
c = float(input("Ingrese la longitud del tercer segmento: "))


if a + b > c and a + c > b and b + c > a:
    print("Es posible formar un triángulo con estos segmentos.")
else:
    print("No es posible formar un triángulo con estos segmentos.")
