"""Ejercicio 
- Programar una función que reciba su D.N.I, ingresados en el programa principal, y lo muestre. 
- Obtener una lista con 30 valores deficientes, entre 10 y 1000, sin repetir. Determinar que no se repitan con una función.
- Recorrer la lista generada y pasar, a una segunda lista, aquellos valores que sean menores al promedio entero, de toda la lista generada.
- Ordenar esta segunda lista de mayor a menor y mostrarla, con los valores separados por 3 espacios. 
- De la segunda lista, obtener una tercer lista, en el programa principal, con aquellos valores que cuya suma de dígitos sea impar, determinado con otra 
  función, y mostrarla, ej: 25 --> 2 + 5 = 7 --> lista 3 
Número deficiente: es cuando la suma de sus divisores, sin considerar el propio número, es menor que el número, Ej 15 = 1 + 3 + 5 --> es deficiente."""

import random

def documento(dni):
    print("Su DNI es:",dni)

def valores_deficientes(valor):
    suma_divisores = 0
    for i in range(1,valor):
        if valor % i == 0:
            suma_divisores += i
        if valor > suma_divisores:
            return True

def suma_digitos(numero):
    digito = 0
    modulo = 1
    while modulo != 0:
        modulo = numero % 10
        digito += modulo
        numero = numero // 10
    if digito % 2 != 0:
        return True


def operaciones():
    contador = 0
    lista_uno = []
    lista_dos = []
    lista_tres = []
    suma_valores = 0
    aux = 0
    dni = int(input("Introducir su DNI: "))
    documento(dni)
    while contador < 30:
        valor = random.randint(10,1000)
        if valores_deficientes(valor):
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
    promedio = suma_valores // 30
    
    for x in range(len(lista_uno)):
        if lista_uno[x] < promedio:
            lista_dos.append(lista_uno[x])
            
    for i in range(len(lista_dos)):
        for j in range(len(lista_dos)):
            if lista_dos[j] < lista_dos[i]:
                aux = lista_dos[j]
                lista_dos[j] = lista_dos[i]
                lista_dos[i] = aux
                
    for a in range(len(lista_dos)):
        print(lista_dos[a], end="   ")
    print("\n")    
    for z in range(len(lista_dos)):
        numero = lista_dos[z]
        if suma_digitos(numero):
            lista_tres.append(numero)
    print(lista_tres)
operaciones()
