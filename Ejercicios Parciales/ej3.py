import random

def es_primo(valores):
    div = 1
    contdiv = 0
    while div <= valores:
        if valores % div == 0:
            contdiv += 1
        div += 1
    if contdiv <= 2:
        return True

def raiz_exacta(valores):
    for x in range(valores):
        if x * x == valores:
            return True

def cartas():
    cont_primo = 0
    cont_mult_dos = 0
    cont_espada = 0
    cont_oro = 0
    cont_raices = 0
    for i in range(0,80):
        palo = random.randint(1,4)
        valores = random.randint(1,12)
        primo = es_primo(valores)
        if primo == True:
            cont_primo += 1
            print(valores, end=" ")
        if valores % 2 == 0:
            cont_mult_dos += 1
        if palo == 3 and valores == 7:
            cont_espada +=1
        if palo == 1 and valores == 5:
            cont_oro += 1
        porcentaje = cont_oro / 80 * 100
        if raiz_exacta(valores) == True:
            cont_raices += 1
    print("Salieron",cont_primo,"veces valores primos")
    print("Salieron",cont_mult_dos,"numeros múltiplos de 2")
    print("El 7 de espada salió",cont_espada,"veces")
    print("Porcentaje correspondiente a la cantidad de veces que salió el 5 de oro:",porcentaje, "%")
    print("Cantidad de números con raíz exacta:",cont_raices)
cartas()
        
    