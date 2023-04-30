"""Realizar un programa que lea un número natural H e imprima un mensaje
indicando si H es primo o no. Se dice que un número es primo cuando sólo
es divisible por si mismo y por la unidad."""
def numero_primo():
    numero = int(input("Introducir un número natural: "))
    if numero == 1 or numero == 0:
        print("El número ingresado no es primo")
        return False
    for i in range (2,numero):
        if numero % i == 0:
            print("El número ingresado no es primo")
            return False
    print("El número ingresado es primo")
    return True
numero_primo()