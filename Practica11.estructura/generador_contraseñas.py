import random

def generar_contraseñas(longitud):
  caracteres = "ASDFGHpoiuyt743692"
  contraseña = ""
  for _ in range(longitud):
    contraseña += caracteres[random.randint(0, len(caracteres) - 1)]
  return contraseña
