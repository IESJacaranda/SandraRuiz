"""
Ejercicio 7
Design a method called isPrime that receives one positive integer number greater than 0 
as parameter. The method should return True if the number is prime or False if not. 
If the parameter is not valid the method will no return anything.
"""

def isPrime(number):
    if number>0:
        divisor=0
        for i in range(1,number+1):
            if number%i==0:
                divisor+=1
        if divisor==2:
            result=True
        else:
            result=False
    else:
        return None               
    
    return result


assert(isPrime(-5)==None)
assert(isPrime(0)==None)
assert(isPrime(1)==False)
assert(isPrime(2)==True)
assert(isPrime(3)==True)
assert(isPrime(4)==False)
assert(isPrime(5)==True)
assert(isPrime(96)==False)
assert(isPrime(97)==True)
