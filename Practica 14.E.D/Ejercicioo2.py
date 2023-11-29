import re

def buscar_fecha(cadena):
   
   fechas = r"\b\d{2}/\d{2}/\d{4}\b"
   resultado = re.search(fechas, cadena)

   return resultado is not None

print(buscar_fecha("Hoy es 25/11/2023")) 
print(buscar_fecha("Mañana es 22-11-2023")) 
