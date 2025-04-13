from tkinter import *
from tkinter.colorchooser import askcolor

def draw(event):
    global eraserOn,col,oldX,oldY
    if eraserOn:
        col = "white"
    if oldX and oldY:
        canvas.create_line(oldX,oldY,event.x,event.y,width=sizescale.get(),fill=col,capstyle="round",smooth=True,splinesteps=50)
    oldX = event.x
    oldY = event.y

def reset(event):
    global oldX,oldY
    oldX=None
    oldY=None

def activateBtn(button,eraserMode=False):
    global active,eraserOn
    active.config(relief="raised")
    active = button
    active.config(relief="sunken")
    eraserOn = eraserMode

def useBrush():
    activateBtn(brush)

def useEraser():
    activateBtn(eraser,True)

def useColour():
    global col
    activateBtn(colour)
    col = askcolor()[1]    
    print(col)
    activateBtn(brush)

main = Tk()
main.title("Paint")

shapes = ["Circle","Rectangle","Line"]
varShapes = shapes[2]
shape = OptionMenu(main,varShapes,*shapes)
shape.grid(row=1,column=0)

brush = Button(main,text="Brush",command=useBrush)
brush.grid(row=1,column=1,pady=10,padx=10)

colour = Button(main,text="Colour",command=useColour)
colour.grid(row=1,column=2)

eraser = Button(main,text="Eraser",command=useEraser)
eraser.grid(row=1,column=3,pady=10,padx=10)

sizescale = Scale(main,from_=1,to=20,orient=HORIZONTAL)
sizescale.grid(row=1,column=4)

canvas = Canvas(main,background="white",width=500,height=500)
canvas.bind("<B1-Motion>",draw)
canvas.bind("<ButtonRelease-1>",reset)
canvas.grid(row=2,column=0,columnspan=5)

#initial setup
oldX = None
oldY = None
col = "black"
width = 3
sizescale.set(width)
active = brush
active.config(relief="sunken")
eraserOn = False


main.mainloop()