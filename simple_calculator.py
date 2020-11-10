from tkinter import *
from functools import partial

def call_result(label_result,n1,n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result = %d" % result) 
    return

root = Tk()
root.geometry("400x200+100+200")

root.title("Calculator")

n1 = StringVar()
n2 = StringVar()

labeln1 = Label(root,text="A").grid(row=1,column=0)
labeln2 = Label(root,text="B").grid(row=2,column=0)

labelresult = Label(root)
labelresult.grid(row=7,column=2)

entryn1 = Entry(root,textvariable = n1).grid(row=1,column=2)
entryn2 = Entry(root,textvariable = n2).grid(row=2,column=2)

call_result = partial(call_result,labelresult,n1,n2)

buttoncal = Button(root,text="Calcuate",command=call_result).grid(row=3,column=0)
root.mainloop() 
