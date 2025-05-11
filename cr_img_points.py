import pyautogui
import fun
from time import sleep


def b_arrow_right():
    pos_button = fun.locCenterImg('img/arena/hall_of_glory_icon.png', 0.9)
    fun.move_mause(pos=pos_button)
    x, y = pos_button
    x -= 108
    y += 585
    fun.move_mause(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 44
    change_y = 50
    x_demo += change_x
    y_demo += change_y
    fun.move_mause(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/b_arrow_right.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/overall/b_arrow_right.png')
    fun.move_mause(pos=pos)
    print('foto ok')
    return


def b_arrow_left():
    pos_button = fun.locCenterImg('img/arena/hall_of_glory_icon.png', 0.9)
    fun.move_mause(pos=pos_button)
    x, y = pos_button
    x -= 833
    y += 585
    fun.move_mause(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 44
    change_y = 50
    x_demo += change_x
    y_demo += change_y
    fun.move_mause(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/b_arrow_left.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/overall/b_arrow_left.png')
    fun.move_mause(pos=pos)
    print('foto ok')
    return


def b_begin():
    pos_button = fun.locCenterImg('img/arena/hall_of_glory_icon.png', 0.9)
    fun.move_mause(pos=pos_button)
    x, y = pos_button
    x -= 833
    y += 665
    fun.move_mause(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 44
    change_y = 40
    x_demo += change_x
    y_demo += change_y
    fun.move_mause(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/b_begin.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/overall/b_begin.png')
    fun.move_mause(pos=pos)
    print('foto ok')
    return


def energy_value_img(*, line, name_fi):
    """
    1 line  x += 480  y += 143
    2 line  x += 480  y += 143 + 103
    3 line  x += 480  y += 143 + 103 + 103
    """
    pos = fun.locCenterImg('img/station_master.png')
    fun.move_mause(pos=pos)
    x, y = pos
    x += 480 + 20
    y += 45 + (103 * line)
    # fun.move_mause(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 88 - 20
    change_y = 40 - 5
    x_demo += change_x
    y_demo += change_y
    # fun.move_mause(pos=(x_demo, y_demo))
    fun.foto(f'img/stationmaster/energy_indicator/en{name_fi}.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/stationmaster/energy_indicator/en{name_fi}.png', confidence=0.95)
    fun.move_mause(pos=pos)
    print(f'foto en{name_fi}.png ok')
    return


energy_value_img(line=1, name_fi=1)
