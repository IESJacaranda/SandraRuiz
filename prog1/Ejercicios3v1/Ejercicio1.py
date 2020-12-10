"""
Ejercicio 1
Design a method called factorial that receives a positive integer and returns the 
factorial. If the number is negative the method should return -1.


Factorial
El factorial de un entero positivo n, el factorial de n o n factorial se define 
en principio como el producto de todos los números enteros positivos desde 1 
(es decir, los números naturales) hasta n. Por ejemplo:

    5 ! = 1 × 2 × 3 × 4 × 5 = 120

"""


def factorialNumero(numero):
    resultado=1
    if numero<0:
        resultado=-1  
    else:
        for i in range (1,numero+1):  
            resultado*=i
            
    return resultado
        

        
#numero=int(input("Dame un numero entero: "))

    
#print(factorialNumero(numero))



assert(factorialNumero(0)==1)
assert(factorialNumero(-1)==-1)
assert(factorialNumero(-50)==-1)
assert(factorialNumero(3)==6)
assert(factorialNumero(5)==120)
assert(factorialNumero(4)==24)

