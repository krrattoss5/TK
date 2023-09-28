from tkinter import *

root = Tk()
root.title('Checkbox')
root.geometry('500x500')

var = StringVar()
c = Checkbutton(root,text='soy un checkbutton',variable=var,onvalue='si',offvalue='chanchito feliz')
c.pack()

def mostrar():
  l = Label(root,text=var.get())
  l.pack()

btn = Button(root,text='click',command=mostrar)
btn.pack()

root.mainloop()