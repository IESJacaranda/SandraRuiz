"""
Enunciado: Crea un programa que pida al usuario un entero mayor que 0 y
muestre por la salida estándar todos los números primos comprendidos
entre el número 1 y el facilitado por el usuario. Devuelve los resultados 
en una estructura de lista y haz uso de la función desarrollada previamente.
"""

def esNumeroPrimo(numero):
    divisor=0
    for i in range(1,numero):
        if numero%i==0:
            divisor+=i
    return divisor <= 2
    
def calculaNumerosPrimos(numero):
    lista=[]
    for i in range(2,numero + 1):
        if esNumeroPrimo(i):
            lista.append(i)
            
    return lista

numero = int(input("Introduce un numero entero mayor que 0: "))

print(calculaNumerosPrimos(numero))