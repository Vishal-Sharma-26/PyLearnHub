from tkinter import *

root = Tk()
root.title("Tips & Tricks")
root.geometry("600x400")

root.wm_iconbitmap("logo.ico")   # To change the icon of window
root.configure(background="gray")   # To change background color

width = root.winfo_screenwidth()   # To get screen width
height = root.winfo_screenwidth()  # To get screen height

print(f"{width} x {height}")    # To print screen size

Button(text="Close", command= root.destroy).pack()   # destroy is used to close the window

root.mainloop()