"""Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores.
Finalizar la lectura de datos con -1."""
def numeros():
    nro = int(input("Introducir un número (para finalizar introducir -1): "))
    while nro != -1 :
        if nro % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        nro = int(input("Introducir un número (para finalizar introducir -1): "))
numeros()