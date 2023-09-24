from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola Mundo!')

def click1():
  messagebox.showwarning('PopUp','Hola Warning!')

def click2():
  messagebox.showerror('PopUp','Hola Error!')

def click3():
  messagebox.showinfo('PopUp','Hola Info!')

def click4():
  repuesta = messagebox.askquestion('PopUp','Hola Pregunta!')
  if repuesta == 'yes':
    messagebox.showinfo('PopUp','La res puesta es ' + repuesta)
  else:
    messagebox.showinfo('PopUp','La res puesta es ' + repuesta)

def click5():
  res = messagebox.askokcancel('PopUp','Cancel?')
  if res:
    messagebox.showinfo('PopUp','La res puesta es ok')
  else:
    messagebox.showinfo('PopUp','La res puesta es cancel')



Button(root, text='presioname',command=click1).pack()

Button(root, text='presioname',command=click2).pack()

Button(root, text='presioname',command=click3).pack()

Button(root, text='presioname',command=click4).pack()

Button(root, text='presioname',command=click5).pack()

root.mainloop()