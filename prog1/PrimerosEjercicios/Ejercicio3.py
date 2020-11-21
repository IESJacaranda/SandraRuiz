"""
Ejercicio 3
Realizar un programa que lea un número por teclado. El programa debe imprimir en pantalla un mensaje con “El número xx es 
múltiplo de 2” o un mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3 deben aparecer los dos mensajes. 
Si no es múltiplo de ninguno de los dos el programa finaliza sin mostrar ningún mensaje.

"""

number = int(input("Dime un número:"))
if number % 2 == 0:
    print(str(number)+ " es múltiplo de 2")
if number % 3 == 0:
    print(str(number)+ " es múltiplo de 3")