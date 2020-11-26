'''
Ejercicio 6
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.
'''

def hiddenWord(cadena, cadena2):
    resultado=True
    for i in range (0,len(cadena)):
        for j in range (0,len(cadena2)):
            if cadena[i]==cadena2[j]:
                resultado==True
    
    return resultado

assert(hiddenWord("shybaoxlna", "hola")==True)
assert(hiddenWord("hipopotamo", "toma")==True)
assert(hiddenWord("shybaoxlna", "pretzel")==False)
