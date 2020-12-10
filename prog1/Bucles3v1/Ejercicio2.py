"""
Ejercicio 2
Design a method called leapYear that returns 1 if the number that receives the method is a leap year. 
In other case, the method returns -1. A year is a leap year if it is multiple of 4 but the year is not 
multiple of 100 or multiple of 400.

"""

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return -1
    
    

#year=int(input("Dime un año: "))
#while year<=0:
#    year=int(input("Error. Dime un año"))
        
assert(leapYear(2000)==1)
assert(leapYear(2100)==-1)
assert(leapYear(1992)==1)

'''
Solución clase:

def leapYear(year):
    multiplo4 = (year%4==0) #variable de tipo boolean pq guarda el resultado de una comparacion
    multiplo100 = (year%100==0) #variable de tipo boolean pq guarda el resultado de una comparacion
    multiplo400 = (year%400==0) #variable de tipo boolean pq guarda el resultado de una comparacion
    
    if multiplo4 and (not multiplo100 or multiplo400):
        return 1
    else:
        return -1
        
assert(leapYear(2000)==1)
assert(leapYear(2100)==-1)
assert(leapYear(1992)==1)

En este caso tendría que haber 8 casos de prueba:
- 1 para la condición return 1
- 1 para la condición return -1
- 2 para el boolean multiplo4 (uno para el True y otro para el False)
- 2 para el boolean multiplo100 (uno para el True y otro para el False) 
- 2 para el boolean multiplo400 (uno para el True y otro para el False)
'''    