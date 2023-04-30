"""La sucesión de Fibonacci es una sucesión de números enteros donde cada
término se obtiene como suma de los dos anteriores, siendo los dos primeros
0 y 1. Por lo tanto, Fib=0,1,1,2,3,5,8,13,21... Realizar un programa que lea
N e imprima los N primeros términos de esta sucesión, como así también la
suma de los mismos."""
def sucesion_fibonacci():
    contador = 0
    numero = int(input("Introducir un número: "))
    if numero <= 2:
        print("Introducir un número mayor")
        return False
    for i in range(2,numero):
        if numero >= 0:
            contador = i + 2
            suma = contador + numero * 2 
    print("La sucesión del número es", suma,contador)
sucesion_fibonacci()
            
            