"""
Ejercicio 12
Crea un programa que tras introducir una fecha en formato DD-MM-YYYY indique si la fecha es correcta (ten en cuenta que pueden existir años bisiestos).

"""

day = int(input("Introduce un día del mes en formato numérico (DD):"))
month = int(input("Introduce un mes del año en formato numérico (MM):"))
year = int(input("Introduce un año en formato numérico (AAAA):"))
if month >= 1 and month <= 12:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day >= 1 and day <= 31:
            print("La fecha es correcta")
        else:
            print("La fecha no es correcta")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day >= 1 and day <= 30:
            print("La fecha es correcta")
        else:
            print("La fecha no es correcta")
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day >= 1 and day <= 29:
                print("La fecha es correcta")
        elif day >= 1 and day <= 28:
            print("La fecha es correcta")
        else:
            print("La fecha no es correcta")
else:
    print("La fecha no es correcta")