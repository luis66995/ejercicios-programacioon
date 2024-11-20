#12.-programa o una función que reciba un día, mes y año y devuelva verdadero si la fecha es real
#y falso si la fecha es irreal. Un ejemplo de fecha irreal es 30 de febrero o 31 de abril o 29 de febrero de 2021.
def es_fecha_valida(dia, mes, año):
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            dias_en_mes = 29
        else:
            dias_en_mes = 28
    elif mes in [4, 6, 9, 11]:
        dias_en_mes = 30
    else:
        dias_en_mes = 31

    if 1 <= dia <= dias_en_mes:
        return True
    else:
        return False
