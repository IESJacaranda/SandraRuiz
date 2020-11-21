"""
Ejercicio 2
Realizar un programa que solicite dos números por teclado e imprima en pantalla si son iguales, el primero mayor que el 
segundo o el primero más pequeño que el segundo.

"""

number1 = int(input("Dime un número"))
number2 = int(input("Dime otro número"))
if number1 == number2:
    print("Ambos números son iguales")
elif number1 < number2:
    print("El primer número es menor que el segundo")
elif number1 > number2:
    print("El primer número es mayor que el segundo")