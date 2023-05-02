"""En una veterinaria, se ingresa el tipo
de animal, siendo ellos 1-perro, 2-gato,
3-conejo y por cada uno se ingresa 1 o 2,
correspondiendo al macho y hembra, respectivamente
El fin del ingreso se indica ingresando -1.
Informar:
-La cantidad de animales tratados, cuantas
hembras perras y cuantos machos conejos se trataron.
-Porcentaje de gatos ingresados."""
def veterinaria():
    cant_animales = 0
    cant_gatos = 0
    cant_hembras_perras = 0
    cant_machos_conejos = 0
    while True:
        animal = int(input("Introducir 1-perro, 2-gato, 3-conejo (finalizar con -1): "))
        if animal != -1:
            genero = int(input("Introducir 1 si es macho o 2 si es hembra: "))
            cant_animales += 1
            if animal == 1 and genero == 2:
                cant_hembras_perras += 1
            if animal == 3 and genero == 1:
                cant_machos_conejos += 1
            if animal == 2:
                cant_gatos += 1
        else:
            break
    porcentaje = cant_gatos / cant_animales * 100
    print("Cantidad de animales tratados:",cant_animales)
    print("Cantidad de hembras perras tratadas:",cant_hembras_perras)
    print("Cantidad de machos conejos tratados:",cant_machos_conejos)
    print("Porcentaje de gatos ingresados:",porcentaje, "%")
veterinaria()