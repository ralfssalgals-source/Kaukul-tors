from tkinter import*
from math import*
from tkinter import Tk

manslogs=Tk()
manslogs.title("kauku.parasts")


def btnClick(number):
    Current=E.get() #nolasa E saturu
    E.delete(0, END) # nodzēš visu E lodziņā no 0 līdz end
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


def Vienads(): # šeit ir  + - * /  funkcija
    global num2
    num2=(float(E.get()))
    result=0
    if mathOp=="+": # ja ir viena no opcijām tad maina rezultātu
        result=num1 + num2
    elif mathOp=="-":
        result=num1 - num2
    elif mathOp=="*":
        result=num1 * num2
    elif mathOp=="/":
        result=num1 / num2

    else:
        result = 0 # ja nav izvēlēta darbība pagaidām atstāj rezultātu 0 
    E.delete(0,END)
    E.insert(0,str(result))
    return 0 


def Clear(): # notīra visu un pārtaisa uz 0
    E.delete(0, END)
    num1 = 0
    num2 = 0
    mathOp =" "
    return 0 
   

def kvad(): # kvadrāts = paaugstina num1 kvadrātā
    global operator
    global num1
    global mathOp
    num1 = (float(E.get())**2) # kvadrātā
    E.delete(0, END)
    E.insert(0, num1)
    return 0 


def kvadratSk(): # atrod kvadrātsakni num1
    global operator
    global num1
    global mathOp
    num1 = (float(E.get()))
    num1 = sqrt(num1) # kvadrātsakne
    E.delete(0, END)
    E.insert(0, num1)
    return 0 


def PlusMin(): # reizina num1 ar -1 . Izskatās -/+
    global operator
    global num1
    global mathOp
    num1 = -(float(E.get())) # reiz -
    E.delete(0, END)
    E.insert(0, num1)
    return 0 


def logy(): # funkcija logoritmam
    global operator
    global mathOp
    global num1
    num1 = (float(E.get()))
    num1=log(num1) # logaritms
    E.delete(0, END)
    E.insert(0, str(num1))
    return 0

# zem šī ir pogas no 0 līdz 9

btn0 = Button(manslogs, text="0", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(0), bg='gray', height= 2, width= 3)
btn1 = Button(manslogs, text="1", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(1), bg='gray', height= 2, width= 3)
btn2 = Button(manslogs, text="2", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(2), bg='gray', height= 2, width= 3)
btn3 = Button(manslogs, text="3", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(3), bg='gray', height= 2, width= 3)
btn4 = Button(manslogs, text="4", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(4), bg='gray', height= 2, width= 3)
btn5 = Button(manslogs, text="5", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(5), bg='gray', height= 2, width= 3)
btn6 = Button(manslogs, text="6", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(6), bg='gray', height= 2, width= 3)
btn7 = Button(manslogs, text="7", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(7), bg='gray', height= 2, width= 3)
btn8 = Button(manslogs, text="8", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(8), bg='gray', height= 2, width= 3)
btn9 = Button(manslogs, text="9", padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnClick(9), bg='gray', height= 2, width= 3)

# zem šī ir visas pogas kuras ir saistītas ar darbībām
btnSum = Button(manslogs, text= '+', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnCommand("+"), bg='light gray', height= 2, width= 3)
btnMin = Button(manslogs, text= '-', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnCommand("-"), bg='light gray', height= 2, width= 3)
btnTim = Button(manslogs, text= '*', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnCommand("*"), bg='light gray', height= 2, width= 3)
btnDiv = Button(manslogs, text= '/', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=lambda:btnCommand("/"), bg='light gray', height= 2, width= 3)
btnEquel = Button(manslogs, text= '=', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=Vienads, bg='dark gray', fg= 'green', height= 2, width= 3)
btnlog = Button(manslogs, text= 'log', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=logy, bg='light gray', height= 2, width= 3)
btnClear = Button(manslogs, text= 'c', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=Clear, bg='dark gray', fg='red', height= 2, width= 3)
btnMinFy = Button(manslogs, text= '+/-', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=PlusMin, bg='light gray', height= 2, width= 3)
btnSquer = Button(manslogs, text= '^2', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=kvad, bg='light gray', height= 2, width= 3)
btnSquerRoot = Button(manslogs, text= '^0.5', padx="40", pady="20", bd= 6, font=("Arial Black", 12), command=kvadratSk, bg='light gray', height= 2, width= 3)

# zem šī ir pogu novietojums 0 - 9
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

# zem šī ir pogu novietojums darbībām
btnSum.grid(row=4, column= 4)
btnMin.grid(row=3, column= 4)
btnTim.grid(row=2, column= 4)
btnDiv.grid(row=1, column= 4)
btnEquel.grid(row=5, column= 4)
btnlog.grid(row=5, column= 3)
btnClear.grid(row=1, column= 1)
btnMinFy.grid(row=5, column= 1)
btnSquer.grid(row=6, column= 1)
btnSquerRoot.grid(row=6, column= 2)


# zem šī ir tas logs kurš parāda darbības un atbildes
E = Entry(manslogs, width=20, bd= 20, font=("Arial Black", 20))
E.grid(row=0, column=1, columnspan=4)

manslogs.mainloop()