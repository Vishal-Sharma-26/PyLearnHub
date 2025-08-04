from tkinter import *

root = Tk()
root.title("Events")
root.geometry("600x450")

def click(event):     # event is a special variable that contains information about the event that triggered the function. It has attributes like x and y which are the coordinates of where you clicked on the screen.
    print(f"You clicked {event.x}, {event.y}")   # event.x and event.y give us the position of the mouse when we clicked


widget = Button(root, text="Click me")
widget.pack()

widget.bind('<Button-1>', click)    # <Button-1> means left click and <Button-2> means right click and <Double-1> means double click and <Triple-1> means triple click
widget.bind('<Double-1>', quit)     # This will quit the program when you double click the button


root.mainloop()