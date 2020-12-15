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
    count=0
    for i in divisors:
        if isPrime(i)==True:
            count+=1
    
    return count


assert(numberDivisorPrime([1,3,5,15])==2)


