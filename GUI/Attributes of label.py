from tkinter import *

from openpyxl.styles.builtins import title

root = Tk()
root.geometry("600x400")
root.title("Attributes of Labels")

# Label Attributes are:
'''
text - adds text to the label
bg - sets background color
fg - sets foreground (text) color
font - sets font and size ('arial', 18)
padx - adds horizontal padding
pady - adds vertical padding
relief - border styling (SUNKEN, RAISED, GROOVE, RIDGE)
borderwidth - sets border width
'''

title_label = Label(text='''The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. 
                         \nRunning python -m tkinter from the command line should open a window demonstrating a simple Tk interface,  
                         \nof Tcl/Tk is installed, so you can read the Tcl/Tk documentation specific to that version.
                         \nThe official Python binary release bundles Tcl/Tk 8.6 threaded. See the source code for the _tkinter module  
                         \nbut adds a fair amount of its own logic to make the experience more pythonic. This documentation will concentrate on these additions and changes''',
                         bg="red", fg="white", font=("arial", 10, "bold"), padx=30, pady=30, relief=SUNKEN, borderwidth=10)


# Pack Attributes are:
'''
anchor - aligns widget in parent container; default is CENTER and may be set to N, NE, E, SE, S, SW, W, NW, or CENTER
expand - if true, widget expands to fill any space not otherwise used in parent; default is false
fill - determines whether widget fills both x and y directions; options are NONE (default), X, Y, BOTH
side - where widget appears within parent; options are TOP (default), BOTTOM, LEFT, RIGHT
sticky - controls how widget resizes when parent frame is resized; default is NONE; see packer reference for details
padx - horizontal padding around widget; may be given as either a single number or a pair of numbers; each represents the minimum number of pixels to pad widget's width in the x direction
pady - vertical padding around widgetl may be given as either a single number or a pair of numbers; each represents the minimum number of pixels to pad widget's height in the y direction
'''

title_label.pack(anchor="nw")   # anchor attribute is used to align the label at north west corner of the screen
title_label.pack(anchor="n")    # anchor attribute is used to align the label at north corner of the screen
title_label.pack(anchor="e")   # anchor attribute is used to align the label at east corner of the screen
title_label.pack(anchor="se")   # anchor attribute is used to align the label at south east corner of the screen
title_label.pack(anchor="s")   # anchor attribute is used to align the label at south corner of the screen
title_label.pack(anchor="sw")   # anchor attribute is used to align the label at south west corner of the screen
title_label.pack(anchor="w")   # anchor attribute is used to align the label at west corner of the screen
title_label.pack(anchor="ne")   # anchor attribute is used to align the label at north east corner of the screen

title_label.pack(side="bottom", anchor="sw", fill=X)  # side attribute is used to align the label at bottom of the screen and fill=X is used to fill the label horizontally
title_label.pack(side="left", fill=Y)   # side attribute is used to align the label at left of the screen and fill=Y is used to fill the label vertically. Now you can also use side="right" to the label
title_label.pack(side="right", padx=30, pady=60)  # padx and pady attributes are used to add padding to the label


root.mainloop()