"""Una empresa aplica el siguiente procedimmientos en la
comercialización de sus productos:
- Aplica el precio base a la primera docena de unidades.
- Aplica un 10% de descuento en todas las unidades entre
13 y 100.
- Aplica un 25% de descuento a todas las unidades por encima
de las 100.

Por ejemplo, supongamos que vende 230 unidades de un producto
cuyo precio base es 100. El cálculo resultante sería:
    100 * 12 + 90 * 88 + 75 * 130 = 18870
    y el promedio es de 18870/230 = 82.04
    
Escribir un programa que lea la cantidad solicitada de un
producto y su precio base, y muestre el valor total de la venta
y el precio promedio por unidad. El fin de la carga se determina
ingresando -1 como cantidad solicitada. Al finalizar informar:
- Cantidad de ventas realizadas total.
- Cantidad de ventas en las que se aplicó un 10% de descuento.
- Cantidad de ventas en las que SOLO se aplicó el precio base,
es decir que no se le realizaron descuentos."""
def contaduria():
    ventas_con_10 = 0
    ventas_mayores = 0
    ventas_solo_base = 0
    while True:
        cantidad = int(input("Introducir la cantidad solicitada del producto (finalizar con -1): "))
        if cantidad != -1:
            precio_base = int(input("Introducir precio base de la docena: "))
            if cantidad >= 0 and cantidad <= 12:
                ventas_solo_base += 1
                precio_1 = precio_base * cantidad
                suma_total = precio_1
            if cantidad >= 13 and cantidad <= 100:
                ventas_con_10 += 1
                descuento = precio_base - (precio_base * 10 / 100)
                precio_2 = descuento * cantidad
                suma_total = precio_1 + precio_2
            if cantidad > 100:
                ventas_mayores += 1
                descuento = precio_base - (precio_base * 25 / 100)
                precio_3 = descuento * cantidad
                suma_total = precio_1 + precio_2 + precio_3
            promedio = suma_total / cantidad
        else:
            break
        print("El valor total de la venta realizada es:",suma_total)
        print("El promedio por unidad es:",promedio)
        print("La cantidad de ventas realizadas es:", ventas_solo_base + ventas_con_10 + ventas_mayores)
        print("La cantidad de ventas realizadas con un 10% es:", ventas_con_10)
        print("La cantidad de ventas realizadas con el precio base:",ventas_solo_base)
contaduria()
            
    












