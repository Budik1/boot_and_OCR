import time

import fun

from baza import baza_paths as b_p
import tools
# from tools import sounds

line_1, line_2, line_3 = 217, 320, 423
xp_ = 548
shift_up = 35
change_x = 40  # 17
change_y = 23





def arial_task():
    """
    Создание полной картинки заданий
    :return:
    """
    # big_task: str = 'img/test/test_tasks/'
    path_img = b_p.task_big
    name_img = 'arial_task.png'

    show_move = True
    pos_start = fun.find_link_station_master()
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 270 - 6
    y += 152 - 2
    # fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x_full = 268  # - 6
    change_y_full = 260  # - 2
    x_demo += change_x_full
    y_demo += change_y_full
    # fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    'img/ test/ test_tasks/arial_task.png'
    fun.foto(f'{path_img}{name_img}', (x, y, change_x_full, change_y_full))
    # pos = fun.locCenterImg(f'{path_img}{name_img}')
    # fun.Mouse.move(pos=pos)
    # sounds.sound_vic(block=False)
    print(f'{path_img}{name_img} создан')
    print('ok')
    # print(x, y, change_x, change_y)
    return x, y, change_x_full, change_y_full


def get_price_energy():
    path_energy_task = b_p.energy_task_value
    list_energy = ['en_1.png', 'en_2.png', 'en_3.png', 'en_7.png', ]
    region_img = arial_task()
    for img in list_energy:
        pos_en = fun.locCenterImg(f'{path_energy_task}{img}', region=region_img)
        if pos_en:
            print(fun.extraction_digit(item=img))
            tools.Mouse.move(pos=pos_en, speed=0.5)
            time.sleep(1)


def region_task_line():
    # big_task = 'img/test/test_tasks/'
    path_img = b_p.task_big
    name_img1 = 'arial_task_line_1.png'
    show_move = True
    change_x = 270
    # change_y = 103
    change_y = 80
    # шаг 103
    pos_start = fun.find_link_station_master()
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 268
    y += 152
    # fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    x_demo, y_demo = x, y

    x_demo += change_x
    y_demo += change_y
    tools.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    fun.foto(f'{path_img}{name_img1}', (x, y, change_x, change_y))
    #
    name_img2 = 'arial_task_line_2.png'
    x, y = pos_start
    x += 268
    y += 152 + 90
    # fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    x_demo, y_demo = x, y
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    fun.foto(f'{path_img}{name_img2}', (x, y, change_x, change_y))
    #
    name_img3 = 'arial_task_line_3.png'
    x, y = pos_start
    x += 268
    y += 152 + 90 + 90
    # fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    x_demo, y_demo = x, y
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    fun.foto(f'{path_img}{name_img3}', (x, y, change_x, change_y))
