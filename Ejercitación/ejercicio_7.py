"""Generar la sucesión de Fibonacci hasta la posición 30.
Obtener y mostrar la suma de los valores ubicados en posiciones
primas, a partir de la posición 3. Hacerlo con for"""
 
def es_primo(c):
    div = 1
    contdiv = 0
    while div <= c:
        if c % div == 0:
            contdiv += 1
        div += 1
    if contdiv <= 2:
        return 1
    
def fibonacci():
    a = 1
    b = 1
    resultado = 0
    suma = 0
    posicion = 0
    for i in range(0,30):
        c = a+b
        posicion += 1
        print(c, end= " ")
        if posicion >= 3 and posicion <= 30:
            resultado = es_primo(c)
            if resultado == 1:
                suma += c
        a = b
        b = c
    print("\n""La suma de los valores ubicados en posiciones primas es:", suma)
fibonacci()


        

    
        
        
        
        