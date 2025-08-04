from tkinter import *
import tkinter.messagebox as tmsg    # Message box module is imported here.

root = Tk()
root.title("Slider")
root.geometry("600x400")

my_slider = Scale(root, from_=10, to=50)     # Scale is used for sliders default value is vertical slider.
my_slider.pack()

my_slider1 = Scale(root, from_=0, to=100, orient=HORIZONTAL,  tickinterval=50)    # Horizontal slider and tick interval is the distance between two ticks.
my_slider1.pack()

Label(root, text="How many rupees do you want?").pack()
my_slider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
my_slider2.set(10)   # Set function sets a default value in scale.
my_slider2.pack()
Button(root, text="Buy", pady=10, command=lambda: tmsg.showinfo("Amount", f"You have bought {my_slider2.get()} rupees worth of items.")).pack()   # Get function gets the current value of scale and displays it on button click.

root.mainloop()