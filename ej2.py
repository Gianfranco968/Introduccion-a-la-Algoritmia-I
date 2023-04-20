"""Leer un número entero e imprimir un mensaje indicando si es par o impar"""
def calculo():
    a = int(input("Introducir un número: "))
    if a % 2 == 0:
        print("El número", a, "es par")
    else:
        print("El número", a, "es impar")
calculo()