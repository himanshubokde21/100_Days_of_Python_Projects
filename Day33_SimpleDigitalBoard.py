import tkinter as tk
from tkinter.colorchooser import askcolor

class DigitalBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Board")

        self.canvas = tk.Canvas(root, background='black', width=800, height=600)
        self.canvas.pack(expand=True, fill="both")

        self.drawing = False
        self.penColor = "white"
        self.lineWidth = 2

        self.canvas.bind('<Button-1>', self.startDraw)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.stopDraw)

        self.setupControls()

    def startDraw(self, event):
        self.drawing = True
        self.lastX = event.x
        self.lastY = event.y

    def draw(self, event):
        if self.drawing:
            currX, currY = event.x, event.y
            self.canvas.create_line(self.lastX, self.lastY, currX, currY, fill=self.penColor, width=self.lineWidth, capstyle=tk.ROUND, smooth=True)
            self.lastX = currX
            self.lastY = currY

    def stopDraw(self, event):
        self.drawing = False

    def setupControls(self):
        controlFrame  = tk.Frame(self.root)
        controlFrame.pack(fill='x')

        colorBtn = tk.Button(controlFrame, text="Change Color", command=self.chooseColor)
        colorBtn.pack(side='left', padx=5)

        clearBtn = tk.Button(controlFrame, text="Clear", command=self.clearCanvas)
        clearBtn.pack(side='left', padx=5)

    def chooseColor(self):
        color = askcolor(color=self.penColor)[1]
        if color:
            self.penColor = color
        
    def clearCanvas(self):
        self.canvas.delete('all')

def main():
    root = tk.Tk()
    app = DigitalBoard(root)
    root.mainloop()

if __name__ == '__main__':
    main()

