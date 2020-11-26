'''
Ejercicio 7
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera.
'''

def wordHidden(cadena, cadena2, cadena3):
    resultado=True
    for i in range (0,len(cadena)):
        for j in range (0,len(cadena2)):
            if cadena[i]==cadena2[j]:
                resultado==True
                for k in range (0,len(cadena3)):
                    cadena2[j]==cadena3[k]

    return cadena3

assert(wordHidden("shybaoxlna", "hola", "mazo")=="mazo")
