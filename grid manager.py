from tkinter import *

window = Tk()
window.title("The Grid Manager")
window.geometry("400x300+20+10")
class MyWindow:
    def __init__(self,window):
        self.txt1 = Entry(window,justify="center")
        self.txt1.grid(row=0,column=0,padx=2,pady=2)
        self.txt1.insert(0,"row 0, column 0")
        self.txt2 = Entry(window,justify="center")
        self.txt2.grid(row=0,column=1,padx=2,pady=2)
        self.txt2.insert(0,"row 0, column 1")
        self.txt3 = Entry(window,justify='center')
        self.txt3.grid(row=0, column=2, padx=2,pady=2)
        self.txt3.insert(0,"row 0, column 2")
        self.txt4 = Entry(window,justify='center')
        self.txt4.grid(row=1, column=0, padx=2,pady=2)
        self.txt4.insert(0,"row 1, column 0")
        self.txt5 = Entry(window,justify='center')
        self.txt5.grid(row=1, column=1, padx=2,pady=2)
        self.txt5.insert(0,"row 1, column 1")
        self.txt6 = Entry(window,justify='center')
        self.txt6.grid(row=1, column=2, padx=2,pady=2)
        self.txt6.insert(0,"row 1, column 2")

        self.txt7 = Entry(window,justify='center')
        self.txt7.grid(row=2, column=0, padx=2,pady=2)
        self.txt7.insert(0,"row 2, column 0")
        self.txt8 = Entry(window,justify='center')
        self.txt8.grid(row=2, column=1, padx=2,pady=2)
        self.txt8.insert(0,"row 2, column ")
        self.txt9 = Entry(window,justify='center')
        self.txt9.grid(row=2, column=2, padx=2,pady=2)
        self.txt9.insert(0,"row 2, column 2")

#calculator
        self.lbl1=Label(window,text="Enter the 1st number:")
        self.lbl1.grid(row=4,column=0,sticky=W)
        self.txt10 = Entry(window)
        self.txt10.grid(row=4, column=1, padx=2,pady=2)
        self.lbl2 = Label(window,text="Enter the 2nd number:")
        self.lbl2.grid(row=5,column=0,sticky=W)
        self.txt11=Entry(window)
        self.txt11.grid(row=5,column=1)

        self.lbl3 = Label(window,text="Choose the operator:",font=('Arial',10))
        self.lbl3.grid(row=6,column=0)

        self.btn1 = Button(window,text="Add")
        self.btn1.grid(row=6, column=1,pady=2)
        self.btn1.bind('<Button-1>',self.add)
        self.btn2 = Button(window,text="Subtract")
        self.btn2.grid(row=7, column=1,pady=2)
        self.btn2.bind('<Button-1>', self.sub)
        self.btn3 = Button(window,text="Multiply")
        self.btn3.grid(row=6, column=2,pady=2)
        self.btn3.bind('<Button-1>', self.mul)
        self.btn4 = Button(window,text="Divide")
        self.btn4.grid(row=7, column=2,pady=2)
        self.btn4.bind('<Button-1>', self.div)
        self.lbl4 = Label(window,text="Results",font=('Arial',10))
        self.lbl4.grid(row=8,column=0,sticky=E)
        self.txt12=Entry(window)
        self.txt12.grid(row=8,column=1)
    def add(self,event):
        self.txt12.delete(0,END)
        num1=int(self.txt10.get())
        num2=int(self.txt11.get())
        answer=num1+num2
        self.txt12.insert(END,str(answer))
    def sub(self,event):
        self.txt12.delete(0,END)
        num1=int(self.txt10.get())
        num2=int(self.txt11.get())
        answer=num1-num2
        self.txt12.insert(END,str(answer))
    def mul(self,event):
        self.txt12.delete(0,END)
        num1=int(self.txt10.get())
        num2=int(self.txt11.get())
        answer=num1*num2
        self.txt12.insert(END,str(answer))
    def div(self,event):
        self.txt12.delete(0,END)
        num1=int(self.txt10.get())
        num2=int(self.txt11.get())
        answer=num1/num2
        self.txt12.insert(END,str(answer))
mywin = MyWindow(window)
window.mainloop()

