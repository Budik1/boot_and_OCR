import pyautogui
import fun
from time import sleep
import my_color_text as myCt
from heroes import Hero, Activ


def foto_danger():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    x, y = kv_close
    x -= 585
    y -= 435
    x_s, y_s = x, y
    x += 862
    y += 485
    x_r, y_r = x, y
    name_foto = fun.date_and_time_in_name_file() + ".png"
    fun.foto(('img/Cr/' + name_foto), (x_s, y_s, x_r, y_r))
    print('foto')


def selection_hero_in_kv():
    hero = fun.selection_hero()
    if not hero:
        exit_kv = fun.locCenterImg('img/exit_kv.png')
        if exit_kv:
            fun.move_to_click(exit_kv, 0)
        hero = fun.selection_hero()
    klan = fun.find_link_klan()
    if klan:
        x, y = klan
        x += 100
        pos = x, y
        fun.move_to_click(pos, 0)


def battle(q_call):
    # print(f'{q_call} бой')
    fun.my_print_to_file('battle')
    raid = False
    kv_skip_battle = fun.locCenterImg('img/kv/kv_skip_battle.png', confidence=0.85)
    fun.my_print_to_file(f'{kv_skip_battle} kv_skip_battle')
    danger = fun.locCenterImg('img/kv/kv_danger.png', confidence=0.9)
    fun.my_print_to_file(f'{danger} danger')
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    fun.my_print_to_file(f"{kv_close}, kv_close")
    while not kv_skip_battle:
        sleep(1)
        kv_skip_battle = fun.locCenterImg('img/kv/kv_skip_battle.png', confidence=0.85)
        fun.my_print_to_file(f'{kv_skip_battle} kv_skip_battle цикл ожидания')
    it_kv = 0
    while not kv_close:
        it_kv += 1
        if not danger and kv_skip_battle and it_kv >= 10:
            fun.move_to_click(kv_skip_battle, 0.5)
            # print(' пропуск боя')
        sleep(1)
        kv_skip_battle = fun.locCenterImg('img/kv/kv_skip_battle.png', confidence=0.85)
        danger = fun.locCenterImg('img/kv/kv_danger.png', confidence=0.9)
        kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if danger:
        print(" опасный")
        Hero.app_danger(Activ.hero_activ)
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        # print(kv_close, 'kv_close')
        victory = fun.locCenterImg('img/kv/victory_battle_in_kv.png', confidence=0.95)
        defeat = fun.locCenterImg('img/kv/defeat_battle_in_kv.png', confidence=0.95)
        if victory:
            result = "победа"
            print(f'бой {q_call}, {myCt.tc_yellow(result)}')
            # print(Hero.get_name_ru(Activ.hero_activ))

            if danger:
                # print('победа над опасным')
                Hero.app_danger_v(Activ.hero_activ)
                foto_danger()
        elif defeat:
            result = "поражение"
            print(f'бой {q_call}, {myCt.tc_yellow(result)}')
            # print(myCt.tc_red(result))
        else:
            result = ''
            print(f'бой {q_call}, {myCt.tc_yellow(result)}')

    qty_danger = Hero.get_qty_danger(Activ.hero_activ)
    qty_danger_v = Hero.get_qty_danger_v(Activ.hero_activ)
    print(f'встретил {qty_danger}, побед {qty_danger_v}')
    fun.move_to_click(kv_close, 0.3)

    # print("закрыть результат боя")


def kv():
    fun.my_print_to_file('kv_and_raid.kv')
    selection_hero_in_kv()
    kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
    # fun.my_print_to_file(f'kv_reload {kv_reload}')
    fun.my_print_to_file("нажать 'обновить'")
    fun.move_to_click(kv_reload, 1)

    q_attack = 0
    kv_wait_attack = fun.locCenterImg('img/kv/kv_wait_attack.png', confidence=0.9)
    # fun.my_print_to_file(f'kv_wait_attack {kv_wait_attack}')
    kv_attak = fun.locCenterImg('img/kv/kv_attak.png', confidence=0.9)
    # fun.my_print_to_file(f'kv_attak {kv_attak}')
    if not kv_attak and not kv_wait_attack:
        print('ждем начало кв')
    it_w_a = 0
    it_w_rel = 0
    while True:

        if kv_wait_attack:
            it_w_a += 1
            if it_w_a == 1:
                # print("ждем возможность атаковать")
                kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
                fun.move_to_click(kv_reload, 1)
        if kv_attak:
            it_w_a = 0
            q_attack += 1
            fun.move_to_click(kv_attak, 0)
            battle(q_attack)
        kv_wait_attack = fun.locCenterImg('img/kv/kv_wait_attack.png', confidence=0.9)
        kv_attak = fun.locCenterImg('img/kv/kv_attak.png', confidence=0.9)


def loot():
    backpack = fun.locCenterImg('img/kv/backpack.png', confidence=0.9)
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

    name_foto = fun.date_and_time_in_name_file() + ".png"
    fun.foto(('img/Cr/' + name_foto), (x_s, y_s, x_r, y_r))


def go_in_clan():
    pass
