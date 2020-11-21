def healthCheck():
    estiloVida = ""
    edad = 0
    peso = 0.0
    mensaje = "No es urgente que acuda al médico si no tiene problemas de salud"
    
    while peso>=0:
        peso = float(input("Por favor, introduce tu peso en kg:"))
        if peso>=0:
            estiloVida = input("Que estilo de vida llevas (Sedentaria, Activa o Muy activa)?")
            while estiloVida != "Sedentaria" and estiloVida != "Activa" and estiloVida != "Muy activa":
                estiloVida = input("Que estilo de vida llevas (Sedentaria, Activa o Muy activa)?")
            edad = int(input("Que edad tienes?"))
            while edad <= 0:
                edad = int(input("Que edad tienes?"))
            print(giveMeMyHealthStatus(estiloVida, edad, peso)) #Llamamos a la función desarrollada abajo
          
    print("Nos vemos en otra ocasión. Que le vaya bien")

#En el siguiente código desarrollamos la función con las condiciones del problema

def giveMeMyHealthStatus(estiloVida, edad, peso):
    mensaje= ""
    if peso > 100:
        mensaje = "Debería ir al médico"
    elif edad > 70 and estiloVida=="Sedentaria":
        mensaje = "Debería ir al médico"
    elif peso > 74.4 and edad > 50:
        mensaje = "Debería ir al médico"
    else:
        mensaje = "No es urgente que acuda al médico si no tiene problemas de salud"
    return mensaje

"""
Estos son los casos de prueba para comprobar los valores de la estructura lógica
print("S, 71a, 15k " +giveMeMyHealthStatus("Sedentaria", 71, 15))
print("S, 71a, 15k " +giveMeMyHealthStatus("Sedentaria", 71, 115))
print("S, 71a, 15k " +giveMeMyHealthStatus("Sedentaria", 70, 115))
print("S, 71a, 15k " +giveMeMyHealthStatus("Sedentaria", 70, 85))
print("S, 71a, 15k " +giveMeMyHealthStatus("Sedentaria", 70, 72))
"""

healthCheck()