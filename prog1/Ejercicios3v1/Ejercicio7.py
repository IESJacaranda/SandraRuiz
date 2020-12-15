"""
Ejercicio 7
Design a method called isPrime that receives one positive integer number greater than 0 
as parameter. The method should return True if the number is prime or False if not. 
If the parameter is not valid the method will no return anything.
"""

'''
Esta función calcula si un número es primo. Devuelve cierto si lo es, 
falso si no lo es y nada si el valor es incorrecto.
'''
def isPrime(number):
    result = None 
    if number>0:
        result = True
        for i in range(2,number): #no vale para el 2
            if number%i==0:
                return False

    
    return result


assert(isPrime(-5)==None)
assert(isPrime(0)==None)
assert(not isPrime(1))
assert(isPrime(2)==True)
assert(isPrime(3)==True)
assert(not isPrime(4))
assert(isPrime(5)==True)
assert(not isPrime(96))
assert(isPrime(97)==True)


'''
Solución válida para el dos con bucle while:


def isPrime(number):
    result = None 
    if number>0:
        prime = True
        i = 2
        while i<number//2+1 and prime:
            if number%i==0:
                prime = False
            i+=1
    
    return prime

'''
