from tkinter import *
from time import strftime
from tkinter import font as f
import random

def colgen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour1 = f'#{r:02x}{g:02x}{b:02x}'
    return colour1

def timeF():
    timeN = strftime(" %H:%M:%S %Z ")
    colour1 = colgen()
    colour2 = colgen()

    clock.config(text=timeN,background=colour1,foreground=colour2)
    clock.after(1000,timeF)

main = Tk()
main.title("Clock")
FONT = f.Font(family="calibri",weight="bold",size=30)
FONTs = f.Font(family="calibri",weight="bold",size=18)

mdc = Label(main,font=FONTs,text="My Digital Clock")
mdc.pack()
clock = Label(main,font=FONT,background="red",foreground="white")
clock.pack(padx=10,pady=10)
timeF()


main.mainloop()