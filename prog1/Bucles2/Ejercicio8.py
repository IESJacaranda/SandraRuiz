"""
Ejercicio 8
Design a program that asks for a set of numbers. After inputting each number, the program should ask “Do you want to enter 
more numbers (Y/N)?”. If the answer is “Y” the program asks for other numbers. When the user finishes to enter all the numbers, 
the program should say which one is the smallest. The messages are the following:
“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
"""

#Solución 1:

def pideNumeros():
    num = int(input("Enter one number: "))
    listaNumeros =[] #declara lista vacía
    listaNumeros.append(num) #mete elemento al final de la lista
    while "Y"==input("Do you want to enter more number (Y/N)?"): #condicion de entrada
        num = int(input("Enter one number: "))
        listaNumeros.append(num)
        
    print(obtenerElMenorElemento(listaNumeros))



#Esta función devuelve el elemento menor de una lista numérica

def obtenerElMenorElemento(numbers):

    menor = numbers[0]
    for i in numbers:
        if i < menor:
            menor=i
            
    return menor


#assert(obtenerElMenorElemento([3,7,9])==3)
#assert(obtenerElMenorElemento([3,7,0])==0)
#assert(obtenerElMenorElemento([40,-2,0])==-2)

pideNumeros()



"""
Solución 2 resumida:


def pideNumeros():
    listaNumeros =[int(input("Enter one number: "))]
    while "Y"==input("Do you want to enter more number (Y/N)?"):
        listaNumeros.append(int(input("Enter one number: ")))
        
    print(obtenerElMenorElemento(listaNumeros))



#Esta función devuelve el elemento menor de una lista numérica

def obtenerElMenorElemento(numbers):

    menor = numbers[0]
    for i in numbers:
        if i < menor:
            menor=i
            
    return menor


#assert(obtenerElMenorElemento([3,7,9])==3)
#assert(obtenerElMenorElemento([3,7,0])==0)
#assert(obtenerElMenorElemento([40,-2,0])==-2)

pideNumeros()
"""