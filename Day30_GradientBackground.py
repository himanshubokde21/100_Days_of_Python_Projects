from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import CircleButton, Colorscale, ColorVar
import os
import cv2

root = Tk()

colorVar = ColorVar(value='#333')
Colorscale(root, value='hex', variable=colorVar, gradient=('#ff512f', '#dd2476'), width=400).pack(pady=100)

root.title("Gradient Backgraound")
root.configure(bg=colorVar)
root.geometry("400x500")
root.mainloop()

