from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os 

root = Tk()
global content 
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
textArea = Text(root, width=int(screenWidth/9), height=int(screenHeight/19))

def textBox():
    textArea.delete('1.0', tk.END)
    textArea.pack(fill=tk.BOTH, expand=False)

def openTxT():
    global content
    filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="select file", filetype=(("Text file", "*.txt"), ('All File', '*.*')))
    if filepath:
        with open(filepath) as file:
            content = file.read()
            textArea.insert(tk.END, content)
            textArea.pack(fill=tk.BOTH, expand=False)
            

def saveFile():
    global content
    filepath = filedialog.asksaveasfilename(initialdir=os.getcwd(), filetypes=[("Text file", "*.txt")], initialfile="Unititled.txt")
    with open(filepath, 'w') as file:
        file.write(content)

frame = Frame(root, bg="#313738")
frame.pack(side=tk.TOP, padx=15, pady=5)

newBtn = Button(frame, text="new", command=textBox)
newBtn.pack(side=tk.LEFT, padx=10)

saveBtn = Button(frame, text="save", command=saveFile)
saveBtn.pack(side=tk.LEFT, padx=12)

openBtn = Button(frame, text="open", command=openTxT)
openBtn.pack(side=tk.LEFT, padx=16)

exitBtn = Button(frame, text="exit", command=exit)
exitBtn.pack(side=tk.LEFT, padx=14)

root.title("Simple Notepad")
root.geometry("500x500")
root.configure(bg="#313738")
root.mainloop()