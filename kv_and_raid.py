import pyautogui
from fun import move_to_click, my_print_to_file, foto, name_f
from time import sleep


def foto_danger():
    kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    x, y = kv_close
    x -= 585
    y -= 435
    x_s, y_s = x, y
    x += 862
    y += 485
    x_r, y_r = x, y
    name_foto = name_f() + ".png"
    foto(('img/Cr/' + name_foto), (x_s, y_s, x_r, y_r))
    print('foto')


def battle(q_call):
    print(f'{q_call} бой')
    my_print_to_file('battle')

    kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.85)
    my_print_to_file(f'{kv_skip_battle} kv_skip_battle')
    danger = pyautogui.locateCenterOnScreen('img/kv/kv_danger.png', confidence=0.9)
    my_print_to_file(f'{danger} danger')
    kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    my_print_to_file(f"{kv_close}, kv_close")
    while not kv_skip_battle:
        sleep(1)
        kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.85)
        my_print_to_file(f'{kv_skip_battle} kv_skip_battle цикл ожидания')
    it_kv = 0
    while not kv_close:
        it_kv += 1
        if not danger and kv_skip_battle and it_kv >= 5:
            move_to_click(kv_skip_battle, 0.5)
            print(' пропуск боя')
        sleep(1)
        kv_skip_battle = pyautogui.locateCenterOnScreen('img/kv/kv_skip_battle.png', confidence=0.85)
        danger = pyautogui.locateCenterOnScreen('img/kv/kv_danger.png', confidence=0.9)
        kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    if danger:
        print(" опасный")
    kv_close = pyautogui.locateCenterOnScreen('img/kv/kv_close.png', confidence=0.9)
    foto_danger()
    move_to_click(kv_close, 0.3)
    print("закрыть результат боя")


def kv():
    my_print_to_file('kv_and_raid.kv')
    kv_reload = pyautogui.locateCenterOnScreen('img/kv/kv_reload.png', confidence=0.9)
    # my_print_to_file(f'kv_reload {kv_reload}')
    my_print_to_file("нажать 'обновить'")
    move_to_click(kv_reload, 1)

    q_attack = 0
    kv_wait_attack = pyautogui.locateCenterOnScreen('img/kv/kv_wait_attack.png', confidence=0.9)
    # my_print_to_file(f'kv_wait_attack {kv_wait_attack}')
    kv_attak = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)
    # my_print_to_file(f'kv_attak {kv_attak}')
    if not kv_attak and not kv_wait_attack:
        print('ждем начало кв')
    it_w_a = 0
    it_w_rel = 0
    while True:

        if kv_wait_attack:
            it_w_a += 1
            if it_w_a == 1:
                print("ждем возможность атаковать")
                kv_reload = pyautogui.locateCenterOnScreen('img/kv/kv_reload.png', confidence=0.9)
                move_to_click(kv_reload, 1)
        if kv_attak:
            it_w_a = 0
            q_attack += 1
            move_to_click(kv_attak, 0)
            battle(q_attack)
        kv_wait_attack = pyautogui.locateCenterOnScreen('img/kv/kv_wait_attack.png', confidence=0.9)
        kv_attak = pyautogui.locateCenterOnScreen('img/kv/kv_attak.png', confidence=0.9)




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
    foto(('img/Cr/' + name_foto), (x_s, y_s, x_r, y_r))
