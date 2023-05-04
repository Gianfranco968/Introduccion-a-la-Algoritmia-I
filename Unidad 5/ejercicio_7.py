""" Leer un número entero e invertir las cifras que contiene.
Imprimir por pantalla el número invertido. Tener en cuenta que
el número puede ser negativo. Por ejemplo, si se ingresa 1234
debe mostrar 4321."""
def invertir():
    numeros = int(input("Introducir números: "))
    while numeros != 0:
        ultimo_numero = numeros % 10
        numeros = numeros // 10
        print(ultimo_numero, end=" ")
invertir()