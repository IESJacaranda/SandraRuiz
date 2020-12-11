"""
Ejercicio 4
Design a method called dayOfWeek that receives three integer parameters: day, month and year. 
The method should return a number between 0 and 6 that is the day in the week for that date. 
You have to know the next algorithm:
       
       a = (14 - month) / 12
       y = year - a
       m = month + 12 * a – 2
       d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
       
       If the variable d is zero was Sunday, 1 Monday……………... 6 Saturday. 
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


def dayOfWeek(day,month,year):
    d=-1
    
    if month>=1 and month<=12 and day>0 and day <= daysInMonth(month,year):
        a = (14-month)//12
        y = year - a
        m = month + 12*a - 2
        d = (day + y + (y//4) - (y//100) + (y//400) + (31*m) // 12) % 7
# / es división float y // es división int (para que no de decimales)
    
    return d


dayNames=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#esta variable esta 

def gimmeADate():
    date=[]
    date.append(int(input("Gimme the day: ")))
    date.append(int(input("Gimme the month: ")))
    date.append(int(input("Gimme the year: ")))
    
    return date


def main():
    date = gimmeADate()
    d = dayOfWeek(date[0],date[1],date[2]) #como date es una lista, posicion0 es dia, posicion1 es mes y posicion2 es año
   
#Utilizamos el siguiente if porque para los valores de día y mes incorrectos, el resultado d
#es igual a -1 y el valor -1 de la lista es "Saturday".
    while d==-1: #para comprobar si la fecha es correcta. No sale del bucle hasta que la fecha sea correcta
        print("The date you entered is not right")
        date = gimmeADate()
    
    print("That day was: %s" % dayNames[d])

main()


def test():
    assert(dayOfWeek(5,2,2014)==3)
    assert(dayOfWeek(19,12,2020)==6)
    assert(dayOfWeek(11,13,2020)==-1)
    assert(dayOfWeek(0,12,2020)==-1)
    assert(dayOfWeek(10,-3,2020)==-1)
    assert(dayOfWeek(30,3,2020)==1)
    assert(dayOfWeek(16,7,2021)==5)
    assert(dayOfWeek(23,8,2020)==0)
    assert(dayOfWeek(29,2,2020)==6)
    assert(dayOfWeek(31,2,2020)==-1)
    
test()