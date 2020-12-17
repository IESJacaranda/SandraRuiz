'''
Ejercicio 4

Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
Muestra el máximo de los números guardado en la lista, muestra los números pares.
'''


numero=int(input("Dime un número (negativo para parar): "))

def creaLista(numero):
    lista=[]
    while numero>0:
        lista.append(numero)
    
    return lista

def numMayor(lista):
    mayor=lista[0]
    for i in lista:
        if mayor < i:
            mayor=i
        
    return mayor


def numPares(lista):
    listaPar=[]
    for i in lista:
        if i%2==0:
            listaPar.append(i)
    
    return listaPar

def main():
    
    creaLista(numero)
    print("El número mayor de la lista es %s" % numMayor(creaLista(numero)))
    print("Los números pares de la lista son: %s" % numPares(creaLista(numero)))
          
main()