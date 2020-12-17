'''
Ejercicio 2:
Realiza un programa que lea 10 números, debe imprimir los 10 número y después 
desplazarlos una posición, de tal forma que el último pase a la primera posición, 
el primero a la segunda, el segundo a la tercera, y así sucesivamente.
'''

def leerNumeros(lista):
    listaMod=[]
    listaMod.append(lista[-1])
    for i in range (len(lista)-1):
        listaMod.append(lista[i])
        
    return listaMod

assert(leerNumeros([1,2,3,4,5,6,7,8,9,10])==[10,1,2,3,4,5,6,7,8,9])
    
