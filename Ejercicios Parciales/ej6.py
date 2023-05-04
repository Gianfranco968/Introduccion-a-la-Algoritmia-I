"""Ingresar por teclado la cantidad de términos a generar de la
siguiente serie:
1 7 19 43 91 187 379 763 1531 3067 6139
El primer término es el 1 y cada término se genera como el doble del
término anterior más 5.
Mostrar la serie por pantalla e informar la suma de los términos generados."""
def fibonacci():
    b = 1
    for i in range(0,11):
        c = b * 2 + 5
        print(b, end=" ")
        a = b
        b = c
fibonacci()