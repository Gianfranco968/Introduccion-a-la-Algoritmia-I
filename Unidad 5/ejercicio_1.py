"""Leer números que representan edades de un grupo de personas, finalizando
la lectura cuando se ingrese el número -1. Imprimir cuántos son menos
de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos
grupos. Descartar valores que no representan una edad válida. (Se
considera válida una edad entre 0 y 100)."""
def edad_valida():
    cantidad_menores = 0
    cantidad_mayores_o_igual = 0
    personas_1 = 0
    personas_2 = 0
    while True:
        persona = int(input("Introducir edad (finalizar con -1): "))
        if persona != -1:
            if persona >= 0 and persona <= 100:
                if persona < 18:
                    cantidad_menores += 1
                    personas_1 += persona
                if persona >= 18:
                    cantidad_mayores_o_igual += 1
                    personas_2 += persona
        else:
            break
    if cantidad_menores > 0 or cantidad_mayores_o_igual > 0:
        promedio_menores = personas_1 / cantidad_menores
        print("Hay",cantidad_menores,"personas menores de 18 años", "\n"
              "El promedio de edad de personas menores de 18 años es de:",promedio_menores,"\n")
    if cantidad_mayores_o_igual > 0:
        promedio_mayores_o_igual = personas_2 / cantidad_mayores_o_igual
        print("Hay",cantidad_mayores_o_igual,"personas mayores o igual a 18 años", "\n"
              "El promedio de edad de personas mayores o igual a 18 años es de:",promedio_mayores_o_igual)
edad_valida()

