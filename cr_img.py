import pyautogui
from time import sleep

import fun
from t import sounds
import find_img as find


def cri_event_img(*, x_reg, y_reg, name):
    pos = fun.locCenterImg(name)
    if pos:
        x, y = pos
        x -= x_reg / 2
        y -= y_reg / 2
        fun.foto(name, (x, y, x_reg, y_reg))


def get_screenshot_task():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_big, region2_big, region3_big = fun.get_areas_task_big()

    fun.foto_pos(name_img="img/test/big_1.png", region=region1_big,
                 tune_x=tune_x, tune_y=tune_y, tune_s=tune_s, tune_v=tune_v)
    fun.foto_pos(name_img="img/test/big_2.png", region=region2_big,
                 tune_x=tune_x, tune_y=tune_y, tune_s=tune_s, tune_v=tune_v)
    fun.foto_pos(name_img="img/test/big_3.png", region=region3_big,
                 tune_x=tune_x, tune_y=tune_y, tune_s=tune_s, tune_v=tune_v)


def fashion():
    """
        образец
        """
    name_create_img = 'img/overall/link_money_token.png'
    show_move = True
    pos_start = find.find_my_game2()
    # показать привязку
    fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 20
    y += 25 + 6
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
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
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return


def victory_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        # print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 335
        y -= 230
        pos_foto = x, y
        # pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        # region = x, y
        # pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/victory_battle_in_kv.png', region=(x, y, 110, 41))


def defeat_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        # print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 340
        y -= 230
        pos_foto = x, y
        # pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        # pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/defeat_battle_in_kv.png', region=(x, y, 140, 45))


def victory_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 55
        y -= 405
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/victory_in_arena.png', region=(x, y, 140, 65))
    print('отработал')


def defeat_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 110
        y -= 295
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 180
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/defeat_in_arena.png', region=(x, y, 180, 65))
    print('отработал')


def gift_img():
    pos = fun.find_link_klan()
    x, y = pos
    x += 118  # 148
    y += 350  # 300
    pyautogui.moveTo(x, y)
    x_v = x
    y_v = y
    x_v += 28
    pyautogui.moveTo(x_v, y)
    y_v += 40
    # pyautogui.moveTo(x_v, y_v)
    fun.foto('img/test/gift2.png', (x, y, 28, 25))
    print("сделано")


def lvl_img():
    pos = fun.find_link_klan()
    x, y = pos
    x_f = x - 85
    y_f = y - 70
    # pyautogui.moveTo((x_f, y_f), duration=1)
    # x_r = x_f + 55
    # y_r = y_f + 40
    # pyautogui.moveTo((x_r, y_r), duration=1)
    fun.foto('img/test/lvl.png', (x_f, y_f, 55, 40))
    print("сделано")


def work():
    pos = fun.vizit_to_station_master()
    x, y = pos
    x += 450
    y -= 5
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 90
    change_y = 30
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/work.png', (x, y, change_x, change_y))
    pos_work = fun.locCenterImg(f'img/overall/work.png')
    fun.Mouse.move(pos=pos_work)


def work_8_hour():
    fun.vizit_to_station_master()
    pos_work = fun.locCenterImg('img/overall/work.png')
    fun.Mouse.move(pos=pos_work)
    x, y = pos_work
    x -= 224
    y += 430
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 200
    change_y = 50
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/work_8_hour.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/overall/work_8_hour.png')
    fun.Mouse.move(pos=pos)


def station_exit():
    pos_close = find.find_close()
    fun.Mouse.move(pos=pos_close, speed=1)
    x, y = pos_close
    x -= 600 - 6
    y -= 640 - 4
    fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 290 - 6 - 2
    change_y = 50 - 4
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo))
    fun.foto(f'img/tonelli/station_exit.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/tonelli/station_exit.png')
    fun.Mouse.move(pos=pos)


def button_expand():
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    # fun.Mouse.move(pos=pos_my)
    x, y = pos_my
    x += 280
    y -= 55
    # fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 25
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/button_expand.png', (x, y, change_x, change_y))
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.Mouse.move(pos=img_button_expand, speed=1)


def img_change_hero():
    # развернуть на весь экран
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.Mouse.move_to_click(pos_click=img_button_expand)
    #
    sleep(0.2)
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_my
    x += 500 - 10
    y -= 20
    # fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 32
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo))
    # fun.foto(f'img/person/change_hero_gavr.png', (x, y, change_x, change_y))
    change_hero = pyautogui.screenshot(region=(x, y, change_x, change_y))
    pos_menu_chenge_acc = fun.locCenterImg(change_hero)
    open_menu_chenge_acc = fun.locCenterImg('img/person/add_acc.png')
    if not open_menu_chenge_acc:
        fun.Mouse.move_to_click(pos_click=pos_menu_chenge_acc)
    img(pos_menu_chenge_acc)


def img(pos_clic):
    x, y = pos_clic
    x -= 125
    y += 97
    # fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 180
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo))
    # создание
    fun.foto('img/person/change_hero/change_hero_mara.png', (x, y, change_x, change_y))
    # проверка
    sleep(1)
    her_gady = fun.locCenterImg('img/person/change_hero_gady.png')
    her_gavr = fun.locCenterImg('img/person/change_hero_gavr.png')
    her_mara = fun.locCenterImg('img/person/change_hero_mara.png')
    her_veles = fun.locCenterImg('img/person/change_hero_veles.png')
    if her_veles:
        print('her Veles')
        fun.Mouse.move(pos=her_veles, speed=1)
        sleep(2)
    if her_gady:
        print('her Gady')
        fun.Mouse.move(pos=her_gady, speed=1)
        sleep(2)
    if her_gavr:
        print('her Gavr')
        fun.Mouse.move(pos=her_gavr, speed=1)
        sleep(2)
    if her_mara:
        print('her Mara')
        fun.Mouse.move(pos=her_mara, speed=1)
        sleep(2)


def img2(pos_clic):
    # добавить аккаунт
    # pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_clic
    x -= 95
    y += 97 + 130 + 35
    fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 180
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo))
    fun.foto(f'img/person/change_hero/add_acc.png', (x, y, change_x, change_y))


def button_collapse():
    #
    # развернуть на весь экран
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.Mouse.move_to_click(pos_click=img_button_expand)
    #
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)

    x, y = pos_my
    x += 700 - 17
    y -= 57
    # fun.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 25
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    # fun.Mouse.move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/button_collapse.png', (x, y, change_x, change_y))
    img_button_collapse = fun.locCenterImg('img/overall/button_collapse.png')
    fun.Mouse.move(pos=img_button_collapse, speed=1)


def aktiv_win_game():
    pos = fun.locCenterImg('img/overall/avtoriz/aktiv_win_game.png')
    if pos:
        # 34x98
        x, y = pos
        x -= 34 / 2
        y -= 98 / 2
        fun.foto('img/overall/avtoriz/aktiv_win_game.png', (x, y, 34, 98))


def continue_hero():
    pos = fun.locCenterImg('img/overall/event_entry/transmitted data.png')
    if pos:
        print('ok')
        # 34x98
        x, y = pos
        x -= 270 / 2
        y -= 60 / 2
        # fun.foto('img/overall/event_entry/continue_gavr.png', (x, y, 270, 60))
    return


def info_img():
    """
    создание более качественной картинки своими средствами
    """
    pos = tuple(fun.locCenterImg(name_img='img/overall/info.png', confidence=0.8))
    # print(type(pos))
    if pos:
        print('ok')
        # 33x41
        x, y = pos
        pos_change = 33, 41
        x -= (pos_change[0] / 2) - 2
        y -= (pos_change[1] / 2) - 2
        fun.foto('img/overall/info.png', (x, y, pos_change[0], pos_change[1]))
    new_pos = fun.locCenterImg(name_img='img/overall/info.png')
    fun.Mouse.move(pos=new_pos)
    return


def dress():
    """
    образец
    """
    name_create_img = 'img/person/dress/slots/jacket_point.png'
    show_move = False
    pos_start = find.find_exit_person()
    # показать привязку
    fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    # x += 251, y -= 486 верхний правый слот
    # x += 371, y -= 341 слот перчаток
    # x += 713, y -= 341 слот жакета
    # x += 175, y -= 232 слот брюки
    # x += 713, y += 125 слот обувь
    x += 713
    y -= 341
    fun.Mouse.move(pos=(x, y), speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 89
    change_y = 89
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)

    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return


def dress_region():
    name_create_img = 'img/person/dress/region shoes.png'
    show_move = True
    pos_start = find.find_exit_person()
    # показать привязку
    fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    # x += 251, y -= 486 верхний правый слот
    # x += 371, y -= 341 слот перчаток
    # x += 713, y -= 232 слот брюки
    # x += 713, y -= 341 слот жакета
    # x += 713, y -= 125 слот обувь
    x += 713 - 30
    y -= 125 + 30
    top_pos = x, y
    print('слот обувь')
    fun.Mouse.move(pos=top_pos, speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 90 + 60
    change_y = 90 + 60
    print(f'регион ({top_pos[0] - pos_start[0]}, {top_pos[1] - pos_start[1]}, {change_x}, {change_y})')
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    #
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.Mouse.move(pos=pos)

    print('ok')


def no_energy():
    name_create_img = 'img/station_master/energy_indicator/no_energy.png'
    show_move = True
    pos_start = find.find_station_master()
    # показать привязку
    fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 270
    y += 455 + 7
    top_pos = x, y
    print('место')
    fun.Mouse.move(pos=top_pos, speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 59
    change_y = 41
    # # print(f'регион ({top_pos[0] - pos_start[0]}, {top_pos[1] - pos_start[1]}, {change_x}, {change_y})')
    x_demo += change_x
    y_demo += change_y
    fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)

    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.Mouse.move(pos=pos)
    sounds.sound_vic()
    print(f'файл {name_create_img} создан')

# info_img()
# energy_img()
