"""
Ejercicio 2
Design a method called leapYear that returns 1 if the number that receives the method is a leap year. 
In other case, the method returns -1. A year is a leap year if it is multiple of 4 but the year is not 
multiple of 100 and not multiple of 400.

"""

def leapYear(year):
    mensaje = ""

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        mensaje="Es bisiesto"
    else:
        mensaje=-1
    
    print(mensaje)    
    
    #return mensaje


year=int(input("Dime un año: "))
while year<=0:
    year=int(input("Error. Dime un año"))
        
#assert(leapYear(2000)=="Es bisiesto")
#assert(leapYear(2100)==-1)
#assert(leapYear(1992)=="Es bisiesto")

leapYear(year)
