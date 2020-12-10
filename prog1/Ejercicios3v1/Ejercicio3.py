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


def daysInMonth(month,year):
    days=-1
    daysPerMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    
    if (month>0 and month<13) and year>=0:
        if (leapYear(year)==True and month==2):
            days = 29
        else:
            days = daysPerMonth[month-1] #me dan mes 1 (enero, así que 1-1=0, posición 0 son los dias de enero
                
    return days


        
assert(daysInMonth(2,2000)==29)
assert(daysInMonth(2,1999)==28)
assert(daysInMonth(-3,2100)==-1)
assert(daysInMonth(1,1992)==31)
assert(daysInMonth(4,1986)==30)
assert(daysInMonth(4,-5)==-1)