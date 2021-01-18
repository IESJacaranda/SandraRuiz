'''
Author: Sandra Ruiz Jiménez

Ejercicio 3

Realizar una función que dada una fecha en formato 12 horas nos devuelva la 
fecha en formato 24 horas.

La función recibirá una cadena con el siguiente formato hh:mm:ssAM u hh:mm:ssPM 
y deberá devolver el formato de fecho hh:mm:ss con 24 horas.

Si la fecha que recibe no tiene el formato adecuado deberá devolver una 
cadena vacía.

Ejemplos:

convierteFecha(“12:02:04AM”) → “”
convierteFecha(“12:02:04PM”) → “”
convierteFecha(“11:02:04AM”) → “11:02:04”
convierteFecha(“11:02:04PM”) → “23:02:04”
convierteFecha(“14:89:04AM”) → “”
convierteFecha(“12:02:04AP”) → “”
'''

def modificaCadena(cadena):
    for i in range(len(cadena)):
        if cadena[i]!=":" and cadena[i]!="A" and cadena[i]!="M" and cadena[i]!="P":
            cadenaMod=str(cadena[i])

    return cadenaMod
        
print(modificaCadena("12:02:04AM"))