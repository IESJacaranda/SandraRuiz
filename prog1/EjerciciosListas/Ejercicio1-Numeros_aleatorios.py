'''
Ejercicio 1:

Crea un programa que genere 1OO números de forma aleatoria y que posteriormente 
    ofrezca al usuario la posibilidad de:
        1. Conocer el mayor de los números
        2. Conocer el menor de los números
        3. Obtener la suma de todos los números
        4. Obtener la media de los números
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

#Esta función crea una lista vacía en la que añade 100 números enteros aleatorios, siempre que no estén repetidos.
def generarNumerosAleatorios():
    aleatorios=[]
    for i in range(100):
        numeroAleatorio = random.randint(1,1000)
        aleatorios.append(numeroAleatorio)
        if numeroAleatorio not in aleatorios:
            aleatorios.append(numeroAleatorio)
    
    return aleatorios

#Esta función calcula el número mayor de una lista de números. Recibe una lista y devuelve el número mayor.
def numeroMayor(lista):
    mayor = -1
    if len(lista)>0:
        mayor = lista[0]
        for i in lista:
            if i > mayor:
                mayor = i

    return mayor

assert(numeroMayor([])==-1)
assert(numeroMayor([3,5,7])==7)

#Esta función calcula el número menor de una lista de números. Recibe una lista de números y devuelve el número menor.
def numeroMenor(lista):
    menor = -1
    if len(lista)>0:
        menor = lista[0]
        for i in lista:
            if i < menor:
                menor = i

    return menor

assert(numeroMenor([])==-1)
assert(numeroMenor([3,5,7])==3)

#Esta función calcula la suma de una lista de números. Recibe una lista de números y devuelve la suma de ellos.
def sumNumeros(lista):
    sumaNumeros=0
    for i in lista:
        sumaNumeros += i
        
    return sumaNumeros

assert(sumNumeros([3,5,7])==15)
assert(sumNumeros([])==0)

#Esta función calcula la media de los números de una lista, haciendo uso de una función que los suma.
def mediaNumeros(lista):
    media=0
    if len(lista)>0:
        media=round(sumNumeros(lista)/len(lista),2)
    
    return media


assert(mediaNumeros([3,5,7])==5)
assert(mediaNumeros([])==0)
assert(mediaNumeros([4,1,1,1])==1.75)

'''Esta función recibe una lista y comprueba si un elemento que se introduce por consola está contenido en la misma 
y de ser así lo sustituye. De no ser así devuelve un mensaje
'''
def sustituirNumero(lista, buscado, sustituto):
    for i in range(len(lista)):
        if buscado==lista[i]:
            lista[i]=sustituto
    
    return lista

assert(sustituirNumero([2,2,2], 2, 3)[2]==3)


def mostrarMenu():
    mensaje=""
    mensaje = "1. Conocer el mayor de los números.\n"
    mensaje+= "2. Conocer el menor de los números.\n"
    mensaje+= "3. Obtener la suma de todos los números.\n"
    mensaje+= "4. Obtener la media de los números.\n"
    mensaje+= "5. Sustituir el valor de un elemento por otro número introducido por teclado. \n"
    mensaje+= "6. Mostrar todos los números.\n"
    mensaje+= "Qué opción eliges? \n"
    
    return mensaje


def main():
    
    print(mostrarMenu())
        
    opcion=int(input(mostrarMenu()))
    while opcion<1 or opcion>6:
        opcion=int(input(mostrarMenu()))
        
    mensajeFinal=""
    if opcion==1:
        print("El numero mayor es el %s" % numeroMayor(generarNumerosAleatorios()))
    elif opcion==2:
        print("El numero menor es el %s" % numeroMenor(generarNumerosAleatorios()))
    elif opcion==3:
        print("La suma de los números es %s" % sumNumeros(generarNumerosAleatorios()))
    elif opcion==4:
        print("La media de los números es %s" % mediaNumeros(generarNumerosAleatorios()))
    elif opcion==5:
        buscado=int(input("Dime el número a sustituir: "))
        sustituto=int(input("Por que numero quieres sustituirlo?"))
        if buscado in sustituirNumero(generarNumerosAleatorios(), buscado, sustituto):
            print(sustituirNumero(generarNumerosAleatorios(),buscado,sustituto))
        else: #opcional, no lo pide el programa.
            print("El número no está en la lista.")
    elif opcion==6:
        print("Los números de la lista son: %s" % generarNumerosAleatorios())
        

main()
