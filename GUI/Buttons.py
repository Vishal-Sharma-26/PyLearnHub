from tkinter import *

root = Tk()
root.title("Buttons")
root.geometry("400x350")

def hello():                     # Command is used to call the function when button clicked.
    print("Hello World!")

def name():
    print("Vishal")


frame = Frame(root, borderwidth=4, bg="green", relief=SUNKEN)     # frame is a container for other widgets.
frame.pack(anchor="nw")

btn = Button(frame, fg="black", text="Click Me", command=hello)   # command is used to call the function
btn.pack(side=LEFT, padx=23)

btn1 = Button(frame, fg="black", text="Build By", command=name)
btn1.pack(side=LEFT, padx=23)

btn2 = Button(frame, fg="black", text="Click Me")     # If no command is given then it will not do anything.
btn2.pack(side=LEFT, padx=23)

btn3 = Button(frame, fg="black", text="Click Me")
btn3.pack(side=LEFT, padx=23)


root.mainloop()