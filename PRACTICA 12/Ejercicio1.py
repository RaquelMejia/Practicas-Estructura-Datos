class ListaVacia(Exception):
    def __init__(self, message="La lista esta vacia"):
        self.message = message
        super().__init__(self.message)

def sumaDelista(lista):
    if not lista:
        raise ListaVacia()

    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumaDelista(lista[1:])
try:
    numeros = (6, 12, 1, 9, 11, 8, 14)
    resultado = sumaDelista(numeros)
    print(f"La suma de la lista es : {resultado}")

except ListaVacia as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Otro error: {e}")