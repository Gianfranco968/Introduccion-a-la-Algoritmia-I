def salarios():
    contador_1 = 0
    contador_2 = 0
    sueldo_1 = 0
    sueldo_2 = 0
    sueldo_3 = 0
    sueldo_mas_bajo = 0
    empleado = int(input("Introducir la cantidad de empleados: "))
    for i in range(0,empleado):
        legajo = int(input("Introducir su legajo: "))
        categoria = int(input("Introducir su categoría: "))
        salario = float(input("Introducir su salario: "))
        if salario < 500000 and categoria == 3:
            contador_1 += 1
        if salario > 200000:
            contador_2 += 1
        if categoria == 1:
            sueldo_1 += salario
        elif categoria == 2:
            sueldo_2 += salario
        elif categoria == 3:
            sueldo_3 += salario
    importe_total = sueldo_1 + sueldo_2 + sueldo_3
    promedio_salario = importe_total / empleado
    print("\n""Cantidad de empleados que ganan más de $200.000:",contador_2)
    print("Cantidad de empleados que ganan menos de $50.000:",contador_1)
    print("Importe total de salarios pagados por la empresa:",importe_total)
    print("Importe total categoría 1:", sueldo_1)
    print("Importe total categoría 2:", sueldo_2)
    print("Importe total categoría 3:", sueldo_3)
    print("El promedio de salarios es de:",promedio_salario)
salarios()
            
    
    