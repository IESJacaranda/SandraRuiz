"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 6
Realizar un programa que solicite tres valores de los lados de un posible triángulo e informe
si es un triángulo o no.

"""

def esTriangulo(lados): 
    mensaje = ""
    sumaLados=lado[0]+lado[1]
    if sumaLados<=lado[2]:
        mensaje = "Es un triángulo"    
    else:
        mensaje = "No es un triángulo"
    return mensaje

def pideLados(lados):
    lado1=int(input("Introduce el primer lado"))
    lado2=int(input("Introduce el segundo lado"))
    lado3=int(input("Introduce el tercer lado"))
    
    lados = [lado1, lado2, lado3]
    
    """
    meterlos en una lista tb podría hacerse (declaramos vacia y la definimos)
    lados= []
    lados.append(lado1)
    lados.append(lado2)
    lados.append(lado3)
    """
    
print(pideLados(lados)