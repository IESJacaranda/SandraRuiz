"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 8
Realizar un programa que pregunte el número de partidos jugados en esta 
jornada. Luego para cada uno de los partidos debe preguntar el número de 
goles del equipo local y del equipo visitante y el programa debe determinar 
el resultado de la quiniela. Debe asegurarse que los valores son correctos.

"""

def numeroPartidos():
    mensaje=""
    partido=int(input("Cuantos partidos se han jugado en esta jornada? "))
    while partido<=0:
        partido=int(input("Error. Cuantos partidos se han jugado en esta jornada? "))
    for i in range (0, partido):
        golesLocal=int(input("Numero de goles del equipo local: "))
        while golesLocal<0:
            golesLocal=int(input("Error. Numero de goles del equipo local: "))
        golesVisitante=int(input("Numero de goles del equipo visitante: "))
        while golesVisitante<0:
            golesVisitante=int(input("Error. Numero de goles del equipo visitante: "))
        if golesLocal > golesVisitante:
            mensaje="Resultado: 1"
        elif golesLocal == golesVisitante:
            mensaje="Resultado: X"
        else:
            mensaje="Resultado: 2"
        print(mensaje)

numeroPartidos()    