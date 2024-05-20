import pyautogui
from fun import move_to_click, my_print_to_file, foto, time_now, name_f
from time import sleep

from station_master import enemy_battle


# kv_attack = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)
# while True:
#     if kv_attack:
#         print("attak !!")
#     kv_attack = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)
def battle():
    print('battle')
    my_print_to_file('battle')
    kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.9)
    danger = pyautogui.locateCenterOnScreen('img/kv/kv_danger.png', confidence=0.9)
    kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    while not kv_skip_battle:
        sleep(1)
        kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.9)

    it_kv = 0
    while not kv_close:
        it_kv += 1
        if danger:
            print("опасный")
        if kv_skip_battle and it_kv >= 5:
            move_to_click(kv_skip_battle, 0.5)
            print("закрыть результат боя")
        sleep(1)
        kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.9)
        danger = pyautogui.locateCenterOnScreen('img/kv/kv_danger.png', confidence=0.9)
        kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    move_to_click(kv_close, 0.3)
    print("battle выход")


def kv():
    kv_wait_attack = pyautogui.locateCenterOnScreen('img/kv/kv_wait_attack.png', confidence=0.9)
    kv_attak = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)
    it_w_a = 0
    while True:
        if kv_wait_attack:
            it_w_a += 1
            if it_w_a == 1:
                print("ждем возможность атаковать")
                kv_reload = pyautogui.locateCenterOnScreen('img/kv/kv_reload.png', confidence=0.9)
                move_to_click(kv_reload, 1)
        if kv_attak:
            it_w_a = 0
            move_to_click(kv_attak, 0)
            battle()

        kv_wait_attack = pyautogui.locateCenterOnScreen('img/kv/kv_wait_attack.png', confidence=0.9)
        kv_attak = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)


kv()

# mining_loot = pyautogui.locateCenterOnScreen('img/kv/mining_loot.png', confidence=0.9)
# print(mining_loot)
# pyautogui.moveTo(mining_loot, duration=2)


def loot():
    backpack = pyautogui.locateCenterOnScreen('img/kv/backpack.png', confidence=0.9)
    pyautogui.moveTo(backpack, duration=2)

    x, y = backpack
    x -= 220
    x_s = x
    y -= 145
    y_s = y
    pos = x, y
    pyautogui.moveTo(pos, duration=2)
    x += 755
    x_r = x
    y += 615
    y_r = y
    pos = x, y
    pyautogui.moveTo(pos, duration=2)

    name_foto = name_f() + ".png"
    foto(('img/Cr/' + name_foto), (x_s, y_s, x_r,y_r))
