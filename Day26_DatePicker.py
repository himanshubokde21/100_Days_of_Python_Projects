from tkinter import *
import tkinter as tk
from tkcalendar import Calendar

root = Tk()

cal = Calendar(root, selectmode='day', year=2020, month=5, day=22)
cal.pack(pady=20)

def getDate():
    date.configure(text=f"Selected Date is {cal.get_date()}")

Button(root, text="Get Date", command=getDate).pack(pady=20)
date = Label(root, text=" ")
date.pack(pady=20)

root.title("Calendar")
root.geometry("400x400")
root.configure(bg="#313738")
root.mainloop()