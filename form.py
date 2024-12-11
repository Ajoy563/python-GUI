import tkinter as tk
from tkinter import *
from tkinter import messagebox
import openpyxl
import os

root=tk.Tk()
root.geometry("1400x800")
root.configure(bg="light grey")
l=Label(root, text="Student Details",
        font="lucida 55 bold",bg="light grey", fg="black")
l.grid(row=0, column=0, columnspan=3, pady=20)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
#Student name
name=Label(root, text="Student Name", 
           font="lucida 25 bold",bg="light grey", fg="black")
name.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
nameentry=Entry(root)
nameentry.grid(row=2, column=0, padx=10, pady=20)

#parent's name
pname=Label(root, text="Parent's Name",
            font="lucida 25 bold",bg="light grey", fg="black")
pname.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
pnameentry=Entry(root)
pnameentry.grid(row=2, column=1, padx=10, pady=20)

#Address
add=Label(root, text="Address", 
          font="lucida 25 bold",bg="light grey", fg="black")
add.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
addentry=Entry(root)
addentry.grid(row=2, column=2, padx=10, pady=20, ipadx=25)

#10th Marks
x=Label(root, text="10th Marks",
        font="lucida 25 bold",bg="light grey", fg="black")
x.grid(row=3, column=0, padx=10, pady=10)
xentry=Entry(root)
xentry.grid(row=4, column=0, padx=10, pady=20)

#12th marks
xii=Label(root, text="12th Marks", 
          font="lucida 25 bold",bg="light grey", fg="black")
xii.grid(row=3, column=1, padx=10, pady=10)
xiientry=Entry(root)
xiientry.grid(row=4, column=1, padx=10, pady=20)

#DOB
dob=Label(root, text="Date of Brith", 
          font="lucida 25 bold",bg="light grey", fg="black")
dob.grid(row=3, column=2, padx=10, pady=10)
dobentry=Entry(root)
dobentry.grid(row=4, column=2, padx=10, pady=20)

#Gender
v = IntVar()
g = ["Male", "Female", "Others"]

def choice():
    selected_gender = g[v.get() - 1]
    genderentry.delete(0, END)
    genderentry.insert(0, selected_gender)

gender = Label(root, text="Gender", font="lucida 25 bold", bg="light grey", fg="black")
gender.grid(row=5, column=0, padx=10, pady=10)

gender_frame = Frame(root, bg="light grey")
gender_frame.grid(row=6, column=0, padx=10, pady=10)

tk.Radiobutton(gender_frame, text=g[0], bg="light grey", fg="black", padx=20, variable=v, value=1, command=choice).pack(anchor="w", pady=5)
tk.Radiobutton(gender_frame, text=g[1], bg="light grey", fg="black", padx=20, variable=v, value=2, command=choice).pack(anchor="w", pady=5)
tk.Radiobutton(gender_frame, text=g[2], bg="light grey", fg="black", padx=20, variable=v, value=3, command=choice).pack(anchor="w", pady=5)

genderentry = Entry(root, textvariable="male")
genderentry.grid(row=7, column=0, padx=10, pady=20)

#Department
debt=Label(root, text="Department", 
          font="lucida 25 bold",bg="light grey", fg="black")
debt.grid(row=5, column=2, padx=10, pady=10)
deptentry=Entry(root)
deptentry.grid(row=6, column=2, padx=10, pady=10,ipadx=25)

#Submit Button
def submit():
    filepath="/Users/ajoydas/Desktop/form/data.xlsx"
    if not os.path.exists(filepath):
        workbook=openpyxl.Workbook()
        sheet=workbook.active
        heading=["Student's Name","Parent's Name","Address","10th Marks","12th Marks","DOB","Gender","Department"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook=openpyxl.load_workbook(filepath)
    sheet=workbook.active
    sheet.append([nameentry.get(),pnameentry.get(),addentry.get(),xentry.get(),xiientry.get(),dobentry.get(),genderentry.get(),deptentry.get()])
    workbook.save(filepath)

    nameentry.delete(0, END)
    pnameentry.delete(0, END)
    addentry.delete(0, END)
    xentry.delete(0, END)
    xiientry.delete(0, END)
    dobentry.delete(0, END)
    genderentry.delete(0, END)
    deptentry.delete(0, END)

    messagebox.showinfo("Information", "Submitted!!")
Button(root, text="Submit",font="lucida 45 bold",bg="light grey", fg="black",command=submit).grid(row=12,column=1, padx=10, pady=10)

root.mainloop()