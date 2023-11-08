import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = 'light pink')
canvas.pack()

# create a tuple for sides. width defines border
canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 15, dash = (4, 2, 1, 1), outline = 'green') 
canvas.create_oval((200, 0, 100, 100), fill = 'purple', outline = 'violet', width = 15)
canvas.create_arc(
    (200, 0, 100, 100), 
    fill = 'red', 
    start = 45, # start point of 360 degree
    extent = 180, # angle definition
    style = tk.ARC, # tk.PIESLICE / ARC / CHORD etc changes the shape of the arc
    width = 15) # border size

canvas.create_line((0, 0, 100, 150), fill = 'blue')
# canvas.create_polygon((0,0, 100,200, 300,50, 150,-50), fill = 'yellow')

canvas2 = tk.Canvas(window, bg = 'purple')
canvas2.pack()

# canvas2.create_text((100,200), text = 'this is some text', width = 50)

# canvas2.create_window((150,100), window = ttk.Label(window, text = 'this is text in a canvas'))

# exercise

# event handler for capturing the starting position
def set_pos_start(event):
    # without global, start_x and start_y are treated locally
    global start_x, start_y
    start_x = event.x
    start_y = event.y

# event handler for drawing a line from the starting position to the ending position
def set_pos_end(event):
    end_x = event.x
    end_y = event.y
    # create a line on the canvas from start to end
    canvas2.create_line(start_x, start_y, end_x, end_y)

# bind the event handlers to the canvas
canvas2.bind('<Button-1>', set_pos_start)  
canvas2.bind('<ButtonRelease-1>', set_pos_end)

# seems i made it more complicated than necessary. here is the solution:
def draw_on_canvas(event):
    x = event.x
    y = event.y
    # draw ovals on the pointer so that the brush size is more impressionable. filling it black makes it less like a spray paint
    canvas2.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

def brush_size_adjust(event):
    global brush_size
    # use print(event) to find information on mousewheel. we see that it is delta=120 or delta=-120, depending on up or down
    print(event)
    # this allows us to write the following code:
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    # limit brush size between 2 values, meaning no smaller than 0, and no larger than 50.
    brush_size = max(0, min(brush_size, 50))

brush_size = 4
canvas2.bind('<Motion>', draw_on_canvas)

# as an extra
canvas2.bind('<MouseWheel>', brush_size_adjust)

# run
window.mainloop()

# exercise
# use event binding to create a basic paint app
# can see line being drawn where mouse is