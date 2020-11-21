"""
Ejercicio 4
Design a program that reads a positive number N greater than 0 and show the result of the sum of the N numbers between 1 and N. 
If the number N is not valid, the program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.”
"""

#Solución con bucle while y con fórmula: no es esta solución la mejor, mejor sin fórmula

numero = int(input("Introduce un numero mayor que 0:"))
resultadoOK = False
while resultadoOK==False:
    if numero>0:
        print("La suma de los "+str(numero)+" primeros números es "+str((numero*(numero+1))/2))
        resultadoOK = True
    else:
        numero = int(input("El número no es correcto. Introduce un numero mayor que 0:"))


"""
Solución con bucle while y bucle for sin fórmula:

numero = 0
suma = 0
while numero<1:
    numero = int(input("Introduce un numero mayor que 0:"))
    if numero<1:
        print("El número no es correcto. Introduce un numero mayor que 0:")
for i in range(1,numero+1):
    suma = suma+i
print("La suma de los "+str(numero)+" primeros números es "+str(suma))



Solución con 2 bucles while:

numero = 0
suma = 0
while numero<1:
    numero = int(input("Introduce un numero mayor que 0:"))
    if numero<1:
        print("El número no es correcto. Introduce un numero mayor que 0:")
while numero>0:
    suma = suma+numero
    numero = numero-1
print("La suma de los números hasta el numero introducido es "+str(suma))

"""