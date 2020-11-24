"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 8
Realizar un programa que pregunte el número de partidos jugados en esta 
jornada. Luego para cada uno de los partidos debe preguntar el número de 
goles del equipo local y del equipo visitante y el programa debe determinar 
el resultado de la quiniela. Debe asegurarse que los valores son correctos.

"""

def calculaQuiniela():
    resultado=""
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
            resultado="Resultado: 1"
        elif golesLocal == golesVisitante:
            resultado="Resultado: X"
        else:
            resultado="Resultado: 2"
        print(resultado)

calculaQuiniela()


'''
Solución clase:


numeroPartidos = int(input("Cuantos partidos hubo esta semana?")
while numeroPartidos<=0:
    numeroPartidos = int(input("Error. Cuantos partidos hubo esta semana?")
def calculaResultadoQuiniela(partidos):
    resultado = []
    
    for i in range(partidos):
        golesLocal = int(input("Cuantos goles marco el equipo local?")
        while golesLocal<0:
            golesLocal = int(input("Error. Cuantos goles marco el equipo local?")
        golesVisitante = int(input("Cuantos goles marco el equipo visitante?")
        while golesVisitante<0:
            golesVisitante = int(input("Error. Cuantos goles marco el equipo local?")
        
    return resultado
    
    
    
calculaResultadoQuiniela(numeroPartidos)