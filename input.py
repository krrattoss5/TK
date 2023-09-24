from tkinter import *

root = Tk()
root.title('Hola Mundo!')

def click():
  texto = e.get()
  textvariable.set(texto)
  #l = Label(root,text=texto)
  #l.pack()
  e.delete(0,END)
  #l.configure(text=texto)

e = Entry(root,width=40)
e.pack()
e.insert(0,"Ingresar Texto:")

btn = Button(root,text='click',command=click)
btn.pack()

textvariable = StringVar()
l = Label(root,textvariable=textvariable)
l.pack()


root.mainloop()