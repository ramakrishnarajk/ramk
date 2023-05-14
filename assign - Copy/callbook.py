from tkinter import *

def pi():
    print("hai")
btn =[]
t = Tk()
t.geometry('500x200')

btn.append(Button(t , text = 'click me!' ,command = pi))
btn[0].pack()

t.mainloop()
