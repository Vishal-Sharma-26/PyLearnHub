from tkinter import *

root = Tk()
root.geometry("655x335")

user = Label(root, text="Username")
password = Label(root, text="Password")

def getvals():
    print(f"{uservalue.get()}, {passvalue.get()}")    # f-string is used to format the output of the function getvals

# Grid is used to place the widgets at specific positions on screen

user.grid()   # row and column are optional parameters in grid method
password.grid(row=1)

# Variable Classes:
'''
BooleanVar - stores boolean values
DoubleVar - stores double values
IntVar - stores integer values
StringVar - stores string values
'''

uservalue = StringVar()    # StringVar class object created to store user value entered by user
passvalue = StringVar()

userentry = Entry(root, textvariable= uservalue)    # Entry widget takes variable as an argument which will be stored in uservalue variable
passentry = Entry(root, textvariable= passvalue)    # Entry widget takes variable as an argument which will be stored in passvalue variable

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)


btn = Button(text="Submit", command=getvals, bg="red" ).grid(column=1)

root.mainloop()