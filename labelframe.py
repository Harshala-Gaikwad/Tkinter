from tkinter import*

top = Tk()
top.geometry("300x200")

lframe1 = LabelFrame(top,text="Positive Comments")
lframe1.pack(fill="both",expand=1)

toplabel = Label(lframe1,text="Place to put the positive comments")
toplabel.pack()

lframe1 = LabelFrame(top,text="Negative Comments")
lframe1.pack(fill="both",expand=1)

toplabel = Label(lframe1,text="Place to put the negative comments")
toplabel.pack()

top.mainloop()
