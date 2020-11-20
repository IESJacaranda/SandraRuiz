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

def calculaPerimetro(listaLados):
    perimetro=0
    for i in range(listaLados):
        longLado=(int(input("Cuanto mide el lado? ")))
        while longLado<=0:
            longLado=(int(input("No es correcto. Cuanto mide el lado? ")))
        perimetro+=longLado
    
    return perimetro

def compruebaFigura(listaLados):
    while numLado<3: 
        list.append(numLado)
    
        
def pideLados():
    listaLados= []

    
    
    print("El perímetro es %s" % (calculaPerimetro(listaLados)))


numLado=(int(input("Cuantos lados tiene la figura? ")))
            
pideLados()