"""Ingresar 2 números e informar si son números amigos.
Son números amigos aquellos números cuya suma de divisores
de uno, sin el propio número, es igual al otro, y viceversa.
Ej: 220 y 284 son amigos."""

def divisores_b():
    suma_resto_a = 0
    suma_resto_b = 0
    a = int(input("Introducir un número: "))
    for i in range(1,a+1):
        if a % i == 0:
            resto_a = a // i
            suma_resto_a += resto_a
            print(resto_a, end=" ")
    print("\n""La suma de resto es:",suma_resto_a)
    b = int(input("\n""Introducir otro número: "))
    for x in range(1,b+1):
        if b % x == 0:
            resto_b = b // x
            suma_resto_b += resto_b
            print(resto_b, end=" ")
    print("\n""La suma de resto es:",suma_resto_b)
    if suma_resto_a == suma_resto_b:
        print("\n""Los numeros:",a,"y",b,"son amigos")
    else:
        print("\n""Los numeros:",a,"y",b," no son amigos")
divisores_b()
                      
            