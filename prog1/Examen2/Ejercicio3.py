"""
Examen 2 Diciembre - Ejercicio 3

Realizar un programa que nos sirva para crear el id de usuario que nuestros empleados 
utilizarán para conectarse a nuestras aplicaciones. 
El programa debe preguntarle al usuario su nombre y sus apellidos, separando los datos por coma. 
Es decir si me preguntan a mi yo debo poner JoséManuel,Sevillano,Armenta (puedes suponer que nos 
van a dar los valores bien). 
Luego debe preguntar el dni, debe comprobar que se trata de un dni válido, si no es válido volver 
a preguntarlo hasta que nos dé un dni válido. 
Por último debe llamar a una función que devuelva el id. 
Para calcular el id le pasaremos la cadena con el nombre y apellidos y creará el id con los tres 
primeros caracteres del nombre, los tres últimos del primer apellido, los tres 
primeros del segundo apellido y los tres primeros números del dni.

Pasos del algoritmo:

1. Solicitar datos
    a. Nombre y Apellidos
    b. DNI ==> validar
2. Separamos nombre y apellidos ==> lista
3. Llamamos a la función que nos genera el id de usuario
"""

def calcularLetra(numeroDNI):
    return "TRWAGMYFPDXBNJZSQYHLCKE"[numeroDNI % 23]


def separarNumeroDNI(dniConLetra):
    numeroTmp = ""
    for i in range(len(dniConLetra)-1):
        numeroTmp+=dniConLetra[i]
    return int(numeroTmp)

    
def esDniValido(dniConLetra):
    numeroDNI = separarNumeroDNI(dniConLetra)
    resultado = False
    if dniConLetra[-1]==calcularLetra(numeroDNI):
        resultado=True
    
    return resultado



"""
Esta función recibe una cadena de texto con datos identificativos (nombre y apellidos) 
sin espacios entre ellos y separados por comas y devuelve una lista con los anteriores de
forma individual
"""
def separarCadena(nombre):
    lista= []
    tmp = ""
    for i in nombre:
        if i != ",":
            tmp+=i
        else:
            lista.append(tmp)
            tmp=""
    lista.append(tmp) #para que añada a la lista el segundo apellido
    
    return lista



#assert(separarCadena("JoseManuel,Sevillano,Armenta")==["JoseManuel","Sevillano","Armenta"])
#assert(separarCadena("Sandra,Ruiz,Jimenez")==["Sandra", "Ruiz","Jimenez"])



"""
A partir de una lista con nombre y paellidos junto al dni construye un identificador de
usuario de como máximo 12 caracteres
"""
def generaIdUsuario(listaIdentificadores, dni):
    idUsuario=""
    listaIdentificadores.append(dni) #de esta manera me quedo con una sola lista
    
    for i in range (0,len(listaIdentificadores)): #la i toma 4 valores, los 4 elementos de la lista
        if i!=1: 
            for j in range(3): #nombre,apellido2 y dni, necesito las 3 primeras posiciones
                idUsuario += listaIdentificadores[i][j]
        else:
            for k in range(-3,0): #apellido1, necesito las 3 ultimas posiciones
                idUsuario += listaIdentificadores[i][k]
                        
    return idUsuario.lower()


"""
Otra solución con variables y sin bucle:

def generaIdUsuario(listaIdentificadores, dni):
    idUsuario=""
    listaIdentificadores.append(dni)
        
    nombre = listaIdentificadores[0]
    apellido1 = listaIdentificadores[1]
    apellido2 = listaIdentificadores[2]
    
    idUsuario = nombre[0] + nombre[1] + nombre[2]
    idUsuario += apellido1[-3] + apellido1[-2] + apellido1[-1]
    idUsuario += apellido2[0] + apellido2[1] + apellido2[2]  
    idUsuario += dni[0] + dni[1] + dni[2]  
    
    return idUsuario.lower()

"""


nombreSeparado=["Miguel","DeCervantes","Saavedra"]
dniValido8Cifras = "14141414W"

assert(generaIdUsuario(nombreSeparado, dniValido8Cifras)=="migtessaa141")



def funcionPrincipal():
    nombre_apellidos=input("Introduce tu nombre y apellidos separados por coma: ")
    dni=input("Introduce tu dni en formato 11111111X: ")
    
    while (not esDniValido(dni)):
        dni=input("Error. Introduce tu dni en formato 11111111X: ") 
        
    print("El id de usuario es %s" % generaIdUsuario(separarCadena(nombre_apellidos), dni))
    
funcionPrincipal()