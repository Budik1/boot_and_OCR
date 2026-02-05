from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import baza_dannyx as b_d


class Window(Tk):
    def __init__(self, width_tool, height_tool, position_x_tool, position_y_tool):
        super().__init__()
        height_tool = b_d.line5
        # конфигурация окна
        self.title("окно настроек")
        self.geometry(f'{width_tool}x{height_tool}+{position_x_tool}+{position_y_tool}')

        # определение кнопки
        self.button = ttk.Button(self, text="закрыть")
        self.button["command"] = self.button_clicked
        self.button.place(x=b_d.col_0, y=height_tool - b_d.height_line)

    def button_clicked(self):
        self.destroy()
