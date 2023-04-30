"""Realizar un programa para ingresar desde el teclado un conjunto de números.
Al finalizar mostrar por pantalla el primer y último valor ingresado.
Finalizar la lectura con -1."""
def numeros():
    primer_numero = 0
    ultimo_numero = 0
    for i in range(1000):
        nro = int(input("Introducir un número (introducir -1 si desea terminar): "))
        if nro == -1:
            break
        if primer_numero <= 0:
            primer_numero = nro
        ultimo_numero = nro
    print("El primer numero es: ",primer_numero)
    print("El ultimo numero es: ",ultimo_numero)
numeros()