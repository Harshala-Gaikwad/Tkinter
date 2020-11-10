from tkinter import *

top = Tk()
top.geometry("200x200")
chkvar1 = IntVar()
chkvar2 = IntVar()
chkvar3 = IntVar()
ckhbtn1 = Checkbutton(top,text='C',variable=chkvar1,onvalue=1,offvalue=0,height=2,width=10).pack()
ckhbtn2 = Checkbutton(top,text='C++',variable=chkvar2,onvalue=1,offvalue=0,height=2,width=10).pack()
ckhbtn3 = Checkbutton(top,text='JAVA',variable=chkvar3,onvalue=1,offvalue=0,height=2,width=10).pack()


top.mainloop()
