"""
Ejercicio 6
Design a method called numberOfNumbers that receives one positive integer and 
returns its number of digits (11578 → 5, 22 → 2, and so on). 
If the value entered by the user is not valid, then the method should return -1.
"""

"""
def numberOfNumbers(number):
    digitsNumber=-1
    if number>0:
        digitsNumber=len(str(number))
        
    return digitsNumber
    
    
assert(numberOfNumbers(-1)==-1)
assert(numberOfNumbers(-30)==-1)
assert(numberOfNumbers(0)==-1)
assert(numberOfNumbers(9)==1)
assert(numberOfNumbers(10)==2)
assert(numberOfNumbers(99)==2)
assert(numberOfNumbers(100)==3)
assert(numberOfNumbers(1000)==4)
assert(numberOfNumbers(59393038)==8)

"""
'''
Esta función recibe un entero positivo y calcula sus dígitos.
'''
def numberOfNumbers(number):
    count=-1
    
    if number>0:
        count=1
        while number>=10:
            count+=1
            number=number//10
    
    return count


assert(numberOfNumbers(-1)==-1)
assert(numberOfNumbers(0)==-1)
assert(numberOfNumbers(9)==1)
assert(numberOfNumbers(10)==2)
assert(numberOfNumbers(99)==2)
assert(numberOfNumbers(100)==3)
assert(numberOfNumbers(1000)==4)
assert(numberOfNumbers(59393038)==8)