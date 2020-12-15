'''
Revisión listas, bucles for y funciones
'''

#Declaración y definición de listas

lista1 = [1,2,3,5,7,9,11,15]
lista2 = ["1","2","3","5","7","9","11","15"]

lista1 = [] #Declaración de lista vacía

print(type(lista1[0])) #respuesta <class 'int'>
print(type(lista2[0])) #respuesta <class 'str'>

print(lista1[0]==lista2[0]) #respuesta False


#Recorrido de listas

lista1 = [1,2,3,5,7,9,11,15]

for i in range (len(lista1)):
    print(i) #imprime las posiciones: 0,1,2,3,4,5,6,7
    print(lista1[i]) #imprime los valores de la lista: 1,2,3,5,7,9,11,15

for i in range(0,len(lista1)):
    print(i) #imprime las posiciones: 0,1,2,3,4,5,6,7
    print(lista1[i]) #imprime los valores de la lista: 1,2,3,5,7,9,11,15
    
for i in range(0,len(lista1),1):
    print(i) #imprime las posiciones: 0,1,2,3,4,5,6,7
    print(lista1[i]) #imprime los valores de la lista: 1,2,3,5,7,9,11,15

'''
Los 3 bucles for anteriores son iguales, porque en los bucles for
se sobreentiende el límite inicial 0 y el step 1, así que si no se
escriben hacen lo mismo que si se escribieran.
'''
        
for i in lista1:
    print(i) #imprime los valores de la lista: 1,2,3,5,7,9,11,15

    
#Para recorrer ambas listas:

lista1 = [1,2,3,5,7,9,11,15]
lista2 = ["1","2","3","5","7","9"]


for i in range(len(lista1)):
    print((lista1[i], lista2[i])) 
#lista2, como no tiene posición 6 y 7, está out of range

for i in range(len(lista2)):
    print((lista1[i], lista2[i])) 
#se imprimen todos los elementos de lista2 y solo 6 posiciones de lista1
    
for i in range(len(lista2)):
    print(lista1[i]==lista2[i]) 
#se imprimen todos los elementos de lista2 y solo 6 posiciones de lista1
#salen que los valores son False, no son iguales
    
for i in range(len(lista2)):
    print(lista1[i],lista2[i],str(lista1[i])==lista2[i]) 
#se imprimen todos los elementos de lista2 y solo 6 posiciones de lista1
#salen que los valores son True, porque hemos convertido lista1 a cadena de texto


lista1 = [1,2,3,5,7,9,11,15]
lista2 = ["1","2","3","5","7","9"]
cadena= "123579"
for i in range(len(lista2)):
    print(lista1[i],lista2[i], str(lista1[i])==lista2[i],cadena[i])
'''                
se imprimen todos los elementos de lista2 y solo 6 posiciones de lista1
y de cadena
(1,'1') 1 True
(2,'2') 2 True
(3,'3') 3 True
(5,'5') 5 True
(7,'7') 7 True
(9,'9') 9 True            
'''

''''

https://colab.research.google.com/notebooks/intro.ipynb#recent=true
sirve para compilar código Python online, por si no funciona Eclipse 

'''

def definicionDeUnaFuncionSinArgumentos():
    print("No recibo ningún argumento ni devuelvo nada")
    
definicionDeUnaFuncionSinArgumentos(3)

'''
Esta función da error, por el (3), ya que la función no recibe ningún
argumento, pero le se le da uno.
Los argumentos es lo que tienen entre paréntesis las funciones y cuando la llamo
debe ser igual que en la función.
'''

def definicionDeUnaFuncionSinArgumentos1():
    print("No recibo ningún argumento ni devuelvo nada")
    
print(definicionDeUnaFuncionSinArgumentos1())
'''
imprime:
No recibo ningún argumento ni devuelvo nada
None #esto lo devuelve porque no hay ningún return.
Es equivalente a hacer:
'''
def definicionDeUnaFuncionSinArgumentos2():
    print("No recibo ningún argumento ni devuelvo nada")
    return None
    
print(definicionDeUnaFuncionSinArgumentos2())

''''
Las funciones tienen que devolver argumentos, por eso no es aconsejable
que impriman nada y, son mejores los return.
'''
def definicionDeUnaFuncionSinArgumentos3():
    return "No recibo ningún argumento ni devuelvo nada"
    
print(definicionDeUnaFuncionSinArgumentos3())

#Funciones con argumentos:

def funcionConArgumentosYReturn(numero):
    mensaje=""
    if (numero%2==0):
        mensaje+= "El número %s es par" % numero
    else:
        mensaje+= "El número %s es impar" % numero
    
    return mensaje
    
print(funcionConArgumentosYReturn())
'''
La función anterior da error porque en la linea 140 espera una llamada
con argumento y no lo tiene
'''

def funcionConArgumentosYReturn2(numero):
    mensaje=""
    if (numero%2==0):
        mensaje+= "El número %s es par" % numero
    else:
        mensaje+= "El número %s es impar" % numero
    
    return mensaje

print(funcionConArgumentosYReturn2(4))
'''
La función anterior imprime por pantalla "El número 4 es par"
'''

def funcionConArgumentosYReturn3(numero):
    mensaje=""
    if (numero%2==0):
        mensaje+= "El número %s es par" % numero
    else:
        mensaje+= "El número %s es impar" % numero
    
    return mensaje

funcionConArgumentosYReturn3(4)
'''     
La función anterior se ejecuta y devuelve un mensaje, solo que no
la imprime por pantalla al no haber un print, por lo que en consola 
vamos a ver un terminated y ya está
'''

def funcionConArgumentosYReturn4(numero=15):
    mensaje=""
    if (numero%2==0):
        mensaje+= "El número %s es par" % numero
    else:
        mensaje+= "El número %s es impar" % numero
    
    return mensaje

print(funcionConArgumentosYReturn4())
'''
Esto no lo vamos a ver, pero esta función imprime por pantalla
El número 15 es impar
'''

def funcionConArgumentosYReturn5(numero=15):
    mensaje=""
    if (numero%2==0):
        mensaje+= "El número %s es par" % numero
    else:
        mensaje+= "El número %s es impar" % numero
    
    return mensaje

print(funcionConArgumentosYReturn5(6))
'''
Esto tampoco lo vamos a ver, pero esta función sobreescribe el 6 que le
damos como argumento y devuelve por pantalla:
El número 6 es par"
'''

'''
Una función puede recibir "infinitos" argumentos como máximo y como mínimo
ninguno, pero hay que llamarla con el mismo número de argumentos con la que 
está definida.

'''

'''
Las variables que hemos visto:
- Los boolean
- Los int
- Los string
- Tb las funciones las entiende Python como una variable con más argumentos.
'''

'''
TESTS:
Una función que interactúa con el usuario (le pide datos), no hay que hacerle
tests.
'''