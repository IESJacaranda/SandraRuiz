"""
Created on 17 nov.2020
@author: Sandra Ruiz Jimenez

Ejercicio 5
Realizar un programa que solicite la coordenada x e y de un punto e informe si se encuentre
en el primer, segundo, tercer o cuarto cuadrante.

"""

def calculaCuadrante (x, y):
    cuadrante = ""
    if x>0 and y>0:
        cuadrante = "Primer cuadrante."
    elif x<0 and y>0:
        cuadrante = "Segundo cuadrante."
    elif x<0 and y<0:
        cuadrante = "Tercer cuadrante."
    elif x>0 and y<0:
        cuadrante = "Cuarto cuadrante."
    elif x==0 and y==0:
        cuadrante = "Origen de coordenadas"
    elif x!=0 and y==0:
        cuadrante = "Eje x"
    else:
        cuadrante = "Eje y"
         
    return cuadrante


def dimeCuadrante():
    while True:
        x=float(input("Dime la coordenada x: "))
        y=float(input("Dime la coordenada y: "))
        print("Ese punto pertenece a %s" % (calculaCuadrante(x, y)))
        
""" podría ponerse más sintético
def dimeCuadrante():
    while True:
        print("Ese punto pertenece a %s" % (calculaCuadrante (float(input("Dime la coordenada x: ")), float(input("Dime la coordenada y: ")))))
"""

dimeCuadrante()
"""casos de prueba
print(calculaCuadrante(1, 2)) #primer cuadrante
print(calculaCuadrante(-1, 2)) #segundo cuadrante
print(calculaCuadrante(-1, -2)) #tercer cuadrante
print(calculaCuadrante(1, -2)) #cuarto cuadrante
print(calculaCuadrante(0, 0)) #origen de coordenadas
print(calculaCuadrante(1, 0)) #eje x
print(calculaCuadrante(0, -1)) #eje y

#Una vez comprobados los print, ponemos assert y lo igualamos al return
assert(calculaCuadrante(1, 2)=="Primer cuadrante")
assert(calculaCuadrante(-1, 2)=="Segundo cuadrante")
assert(calculaCuadrante(-1, -2)=="Tercer cuadrante")
assert(calculaCuadrante(1, -2)=="Cuarto cuadrante")
assert(calculaCuadrante(0, 0)=="Origen de coordenadas")
assert(calculaCuadrante(1, 0)=="Eje x")
assert(calculaCuadrante(0, -1)=="Eje y")

""" 