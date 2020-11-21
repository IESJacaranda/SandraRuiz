"""
Ejercicio 7
Design a program that asks how many numbers the user wants to write. After the user enters all numbers, 
the program should say the medium of the numbers. If the user inputs a wrong number, the program should ask for it again. 
The messages are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not valid.
“The medium is XX.XX” to show the result.
"""

#Solución con while:


cantidadNumeros = int(input("Cuantos numeros quieres introducir?"))
suma = 0
i = 1
while i<=cantidadNumeros:
    numero = int(input("Introduce un numero mayor que 0:"))
    if numero>0:
        suma = suma+numero
        i += 1
    else:
        print("El número no es válido, debe ser mayor que 0.")
print("La media es "+str(suma/cantidadNumeros))
