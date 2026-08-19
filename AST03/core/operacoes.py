from math import sqrt
from statistics import mean

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError()

def raiz_quadrada(numero):
    if numero >= 0:
        return sqrt(numero)
    else:
        raise ValueError()

def calcular_media(lista_numeros):
    if len(lista_numeros):
        return mean(lista_numeros)
    else:
        return False
