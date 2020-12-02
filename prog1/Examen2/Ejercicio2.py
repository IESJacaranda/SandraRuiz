"""
Examen 2 Diciembre - Ejercicio 2

Realizar una función que reciba como parámetro una cadena que contenga un dni y 
devuelva un True si el dni es válido y False en caso contrario. Para calcular la letra 
debemos tomar el número completo de hasta 8 cifras de nuestro DNI, lo dividimos entre 23 
y nos quedamos con el resto de dicha división.

El resultado anterior es un número entre 0 y 22. A cada uno de estos posibles 
números le corresponde una letra, según la siguiente tabla:

*(Aquí comprobamos cada resto (numero entero) y sustituimos por letra (string)). 

Si el formato no es válido deberá devolver False.

Mejora opcional: Ten en cuenta que hay dni que en vez de 8 números pueden tener 7.

Entrega las pruebas que has realizado.

"""


def dniL(dni):
    
    resto=dni%23
    letra=""
    if resto==0:
        letra="T"
    elif resto==1:
        letra="R"
    elif resto==2:
        letra="W"
    elif resto==3:
        letra="A"
    elif resto==4:
        letra="G"
    elif resto==5:
        letra="M"
    elif resto==6:
        letra="Y"
    elif resto==7:
        letra="F"
    elif resto==8:
        letra="P"
    elif resto==9:
        letra="D"
    elif resto==10:
        letra="X"
    elif resto==11:
        letra="B"
    elif resto==12:
        letra="N"
    elif resto==13:
        letra="J"
    elif resto==14:
        letra="Z"
    elif resto==15:
        letra="S"
    elif resto==16:
        letra="Q"
    elif resto==17:
        letra="V"
    elif resto==18:
        letra="H"
    elif resto==19:
        letra="L"
    elif resto==20:
        letra="C"
    elif resto==21:
        letra="K"
    elif resto==22:
        letra="E"
    else:
        letra="El DNI no es correcto"
    
    return letra
    
          

                        
assert(dniL(75410143)=="C")
assert(dniL(15409981)=="G")


def dniVerificacion(dni,letra):
    if dniL=="T" or dniL=="R" or dniL=="W" or dniL=="A" or dniL=="G" or dniL=="M" or dniL=="Y" or dniL=="F" or dniL=="P" or dniL=="D" or dniL=="X" or dniL=="B" or dniL=="N" or dniL=="J" or dniL=="Z" or dniL=="S" or dniL=="Q" or dniL=="V" or dniL=="H" or dniL=="L" or dniL=="C" or dniL=="K" or dniL=="E":
        return True
    else:
        return False
    
assert(dniVerificacion(75410143,"C")==True)
assert(dniVerificacion(15409981,"G")==True)
assert(dniVerificacion(15410000,"H")==False)