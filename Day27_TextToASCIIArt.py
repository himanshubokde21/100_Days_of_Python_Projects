from tkinter import *
import tkinter as tk
import pyfiglet as pf

root = Tk()

textVar = tk.StringVar()
colorVar = tk.StringVar()

def ascii():
    text = textVar.get()
    color = colorVar.get() or "black"
    ascii_art = pf.figlet_format(text, font="standard")
    resLabel.configure(text=ascii_art, fg=color)

resLabel = Label(root, text=' ', bg='#313738', font=("Courier", 12), justify=LEFT)
resLabel.pack(pady=30)

textLabel = Label(root, text="Enter Text", font=("Times New Roman", 16, "bold"), bg='#313738', fg="white")
textLabel.pack(pady=15)

textEntry = tk.Entry(root, textvariable=textVar, width=50, justify=CENTER)
textEntry.pack()

colorLabel = Label(root, text="Enter Color (e.g., red, blue)", font=("Times New Roman", 16, "bold"), bg='#313738', fg="white")
colorLabel.pack(pady=15)

colorEntry = tk.Entry(root, textvariable=colorVar, width=50, justify=CENTER)
colorEntry.pack()

asciiBtn = Button(root, text="Generate ASCII", command=ascii)
asciiBtn.pack(pady=10)

root.title("ASCII ART")
root.geometry("450x450")
root.configure(bg="#313738")

root.mainloop()
