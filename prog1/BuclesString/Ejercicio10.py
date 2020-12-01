'''
Ejercicio 10
Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3

'''

def wordNumber(frase):
    count=1
    for i in range (0, len(frase)):
        if frase[i]==" ":
            count+=1        
    return count
    
    

assert(wordNumber("He estudiado mucho")==3)
assert(wordNumber("Es una lata levantarse temprano")==5)