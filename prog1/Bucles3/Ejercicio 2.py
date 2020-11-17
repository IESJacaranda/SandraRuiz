"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 2
Diseñar un programa que pida dos números, la base y la potencia, y muestre 
el resultado de elevar la base a la potencia sin usar el operador de potencia, 
es decir, sólo con multiplicaciones. Hay que tener en cuenta que la potencia 
puede ser negativa.
"""

def calculaPotencia(base, exponente):
    resultado=1
    if exponente>=0:
        for i in range (1,exponente+1):
            resultado*=base
        return resultado
    elif exponente<0:
        exponente=0-exponente
        for i in range (1,exponente+1):
            resultado*=base
        return 1/resultado

"""
base=int(input("De que numero quieres calcular la potencia? "))
exponente=int(input("A que numero quieres elevarlo? "))
"""

print(calculaPotencia(2, 2) == 4)
print(calculaPotencia(5, 8) == 390625)
print(calculaPotencia(2, -2) == 0.25)
print(calculaPotencia(-2, 5) == -32)