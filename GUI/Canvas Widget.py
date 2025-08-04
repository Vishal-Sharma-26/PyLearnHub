from tkinter import *

root = Tk()
root.title("Canvas Widget")

canvas_width=800    # width of canvas widget
canvas_height=400   # height of canvas height

root.geometry(f"{canvas_width}x{canvas_height}")      # Create a window with given size of canvas widget
can_widget = Canvas(root, width=canvas_width, height=canvas_height)    # Create a canvas widget and pack it into the root window
can_widget.pack()

can_widget.create_line(0, 0, 800, 400)     # Create line in canvas from point (0,0) to point (800, 400). Where first two points are starting point and last two points are ending points.

can_widget.create_rectangle(5, 7, 600, 400, fill="Blue")    # Create rectangle in canvas. First four parameters are coordinates of top left corner and bottom right corner respectively.

can_widget.create_text(200, 200, text="Hey this is a Canvas")  # Create text in canvas at position (200, 200)

can_widget.create_oval(250, 150, 350, 250)   # Create oval in canvas. First four parameters are coordinates of top left corner and bottom right corner respectively

root.mainloop()
