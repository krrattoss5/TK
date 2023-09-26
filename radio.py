from tkinter import *

root = Tk()
root.title('Radio')

r = IntVar()
r.set('2')

CHANCHITOS = [
  ('Feliz', 'Feliz'),
  ('Triste', 'Triste'),
  ('Amargado', 'Amargado'),
  ('Wolfgang', 'Wolfgang')
]

chanchito = StringVar()
chanchito.set('Wolfgang')

for text, chancho in CHANCHITOS:
  Radiobutton(root,text=text,variable=chanchito,value=chancho).pack()

#Radiobutton(root,text='option 1', variable=r, value=1).pack()
#Radiobutton(root,text='option 2', variable=r, value=2).pack()

Label(root, textvariable=chanchito).pack()

root.mainloop()