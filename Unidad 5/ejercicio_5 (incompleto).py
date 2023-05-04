"""Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
un número entero N que representa una cantidad de días. Realizar un programa que
imprima la nueva fecha que resulta de sumar N días a la fecha dada. Tener en cuenta
los años bisiestos tal como se detalla en el ejercicio 7 de la practica 3."""
def calendario():
    D = int(input("Introducir el día: "))
    M = int(input("Introducir el mes: "))
    A = int(input("Introducir el año: "))
    N = int(input("Introducir la cantidad de días: "))
    if  A <= 2023 and A >= 1:
        if M == 4 or M == 6 or M == 8 or M == 11:
            if D <= 30 and D >= 1:
                D = D + N
                if D > 30:
                    resto = D - 30
                    D -= D
                    reinicio = resto
                    M = M + 1
                    print("Dia:",reinicio,"Mes:",M,"Año",A)
        if M == 2:
            if D <= 28 and D >= 1:
                D = D + N
            if D > 28:
                resto = D - 28
                D -= D
                reinicio = N + D + resto
                M = M + 1
                print("Dia:",reinicio,"Mes:",M,"Año",A)
        else:
            if D <= 31 and D >= 1:
                D = D + N
                if D > 31:
                    resto = D - 31
                    D -= D
                    reinicio = resto
                    M = M + 1
                    print("Dia:",reinicio,"Mes:",M,"Año",A)
calendario()    
