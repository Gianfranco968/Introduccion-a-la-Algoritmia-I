"""El factorial de un número entero N mayor que cero se define como
el producto de todos los enteros X tales que 0 < X <= N. Desarrollar
un programa para calcular el factorial de un número dado. Deberán
rechazarse las entradas inválidas (menores que 0)."""
def factorial ():
    contador = 1
    numero = int(input("Introducir un número que se quiera calcular su factorial: "))
    if numero < 0:
        print("No se admiten numeros menores a 0")
    for i in range(1,numero):
        if numero >= 0:
            contador = contador * numero
            numero = numero - 1
    print("El factorial del número es:",contador)
factorial()