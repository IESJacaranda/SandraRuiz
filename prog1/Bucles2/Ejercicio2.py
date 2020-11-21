"""
Ejercicio 2
Design a program for reading an integer between 0 and 10 and show the times table. 
To ask for the number you should show the next message "Enter one number between 0 and 10”. 
If the number is out of the boundaries, the program should show the message “The number is out of the boundaries”. 
If the number is valid, it should show the times table following the next format:
7*0=0
7*1=7 …..
7*10=70
"""

#Solución con bucle for:

numero = int(input("Introduce un numero comprendido entre 0 y 10:"))
if numero>0 and numero<10:
    for i in range(0,11):
        print(str(numero)+"*"+str(i)+"="+str(numero*i))
else:
    print("El numero introducido no esta comprendido entre 0 y 10")

"""
Solución con bucle for y bucle while:

import time
while True:
    numero = int(input("Introduce un numero comprendido entre 0 y 10:"))
    if numero>0 and numero<10:
        for i in range(0,11):
            print(str(numero)+"*"+str(i)+"="+str(numero*i))
    else:
        print("El numero introducido no esta comprendido entre 0 y 10")
    time.sleep(2)

"""