"""
Design a method called myPower that receives two positive integer numbers 
and computes the power of the first parameter raised to the second one. 
You can only use the multiplication. 
Remember that any number raised to 0 equals 1.

"""

def myPower(base,exponente):
    potencia=1
    if exponente<0:
        exponente = -exponente
        base=1/base
    for i in range(exponente):
        potencia*=base
        
    return potencia



assert(myPower(5,2)==25)
assert(myPower(6,7)==279936)
assert(myPower(8000,0)==1)
assert(myPower(2,-2)==0.25)
assert(myPower(-2,5)==-32)
assert(myPower(-2,-2)==0.25)
