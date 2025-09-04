import time

from scipy.fftpack import shift

import fun
import sounds

import baza_paths as b_p


def get_patron_img():
    path_img = b_p.num_path
    name_img = 'patron.png'
    show_move = False
    shift_left = 499
    shift_down = 225
    x_or, y_or = fun.find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + shift_left
    y = y_or + shift_down
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    time.sleep(2)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 25  # 17
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), speed=1, show=show_move)
    fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}{name_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('ok')


def nam_pos_line1(*, pos, name):
    path_img = b_p.num_path
    name_img = f'{name}.png'
    show_move = True
    region = fun.get_areas_task_big_1()
    pos_patron = fun.locCenterImg(name_img=f'{b_p.num_path}patron.png', region=region)
    if pos_patron:
        # показать пос привязки
        fun.Mouse.move(pos=pos_patron, show=show_move)
        # найти верхний левый угол и показать
        x, y = pos_patron
        if name == 1:
            shift_left = -(11 + 10 * pos)
        else:
            shift_left = -(14 + 10 * pos)
        shift_up = -11
        x += shift_left
        y += shift_up
        fun.Mouse.move(pos=(x, y), show=show_move)
        # найти правый нижний угол и показать
        if name == 1:
            change_x = + 7
        else:
            change_x = + 10
        change_y = + 22
        fun.Mouse.move(pos=(x + change_x, y + change_y), show=show_move)
        fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{path_img}{name_img}')
        fun.mouse_move(pos=pos)
        sounds.sound_vic()
        print('ok')
    else:
        print('no img')


def nam_pos_line2(*, pos, name):
    path_img = b_p.num_path
    name_img = f'{name}.png'
    show_move = True
    region = fun.get_areas_task_big_2()
    pos_patron = fun.locCenterImg(name_img=f'{b_p.num_path}patron.png', region=region)
    if pos_patron:
        # показать пос привязки
        fun.Mouse.move(pos=pos_patron, show=show_move)
        # найти верхний левый угол и показать
        x, y = pos_patron
        if name == 1:
            shift_left = -(14 + 10 * pos)
        else:
            shift_left = -(14 + 10 * pos)

        shift_up = -11
        x += shift_left
        y += shift_up
        fun.Mouse.move(pos=(x, y), show=show_move)
        # найти правый нижний угол и показать
        if name == 1:
            change_x = + 8
        else:
            change_x = + 10
        change_y = + 22
        fun.Mouse.move(pos=(x + change_x, y + change_y), show=show_move)
        fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{path_img}{name_img}')
        fun.mouse_move(pos=pos)
        sounds.sound_vic()
        print('ok')
    else:
        print('no img')


def nam_pos_line3(*, pos, name):
    path_img = b_p.num_path
    name_img = f'{name}.png'
    show_move = True
    region = fun.get_areas_task_big_3()
    pos_patron = fun.locCenterImg(name_img=f'{b_p.num_path}patron.png', region=region)
    if pos_patron:
        # показать пос привязки
        fun.Mouse.move(pos=pos_patron, show=show_move)
        # найти верхний левый угол и показать
        x, y = pos_patron
        shift_left = -(14 + 10 * pos)
        shift_up = -11
        x += shift_left
        y += shift_up
        fun.Mouse.move(pos=(x, y), show=show_move)
        # найти правый нижний угол и показать
        change_x = + 10
        change_y = + 22
        fun.Mouse.move(pos=(x + change_x, y + change_y), show=show_move)
        fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{path_img}{name_img}')
        fun.mouse_move(pos=pos)
        sounds.sound_vic()
        print('ok')
    else:
        print('no img')

# get_patron_img()
# nam_pos_line1(pos=3, name=1)
# nam_pos_line2(pos=1, name=6)
# nam_pos_line3(pos=2, name=7)

def find_img(*, name):
    path = b_p.num_path
    rp1, rp2, rp3, rxp1, rxp2, rxp3 = fun.get_areas_task_small()
    con = 0.84
    pos = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rp1)
    pos_xp = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rxp1)
    print(f'{pos=},   {pos_xp=}')
    print()
    pos = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rp2)
    pos_xp = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rxp2)
    print(f'{pos=},   {pos_xp=}')
    print()
    pos = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rp3)
    pos_xp = fun.locCenterImg(name_img=f'{path}{name}.png', confidence=con, region=rxp3)
    print(f'{pos=},   {pos_xp=}')

find_img(name=4)