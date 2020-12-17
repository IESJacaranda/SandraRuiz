'''
Ejercicio 4

Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. 
Muestra el máximo de los números guardado en la lista, muestra los números pares.
'''



    


def creaLista(listaNumeros, numero):
    if numero>=0:
        listaNumeros.append(numero)
    return listaNumeros


def numMayor(lista):
    mayor=0
    if len(lista)>0:
        mayor = lista[0]
        for i in lista:
            if i > mayor:
                mayor = i

    return mayor


def numPares(lista):
    listaPar=[]
    for i in lista:
        if i%2==0:
            listaPar.append(i)
    
    return listaPar

def main():
    numero=0
    listaNumeros=[]
    while numero>=0:
        numero=int(input("Dime un número (negativo para parar): "))
        lista = creaLista(listaNumeros, numero)
    print("El número mayor de la lista es %s" % numMayor(creaLista(listaNumeros, numero)))
    print("Los números pares de la lista son: %s" % numPares(creaLista(listaNumeros, numero)))
          
main()
