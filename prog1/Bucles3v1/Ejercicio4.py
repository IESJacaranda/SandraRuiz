"""
Ejercicio 4
Design a method called dayOfWeek that receives three integer parameters: day, month and year. The method should 
return a number between 0 and 6 that is the day in the week for that date. 
You have to know the next algorithm:
       
       a = (14 - month) / 12 
       y = year – a 
       m = month + 12 * a – 2 
       d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
       
       If the variable d is zero was Sunday, 1 Monday……………... 6 Saturday. 
"""

def dayOfWeek(day,month,year):
    a = (14 - month) / 12 
    y = year - a 
    m = month + 12 * a - 2 
    d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7
    result=""
    if d==0:
        result="Sunday"
    elif d==1:
        result="Monday"
    elif d==2:
        result="Tuesday"
    elif d==3:
        result="Wednesday"        
    elif d==4:
        result="Thursday"
    elif d==5:
        result="Friday" 
    else:
        result="Saturday"   
            
    return result


assert(dayOfWeek(5,2,2014)==3)
assert(dayOfWeek(19,12,2020)==4)
assert(dayOfWeek(30,1,2020)==6)
assert(dayOfWeek(30,3,2020)==2)
assert(dayOfWeek(12,7,2021)==1)
assert(dayOfWeek(23,8,2020)==0)