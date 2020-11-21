"""
Ejercicio 5
Design a program that asks for numbers until the user inputs a negative one. When this happens, the program will show how many 
positive numbers have been introduced by the user. The messages are the following:
“Enter a number (negative to finish):” 
“You have entered XX positive numbers.”
"""

#Solución con bucle while:

numero = int(input("Introduce un numero (negativo para terminar):"))
positivo = 0
while numero>=0:
    positivo += 1
    numero = int(input("Introduce un numero (negativo para terminar):"))
print("Has introducido "+str(positivo)+" positivos")

"""
Solución con bucle while y función def:

def positiveNumberAmount():
    num = int(input("Introduce un numero (negativo para terminar):"))
    positivo = 0
    while num>=0:
        positivo += 1
        num = int(input("Introduce un numero (negativo para terminar):"))
    return positivo
print("Has introducido "+str(positiveNumberAmount())+" numeros positivos")

"""