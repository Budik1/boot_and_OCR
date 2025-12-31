import time
import fun
import sounds

import baza_paths as b_p


def get_energy_line_1_img():
    path_img = b_p.energy_task_value
    name_img = 'en_1.png'
    show_move = False
    xp_ = 518 + 30
    line_1, line_2, line_3 = 217, 320, 423
    shift_up = 35
    x_or, y_or = fun.find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + xp_
    y = y_or + line_1 - shift_up
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    time.sleep(2)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 40  # 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), speed=1, show=show_move)
    fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}{name_img}')
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')


def get_energy_line_2_img():
    path_img = b_p.energy_task_value
    name_img = 'en_4.png'
    show_move = False
    xp_ = 518 + 30
    line_1, line_2, line_3 = 217, 320, 423
    shift_up = 35
    x_or, y_or = fun.find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + xp_
    y = y_or + line_2 - shift_up
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    time.sleep(2)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 40  # 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), speed=1, show=show_move)
    fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}{name_img}')
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')


def get_energy_line_3_img():
    # energy_task_value: str = 'img/station_master/energy_value/'

    path_img = b_p.energy_task_value
    name_img = 'en_5.png'

    show_move = False
    xp_ = 518 + 30
    line_1, line_2, line_3 = 217, 320, 423
    shift_up = 35
    x_or, y_or = fun.find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + xp_
    y = y_or + line_3 - shift_up
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    time.sleep(2)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 40  # 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), speed=1, show=show_move)
    fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}{name_img}')
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')


def arial_task():
    # big_task: str = 'img/test/test_tasks/'
    path_img = b_p.task_big
    name_img = 'arial_task.png'

    show_move = True
    pos_start = fun.find_link_station_master()
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 270
    y += 152
    # fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 268
    change_y = 260
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    fun.foto(f'{path_img}{name_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}{name_img}')
    # fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')
    # print(x, y, change_x, change_y)
    return x, y, change_x, change_y


def get_price_energy():
    path_energy_task = b_p.energy_task_value
    list_energy = ['en_1.png', 'en_2.png', 'en_3.png', 'en_7.png', ]
    region_img = arial_task()
    for img in list_energy:
        pos_en = fun.locCenterImg(f'{path_energy_task}{img}', region=region_img)
        if pos_en:
            print(fun.extraction_digit(item=img))
            fun.Mouse.move(pos=pos_en, speed=0.5)
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
    fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
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


# arial_task()
