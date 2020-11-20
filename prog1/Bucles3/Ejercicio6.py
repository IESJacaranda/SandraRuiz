"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 6
Realizar un programa que solicite tres valores de los lados de un posible triángulo e informe
si es un triángulo o no.

"""


def esTriangulo(): 
    lado1=int(input("Introduce el primer lado: "))
    while lado1<=0:
        lado1=int(input("Error. Introduce el primer lado: ")) 
    
    lado2=int(input("Introduce el segundo lado: "))
    while lado2<=0:
        lado2=int(input("Error. Introduce el segundo lado: ")) 
    
    lado3=int(input("Introduce el tercer lado: "))
    while lado3<=0:
        lado3=int(input("Error. Introduce el tercer lado: ")) 
    
    mensaje = ""
    if (lado1+lado2)>lado3:
        mensaje = "Es un triángulo"
        
    elif lado2+lado3>lado1:
        mensaje = "Es un triángulo"
    elif lado1+lado3>lado2:
        mensaje = "Es un triángulo"    
    else:
        mensaje = "No es un triángulo"
    
    print(mensaje)

esTriangulo()






"""
    meterlos en una lista tb podría hacerse (declaramos vacia y la definimos)
    lados= []
    lados.append(lado1)
    lados.append(lado2)
    lados.append(lado3)
"""
    
