import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')
    print(radio_var.get())

# don't actually need to use master=, it is implied. don't need a function, can use lambda. also as we can't call functions here, we cannot pass a parameter normally
button = ttk.Button(window, text='A simple button', command = lambda: print('a basic button'))
button.pack()

button_string = tk.StringVar(value = 'A button with string var')
button2 = ttk.Button(window, text='A simple button', command = button_func, textvariable = button_string) 
button2.pack()

# checkbutton

# check.get() does not work so we need a tkinter variable to perform a .get()
check_var = tk.StringVar()
check = ttk.Checkbutton(
    window, 
    text = 'checkbox 1', 
    command = lambda: print(check_var.get()), # command = lambda: print(type(check_var.get())), returns class 'str'
    variable = check_var) # it's not called textvariable because it doesn't set a text of the checkbox. instead will store a value if box is ticked or not.
check.pack() # returns 1 if checked, 0 if not

# can also use IntVar
check_var2 = tk.IntVar()
check2 = ttk.Checkbutton(
    window, 
    text = 'checkbox 2', 
    command = lambda: print(check_var2.get()), # command = lambda: print(type(check_var2.get())), returns class 'int'
    variable = check_var2) 
check2.pack()

# the most common use-case for something like this will be a boolean variable, as a True/False would make the most sense
check_var3 = tk.BooleanVar()
check3 = ttk.Checkbutton(
    window, 
    text = 'checkbox 3', 
    command = lambda: print(check_var3.get()), # command = lambda: print(type(check_var3.get())), returns class 'bool'
    variable = check_var3) 
check3.pack()
# returns True/False

# for the purpose of this lesson, we will continue working with int data type
check_var4 = tk.IntVar(value = 10) # by default box is now checked
check4 = ttk.Checkbutton(
    window, 
    text = 'checkbox 4', 
    command = lambda: print(check_var4.get()), 
    variable = check_var4,
    onvalue = 10,# value being returned when box is checked
    offvalue = 5) # value being returned when box is unchecked
check4.pack()
# returns 10/5

# radio buttons
# we have a problem because one value is a string and one value is an integer. the best workaround for this is to use StringVar. will convert integer into string to be workable
radio_var = tk.StringVar()
# each of them must have a value otherwise they tick in tandem
radio1 = ttk.Radiobutton(
    window, 
    text = 'Radiobutton 1', 
    value = 'radio 1',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text = 'Radiobutton 2', 
    value = 2, 
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio2.pack()

# additional checkboxes
check_var_new = tk.IntVar(value = 10)
check_new1 = ttk.Checkbutton(
    window, 
    text = 'Freshbox 1', 
    command = lambda: print(check_var_new.get()), 
    variable = check_var_new,
    onvalue = 10,
    offvalue = 5) 
check_new1.pack()

check_new1 = ttk.Checkbutton(
    window, 
    text = 'Freshbox 2', 
    command = lambda: print(check_var_new.set(5))) # unchecks first checkbox 
check_new1.pack()

# exercise
exercise_boolean = tk.BooleanVar()
exercise_check = ttk.Checkbutton(
    window,
    text = 'Exercise Check',
    variable = exercise_boolean,
    command = lambda: print(exercise_rad_var.get()) if exercise_boolean.get() else None)
exercise_check.pack()

exercise_rad_var = tk.StringVar()
exercise_radio1 = ttk.Radiobutton(
    window, 
    text = 'Exercise Radio 1', 
    value = 'A', 
    command = lambda: print(exercise_boolean.get(), exercise_boolean.set(False)), # prints True/False None, lambda clearly not working here
    variable = exercise_rad_var)
exercise_radio1.pack()

exercise_radio2 = ttk.Radiobutton(
    window, 
    text = 'Exercise Radio 2', 
    value = 'B', 
    command = lambda: print(exercise_boolean.get(), exercise_boolean.set(False)), # prints True/False None, lambda clearly not working here
    variable = exercise_rad_var)
exercise_radio2.pack()

# the way it was written by Clear Code:
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

# data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
answer_check = ttk.Checkbutton(window, text = 'exercise check', variable = check_bool, command = lambda: print(radio_string.get()))
answer_radio1 = ttk.Radiobutton(window, text = 'Radio A', value = 'A', command = radio_func, variable = radio_string)
answer_radio2 = ttk.Radiobutton(window, text = 'Radio B', value = 'B', command = radio_func, variable = radio_string)

# layout
answer_check.pack()
answer_radio1.pack()
answer_radio2.pack()


# run
window.mainloop()

# exercise
# create another checkbutton and 2 radiobuttons
# radio button:
    # values for the buttons are A and B
    # ticking either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton
# check button:
    # ticking the checkbutton prints the value of the radio button value
    # use tkinter var for Booleans