from tkinter import *
# pip install Pillow
from PIL import ImageTk,Image
root = Tk('Hola Mundo!')

#image = Image.open('imagen.png')
#image.show()

img = ImageTk.PhotoImage(Image.open('imagen.png'))
l = Label(image=img)
l.pack()

root.mainloop()