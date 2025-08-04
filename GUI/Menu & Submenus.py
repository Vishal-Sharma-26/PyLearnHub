from tkinter import *

root = Tk()
root.title("Menu and Submenu")
root.geometry("600x400")

def my_command():    # This is a function to be called when the user clicks on any of the options in the menu bar.
    print("Hello World!")

my_menu = Menu(root)
my_menu.add_command(label="File", command=my_command)
my_menu.add_command(label="Exit", command=quit)
root.config(menu=my_menu)

menubar = Menu(root)     # Creating a menubar object.
m1 = Menu(menubar, tearoff=0)         # Creating a submenu object, tearoff parameter removes the dotted line that appers by defult.
m1.add_command(label="New File", command=my_command)
m1.add_command(label="Save", command=my_command)       #  Adding commands to the respective submenus
m1.add_separator()
m1.add_command(label="Save As", command=my_command)
m1.add_command(label="Open", command=my_command)
root.config(menu=menubar)       # Configuring the main window with the created
menubar.add_cascade(label="File", menu=m1)       # Adding the submenu to the menubar.


m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Terminal", command=my_command)
m2.add_command(label="Cut", command=my_command)
m2.add_command(label="Copy", command=my_command)
m2.add_command(label="Paste", command=my_command)
root.config(menu=menubar)
menubar.add_cascade(label="Edit", menu=m2)

root.mainloop()