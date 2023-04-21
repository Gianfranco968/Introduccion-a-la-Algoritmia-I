"""Diseñar un programa que calcule y muestre el sueldo neto de un empleado
en base a su sueldo básico y su antiguedad en años. Si es soltero se le incrementa
el suelo en 5% del salario bruto por cada año de antiguedad, mientras que si es casado
se le incrementa el suelo en 7% del bruto por cada año de antiguedad. También se le
realizan los siguientes descuentos: Jubilación: 11%, Obra Social: 3%, Sindicato: 3%"""
def sueldo_empleados():
    sueldo_basico = float(input("Introducir el sueldo básico del empleado: "))
    antiguedad = int(input("Introducir la antiguedad del empleado: "))
    estado_civil = int(input("Introducir 1 si es casado o 2 si es soltero: "))
    if estado_civil == 1:
        sueldo_bruto = sueldo_basico + (sueldo_basico / 100 * 7) * antiguedad
        sueldo_neto = sueldo_bruto - (sueldo_bruto / 100 * 17)
        print("Su antiguedad es:",antiguedad,"años","\n"
              "Su sueldo neto es:",sueldo_neto,"pesos")
    if estado_civil == 2:
        sueldo_bruto = sueldo_basico + (sueldo_basico / 100 * 5) * antiguedad
        sueldo_neto = sueldo_bruto - (sueldo_bruto / 100 * 17)
        print("Su antiguedad es:",antiguedad,"años","\n"
              "Su sueldo neto es:",sueldo_neto,"pesos")
sueldo_empleados()
        