from tkinter import*
from math import*
from tkinter import Tk

manslogs=Tk()
manslogs.title("kaka.parasts")


def btnClick(number):
    Current=E.get() #nolasa E saturu
    E.delete(0, END) # nodzēs visu E lodzinā no 0 līdz end
    newNumber= str(Current) + str(number)
    E.insert(0, newNumber) # ievieto no 0 lidz newnumber
    return 0

def btnCommand(command):
    global number
    global mathOp
    global num1
    global num2
    mathOp=command
    num1 = (float(E.get()))
    E.delete(0, END)
    return 0


def Vienads():
    global num2
    num2=(float(E.get()))
    result=0
    if mathOp=="+":
        result=num1 + num2
    elif mathOp=="-":
        result=num1 - num2
    elif mathOp=="*":
        result=num1 * num2
    elif mathOp=="/":
        result=num1 / num2

    else:
        result = 0
    E.delete(0,END)
    E.insert(0,str(result))
    return 0 




btn0 = Button(manslogs, text="0", padx="40", pady="20", bd= 3, command=lambda:btnClick(0))
btn1 = Button(manslogs, text="1", padx="40", pady="20", bd= 3, command=lambda:btnClick(1))
btn2 = Button(manslogs, text="2", padx="40", pady="20", bd= 3, command=lambda:btnClick(2))
btn3 = Button(manslogs, text="3", padx="40", pady="20", bd= 3, command=lambda:btnClick(3))
btn4 = Button(manslogs, text="4", padx="40", pady="20", bd= 3, command=lambda:btnClick(4))
btn5 = Button(manslogs, text="5", padx="40", pady="20", bd= 3, command=lambda:btnClick(5))
btn6 = Button(manslogs, text="6", padx="40", pady="20", bd= 3, command=lambda:btnClick(6))
btn7 = Button(manslogs, text="7", padx="40", pady="20", bd= 3, command=lambda:btnClick(7))
btn8 = Button(manslogs, text="8", padx="40", pady="20", bd= 3, command=lambda:btnClick(8))
btn9 = Button(manslogs, text="9", padx="40", pady="20", bd= 3, command=lambda:btnClick(9))


btnSum = Button(manslogs, text= '+', padx="40", pady="20", bd= 3, command=lambda:btnCommand("+"))
btnMin = Button(manslogs, text= '-', padx="40", pady="20", bd= 3, command=lambda:btnCommand("-"))
btnTim = Button(manslogs, text= '*', padx="40", pady="20", bd= 3, command=lambda:btnCommand("*"))
btnDiv = Button(manslogs, text= '/', padx="40", pady="20", bd= 3, command=lambda:btnCommand("/"))
btnEquel = Button(manslogs, text= '=', padx="40", pady="20", bd= 3, command=Vienads)
btnCom = Button(manslogs, text= '.', padx="40", pady="20", bd= 3)
btnClear = Button(manslogs, text= 'c', padx="40", pady="20", bd= 3)
btnMinFy = Button(manslogs, text= '-( )', padx="40", pady="20", bd= 3)
btnWallL = Button(manslogs, text= '(', padx="40", pady="20", bd= 3)
btnWallR = Button(manslogs, text= ')', padx="40", pady="20", bd= 3)
btnSquer = Button(manslogs, text= '^2', padx="40", pady="20", bd= 3)
btnSquerRoot = Button(manslogs, text= '^0.5', padx="40", pady="20", bd= 3)


btn0.grid(row=5, column= 2)
btn1.grid(row=4, column= 1)
btn2.grid(row=4, column= 2)
btn3.grid(row=4, column= 3)
btn4.grid(row=3, column= 1)
btn5.grid(row=3, column= 2)
btn6.grid(row=3, column= 3)
btn7.grid(row=2, column= 1)
btn8.grid(row=2, column= 2)
btn9.grid(row=2, column= 3)


btnSum.grid(row=4, column= 4)
btnMin.grid(row=3, column= 4)
btnTim.grid(row=2, column= 4)
btnDiv.grid(row=1, column= 4)
btnEquel.grid(row=5, column= 4)
btnCom.grid(row=5, column= 3)
btnClear.grid(row=1, column= 1)
btnMinFy.grid(row=5, column= 1)
btnWallL.grid(row=1, column= 2)
btnWallR.grid(row=1, column= 3)
btnSquer.grid(row=6, column= 1)
btnSquerRoot.grid(row=6, column= 2)

E = Entry(manslogs, width=15, bd= 5, font=("Arial Black", 20))
E.grid(row=0, column=1, columnspan=4)

manslogs.mainloop()