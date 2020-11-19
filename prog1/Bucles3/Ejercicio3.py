"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 3
Diseñar un programa que lea números hasta que el usuario introduzca el 0. 
Debe informar de la media de los números leídos (sin tener en cuenta el 0) 
y el valor máximo y mínimo introducido.
"""


            
def media(numbers):
    total=0
    numberCounting=0
    for i in numbers:
        numberCounting+=1
        total+=i

    return(total/numberCounting) 

    
def minimo(numbers):
    menor = numbers[0]
    for i in numbers:
        if i < menor:
            menor=i
            
    return menor


def maximo(numbers):
    mayor = numbers[0]
    for i in numbers:
        if i > mayor:
            mayor=i
            
    return mayor


def calculaMediaMinimoMaximo():
    num=-1
    listaNumeros = []
    while num!=0:
        num=int(input("Dime un número (0 para parar): "))
        if num!=0:
            listaNumeros.append(num)
    return "La media es %s, el minimo %s y el maximo %s" % (media(listaNumeros), minimo(listaNumeros), maximo(listaNumeros))                
    
print(calculaMediaMinimoMaximo())


"""
La solución de clase sin listas (permite salida si el numero introducido es 0).

def calculaMediaMinimoMaximo():
    sumatorio = 0
    
    numero = int(input("Introduce un número: "))
    maximo = numero
    minimo = numero
    i = 1
    
    while numero!=0:
        sumatorio += numero
        if numero < minimo:
            minimo = numero
        if numero > maximo
            maximo = numero
        num=int(input("Dime un número (0 para parar): "))
        if numero!=0:
            i+=1
        
    return "La media es %s, el minimo %s y el maximo %s" % (sumatorio/i, minimo, maximo)                
    
print(calculaMediaMinimoMaximo())


Solución de clase con listas (con listas es menos eficiente, pq hay que
recorrer la lista completa):

def pideNumeros():
    listaNumeros = []
    
    num=int(input("Dime un número (0 para parar): "))
    listaNumeros.append(num)
    
    while num!=0:
        num=int(input("Dime un número (0 para parar): "))
        if numero!=0
            listaNumeros.append(num)
    
    return listaNumeros            
    
    
def calculaMinMaxMedia(lista):
    sumatorio = 0
    minimo = 0
    maximo = 0
    
    for numero in lista:
        sumatorio += numero
        if numero < minimo:
            minimo = numero
        if numero > maximo
            maximo = numero
            
    return "La media es %s, el minimo %s y el maximo %s" % (sumatorio/len(lista), minimo, maximo)                

print(calculaMinMaxMedia(pideNumeros()))
"""