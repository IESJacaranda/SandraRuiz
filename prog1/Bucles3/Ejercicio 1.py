"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 1
Diseñar un programa que calcule el perímetro de una figura geométrica. 
Para ello debemos preguntar “¿Cuántos lados tiene la figura?”. 
Luego debemos pedir la longitud de cada uno de los lados y mostrar el perímetro. 
Se debe garantizar que los datos son correctos.
"""
#perímetro = suma lados

def pideLados():
    numLado=(int(input("Cuantos lados tiene la figura? ")))
    while numLado<3: 
        numLado=(int(input("Cuantos lados tiene la figura? ")))
    perimetro=0
    for i in range(1,numLado+1):
        longLado=(int(input("Cuanto mide el lado? ")))
        while longLado<=0:
            longLado=(int(input("No es correcto. Cuanto mide el lado? ")))
        perimetro+=longLado
        
        
    print(perimetro)
        
BUSCAR LOS POLÍGONOS IRREGULARES

pideLados()