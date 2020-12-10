"""
Ejercicio 6
Design a method called numberOfNumbers that receives one integer positive number as parameter. The method should 
return the number of digits of the number that received by parameter. If the parameter is not valid the method 
should return -1.
"""

def numberOfNumbers(number):
    if number<=0:
        digitsNumber=-1
    elif number>0: 
        number=str(number)
        digitsNumber=len(number)
        
    
        
    return digitsNumber
    
    
assert(numberOfNumbers(-1)==-1)
assert(numberOfNumbers(0)==-1)
assert(numberOfNumbers(9)==1)
assert(numberOfNumbers(10)==2)
assert(numberOfNumbers(99)==2)
assert(numberOfNumbers(100)==3)
assert(numberOfNumbers(1000)==4)
assert(numberOfNumbers(59393038)==8)