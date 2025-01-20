import tkinter as tk
import time

def update_time():
    curr_time = time.strftime('%H:%M:%S')
    label.configure(text=curr_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title('Digital Clock')

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()
root.mainloop()