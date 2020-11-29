'''
Ejercicio 7
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla 
por la tercera.
'''

def buscarYReemplazar(frase, palabra, reemplazo):
    if len(palabra)>len(frase):
        return frase
    fraseMod = ""
    iFrase = 0
    
    for i in range (0, len(frase):
        if frase[i]==palabra[i]:
            if palabra[i] == reemplazo[i]:
                iReemplazo+=fraseMod.replace(palabra[i], reemplazo[i])
        iFrase+=1
        print(fraseModificada)
    return fraseModificada
    

"""    
    while para recorrer la fraseEjemplo.
    En cuanto tenga un match entre primer elemento palabra y primer elemento de frase, voy a comprobar los demas elementos.
    si coinciden utilizo la sustitucion. Para eso uso variable auxiliar que es el mensaje de salida.
    Si veo que no coincide 
        
        utilizaría mas de while
        print()

            
           
    return "" 
"""

frase = "La lluvia en Sevilla es una maravilla, porque en Sevilla hace mucho calor"

assert(buscarYReemplazar(frase, "Sevilla", "Córdoba")=="La lluvia en Córdoba es una maravilla, porque en Córdoba hace mucho calor")
