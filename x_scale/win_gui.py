from tkinter import *
import fun
import stereotypes
from baza import baza_dannyx as b_d


screen_width, screen_height = fun.screen_size()  # получение разрешения экрана
right_indent = 50  # отступ от правого края экрана
top_indent = 50  # отступ от верхнего края экрана

width_root = b_d.lst_columns_root[-1] + 73  # Ширина окна Tk
height_root = b_d.line9 + b_d.height_line + 2  # Высота окна Tk

position_y_root = top_indent  # отступ от верхнего края экрана для окна root
position_x_root = screen_width - width_root - right_indent  # отступ от правого края экрана для окна root

width_tool = width_root
height_tool = height_root
position_y_tool = top_indent * 2 + height_root
position_x_tool = position_x_root

# класс окна 'помощник "Метро 2033"'
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('parent')
        self.master.geometry(f'{width_root}x{height_root}+{position_x_root}+{position_y_root}')
        self.master.resizable(False, False)

        self.master.mainloop()

# класс окна калибровка sizing
class Sizing:
    def __init__(self, master):
        self.master = master
        self.master.title('Калибровка')
        self.master.geometry(f'{width_tool}x{height_tool}+{position_x_tool}+{position_y_tool}')
        self.skale = stereotypes.interest_point.get_caliber_corner()
        self.one_scr_mess = 'Окно станции'


        self.master.mainloop()

root = Tk()
Sizing(root)