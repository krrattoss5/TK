from tkinter import *

root = Tk()
root.title('Hola Mundo!')

l = Label(root,text='Hola Mundo!')
def click():
  l.pack()

btn = Button(root, text='Clikeame', command=click, fg='#fff', bg='green')
btn.pack()

root.mainloop()