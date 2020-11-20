"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 4

Diseñar un programa que muestre un menú con las siguientes opciones:

1. Cambio de euros a dólares.
2. Cambio de dólares a euros.
3. Cambio de euros a libras.
4. Cambio de libras a euros.
5. Cambio de libras a dólares.
6. Cambio de dólares a libras.
7. Salir.

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

CAMBIO_EURO_DOLAR = 0.84    #estas tres son constantes
CAMBIO_EURO_LIBRA = 0.89
CAMBIO_LIBRA_DOLAR = 0.75


def calcularCambio(opcion, cantidadAConvertir):
    if opcion==str(1): #euro a dolar
        cantidadConvertida=cantidadAConvertir/CAMBIO_EURO_DOLAR
    elif opcion==str(2): #dolar a euro
        cantidadConvertida=cantidadAConvertir*CAMBIO_EURO_DOLAR
    elif opcion==str(3): #euro a libra
        cantidadConvertida=cantidadAConvertir*CAMBIO_EURO_LIBRA
    elif opcion==str(4): #libra a euro
        cantidadConvertida=cantidadAConvertir/CAMBIO_EURO_LIBRA
    elif opcion==str(5): #libra a dolar
        cantidadConvertida=cantidadAConvertir/CAMBIO_LIBRA_DOLAR
    elif opcion==str(6): #dolar a libra
        cantidadConvertida=cantidadAConvertir*CAMBIO_LIBRA_DOLAR
    
    return round(cantidadConvertida, 3)
#la funcion round y luego el 3 indican el numero de decimales que quiero


#los modos de prueba:
print(calcularCambio(1, 1))
print(calcularCambio(2, 1))
print(calcularCambio(3, 1))
print(calcularCambio(4, 1))
print(calcularCambio(5, 1))
print(calcularCambio(6, 1))


        
def mostrarMenu():
    mensaje ="1. Cambio de euros a dólares \n"
    mensaje+="2. Cambio de dólares a euros \n"
    mensaje+="3. Cambio de euros a libras \n"
    mensaje+="4. Cambio de libras a euros \n"
    mensaje+="5. Cambio de libras a dólares \n"
    mensaje+="6. Cambio de dólares a libras \n"
    mensaje+="7. Salir \n"
    return mensaje


def programaPrincipal():
    print(mostrarMenu())
    opcion = input("Introduzca una opción: ")
    while opcion!=str(7)
        cantidadAConvertir = float(input("Introduce la cantidad a cambiar: ")
        resultado = calcularCambio(opcion, cantidadAConvertir)
        print("El cambio de dólares a ... es igual a %s" % resultado)
        print(mostrarMenu())
        opcion = input("Introduzca una opción: ")


Solución de Fran:

CAMBIO_EURO_DOLAR = 0.84    #estas tres son constantes
CAMBIO_EURO_LIBRA = 0.89
CAMBIO_LIBRA_DOLAR = 0.75

def convertirEuroaDolar(valor):
    return VALOR/cambio_EURO_DOLAR
    
def convertirDolaraEuro(valor):
    return VALOR*cambio_EURO_DOLAR

def convertirEuroaLibra(valor):
    return VALOR*cambio_EURO_LIBRA

def convertirLibraaEuro(valor):
    return VALOR/cambio_EURO_LIBRA

def convertirLibraaDolar(valor):
    return VALOR/cambio_LIBRA_DOLAR

def convertirDolaraLibra(valor):
    return VALOR*cambio_LIBRA_DOLAR
    
    
def calcularCambio(opcion, cantidadAConvertir):
    if opcion==str(1): #euro a dolar
        cantidadConvertida=convertirEuroaDolar/CAMBIO_EURO_DOLAR
    elif opcion==str(2): #dolar a euro
        cantidadConvertida=convertirDolaraEuro*CAMBIO_EURO_DOLAR
    elif opcion==str(3): #euro a libra
        cantidadConvertida=convertirEuroaLibra*CAMBIO_EURO_LIBRA
    elif opcion==str(4): #libra a euro
        cantidadConvertida=convertirLibraaEuro/CAMBIO_EURO_LIBRA
    elif opcion==str(5): #libra a dolar
        cantidadConvertida=convertirLibraaDolar/CAMBIO_LIBRA_DOLAR
    elif opcion==str(6): #dolar a libra
        cantidadConvertida=convertirDolaraLibra*CAMBIO_LIBRA_DOLAR
    
    return round(cantidadConvertida, 3)
    
#la funcion round y luego el 3 indican el numero de decimales que quiero


#los modos de prueba:
print(calcularCambio(1, 1))
print(calcularCambio(2, 1))
print(calcularCambio(3, 1))
print(calcularCambio(4, 1))
print(calcularCambio(5, 1))
print(calcularCambio(6, 1))


        
def mostrarMenu():
    mensaje ="1. Cambio de euros a dólares \n"
    mensaje+="2. Cambio de dólares a euros \n"
    mensaje+="3. Cambio de euros a libras \n"
    mensaje+="4. Cambio de libras a euros \n"
    mensaje+="5. Cambio de libras a dólares \n"
    mensaje+="6. Cambio de dólares a libras \n"
    mensaje+="7. Salir \n"
    return mensaje


def programaPrincipal():
    print(mostrarMenu())
    opcion = input("Introduzca una opción: ")
    while opcion!=str(7)
        cantidadAConvertir = float(input("Introduce la cantidad a cambiar: ")
        resultado = calcularCambio(opcion, cantidadAConvertir)
        print("El cambio de dólares a ... es igual a %s" % resultado)
        print(mostrarMenu())
        opcion = input("Introduzca una opción: ")
        
"""