from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import os

import fun
import station_master
import baza_dannyx as b_d
import baza_paths as b_p
import heroes
import create_and_analiz_task_img

import stereotypes


height_line =24
line_0 = 0
line_1 = height_line
line_2 = height_line * 2

root = Tk()
root.title(' помощник создания картинок')
root.geometry(f'400x400+1200+450')  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

oko_hero_label = ttk.Label()
oko_hero_label.config(text='Создано картинок -')
oko_hero_label.place(x=0, y=line_0)

ttk.Button(text='Имя персонажа', width=15).place(x=0, y=line_1)
ttk.Button(text='Имя персонажа', width=15).place(x=0, y=line_2)


root.mainloop()
