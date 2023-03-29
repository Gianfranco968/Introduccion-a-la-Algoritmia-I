"""Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
"""
def porcentajes():
    persona_1 = int(input("Introducir el valor de la primera persona: "))
    persona_2 = int(input("Introducir el valor de la segunda persona: "))
    persona_3 = int(input("Introducir el valor de la tercer persona: "))
    dinero_total = persona_1 + persona_2 + persona_3
    porcentaje_1 = persona_1 * 100 / dinero_total
    porcentaje_2 = persona_2 * 100 / dinero_total
    porcentaje_3 = persona_3 * 100 / dinero_total
    print("El porcentaje de la primera persona es de:",porcentaje_1,"\n"
          "El porcentaje de la segunda persona es de:",porcentaje_2,"\n"
          "El porcentaje de la tercera persona es de:",porcentaje_3)
porcentajes()