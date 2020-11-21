"""
Ejercicio 10
Design a program that reads an integer positive number and says the “factorial” of the number. To calculate the factorial 
you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1 
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX”
"""

#Solución con for:

num = int(input("Introduce un numero entero positivo:"))
def factorial(num):
    resultado = 1
    if num==0 or num==1:
        resultado = 1
    else:
        for i in range(1,num+1):
            resultado = resultado*i
    return resultado
print("El factorial de "+str(num)+" es "+str(factorial (num)))


"""
Solución con for más compacta:

num = int(input("Introduce un numero entero positivo:"))
def factorial(num):
    resultado = 1
    if num>1:
        for i in range(1,num+1):
            resultado = resultado*i
    return resultado
print("El factorial de "+str(num)+" es "+str(factorial (num)))



Solución 1 con while

num = int(input("Introduce un numero entero positivo:"))
def factorial(num):
    resultado = 1
    contador = 1
    while contador <= num:
        resultado = resultado*contador
        contador = contador+1
    return resultado
print("El factorial de "+str(num)+" es "+str(factorial (num)))



Solución 2 con while

num = int(input("Introduce un numero entero positivo:"))
def factorial(num):
    resultado = 1
    while num > 1:
        resultado = resultado*num
        num = num-1
    return resultado
print("El factorial de "+str(num)+" es "+str(factorial (num)))



Solución con factorial recursivo (no entra en el examen, lo veremos más adelante):

num = int(input("Introduce un numero entero positivo:"))
def factorialRecursivo(num):
    return num > 1 and num * factorialRecursivo(num-1) or 1
print("El factorial de "+str(num)+" es "+str(factorialRecursivo (num)))

"""