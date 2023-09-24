from tkinter import * #importar todo

root = Tk() #crear app
root.title('Hola mundo') #titulo de la ventana
root.geometry('200x400') #tamaños por defecto ancho y alto

#variable|  instancia(lugar donde se muestra, y lo que se quiere mostrar)
l1 = Label(root, text='Hola!.')
l2 = Label(root, text='Chao.')

l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
# label.pack() # aquidecimos que se puede mostrar

root.mainloop() #instruccion que queda escuchando la app y sus cambios