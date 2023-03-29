"""Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas."""
"""Los factores de conversión son:"""
# 1 pie = 12 pulgadas
# 1 yarda = 3 pies
# 1 pulgada = 2,54 cm
# 1 metro = 100 cm
def conversor():
    usuario = int(input("Introducir medida en metros: "))
    medida_pulgadas = usuario * 100 / 2.54
    medida_centimetros = usuario * 100
    medida_pies = medida_pulgadas / 12
    medida_yardas = medida_pies / 3
    print("En centímetros son:", medida_centimetros,"\n"
          "En pulgadas son:", medida_pulgadas, "\n"
          "En pies son:", medida_pies,"\n"
          "En yardas son:", medida_yardas)
conversor()