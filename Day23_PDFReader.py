from tkinter import *
from tkinter import filedialog
import tkinter as tk 
from PIL import Image, ImageTk
import fitz 

def readPDF():
    filepath = filedialog.askopenfilename(
        title='Select a PDF file',
        filetypes=[('PDF Files', '*.pdf')]
    )
    if filepath:
        try:
            pdf_document = fitz.open(filepath)
            for widget in root.winfo_children():
                if isinstance(widget, Frame) and widget != frame:
                    widget.destroy()
            page = pdf_document[0] 
            pix = page.get_pixmap()  
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pdf_frame = Frame(root)
            pdf_frame.pack(fill=BOTH, expand=YES)
            x_scrollbar = Scrollbar(pdf_frame, orient=HORIZONTAL)
            y_scrollbar = Scrollbar(pdf_frame, orient=VERTICAL)
            canvas = Canvas(pdf_frame, xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
            x_scrollbar.config(command=canvas.xview)
            y_scrollbar.config(command=canvas.yview)
            x_scrollbar.pack(side=BOTTOM, fill=X)
            y_scrollbar.pack(side=RIGHT, fill=Y)
            canvas.pack(side=LEFT, fill=BOTH, expand=YES)
            tk_img = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, anchor=NW, image=tk_img)
            canvas.image = tk_img  
            canvas.config(scrollregion=canvas.bbox(ALL))
        except Exception as e:
            print(f"Error opening file: {e}")

def exitWin():
    root.destroy()

root = Tk()

exitBtn = Button(root, text="Exit", bg='gray',command=exitWin)
exitBtn.pack(side=tk.BOTTOM, padx=12, pady=5)

selectBtn = Button(root, text="Select file", bg='gray' ,command=readPDF)
selectBtn.pack(side=tk.BOTTOM, padx=15, pady=5)

root.title("PDF Viewer")
root.geometry('600x700')
root.config(bg='#17161b')
root.mainloop()