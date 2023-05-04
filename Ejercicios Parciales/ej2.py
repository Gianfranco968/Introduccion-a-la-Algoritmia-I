"""Leer un número entero cualquiera y mostrar el
mayor y el menor dígito que contenga el mismo.
# El número ingresado puede ser positivo, negativo
o 0, y no se permite el ingreso dígito a dígito.
Por ejemplo, si se ingresa 4375 debe mostrarse 7 y 3."""
def calculos():
    numero = int(input("Introducir números: "))
    num_grande = 0
    num_chico = 9
    if numero < 0:
        numero = numero * -1
        while numero != 0:
            ultimo_numero = numero % 10
            numero = numero // 10
            if ultimo_numero < num_grande:
                num_chico = ultimo_numero
            if ultimo_numero < num_chico:
                num_grande = ultimo_numero
        print("El número más grande fue:",num_grande)
        print("El número más chico fue:",num_chico)
        
    elif numero == 0:
        num_grande += 0
        num_chico -= num_chico
        print("El número más grande fue:",num_grande)
        print("El número más chico fue:",num_chico)
        
    else:
        while numero != 0:
            ultimo_numero = numero % 10
            numero = numero // 10
            if ultimo_numero > num_grande:
                num_grande = ultimo_numero
            if ultimo_numero < num_chico:
                num_chico = ultimo_numero
        print("El número más grande fue:",num_grande)
        print("El número más chico fue:",num_chico)
calculos()