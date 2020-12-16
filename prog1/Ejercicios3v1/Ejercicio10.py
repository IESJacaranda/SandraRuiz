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
    for i in range(1,number//+1):
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

'''
Solución clase:

def getDivisors(number):
    divisors = []
       
    if number > 0:
        for i in range (1,(number//2)+1):
            if number%i==0:
                divisors.append(i)
    
    return divisors

def sumaListaNumeros(lista):
    sumaTotal=0
    
    for elemento in lista:
        sumaTotal+=elemento
        
    return sumaTotal
            
assert(sumaListaNumeros([])==0)
assert(sumaListaNumeros([1,3,5,9])==18)      
   

def areFriends(number1, number2):
    friends = False
    if number1!=number2 and number1>0 and number2>0:
        sumaDiv_1=sumaListaNumeros(getDivisors(number1))
        sumaDiv_2=sumaListaNumeros(getDivisors(number2))
        friend = (number1==sumaDiv_2) and (number2==sumaDiv_1) 
    
    return friends

'''
'''
* más reducido:

def areFriends(number1, number2):
    return number1!=number2 and number1==sumaListaNumeros(getDivisors(number2)) and number2==sumaListaNumeros(getDivisors(number1))_

assert(areFriends(220, 284))
assert(areFriends(1184, 1210))
assert(not areFriends(0, 120))
assert(not areFriends(748,-1))
assert(not areFriends(10,20))

'''
