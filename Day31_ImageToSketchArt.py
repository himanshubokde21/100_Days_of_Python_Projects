from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
import threading

root = Tk()

def downloadImg(image):
    imgName = "sketch_image.png"
    savePath = os.path.join(os.path.expanduser('~'), 'Downloads')
    path = os.path.join(savePath, imgName)
    try:
        cv2.imwrite(path, image)
        Label(root, text="Image saved in Downloads", bg="#313738", fg="white").pack()
    except Exception as e:
        Label(root, text=f"Error saving image: {str(e)}", bg="#313738", fg="white").pack()

def genPencilSketch(src):
    if src:
        
        img = cv2.imread(src)
        img = cv2.resize(img, (250, 250))  

        sketch, _ = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

        sketchRGB = cv2.cvtColor(sketch, cv2.COLOR_BGR2RGB)
        sketchPhotoImg = ImageTk.PhotoImage(image=Image.fromarray(sketchRGB))

        sketchImgLabel = Label(root, image=sketchPhotoImg, width=250, height=250)
        sketchImgLabel.image = sketchPhotoImg 
        sketchImgLabel.pack()

        downBtn = Button(root, text="Download", command=lambda: downloadImg(sketch))
        downBtn.pack(pady=10)

def runPencilSketch(src):
    threading.Thread(target=genPencilSketch, args=(src,), daemon=True).start()

imgLabel = Label(root, text=' ')
def addFile():
    filePath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", 
                                          filetypes=[("Image Files", ("*.jpg", "*.png"))])
    if filePath:
        imgLabel.pack_forget()
        imgContent = Image.open(filePath)
        imgContent = imgContent.resize((250, 250), Image.LANCZOS)
        img = ImageTk.PhotoImage(imgContent)

        imgLabel.configure(image=img, width=250, height=250)
        imgLabel.image = img 
        imgLabel.pack()

        genSketchBtn = Button(root, text="Generate Pencil Sketch", command=lambda: runPencilSketch(filePath))
        genSketchBtn.pack(pady=10)

addFileBtn = Button(root, text="Add Image", command=addFile)
addFileBtn.pack(pady=15)

root.title("Pencil Sketch Art")
root.geometry("500x650")
root.configure(bg="#313738")
root.mainloop()
