"""
Ejercicio 5
Design a method called myPower that receives one integer and one integer positive numbers as parameters and 
the method calculates the power of the first parameter raised the second number. You only can use the multiplication. 
If the parameters are not right (the second parameter is negative) the method should return -1. 
Remember that any number raised 0 is 1.

"""

def myPower(number,positiveNumber):
    potencia=1
    if positiveNumber<0:
        potencia=-1
    else:
        for i in range(1,positiveNumber+1):
            potencia*=number

    print(potencia)              
    
    #return potencia



number=int(input("Gimme an integer number: "))
positiveNumber=int(input("Gimme one positive number: "))


#assert(myPower(5,2)==25)
#assert(myPower(-1,3)==-1)
#assert(myPower(6,7)==279936)
#assert(myPower(4,-3)==-1)
#assert(myPower(8000,0)==1)

myPower(number,positiveNumber)