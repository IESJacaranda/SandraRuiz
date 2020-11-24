"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 6
Realizar un programa que solicite tres valores de los lados de un posible 
triángulo e informe si es un triángulo o no.

"""


primerLado = int(input("Introduce el primer lado:"))
segundoLado = int(input("Introduce el primer lado:"))
tercerLado = int(input("Introduce el primer lado:"))

lados= [primerLado, segundoLado, tercerLado]

def esTriangulo(lados):
    esUnTriangulo = False
    
    if len(lados)==3 :
        if lados[0]+lados[1]<=lados[2]:
            esUnTriangulo = False
        elif lados[0]+lados[2]<=lados[1]:
            esUnTriangulo = False
        elif lados[1]+lados[2]<=lados[0]:
            esUnTriangulo = False
    else:
        esUnTriangulo = False
        
    return esUnTriangulo 

print(esTriangulo([3,4,5]))
print(esTriangulo([3,4,15]))
print(esTriangulo([3,3,3]))
print(esTriangulo([15,4,3]))
print(esTriangulo([3,1,4]))


"""
    meterlos en una lista tb podría hacerse (declaramos vacia y la definimos)
    lados= []
    lados.append(lado1)
    lados.append(lado2)
    lados.append(lado3)
"""
    
"""
Solucion clase: más sintética


primerLado = int(input("Introduce el primer lado:"))
segundoLado = int(input("Introduce el primer lado:"))
tercerLado = int(input("Introduce el primer lado:"))


lados= [primerLado, segundoLado, tercerLado]

def esTriangulo(lados):
   return len(lados)==3 and not ((lados[0]+lados[1]<=lados[2]) or
                            (lados[0]+lados[2]<=lados[1]) or
                            (lados[1]+lados[2]<=lados[0]))

    else:
        esUnTriangulo = False
        
    return esUnTriangulo
    
    
print(esTriangulo([3,4,5]))
print(esTriangulo([3,4,15]))
print(esTriangulo([3,3,3]))
print(esTriangulo([15,4,3]))
print(esTriangulo([3,1,4]))
"""