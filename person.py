import pyautogui
import fun
from time import sleep
from heroes import Hero, Activ

# duration=d_drag и duration=d с предметом и в свободном состоянии
d = 0.4
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
    'пустой слот': 'img/person/slot.png',
    'маленький слот': 'img/person/smol_slot.png',
    'фото героя': 'img/person/hero.png',
    'выход': 'img/b_exit.png',
}


def change_jacket_green():
    pass


def change_jacket_raid():
    jacket_r = fun.locCenterImg(item_person["куртка рейдовая"], confidence=0.9)
    jacket_b = fun.locCenterImg(item_person['куртка броня Гаврил'], confidence=0.9)
    pyautogui.moveTo(jacket_r, duration=d)
    pyautogui.dragTo(jacket_b, duration=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def change_trousers():
    trousers_burbon = fun.locCenterImg(item_person['брюки Бурбон'], confidence=0.9)
    trousers_b = fun.locCenterImg(item_person['брюки броня'], confidence=0.9)
    pyautogui.moveTo(trousers_burbon, duration=d)
    pyautogui.dragTo(trousers_b, duration=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def change_gloves():
    gloves_point = fun.locCenterImg(item_person['место перчаток'], confidence=0.9)
    # если перчатки не надеты одеваем
    if gloves_point is not None:
        gloves = fun.locCenterImg(item_person['перчатки'], confidence=0.9)
        pyautogui.moveTo(gloves, duration=d)
        pyautogui.dragTo(gloves_point, duration=d_drag)
    # иначе снимаем
    else:
        gloves = fun.locCenterImg(item_person['перчатки'], confidence=0.9)
        slot = fun.locCenterImg(item_person['пустой слот'], confidence=0.9)
        pyautogui.moveTo(gloves, duration=d)
        pyautogui.dragTo(slot, duration=d_drag)
    # отводим указатель
    p_slot = fun.locCenterImg(item_person['маленький слот'], confidence=0.9)
    pyautogui.moveTo(p_slot, duration=d)
    sleep(0.5)


def change_dress():
    inventory = fun.locCenterImg(item_person['инвентарь'], confidence=0.9)
    # цикл в ожидании появления инвентаря
    fun.move_to_click(inventory, 0.3)
    print('готов к переодеванию')
    change_jacket_raid()
    change_trousers()
    change_gloves()
    print('переодет')


def pereodevanie():
    hero = fun.locCenterImg(item_person['фото героя'], confidence=0.9)
    if hero is not None:
        fun.move_to_click(hero, 0.3)
        sleep(0.5)
        change_dress()
    else:
        change_dress()
    exit_ = fun.locCenterImg(item_person['выход'], confidence=0.9)
    fun.move_to_click(exit_, 0.3)


def change_acc(*, hero_name_in_file):
    fun.selection_hero()
    activ_hero = Hero.get_hero_name_in_file(Activ.hero_activ)
    # print(f'{hero_name_in_file=}, {activ_hero=}')
    if hero_name_in_file == activ_hero:
        print('этот герой уже активен')
        return

    # print(f'img/person/change_hero_{hero_name_in_file}.png')
    # развернуть на весь экран
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    # print(f"{img_button_expand=}")
    if not img_button_expand:
        pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
        while not pos_my:
            pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
        x, y = pos_my
        x -= 50
        y -= 50
        fun.move_to_click(pos_click=(x, y), z_p_k=0.5)
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.move_to_click(pos_click=img_button_expand)
    # вычисление позиции смены аккаунта
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_my
    x += 506
    y -= 5
    pos_menu_chenge_acc = x, y
    # открыть меню
    open_menu_chenge_acc = fun.locCenterImg('img/person/change_hero/add_acc.png')
    if not open_menu_chenge_acc:
        fun.move_to_click(pos_click=pos_menu_chenge_acc, z_p_k=0.2)
    # нажать нужного героя
    cange_hero = fun.locCenterImg(f'img/person/change_hero/change_hero_{hero_name_in_file}.png')
    # print(cange_hero)
    fun.move_to_click(pos_click=cange_hero, z_p_k=0.2)
    #
    img_button_collapse = fun.locCenterImg('img/overall/button_collapse.png')
    fun.move_to_click(pos_click=img_button_collapse, z_p_k=0.2)
    #
    pos = fun.locCenterImg('img/overall/event_entry/pos_t.png')
    while not pos:
        pos = fun.locCenterImg('img/overall/event_entry/pos_t.png')
        hero_name_in_file_list = ['gavr', 'gady', 'veles', 'mara']
        if hero_name_in_file in hero_name_in_file_list:
            continue_heroes = fun.locCenterImg(f'img/overall/event_entry/continue_{hero_name_in_file}.png')
            if continue_heroes:
                fun.move_to_click(pos_click=continue_heroes)

    slider = fun.locCenterImg('img/overall/slider_v.png', 0.7)
    if slider:
        x, y = slider
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.dragTo(x, y + 45, duration=1)
    print('смена героя проведена')
