'''
Author: Sandra Ruiz Jiménez

Ejercicio 2

Estamos trabajando en una empresa que se dedica a realizar desafíos entre dos 
contrincantes, por ejemplo, contrincante A y contrincante B. Un revisor califica 
los dos desafíos, otorgando puntos en una escala del 1 al 100 para tres categorías: 
claridad del problema, originalidad y dificultad a cada uno de los contrincantes.

Al final de la revisión tendremos un array o lista con las calificaciones del 
contrincante A y otro array o lista con las calificaciones del contrincante B. 
En cada array o lista tendremos la calificación a la claridad del problema, 
luego a la originalidad y luego a la dificultad por cada uno de los retos. 
Por ejemplo si han realizado 2 retos, tenemos el siguiente array para el 
contrincante A

50    80    20     60    70    75

Lo que indica que en el primer reto en claridad del problema obtuvo un 50, 
en originalidad un 80 y en dificultad un 20, y en el segundo reto obtuvo un 
60 en claridad del problema, un 70 en originalidad y un 75 en dificultad.

El contrincante que gana cada reto será el que obtenga más puntos sumando 
la claridad del problema, la originalidad y la dificultad.


Realizar una función que dado dos listas de calificaciones de los dos contrincantes, 
nos devuelva el número de partidas que ha ganado el primer contrincante.

Realizar un programa que usando la función anterior, pregunte cuántos retos 
van a jugar, luego pregunte la valoración para cada reto y cada participante, 
y por último informe de las partidas ganadas por cada participante.
'''

'''
Esta función suma las calificaciones de una partida, recibe una lista
con 3 elementos numéricos y devuelve la suma de los mismos
'''
def sumaCalificacionesPartida(lista):
    suma=0
    for i in lista:
        suma+=i
    
    return suma

assert(sumaCalificacionesPartida([50,80,20])==150)
assert(sumaCalificacionesPartida([60,70,75])==205)

'''
Esta función debería recibir la lista de calificaciones de cada jugador
y dividirla en tantas listas como retos hayan jugado, pero no funciona.
'''
def divideListaCalificaciones(lista):
    lista1=[]
    while len(lista)>=0 and len(lista)=<2
    for i in range (len(lista)):
        if i<=2:
            lista1.append(lista[i])
        elif i>2 and i<=5:    
            lista2.append(lista[i])
        elif i>2 and i<=5:  
            
   
assert(divideListaCalificaciones([60,70,75,50,40,30])==[60,70,75],[50,40,30])
  
"""
Esta función es la principal que interactura con el usuario,
pide los datos y comprueba que son correctos y los mete en dos listas.
Devuelve el numero de partidas ganadas de cada usuario.
"""
               
def main():
    calificacionesA=[]
    calificacionesB=[]
    numeroRetos=int(input("Numero retos: "))
    while numeroRetos<0:
        numeroRetos=int(input("Numero retos: "))
    if numeroRetos>0:
        for i in range(numeroRetos):
            claridad=int(input("Puntuacion claridad participante A: "))
            while claridad<0 and claridad>100:
                claridad=int(input("Puntuacion claridad participante A: "))
            if claridad>=0 and claridad<=100:
                calificacionesA.append(claridad)
            originalidad=int(input("Puntuacion originalidad participante A: "))
            while originalidad<0 and originalidad>=100:
                originalidad=int(input("Puntuacion originalidad participante A: "))
            if originalidad>=0 and originalidad<=100:
                calificacionesA.append(originalidad)
            dificultad=int(input("Puntuacion dificultad participante A: "))
            while dificultad<0 and dificultad>100:
                dificultad=int(input("Puntuacion dificultad participante A: "))
            if dificultad>=0 and dificultad<=100:
                calificacionesA.append(dificultad)
            
            claridad=int(input("Puntuacion claridad participante B: "))
            while claridad<0 and claridad>100:
                claridad=int(input("Puntuacion claridad participante B: "))
            if claridad>=0 and claridad<=100:
                calificacionesB.append(claridad)
            originalidad=int(input("Puntuacion originalidad participante B: "))
            while originalidad<0 and originalidad>=100:
                originalidad=int(input("Puntuacion originalidad participante B: "))
            if originalidad>=0 and originalidad<=100:
                calificacionesB.append(originalidad)
            dificultad=int(input("Puntuacion dificultad participante B: "))
            while dificultad<0 and dificultad>100:
                dificultad=int(input("Puntuacion dificultad participante B: "))
            if dificultad>=0 and dificultad<=100:
                calificacionesB.append(dificultad)
    
main()

    