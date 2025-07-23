import pyautogui

import find_img
import fun
import sounds
import find_img as find
from time import sleep

def dress():
    """
    образец
    """
    name_create_img = 'img/person/dress/slots/jacket_point.png'
    show_move = False
    pos_start = find.find_exit_person()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    # x += 251, y -= 486 верхний правый слот
    # x += 371, y -= 341 слот перчаток
    # x += 713, y -= 341 слот жакета
    # x += 175, y -= 232 слот брюки
    # x += 713, y += 125 слот обувь
    x += 713
    y -= 341
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 89
    change_y = 89
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return


def link_money_token():
    """
    образец
    """
    name_create_img = 'img/overall/link_money_token.png'
    # show_move = True
    # pos_start = find.find_my_game2()
    # # показать привязку
    # fun.mouse_move(pos=pos_start, speed=1)
    # # найдем верхний угол
    # x, y = pos_start
    # x -= 20
    # y += 25 + 6
    # fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    # x_demo, y_demo = x, y
    # change_x = 39
    # change_y = 51
    # x_demo += change_x
    # y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    # fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return

link_money_token()