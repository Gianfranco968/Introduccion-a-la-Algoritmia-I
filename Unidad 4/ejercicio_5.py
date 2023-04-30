"""Desarrollar un programa que imprima los números naturales
comprendidos entre 1 y N. El valor de N se ingresa desde el teclado."""
def numeros_naturales():
    contador = 0
    N = int(input("Introducir un número: "))
    for i in range (1, N):
        contador = contador + 1
        print(contador)
numeros_naturales()