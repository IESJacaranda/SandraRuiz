"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 4

Diseñar un programa que muestre un menú con las siguientes opciones:

1. Cambio de euros a dólares
2. Cambio de dólares a euros
3. Cambio de euros a libras
4. Cambio de libras a euros.
5. Cambio de libras a dólares
6. Cambio de dólares a libras
7. Salir

El programa debe pedir una opción, luego una cantidad según corresponda y 
mostrar la conversión correspondientes. 
El programa terminará cuando pulse un 7.

"""

print("1. Cambio de euros a dólares")
print("2. Cambio de dólares a euros")
print("3. Cambio de euros a libras")
print("4. Cambio de libras a euros")
print("5. Cambio de libras a dólares")
print("6. Cambio de dólares a libras")
print("7. Salir")
        

def conversorMoneda(moneda,amount):
    
    if moneda==1:
        total=amount*1.19
    elif moneda==2:
        total=amount*0.84
    elif moneda==3:
        total=amount*0.89
    elif moneda==4:
        total=amount*1.12
    elif moneda==5:
        total=amount*1.32
    elif moneda==6:
        total=amount*0.76
    
    return total

def menu():
    moneda=int(input("Que numero de opcion quiere realizar?"))
    while moneda>=1 and moneda<=6:
        amount=float(input("Cuanto quiere cambiar?"))
        print(conversorMoneda(moneda, amount))
        moneda=int(input("Que numero de opcion quiere realizar?"))
    if moneda==7:
        print("Gracias por usar el programa.")    
        
menu()

"""
Solución clase:

def mostrarMenu():
    mensaje ="1. Cambio de euros a dólares \n"
    mensaje+="2. Cambio de dólares a euros \n"
    mensaje+="3. Cambio de euros a libras \n"
    mensaje+="4. Cambio de libras a euros \n"
    mensaje+="5. Cambio de libras a dólares \n"
    mensaje+="6. Cambio de dólares a libras \n"
    mensaje+="7. Salir \n"
    print(mensaje)


def calcularCambio(modo, cantidadAConvertir):
    return ""
    
mostrarMenu()
opcion = input("Introduzca una opción: ")
while opcion!=str(7)
    cantidadAConvertir = float(input("Introduce la cantidad a cambiar: ")
    resultado = calcularCambio(modo, cantidadAConvertir)
    print("El cambio de dólares a ... es igual a %s" % resultado)
    print(mostrarMenu())
    opcion = input("Introduzca una opción: ")

"""