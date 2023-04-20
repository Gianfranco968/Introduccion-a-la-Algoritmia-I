"""Una remisería requiere un programa que calcule el precio de un viaje a partir de
la cantidad de kilómetros que desea recorrer el usuario.
Para eso cuenta con la siguiente tarifa:
- Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo.
- Si recorre entre 0 y 10 km: $30 por km
- Si recorre 10 km o más: $20 por km"""
viaje_minimo = 250
precio_1 = 30
precio_2 = 20
def calculo_viaje():
    viaje = int(input("Introducir la cantidad de kilómetros: "))
    if viaje >= 0 and viaje < 10:
        costo = viaje_minimo + viaje * precio_1
        print(costo)
    if viaje >= 10:
        costo = viaje_minimo + viaje * precio_2
        print(costo)
calculo_viaje()