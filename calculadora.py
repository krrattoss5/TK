from tkinter import *

root = Tk()
root.title('Calculadora de Didier')
root.configure(background='#333333')
root.geometry('130x168')

equation = StringVar()

def press(num):
  equation.set(equation.get() + str(num))

def equalpress():
  try:
    total = str(eval(equation.get()))
    equation.set(total)
  except:
    equation.set('ERROR')

def clearpress():
  equation.set('')

expresion_entry = Entry(root,textvariable=equation)
expresion_entry.grid(row=0,columnspan=4,sticky='nswe')

btn7 = Button(root,text=' 7 ',fg='#fff',background='#666',command=lambda: press(7)).grid(row=1,column=0,sticky='nswe')

btn8 = Button(root,text=' 8 ',fg='#fff',background='#666',command=lambda: press(8)).grid(row=1,column=1,sticky='nswe')

btn9 = Button(root,text=' 9 ',fg='#fff',background='#666',command=lambda: press(9)).grid(row=1,column=2,sticky='nswe')

btn4 = Button(root,text=' 4 ',fg='#fff',background='#666',command=lambda: press(4)).grid(row=2,column=0,sticky='nswe')

btn5 = Button(root,text=' 5 ',fg='#fff',background='#666',command=lambda: press(5)).grid(row=2,column=1,sticky='nswe')

btn6 = Button(root,text=' 6 ',fg='#fff',background='#666',command=lambda: press(6)).grid(row=2,column=2,sticky='nswe')

btn1 = Button(root,text=' 1 ',fg='#fff',background='#666',command=lambda: press(1)).grid(row=3,column=0,sticky='nswe')

btn2 = Button(root,text=' 2 ',fg='#fff',background='#666',command=lambda: press(2)).grid(row=3,column=1,sticky='nswe')

btn3 = Button(root,text=' 3 ',fg='#fff',background='#666',command=lambda: press(3)).grid(row=3,column=2,sticky='nswe')

btn0 = Button(root,text=' 0 ',fg='#fff',background='#666',command=lambda: press(0)).grid(row=4,column=0,columnspan=2,sticky='nswe')

btnDec = Button(root,text=' ▪️ ',fg='#fff',background='#666',command=lambda: press('.')).grid(row=4,column=2,columnspan=2,sticky='nswe')

plus = Button(root,text=' + ',fg='#fff',background='#fe9727',command=lambda: press('+')).grid(row=1,column=3,sticky='nswe')

minus = Button(root,text=' - ',fg='#fff',background='#fe9727',command=lambda: press('-')).grid(row=2,column=3,sticky='nswe')

multiply = Button(root,text=' * ',fg='#fff',background='#fe9727',command=lambda: press('*')).grid(row=3,column=3,sticky='nswe')

divide = Button(root,text=' / ',fg='#fff',background='#fe9727',command=lambda: press('/')).grid(row=4,column=3,sticky='nswe')

equal = Button(root,text=' = ',fg='#fff',background='#fe9727',command=equalpress).grid(row=5,column=3,sticky='nswe')

clear = Button(root,text=' CLEAR ',fg='#fff',background='#999999',command=clearpress).grid(row=5,column=0,columnspan=3,sticky='nswe')

root.mainloop()