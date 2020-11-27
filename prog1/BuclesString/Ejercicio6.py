'''
Ejercicio 6
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.
'''

def hiddenWord(frase, palabra):
    resultado = False
    
    iPalabra = 0
    for iFrase in range (0,len(frase)):
        if iPalabra<len(palabra) and frase[iFrase]==palabra[iPalabra]:
            iPalabra+=1
            
    return iPalabra==len(palabra)


assert(hiddenWord("shybaoxlna", "hola")==True)
assert(hiddenWord("shybaoxlnabc", "hola")==True)
assert(hiddenWord("hipopotamo", "tamo")==True)
assert(hiddenWord("shybaoxlna", "pretzel")==False)

'''
Solucion 2

def hiddenWord(frase, palabra):
    resultado = False
    
    iPalabra = 0
    iFrase = 0
    
    while iFrase < len(frase):
        if iPalabra<len(palabra) and frase[iFrase]==palabra[iPalabra]:
            iPalabra+=1
        iFrase+=1
        
    return iPalabra==len(palabra)


assert(hiddenWord("shybaoxlna", "hola")==True)
assert(hiddenWord("shybaoxlnabc", "hola")==True)
assert(hiddenWord("hipopotamo", "tamo")==True)
assert(hiddenWord("shybaoxlna", "pretzel")==False)


#Si pongo un:

    resultado = (iPalabra==len(palabra))
    return resultado

Usando el modo debug puedo ver directamente el valor, en este caso boolean, que tiene
la variable resultado.
Una vez que compruebo que el algoritmo funciona correctamente, entonces modifico para
no utilizar la variable resultado solo una vez y pongo:
    
    return iPalabra==len(palabra)
'''