"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 3
Diseñar un programa que lea números hasta que el usuario introduzca el 0. 
Debe informar de la media de los números leídos (sin tener en cuenta el 0) 
y el valor máximo y mínimo introducido.
"""

def pideNumeros():
    listaNumeros =[int(input("Dime un numéro (0 para parar): "))]
    print(mediaNum(listaNumeros))
    print(obtenerElMenorElemento(listaNumeros))
    print(obtenerElMayorElemento(listaNumeros))

            
def mediaNum(numbers):
    x=0
    total=0
    while x==0:
        listaNumeros.append(int(input("Dime un número (0 para parar): "))
        if number==0:
            total+=numbers
        else:
            x+=1
    return(total/numbers) 

    
def obtenerElMenorElemento(numbers):
    menor = numbers[0]
    for i in numbers:
        if i < menor:
            menor=i
            
    return menor


def obtenerElMayorElemento(numbers):
    mayor = numbers[0]
    for i in numbers:
        if i > mayor:
            mayor=i
            
    return mayor

pideNumeros()