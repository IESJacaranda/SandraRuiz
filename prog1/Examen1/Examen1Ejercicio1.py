import time
print("Bienvenido/a al Gimnasio Jacafitness")
time.sleep(1)
dia = input("Que dia le interesa venir?")
hora = int(input("A que hora le interesa venir?"))
if dia == "Lunes" or dia == "Miercoles" or dia == "Jueves":
    if hora >= 12 and hora<=14:
        print("Puede asistir a Spinning de 12 a 14")
    elif hora>=16 and hora<=20:
        print("Puede asistir a Yoga de 16 a 20")
    elif hora>=20 and hora<=22:
        print("Puede asistir a Body Combat de 20 a 22")
elif dia == "Martes" or dia == "Viernes":
    if hora >= 12 and hora<=14:
        print("Puede asistir a Yoga de 12 a 14")
    elif hora>=16 and hora<=20:
        print("Puede asistir a Spinning de 16 a 20")
    elif hora>=20 and hora<=22:
        print("Puede asistir a Body Combat de 20 a 22")
else:
    print("Lo sentimos, en dicho día y horario no se imparten clases")