"""
Ejercicio 8
Realizar un programa que lea por teclado las funciones de un reloj digital (horas, minutos, segundos) comprendidas entre las 
0.0.0 y las 23.59.59 e informe cuál de ellas es mayor.
Ejemplo:     Hora 1 → 12:35:37  ;    Hora 2 → 12:38:36
    “Hora 2 es mayor”

"""

hour1 = int(input("Introduzca la primera hora:"))
min1 = int(input("los minutos:"))
sec1 = int(input("los segundos:"))
hour2 = int(input("Introduzca la segunda hora:"))
min2 = int(input("los minutos:"))
sec2 = int(input("los segundos:"))
Calseg1 = hour1 * 3600 + min1 * 60 + sec1
Calseg2 = hour2 * 3600 + min2 * 60 + sec2
if hour1 >= 0 and hour1 <= 23 and min1 >= 0 and min1 <= 59 and sec1 >= 0 and sec1 <= 59 and hour2 >= 0 and hour2 <= 23 and min2 >= 0 and min2 <= 59 and sec2 >= 0 and sec2 <= 59:
    if Calseg1 > Calseg2:
        print("Hora 1 es mayor")
    elif Calseg1 < Calseg2:
        print("Hora 2 es mayor")
    else:
        print("Ambas horas son iguales")
else:
    print("Los datos introducidos no son correctos")