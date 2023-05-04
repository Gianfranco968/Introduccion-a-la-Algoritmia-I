"""Una entidad bancaria cuenta con cajeros automáticos capaces de manejar cuatro 
denominaciones distintas de billetes. Actualmente se los carga con billetes de $1000, $500,
$200 y $100. Desarrollar un programa para ingresar una cantidad de dinero e imprimir
cuántos billetes de cada denominación debe entregar el cajero, teniendo en cuenta que:

a. Deberán rechazarse aquellos importes que no puedan entregarse con los billetes
presentes en el cajero. Por ejemplo, no es posible entregar $250 porque el billete
más pequeño es $100.

b. El programa debe minimizar la cantidad de billetes entregada, con la excepción
planteada en el punto siguiente.

c. Debe contemplarse la posibilidad de entregar "cambio" en todas las operaciones. Por 
eso, si una extracción no incluye billetes "pequeños" ($200 y $100) deberá 
reemplazarse uno de los billetes "grandes" ($1000 y $500) por su equivalente en 
denominaciones pequeñas.

Repetir el ingreso de montos a extraer hasta ingresar -1, rechazar los montos negativos.
Al finalizar informar cuántas extracciones necesitaron reemplazar uno de los billetes grandes 
para entregar cambio."""
def cajero():
    billete_mil = 0
    billete_quinientos = 0
    billete_doscientos = 0
    billete_cien = 0
    while True:
        cantidad = int(input("Introducir la cantidad de dinero (finalizar con -1): "))
        if cantidad != -1:
            if cantidad >= 1000:
                cantidad = cantidad % 1000
                billete_mil += 1
            if cantidad >= 500:
                cantidad = cantidad % 500
                billete_quinientos += 1
            if cantidad >= 200:
                cantidad = cantidad % 200
                billete_doscientos += 1
            if cantidad >= 100:
                cantidad = cantidad % 100
                billete_cien += 1
            if cantidad <= 100:
                billete_quinientos += 1
            if cantidad <= 200 and cantidad > 100:
                billete_mil += 1
            elif cantidad > 0 and cantidad < 100:
                print("Error, se debe introducir valores entre 100, 200, 500 y 1000")
        else:
            break
        print("Billetes de 1000:",billete_mil)
        print("Billetes de 500:",billete_quinientos)
        print("Billetes de 200:",billete_doscientos)
        print("Billetes de 100:",billete_cien)
cajero()






