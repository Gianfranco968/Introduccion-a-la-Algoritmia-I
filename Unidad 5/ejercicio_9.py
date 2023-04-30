"""Ingresar un número N y validar que sea positivo. Luego:
a. Mostrar los primeros números impares, hasta alcanzar el
número ingresado.
b. Informar la suma de esos números impares.
Ejemplo:
- Si se ingresa 5, se debe mostrar 1 3 5 y la suma 9.
- Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
- Si se ingresa -5, se debe pedir otro número."""

def numeros():
    suma = 0
    numero = int(input("Introducir un número: "))
    if numero >= 0:
        for i in range(0,numero):
            if i % 2 == 0:
                variable = i + 1
                suma = suma + variable
                print(variable, end=" ")
        print("\n""La suma de los números impares es:",suma)
    else:
        print("Ingresar otro número")
numeros()
        
        
        