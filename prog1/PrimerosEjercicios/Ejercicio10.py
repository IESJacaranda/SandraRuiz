"""
Ejercicio 10
Realizar un programa que lea un carácter y dos números enteros por teclado. Si el carácter leído es un operador aritmético, calcular la operación correspondiente, 
si es cualquier otro debe mostrar un error.

"""

entero1 = int(input("Introduce un número entero:"))
caracter = input("Introduce un operador aritmético:")
entero2 = int(input("Introduce otro número entero:"))
if caracter == "+":
    resultado = entero1 + entero2
    print("El resultado es",str(resultado))
elif caracter == "-":
    resultado = entero1 - entero2
    print("El resultado es",str(resultado))
elif caracter == "*":
    resultado = entero1 * entero2
    print("El resultado es",str(resultado))
elif caracter == "/":
    resultado = entero1 / entero2
    print("El resultado es",str(resultado))
else:
    print("El caracter introducido no es un operador aritmético")