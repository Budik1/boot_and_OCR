import pyautogui
from time import sleep

# from icecream import ic
# ic.configureOutput(includeContext=True)
# print = ic

import find_img
import fun

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
    '': '', }
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
    fun.Mouse.take_drag_drop(pos_take=jacket_r, pos_drop=jacket_b, speed=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    fun.Mouse.move(pos=p_slot, speed=speed)
    sleep(0.5)


def change_trousers():
    trousers_burbon = fun.locCenterImg(item_person['брюки Бурбон'], confidence=0.9)
    trousers_b = fun.locCenterImg(item_person['брюки броня'], confidence=0.9)
    fun.Mouse.move(pos=trousers_burbon, speed=speed)
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
        fun.Mouse.move(pos=gloves, speed=speed)
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
    fun.Mouse.move_to_click(pos_click=inventory, z_p_k=0.3)
    print('готов к переодеванию')
    change_jacket_raid()
    change_trousers()
    change_gloves()
    print('переодет')


def pereodevanie():
    hero = fun.locCenterImg(item_person['фото героя'], confidence=0.9)
    if hero is not None:
        fun.Mouse.move_to_click(pos_click=hero, z_p_k=0.3)
        sleep(0.5)
        change_dress()
    else:
        change_dress()
    exit_ = fun.locCenterImg(item_person['выход'], confidence=0.9)
    fun.Mouse.move_to_click(pos_click=exit_, z_p_k=0.3)


def is_activate_win(*, show=False):
    """
    Проверка видно ли всё окно
    :param show: если True показать позицию кнопки "развернуть"
    :return: позиция кнопки "развернуть"
    """
    #
    value_correct_for_activate_win = 40
    pos_expand = find_img.find_button_expand()
    while not pos_expand:
        pos1 = fun.locCenterImg(name_img='img/overall/my_game1.png')
        x, y = pos1
        y -= value_correct_for_activate_win
        pos1_1 = x, y
        fun.Mouse.move_to_click(pos_click=pos1_1)
        # найти кнопку "развернуть"
        pos_expand = find_img.find_button_expand()
    if show:
        # показать кнопку "развернуть"
        fun.Mouse.move(pos=pos_expand)
    return pos_expand


def activated_change_menu():
    value_correct_for_activate_menu = 23
    is_activate_win()
    # проверка открытого меню
    pos_add = fun.locCenterImg(name_img='img/person/change_hero/add_acc.png')
    pos_menu = None
    # позиция кнопки меню
    list_img_menu = ['img/person/hero_id/gady/menu_acc_her_gadya.png',
                     'img/person/hero_id/gavr/menu_acc_her_gavr.png',
                     'img/person/hero_id/mara/menu_acc_her_mara.png']
    for img in list_img_menu:
        pos_menu = fun.locCenterImg(name_img=img)
        if pos_menu:
            break
    # если меню не открыто
    if not pos_add:
        x, y = pos_menu
        x -= value_correct_for_activate_menu
        pos_click = x, y
        fun.Mouse.move_to_click(pos_click=pos_click)

    return pos_menu


def change_acc(*, change_hero_name):
    move_time = 0.3
    #
    vid = fun.selection_hero()
    while not vid:
        fun.push_close_all_()
        vid = fun.selection_hero()
    activ_hero = Hero.get_name_id(Activ.hero_activ)
    #
    if change_hero_name == activ_hero:
        print('этот герой уже активен')
        return
    activated_change_menu()
    # нажать нужного героя
    change_hero = fun.locCenterImg(f'img/person/change_hero/change_hero_{change_hero_name}.png')
    fun.Mouse.move_to_click(pos_click=change_hero, move_time=move_time, z_p_k=0.2)
    # проверка начала процесса смены
    # print('ожидание начала процесса смены')
    scrin_change = fun.selection_hero(show_name=False)
    # print(f'{scrin_change=}')
    # print(f'{bool(scrin_change)=}')
    while scrin_change:
        scrin_change = fun.selection_hero(show_name=False)
        # print(f'{bool(scrin_change)=}')

    # print(' начало процесса смены')
    #
    pos = find_img.find_info()
    # print(f'{pos=}')
    fun.Mouse.move(pos=pos, speed=0.05)
    while not pos:
        pos = find_img.find_info()
        continue_heroes = fun.locCenterImg(f'img/overall/event_entry/continue_{change_hero_name}.png')
        # print('Поиск "продолжить как.."')
        if continue_heroes:
            fun.Mouse.move_to_click(pos_click=continue_heroes, move_time=move_time, z_p_k=0.2)
    pos_info = find_img.find_info()
    while not pos_info:
        pos_info = find_img.find_info()
    hero_name = fun.selection_hero(show_name=False)
    print(f'{hero_name} активен')
    return hero_name
