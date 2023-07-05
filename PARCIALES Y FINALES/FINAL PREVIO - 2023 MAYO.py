"""
- Programar una función que reciba su nro de documento,desde el programa principal, y lo muestre.
- Generar dos listas, de forma aleatoria, con valores comprendidos entre 5 y 500,La cantidad de valores
  de cada lista deberá ser ingresada por teclado, debiendo estar entre 5 y 15. Deberá controlarse que
  el valor ingresado esté dentro de los valores mencionados. Las longitudes de cada lista pueden ser
  distintas o iguales. Una función ordenará cada lista, de manera ascendente, por cualquier método. 
- Obtener una tercer lista,que resulta ser la unión de las dos listas anteriores. Cabe aclarar que la
  tercer lista,en la medida que se va creando, ya debe ir quedando ordenada. Dicho de otra manera, no es
  válido crear la tercer lista con una lista detrás de la otra y después se ordena la tercera lista. 
- Mostrar las 3 listas Ej: lista1[2,5,7,8] ya ordenada -lista2[1,4,15,20,25] ya ordenada Lista3 Primero
  pasa el 1, luego el 2, luego el 4, luego el 5, luego el 7 y el 8 y por último, todo lo que resta de la
  lista 2. Quedando lista3[1,2,4,5,7,8,15,20,25] Ingresar un valor por teclado, comprendido entre 5 y 500,
  y verificar si se encuentra en la terceralista, utilizando la búsqueda binaria.
"""
import random

def documento(dni):
    print("Su documento es:",dni)
    
def operaciones():
    lista_uno = []
    lista_dos = []
    lista_tres = []
    aux_1 = 0
    aux_2 = 0
    
    dni = int(input("Introducir su DNI: "))
    documento(dni)
    
    long_1 = int(input("Cuántos valores desea ingresar en la 1er lista (debe estar entre 5 y 15): "))
    long_2 = int(input("Cuántos valores desea ingresar en la 2da lista (debe estar entre 5 y 15): "))
    
    if long_1 >= 5 and long_1 <= 15:
        for cantidad in range(long_1):
            valor_1 = random.randint(5,500)
            lista_uno.append(valor_1)
        for x in range(len(lista_uno)-1):
            for z in range(len(lista_uno)-1):
                if lista_uno[z] > lista_uno[x+1]:
                    aux_1 = lista_uno[z]
                    lista_uno[z] = lista_uno[x+1]
                    lista_uno[x+1] = aux_1
        print(lista_uno)
        
    if long_2 >= 5 and long_2 <= 15:        
        for cantidad in range(long_2):
            valor_2 = random.randint(5,500)
            lista_dos.append(valor_2)
        for x in range(len(lista_dos)-1):
            for z in range(len(lista_dos)-1):
                if lista_dos[z] > lista_dos[x+1]:
                    aux_2 = lista_dos[z]
                    lista_dos[z] = lista_dos[x+1]
                    lista_dos[x+1] = aux_2    
        print(lista_dos)
    
    a = 0
    b = 0
    while a != long_1 and b != long_2:
        if lista_uno[a] > lista_dos[b]:
            lista_tres.append(lista_dos[b])
            b += 1
        elif lista_uno[a] < lista_dos[b]:
            lista_tres.append(lista_uno[a])
            a += 1
    print(lista_tres)
    
    usuario = int(input("Introducir un valor entre 5 y 500: "))
    if usuario >=5 and usuario <= 500:
        mini = 0
        maxi = len(lista_tres)-1
        posicion = -1
        while mini <= maxi and posicion == -1:
            med = (mini + maxi) // 2
            if usuario == lista_tres[med]:
                posicion = med
            if usuario > lista_tres[med]:
                mini = med + 1
            else:
                maxi = med - 1
        if posicion != -1:
            print("El valor",usuario,"se encuentra en la posición",posicion)
        else:
            print("El valor",usuario,"NO se encuentra en dicha lista")
    else:
        print("ERROR --> dicho valor no se encuentra entre 5 y 500")
    
operaciones()






