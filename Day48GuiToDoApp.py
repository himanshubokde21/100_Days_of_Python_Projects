import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.task_listbox = tk.Listbox(self.frame, height=15, width=50, font=('arial', 12))
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=50, font=('arial', 12))
        self.entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", width=48, command=self.add_task, font=('arial', 12))
        self.add_task_button.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", width=48, command=self.delete_task, font=('arial', 12))
        self.delete_task_button.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
            self.tasks = [task.strip() for task in tasks]
            self.update_task_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.protocol("WM_DELETE_WINDOW", app.save_tasks)
    root.mainloop()
