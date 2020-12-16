import pyautogui
import time

mensaje = "Ya quiero ir a dormir"
n= 20

time.sleep(5)

for i in range(n):
    pyautogui.typewrite(mensaje + "\n")
    #time.sleep(1)
