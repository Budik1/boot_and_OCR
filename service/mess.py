from tkinter import *

index = 0


def changeColor():
    global index
    if index % 2 == 0:
        label.configure(bg="purple")
    else:
        label.configure(bg="blue")
    index += 1


root = Tk()
root.title("Push event")

label = Label(text="")
label.configure(text="msg will change push")
label.pack(side=LEFT, ipadx=5, ipady=5)

Button(text='push', command=changeColor).pack()

root.mainloop()
