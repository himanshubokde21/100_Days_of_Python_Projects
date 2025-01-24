from tkinter import *
from datetime import date

class Age_Calculator:
    def __init__(self):
        self.root = Tk()

        self.year_entry = StringVar()
        self.month_entry = StringVar()
        self.day_entry = StringVar()

        Label(self.root, text="AGE CALCULATOR", font=('arial', 16, 'bold')).pack(pady=10)

        Label(self.root, text="day (dd)").pack()
        Entry(self.root, textvariable=self.day_entry, width=20).pack()

        Label(self.root, text="month (mm)").pack()
        Entry(self.root, textvariable=self.month_entry, width=20).pack()

        Label(self.root, text="year (yyyy)").pack()
        Entry(self.root, textvariable=self.year_entry, width=20).pack()

        Button(self.root, text="calculate age", command=self.calculate_age).pack(pady=20)

        self.root.title("Age Calculator")
        self.root.geometry("400x450")
        self.root.mainloop()

    def calculate_age(self):
        today = date.today()

        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        day = int(self.day_entry.get())

        birthday = date(year, month, day)
        age = today.year - birthday.year

        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1

        Label(self.root, text=f"your age is {age}", font=('arial', 14, 'bold')).pack()
     

if __name__ == '__main__':
    Age_Calculator()