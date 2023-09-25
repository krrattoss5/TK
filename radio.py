from tkinter import *

root = Tk()
root.title('Radio')

r = IntVar()
r.set('2')

Radiobutton(root,text='option 1', variable=r, value=1).pack()
Radiobutton(root,text='option 2', variable=r, value=2).pack()

Label(root, textvariable=r).pack()

root.mainloop()