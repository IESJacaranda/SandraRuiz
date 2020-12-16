'''
    1. Crea un programa que genere 1OO números de forma aleatoria y que posteriormente 
    ofrezca al usuario la posibilidad de:
        1. Conocer el mayor de los números
        2. Conocer el menor de los números
        3. Obtener la suma de todos los números
        4. Obtener la media d ellos números
        5. Sustituir el valor de un elemento por otro número introducido por teclado.
        6. Mostrar todos los números.
    Realiza las opciones con funciones.
'''
'''
#Números aleatorios:

import random

for i in range(10):
    numeroAleatorio = random.randint(1,100)
    print(numeroAleatorio) 

'''

import random

def generaNumerosAleatorios():
    listaAleatorios=[]
    for i in range(100):
        numeroAleatorio = random.randint(1,10000)
        listaAleatorios.append(numeroAleatorio)
        if numeroAleatorio not in listaAleatorios:
            listaAleatorios.append(numeroAleatorio)

    return listaAleatorios

print(generaNumerosAleatorios())

def menu():
    mensaje=""
    mensaje="1. Conocer el mayor de los números. /n"
    mensaje+="2. Conocer el menor de los números. /n"
    mensaje+="3. Obtener la suma de todos los números. /n"
    mensaje+="4. Obtener la media d ellos números. /n"
    mensaje+="5. Sustituir el valor de un elemento por otro número introducido por teclado. /n"
    mensaje+="6. Mostrar todos los números. /n"

    return mensaje

