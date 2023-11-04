import os 
from time import sleep
import generador_contraseñas as mc

contraseña = mc.generar_contraseñas(10)
print(contraseña)