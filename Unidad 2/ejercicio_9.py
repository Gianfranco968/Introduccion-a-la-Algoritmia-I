"""Una inmobiliaria paga a sus vendedores un salario de $50000, más una 
comisión de $5000 por cada venta realizada, más el 5% del valor de las 
ventas. Realizar un programa que imprima el número del vendedor y el 
salario que le corresponde en un determinado mes. Se leen el número 
del vendedor, la cantidad de ventas que realizó y el valor total de las 
mismas."""
def calculo_sueldo():
    empleado = int(input("Introducir el número de empleado: "))
    ventas = int(input("Introducir la cantidad de ventas realizadas por el mismo: "))
    valor = int(input("Introducir el valor total de las mismas: "))
    salario = 50000
    comisión = 5000 * ventas
    valor_ventas = valor * 5 / 100
    suma_total = salario + comisión + valor_ventas
    print("Empleado número:", empleado,"\n"
          "Salario correspondiente:",suma_total)
calculo_sueldo()