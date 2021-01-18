'''
Author: Sandra Ruiz Jiménez

Ejercicio 1

Un anagrama es el procedimiento de crear una palabra a partir de otra reordenando 
las letras de la primera palabra, por lo tanto diremos que una palabra es un 
anagrama de otra si la primera palabra se puede formar a partir de las letras 
de la otra y no es la misma palabra.

Realizar una función que reciba como argumento dos palabras y devuelva verdadero 
si dichas palabras son anagramas y falso en caso contrario, por ejemplo “sergio” 
y “riesgo”

Realizar las llamadas necesarias para probar la función anterior de forma que 
se testee que funciona bien la función en todos los posibles casos.

** Considera sólo palabras cuyas letras tengan una sola ocurrencia.
'''

'''
Esta función calcula si una palabra es anagrama (siempre que las palabras 
tengan letras con una sola ocurrencia). Recibe dos palabras y devuelve
verdadero si son anagramas y falso si no lo son
'''
def esAnagrama(palabra1, palabra2):
    count=0
    for i in palabra1:
        for j in palabra2:
            if i==j:
                count+=1
        if count==len(palabra1) and count==len(palabra2):
            resultado=True
        else:
            resultado=False
    return resultado

assert(esAnagrama("sergio", "riesgo"))
assert(esAnagrama("cosa", "saco"))
assert(not esAnagrama("manuel", "piloto"))
assert(not esAnagrama("sergio", "riesgos"))

'''
Función principal que interactua con el usuario por consola (pide dos variables) y 
comprueba si las palabras son anagramas y devuelve un mensaje por pantalla
''' 
def main():
    palabraPrimera=input("Introduce una palabra: ")
    palabraSegunda=input("Introduce otra palabra: ")
    if esAnagrama(palabraPrimera,palabraSegunda)==True:
        print("Las palabras introducidas son anagramas")
    else:
        print("Las palabras introducidas no son anagramas")
        
main()
