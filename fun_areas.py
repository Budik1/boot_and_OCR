import pyautogui
import datetime
from time import sleep, time

# import fun
import sounds
import find_img
import fun_down
import baza_dannyx as b_d
import color_text

import heroes

par_conf = 0.79
oblast = (51, 707, 92, 111)


def get_areas_task_small(width=77, height=42):
    """Получение значений "region=" для поиска значений в малых регионах пуль и опыта
        :return: кортеж из шести списков значений"""
    my_log_file('fun.get_areas_task_small')
    pul, xp_ = 404 - 34 - 10 + 1, 518 - 40 - 34 - 10 - 10 + 2
    line_1, line_2, line_3 = 160, 250, 340

    x_or, y_or = find_link_station_master_alt()

    x_an_xp = x_or + xp_
    x_an_pul = x_or + pul

    # регион поиска 1 (позиция анализа)
    y_1an = y_or + line_1
    region1_pul = [x_an_pul, y_1an, width, height]
    region1_xp = [x_an_xp, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = y_or + line_2
    region2_pul = [x_an_pul, y_2an, width, height]
    region2_xp = [x_an_xp, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = y_or + line_3
    region3_pul = [x_an_pul, y_3an, width, height]
    region3_xp = [x_an_xp, y_3an, width, height]

    return region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp


def get_areas_task_big_1_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_1')
    # width, height = 77, 42
    pul = 404
    pos_1 = 190
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul
    width += big
    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region_big_1 = [x_an_pul, y_1an, width, height]
    return region_big_1


def get_areas_task_big_2_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_2')
    # width, height = 77, 42
    pul = 404
    pos_2 = 280
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul  # начальная точка
    width += big  #
    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region_big_2 = [x_an_pul, y_2an, width, height]
    return region_big_2


def get_areas_task_big_3_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_2')
    # width, height = 77, 42
    pul = 404
    pos_3 = 370
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul  # начальная точка
    width += big  #
    # регион поиска 2 (позиция анализа)
    y_3an = int(y_or + pos_3)
    region_big_3 = [x_an_pul, y_3an, width, height]
    return region_big_3


def get_areas_task_big(width=77, height=42, refactor=None):
    """Получение значений "region=" для поиска заданий в больших регионах
        :return: кортеж из трех списков значений"""
    my_log_file('')
    my_log_file('fun.get_areas_task_big')
    # my_print_to_file('fun.get_areas_task_big')
    # print('')
    pul = 370
    # pos_1, pos_2, pos_3 = 217, 320, 423
    pos_1, pos_2, pos_3 = 160, 250, 340
    big = 56  # 56

    x_or, y_or = find_link_station_master_alt()
    x_an_pul = x_or + pul
    width += big
    if refactor:
        # print(f'{x_or=}, {y_or=}')
        Mouse.move(pos=(x_or, y_or))
        # print(f'{x_or=}, {y_or=}, {x_an_pul=}, {width}')

    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region1_big = [x_an_pul, y_1an, width, height]
    if refactor:
        # fun.Mouse.move(pos=(x_an_pul, y_1an))
        # print(f'fun.get_areas_task_big {region1_big=}')
        # print()
        name_create_img = 'img/test/areas_task1.png'
        foto(f'{name_create_img}', (x_an_pul, y_1an, width, height))

    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region2_big = [x_an_pul, y_2an, width, height]
    if refactor:
        name_create_img = 'img/test/areas_task2.png'
        foto(f'{name_create_img}', (x_an_pul, y_2an, width, height))

    # регион поиска 3 (позиция анализа)
    y_3an = int(y_or + pos_3)
    region3_big = [x_an_pul, y_3an, width, height]
    if refactor:
        name_create_img = 'img/test/areas_task3.png'
        foto(f'{name_create_img}', (x_an_pul, y_3an, width, height))

    return region1_big, region2_big, region3_big


