"""Ingresar 3 valores correspondientes a la longitud de los lados de un triángulo.
Informar:
a - Si los valores ingresados forman un triángulo.
b - Si se form un triángulo, que triángulo es?"""

lado_a = float(input("Introducir la medida del lado A: "))
lado_b = float(input("Introducir la medida del lado B: "))
lado_c = float(input("Introducir la medida del lado C: "))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c + lado_a > lado_a:
    print("Los valores ingresados forman un triángulo")
    if lado_a == lado_b == lado_c:
        print("Forma un triángulo equilátero")
    else:
        if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("Forma un triángulo isósceles")
        else:
            print("Forma un triángulo escaleno")
else:
    print("Los valores ingresados no forman un triángulo")