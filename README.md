### Tutorials from YouTube

## Overview

I have been watching these YouTube video from Clear Code and b001:

- The ultimate introduction to modern GUIs in Python [ with tkinter ]
- https://www.youtube.com/watch?v=mop6g-c5HEY

- Python Lambda Functions??
- https://www.youtube.com/watch?v=KR22jigJLok

I am just writing everything out alongside my viewing to better understand what I am being taught. Following my recent attempt at a project, I know that I need to better understand UI development. This is my exploration into that.
I will catalogue everything in this repository as I am learning it, so that I may refer to it easily for later use.

## Understanding and Reasoning, a necessary reminder

Widgets are the building blocks of tkinter. Understanding the widgets and controlling them is key to mastering any gui framework. Having a solid understanding of how to do so will help me save so much time in the future if I am able to put apps together without much need for googling such things. Thankfully this is mutually transferable knowledge and can be applied to other things such as React. 

Within Tkinter we have 2 sets of widgets:

- tk widgets (originals)
- ttk widgets (modern and more stylised, and are mainly what should be used)

There are 2 major ways to get data from a widget:

- tkinter variables (use most of the time)
- get() method

Lots of widgets have obvious data that the user would want to get. Hence, there is a get method. For example, entry has a get method that returns its text, and this is the easiest way to get data from a widget. It is important to note that most widgets do not have a get() method however. Every widget has a config method, and we can use this to update them, at least in a basic way, which can be shorthanded:

- Label.configure(text = 'some new text')
- Label['text'] = 'some new text'

We get the widget, then we pass a named argument, in this case 'text' which is the same as text= in the former example, and then we can assign whatever new value we would like to assign to it.
Tkinter has a bunch of inbuilt variables that are designed to work really well with widgets. These are automatically updated by a widget and they update the contents of a widget. Fundamentally, they still store basic data structures, using strings, integers and booleans. For this we will need to create variables such as StringVar (string variables) or IntVar (int variables). These are used to automatically get the data from potentially an entry widget to update something like a label widget. It allows them to always be connected within a dynamic set and get relationship.

Within this lesson, we are introduced to 3 different major kinds of buttons. It's important to know these as to distinguish between them for their functional purposes within an application. To use these properly, it is mandatory to use tkinter variables.

These are:

- Button
- Checkbutton
- Radiobutton

We then covered functions with arguments inside of a button. Most of which has been covered, simply by using lambda: print functions, as the string is treated as an argument. Meaning lambda is the way to solve this. Alternatively it is possible to create a function that returns another function and incorporate arguments that way.

Following buttons and their functionality, we moved onto event binding. Events can be a lot of things, for example:

- Keyboard inputs
- A widget being changed
- A widget getting selected/unselected
- Mouse click/motion/wheel

What's super useful about these events is they can be observed and used. For example, run a function on a button press. These are very easy to use for the most part. Essentially, we just need to bind an event to a widget. For example:

- Widget.bind(event, function)
- Format: modifier-type-detail
- Example: window.bind('<Alt-KeyPress-a>', lambda event: print(event))
- Result: <KeyPress event send_event=True state=Mod1|0x20000 keysym=a keycode=65 char='a' x=220 y=331>
- https://www.pythontutorial.net/tkinter/tkinter-event-binding/ (website with all types of events)

The important part of this result, being char='a' x=220 y=331, as it tells us where on the widget, and what key is being pressed. window can be changed with button or etcetera.

Comboboxes and Spinboxes are fairly straightforward, I do however just want a quick reference to some syntax in setting up item lists within the boxes, using:

- combo['values'] = items
- combo.configure(values = items)

Whereby both of these function in the same way, much like how we had with labels. The first example is more concise and therefore more preferable.

Just knowing these few fundamentals have allowed me to understand much better what it is I am trying to create when engaging with interface qualities using python.

Furthermore, I included a secondary video just to introduce lambda functions to my portfolio of knowledge. I was using them in the previous function, but didn't inherently understand them particularly well. Ultimately, I now realise that they are functionally the same as a regular function. Lambda functions can only have single line expressions. It is assumed that whatever gets computed gets returned. They aren't bound to a name, and they are essentially anonymous functions. They aren't bound to an identifier. They can be assigned to a variable. Their core functionality is that they can be passed into a higher order function. A higher order function can take in another function as an input (in this case, a lambda function), or it may return a function as an output, or both.

## Exercises

- Basic Window and Widgets
- Getting and Setting Widget Data
- Tkinter Variables
- Lambda functions
- Buttons
- Functions With Arguments (Inside a Button)
- Event Binding
- Combobox and Spinbox
- Canvas


## Applications

- Simple Distance Conversion Calculator