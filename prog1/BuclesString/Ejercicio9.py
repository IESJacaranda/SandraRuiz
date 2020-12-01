'''
Ejercicio 9
Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio"

'''

def agrupaConsonantesyVocales(frase):
    fraseOrdConsonante = ""
    fraseOrdVocal= ""
    for i in range (0, len(frase)):
        if frase[i]!=" " and (frase[i]!="a" and frase[i]!="e" and frase[i]!="i" and frase[i]!="o" and frase[i]!="u"):
            fraseOrdConsonante+=frase[i]
        elif frase[i]!=" " and (frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u"):
            fraseOrdVocal+=frase[i]     
                   
    return fraseOrdConsonante+fraseOrdVocal
    
  

assert(agrupaConsonantesyVocales("curso de programacion")=="crsdprgrmcnuoeoaaio")
