from tkinter import *

class GUI(Tk):    # Inheritance from TK class of Tkinter module
    def __init__(self):   # Constructor
        super().__init__()   # Calling constructor of parent class
        self.geometry("600x400")   # Setting geometry of the window

    def status(self):    # Creating a function to display status bar
        self.var = StringVar()   # Creating variable for status bar
        self.var.set("Ready")  # Setting default value of status bar
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")   # Creating status bar label with variable and setting its properties
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button clicked")

    def createbutton(self, inptext):   # Creating a function to create button with given text and calling click function on click. inptext is the text that will be displayed on the button
        Button(text=inptext, command=self.click).pack()

if __name__ == '__main__':   # Main function
    window = GUI()  # Creating object of GUI class
    window.status()   # Calling status function
    window.createbutton("Click me!")   # Calling createbutton function with "Click me!" as argument
    window.mainloop() # Running the mainloop of the window