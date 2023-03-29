"""Desarrollar un programa que permita ingresar dos números enteros A y B a través del teclado. Imprimir su suma y su diferencia."""
def calculo_matematico():
    número_a = int(input("Ingresar un número entero: "))
    número_b = int(input("Ingresar otro número entero: "))
    suma_total = número_a + número_b
    diferencia = número_a - número_b
    print("La suma es:", suma_total, "y su diferencia:", diferencia)
calculo_matematico()