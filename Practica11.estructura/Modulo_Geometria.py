import math

def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_rectangulo(altura, ancho):
    return altura * ancho

def perimetro_rectangulo(largo, ancho):
    return 2 * (largo + ancho)

def area_triangulo(base, altura):
    return (base * altura) / 2

def perimetro_triangulo(base, altura, lado_2):
    return base + altura + lado_2