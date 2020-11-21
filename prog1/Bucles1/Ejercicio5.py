"""
Ejercicio 5
Diseñar un programa que muestre, para cada número introducido por teclado, si es par, si es positivo y su cuadrado. 
El proceso se repetirá hasta que el número introducido por teclado sea 0.
"""

#Solución 1 usando bucle while

numero = 1
while numero!=0:
    numero = int(input("De que numero quieres saber si es par, positivo y su cuadrado?"))
    if numero<0 or numero>0:
        if numero%2==0:
            print("El número es par")
        else:
            print("El número es impar")
        if numero>0:
            print("El número es positivo")
        else:
            print("El número es negativo")
        print("Su cuadrado es "+str(numero*numero))
print("0, sale del bucle")




"""
Solución 1 usando bucle while

numero = 1
while numero != 0:
    result = ""
    numero = int(input("Dime un numero"))
    if numero != 0:
        if numero % 2 == 0:
            result += ("Su número es par, ")
        else:
            result += ("Su número es impar, ")
        if numero > 0:
            result += ("positivo y su cuadrado es ")
        else:
            result += ("positivo y su cuadrado es ")
        result = result+str(numero*numero)
        print(result)
print("0, sale del bucle")

"""