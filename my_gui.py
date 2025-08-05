from PyQt5 import QtWidgets

import mini_gui
import fun
import revision_tents
import heroes
from heroes import Activ
import complex_phrases

vip_case_all = 0

def tent_inspection():
    while True:
        revision_tents.qty_vip()


class ExampleApp(QtWidgets.QMainWindow, mini_gui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mini_gui.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.vip_q = ""
        self.Button.clicked.connect( tent_inspection)
        self.label.setText(self.vip_q)

def main():
    app = QtWidgets.QApplication([])  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

main()