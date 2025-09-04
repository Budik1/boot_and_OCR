from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import os

import fun
import station_master
import baza_dannyx as b_d
import baza_paths as b_p
import heroes
import create_and_analiz_img


def changeColor(*, her_active):
    """
    Меняет цвет поля активного героя
    """
    if her_active == 'Gady':
        label_1.configure(background="yellow")
    else:
        label_1.configure(background='white')
    if her_active == 'Gavr':
        label_2.configure(background="yellow")
    else:
        label_2.configure(background='white')
    if her_active == 'Велес':
        label_3.configure(background="yellow")
    else:
        label_3.configure(background='white')
    if her_active == 'Mara':
        label_4.configure(background="yellow")
    else:
        label_4.configure(background='white')
    return


def who_is_this():
    # img/test/test_tasks/task/Mara
    # img/test/test_tasks/task/mara
    name_hero = fun.selection_hero()
    path = f'{b_p.task_hero}{heroes.Activ.name_file_}'
    print(path)
    changeColor(her_active=name_hero)
    return


def form_path_name_file():
    """
    Создание пути сохранения файла по имени героя.
    :return:
    """
    if heroes.Activ.hero_activ_name:
        name_file = ''
        if name_file_line_1.get():
            name_file = name_file_line_1.get()
        elif name_file_line_2.get():
            name_file = name_file_line_2.get()
        elif name_file_line_3.get():
            name_file = name_file_line_3.get()
        path_file = f'img/station_master/test_tasks_{heroes.Activ.hero_activ_name}/{name_file}.png'
        print(f'{path_file=}')
    return


def info_name_file():
    fun.selection_hero(show_name=False)
    path_energy_task = b_p.task_hero
    path_energy_task_hero = f'{path_energy_task}{heroes.Activ.hero_activ_name}/'
    files = os.listdir(path_energy_task_hero)
    print(files)


root = Tk()
root.title(' помощник "Метро 2033"')
root.geometry(f'365x362+1200+450')  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

name_file_line_1 = StringVar()
name_file_line_2 = StringVar()
name_file_line_3 = StringVar()

w_l = 8
step = 30
line_0 = step * 0
line_1 = step * 1
line_2 = step * 2
line_3 = step * 3
line_4 = step * 4
line_5 = step * 5
line_6 = step * 6

step_tab = 90
sh = 4
rev = 20

tab_0 = sh + step_tab * 0
tab_1 = sh + step_tab * 1
tab_2 = sh + step_tab * 2
tab_3 = sh + step_tab * 3

label_1 = ttk.Label()
label_1.configure(text="gady", borderwidth=2, relief="ridge", padding=5, width=w_l)
label_1.place(x=tab_0, y=line_0)

label_2 = ttk.Label()
label_2.configure(text='gavr', borderwidth=2, relief="ridge", padding=5, width=w_l)
label_2.place(x=tab_1, y=line_0)

label_3 = ttk.Label()
label_3.configure(text='veles', borderwidth=2, relief="ridge", padding=5, width=w_l)
label_3.place(x=tab_2, y=line_0)

label_4 = ttk.Label()
label_4.configure(text='mara', borderwidth=2, relief="ridge", padding=5, width=w_l)
label_4.place(x=tab_3, y=line_0)

ttk.Button(text='Кто?', width=4, command=who_is_this).place(x=tab_0, y=line_2)
ttk.Label(text='строка и имя файла', width=21, background='#858585', foreground='#050505').place(x=tab_1, y=line_2)

ttk.Button(text='строка 1', width=7, command=form_path_name_file).place(x=tab_1, y=line_3)
ttk.Button(text='строка 2', width=7, command=form_path_name_file).place(x=tab_1, y=line_4)
ttk.Button(text='строка 3', width=7, command=form_path_name_file).place(x=tab_1, y=line_5)
ttk.Button(text='состояние', width=7, command=info_name_file).place(x=tab_1, y=line_6)

ttk.Entry(textvariable=name_file_line_1, width=3).place(x=tab_2, y=line_3)
ttk.Entry(textvariable=name_file_line_2, width=3).place(x=tab_2, y=line_4)
ttk.Entry(textvariable=name_file_line_3, width=3).place(x=tab_2, y=line_5)

line_img = b_d.line5 + 5
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=create_and_analiz_img.analiz_task).place(x=tab_0, y=line_3)
# ttk.Button(root, image=imagePul, command=station_master.option_task_money).place(x=tab_0, y=line_3)

root.mainloop()
