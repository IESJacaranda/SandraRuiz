"""
Ejercicio 7
Design a method called isPrime that receives one integer positive number greater than 0 as parameter. The method 
should return 1 if the number is prime or 0 if the number is not prime. If the parameter is not valid the method 
should return -1.
"""

def isPrime(number):
    if number<=0:
        result=-1
    else:
        divisor=0
        for i in range(1,number+1):
            if number%i==0:
                divisor+=1
        if divisor==2:
            result=1
        else:
            result=0
                    
    return result

assert(isPrime(-5)==-1)
assert(isPrime(0)==-1)
assert(isPrime(1)==0)
assert(isPrime(2)==1)
assert(isPrime(3)==1)
assert(isPrime(4)==0)
assert(isPrime(5)==1)
assert(isPrime(96)==0)
assert(isPrime(97)==1)
