"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 3
Diseñar un programa que lea números hasta que el usuario introduzca el 0. 
Debe informar de la media de los números leídos (sin tener en cuenta el 0) 
y el valor máximo y mínimo introducido.
"""

def pideNumeros():
    num=-1
    listaNumeros = []
    while num!=0:
        num=int(input("Dime un número (0 para parar): "))
        if num!=0:
            listaNumeros.append(num)
                    
    print("La media de los numeros es "+str(mediaNum(listaNumeros)))
    print("El valor minimo introducido es "+str(obtenerElMenorElemento(listaNumeros)))
    print("El valor maximo introducido es "+str(obtenerElMayorElemento(listaNumeros)))

            
def mediaNum(numbers):
    total=0
    numberCounting=0
    for i in numbers:
        numberCounting+=1
        total+=i

    return(total/numberCounting) 

    
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