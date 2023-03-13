import pyautogui as pg
import time

msg=(input("Enter the message you want to send:" ))
r=int(input("Enter the quantity you want to send: "))

if(r>0):
    time.sleep(5)
    for i in range(r):
         g=msg
         pg.write(g)
         pg.press("enter") 
else:
    print("Please Enter the range value")