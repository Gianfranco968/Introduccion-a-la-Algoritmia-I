"""General la serie de Fibonacci hasta la posición 40.
Informar cuantos valores hay múltiplos de 3, entre las
posiciones 12 a 30.
Mostrarlos juntos con su posición"""
def fibonacci():
    a = 1
    b = 1
    posicion = 0
    for i in range(0,40):
        c = a+b
        posicion += 1
        a = b
        b = c
        if posicion >= 12 and posicion <= 30:
            if c % 3 == 0:
                print("Posicion:",posicion,"Número:",c)
fibonacci()