"""
Ejercicio 4
Realizar un programa que lea la edad de una persona menor a 100 años e informe de si es un niño (0-12 años), 
un adolescente (13-17), un joven (18-29) o un adulto.

"""

age = int(input("¿Qué edad tiene la persona?"))
if age >= 0 and age <= 12:
    print("Esa persona es un niño o una niña")
elif age >= 13 and age <= 17:
    print("Esa persona es un/una adolescente")
elif age >= 18 and age <= 29:
    print("Esa persona es un/una joven")
elif age >= 30 and age < 100:
    print("Esa persona es un adulto o una adulta")