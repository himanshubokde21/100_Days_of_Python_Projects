import tkinter as tk
from tkinter import messagebox

class NoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Notes")

        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack()

        tk.Button(self.root, text="save Note", command=self.save_note).pack()

        self.root.mainloop()

    def save_note(self):
        content = self.text_area.get("1.0", tk.END)
        with open('note.txt', 'w') as file:
            file.write(content)
        messagebox.showinfo("Success", "note Saved!")

NoteApp()