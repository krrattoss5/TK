from tkinter import *

root = Tk()
root.title('Sliders')

vertical = Scale(root,from_=0,to=200,command=lambda x: enviar())
vertical.pack()
horizontal = Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizontal.pack()

def enviar():
  hor = horizontal
  ver = vertical.get()
  print(str(hor) + ' ' + str(ver))

btn = Button(root,text='enviar',command=enviar)
btn.pack()

root.mainloop()