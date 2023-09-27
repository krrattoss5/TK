from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Windows')

def open():
  img = ImageTk.PhotoImage(Image.open('1.jpg'))
  top = Toplevel()
  top.title('Nueva ventana')
  l = Label(top,text='soy una nueva ventana').pack()
  l2 = Label(top,image=img).pack()
  top.mainloop()

# def open():
#   # global img
#   img = ImageTk.PhotoImage(Image.open('1.jpg'))
#   top = Toplevel()
#   top.title('Nueva ventana')
#   l = Label(top,text='soy una nueva ventana').pack()
#   l2 = Label(top,image=img).pack()

# def open(img):
#   top = Toplevel()
#   top.title('Nueva ventana')
#   l = Label(top,text='soy una nueva ventana').pack()
#   l2 = Label(top,image=img).pack()

#   img = ImageTk.PhotoImage(Image.open('1.jpg'))

#btn = Button(root,text='click',command=lambda: open(img)).pack()

btn = Button(root,text='click',command=open).pack()

root.mainloop()