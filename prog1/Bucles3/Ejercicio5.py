"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 5
Realizar un programa que solicite la coordenada x e y de un punto e informe si se encuentre
en el primer, segundo, tercer o cuarto cuadrante.

"""

def calculaCoordenada ():
    x=1
    while x!=0:
        x=int(input("Dime la coordenada x: "))
        y=int(input("Dime la coordenada y: "))
        if x>0:
            if y>0:
                print("El punto se encuentra en el segundo cuadrante.")
            elif y<0:
                print("El punto se encuentra en el cuarto cuadrante.")
            else:
                print("Error, el punto no se encuentra en ningún cuadrante.")
        elif x<0:
            if y>0:
                print("El punto se encuentra en el primer cuadrante.")
            elif y<0:
                print("El punto se encuentra en el tercer cuadrante.")
            else:
                print("Error, el punto no se encuentra en ningún cuadrante.")
        else:
            print("Error, el punto no se encuentra en ningún cuadrante.")
        
calculaCoordenada()