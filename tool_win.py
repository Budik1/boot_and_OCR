from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk

from baza import baza_dannyx as b_d
from baza import variables as var


class Window(Tk):
    def __init__(self, width_tool, position_x_tool, position_y_tool):
        super().__init__()
        height_tool = b_d.line5
        # конфигурация окна
        self.title("окно настроек")
        self.geometry(f'{width_tool}x{height_tool}+{position_x_tool}+{position_y_tool}')

        # определение кнопки
        self.button = ttk.Button(self, text="закрыть")
        self.button["command"] = self.button_clicked
        self.button.place(x=b_d.col_0, y=height_tool - b_d.height_line)

        self.enabled = StringVar()
        self.enabled_checkbutton = ttk.Checkbutton(self, text="Включить",
                                                   # offvalue="Отключено", onvalue="Включено",
                                                   variable=self.enabled,
                                                   command=self.check_changed)
        # self.enabled_checkbutton["command"] = self.check_changed
        self.enabled_checkbutton.place(x=b_d.col_0, y=b_d.line0)

        self.enabled_lbl = ttk.Label
        self.en_lbl()

    def button_clicked(self):
        self.destroy()

    def check_changed(self):
        print(f"{self.enabled.get()=}")

    def en_lbl(self):
        self.enabled_lbl = ttk.Label(self, textvariable=self.enabled)
        self.enabled_lbl.place(x=b_d.col_0, y=b_d.line1)
        print(f"{self.enabled.get()=}")
