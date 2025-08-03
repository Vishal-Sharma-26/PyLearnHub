from tkinter import *
from PIL import Image, ImageTk   # Pillow library to add image in GUI in jpg format

root = Tk()

root.geometry("700x600")
photo = PhotoImage(file="java.png")   # create an object of class PhotoImage which takes path as argument

label = Label(image=photo)
label.pack()


'''For .jpg images'''

image = Image.open("img.jpg")      # open the image file
photo2 = ImageTk.PhotoImage(image)   # convert it into a form that can be shown by tkinter

label2 = Label(image=photo2)    # create a label and show the image in it
label2.pack()   # pack the label on screen

root.mainloop()