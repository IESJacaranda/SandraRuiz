'''
    1. Crea un programa que genere 1OO números de forma aleatoria y que posteriormente 
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
        
    print(aleatorios)
    
    return aleatorios

#Esta función calcula el número mayor de una lista de números. Recibe una lista y devuelve el número mayor.
def numeroMayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i

    return mayor


#Esta función calcula el número menor de una lista de números. Recibe una lista de números y devuelve el número menor.
def numeroMenor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i

    return menor


#Esta función calcula la suma de una lista de números. Recibe una lista de números y devuelve la suma de ellos.
def sumNumeros(lista):
    sumaNumeros=0
    for i in lista:
        sumaNumeros += i
        
    return sumaNumeros


#Esta función calcula la media de los números de una lista, haciendo uso de una función que los suma.
def mediaNumeros(lista):
    return sumNumeros(lista)/len(lista)


'''Esta función recibe una lista y comprueba si un elemento que se introduce por consola está contenido en la misma 
y de ser así lo sustituye. De no ser así devuelve un mensaje
'''
def sustituirNumero(lista):
    numero=int(input("Dime un número: "))
    if numero not in lista:
        resultado="El número no está en la lista."
    else:
        sustituto=int(input("Por que numero quieres sustituirlo?"))
        for i in range(len(lista)):
            if lista[i]==numero:
                lista[i]=sustituto
        resultado="La lista nueva es %s" % lista
    
    return resultado


def mostrarMenu():
    mensaje=""
    mensaje = "1. Conocer el mayor de los números.\n"
    mensaje+= "2. Conocer el menor de los números.\n"
    mensaje+= "3. Obtener la suma de todos los números.\n"
    mensaje+= "4. Obtener la media de los números.\n"
    mensaje+= "5. Sustituir el valor de un elemento por otro número introducido por teclado. \n"
    mensaje+= "6. Mostrar todos los números.\n"

    return mensaje


def main():

    print(mostrarMenu())
    
    opcion=int(input("Qué opción eliges? "))
    while opcion<1 or opcion>6:
        opcion=int(input("Qué opción eliges? "))
        
    mensajeFinal=""
    if opcion==1:
        mensajeFinal = "El numero mayor es el %s" % numeroMayor(generarNumerosAleatorios())
    elif opcion==2:
        mensajeFinal = "El numero menor es el %s" % numeroMenor(generarNumerosAleatorios())
    elif opcion==3:
        mensajeFinal = "La suma de los números es %s" % sumNumeros(generarNumerosAleatorios())
    elif opcion==4:
        mensajeFinal = "La media de los números es %s" % mediaNumeros(generarNumerosAleatorios())
    elif opcion==5:
        mensajeFinal = "%s" % sustituirNumero(generarNumerosAleatorios())
    elif opcion==6:
        mensajeFinal = "Los números de la lista son: %s" % generarNumerosAleatorios()
        
    return mensajeFinal

print(main())
