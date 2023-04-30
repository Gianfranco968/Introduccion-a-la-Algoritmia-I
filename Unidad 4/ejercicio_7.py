"""Leer 10 números enteros e imprimir su promedio, el mayor valor leído
y en que posición se encontraba. Si se ingresó más de una vez sólo debe
informar la primera."""
def calculo():
    nro = int(input("Introducir un número: "))
    promedio = nro
    mayor = nro
    posicion = 1
    for i in range (2,11):
        nro = int(input("Introducir un número: "))
        promedio += nro
        if nro > mayor:
            mayor = nro
            posicion = i
    calculo_promedio = promedio / 10
    print("El promedio es:",calculo_promedio, "\n"
          "El mayor valor es:",mayor, "\n"
          "La posición es:",posicion)
calculo()
        