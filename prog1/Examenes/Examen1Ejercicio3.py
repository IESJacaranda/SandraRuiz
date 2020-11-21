numero1 = int(input("Introduce un numero"))
numero2 = int(input("Introduce otro numero"))
def maximoComunDivisor(numero1,numero2):
    mcd = 1

#con esta parte calculamos cual es el menor, para optimizar el problema
    menor = numero1
    if numero1 > numero2:
        menor = numero2
#con esta parte calculamos el rango            
    for i in range(1,menor+1):
        if (numero1%i==0 and numero2%i==0):
            mcd = i
    print(mcd)
    return mcd

"""
Define varios bloques de test:

def test():
    assert(maximoComunDivisor(3,7)==1)
    assert(maximoComunDivisor(4,9)==1)
    assert(maximoComunDivisor(4,16)==4)
    #print("Todos los test han sido superados con éxito") Este print es de control

test()
"""
maximoComunDivisor(numero1,numero2)