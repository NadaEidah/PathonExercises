#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:24:18 2019

@author: nada
"""

#Exercises DAY Eleven 
print('--------Exercise 1--------------')

from tkinter import *
def ex1 ():
    if value1.get() == "Orange" and value2.get() == "CodingAcademy" :
        y = messagebox.showinfo("Login", "Successful login")
        if y == "ok":
            root.destroy()
    else:
        messagebox.showinfo("Login", "Wrong User Name or Password")
root = Tk()
value1 = StringVar()
value2 = StringVar()

name = Label(root, text = "Name").grid(row=0, column = 0)

e1 = Entry(root, textvariable= value1).grid(row = 0, column =1)

password = Label(root, text ="Password").grid(row = 1, column = 0)

e2 = Entry(root, textvariable= value2).grid(row = 1, column =1)

submit = Button(root, text="Submit", command= ex1).grid(row = 4, column = 0)

root.mainloop()




print('--------Exercise 2--------------')

from tkinter import *
from tkinter import messagebox 
from tkinter import scrolledtext

root=Tk()
def masages1():
    messagebox.showinfo("","This is a message")
  
def masages2():
    
    root2 = Toplevel(root)
    
    labNumber = Label(root2,text="Emp Number").grid(row=0,column=0)
    
    inputNumber=Entry(root2).grid(row=0,column=1)
    
    labName = Label(root2,text="Emp Name").grid(row=1,column=0)
    
    inputName=Entry(root2).grid(row=1,column=1)
    
    btnExit=Button(root2,text="Exit",command=lambda : root2.destroy()).grid(row=2,column=0)
    
def masages3():
    root2 = Toplevel(root)
    labNumber = Label(root2,text="on console").grid(row=0,column=0)
    for a in range(19):
        print('The count is '+str(a))
    
    
b1=Button(root,text='open message',command=masages1)
b2=Button(root,text='open message child 1',command=masages2)
b3=Button(root,text='open message child 2',command=masages3)

b1.pack()
b2.pack()
b3.pack()

root.mainloop()

print('--------Exercise 3--------------')

from tkinter import *
from tkinter.colorchooser import *
win=Tk()

def getColor():
    color=askcolor()
    print(color)
    win.configure(background=color[1])
foo=Button(text="select color", command=getColor)
foo.pack()
win.mainloop()



