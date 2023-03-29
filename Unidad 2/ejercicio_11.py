""" Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a
cuántos billetes equivale, considerando que existen billetes de $1000, $500, $100, $50, $10, $5 y $1. 
Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""
def cajero_automático():
    usuario = int(input("Cúanta plata desea sacar del cajero automático: "))
    if usuario >= 1000:
        billete_mil = usuario // 1000
        print("Billetes de $1000:", billete_mil, "\n")
        usuario = usuario % 1000
    if usuario >= 500:
        billete_quinientos = usuario // 500
        print("Billetes de $500:", billete_quinientos, "\n")
        usuario = usuario % 500
    if usuario >= 100:
        billete_cien = usuario // 100
        print("Billetes de $100:", billete_cien, "\n")
        usuario = usuario % 100
    if usuario >= 50:
        billete_cincuenta = usuario // 50
        print("Billetes de $50:", billete_cincuenta)
        usuario = usuario % 50
    if usuario >= 10:
        billete_diez = usuario // 10
        print("Billetes de $10:", billete_diez)
        usuario = usuario % 10
    if usuario >= 1:
        billete_uno = usuario // 1
        print("Billetes de $1:", billete_uno)
        usuario = usuario % 1
cajero_automático()
    