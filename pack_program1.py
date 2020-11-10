from tkinter import *
parent = Tk()
# Code to add widgets will go here...
redbutton = Button(parent,text="RED",fg="red")
redbutton.pack(side=LEFT)
redbutton = Button(parent,text="BLACK",fg="black")
redbutton.pack(side=RIGHT)
redbutton = Button(parent,text="BLUE",fg="blue")
redbutton.pack(side=TOP)
redbutton = Button(parent,text="GREEN",fg="green")
redbutton.pack(side=BOTTOM)
parent.mainloop()
