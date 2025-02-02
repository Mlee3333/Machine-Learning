from tkinter import *
from tkinter import messagebox
import random
import tkinter.font as f

number =  random.randint(1,20)

def start():
    name = entry1.get()
    messagebox.showinfo("Guess the number",name+", guess a number from 1 to 20: ")
    frame1.tkraise()

def guess():
    num = int(entry2.get())
    if num == number:
        messagebox.showinfo("Correct","WELL DONE!! YOU GUESSED CORRECTLY !!")
    elif num < number:
        messagebox.showinfo("Guess again","Sorry! Too low!")
    elif num > number:
        messagebox.showinfo("Guess again","Sorry! Too high!")
    entry2.delete(0,END)

main = Tk()
main.title("Guess the number")
main.config(background="cyan")
font = f.Font(family="calibri",size=16)
frame1 = Frame(main,background="red",pady=30)
frame1.grid(row=2,column=1,rowspan=3,columnspan=3)
frame = Frame(main,background="cyan",pady=30)
frame.grid(row=2,column=1,rowspan=3,columnspan=3)

lblT = Label(main,text="Guess the Number: ",font=font,foreground="dark blue",background="cyan")
lblT.grid(row=1,column=1,columnspan=3)

lblN = Label(frame,text="Enter your name: ",font=font,foreground="dark blue",background="cyan")
lblN.grid(row=2,column=1,padx=30)

entry1 = Entry(frame,font=font)
entry1.grid(row=2,column=2,padx=10)

btnOk = Button(frame,text="Ok",font=font,command=start)
btnOk.grid(row=3,column=1,columnspan=2,pady=30)

lblE = Label(frame1,text="Enter your guess: ",font=font,foreground="white",background="red")
lblE.grid(row=2,column=1,padx=30)

entry2 = Entry(frame1,font=font)
entry2.grid(row=2,column=2,padx=10)

btnG = Button(frame1,text="Guess",font=font,command=guess)
btnG.grid(row=3,column=1,columnspan=2,pady=30)

main.mainloop()