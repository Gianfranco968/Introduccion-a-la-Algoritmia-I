"""Leer un número binario ingresado como entero y mostrar un mensaje
informando cuántos dígitos contiene. Ejemplo: si se ingresa 1100101 se
debe informar "El número 1100101 tiene 7 dígitos."""

def es_primo(ultimo_numero):
    div = 1
    contdiv = 0
    while ultimo_numero >= div:
        if ultimo_numero % div == 0:
            contdiv = contdiv + 1
        div = div + 1
    if contdiv <= 2:
        return 1

numero = int(input("Introducir digitos: "))
contador = 0
while numero != 0:
    ultimo_numero = numero % 10
    if es_primo(ultimo_numero):
        contador += 1
    numero = numero // 10
print("El número tiene",contador,"digitos")