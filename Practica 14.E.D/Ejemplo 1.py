import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')

    coincidencia = patron.match(cadena)
    return bool(coincidencia)

codigo1 = "EMP123"
codigo2 = "EMP4567"
codigo3 = "ABC123"

print(f'{codigo1}: {es_codigo_empleado_valido(codigo1)}')  
print(f'{codigo2}: {es_codigo_empleado_valido(codigo2)}')  
print(f'{codigo3}: {es_codigo_empleado_valido(codigo3)}') 