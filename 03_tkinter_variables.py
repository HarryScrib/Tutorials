import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window 
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable - we use value = to set a start value
string_var = tk.StringVar(value = 'start value') # stringvar will contain some kind of string which we will pass to the label text. we can also connect it to the entry, which will override the stringvar

# widgets
label = ttk.Label(master = window, text = 'Label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

# exercise 
exercise_var = tk.StringVar(value = 'test')
# exercise_var.set('test') also works

exercise_label = ttk.Label(master = window, textvariable = exercise_var)
exercise_label.pack()

exercise_entry1 = ttk.Entry(master = window, textvariable = exercise_var)
exercise_entry1.pack()

exercise_entry2 = ttk.Entry(master = window, textvariable = exercise_var)
exercise_entry2.pack()


# run
window.mainloop()

# exercise
# create 2 entry fields and 1 label, they should all be connected via a StringVar
# set a start value of 'test'