"""
Ejercicio 8
Design a method called secondOrder that receives three integer positive number as parameters. 
This parameters are the coefficients of a second order equation (ax2+bx+c=0) and your code 
should return the solutions to this equation. If the parameters are not valid the method 
should return -1
"""

import math

def secondOrder(a,b,c):
    soluciones = []
    
    radical = b**2 - 4*a*c
    
    if radical >=0 and a>0: #de esta manera evitamos las soluciones con numeros complejos
        x1 = -b + math.sqrt(radical) / 2*a
        x1 = -b - math.sqrt(radical) / 2*a
        
        if radical==0:
            soluciones.append(sol1)
        else:
            soluciones.append(sol1)
            soluciones.append(sol2)

            
    return soluciones

#casos de prueba no sirven
assert(secondOrder(-1,7,-10)==[2,5])
assert(secondOrder(0,7,-10)==[-1])
assert(secondOrder(1,-2,1)==1/2, 1/3)


'''
Solución anterior simplificada:

def secondOrder(a,b,c):
    soluciones = []
    
    radical = b**2 - 4*a*c
    
    if radical==0:
        soluciones.append(-b + math.sqrt(radical) / 2*a)
    else:
        soluciones.append(-b + math.sqrt(radical) / 2*a)
        soluciones.append(-b - math.sqrt(radical) / 2*a)

            
    return soluciones
