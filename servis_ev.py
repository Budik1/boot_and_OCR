from tkinter import *

import fun





def changeColor():
    her = fun.selection_hero()

    if her == 'Gady':
        label_1.configure(bg="purple")
        it1_stat.set(her)
    else:
        label_1.configure(bg=None)
        it1_stat.set('')
    if her == 'Gavr':
        label_2.configure(bg="purple")
        it2_stat.set(her)
    else:
        label_2.configure(bg=None)
        it2_stat.set('')
    if her == 'Велес':
        label_3.configure(bg="purple")
        it3_stat.set(her)
    else:
        label_3.configure(bg=None)
        it3_stat.set('')
    if her == 'Mara':
        label_4.configure(bg="purple")
        it4_stat.set(her)
    else:
        label_4.configure(bg=None)
        it4_stat.set('')





root = Tk()
root.title('servise')
root.geometry('300x200+1200+400')
it1_stat = StringVar()
it2_stat = StringVar()
it3_stat = StringVar()
it4_stat = StringVar()

Button(text=' 1 ', width=3, command=changeColor).place(x=0, y=0)
Button(text=' 2 ', width=3, command=changeColor).place(x=0, y=40)
Button(text=' 3 ', width=3, command=changeColor).place(x=0, y=80)
Button(text=' 4 ', width=3, command=changeColor).place(x=0, y=120)

label_1 = Label()
label_1.configure(textvariable=it1_stat, width=8)
label_1.place(x=50, y=0)

label_2 = Label()
label_2.configure(textvariable=it2_stat, width=8)
label_2.place(x=50, y=40)
#
label_3 = Label()
label_3.configure(textvariable=it3_stat, width=8)
label_3.place(x=50, y=80)
#
label_4 = Label()
label_4.configure(textvariable=it4_stat, width=8)
label_4.place(x=50, y=120)

root.mainloop()
