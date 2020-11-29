'''
Ejercicio 9
Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio"

'''

def agrupaConsonantesyVocales (frase):
    fraseOrdConsonante = ""
    fraseOrdVocal= ""
    fraseMod = frase.replace(" ", "")
    for i in range (0, len(fraseMod)):
        if fraseMod[i]!="a" and fraseMod[i]!="e" and fraseMod[i]!="i" and fraseMod[i]!="o" and fraseMod[i]!="u":
            fraseOrdConsonante+=fraseMod[i]
        elif fraseMod[i]=="a" or fraseMod[i]=="e" or fraseMod[i]=="i" or fraseMod[i]=="o" or fraseMod[i]=="u":
            fraseOrdVocal+=fraseMod[i]     
            
    return fraseOrdConsonante+fraseOrdVocal
    
  

assert(agrupaConsonantesyVocales("curso de programacion")=="crsdprgrmcnuoeoaaio")
