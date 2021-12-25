# Resolve this code
#base = input('Introduce la base imponible de la factura; ')
#print(aplica_iva(base, iva))
#
#def aplica_iva(base, iva = 21):
#    base = base * iva
#    return base
#

def aplica_iva(base, iva = 21):
    base = base * (1+(iva/100))
    return base

base = float(input('Introduce la base imponible de la factura; '))
print(aplica_iva(base))

