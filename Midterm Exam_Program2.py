from tkinter import *
from tkinter import ttk
window = Tk()

window.title("Special MidTerm Exam in OOP")
window.geometry("500x400+20+10")

btn = Button(window, text = "Click to Change Color")
btn.place(x= 180, y=170)
btn.config(bg='white')
btn.config(fg='black')
btn.config(activebackground='yellow')

window.mainloop()

