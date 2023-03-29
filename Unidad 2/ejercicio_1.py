"""Calcular el valor de las siguientes expresiones, respetando el orden de operaciones establecido"""
#a. 12 * 4 + 4 * 5
def punto_a():
    multiplicación_1 = 12 * 4
    multiplicación_2 = 4 * 5
    resultado = multiplicación_1 + multiplicación_2
    print(resultado)
punto_a()

#b. (12 * (1 - 5) + 4) * 3
def punto_b():
    resta = (1 - 5)
    multiplicación_1 = 12 * resta + 4
    multiplicación_2 = multiplicación_1 * 3
    print(multiplicación_2)
punto_b()

#c. 12 * 1 - 5 + 4 * 3
def punto_c():
    multiplicación_1 = 12 * 1
    multiplicación_2 = 4 * 3
    resultado = multiplicación_1 - 5 + multiplicación_2
    print(resultado)
punto_c()

#d. (17 - 2) / 5
def punto_d():
    resta = 17 - 2
    división = resta / 5
    print(división)
punto_d()

#e. 3 + 2 * 2 - (8 * 4 + 1 / 2.0) * 3
def punto_e():
    multiplicación_1 = 2 * 2
    suma_1 = 3 + multiplicación_1
    multiplicación_2 = 8 * 4
    división = 1 / 2.0
    suma_2 = multiplicación_2 + división
    multiplicación_3 = suma_2 * 3
    resultado = suma_1 - multiplicación_3
    print(resultado)
punto_e()

#f. 5 * 4 / 2
def punto_f():
    multiplicación = 5 * 4
    división = multiplicación / 2
    print(división)
punto_f()
    
#g. 5 * (4 / 2)
def punto_g():
    división = 4 / 2
    multiplicación = 5 * división
    print(multiplicación)
punto_g()

#h. 24 / 2 ** 2
def punto_h():
    potencia = 2 ** 2
    división = 24 / potencia
    print(división)
punto_h()

#i. (24 / 2) ** 2
def punto_i():
    división = 24 / 2
    potencia = división ** 2
    print(potencia)
punto_i()

#j. 3 + 4 * 6 / 2 – 5
def punto_j():
    multiplicación = 4 * 6
    división = multiplicación / 2
    resultado = 3 + división - 5
    print(resultado)
punto_j()

#k. 3 + 4 * 6 / (2 – 5)
def punto_k():
    multiplicación = 4 * 6
    resta = 2 - 5
    división = multiplicación / resta
    resultado = 3 + división
    print(resultado)
punto_k()

#l. (- 0.1) * 3
def punto_l():
    multiplicación = -0.1 * 3
    print(multiplicación)
punto_l()

#m. – 9 ** 2
def punto_m():
    potencia = -9 ** 2
    print(potencia)
punto_m()

#n. (– 9) ** 2
def punto_n():
    potencia = (-9) ** 2
    print(potencia)
punto_n()

#o. 10 / 3
def punto_o():
    división = 10 / 3
    print(división)
punto_o()

#p. 10 // 3
def punto_p():
    división = 10 // 3
    print(división)
punto_p()

#q. 12 % 5
def punto_q():
    porcentaje = 12 * 5 / 100
    print(porcentaje)
punto_q()


