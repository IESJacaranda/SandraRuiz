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
    iPalabra = 0
    iReemplazo= 0
    
    while iPalabra<len(palabra) and frase[iFrase]==palabra[iPalabra]:
        fraseMod=frase.replace(palabra, reemplazo)
    return fraseMod    



frase = "La lluvia en Sevilla es una maravilla, porque en Sevilla hace mucho calor"

assert(buscarYReemplazar(frase, "Sevilla", "Córdoba")=="La lluvia en Córdoba es una maravilla, porque en Córdoba hace mucho calor")
