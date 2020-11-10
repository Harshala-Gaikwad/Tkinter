from tkinter import *

top = Tk()
top.geometry("200x200")

lbl = Label(top,text = "A list of favourite countries....").pack()

listbox = Listbox(top)
listbox.insert(1,"India")
listbox.insert(2,"USA")
listbox.insert(3,"Japan")
listbox.insert(4,"Australia")
listbox.pack()
top.mainloop()
