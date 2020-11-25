'''
Ejercicio 2
Design a function called lowCaseInString that has a string of characters as parameter, 
the method should return how many of those characters are lowcase letters.
'''

def lowCaseInString (cadena):
    count=0
    
    for i in range (0, len(cadena)):
        if cadena[i].islower():
            count+=1
            #print(cadena[i])
    return count

assert(lowCaseInString("Brenes!")==5) #si son True, no devuelven nada
#assert(lowCaseInString("Hola")==3)
#assert(lowCaseInString("Jacaranda")==8)

'''
Solucion clase

def lowCaseInString (cadenaCaracteres):
    lowCaseCount=0
    
    for c in cadenaCaracteres:
        if c.islower():
            lowCaseCount+=1
            
    return lowCaseCount

assert(lowCaseInString("Brenes!")==5) #si son True, no devuelven nada
assert(lowCaseInString("Hola")==3)
assert(lowCaseInString("Jacaranda")==8)
'''
