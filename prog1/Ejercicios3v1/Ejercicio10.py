"""
Ejercicio 10
    10. Design a method called friend that receives two positive number as parameters. 
    The method should return true if the number are friends and false in other case. 
    Two numbers are friends if the addition of all the divisors (itself is not considered) 
    of one number equals the other one and vice versa. If the parameters are not valid 
    the method should return false.

"""


def sumDivisor(number):
    sum=0
    for i in range(1,number-1):
        if number%i==0:
            sum+=i
    return sum    


def friend(number1, number2):
    result=False
    if number1>0 and number2>0 and sumDivisor(number1)==number2 and sumDivisor(number2)==number1:
        result=True
    
    return result


assert(friend(220, 284)==True)
assert(friend(1184, 1210)==True)
assert(friend(0, 120)==False)
assert(friend(748,-1)==False)
assert(friend(10,20)==False)