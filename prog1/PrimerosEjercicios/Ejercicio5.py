"""
Ejercicio 5
Realizar un programa que solicite cuatro números e imprima la media de los números. También debe imprimir aquellos números 
que sean superiores a la media.

"""

numero1 = int(input("Dame un número:"))
numero2 = int(input("Dame otro número:"))
numero3 = int(input("Dame otro número:"))
numero4 = int(input("Dame otro número:"))
media = (numero1 + numero2 + numero3 + numero4)/4
print("La media de los cuatro números es "+str(media))
if media < numero1:
    print(str(numero1)+" es superior a la media")
if media < numero2:
    print(str(numero2)+" es superior a la media")
if media < numero3:
    print(str(numero3)+" es superior a la media")
if media < numero4:
    print(str(numero4)+" es superior a la media")