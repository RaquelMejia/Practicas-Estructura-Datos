import re

def encontrar_ocurrencias(texto, palabra):
   patron = r'\b' + palabra + r'\b'
   coincidencias = re.finditer(patron, texto)
   for coincidencia in coincidencias:
       print(coincidencia)

texto = "Hola, mi nombre es Raquel y mi nombre es Raquel."
palabra = "Raquel"
encontrar_ocurrencias(texto, palabra)
