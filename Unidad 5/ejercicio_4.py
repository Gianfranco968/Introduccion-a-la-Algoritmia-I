"""Una empresa factura a sus clientes el último día de cada mes.
Si el cliente paga su factura dentro de los primeros 10 días del
mes siguiente, tiene un descuento de $200 o del 2% de la factura,
lo que resulte más conveniente para el cliente.
Si paga en los siguientes 10 días del mes deberá pagar el importe
original de la fatura, mientras que si paga después del día 20
deberá abonar una multa de $350 o del 10% de se factura, lo que
resulte mayor. Escribir un programa que lea el números del cliente
y el total de la factura, y emita un informe donde conste el número
del cliente y los tres importes que podría abonar según la fecha de
pago."""
def pago_sueldo():
    diez_dias = 200
    multa = 350
    numero_cliente = int(input("Introducir número cliente: "))
    total_factura = int(input("Introducir el valor total de la factura: "))
    descuento_porcentaje = total_factura - total_factura / 100 * 2
    descuento_pesos = total_factura - diez_dias
    if descuento_pesos > descuento_porcentaje:
        print("Los primeros 10 días tendrá que pagar", descuento_porcentaje)
    else:
        print("Los primeros 10 días tendrá que pagar", descuento_pesos)
    print("Si paga en los siguientes 10 dias tendrá que pagar",total_factura)
    aumento = total_factura + total_factura / 100 * 10
    if multa > aumento:
        print("La multa a pagar es:", multa)
    else:
        print("La multa a pagar es:", aumento)
pago_sueldo()