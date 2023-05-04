"""Generar 50 valores entre 50 y 200 e informar
cuantos valores deficientes fueron generados"""
def deficiente(numeros):
    resto = 0
    suma = 0
    for i in range(2,numeros+1):
        if numeros % i == 0:
            resto = numeros // i
            suma += resto
    if suma < numeros:
        return True

import random
def valores_deficientes():
    deficientes = 0
    for i in range(0,50):
        numeros = random.randint(50,200)
        if deficiente(numeros):
            deficientes += 1
    print("Existen:",deficientes,"numeros deficientes")
valores_deficientes()