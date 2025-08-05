from tkinter import *

root = Tk()
root.title("Scrollbar")
root.geometry("600x400")

scrollbar = Scrollbar(root)    # scrollbar is a widget that can be used to scroll through the content of a window or frame.
scrollbar.pack(side=RIGHT, fill=Y)   # side=RIGHT means that the scrollbar will be placed on the right side of the root window.


# A listbox is a widget that displays a list of items and allows the user to select one or more items from it.
listbox = Listbox(root, yscrollcommand= scrollbar.set)   # yscrollcommand is an option that specifies the command to be executed when the vertical scrollbar is moved.
for i in range(344):
    listbox.insert(END, F"Item {i}")  # END is a constant that represents the end of the list. The insert method inserts the given item at the specified position.

listbox.pack(fill="both")   # fill="both" means that the listbox will expand both horizontally and vertically to fill any extra space available in the root window.
scrollbar.config(command=listbox.yview)    # config is a method that is used to configure the properties of a widget. In this case, we are configuring the scrollbar to control the vertical scrolling of the listbox.


text = Text(root, yscrollcommand= scrollbar.set)   # text is a widget that allows the user to enter multiline text. It has similar option as the listbox widget
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()