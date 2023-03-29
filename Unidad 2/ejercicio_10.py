"""Leer un período en segundos e imprimirlo expresado en días, horas, 
minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 
7 horas, 33 minutos y 20 segundos."""
def pasaje_de_unidades():
    periodo = int(input("Introducir el periodo en segundos: "))
    dias = periodo // (24 * 60 * 60)
    segundos = periodo % (24 * 60 * 60)
    horas = segundos // (60 * 60)
    segundos = periodo % (60 * 60)
    minutos = segundos // 60
    segundos = periodo % 60
    print("Dias", dias, "\n"
          "Horas:", horas,"\n"
          "Minutos:", minutos,"\n"
          "Segundos:", segundos)
pasaje_de_unidades()
    