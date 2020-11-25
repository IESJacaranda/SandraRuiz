'''
Ejercicio 5

Design a function called palindrome that has a string of characters as parameter, 
and return true if it is a palindrome or false in other case. 
A word is a palindrome, if it is reads the same from left to right as from right 
to left, ignoring whites. For example: "anilina" or "el abad le dio arroz al zorro". 
To simplify the problem, you can assume that simple characters are used, that is, 
without tildes or dieresis.
'''
'''
cadena = "Esta variable contiene una cadena de texto"
print("%s %s" %(type(cadena), cadena)) #me imprime la cadena

cadena = cadena.islower()
print("{} {}".format(type(cadena), cadena)) #me imprime un Boolean, en este caso False

cadena = cadena.lower()
print("{} {}".format(type(cadena), cadena)) #me imprime la cadena en minúscula

Los prints: dos formas de escribirlos
print("%s %s" %(type(cadena), cadena)) #me imprime la cadena
print("{} {}".format(type(cadena), cadena))
'''


def palindrome(cadena):
    cadena = cadena.lower()
    reverso=-1
    for i in range (0,len(cadena)):
        if cadena[i] != cadena[reverso]:
            palindrome == False
            reverso-=1
    return reverso        


assert(palindrome("Amar da drama")==True)
assert(palindrome("Amigo, no gima")==True)
assert(palindrome("A mi loca Colima")==True)
assert(palindrome("Manuel no te arrimes a la pared")==False)