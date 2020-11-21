"""
Ejercicio 7
Realizar un programa que lea el estado civil de una persona (S-Soltero, C-Casado, V-Viudo y D-Divorciado) y su edad. 
Después debe mostrar por pantalla el porcentaje de retención que debe aplicarse de acuerdo con las siguientes reglas:
- A los solteros o divorciados menores de 35 años, un 12%.
- Todas las personas mayores de 50 años, un 8.5%.
- A los viudos o casados menores de 35 años, un 11.3%.
- Al resto de casos se aplica un 10.5%.

"""

edad = int(input("Introduce tu edad"))
estadocivil = input("Introduce tu estado civil")
if edad > 50:
    print("Tu porcentaje de retención es del 8.5%")
elif edad < 35:
    if estadocivil == "Soltero" or estadocivil == "soltero" or estadocivil == "Divorciado" or estadocivil == "divorciado":
        print("Tu porcentaje de retención es del 12%")
    elif estadocivil == "Casado" or estadocivil == "casado" or estadocivil == "Viudo" or estadocivil == "viudo":
        print("Tu porcentaje de retención es del 11.3%")
else:
    print("Tu porcentaje de retención es del 10.5%")