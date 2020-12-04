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


def esUnPoligono(lado):
    esPoligono = True
    
    for i in range(0,len(lado)):   #validacion de si lados son positivos
        if(lado[i]>=0):
            esPoligono = False
 
 
    for i in range(0, len(lado)): #validacion de si es un polígono
        sumaLados=0
        for j in range (0, len(lado)):
            if (j!=i): #esto sirve para que no me sume los lados
                sumaLados+=lado[j]
        if sumaLados <= lado[i]:
            esPoligono = False
                
   
    return esPoligono
    
    
    

print(esUnPoligono([0, 1, 3, 5]))
print(esUnPoligono([1, -1, 3]))
print(esUnPoligono([10, 10, 10, 10]))



"""

Otra solución: esta es más óptima


def esUnPoligono(lado):;
    esPoligono = True
    
    for i in range(0,len(lado)):   #validacion de si es positivo
        if(lado[i]>=0):
            esPoligono = False
    
    
    ladoMayor=lado[0]    #estima limite superior y luego compara con suma de todos
    sumaTotalLados = 0
    for i in range (0,len(lado)):
        if lado[i]>ladoMayor:
            ladoMayor = lado[i]
        sumaTotalLados+=lado[i]
    
    
    return ladoMayor < (sumaTotalLados-ladoMayor)
    
    
    
print(esUnPoligono([0, 1, 3, 5]))
print(esUnPoligono([1, -1, 3]))
print(esUnPoligono([10, 10, 10, 10]))

"""