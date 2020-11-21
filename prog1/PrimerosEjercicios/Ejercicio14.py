numero = int(input("¿Para qué número quieres calcular la tabla de multiplicar?"))
import time
segundo = int(input("¿Desde qué segundo quieres hacer una cuenta a trás?"))
for i in range(segundo):
    print(segundo-i)
    time.sleep(1)