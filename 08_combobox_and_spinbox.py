import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

# Combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0]) # set startup option
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure(values = items) also works
combo.pack()

# events
# pull selected item and reference label
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'a label') # can also use textvariable=food_string
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window, 
    from_ = 3, 
    to = 20, 
    increment = 3, 
    command = lambda: print(spin_int.get()),
    textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1, 2, 3, 4, 5)
spin.pack()

# exercise
exer_values = ('A', 'B', 'C', 'D', 'E')
exer_var = tk.StringVar(value = exer_values[0])
exer_spin = ttk.Spinbox(window, textvariable = exer_var, values = exer_values)
exer_spin.pack()

exer_spin.bind('<<Decrement>>', lambda event: print(exer_var.get()))

# run
window.mainloop()

# exercise
# create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased