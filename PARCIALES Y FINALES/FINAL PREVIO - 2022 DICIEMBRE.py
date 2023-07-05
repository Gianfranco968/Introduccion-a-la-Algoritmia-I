"""
EJERCICIO 1
Ingresar un número entero y positivo y generar la siguiente serie.
Si el valor es impar, multiplicarlo por 3 y sumarle 1; si el valor es par, dividirlo por 2.
Evaluar el resultado obtenido e Ir repitiendo las operaciones, según corresponda, hasta que el valor final sea 1.
Por ejemplo, se ingresa el 7.
7*3+1= 22/2= 11*3+1= 34/2= 17*3+1= 52/2= 26/2= 13*3+1= 40/2= 20/2= 10/2= 5*3+1= 16/2= 8/2= 4/2= 2/2= 1

Se solicita:
- Ir guardando los resultados obtenidos en una lista.
- Informar cuantos valores se guardaron en la lista.
- Informar si en la lista hay valores primos, y cuantos. Determinar si el valor es primo con una función.
- Mostrar la lista original con los valores separados por 3 espacios.
- Ordenar la lista de manera descendente y volverla a mostrar.

Número primo: Número divisible solamente por 1 y por si mismo. Ej 5
"""

def es_primo(numero):
    div = 1
    contdiv = 0
    while div <= numero:
        if numero % div == 0:
            contdiv += 1
        div += 1
    if contdiv <= 2:
        return True

def operaciones():
    lista = []
    contador = 0
    primos = 0
    aux = 0
    numero = int(input("Introducir un número: "))
    while numero !=1:
        if numero % 2 != 0:
            multiplicacion = numero * 3
            suma = multiplicacion + 1
            numero = suma
        print(numero, end=" ")
        lista.append(numero)
        if numero % 2 == 0:
            division = numero // 2
            numero = division
            if numero % 2 != 0:
                print(numero, end=" ")
                lista.append(numero)
    print("\n")
    print(lista)
    
    for valores in range(len(lista)):
        contador += 1
        if es_primo(lista[valores]):
            primos += 1
    print("En la lista se guardaron:",contador,"valores")
    print("En la lista hay:",primos,"valores primos")
    
    for numeros in range(len(lista)):
        print(lista[numeros], end="   ")
        
    print("\n")
    
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if lista[j] < lista[i+1]:
                aux = lista[j]
                lista[j] = lista[i+1]
                lista[i+1] = aux
    
    for numeros in range(len(lista)):
        print(lista[numeros], end="   ")
    
operaciones()

print("\n")

"""
EJERCICIO 2
Cargar una lista con 30 valores, generados aleatoriamente y que no se repitan, comprendidos entre 1 y 70.
Ingresar un dato por teclado, el que deberá estar comprendido entre los valores indicados.
Buscarlo en la lista obtenido utilizando la búsqueda binaria.
Si el valor no está, informarlo y permitir el ingreso de un nuevo dato a buscar.
Si el valor está, informar si es un número deficiente.

Número deficiente: Número que es mayor a la suma de sus divisores, sin considerar el propio número. Ej 8>1+2+4
"""

import random
def operaciones():
    contador = 0
    aux = 0
    lista = []
    while contador < 30:
        numeros = random.randint(1,70)
        if len(lista) == 0:
            lista.append(numeros)
            contador += 1
        else:
            i = 0
            cont = 0
            while cont == 0 and i<len(lista):
                if lista[i] == numeros:
                    cont = 1
                i += 1
            if cont == 0:
                lista.append(numeros)
                contador += 1
    
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    
    print(lista)
    
    suma = 0
    verificar = 0
    mini = 0
    maxi = len(lista)-1
    posicion = -1
    while verificar != 1:
        usuario = int(input("Introducir el valor que desea buscar: "))
        while mini <= maxi and posicion == -1:
            med = (mini + maxi) // 2
            if usuario == lista[med]:
                posicion = med
            if usuario > lista[med]:
                mini = med + 1
            else:
                maxi = med - 1
        if posicion != -1:
            for i in range(1,usuario):
                divisores = usuario % i
                if divisores == 0:
                    suma += i
            if suma < usuario:
                print("El número",usuario,"se encuentra en la posición",posicion,"y es un NÚMERO DEFICIENTE")
                verificar = 1
            else:
                print("El número",usuario,"se encuentra en la posición",posicion,"y NO es un NÚMERO DEFICIENTE")
                verificar = 1 
        else:
            print("El número",usuario,"NO está en la lista, introducir nuevamente")
            verificar = 0
        usuario = 0
        mini = 0
        maxi = len(lista)-1
        posicion = -1
operaciones()
                
                
                









