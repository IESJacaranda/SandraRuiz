"""
Ejercicio 9
Design a method called numberDivisorPrime that receives a positive number as a parameter. 
The method should return the number of prime divisors for this parameter. 
If the parameter is not valid the method should return -1.
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
    
    return result


def numberDivisors(number):
    divisors=[]
    if number>0:
        for i in range(1,number+1):
            if number%i==0:
                divisors.append(i)
    else:
        divisors=-1
    return divisors


assert(numberDivisors(15)==[1,3,5,15])
assert(numberDivisors(-1)==-1)
assert(numberDivisors(45)==[1,3,5,9,15,45])
assert(numberDivisors(4)==[1,2])
assert(numberDivisors(0)==-1)
assert(numberDivisors(-3)==-1)
assert(numberDivisors(582)==[1,2,3,6,97,194,291,582])


def numberDivisorPrime(divisors):
    primeDivisors=[]
    for i in divisors:
        if isPrime(i):
            primeDivisors.append(i)
    
    return len(primeDivisors)


assert(numberDivisorPrime([1,3,5,15])==2)


'''
Solución clase:

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
    

def numberDivisorPrime(number):
    divisors = []
    primeDivisors = []
    size = -1
    
    if number > 0:
        for i in range (1,(number//2)+1):
            if number%i==0:
                divisors.append(i)
    
        for div in divisors:
            if divisors(div):
                primeDivisors.append(div)
    
    return len(primeDivisors)



Solución 2: más óptima

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
    

def numberDivisorPrime(number):
    divisors = []
    primeDivisors = []
    size = -1
    
    if number > 0:
        for i in range (1,number):
            if number%i==0 and isPrime(number):
                primeDivisors.append(i)
        size = len(primeDivisors)
    
    return len(primeDivisors)

assert(numberDivisorPrime(5)==1)
assert(numberDivisorPrime(2)==1)
assert(numberDivisorPrime(8)==2)
assert(numberDivisorPrime(63)==3)
assert(numberDivisorPrime(1)==0)
assert(numberDivisorPrime(63)!=2)
assert(numberDivisorPrime(0)==-1)
assert(numberDivisorPrime(-2)==-1)

'''
