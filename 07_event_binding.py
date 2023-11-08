import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

# events
# we need to specify event otherwise tkinter automatically inserts an argument into lambda function
button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# a good way to visualise events is to make use of Motion
text.bind('<Motion>', get_pos)
# you also don't need to specify the type of keypress, you can check for any kind of keypress, along with the character itself
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
# let's say we want to check if the user has selected the entry field
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
# likewise it works with out
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# exercise event

text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# run
window.mainloop()

# exercise
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected