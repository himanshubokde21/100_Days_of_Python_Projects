import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.books = []

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.grid(row=0, column=0)
        
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)
        
        self.author_label = tk.Label(root, text="Author:")
        self.author_label.grid(row=1, column=0)
        
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)
        
        self.add_book_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_book_button.grid(row=2, column=0, columnspan=2)
        
        self.borrow_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.borrow_button.grid(row=3, column=0, columnspan=2)
        
        self.return_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_button.grid(row=4, column=0, columnspan=2)
        
        self.books_listbox = tk.Listbox(root)
        self.books_listbox.grid(row=5, column=0, columnspan=2)
        
        self.update_books_listbox()
    
    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.books.append({"title": title, "author": author, "status": "available"})
            self.update_books_listbox()
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both title and author.")
    
    def borrow_book(self):
        selected_book_index = self.books_listbox.curselection()
        if selected_book_index:
            book = self.books[selected_book_index[0]]
            if book["status"] == "available":
                book["status"] = "borrowed"
                self.update_books_listbox()
            else:
                messagebox.showinfo("Info", "The book is already borrowed.")
        else:
            messagebox.showerror("Error", "Please select a book to borrow.")
    
    def return_book(self):
        selected_book_index = self.books_listbox.curselection()
        if selected_book_index:
            book = self.books[selected_book_index[0]]
            if book["status"] == "borrowed":
                book["status"] = "available"
                self.update_books_listbox()
            else:
                messagebox.showinfo("Info", "The book is not borrowed.")
        else:
            messagebox.showerror("Error", "Please select a book to return.")
    
    def update_books_listbox(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.books:
            self.books_listbox.insert(tk.END, f"{book['title']} by {book['author']} - {book['status']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
