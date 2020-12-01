'''
Ejercicio 7
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla 
por la tercera.
'''

def buscarYReemplazar(frase, palabra, reemplazo):
    if len(palabra)>len(frase):
        return frase

    cadenaFinal = ""
    indicadorPosicionFrase = 0
    
    while indicadorPosicionFrase < len(frase): #itera sobre frase 
        coincidencia = True
        indicadorPalabra= 0
        while coincidencia and indicadorPalabra < len(palabra): #Búsqueda
            if not palabra[indicadorPalabra]==frase[indicadorPosicionFrase+indicadorPalabra]:
                coincidencia = False
            indicadorPalabra+=1
        
        #Concatenacion o reemplazo
        if not coincidencia: #concatenación
            cadenaFinal+=frase[indicadorPosicionFrase] #añade a cadena Final sin modificar la variable frase    
            indicadorPosicionFrase+=1
        else: # si hay coincidencia salta aquí: Reemplazo
            for i in reemplazo:
                cadenaFinal+=i
            indicadorPosicionFrase+=len(palabra)

    return cadenaFinal




fraseEjemplo = "La lluvia en Sevilla es una maravilla, porque en Sevilla hace mucho calor"

assert(buscarYReemplazar(fraseEjemplo, "Sevilla", "Córdoba")=="La lluvia en Córdoba es una maravilla, porque en Córdoba hace mucho calor")



