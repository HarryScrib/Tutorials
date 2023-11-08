import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# create function which gets information from entry field using get method and the stored entry integer variable
def convert():
    mile_input = entry_int.get()
    km_output = round(mile_input * 1.61, 2) # converting miles to km
    output_string.set(f'{km_output} km') # set value of output label

# create simple app with tkinter

# window
window = ttk.Window(themename = 'cosmo') # tk.Tk replaced by ttk.Window() as part of bootstrap styling
window.title('Simple Distance Conversion Tool') # title the window
window.geometry('300x150') # size of the window on open

# title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold') # create label widget
title_label.pack()

# input field
input_frame = ttk.Frame(master = window) # create frame to put widgets into
entry_int = tk.IntVar() # creates separate variable that stores and updates values
entry = ttk.Entry(master = input_frame, textvariable = entry_int) # create entry widget with text variable storage functionality - storing to entry_int
button = ttk.Button( # create button widget
    master = input_frame, 
    text = 'Convert', 
    style = 'info', # changes button colour to purple using the bootstrap themes
    command = convert) # calls convert function
entry.pack(side = 'left', padx = 10) # side left puts them next to each other, padx gives them x axis padding.
button.pack(side = 'left')
input_frame.pack(pady = 10) # pads on the y axis to give more space between frame and label

# output
output_string = tk.StringVar() # stores string
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string) # text variable overrides whatever text is inside of label.
output_label.pack(pady = 5)

# run
window.mainloop()