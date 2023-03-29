"""Una persona invierte su capital en un banco y desea saber cuánto dinero ganará es un mes,
teniendo en cuenta que el banco paga 2% mensual. ¿Cúanto ganará en seis meses si deja su dinero invertido?"""
def ganancia():
    usuario = int(input("Introducir el capital que dispone: "))
    ganancia_mensual = usuario * 2 / 100
    ganancia_total = ganancia_mensual * 6
    print("En 1 mes obtendrá una ganancia de:", ganancia_mensual, "$", "\n"
          "En 6 meses obtendrá una ganancia de:", ganancia_total, "$")
ganancia()