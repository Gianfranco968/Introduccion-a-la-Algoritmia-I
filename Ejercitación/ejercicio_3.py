"""Realizar un algoritmo que ingrese primero la cantidad de
empleados de la empresa y a continuación el sueldo de cada uno 
Informar:
Cantidad de sueldos mayores a 15000 
Cuantos sueldos hay entre 12000 y 20000 
Sueldo máximo"""
def sueldo():
    sueldo_mayor = 0
    sueldo_medio = 0
    sueldo_maximo = 0
    empleados = int(input("Introducir la cantidad de empleados: "))
    for i in range(empleados):
        sueldo_empleado = int(input("Introducir el suelo del empleado: "))
        if sueldo_empleado > 15000:
            sueldo_mayor += 1
        if sueldo_empleado >= 12000 and sueldo_empleado <= 20000:
            sueldo_medio += 1
        if i == 0 or sueldo_empleado > sueldo_maximo:
            sueldo_maximo = sueldo_empleado
    print("La cantidad de sueldos mayores a $15.000 son:",sueldo_mayor)
    print("La cantidad de sueldos entre $12.000 y $20.000 son:",sueldo_medio)
    print("El sueldo máximo es:",sueldo_maximo)
sueldo()
            