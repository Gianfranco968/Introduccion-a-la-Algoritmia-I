"""Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico
del libro es de $500, más $3,20 por página con encuadernación rústica. Si el número de páginas supera las 300
la encuadernación debe ser una tela, lo que incrementa el costo en $200. Además, si el número de páginas
sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incremental el costo en otros
$336. Desarrollar un programa que calcule el costo de un libro dado el número de páginas."""
def contaduria():
    libro = 500
    encuadernacion_tela = 200
    encuadernacion_especial = 336
    paginas = int(input("Introducir la cantidad de páginas: "))
    if paginas <= 300:
        costo_total = libro + paginas * 3.20
        print("El precio del libro es:",costo_total,"$")
    if paginas > 300 and paginas < 600:
        costo_total = libro + paginas * 3.20 + encuadernacion_tela
        print("El precio del libro es:",costo_total,"$")
    if paginas >= 600:
        costo_total = libro + paginas * 3.20 + encuadernacion_especial
        print("El precio del libro es:",costo_total,"$")
contaduria()
    