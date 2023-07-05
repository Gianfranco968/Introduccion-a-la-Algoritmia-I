"""
EJERCICIO 1
Se ingresa por teclado, el número de vendedor y el importe de cada venta realizado por éste.
El nro de vendedor puede ser 1, 2 o 3. Este dato deberá controlarse.
En un vector, se deberá ir cargando el número de vendedor y en otro el importe de cada
venta, correspondiéndose la posición de uno con la del otro.
El fin de la carga se indica con el vendedor 0.
Por fin de la carga, recorrer los vectores e indicar.
- Cuánto vendió cada vendedor (en dinero) y cuántas ventas hizo cada vendedor.
- Cuál fue el vendedor que más vendió, en dinero y cual fue el vendedor que más
  ventas hizo, en cantidad.
- Cuántas ventas superiores a $5000 hubo y cuál fue el porcentaje de éstas en
  relación a las ventas totales.
"""

def empresa():
    cant_ventas_1 = 0
    cant_ventas_2 = 0
    cant_ventas_3 = 0
    cant_sup_1 = 0
    cant_sup_2 = 0
    cant_sup_3 = 0
    dinero_vendedor_1 = 0
    dinero_vendedor_2 = 0
    dinero_vendedor_3 = 0
    vendedor = int(input("Introducir el número del vendedor (puede ser 1,2 o 3) (para finalizar la carga introducir 0): "))
    if vendedor != 0:
        while vendedor >= 1 and vendedor <= 3:
            if vendedor == 1:
                importe = int(input("Introducir el importe de la venta realizada: "))
                cant_ventas_1 += 1
                dinero_vendedor_1 += importe
                if dinero_vendedor_1 > 5000:
                    cant_sup_1 += 1
                vendedor = int(input("Introducir el número del vendedor (puede ser 1,2 o 3) (para finalizar la carga introducir 0): "))
            if vendedor == 2:
                importe = int(input("Introducir el importe de la venta realizada: "))
                cant_ventas_2 += 1
                dinero_vendedor_2 += importe
                if dinero_vendedor_2 > 5000:
                    cant_sup_2 += 1
                vendedor = int(input("Introducir el número del vendedor (puede ser 1,2 o 3) (para finalizar la carga introducir 0): "))
            if vendedor == 3:
                importe = int(input("Introducir el importe de la venta realizada: "))
                cant_ventas_3 += 1
                dinero_vendedor_3 += importe
                if dinero_vendedor_3 > 5000:
                    cant_sup_3 += 1
                vendedor = int(input("Introducir el número del vendedor (puede ser 1,2 o 3) (para finalizar la carga introducir 0): "))
    print("\n""El vendedor nro: 1 lo vendido está evaluado en",dinero_vendedor_1,"$","y realizó",cant_ventas_1,"ventas")
    print("\n""El vendedor nro: 2 lo vendido está evaluado en",dinero_vendedor_2,"$","y realizó",cant_ventas_2,"ventas")
    print("\n""El vendedor nro: 3 lo vendido está evaluado en",dinero_vendedor_3,"$","y realizó",cant_ventas_3,"ventas")
    
    if dinero_vendedor_1 > dinero_vendedor_2 and dinero_vendedor_1 > dinero_vendedor_3:
        print("\n""El vendedor que más vendió es el nro: 1 con un total de",dinero_vendedor_1,"$")
    elif dinero_vendedor_2 > dinero_vendedor_1 and dinero_vendedor_2 > dinero_vendedor_3:
        print("\n""El vendedor que más vendió es el nro: 2 con un total de",dinero_vendedor_2,"$")
    else:
        print("\n""El vendedor que más vendió es el nro: 3 con un total de",dinero_vendedor_3,"$")
    
    if cant_ventas_1 > cant_ventas_2 and cant_ventas_1 > cant_ventas_3:
        print("\n""El vendedor que más ventas realizó es el nro: 1 con un total de",cant_ventas_1,"$")
    elif cant_ventas_2 > cant_ventas_1 and cant_ventas_2 > cant_ventas_3:
        print("\n""El vendedor que más ventas realizó es el nro: 2 con un total de",cant_ventas_2,"$")
    elif cant_ventas_1 == cant_ventas_2 == cant_ventas_3:
        print("\n""Todos realizaron la misma cantidad de ventas")
    else:
        print("\n""El vendedor que más ventas realizó es el nro: 3 con un total de",cant_ventas_3,"ventas")
    
    cant_ventas_totales_sup = cant_sup_1 + cant_sup_2 + cant_sup_3
    cant_ventas_totales = cant_ventas_1 + cant_ventas_2 + cant_ventas_3
    porcentaje_sup = cant_ventas_totales_sup / cant_ventas_totales * 100
    print("\n""Se realizaron",cant_ventas_totales_sup,"ventas superiores a $5.000 en total y representa un",porcentaje_sup,"% de las ventas totales")
        
empresa()      

print("\n")
print("-----------------------------------------------------")
print("\n")
"""
EJERCICIO 2
- Cargar un vector A[10], de manera desordenada.
- Ordenarlo por el método de selección.
- Ingresar un valor por teclado, buscarlo, e informar con una leyenda, en que posición se lo encontró.
- Si no está, informarlo.
"""

import random

def operaciones():
    lista = []
    aux = 0
    
    for i in range(10):
        numeros = random.randint(0,100)
        lista.append(numeros)
    print(lista)
    
    for x in range(len(lista)):
        for z in range(x+1,len(lista)):
            if lista[x] > lista[z]:
                aux = lista[x]
                lista[x] = lista[z]
                lista[z] = aux
    print(lista)
    
    usuario = int(input("Introducir el valor que desea buscar: "))
    mini = 0
    maxi = len(lista)-1
    posicion = -1
    while mini <= maxi and posicion == -1:
        med = (mini + maxi) // 2
        if usuario == lista[med]:
            posicion = med
        if usuario > lista[med]:
            mini = med + 1
        else:
            maxi = med - 1
    if posicion != -1:
        print("El valor",usuario,"se encuentra en la posición",posicion)
    else:
        print("El valor",usuario,"NO se encuentra en la lista")
        
operaciones()