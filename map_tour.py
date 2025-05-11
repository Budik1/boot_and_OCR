import tkinter

import baza_dannyx as b_d
from tkinter import Tk
from tkinter import ttk
import sys


def butt_exit():
    root.destroy()
    sys.exit()

# print(len(b_d.list_of_stations))
def ret_name_station(event):
    b_d.states_select = combo.get()


def but_print():
    print(b_d.states_select)


def get_list_name_station():
    list_name_station_ = ['домой']
    for name in range(len(b_d.list_of_stations)):
        list_name_station_ += [b_d.list_of_stations[name][0]]
    return list_name_station_


root = Tk()
# root.geometry('400x400')

list_name_station = get_list_name_station()

ttk.Button(text='Exit', command=butt_exit).pack(fill=tkinter.X)
ttk.Button(text='Print', command=but_print).pack(fill=tkinter.X)


combo = ttk.Combobox(values=list_name_station, width=30,state="readonly")
combo.current(0)
combo.pack(side=tkinter.LEFT)
combo.bind("<<ComboboxSelected>>", ret_name_station)

root.mainloop()

get_list_name_station()
