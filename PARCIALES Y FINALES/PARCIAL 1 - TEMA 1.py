"""Ejercicio – Resolverlo con For

Generar dos números aleatorios simulando el palo y el valor de una carta española 
Uno de ellos, puede obtener cuatro valores posibles, correspondiendo ellos, al palo: 1 –oro, 
2 – basto, 3 – espada y 4 - copa 
Con el otro, puede obtener los valores 1 al 12, que representa los valores de la carta 
Se producen 80 “tiradas”, obteniendo en cada una de ellas, el palo y el número 
Por fin de proceso, indicar: 
    a) Cuántas veces salió un valor primo. Determinarlo con una función e ir mostrándolo 
    en la medida que van saliendo, en una misma línea 
    b) Cuántas veces salió un número múltiplo de 2 
    c) Cuántas veces salió el 7 de espadas 
    d) Porcentaje de veces que salió el 5 de oro. 
    e) Con otra función, determinar cuantos números tienen raíz exacta"""

def es_primo(valor):
    div = 1
    contdiv = 0
    while div <= valor:
        if valor % div == 0:
            contdiv +=1
        div +=1
    if contdiv <= 2:
        print(valor, end=" ")
        return True

def raiz_exacta(valor):
    for i in range(valor):
        if i * i == valor:
            return True

import random
def operaciones():
    cont_primo = 0
    cont_mult = 0
    cont_esp = 0
    cont_oro = 0
    cont_raiz = 0
    for i in range(80):
        palo = random.randint(1,4)
        valor = random.randint(1,12)
        if es_primo(valor):
            cont_primo += 1
        if valor % 2 == 0:
            cont_mult += 1
        if palo == 3 and valor == 7:
            cont_esp += 1
        if palo == 1 and valor == 5:
            cont_oro += 1
        if raiz_exacta(valor):
            cont_raiz += 1
    porcentaje = cont_oro / 80 * 100
    print("\n""Un valor primo salió",cont_primo,"veces")
    print("Salieron",cont_mult,"números múltiplos de 2")
    print("El 7 de espada salió",cont_esp,"veces")
    print("El 5 de oro salió en un",porcentaje,"%")
    print("Hay",cont_raiz,"números con raíz exacta")
operaciones()
    
    
        
    