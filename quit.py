from tkinter import *

root = Tk()
root.title('quit')

exit = Button(root,text='Salir',command=root.quit)
exit.pack()

root.mainloop()