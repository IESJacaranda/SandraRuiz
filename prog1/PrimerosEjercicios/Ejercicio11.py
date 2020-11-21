"""
Ejercicio 11
Elabora un programa que dadas las dimensiones de los tres lados de un triángulo determine si el triángulo es equilátero, isósceles o escaleno y/o rectángulo.
Extra: calcula su área.

"""

import math
lado1 = int(input("Dame el primer lado del triángulo:"))
mayor = lado1
lado2 = int(input("Dame el segundo lado del triángulo:"))
lado3 = int(input("Dame el tercer lado del triángulo:"))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado2 > mayor:
        mayor = lado2
    if lado3 > mayor:
        mayor = lado3
    if lado1 == lado2 and lado1 == lado3:
        print("El triángulo es equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print("El triángulo es escaleno")
        if lado1 == mayor and lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
            print("El triángulo es rectángulo")
        elif lado2 == mayor and lado2 * lado2 == lado1 * lado1 + lado3 * lado3:
            print("El triángulo es rectángulo")
        elif lado3 == mayor and lado3 * lado3 == lado1 * lado1 + lado2 * lado2:
            print("El triángulo es rectángulo")
    elif lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado3 != lado2 or lado3 == lado2 and lado2 != lado1:
        print("El triángulo es isósceles")
        if lado1 == mayor and lado1 * lado1 == lado2 * lado2 + lado3 * lado3:
            print("El triángulo es rectángulo")
        elif lado2 == mayor and lado2 * lado2 == lado1 * lado1 + lado3 * lado3:
            print("El triángulo es rectángulo")
        elif lado3 == mayor and lado3 * lado3 == lado1 * lado1 + lado2 * lado2:
            print("El triángulo es rectángulo")
    s = (lado1+lado2+lado3)/2
    area = math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    print("El área del triángulo es ",str(area))
else:
    print("No se trata de un triángulo")