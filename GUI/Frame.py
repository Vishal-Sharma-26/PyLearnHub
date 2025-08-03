from tkinter import *

root = Tk()
root.title("Frame GUI")
root.geometry("640x480")


# Frame is used for grouping the widgets together
f1 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
f1.pack(side="left", fill="y")

f2 = Frame(root, bg="gray", borderwidth=6, relief=SUNKEN)
f2.pack(side="top", fill="x")


var = Label(f1, text="Frame GUI")  # var is a label in f1 frame
var.pack(pady=142)

var = Label(f2, text="Wellcome to Frame")  # var is a label in f2 frame
var.pack()




root.mainloop()