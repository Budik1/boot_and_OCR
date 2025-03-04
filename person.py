import pyautogui
import fun
from time import sleep

# duration=d_drag и duration=d с предметом и в свободном состоянии
d = 0.4
d_drag = 1.4
item_person = {
    'куртка рейдовая': 'img/person/jacket_r.png',
    'брюки рейдовые': '',
    'брюки броня': 'img/person/trousers_b.png',
    'куртка броня Гаврил': 'img/person/jacket_b.png',

    'брюки Бурбон': 'img/person/trousers_bourbon.png',
    'куртка Бурбон': '',

    'перчатки': 'img/person/gloves.png',
    'место перчаток': 'img/person/gloves_point.png',
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


def smena_garderoba():
    inventar = fun.locCenterImg(item_person['инвентарь'], confidence=0.9)
    # цикл в ожидании появления инвентаря
    fun.move_to_click(inventar, 0.3)
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
        smena_garderoba()
    else:
        smena_garderoba()
    exit_ = fun.locCenterImg(item_person['выход'], confidence=0.9)
    fun.move_to_click(exit_, 0.3)
