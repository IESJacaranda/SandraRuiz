'''
Ejercicio 5

Realizar un función que reciba una lista y devuelva una nueva lista cuyo contenido sea igual a la original 
pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver 
[‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]. 
Llamar a dicha función
'''

def main(lista):
    listaInversa= []
    for i in lista:
        listaInversa = [i] + listaInversa
    
    return listaInversa


assert(main(['Di', 'buen', 'día', 'a', 'papa'])==['papa', 'a', 'día', 'buen', 'Di'])