from tkinter import *
from tkinter import ttk

from baza import baza_dannyx as b_d
from baza import variables as var


class Window(Toplevel):
    def __init__(self,root, width_tool, position_x_tool, position_y_tool):
        super().__init__()
        # self.def_rap = 0
        self.height_tool = b_d.line5
        # конфигурация окна
        self.title("окно настроек")
        self.geometry(f'{width_tool}x{self.height_tool}+{position_x_tool}+{position_y_tool}')

        self.def_rap = IntVar()

        # кнопки
        self.but_close = ttk.Button(self, text="закрыть")
        self.but_close["command"] = lambda: self.destroy()
        self.but_close.place(x=b_d.col_0, y=self.height_tool - b_d.height_line)

        self.but_def_rapport = ttk.Button(self, text='вызов функций')
        self.but_def_rapport["command"] = self.change_def_rapport_
        self.but_def_rapport.place(x=b_d.col_0, y=b_d.line0)

        # label
        self.lbl_def_rapport = ttk.Label(self, textvariable=self.def_rap)
        self.lbl_def_rapport.place(x=b_d.col_0, y=b_d.line1)
        # print(f"{var.Parameters.def_rapport=}")


    # @staticmethod
    def change_def_rapport_(self):
        if var.Parameters.def_rapport:
            var.Parameters.def_rapport = 0
        else:
            var.Parameters.def_rapport = 1
        self.def_rap.set(var.Parameters.def_rapport)
        print(var.Parameters.def_rapport)


