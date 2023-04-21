"""Ingresar las notas de dos parciales de un alumno e indicar si promocionó,
aprobó o si debe recuperar.
Informar un error si el valor de alguna nota no está entre 0 y 10.
- Se promociona cuando las notas de ambos parciales son mayores o iguales a 7
- Se aprueba cuando las notas de ambos parciales son mayores o igual a 4
- Se debe recuperar cuando al menos una de las dos notas es menor a 4."""
def notas_facultad():
    a = int(input("Introducir la primera nota: "))
    b = int(input("Introducir la segunda nota: "))
    if a >= 7 and b >= 7:
        print("Promocionó la materia")
    elif a >= 4 and b >= 4:
        print("Aprobó la materia")
    elif a < 4 or b < 4:
        print("Debe recuperar algún  parcial")
    elif a < 0 or a > 10 and b < 0 or b > 10:
        print("Error, nota mal ingresada")
notas_facultad()