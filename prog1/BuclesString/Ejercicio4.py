'''
Ejercicio 4
Design a function called numberInString that has a string of characters as parameter, 
the method should return how many of those characters are numbers.
'''

def numberInString(cadena):
    count=0
    for i in range(len(cadena)):
        if cadena[i].isnumeric():
            count+=1
    return count


assert(numberInString("Los 4440")==4) #si son True, no devuelven nada
assert(numberInString("Hola")==0)
assert(numberInString("El numero 1 de la lista de los 40 Principales")==3)

'''
Solucion clase:

def numberInString(cadena):
    numberCount=0
    for c in range cadena:
        if c.isnumeric():
            numberCount+=1
    return numberCount


assert(numberInString("Los 4440")==4) #si son True, no devuelven nada
assert(numberInString("Hola")==0)
assert(numberInString("El numero 1 de la lista de los 40 Principales")==3)
