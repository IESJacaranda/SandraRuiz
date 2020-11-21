"""
Ejercicio 6
Design a program that reads two integer numbers, for example numberA and numberB, and calculates the product of both numbers without use multiplication, but using the sum. The messages are the following:
“Enter one number:”
“The product is XX”
"""

#Solución con bucle for (VALE PARA POSITIVOS):

numA = int(input("Introduce un numero entero:"))
numB = int(input("Introduce otro numero entero:"))
total = 0
for i in range(numB):
    total = total+numA
print(total)

"""
Solución con bucle for y función def (VALE PARA POSITIVOS):

numA = int(input("Introduce un numero entero:"))
numB = int(input("Introduce otro numero entero:"))
def multiplica(numA,numB):
    total = 0
    for i in range(numB):
        total = total+numA
    return total
print(multiplica(numA,numB))



Solución con bucle while y función def (VALE PARA POSITIVOS):

numA = int(input("Introduce un numero entero:"))
numB = int(input("Introduce otro numero entero:"))
def multiplica(numA,numB):
    total = 0
    counter = 0
    while counter<numB:
        total += numA
        counter += 1
    return total
print(multiplica(numA,numB))



Solución con bucle for y función def (VALE PARA POSITIVOS Y NEGATIVOS):

numA = int(input("Introduce un numero entero:"))
numB = int(input("Introduce otro numero entero:"))
def multiplica(numA,numB):
    result = 0
    if numA>=0:
        numB = 0-numB
        numA = 0-numA
    for i in range(numA,0):
        result = result+numB
    return 0-result
print("El resultado de la multiplicación de "+str(numA)+" y "+str(numB)+" es "+str(multiplica(numA,numB)))

"""