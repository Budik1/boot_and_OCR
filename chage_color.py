from tkinter import *

import fun



def changeColor():
    her = fun.selection_hero()

    if her == 'Gady':
        label.configure(bg="purple")
    else:
        label.configure(bg="blue")


root = Tk()
root.title("Push event")

label = Label(text="")
label.configure(text="msg will change push")
label.pack(side=LEFT, ipadx=5, ipady=5)

Button(text='push', command=changeColor).pack()

root.mainloop()
