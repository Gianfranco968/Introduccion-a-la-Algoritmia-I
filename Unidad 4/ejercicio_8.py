"""Ingresar números, hasta que la suma de los números pares supere 100.
Mostrar cuántos números se ingresaron en total"""
def calculo():
    suma = 0
    contador = 0
    while suma <= 100:
        nro = int(input("Ingrese un número: "))
        contador = contador + 1
        if nro % 2 == 0:
            suma = suma + nro
    print("Se ingresaron:",contador,"numeros", "y la suma es:",suma)
calculo()
    