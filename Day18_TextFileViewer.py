from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

# function to view txt file
def view_txt_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='select a text file', filetype=(('Text File', '*.txt'), ('All File', '*.*')))
    if filename:
        with open(filename) as file:
            content = file.read()
        text_widget = tk.Text(root, wrap=tk.WORD)
        text_widget.insert(tk.END, content)
        text_widget.pack(expand=True, fill='both')


root = Tk()

fram = Frame(root)
fram.pack(side=BOTTOM, padx=25, pady=25)

# select and exit btn
select_file_btn = Button(fram, text='select file', command=view_txt_file)
select_file_btn.pack(side=tk.LEFT)
exit_btn = Button(fram, text='Exit', command=lambda:exit())
exit_btn.pack(side=tk.LEFT, padx=15)

#title and geometry
root.title('text file Viewer')
root.geometry('850x600')
#root.configure(bg='gray')
root.mainloop()