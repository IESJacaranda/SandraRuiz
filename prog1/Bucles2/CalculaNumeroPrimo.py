'''
Enunciado: crea un programa que pida un número y diga si es primo o no.

'''

def esNumeroPrimo():
    num=int(input("Dame un número: "))
    divisor=0
    for i in range(1,num):
        if num%i==0:
            divisor+=i
    if divisor==1:
        print("El número es primo")
    else:
        print("El número no es primo")
        
esNumeroPrimo()


'''
Otra solución:

def esNumeroPrimo():
    num=int(input("Dame un número: "))
    divisor=0
    for i in range(1,num):
        if num%i==0:
            divisor+=i
    return divisor == 1 
"""
Este return equivaldría a:
    if divisor==1:
        return True
    else:
        return False
pq si compara por ej. 1==1 devuelve True y 3==1 devuelve False
"""
        
esNumeroPrimo()

'''