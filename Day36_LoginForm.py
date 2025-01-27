from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username=="" and password=="":
        messagebox.showinfo('', "Black Not Allowed")

    elif username=="Himanshu" and password=="admin":
        messagebox.showinfo("", "login success!")

    else:
        messagebox.showinfo("", "incorrect username and password!")


root = Tk()

global entry1
global entry2

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry1 = Entry(root, bd=3)
entry1.place(x=140, y=20)

entry2 = Entry(root, bd=3)
entry2.place(x=140, y=70)

Button(root, text="Login", command=login, height=1, width=13, bd=4).place(x=100, y=120)

root.title("Login")
root.geometry("300x200")
root.mainloop()