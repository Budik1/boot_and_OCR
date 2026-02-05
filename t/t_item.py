from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self, name_win):
        super().__init__()

        # конфигурация окна
        self.title(name_win)
        self.geometry("250x200")

        # определение кнопки
        self.button_cl = ttk.Button(self, text="закрыть")
        self.button_cl["command"] = self.button_destroy
        self.button_cl.place(x=50, y=10)

        self.button_cr = ttk.Button(text="Создать окно")
        self.button_cr['command'] = self.click
        self.button_cr.place(x=10, y=100)

    def button_destroy(self):
        self.destroy()


    def click(self):
        window = Window(name_win='новое окно')



root = Window(name_win="главное окно")

root.mainloop()
