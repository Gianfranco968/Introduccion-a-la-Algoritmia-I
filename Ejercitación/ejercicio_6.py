"""Generar la serie de Fibonacci hasta el elemento 50.
Informar cuales son los valores que tienen raíz cuadrada
exacta entre las posiciones 10 a 40. Para determinar la
raíz cuadrada, usar el método explicado en clase."""

def raiz_exacta():
    a = 1
    b = 1
    posicion = 0
    for i in range (0,50):
        c = a+b
        posicion += 1
        a = b
        b = c
        if posicion >= 10 and posicion <=40:
            if c ** 0.5 == c // (c**0.5):
                print("Los números con raices cudradas entre la posicion 10 y 40 son:",c, end= " ")
raiz_exacta()