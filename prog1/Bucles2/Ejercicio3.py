"""
Ejercicio 3
Design a program that asks how many numbers the user wants to introduce. Then, the user would have to introduce the numbers 
one by one and the program should say if each one of the numbers is odd or even. If the user inputs 0 or a negative number, 
it is not valid, and the system should ask for another number. The messages are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not valid.
“The number XX is odd”
“The number XX is even”
"""

#Solución con bucle while:

contadora = int(input("Cuantos numeros quieres introducir?"))
par = 0
i = 1
while i<=contadora:
    numero = int(input("Introduce un numero mayor que 0:"))
    if numero>0:
        if numero%2==0:
            print(str(numero)+" es par")
            par += 1
        else:
            print(str(numero)+" es impar")
        i += 1
    else:
        print("El número no es válido, debe ser mayor que 0")
print("Hay "+str(par)+" números pares y "+str(contadora-par)+" impares")


"""
Solución con bucle for y bucle while:


while True:
    howmany = int(input("How many numbers do you want input?"))
    even = 0
    odd = 0
    for i in range(howmany):
        num = int(input("Enter one number greater than 0:"))
        if num<0:
            print("The number is not valid, it should be greater than 0"")
            
"""