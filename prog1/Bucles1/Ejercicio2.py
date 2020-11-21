"""
Ejercicio 2
Diseñar un programa que pida dos números. Deberá ver cuál de ellos es menor y mostrar todos los números comprendidos 
entre el valor menor y mayor, incluyendo ambos números.
"""

#Solución usando bucle for

numero1 = int(input("Dame un número"))
numero2 = int(input("Dame otro número"))
if numero1 < numero2:
    for i in range(numero1,numero2+1):
        print(i)
else:
    for i in range(numero2,numero1+1):
        print(i)
        
"""
Solución usando bucle while

numero1 = int(input("Dame un número"))
numero2 = int(input("Dame otro número"))
i = numero1
while i <= numero2:
    print(i)
    i = i + 1
i = numero2
while i <= numero1:
    print(i)
    i = i + 1
"""
