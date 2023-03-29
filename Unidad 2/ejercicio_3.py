""" Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales."""
def calculo_promedio():
    nota_1 = int(input("Introducir la primer nota del parcial: "))
    nota_2 = int(input("Introducir la segunda nota del parcial: "))
    suma_de_notas = nota_1 + nota_2
    promedio = suma_de_notas / 2
    print("El promedio del alumno es de:", promedio)
calculo_promedio()