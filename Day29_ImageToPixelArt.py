from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
import os

root = Tk()

def downlaodImg(image):
    imgName = "image.png"
    savePath = os.path.join(os.path.expanduser('~'), 'Downloads')
    path = os.path.join(savePath, imgName)
    try:
        image.save(path)
        Label(root, text="Check ~Downloads", bg="#313738", fg="white").pack()
    except:
        Label(root, text="Error in save path", bg="#313738", fg="white").pack()

def genPixelArt(src):
    if src:
        pixelImg = Image.open(src)
        pixelImg = pixelImg.resize((pixelImg.size[0]//28, pixelImg.size[1]//28), Image.NEAREST)
        pixelImg = pixelImg.resize((pixelImg.size[0]*28, pixelImg.size[1]*28), Image.NEAREST)
        pixelImg = pixelImg.resize((250, 250))
        pixelPhotoImg = ImageTk.PhotoImage(pixelImg)
        pixelImgLabel = Label(root, image=pixelPhotoImg, width=250, height=250)
        pixelImgLabel.image = pixelPhotoImg
        pixelImgLabel.pack()
        downBtn = Button(root, text="Download", command=lambda: downlaodImg(pixelImg))
        downBtn.pack(pady=10)



imgLabel = Label(root, text=' ')
def addFile():
    filePath = filedialog.askopenfilename(initialdir=os.getcwd, title="select image", filetypes=[("Image File", ("*.jpg", "*.png"))])
    if filePath:
        imgLabel.pack_forget()
        imgContent = Image.open(filePath)
        imgContent = imgContent.resize((250, 250))
        img = ImageTk.PhotoImage(imgContent)
        imgLabel.configure(image=img, width=250, height=250)
        imgLabel.image = img
        imgLabel.pack()
        genPixelArtBtn = Button(root, text="generate pexel art", command=lambda: genPixelArt(filePath))
        genPixelArtBtn.pack(pady=10)

addFileBtn = Button(root, text="Add Image", command=addFile)
addFileBtn.pack(pady=15)

root.title("Pixel Art")
root.geometry("500x650")
root.configure(bg="#313738")
root.mainloop()