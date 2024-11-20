#10 programa o una función que reciba un número entero que represente un año
# y devuelva verdadero si el año es bisiesto.
def es_bisiesto(year):
  """Determina si un año es bisiesto.

  Args:
    year: Un número entero que representa el año.

  Returns:
    True si el año es bisiesto, False en caso contrario.
  """
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      return True
  else:
      return False

# Ejemplo de uso:
year = int(input("Ingrese un año: "))
if es_bisiesto(year):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")
