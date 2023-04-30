"""Se debe analizar cuántos autos circulan con patente con numeración
par y cuántos con numeración impar en un día. Escribir un programa
que permite ingresar la terminación de la pantente (entre 0 y 9)
hasta ingresar -1 e informe cuántos vehiculos pasaron con numeración
par y cuántos con numeración impar."""
def patentes():
    contador_par = 0
    contador_impar = 0
    patente = int(input("Introducir el número de una patente (finalizar con -1): "))
    while patente != -1:
        if patente % 2 == 0:
            contador_par = contador_par + 1
        if patente % 2 != 0:
            contador_impar = contador_impar + 1
        patente = int(input("Introducir el número de una patente (finalizar con -1): "))
    print("En el dia de hoy pasaron:",contador_par,"autos con patente par")    
    print("En el dia de hoy pasaron:",contador_impar,"autos con patente impar")
patentes()