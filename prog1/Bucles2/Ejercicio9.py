"""
Ejercicio 9
Design a program that reads an integer positive number greater than 0 and says if it’s a “perfect number”. 
A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect.”
"""

#Solución 1:

def perfectNumber():
    number = 0
    while number <= 0:
        number = int(input("Enter an integer positive number greater than 0:"))
        if number <= 0:
            print("The number is not valid, try again.")
        else:
            sumaDivisor = 0
            for i in range(1, number // 2 + 1): 
                if number % i == 0:
                    sumaDivisor = sumaDivisor + i
            if sumaDivisor == number:
                print("The number is perfect")
            else:
                print("The number is not perfect")

perfectNumber()



"""
Solución 2 con dos funciones: 
def testNumbers():
    number = 0
    while number <= 0:
        number = int(input("Enter an integer positive number greater than 0: "))
        if number <= 0:
            print("The number is not valid, try again.")
        else:
            if perfectNumber(number):
                print("The number is perfect.")
            else:
                print("The number is not perfect.")


#Esta función me calcula si un número es perfecto
def perfectNumber (number):
    sumaDivisor = 0
    for i in range(1, number // 2 + 1): 
        if number % i == 0:
            sumaDivisor = sumaDivisor + i
    if sumaDivisor == number:
       return sumaDivisor     


testNumbers ()


"""