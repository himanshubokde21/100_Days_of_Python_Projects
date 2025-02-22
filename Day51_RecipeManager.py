import tkinter as tk
from tkinter import messagebox

class RecipeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Manager")

        self.recipes = []

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.grid(row=0, column=0)
        
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)
        
        self.ingredients_label = tk.Label(root, text="Ingredients:")
        self.ingredients_label.grid(row=1, column=0)
        
        self.ingredients_entry = tk.Entry(root)
        self.ingredients_entry.grid(row=1, column=1)
        
        self.instructions_label = tk.Label(root, text="Instructions:")
        self.instructions_label.grid(row=2, column=0)
        
        self.instructions_entry = tk.Entry(root)
        self.instructions_entry.grid(row=2, column=1)
        
        self.add_recipe_button = tk.Button(root, text="Add Recipe", command=self.add_recipe)
        self.add_recipe_button.grid(row=3, column=0, columnspan=2)
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=4, column=0)
        
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=4, column=1)
        
        self.search_button = tk.Button(root, text="Search", command=self.search_recipe)
        self.search_button.grid(row=5, column=0, columnspan=2)
        
        self.recipes_listbox = tk.Listbox(root)
        self.recipes_listbox.grid(row=6, column=0, columnspan=2)
        
        self.update_recipes_listbox()
    
    def add_recipe(self):
        title = self.title_entry.get()
        ingredients = self.ingredients_entry.get()
        instructions = self.instructions_entry.get()
        if title and ingredients and instructions:
            self.recipes.append({
                "title": title,
                "ingredients": ingredients,
                "instructions": instructions
            })
            self.update_recipes_listbox()
            self.title_entry.delete(0, tk.END)
            self.ingredients_entry.delete(0, tk.END)
            self.instructions_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter title, ingredients, and instructions.")
    
    def search_recipe(self):
        search_term = self.search_entry.get().lower()
        filtered_recipes = [recipe for recipe in self.recipes if search_term in recipe["title"].lower()]
        self.update_recipes_listbox(filtered_recipes)
    
    def update_recipes_listbox(self, recipes=None):
        self.recipes_listbox.delete(0, tk.END)
        if recipes is None:
            recipes = self.recipes
        for recipe in recipes:
            self.recipes_listbox.insert(tk.END, recipe["title"])

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeManager(root)
    root.mainloop()
