"""
Ejercicio 1
Design a program to show all numbers between 1 and 100. If the number is a multiple of 7 you should show the message 
"The number xx is a multiple of 7". 
If the number is a multiple of 13 you should show the message "The number xx is a multiple of 13". 
If the number is a multiple of 7 and 13 you should show both messages.


"""

# Solución 1 con bucle for sin variables:

for i in range(1,101):
    if i%7==0 and i%13==0 :
        print(str(i)+" es multiplo de 7 y de 13")
    elif i%7==0:
        print(str(i)+" es multiplo de 7")
    elif i%13==0:
        print(str(i)+" es multiplo de 13")
    else:
        print(i)
        
"""
#Solución 2 con bucle for y variables:


for i in range(1,101):
    multiplo7 = i%7==0
    multiplo13 = i%13==0
    if multiplo7 and multiplo13:
        print(str(i)+" es multiplo de 7 y de 13")
    elif multiplo7:
        print(str(i)+" es multiplo de 7")
    elif multiplo13:
        print(str(i)+" es multiplo de 13")
    else:
        print(i)




#Solución con bucle while y función def:

def esMultiplo7(numero):
    return numero%7==0
def esMultiplo13(numero):
    return numero%13==0
while True:
    numero = int(input("Dame un numero:"))
    if esMultiplo13(numero):
        print("Es multiplo de 13")
    if esMultiplo7(numero):
        print("Es multiplo de 7")

"""