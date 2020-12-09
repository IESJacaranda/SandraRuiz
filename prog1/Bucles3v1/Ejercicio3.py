"""
Ejercicio 3
Design a method called daysInMonth that returns the integer number of days in the month and year that 
received as arguments. You can use the method leapYear. If the arguments are not valid the method should 
return -1
"""




def leapYear(year):
    mensaje = True
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        mensaje=True
    else:
        mensaje=False  
    
    return mensaje


def daysInMonth(month, year):

    while month<1 and month<12:
        days=-1
    if month==4 or month==6 or month==9 or month==11:
        days=30
    elif month==2:
        if leapYear(year)==True:
            days=29
        else:
            days=28
    else:
        days=31
        
    return days


        
assert(daysInMonth(2,2000)==29)
assert(daysInMonth(2,1999)==28)
assert(daysInMonth(3,2100)==31)
assert(daysInMonth(1,1992)==31)
assert(daysInMonth(4,1986)==30)
