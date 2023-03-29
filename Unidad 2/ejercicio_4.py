"""Escribir un programa que permita ingresar la edad de una persona en años y la convierta a días, imprimiendo el resultado. Considerar que todos los años tienen 365 días.
"""
def edad_expresada_en_dias():
    usuario = int(input("Introducir la edad de la persona: "))
    dias = usuario * 365
    print("La edad de la persona representado en dias es:", dias)
edad_expresada_en_dias()