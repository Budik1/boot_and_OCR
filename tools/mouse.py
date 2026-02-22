import pyautogui
import builtins
import os_action
from .time_processing import *
from . import sounds
from baza import baza_paths as b_p
from time import sleep


def my_log_file(text):
    date_ = date_now()
    time_ = time_now()
    date_time = f'{date_} {time_}'
    path_file = b_p.log_path
    os_action.create_folder(path=path_file)
    file_name = date_ + ".txt"
    file_1 = open('txt/log/' + str(file_name), 'a+', encoding='utf-8')
    try:
        # print = print()
        builtins.print(date_time, text, file=file_1)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        builtins.print(f"Файл '{file_1}' не найден!")
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        builtins.print("Произошла ошибка ввода-вывода при чтении файла!")
    except Exception as e:
        # Обработка других неожиданных исключений
        builtins.print(f"Произошла неожиданная ошибка: {e}")
    finally:
        file_1.close()
    return


class Mouse:

    @staticmethod
    def position_print():
        print()
        print('position()')
        print(pyautogui.position())

    @staticmethod
    def move(*,
             pos: tuple,
             speed=0.2,
             show=True,
             log=True,
             message_l=None) -> None:
        """

        :param pos:
        :param speed:
        :param show:
        :param log:
        :param message_l:
        :return:
        """
        my_log_file('')
        my_log_file(f'tolls.mouse.Mouse.move {message_l}')
        my_log_file(f'{pos=}')
        if log:
            print(f'tolls.mouse.Mouse.move {message_l=}')
        if show:
            pyautogui.moveTo(pos, duration=speed)
        return

    @staticmethod
    def move_to_click(*,
                      pos_click: tuple,
                      move_time: float = 0.75,
                      z_p_k: float = 0.05,
                      log=True,
                      message_l=None) -> None:
        """
        Поместить указатель мыши по координатам и кликнуть, учитывая задержку.

        :param pos_click: Point
        :param move_time: время перемещения указателя мыши в секундах
        :param z_p_k: задержка перед кликом(float)
        :param log:
        :param message_l: цель клика
        :return: None
        """
        my_log_file(f'tolls.mouse.Mouse.move_to_click {message_l=}, {pos_click=}')
        if log:
            print(f'tolls.mouse.Mouse.move_to_click {message_l=}, {pos_click=}')
        sleep(0.3)
        Mouse.move(pos=pos_click, speed=move_time)
        # print('должен быть клик')
        sleep(z_p_k)
        Mouse.left_click(pos=pos_click)
        sleep(0.18)
        return

    @staticmethod
    def left_click(*,
                   pos: tuple,
                   log=False,
                   message_l=None) -> None:
        """

        :param pos:
        :param log:
        :param message_l:
        :return:
        """
        my_log_file('')
        my_log_file(f'tolls.mouse.Mouse.left_click {message_l}')
        my_log_file(f' {pos=}')
        if log:
            print(f'tolls.mouse.Mouse.left_click {message_l=}')
        sounds.click_mouse()
        pyautogui.hotkey('Ctrl')
        pyautogui.click(pos)
        return

    @staticmethod
    def take_drag_drop_y(*,
                         pos_take: tuple,
                         distance: int,
                         speed=0.2, ) -> None:
        """

        :param pos_take:
        :param distance:
        :param speed:
        :return:
        """
        pyautogui.mouseDown(pos_take)
        x, y = pos_take
        y += distance
        new_pos = x, y
        Mouse.move(pos=new_pos, speed=speed)
        pyautogui.mouseUp()
        return

    @staticmethod
    def take_drag_drop(*,
                       pos_take: tuple,
                       pos_drop: tuple,
                       speed: float = 0.2,
                       log=False,
                       message_l=None) -> None:
        """

        :param pos_take:
        :param pos_drop:
        :param speed:
        :param log:
        :param message_l:
        :return:
        """
        my_log_file(f'tolls.mouse.Mouse.take_drag_drop {message_l}')
        if log:
            print(f'tolls.mouse.Mouse.take_drag_drop {message_l=}')
        pyautogui.mouseDown(pos_take)
        Mouse.move(pos=pos_drop, speed=speed)
        pyautogui.mouseUp()
        return
