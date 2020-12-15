"""
Ejercicio 8
Design a method called secondOrder that receives three integer positive number as parameters. 
This parameters are the coefficients of a second order equation (ax2+bx+c=0) and your code 
should return the solutions to this equation. If the parameters are not valid the method 
should return -1
"""
from math import sqrt #importar la funcion de la raiz cuadrada

def secondOrder(a,b,c):
    resultado=-1
    if a!=0:
        x1 = (-b + sqrt(b**2-(4*a*c)) ) / (2*a)
        x2 = (-b - sqrt(b**2-(4*a*c)) ) / (2*a)
        
        resultado = x1, x2
            
    return resultado

assert(secondOrder(-1,7,-10)==2, 5)
assert(secondOrder(0,7,-10)==-1)
assert(secondOrder(1,-2,1)==1/2, 1/3)