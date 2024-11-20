#11.-programa que reciba un número entero entre 0 y 11, debe devolver el
#nombre de mes correspondiente. Toma en cuenta que 0 = Enero y 11 = Diciembre.

numero_mes= int(input("Ingrese un numero entre 0 y 11:"))
if numero_mes==0:
    print("Enero")
elif numero_mes==1:
    print("Febrero")
elif numero_mes==2:
    print("Marzo")
elif numero_mes==3:
    print("Abril")
elif numero_mes==4:
    print("Mayo")
elif numero_mes==5:
    print("Junio")
elif numero_mes==6:
    print("Julio")
elif numero_mes==7:
    print("Agosto")
elif numero_mes==8:
    print("Septiembre")
elif numero_mes==9:
    print("Octubre")
elif numero_mes==10:
    print("Noviembre")
elif numero_mes==11:
    print("Diciembre")
else:
    print("Numero no valido intenta de nuevo")

