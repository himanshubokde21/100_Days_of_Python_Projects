from tkinter import *
from tkinter import filedialog, messagebox
import os
import fitz
from pathlib import Path

root = Tk()

def genAndDownPDF(src, name=None):
    try:
        if src is None:
            raise ValueError("Source document cannot be None")
        if name is None or name.strip() == "":
            name = "Output.pdf"
        else:
            name = f"{name}.pdf"
        Label(root, text="Successfully Generated!", font=('arial', 16, "bold"), fg="white", bg="#313738").pack(pady=5)
        path = os.path.join(os.path.expanduser('~'), 'Downloads', name)
        src.save(path)
        src.close()

    except ValueError as e:
        messagebox.showerror("Error", f"Input error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during PDF generation: {e}")

def addFile():
    try:
        filePath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", 
                                              filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")])
        
        if filePath:
            try:
                # Open only if it's a PDF file
                if not filePath.lower().endswith('.pdf'):
                    raise ValueError("Please select a valid PDF file.")

                file = fitz.open(filePath)  # Open the selected PDF file
                Label(root, text=filePath, font=('arial', 10, "bold"), fg="white", bg="#313738").pack(pady=5)

                Label(root, text="Enter file name (without extension):", fg="white", bg="#313738").pack()
                outputFile = Entry(root, justify=CENTER)
                outputFile.pack(pady=10)

                genPdfBtn = Button(root, text="Generate & Download PDF", 
                                   command=lambda: genAndDownPDF(file, outputFile.get()))
                genPdfBtn.pack(pady=10)

            except Exception as e:
                messagebox.showerror("Error", f"Could not open the selected file: {e}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file dialog: {e}")

# Initial UI setup
srcLabel = Label(root, text='', bg="#313738")
srcLabel.pack()
addFileBtn = Button(root, text="Add File", command=addFile)
addFileBtn.pack(pady=10)

root.title("PDF Converter")
root.geometry("375x450")
root.configure(bg="#313738")
root.mainloop()
