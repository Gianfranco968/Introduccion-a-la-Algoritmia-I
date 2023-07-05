'''-------------------------Final fundamentos-------------------------'''
"""Funcion para que inserte nombre y carrera"""
'''
Insertar numeros primos random a una lista.
Que se inserten de esos numeros solo 30 y sin repetir.
Ordenarlo con x método de ordenamiento.
Utilizar x método de busqueda para saber si ese numero esta o no en la lista.
'''
import random

def facultad():
    nombre = input("Introducir el nombre: ")
    carrera = input("Introducir la carrera: ")
    print(nombre)
    print(carrera)
facultad()

def operaciones():
    lista = []
    contador = 0
    aux = 0
    while contador < 30:
        numero = random.randint(0, 1000)
        div = 1
        contdiv = 0
        while div <= numero:
            if numero % div == 0:
                contdiv += 1
            div += 1
        if contdiv <= 2:
            if len(lista) == 0:  
                lista.append(numero)
                contador += 1
            else:
                i = 0
                cont = 0
                while cont == 0 and i<len(lista):
                    if lista[i] == numero:
                        cont = 1
                    i += 1
                if cont == 0:
                    lista.append(numero)
                    contador += 1
    
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] > lista[i+1]:
                aux = lista[j]
                lista[j] = lista[i+1]
                lista[i+1] = aux
    print(lista)
    
    usuario = int(input("Introducir el valor que desea averigurar su posición: "))
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
