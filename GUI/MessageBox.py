from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.title("Menu and Submenu")
root.geometry("600x400")

def my_command():    # This is a function to be called when the user clicks on any of the options in the menu bar.
    print("Hello World!")

def help():
    tmsg.showinfo("Help", "Thanks for using this program.")      # showinfo is used to display an information message box.

def rate():
    value = tmsg.askquestion("Rating", "Was your experience is good?")    # askquestion is used to display a question message box. It returns yes or no.
    print(value)
    if value == "yes":
        tmsg.showinfo("Thank You", "Thanks for rating us.")   # showinfo is used to display an information message box.
        print("Thanks for rating us.")
    else:
        tmsg.showwarning("Sorry", "We will try to improve ourself.")   # showwarning is used to display a warning message box
        print("Sorry for inconvenience.")


menubar = Menu(root)     # Creating a menubar object.
m1 = Menu(menubar, tearoff=0)         # Creating a submenu object, tearoff parameter removes the dotted line that appers by defult.
m1.add_command(label="New File", command=my_command)
m1.add_command(label="Save", command=my_command)       #  Adding commands to the respective submenus
m1.add_command(label="Save As", command=my_command)
m1.add_command(label="Open", command=my_command)
m1.add_separator()
m1.add_command(label="Settings", command=my_command)
m1.add_command(label="Export", command=my_command)
m1.add_command(label="Print", command=my_command)
m1.add_command(label="Exit", command=quit)      # quit is a built-in function which closes the application.
root.config(menu=menubar)       # Configuring the main window with the created
menubar.add_cascade(label="File", menu=m1)       # Adding the submenu to the menubar.


m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Terminal", command=my_command)
m2.add_command(label="Cut", command=my_command)
m2.add_command(label="Copy", command=my_command)
m2.add_command(label="Paste", command=my_command)
m2.add_separator()
m2.add_command(label="Find", command=my_command)
m2.add_command(label="Select", command=my_command)
m2.add_command(label="Select All", command=my_command)
m2.add_command(label="Sort Lines", command=my_command)
root.config(menu=menubar)
menubar.add_cascade(label="Edit", menu=m2)


m3 = Menu(menubar, tearoff=0)
m3.add_command(label="Find Action", command=my_command)
m3.add_command(label="About", command=my_command)
m3.add_command(label="Checks for Updates", command=my_command)
m3.add_command(label="Help", command=help)
m3.add_separator()
m3.add_command(label="Rate Us", command=rate)

root.config(menu=menubar)
menubar.add_cascade(label="Help", menu=m3)

root.mainloop()