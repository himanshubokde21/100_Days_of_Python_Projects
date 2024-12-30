from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

root  = Tk()

fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image file', filetype=(('JPG File', '*.jpg'), ('PNG file', '*.png'), ('ALL file', 'how are you .txt')))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

lbl = Label(root)
lbl.pack()

btn_1 = Button(fram, text="Select Image", command=showimage)
btn_1.pack(side=tk.LEFT) 
btn_1 = Button(fram, text="Exit", command=lambda:exit())
btn_1.pack(side=tk.LEFT, padx=12) 

root.title('Image Viewer')
root.geometry('400x450')
root.mainloop()