import random
from gtts import gTTS
import playsound
from tkinter import *
from os import sys
from time import ctime
def sound():
    gu = gTTS(text=f"your password is {password}")
    f="hi2.mp3"
    gu.save(f)
    playsound.playsound(f)
def sound2():
    gu = gTTS(text="welcome in our password geanrating application")
    f = "h1i2.mp3"
    gu.save(f)
    playsound.playsound(f)
sound2()
def passar():
    pass
def passq():
    l6=Label(root,text=f"your passworx is:{password}").pack()


   #lo=Label(root,text=f"Your New Password  is:-{password}")
   #lo.pack()

upp = ['A', 'B', 'C', 'D', 'E']
low = ['a', 'b', 'c', 'd', 'e']
special = ['@', '!', '&', '#', '$']
newmaric = ['1', '2', '3', '4', '5', '6']

password = random.choice(upp) + random.choice(low) + random.choice(special) + random.choice(newmaric)
password=password+password+random.choice(special)
# print(password)
root = Tk()
root.geometry("222x222")
root.title("PASSWORD GENARETOR")
b = Button(text="Genarate Password", command=passq).pack(fill=X)
b2=Button(text="sound",command=sound).pack(fill=X,pady=20)
l8=Label(text=ctime()).pack()
root.mainloop()