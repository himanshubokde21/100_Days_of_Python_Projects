import tkinter as tk
from tkinter import messagebox

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")
        master.geometry("300x250")
        master.configure(bg='#f0f0f0')

        self.label_temp = tk.Label(master, text="Enter Temperature:", bg='#f0f0f0')
        self.label_temp.pack(pady=10)

        self.temp_entry = tk.Entry(master, width=15, font=('Arial', 12))
        self.temp_entry.pack()

        self.conversion_var = tk.StringVar(value="C to F")
        self.conversion_menu = tk.OptionMenu(
            master, 
            self.conversion_var, 
            "C to F", 
            "F to C"
        )
        self.conversion_menu.pack(pady=10)

        self.convert_button = tk.Button(
            master, 
            text="Convert", 
            command=self.convert_temperature,
            bg='#4CAF50',
            fg='white'
        )
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(
            master, 
            text="", 
            bg='#f0f0f0', 
            font=('Arial', 12, 'bold')
        )
        self.result_label.pack(pady=10)

    def convert_temperature(self):
        try:
            temp = float(self.temp_entry.get())
            conversion_type = self.conversion_var.get()

            if conversion_type == "C to F":
                result = (temp * 9/5) + 32
                result_text = f"{temp}°C = {result:.2f}°F"
            else:
                result = (temp - 32) * 5/9
                result_text = f"{temp}°F = {result:.2f}°C"

            self.result_label.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

def main():
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
