"""
Ejercicio 1
Design a function called charactersInString that has a character string and a 
character as input parameters and returns how many times that character appears 
in the string. It should do if the string and character are lower case or upper 
case characters.


print("%s: is lower %s" % ("A", "A".islower())) #me da False
print("%s: is upper %s" % ("A", "A".isupper())) #me da True

print("%s: is lower %s" % ("a", "a".islower())) #me da True
print("%s: is lower %s" % ("a", "a".isupper())) #me da False

print("ABC".lower()) #imprime 'abc'
print("abc".upper()) #imprime 'ABC'
print("ABC"[2]) #imprime 'C'

"""


def charactersInString(cadena, caracter):
    count = 0
    
    for i in range (0, len(cadena)):
        if caracter.lower() == cadena[i].lower():
            count+=1
        #print(cadena[i])
        
    return count


#assert(charactersInString("Hola, ¿qué haces?", 'y')==0) #si son True, no devuelven nada
#assert(charactersInString("Hola, ¿qué haces?", 'a')==2)
assert(charactersInString("IES Jacaranda, de Brenes", 'e')==4)

"""
De momento esto da problemas con las tildes, por ejemplo, detecta como diferentes 
'é' y 'e'
"""


"""
Otra solución:
pero 'c' es de tipo cadena, igual que 'cadena' y tampoco podemos hacer cálculos que
tengan que ver con valores de lista (posiciones, etc.)


def charactersInString(cadena, caracter):
    count = 0
    
    for c in cadena:
        if caracter.lower() == cadena[i].lower():
            count+=1
        #print(c)
        
    return count

"""