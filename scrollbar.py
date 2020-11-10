from tkinter import*

top = Tk()
#top.geometry("200x100")

sb = Scrollbar(top)
sb.pack(side = RIGHT,fill=Y)

mylist = Listbox(top,yscrollcommand=sb.set)

for i in range(30):
    mylist.insert(END,"Number"+str(i))
mylist.pack(side=LEFT)
sb.config(command = mylist.yview)
top.mainloop()
