#importing tkinter module.
from tkinter import *
import tkinter.messagebox
#creating object - window of Tk().
window = Tk()
#providing title to the form.
window.title("Registration page")
#this will make a screen size and color.
window.geometry("900x700")
window.configure(background="lightgreen")

#below five fields are declared
label1 = Label(window, text="Employee Registration Form", font=("bold", 18)).grid(row=0, column=1)
Firstname = Label(window, text = "First Name", width=15, font=("bold", 15)).grid(row=2, column=0)
Lastname = Label(window, text = "Last Name", width=15, font=("bold", 15)).grid(row=3, column=0)
Email = Label(window, text = "Email ID", width=15, font=("bold", 15)).grid(row=4, column=0)
Mobile = Label(window, text = "Contact Number", width=15, font=("bold", 15)).grid(row=5, column=0)
age = Label(window, text = "Age", width=15, font=("bold", 15)).grid(row=6, column=0)
gender = Label(window, text = "Gender", width=15, font=("bold", 15)).grid(row=7, column=0)

#using Radiobutton
var = IntVar()
Radiobutton(window, text="Male", padx = 30, variable=var, value=1).grid(row=7, column=1)
Radiobutton(window, text="Female", padx = 20, variable=var, value=2).grid(row=7, column=2)
Radiobutton(window, text="Others", padx = 10, variable=var, value=3).grid(row=7, column=3)
dob = Label(window, text="Date of Birth", width=15, font=("bold", 15)).grid(row=8, column=0)
worklocat = Label(window, text="Work Location", width=15, font=("bold", 15)).grid(row=9, column=0)

#using Dropdown
list1 = ['Chennai', 'Coimbatore', 'Banglore', 'Hyderabad', 'pune', 'Mumbai', 'Mysore', 'Kolkata'];
c=StringVar()
droplist = OptionMenu(window, c, *list1)
droplist.config(width=20)
c.set('Select your work location')
droplist.grid(row=9, column=1)

#Using Check box
code = Label(window, text="Programming languages", width=20, font=("bold", 15)).grid(row=10, column=0)
var1=IntVar()
Checkbutton(window, text="C/C++", variable=var1).grid(row=10, column=1)
var2=IntVar()
Checkbutton(window, text="Java", variable=var2).grid(row=10, column=2)
var3=IntVar()
Checkbutton(window, text="Python", variable=var3).grid(row=10, column=3)

deg = Label(window, text="Highest Degree", width=20, font=("bold", 15)).grid(row=11, column=0)

Firstname1 = Entry(window).grid(row=2, column=1)
Lastname1 = Entry(window).grid(row=3, column=1)
Email1 = Entry(window).grid(row=4, column=1)
Mobile1 = Entry(window).grid(row=5, column=1)
age1 = Entry(window).grid(row=6, column=1)
dob1= Entry(window).grid(row=8, column=1)
deg1= Entry(window).grid(row=11, column=1)
#function declaration
def clicked():
    tkinter.messagebox.showinfo("Welcome", "Your Information Submitted Successfully ! We will let you soon")
Button(window, text="Submit", command=clicked, width=20, bg='brown', fg='white').grid(row=14, column=1)

#this will run the mainloop.
window.mainloop()