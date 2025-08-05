from tkinter import *

root = Tk()
root.title("ListBox")
root.geometry("600x400")

lbx = Listbox(root)   # ListBox is a widget that can be used to display a list of items. It has methods for adding and removing items from the list.
lbx.pack()
lbx.insert(END, "First item")   # insert method is used to add an item to the list box at a specific position.

Button(root, text="Add Item", command=lambda: lbx.insert(ACTIVE, "second item")).pack()   # ACTIVE is a constant that represents the currently slected item in the list box and labda function is used to create a new function on the fly without defining it separately.


root.mainloop()