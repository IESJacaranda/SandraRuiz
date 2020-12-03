"""
Examen 2 Diciembre - Ejercicio 1

1. La primitiva es un tipo de sorteo bisemanal en el que se puede elegir 
combinaciones de 6 números del 1 al 49. Un boleto resulta ganador si esos 6 números 
coinciden con la combinación extraída al azar de un bombo con todas las bolas. 
También existen premios menores a partir de los 3 aciertos.
Diseña una función que reciba como entrada dos listas de números que hagan 
referencia a la combinación ganadora y a la apuesta y devuelva como resultado el 
número de aciertos que tiene la apuesta. 

Adjunta también una captura de pantalla del valor en el IDE de las variables 
hacia la mitad de la ejecución.

2. Realiza un programa que solicite la apuesta de la primitiva y usando la función 
anterior escriba un mensaje con el número de aciertos. Si ha adivinado los 6 números 
deberá escribir. “ENHORABUENA. TIENES EL PLENO”. Valida los datos  de la apuesta de 
forma adecuada.

Si sabes, debes generar de forma aleatoria la combinación ganadora, si no sabes, 
utiliza la combinación ganadora que quieras.

"""


def primitiva(listaGanadora,listaApuesta):
    numAciertos=0
    for i in range (0, len(listaGanadora)):
        for j in range (0, len(listaApuesta)):
            if listaGanadora[i]==listaApuesta[j]:
                numAciertos+=1
    return numAciertos

listaGanadora=[6,8,15,31,38,49]
assert(primitiva(listaGanadora, listaApuesta=[6,9,14,30,37,49])==2)
assert(primitiva(listaGanadora, listaApuesta=[5,7,13,25,28,40])==0)
assert(primitiva(listaGanadora, listaApuesta=[6,8,15,31,38,49])==6)
assert(primitiva(listaGanadora, listaApuesta=[6,8,15,30,38,47])==4)
assert(primitiva(listaGanadora, listaApuesta=[8,9,15,31,38,6])==5)


def acertantePrimitiva(Apuesta):
    if primitiva==6:
        return("ENHORABUENA. TIENES EL PLENO")       
    elif primitiva<=5:    
        return "Su numero de aciertos es %s" % primitiva(listaGanadora,listaApuesta)


assert(acertantePrimitiva([6,9,14,30,37,49])==2)
assert(acertantePrimitiva([5,7,13,25,28,40])==0)
assert(acertantePrimitiva([6,8,15,31,38,49])==6)
assert(acertantePrimitiva([6,8,15,30,38,47])==4)
assert(acertantePrimitiva([8,9,15,31,38,6])==5)



"""
Corrección:

def calculaAciertos(ganadora, apuesta):
    numeroAciertos = 0
    if len(ganadora)==6 and len(apuesta)==6
        #Comprueba combinaciones
        for i in ganadora:
            for j in apuesta:
                if i==j:
                    numeroAciertos+=1
                    
    return numeroAciertos
    

assert(calculaAciertos([], [])==0)
assert(calculaAciertos([1,2,3,4,5,6], [2,15])==0)
assert(calculaAciertos([1,2,3,4,5,6], [2,23,5,15,40])==1)
assert(calculaAciertos([1,2,3,4,5,6], [1,2,3,4,5,6])==6)




combinacionGanadora = [1,3,29,45,6,49]

def compruebaApuesta(ganadora):
    mensaje = ""
    pleno = "ENHORABUENA. TIENES EL PLENO"
    
    apuesta = []
    
    for i in range(6):
        numero=int(input("Introduce un numero de la apuesta: ")
        while (numero > 50 or numero < 1 or numero in apuesta):
            numero=int(input("Error. Introduce un numero de la apuesta: ")
        
        apuesta.append(numero)
    
    numeroAciertos = calculaAciertos(ganadora,apuesta)
    
    if numeroAciertos==6:
        mensaje = pleno
    elif numeroAciertos>=3:
        mensaje = "Tienes %s aciertos" % numeroAciertos
    else:
        mensaje = "Otra vez sera"
        
    return mensaje

print(compruebaApuesta(ganadora))
            
"""
"""
Solución parte 2 ejercicio con random:

import random

def generaCombinacionGanadora():
    combinacionGanadora = []
    i=0
    while i<6:
        numero=random.randint(1,49)
        if numero not in combinacionGanadora:
        combinacionGanadora.append(numero)
        i+=1
    return combinacionGanadora


def compruebaApuesta(ganadora):
    mensaje = ""
    apuesta = []
    
    for i in range(6):
        numero=int(input("Introduce un numero de la apuesta: ")
        while (numero > 50 or numero < 1 or numero in apuesta):
            numero=int(input("Error. Introduce un numero de la apuesta: ")
        
        apuesta.append(numero)
    
    numeroAciertos = calculaAciertos(ganadora,apuesta)
    
    if numeroAciertos==6:
        mensaje = "ENHORABUENA. TIENES EL PLENO"
    elif numeroAciertos>=3:
        mensaje = "Tienes %s aciertos" % numeroAciertos
    else:
        mensaje = "Otra vez sera"
        
    return mensaje

print(compruebaApuesta(generaCombinacionGanadora()))
            
"""