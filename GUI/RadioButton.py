from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("RadioButton")
root.geometry("600x400")

var = StringVar()   # StringVar is a class that stores the values of radio buttons. But we can also use IntVar for integer values.
var.set("Radio")    # This will set the default value of the radio button to "Radio" in this case.
Label(root, text="Choose your favorite programming language:", font="Arial 15 bold", justify=LEFT, padx=14).pack()   # The justify parameter is used to align the text inside the label. Here it's aligned left and there padx parameter is used to add some space between the label and the text.

radio = Radiobutton(root, text="Python", variable=var, value="Python").pack(anchor="w")    # The Radiobutton widget takes three parameters - root (the parent window), text (the text to be displayed on the button) and variable (the variable that stores the value of the selected option).
radio = Radiobutton(root, text="Java", variable=var, value="Java").pack(anchor="w")
radio = Radiobutton(root, text="JavaScript", variable=var, value="JavaScript").pack(anchor="w")
radio = Radiobutton(root, text="SQL", variable=var, value="SQL").pack(anchor="w")
radio = Radiobutton(root, text="HTML & CSS", variable=var, value="HTML & CSS").pack(anchor="w")

Button(root, text="Submit", command=lambda: tmsg.showinfo("Your Preference", f"You have chosen {var.get()}")).pack()

root.mainloop()