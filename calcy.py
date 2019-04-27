from tkinter import *
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("")

top = Frame(root, width = 1600, height = 200)
top.pack(side = TOP)

right= Frame(root, width = 300, height = 800,padx=5,pady=5)
right.place(x=600,y=200)


label_info = Label(top, font = ('Helvetica',50), text ="CALCULATOR", fg = "white",bg="black", bd = 10)
label_info.grid(row = 0, column = 0)
local_time = time.asctime(time.localtime(time.time()))

label_info = Label(top, font = ('algerian',20), text = local_time, fg = "steel blue", bd = 15)
label_info.grid(row = 2, column = 0)
operator=""
inp=StringVar()


def click(x):
    global operator
    operator=operator+str(x)
    inp.set(operator)
    
    
def clear1():
    global operator 
    operator = ""
    inp.set(operator)
    
def calculate():
	global operator
	try:
		sumup = str(eval(operator))
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		sumup = 0
		clear1()
	inp.set(sumup)
	operator = ""


e1 = Entry(right, font = ('algerian',20,'bold'),insertwidth=4,textvariable=inp,bd = 15,fg="blue" ,bg = "white")
e1.grid(columnspan=4)

btn7 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="7", bg="grey",command=lambda:click(7))
btn7.grid(row=1, column= 0)

btn8 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="8", bg="grey",command=lambda:click(8))
btn8.grid(row= 1, column= 1)

btn9 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="9", bg="grey",command=lambda:click(9))
btn9.grid(row=1, column= 2)

plus = Button(right, padx= 16, pady=16, bd= 7, fg= "black", font= ('arial',20,'bold'), text="+", bg="grey",command=lambda:click("+"))
plus.grid(row= 1, column= 3)

btn4 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="4", bg="grey",command=lambda:click(4))
btn4.grid(row=2, column= 0)

btn5 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="5", bg="grey",command=lambda:click(5))
btn5.grid(row= 2, column= 1)

btn6 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="6", bg="grey",command=lambda:click(6))
btn6.grid(row= 2, column= 2)

minus = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="-", bg="grey",command=lambda:click('-'))
minus.grid(row= 2, column= 3)

btn1 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="1", bg="grey",command=lambda:click(1))
btn1.grid(row=3, column= 0)

btn2 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="2", bg="grey",command=lambda:click(2))
btn2.grid(row= 3, column= 1)

btn3 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="3", bg="grey",command=lambda:click(3))
btn3.grid(row= 3, column= 2)

multiply = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="*", bg="grey",command=lambda:click('*'))
multiply.grid(row= 3, column= 3)

btn0 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="0", bg="grey",command=lambda:click(0))
btn0.grid(row= 4, column= 0)

btn_clear = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="C", bg="grey",command=clear1)
btn_clear.grid(row= 4, column= 1)

btn_equal = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="=", bg="grey",command=calculate)
btn_equal.grid(row= 4, column= 2)

division = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="/", bg="grey",command=lambda:click('/'))
division.grid(row= 4, column= 3) 

root.mainloop()
