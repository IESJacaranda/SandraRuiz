'''
Ejercicio 8
Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
'''

def cuentaVocales(cadenaEntrada):
    aparicionA=0
    aparicionE=0
    aparicionI=0
    aparicionO=0
    aparicionU=0
    
    for i in range(0,len(cadenaEntrada)):
        if cadenaEntrada[i].lower()=="a":
            aparicionA=1
        elif cadenaEntrada[i].lower()=="e":
            aparicionE=1
        elif cadenaEntrada[i].lower()=="i":
            aparicionI=1
        elif cadenaEntrada[i].lower()=="o":
            aparicionO=1
        elif cadenaEntrada[i].lower()=="u":
            aparicionU=1
            
    return aparicionA+aparicionE+aparicionI+aparicionO+aparicionU
    
assert(cuentaVocales("Aeiou aeiou")==5)
assert(cuentaVocales("aeio aeio")==4)
assert(cuentaVocales("pqrst xyz")==0)
assert(cuentaVocales("Buenos dias")==5)
