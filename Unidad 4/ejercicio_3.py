"""Realizar un programa para ingresar desde el teclado un conjunto de números y mostrar
por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos con un valor -1."""
def numeros():
    nro = int(input("Introducir un número (finalizar con -1): "))
    menor = nro
    mayor = nro
    while nro != -1:
        if nro < mayor:
            menor = nro
        if nro > menor:
            mayor = nro
        nro = int(input("Introducir un número (finalizar con -1): "))
    print("El número menor es: ",menor)
    print("El número mayor es: ",mayor)
numeros()
        