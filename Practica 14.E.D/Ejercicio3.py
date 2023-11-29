def palabras_minusculas(texto):
    import re
    patron_palabras = re.compile(r'\b[a-z]+\b')

    palabras_encontradas = re.findall(patron_palabras, texto)

    return palabras_encontradas

texto = "PRACTICA numero 14 DE ESTRUCTURAS de datos."

palabras_encontradas = palabras_minusculas(texto)

print(palabras_encontradas)