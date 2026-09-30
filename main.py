from tkinter import *
def press(key):
    global expr
    expr+=str(key)
    display.set(expr)
def clear():
    global expr
    expr=""
    display.set("")
def equals():
    global expr
    try:
        result=str(eval(expr))
        display.set(result)
        expr=result
    except:
        display.set("error")
        expr=""
def show():
    label.config(text=opt.get())
expr=""
root =Tk()
root.configure(bg="black")
root.title("Simple calculator")
root.geometry("380x370")
display = StringVar()
entry= Entry(root, textvariable=display,font='Courier')
entry.grid(columnspan=5,ipadx=100,ipady=20)
label=Label(root, text=" ")
btn1=Button(root,text='1', fg='white',font='Courier', bg='black', command=lambda: press('1'), height=4, width=9)
btn1.grid(row=1,column=0)
btn2=Button(root,text='2', fg='white',font='Courier', bg='black', command=lambda: press('2'), height=4, width=9)
btn2.grid(row=1,column=1)
btn3=Button(root,text='3', fg='white',font='Courier', bg='black', command=lambda: press('3'), height=4, width=9)
btn3.grid(row=1,column=2)
btn4=Button(root,text='4', fg='white',font='Courier', bg='black', command=lambda: press('4'), height=4, width=9)
btn4.grid(row=2,column=0)
btn5=Button(root,text='5', fg='white',font='Courier', bg='black', command=lambda: press('5'), height=4, width=9)
btn5.grid(row=2,column=1)
btn6=Button(root,text='6', fg='white',font='Courier', bg='black', command=lambda: press('6'), height=4, width=9)
btn6.grid(row=2,column=2)
btn7=Button(root,text='7', fg='white',font='Courier', bg='black', command=lambda: press('7'), height=4, width=9)
btn7.grid(row=3,column=0)
btn8=Button(root,text='8', fg='white',font='Courier', bg='black', command=lambda: press('8'), height=4, width=9)
btn8.grid(row=3,column=1)
btn9=Button(root,text='9', fg='white',font='Courier', bg='black', command=lambda: press('9'), height=4, width=9)
btn9.grid(row=3,column=2)
btn0=Button(root,text='0', fg='white',font='Courier', bg='black', command=lambda: press('0'), height=4, width=9)
btn0.grid(row=4,column=1)
plus=Button(root,text='+', fg='white',font='Courier', bg='black', command=lambda: press('+'), height=4, width=9)
plus.grid(row=2,column=4)
minus=Button(root,text='-', fg='white',font='Courier', bg='black', command=lambda: press('-'), height=4, width=9)
minus.grid(row=3,column=4)
divide=Button(root,text='/', fg='white',font='Courier', bg='black', command=lambda: press('/'), height=4, width=9)
divide.grid(row=4,column=4)
multiply=Button(root,text='*', fg='white',font='Courier', bg='black', command=lambda: press('*'), height=4, width=9)
multiply.grid(row=4,column=2)
clr=Button(root, text='Clear', fg='lightblue',font='Courier', bg='black', command=clear, height=4, width=9)
clr.grid(row=4, column=0)
eql=Button(root, text='=', fg='lightblue',font='Courier', bg='black', command=equals, height=4, width=9)
eql.grid(row=1, column=4)
root.mainloop()