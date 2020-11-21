"""
Ejercicio 1
Realizar un programa que lea un número entero por teclado e informe de si el número es par o impar (el cero se considera par).

"""

number = int(input("Dime un número:"))
if number % 2 == 1:
    print("El número es impar")
elif number % 2 == 0:
    print("El número es par")