"""
Ejercicio 1
Diseñar un programa para aprender a contar. El programa pedirá un número y mostrará todos los números comprendidos entre 
el 1 y el número introducido.
"""
#Solución usando bucle for


numero = int(input("¿Hasta qué número quieres contar?"))
for i in range(1,numero+1):
    print(i)
    
"""
Solución usando bucle while:

numero = int(input("¿Hasta qué número quieres contar?"))
i = 1
while i <= numero:
    print(i)
    i = i + 1

"""