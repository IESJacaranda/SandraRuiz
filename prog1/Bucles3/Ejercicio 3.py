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
    