"""Ingresar tres números enteros, calcular su promedio y mostrarlo por pantalla"""
def promedio_de_números():
    número_a = int(input("Ingresar un número entero: "))
    número_b = int(input("Ingresar otro número entero: "))
    número_c = int(input("Ingresar otro número entero: "))
    suma_de_números = número_a + número_b + número_c
    promedio = suma_de_números / 3
    print("El promedio de los tres números es de:", promedio)
promedio_de_números()