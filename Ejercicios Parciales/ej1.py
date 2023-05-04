def deficiente(numeros):
    div = 1
    contdiv = 0
    while numeros > div:
        if numeros % div == 0:
            resto = numeros // div
            if resto != numeros:
                contdiv += resto
        div += 1
    if contdiv < numeros:
        return True

import random
def valores_deficientes():
    deficientes = 0
    for i in range(0,50):
        numeros = random.randint(50,200)
        if deficiente(numeros):
            deficientes += 1
    print("Existen:",deficientes,"numeros deficientes")
valores_deficientes()