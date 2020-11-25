"""
Ejercicio 1
Design a method called factorial that receives a positive integer and returns the 
factorial. If the number is negative the method should return -1.


Factorial
El factorial de un entero positivo n, el factorial de n o n factorial se define 
en principio como el producto de todos los números enteros positivos desde 1 
(es decir, los números naturales) hasta n. Por ejemplo:

    5 ! = 1 × 2 × 3 × 4 × 5 = 120.

"""

numero=int(input("Dame un entero positivo "))
while numero<0:
    numero=int(input("Error. Dame un entero positivo: "))

def factorialNumero(numeros):
    for i in range (numeros):
        