import tkinter as tk
from tkinter import *
def click(event):
    global strvalue
    text=event.widget.cget("text")
    if text == "=":
        if strvalue.get().isdigit():
            value=int(strvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value="Math Error"
        strvalue.set(value)
        screen.update()
    elif text == "C":
        strvalue.set("")
        screen.update()
    elif text == "Back":
        current_value = strvalue.get()
        if current_value:
            strvalue.set(current_value[:-1])
        screen.update()
    else:
        strvalue.set(strvalue.get() + text)
        screen.update()

root=tk.Tk()
root.geometry("330x710")
root.configure(bg="light grey")
root.maxsize(330,710)
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")
#----Display-------
strvalue=StringVar()
strvalue.set("")
screen= Entry(root, textvar=strvalue,bg="light yellow",
              fg="black",font= "lucida 35 bold")
screen.pack(fill=X, ipadx=8, padx=10,pady=10)
#-----Buttons------
def buttons(b,x,y):
    f= Frame(root)
    for i in b:
        button = tk.Button(f, text=str(i), bg="yellow",fg="black",
                           font="lucida 25 bold",
                           padx=20,pady=23,
                           borderwidth=2,
                           relief="sunken")
        button.pack(side=RIGHT,padx=x,pady=y)
        button.bind("<Button-1>", click)
    f.pack(anchor="nw")

b1=["/","Back","C"]
x1=4
y1=10
buttons(b1,x1,y1) 
b2=["9","8","7"]
x2=10
y2=10
buttons(b2,x2,y2)
b3=["6","5","4"]
x3=9.5
y3=10
buttons(b3,x3,y3)
b4=["3","2","1"]
x4=10.5
y4=10
buttons(b4,x4,y4)
b5=["*","-","+"]
x5=11.5
y5=10
buttons(b5,x5,y5)
b6=["=",".","0"]
x6=11.5
y6=10
buttons(b6,x6,y6)

root.mainloop()
