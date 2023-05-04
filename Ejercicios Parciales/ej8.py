"""Hallar promedio divisores"""
def promediodivisores(nro):
    div = 1
    suma = 0
    contdiv = 0
    while nro >= div:
        if nro % div == 0:
            suma += div
            contdiv = contdiv + 1
            print(div, end=" ")
        div = div + 1
    promedio = suma / contdiv
    print("\n""El promedio de los divisores es",promedio)
promediodivisores(16)