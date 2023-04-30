"""Escribir un programa que permita ingresar los números de legajo de los alumnos
de un curso y su nota de examen final. El fin de la carga se determina ingresando
un -1 en el legajo. Informar para cada alumno si aprobó o no el examen considerando
que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea
entre 1 y 10. Terminada la carga de datos, informar:
- Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
- Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
- Porcentaje de alumnos que están aplazados (tienen 1 en el examen)."""
def notas_alumnos():
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    legajo = int(input("Introducir número de legajo (finalizar -1): "))
    while legajo != -1:
        nota_final = int(input("Introducir nota final: "))
        if nota_final >= 1 and nota_final <= 10:
            if nota_final >= 4:
                contador_1 = contador_1 + 1
            if nota_final < 4:
                contador_2 = contador_2 + 1
            if nota_final == 1:
                contador_3 = contador_3 + 1
                porcentaje = nota_final / contador_3
                print("El porcentaje de alumnos aplazados son: ",porcentaje)
        print("La cantidad de alumnos que aprobaron con más o igual a 4: ",contador_1)
        print("La cantidad de alumnos que desaprobaron el examen con menos 4: ",contador_2)
notas_alumnos()