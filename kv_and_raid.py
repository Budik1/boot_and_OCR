import fun
from time import sleep
import my_color_text as myCt
import find_img as find
from heroes import Hero, Activ


def foto_danger():
    kv_close = find.find_close()
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
        exit_kv = find.find_exit_kv()
        if exit_kv:
            fun.mouse_move_to_click(pos_click=exit_kv)
        hero = fun.selection_hero()
    klan = fun.find_link_klan()
    if klan:
        x, y = klan
        x += 100
        pos = x, y
        fun.mouse_move_to_click(pos_click=pos)
    return hero


def battle(q_call):
    # print(f'{q_call} бой')
    fun.my_print_to_file('battle')
    raid = False
    kv_skip_battle = find.find_kv_skip_battle()
    fun.my_print_to_file(f'{kv_skip_battle} kv_skip_battle')
    danger = find.find_kv_danger()
    fun.my_print_to_file(f'{danger} danger')
    kv_close = find.find_kv_close()
    fun.my_print_to_file(f"{kv_close}, kv_close")
    while not kv_skip_battle:
        sleep(1)
        kv_skip_battle = find.find_kv_skip_battle()
        fun.my_print_to_file(f'{kv_skip_battle} kv_skip_battle цикл ожидания')
    it_kv = 0
    while not kv_close:
        it_kv += 1
        if not danger and kv_skip_battle and it_kv >= 10:
            fun.mouse_move_to_click(pos_click=kv_skip_battle, z_p_k=0.5)
            # print(' пропуск боя')
        sleep(1)
        kv_skip_battle = find.find_kv_skip_battle()
        danger = find.find_kv_danger()
        kv_close = find.find_kv_close()
    if danger:
        print(" опасный")
        Hero.app_danger(Activ.hero_activ)
    kv_close = find.find_kv_close()
    if kv_close:
        # print(kv_close, 'kv_close')
        victory = find.find_victory_battle_in_kv()
        defeat = find.find_defeat_battle_in_kv()
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
    fun.mouse_move_to_click(pos_click=kv_close, z_p_k=0.3)

    # print("закрыть результат боя")


def kv():
    fun.my_print_to_file('kv_and_raid.kv')
    selection_hero_in_kv()
    kv_reload = find.find_kv_reload()
    # fun.my_print_to_file(f'kv_reload {kv_reload}')
    fun.my_print_to_file("нажать 'обновить'")
    fun.mouse_move_to_click(pos_click=kv_reload, z_p_k=1)

    q_attack = 0
    kv_wait_attack = find.find_kv_wait_attack()
    # fun.my_print_to_file(f'kv_wait_attack {kv_wait_attack}')
    kv_attak = find.find_kv_attak()
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
                kv_reload = find.find_kv_reload()
                fun.mouse_move_to_click(pos_click=kv_reload, z_p_k=1)
        if kv_attak:
            it_w_a = 0
            q_attack += 1
            fun.mouse_move_to_click(pos_click=kv_attak, z_p_k=0)
            battle(q_attack)
        kv_wait_attack = find.find_kv_wait_attack()
        kv_attak = find.find_kv_attak()


def loot():
    backpack = fun.locCenterImg('img/kv/backpack.png', confidence=0.9)
    fun.mouse_move(pos=backpack, speed=2)

    x, y = backpack
    x -= 220
    x_s = x
    y -= 145
    y_s = y
    pos = x, y
    fun.mouse_move(pos=pos, speed=2)
    x += 755
    x_r = x
    y += 615
    y_r = y
    pos = x, y
    fun.mouse_move(pos=pos, speed=2)

    name_foto = fun.date_and_time_in_name_file() + ".png"
    fun.foto(('img/Cr/' + name_foto), (x_s, y_s, x_r, y_r))


def go_in_clan():
    pass
