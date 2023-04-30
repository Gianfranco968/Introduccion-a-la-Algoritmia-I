"""Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 12345 se
debe imprimir 5."""
def numero_entero(n):
    contador = 0
    if n == -1:
        contador = contador + 1
    while n!= 0 and n!=-1:
        n = n // 10
        contador = contador + 1
    print(contador)
numero_entero(-1)