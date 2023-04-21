"""Leer tres números correspondientes al dia, mes y año de una fecha e imprimir un mensaje indicando si la fecha es válida o no."""
def corroborar_fecha():
    dia = int(input("Introducir el dia: "))
    mes = int(input("Introducir el mes: "))
    año = int(input("Introducir el año: "))
    if año >= 1 and año <= 2023:
        if mes >= 1 and mes <= 12:
            if mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia >= 1 and dia <= 30:
                    print("La fecha es válida")
                else:
                    print("La fecha no es válida")
            if mes == 2:
                if dia >= 1 and dia <= 28:
                    print("La fecha es válida")
                else:
                    print("La fecha no es válida")
            else:
                print("La fecha es válida")
        else:
            print("La fecha no es válida")
    else:
        print("La fecha no es válida")
corroborar_fecha()