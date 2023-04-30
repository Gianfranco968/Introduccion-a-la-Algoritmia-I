"""Desarrollar un programa que imprima la suma de los números impares comprendidos entre 43 y 176"""
def numeros_impares():
    for i in range(43,176):
        if i % 3 == 0 and i % 2 != 0:
            print(i)
numeros_impares()