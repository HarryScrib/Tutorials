import tkinter as tk
from tkinter import ttk

# this function will return None, because we don't define a return value
def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())

# setup
window = tk.Tk()
window.title('Buttons, Functions & Arguments')

# widgets
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

# python runs top to bottom. when it sees us calling the function below, it does so when we create the button. this is not what we want
button = ttk.Button(window, text = 'button', command = button_func(entry_string))
button.pack()
# as a consequence, we see nothing when we press the button. all we get is 'a button was pressed' and 'test' when we start the program.

# one fix for this is to use lambda
# the reason this works is because the lambda function, by default, is not being called, meaning the lambda triggers the call, and the command sees the call
lambda_button = ttk.Button(window, text = 'working button', command = lambda: button_func(entry_string))
lambda_button.pack()

# if we insist on not using a lambda function, and would just like to use a function, we are going to have to use essentially a nested function
def outer_func(parameter):
    def inner_func():
        print('a button will work like this')
        print(parameter.get())
    return inner_func

# from what i understand, the reason this works is because we create inner_func when we create the button i_hate_lambda_button, as outer_func is automatically called
i_hate_lambda_button = ttk.Button(window, text = 'nested button', command = outer_func(entry_string))
i_hate_lambda_button.pack()


# run
window.mainloop()