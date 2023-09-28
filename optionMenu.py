from tkinter import *

root = Tk()
root.title('Option Menu')
root.geometry('500x500')

def enviar():
  l = Label(root,text=value.get())
  l.pack()

value = StringVar()
value.set('Seleccionar')

lista = [
  'Chanchito Feliz',
  'Chanchito Triste',
  'Chanchito Emocionado'
]

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root,text='enviar',command=enviar)
btn.pack()

root.mainloop()