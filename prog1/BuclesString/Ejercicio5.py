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


def isPalindrome(cadena):
    cadena = cadena.lower()
    inversa= ""

    for i in range (0,len(cadena)):
        if cadena[i]==" ":
            cadena[i]==""
        inversa = cadena[i] + inversa
        
    return inversa == cadena        

'''
Hasta ahora hemos visto siempre cadena+=reverso, pero esto nos ordenaría la lista en orden.
Para que almacene los valores al principio en vez de al final, le cambiamos el orden cadena[i]+reverso
'''

assert(isPalindrome("amana")==False)
assert(isPalindrome("amolapaloma")==True)
assert(isPalindrome("Manuel no te arrimes a la pared")==False)

'''
Otra solucion 1:


def isPalindrome(cadena):
    inversa= ""
    
    for c in cadena:
        inversa= cadena[i]+ inversa 
    
    #print(inversa)
        
    return inversa==cadena
    


Otra solución 2:


def isPalindrome(cadena):
    
    esPalindroma= True
    
    for i in range(0,len(cadena)//2):
        if cadena[i]!=cadena[len(cadena)-1-i]:
            esPalindroma = False
    return esPalindroma
    
    
    
Otra solución 3:
#la siguiente función nos valdría para enteros, cadenas y float

def isPalindrome(cadena):

    esPalindroma= True
    cadena= str(cadena) #para convertir números enteros a cadena
    
    for i in range(0,int(len(cadena)//2)):
        sonIguales = (cadena[i]==cadena[len(cadena)-1-i])
        
        if not sonIguales:
            esPalindroma = False
            
    return esPalindroma    


print(isPalindrome2(33388333), type(33388333))   
print(isPalindrome2("33388333"), type("33388333"))
print(isPalindrome2(3338.8333), type(3338.8333))


numeros= "12345678"
length= len(numeros)
print(numeros[length-1])


listaElementos = ["Joseba", "Rafael", "Jose Vicente", "Adela"]

print(len(listaElementos))
print(listaElementos[len(listaElementos)-1])
'''
