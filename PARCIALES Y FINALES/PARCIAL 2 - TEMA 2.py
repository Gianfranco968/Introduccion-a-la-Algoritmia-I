"""Ejercicio 
- Programar una función que reciba su D.N.I, ingresados en el programa principal, y lo muestre. 
- Obtener una lista con 20 valores que tengan raíz cuadrada exacta entre 5 y 500, determinado con una función y que no se repitan. 
- Recorrer la lista generada y pasar, a una segunda lista, aquellos valores que sean mayores al promedio entero, de toda la lista anterior. 
- Ordenar esta segunda lista de mayor a menor. 
- De la segunda lista, obtener una tercer lista, en el programa principal, con aquellos valores que sean oblongos, determinado con otra función,
  y mostrarla con los elementos separados por 5 espacios.
Número oblongo: es aquel número que es el resultado del producto de dos números consecutivos. Ej 42 = 6 * 7 -- 20 = 4 * 5 -- 56 = 7 * 8
Número con raiz cuadrada exacta: Ej: 25 - 49 - 100 - 16 - 9"""

import random

def documento(dni):
    print("Su DNI es:",dni)

def raiz_exacta(valor):
    for i in range(valor):
        if i * i == valor:
            return True

def numeros_oblongos(numero):
    for i in range(numero):
        if i * (i+1) == numero:
            return True

def operaciones():
    lista_uno = []
    lista_dos = []
    lista_tres = []
    contador = 0
    suma_valores = 0
    aux = 0
    dni = int(input("Introducir tu DNI: "))
    documento(dni)
    while contador < 20:
        valor = random.randint(5,500)
        if raiz_exacta(valor):
            if len(lista_uno) == 0:
                lista_uno.append(valor)
                suma_valores += valor
                contador += 1
            else:
                i = 0
                cont = 0
                while cont == 0 and i<len(lista_uno):
                    if lista_uno[i] == valor:
                        cont = 1
                    i += 1
                if cont == 0:
                    lista_uno.append(valor)
                    suma_valores += valor
                    contador += 1
    print(lista_uno)
    
    promedio = suma_valores // 20

    for i in range(len(lista_uno)):
        if lista_uno[i] > promedio:
            lista_dos.append(lista_uno[i])
    
    for x in range(len(lista_dos)):
        for z in range(len(lista_dos)):
            if lista_dos[z] < lista_dos[x]:
                aux = lista_dos[z]
                lista_dos[z] = lista_dos[x]
                lista_dos[x] = aux
    print(lista_dos)
    
    for a in range(len(lista_dos)):
        numero = lista_dos[a]
        if numeros_oblongos(numero):
            lista_tres.append(numero)
    
    for oblongos in range(len(lista_tres)):
        print(lista_tres[oblongos], end="     ")
        
operaciones()
   
#NO EXISTEN NÚMEROS OBLONGOS EN LA LISTA 3 POR ESO NO SE MUESTRA
        
