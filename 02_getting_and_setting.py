import tkinter as tk
from tkinter import ttk

# create a button function that gets the data from the entry widget
def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update label simultaneously. every way works the same (although .config might be removed and configure should be used as default)
    label['text'] = entry_text # probably the one i will use going forward
    label.config(text = entry_text)
    label.configure(text = entry_text)

    # other examples of modifications
    entry['state'] = 'disabled' # determines if widget is enabled or disabled

# window
window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('500x500')

# widgets
label = ttk.Label(master = window, text = 'Label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'this is a button', command = button_func)
button.pack()

# create exercise button function
def exercise_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

exercise_button = ttk.Button(master = window, text = 'exercise button', command = exercise_func)
exercise_button.pack()

# if you want to know everything you can do with a widget, you can write:
print(label.configure())

# run
window.mainloop()

# exercise
# add another button that changes text back to 'some text' and that enables entry