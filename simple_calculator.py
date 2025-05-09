from tkinter import *
import math  
expression = "" 
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 
def equalpress(): 
	try: 
		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
	except: 
		equation.set("error") 
		expression = "" 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 
def sin_button():
	try:
		value = float(expression_field.get())
		result = math.sin(math.radians(value))
		equation.set(str(result))
	except:
		equation.set("error")
def cos_button():
	try:
		value = float(expression_field.get())
		result = math.cos(math.radians(value))
		equation.set(str(result))
	except:
		equation.set(" error ")
def tan_button():
	try:
		value = float(expression_field.get())
		result = math.tan(math.radians(value))
		equation.set(str(result))
	except:
		equation.set("error") 
if __name__ == "__main__": 
	gui = Tk() 
	gui.configure(background="light blue") 
	gui.title("Simple Calculator") 
	gui.geometry("270x360")  
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation) 
	expression_field.grid(columnspan=4, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg='black', bg='white', command=lambda: press(1), height=3, width=7) 
	button1.grid(row=2,column=0) 

	button2 = Button(gui,text='2',fg='black',bg='white', command=lambda: press(2),height=3,width=7) 
	button2.grid(row=2,column=1) 

	button3 = Button(gui,text='3',fg='black',bg='white', command=lambda: press(3),height=3,width=7) 
	button3.grid(row=2,column=2) 

	button4 = Button(gui,text='4', fg='black',bg='white', command=lambda: press(4),height=3,width=7) 
	button4.grid(row=3,column=0) 

	button5 = Button(gui,text='5',fg='black',bg='white', command=lambda: press(5), height=3, width=7) 
	button5.grid(row=3,column=1) 

	button6 = Button(gui,text='6',fg='black', bg='white', command=lambda: press(6),height=3,width=7) 
	button6.grid(row=3,column=2) 

	button7 = Button(gui,text='7', fg='black',bg='white',command=lambda: press(7),height=3,width=7) 
	button7.grid(row=4,column=0) 

	button8 = Button(gui, text='8', fg='black', bg='white',command=lambda: press(8),height=3,width=7) 
	button8.grid(row=4,column=1) 

	button9 = Button(gui, text='9', fg='black', bg='white',command=lambda: press(9), height=3,width=7) 
	button9.grid(row=4,column=2) 

	button0 = Button(gui, text='0', fg='black',bg='white',command=lambda: press(0),height=3,width=7) 
	button0.grid(row=5,column=0) 

	plus = Button(gui, text='+', fg='black',bg='white', command=lambda: press("+"), height=3,width=7) 
	plus.grid(row=2,column=3) 

	minus = Button(gui, text='-', fg='black',bg='white', command=lambda: press("-"), height=3,width=7) 
	minus.grid(row=3,column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=3, width=7) 
	multiply.grid(row=4,column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=3, width=7) 
	divide.grid(row=5,column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='white', command=equalpress, height=3, width=7) 
	equal.grid(row=5,column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='white', command=clear, height=3, width=7) 
	clear.grid(row=5,column=1) 

	Decimal = Button(gui, text='.', fg='black', bg='white', command=lambda: press('.'), height=3,width=7) 
	Decimal.grid(row=6,column=0)

	
sin = Button(gui, text='sin', fg='black', bg='white', command=lambda: press('si'), height=3,width=7)
sin.grid(row=6,column=1)

cos = Button(gui, text='cos', fg='black', bg='white', command=cos_button, height=3, width=7)
cos.grid(row=6, column=2)

tan = Button(gui, text='tan', fg='black', bg='white', command=tan_button, height=3, width=7)
tan.grid(row=6, column=3)

gui.mainloop()
