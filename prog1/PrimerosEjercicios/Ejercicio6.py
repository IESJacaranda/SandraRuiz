"""
Ejercicio 6
Realizar un programa que solicite un carácter por teclado e informe por pantalla si el carácter es una vocal o no lo es. 
Si es una vocal mostrará el mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.

"""

caracter = input("Introduce un caracter:")
if caracter == "A" or caracter == "a":
    print("Es la primera vocal (A)")
elif caracter == "E" or caracter == "e":
    print("Es la segunda vocal (E)")
elif caracter == "I" or caracter == "i":
    print("Es la tercera vocal (I)")
elif caracter == "O" or caracter == "o":
    print("Es la cuarta vocal (O)")
elif caracter == "U" or caracter == "u":
    print("Es la quinta vocal (U)")
else:
    print("No es una vocal")