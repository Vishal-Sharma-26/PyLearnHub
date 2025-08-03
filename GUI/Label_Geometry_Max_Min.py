from tkinter import *

root = Tk()

root.geometry("600x500")  # 600 x 500 is the size of window, where 600 is width and 500 is height
root.minsize(300, 100)  # minimum size of window is 300 x 100, where 300 is width and 100 is height
root.maxsize(1000, 700)  # maximum size of window is 1000 x 700

vab = Label(text="This is the label")    # vab is variable name for label widget
vab.pack()   # pack method will show the label on screen

root.mainloop()