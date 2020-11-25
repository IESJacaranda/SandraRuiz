'''
Ejercicio 3
Design a function called upperCaseInString that has a string of characters as 
parameter, the method should return how many of those characters are upper 
case letters.
'''

def upperCaseInString (cadena):
    count=0
    
    for i in range (0, len(cadena)):
        if cadena[i].isupper():
            count+=1
            #print(cadena[i])
    return count

#assert(upperCaseInString("Hola. Que tal?")==2) #si son True, no devuelven nada
#assert(upperCaseInString("Hola")==1)
assert(upperCaseInString("IES Jacaranda de Brenes")==5)


'''
Solucion clase


def upperCaseInString (cadenaCaracteres):
    upperCaseCount=0
    
    for c in cadenaCaracteres:
        if c.isupper():
            upperCaseCount+=1
            
    return upperCaseCount

assert(upperCaseInString("Hola. Que tal?")==2) #si son True, no devuelven nada
assert(upperCaseInString("Hola")==1)
assert(upperCaseInString("IES Jacaranda de Brenes")==5)

'''