"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 7
Escriba una función que reciba un entero y devuelva si representa un año bisiesto o no,
según la regla, “Un año es bisiesto si es divisible por 400, o bien si es divisible por 4 pero no
por 100”.
Por ejemplo, el año 2000 es bisiesto (es divisible por 400), el año 1992 es bisiesto
(es divisible por 4 y no por 100), y el año 2100 no es bisiesto (es divisible por 4 y también
por 100 y no por 400).

"""


def esBisiesto():
    mensaje = ""
    year=int(input("Dime un año: "))
    while year<=0:
        year=int(input("Error. Dime un año"))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        mensaje="Es bisiesto"
    else:
        mensaje="No es bisiesto"
        
    print(mensaje)
    
        
#assert(esBisiesto(2000)=="Es bisiesto")
#assert(esBisiesto(2100)=="No es bisiesto")
#assert(esBisiesto(1992)=="Es bisiesto")

esBisiesto()
