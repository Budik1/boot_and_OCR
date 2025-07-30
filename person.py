import pyautogui

import find_img
import fun
from time import sleep

from heroes import Hero, Activ

# duration=d_drag и duration=d с предметом и в свободном состоянии
speed = 0.4
d_drag = 1.4
item_person = {
    'куртка рейдовая': 'img/person/dress/jacket_r.png',
    'брюки рейдовые': '',
    'брюки броня': 'img/person/trousers_b.png',
    'куртка броня Гаврил': 'img/person/dress/jacket_b.png',

    'брюки Бурбон': 'img/person/trousers_bourbon.png',
    'куртка Бурбон': '',

    'перчатки': 'img/person/dress/gloves.png',
    'место перчаток': 'img/person/dress/gloves_point.png',
    'орден': 'img/person/orden.png',
    'инвентарь': 'img/person/inventory.png',
    'пустой слот': 'img/person/empty slot.png',
    'маленький слот': 'img/person/smol_slot.png',
    'фото героя': 'img/person/hero.png',
    'выход': 'img/b_exit.png',
}
slots = {
    # регион от exit_person.png
    'место перчаток': 'img/person/slots/gloves_point.png',
    'регион место перчаток': (341, -371, 150, 150),

    'место верха': 'img/person/slots/jacket_point.png',
    'регион место верха': (683, -371, 150, 150),

    'место низа': 'img/person/slots/trousers_point.png',
    'регион место низа': (683, -262, 150, 150),

    'место обуви': 'img/person/slots/shoes_point.png',
    'регион место обуви': (683, -155, 150, 150),

    'пустой слот': 'img/person/slots/empty slot.png',
    'регион пустой слот': (35, -519, 338, 428),

    'маленький слот': 'img/person/slots/smol_slot.png',
    'регион маленький слот': (0, 0, 150, 150),
    '': '',}
dress = {
    'верх_бурбон': 'img/person/dress/jacket_bourbon.png',
    'низ_бурбон': 'img/person/dress/trousers_bourbon.png',
    '': '',
}

def verification_dress(*, item, region_item):
    pass



def change_jacket_green():
    pass

def change_item(*, what, where):
    """
    :param what: что
    :param where: куда
    """
    # брюки на место брюк
    # брюки на пустой слот
    what_file_name = f'img/person/dress/{what}.png'
    where_file_name = f'img/person/dress/{where}.png'
    what_pos = find_img.find_name(path_name=what_file_name)
    where_pos = find_img.find_name(path_name=where_file_name)
    fun.Mouse.move(pos=what_pos, speed=speed)
    fun.Mouse.take_drag_drop(pos_take=what_pos, pos_drop=where_pos, speed=speed)
    # отводим указатель
    pos_finish = find_img.find_smol_slot()
    fun.Mouse.move(pos=pos_finish, speed=speed)



def change_jacket_raid():
    jacket_r = fun.locCenterImg(item_person["куртка рейдовая"], confidence=0.9)
    jacket_b = fun.locCenterImg(item_person['куртка броня Гаврил'], confidence=0.9)
    fun.Mouse.move(pos=jacket_r, speed=speed)
    fun.Mouse.take_drag_drop(pos_take=jacket_r ,pos_drop=jacket_b, speed=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    fun.Mouse.move(pos=p_slot, speed=speed)
    sleep(0.5)


def change_trousers():
    trousers_burbon = fun.locCenterImg(item_person['брюки Бурбон'], confidence=0.9)
    trousers_b = fun.locCenterImg(item_person['брюки броня'], confidence=0.9)
    fun.Mouse.move(pos= trousers_burbon, speed=speed)
    pyautogui.dragTo(trousers_b, duration=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    fun.Mouse.move(pos=p_slot, speed=speed)
    sleep(0.5)


def change_gloves():
    gloves_point = fun.locCenterImg(item_person['место перчаток'], confidence=0.9)
    # если перчатки не надеты одеваем
    if gloves_point is not None:
        gloves = fun.locCenterImg(item_person['перчатки'], confidence=0.9)
        fun.Mouse.move(pos= gloves, speed=speed)
        pyautogui.dragTo(gloves_point, duration=d_drag)
    # иначе снимаем
    else:
        gloves = fun.locCenterImg(item_person['перчатки'], confidence=0.9)
        slot = fun.locCenterImg(item_person['пустой слот'], confidence=0.9)
        fun.Mouse.move(pos=gloves, speed=speed)
        pyautogui.dragTo(slot, duration=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    fun.Mouse.move(pos=p_slot, speed=speed)
    sleep(0.5)


def change_dress():
    inventory = fun.locCenterImg(item_person['инвентарь'], confidence=0.9)
    # цикл в ожидании появления инвентаря
    fun.mouse_move_to_click(pos_click=inventory, z_p_k=0.3)
    print('готов к переодеванию')
    change_jacket_raid()
    change_trousers()
    change_gloves()
    print('переодет')


def pereodevanie():
    hero = fun.locCenterImg(item_person['фото героя'], confidence=0.9)
    if hero is not None:
        fun.mouse_move_to_click(pos_click=hero, z_p_k=0.3)
        sleep(0.5)
        change_dress()
    else:
        change_dress()
    exit_ = fun.locCenterImg(item_person['выход'], confidence=0.9)
    fun.mouse_move_to_click(pos_click=exit_, z_p_k=0.3)


def change_acc(*, change_hero_name):
    move_time = 0.3
    vid = fun.selection_hero()
    while not vid:
        fun.push_close_all_()
        vid = fun.selection_hero()
    activ_hero = Hero.get_hero_name_in_file(Activ.hero_activ)
    # print(f'{activ_hero=}, {activ_hero=}')
    if change_hero_name == activ_hero:
        print('этот герой уже активен')
        return

    # print(f'img/person/change_hero_{hero_name_in_file}.png')
    # развернуть на весь экран
    img_button_expand = find_img.find_button_expand()
    if not img_button_expand:
        # activate win
        pos_my = find_img.find_my_game2()
        while not pos_my:
            pos_my = find_img.find_my_game2()
        x, y = pos_my
        x -= 50
        y -= 50
        fun.Mouse.move_to_click(pos_click=(x, y), move_time=move_time, z_p_k=0.2)
    img_button_expand = find_img.find_button_expand()
    fun.mouse_move_to_click(pos_click=img_button_expand, move_time=move_time, z_p_k=0.2)
    # вычисление позиции меню смены аккаунта
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_my
    x += 506
    y -= 5
    pos_menu_chenge_acc = x, y
    # открыть меню
    menu_change_acc_open = fun.locCenterImg('img/person/change_hero/add_acc.png')
    if not menu_change_acc_open:
        fun.mouse_move_to_click(pos_click=pos_menu_chenge_acc, move_time=move_time, z_p_k=0.2)
    # нажать нужного героя
    cange_hero = fun.locCenterImg(f'img/person/change_hero/change_hero_{change_hero_name}.png')
    fun.mouse_move_to_click(pos_click=cange_hero, move_time=move_time, z_p_k=0.2)
    #
    img_button_collapse = fun.locCenterImg('img/overall/button_collapse.png')
    fun.mouse_move_to_click(pos_click=img_button_collapse, move_time=move_time, z_p_k=0.2)
    #
    pos = fun.locCenterImg('img/overall/event_entry/pos_t.png')
    # print(f'{pos=}')
    while not pos:
        pos = fun.locCenterImg('img/overall/event_entry/pos_t.png')
        hero_name_in_file_list = ['gavr', 'gady', 'veles', 'mara']
        if change_hero_name in hero_name_in_file_list:
            continue_heroes = fun.locCenterImg(f'img/overall/event_entry/continue_{change_hero_name}.png')
            if continue_heroes:
                fun.mouse_move_to_click(pos_click=continue_heroes, move_time=move_time, z_p_k=0.2)

    slider = fun.locCenterImg('img/overall/slider_v.png', 0.7)
    if slider:
        fun.Mouse.move(pos=slider, speed=move_time)
        fun.Mouse.take_drag_drop_y(pos_take=slider, dist=43, speed=1)
    pos_info = find_img.find_info()
    while not pos_info:
        pos_info = find_img.find_info()
    hero_name = fun.selection_hero(show_name=False)
    print(f'{hero_name} активен')
    return hero_name
