import cv2 as cv
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def open_image(filename):
    image = cv.cvtColor(cv.imread(filename), cv.COLOR_BGR2RGB)#rename adam.jpg to something else
    imgtk = ImageTk.PhotoImage(image = Image.fromarray(image))
    placedImage = Label(image=imgtk)
    placedImage.pack()

def select_file():
    filetypes = (
        ('Image files', '*.jpg *.png *.jpeg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    name.config(text = filename)

root = Tk()

filename = "adam.jpg"

root.title("Photo Editor")
root.minsize(500,500)

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
).pack()

name = ttk.Label(text = filename)
name.pack()
        
startButton = ttk.Button(text = "Open Image", command = lambda filename = filename : open_image(filename)).pack()

root.mainloop()
