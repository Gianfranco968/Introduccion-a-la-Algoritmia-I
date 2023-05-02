"""General la serie de Fibonacci hasta la posición 40.
Informar cuantos valores hay múltiplos de 3, entre las
posiciones 12 a 30.
Mostrarlos juntos con su posición"""
def fibonacci():
    a = 1
    b = 1
    for i in range(2,40):
        suma_posiciones = a+b
        a = b
        b = suma_posiciones
        if i >= 12 and i <= 30:
            if suma_posiciones % 3 == 0:
                print(suma_posiciones, end= " ")
fibonacci()