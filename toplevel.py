from tkinter import*

top = Tk()
top.title("TOPLEVEL")
top.geometry("200x200")
def open():
    toplevel = Toplevel(top)
    toplevel.mainloop()
btn = Button(top,text = "open",command=open)
btn.pack(anchor=CENTER)
top.mainloop()
