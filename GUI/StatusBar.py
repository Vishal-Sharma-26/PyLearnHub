from tkinter import *
import time

def update_status():   # Update the status bar after a delay of 2 seconds after clicking on button.
    statusvar.set("Updating...")   # Set temporary value to status variable.
    sbar.update()
    time.sleep(2)    # Delay for 2 seconds.
    statusvar.set("Updated!")   # Set new value to status variable.

root = Tk()
root.title("StatusBar")
root.geometry("600x400")

statusvar = StringVar()   # Create string variable.
statusvar.set("Ready")    # Set initial value to status variable.
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")   # Create label with status variable.
sbar.pack(side=BOTTOM, fill=X)   # Pack it at bottom and make it stretchable.
Button(root, text="Click", command=update_status).pack()


root.mainloop()