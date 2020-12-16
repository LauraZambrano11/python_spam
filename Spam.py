import pyautogui
import time

mensaje = "Este mensaje se puede modificar" #Mensaje a imprimir
n= 20 #Número de repeticiones

time.sleep(5) #Tiempo de espera antes de iniciar la ejecución

for i in range(n):
    pyautogui.typewrite(mensaje + "\n") #Impresión
    #time.sleep(1)  #tiempo entre envío de mensajes, si se quita no hay espera y se envía seguido
