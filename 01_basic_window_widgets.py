import tkinter as tk
from tkinter import ttk

# create button function - will just say 'a button was pressed'
def button_func():
    print('a button was pressed')

# exercise button function
def exercise_button_func():
    print('hello')

# create a window (can also call it root)
window = tk.Tk()
window.title('Window and Widgets') # set title of app
window.geometry('800x500') # set width x height of app on load up

# ttk label
label = ttk.Label(master = window, text = 'This is a test') # just a simple text label
label.pack() # pack above the text box

# tk text
text_box = tk.Text(master = window) # master = parent, where do we want to put this textbox. we want to put it on the window, so we use master = window
text_box.pack() # what pack does, is it places the widget in the middle at the top. as more widgets are packed, they go down the y axis through the middle

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise - ttk label
exercise_label = ttk.Label(master = window, text = 'my label')
exercise_label.pack()

# exercise - ttk button
exercise_button = ttk.Button(master = window, text = 'hello button', command = exercise_button_func)
exercise_button.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func) # a button needs a command to work, so we must make a function to work alongside it. we do not want to CALL it, just PASS it
button.pack()

# run 
window.mainloop() # mainloop updates the gui and checks for events (button clicks, mouse movement, closing the window), which is why it always must be called

# exercise
# add one more text label and a button with a function that prints 'hello'
# the label should say my label and be between the entry widget and the button