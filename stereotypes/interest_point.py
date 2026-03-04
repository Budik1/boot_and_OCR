import os_action
import tools

import fun
from find_img import find_img

DEFAULT_DISTANCE = 760


def get_left_corner() -> tuple:
    """
    Отправная точка всех построений.
    :return:
    :return:
    """
    'img/mark_scale/corner/mark_left.png'
    pos = fun.locCenterImg(name_img='./img/mark_scale/corner/mark_left.png', confidence=0.99)
    x, y, = pos
    x -= 7
    y += 2
    left_corner = x, y
    return left_corner


def get_right_corner() -> tuple:
    pos = fun.locCenterImg(name_img='./img/mark_scale/corner/mark_right.png', confidence=0.99)
    x, y, = pos
    x += 8
    y += 2
    right_corner = x, y
    return right_corner


def get_caliber_corner():
    """
    Определение масштаба через расстояние между углами.
    :return:
    """
    left_corner = get_left_corner()
    right_corner = get_right_corner()
    if left_corner and right_corner:
        x_left_cor, y_left = left_corner
        x_right_cor, y_right = right_corner
        if x_left_cor < x_right_cor:
            distance = x_right_cor - x_left_cor
        else:
            distance = x_left_cor - x_right_cor
    else:
        print("углы не определены")
        distance = DEFAULT_DISTANCE
    caliber = int((distance / DEFAULT_DISTANCE) * 100)
    return caliber

def get_caliber_line():
    path_img_caliber = 'img/mark_scale/line'
    lst_img = os_action.get_lst_files(path=path_img_caliber)
    skale = None
    for img in lst_img:
        rez = find_img(img)
        if rez:
            skale = fun.extraction_digit(item=img)
    return skale


def cr_img():
    target_img = "None"
    # смещение по х, смещение по у, ширина, высота
    img_dict = {
        'hero_fase': [((8 + 6), (8 + 6), (70 - 6 * 2), (70 - 6 * 2)), ['gady', 'gavr', 'mara']]
    }
    target_img = './img/test/token.png'
    #
    key = 'hero_fase'
    pos_start = get_left_corner()
    lst_offsets = img_dict[key][0]
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += lst_offsets[0]
    y += lst_offsets[1]
    # fun.Mouse.move(pos=(x, y), speed=1)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = lst_offsets[2]
    change_y = lst_offsets[3]
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    if target_img == './img/test/token.png':
        fun.foto(f'{target_img}', (x, y, change_x, change_y))
        print(f'{target_img} сделан')
    else:
        answer = input(f"{key} Как сохранить? Варианты 1: ")
        if answer == 'y':
            fun.foto(f'{key}', (x, y, change_x, change_y))
            print(f'{key} сделано')
        else:
            print("выход без создания снимка")
    # sounds.sound_vic(block=False)


def cr_img_line_button_pm(show=False):
    left_cor = get_left_corner()
    caliber = get_caliber_corner()
    name_file_line_scale = f'line_button_pm_{caliber}.png'
    path_scale = f'img/mark_scale/line/'
    os_action.create_folder(path=path_scale)

    x, y = left_cor
    x += 220 * (caliber / 100)
    y -= 130 * (caliber / 100)
    tools.Mouse.move(pos=(x, y), speed=1, show=show)
    x_demo, y_demo = x, y
    change_x = 365 * (caliber / 100)
    change_y = 30 * (caliber / 100)
    x_demo += change_x
    y_demo += change_y
    tools.Mouse.move(pos=(x_demo, y_demo), speed=1, show=show)
    if not os_action.check_folder_or_file(my_path=f'{path_scale}{name_file_line_scale}'):
        fun.foto(path_name=f'{path_scale}{name_file_line_scale}', region=(x, y, change_x, change_y))


get_caliber_line()