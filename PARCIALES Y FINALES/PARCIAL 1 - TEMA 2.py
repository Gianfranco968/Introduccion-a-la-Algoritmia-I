"""Ejercicio – Resolverlo con While

Generar dos números aleatorios simulando un el palo y el valor de una carta 
Uno de ellos, puede obtener cuatro valores posibles, correspondiendo ellos, al palo: 1 –oro, 
2 – basto, 3 – espada y 4 - copa 
Con el otro, puede obtener los valores 1 al 12, que representa los valores de la carta 
Se producen 200 “tiradas”, obteniendo en cada una de ellas, el palo y el número 
Por fin de proceso, indicar: 
    a) Cuántas veces salió un valor perfecto. Determinarlo con una función. Número 
    Perfecto: es cuando la suma de los divisores, sin el propio número es igual al 
    número 
    b) Cuántas veces salió un número múltiplo del primer valor que salió. Ir mostrándolo 
    en la medida que van saliendo, en una misma línea 
    c) Cuántas veces salió el 1 de copas 
    d) Porcentaje de veces que salió el 12 de basto. 
    e) Entre todos los valores que salieron, cuantos de ellos pertenecen al 2do tercio (5-8), 
    y que porcentaje representa este valor sobre el total de “tiradas”. Informarlo con una 
    función """

def es_perfecto(valor):
    divisores = 0
    for i in range(1,valor):
        if valor % i == 0:
            divisores += i
        i+=1
    if divisores == valor:
        return True

def seg_tercio(valor):
    if valor >= 5 and valor <= 8:
        return True

import random
def operaciones():
    contador = 0
    cont_perf = 0
    primer_numero = 0
    cont_mult = 0
    cont_copas = 0
    cont_basto = 0
    cont_tercio = 0
    while contador < 200:
        palo = random.randint(1,4)
        valor = random.randint(1,12)
        if es_perfecto(valor):
            cont_perf += 1
        if contador == 0:
            primer_numero = valor
        if valor % primer_numero == 0:
            cont_mult += 1
            print(valor, end=" ")
        if palo == 4 and valor == 1:
            cont_copas += 1
        if palo == 2 and valor == 12:
            cont_basto += 1
        if seg_tercio(valor):
            cont_tercio +=1
        contador += 1
    porcentaje_basto = cont_basto / 200 * 100
    porcentaje_tercio = cont_tercio / 200 * 100
    print("\n""Un valor perfecto salió",cont_perf,"veces")
    print("Un número múltiplo del primer número (",primer_numero,") en figurar, salió",cont_mult,"veces")
    print("El 1 de copas salió",cont_copas,"veces")
    print("El 12 de basto salió en un",porcentaje_basto,"%")
    print("Hay",cont_tercio,"valores que pertenecen al 2do tercio (5-8) y estos representan el",porcentaje_tercio,"% del total de las tiradas")
operaciones()
        
        
        
        
        
        