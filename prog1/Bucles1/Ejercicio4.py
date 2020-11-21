"""
Ejercicio 4
Diseñar un programa que pida un número entero y nos muestre los 10 siguientes números que son múltiplos de 5.
"""

#Solución 1 usando bucle for

numero = int(input("De que numero quieres saber los siguientes diez múltiplos de 5?"))
for i in range(numero+1, numero+51):
    if i % 5 == 0:
        print(i)
        
"""
otra solución

number = int(input("Dime un número:"))
for i in range(number+1,number+6):
    if i % 5 == 0:
        base = i
for i in range(10):
    print(base + 5 * i)
    
"""
