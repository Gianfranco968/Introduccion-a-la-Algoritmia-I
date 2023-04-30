"""Mostral la tabla de multiplicar (entre 1 y 12) del número 4.
¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la
tabla de multiplicar a mostrar?"""
def tabla_multiplicacion():
    for i in range (1,13):
        calculo = 4 * i
        print("La tabla de multiplicar es la siguiente:",i,calculo)
tabla_multiplicacion()