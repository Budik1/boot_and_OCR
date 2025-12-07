import time
from time import sleep

import fun
import heroes
import sounds
import color_text
import baza_paths as b_p
import complex_phrases
import find_img as find
import color_text as myCt
import solid_memory


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
    # print('foto')


def foto_result_round(*, pos_v, pos_n, path=b_p.result_round, sound=False):
    # сужение
    # коррекция верхнего угла
    'img/ kv/ result_round/ result_all_round/'
    pos_x, pos_y = pos_v
    pos_x += 180
    pos_y += 45
    # коррекция нижнего угла
    x2, y2 = pos_n
    x_r = x2 - pos_x + 80 - 13
    y_r = y2 - pos_y - 20
    #
    name_foto = fun.date_and_time_in_name_file() + ".png"
    fun.foto((path + name_foto), (pos_x, pos_y, x_r, y_r))
    if sound:
        sounds.sound_victory()
    return


def foto_loot_kv(*, point_v, point_n):
    """
    
    :param point_v: 
    :param point_n: 
    :return: 
    """
    path = b_p.loot_round
    'img/ kv/ result_round/ result_round_loot/'
    kor_x_v = 30 + 90 - 35
    kor_y_v = 5 + 127 - 17
    # коррекция верхнего угла
    pos_x, pos_y = point_v
    pos_x += 150 + kor_x_v
    pos_y += 40 + kor_y_v
    # коррекция нижнего угла
    x2, y2 = point_n
    x_r = x2 - pos_x + 80 - 13
    y_r = y2 - pos_y - 20
    #
    name_foto = fun.date_and_time_in_name_file() + ".png"
    fun.foto((path + name_foto), (pos_x, pos_y, x_r, y_r))
    # if sound:
    #     sounds.sound_victory()
    return


def get_name_loot():
    dict_name_loot = {'сержант': 'img/kv/result_round/loot/p1.png',
                      'лейтенант': 'img/kv/result_round/loot/p2.png',
                      'капитан': 'img/kv/result_round/loot/p3.png',
                      'полковник': 'img/kv/result_round/loot/p4.png',
                      'генерал': 'img/kv/result_round/loot/p5.png'}
    result = 'неопознан'
    for name in dict_name_loot:
        name_loot = fun.locCenterImg(name_img=dict_name_loot[name])
        if name_loot:
            result = name_loot
            break
    return result


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


def update_set_dist(*, value_dist):
    temp_set_dist = heroes.Hero.get_set_dist(heroes.Activ.hero_activ)
    if temp_set_dist:
        temp_list = list(temp_set_dist)
    else:
        temp_list = []
    temp_list.append(value_dist)
    set_dist = set(temp_list)
    heroes.Hero.set_set_dist(heroes.Activ.hero_activ, set_dist)
    # отладка
    min_dist = min(set_dist)
    max_dist = max(set_dist)
    print(f'{set_dist=}, {min_dist=}, {max_dist=}')
    return


def distance(*, pos_vic: tuple, pos_cl: tuple) -> int:
    x_vic, y_vic = pos_vic
    x_cl, y_cl = pos_cl
    dist = y_cl - y_vic

    return dist


def battle(target_call):
    fun.my_log_file('kv_and_raid.battle')
    kv_skip_battle = find.find_kv_skip_battle()
    fun.my_log_file(f'{kv_skip_battle} kv_skip_battle')
    danger = find.find_kv_danger()
    fun.my_log_file(f'{danger} danger')
    kv_close = find.find_kv_close()
    fun.my_log_file(f"{kv_close}, kv_close")
    mes = ''
    dang = ''
    while not kv_skip_battle:
        sleep(1)
        kv_skip_battle = find.find_kv_skip_battle()
        fun.my_log_file(f'{kv_skip_battle} kv_skip_battle цикл ожидания')
    it_kv = 0
    while not kv_close:
        it_kv += 1
        if not danger and kv_skip_battle and it_kv >= 10:
            fun.mouse_move_to_click(pos_click=kv_skip_battle, z_p_k=0.5)
        sleep(1)
        kv_skip_battle = find.find_kv_skip_battle()
        danger = find.find_kv_danger()
        kv_close = find.find_kv_close()
    if danger:
        dang = myCt.tc_magenta("опасный ")
        heroes.Hero.app_qty_danger(heroes.Activ.hero_activ)
    kv_close = find.find_kv_close()
    if kv_close:
        victory = find.find_victory_battle_in_kv()
        defeat = find.find_defeat_battle_in_kv()
        if victory:
            result = myCt.tc_yellow("победа ")

            heroes.Hero.up_qty_duel_in_kv_victory(heroes.Activ.hero_activ)
            # print(Hero.get_name_ru(Activ.hero_activ))
            dist_report = distance(pos_vic=victory, pos_cl=kv_close)
            update_set_dist(value_dist=dist_report)
            min_dist = min(heroes.Hero.get_set_dist(heroes.Activ.hero_activ))
            foto_result_round(pos_v=victory, pos_n=kv_close)
            if dist_report > (min_dist/10 + min_dist):
                heroes.Hero.up_count_shoulder_straps_all(heroes.Activ.hero_activ)
                heroes.Hero.up_count_shoulder_straps_kv(heroes.Activ.hero_activ)
                mes = color_text.tc_red('Погон!!')
                foto_result_round(pos_v=victory, pos_n=kv_close,
                                  path='img/kv/result_round/p/', sound=True)
                # foto_loot_kv(point_v=victory, point_n=kv_close)
                # опознать погон
                name_loot = get_name_loot()
                # записать в лист
                list_loot = heroes.Hero.get_list_loot(heroes.Activ.hero_activ)
                list_loot.append(name_loot)

                heroes.Hero.set_list_loot(heroes.Activ.hero_activ, list_loot)

            if danger:
                heroes.Hero.app_danger_v(heroes.Activ.hero_activ)
                foto_danger()
        elif defeat:
            result = myCt.tc_red("поражение ")
        else:
            heroes.Activ.duel_raid += 1
            result = heroes.Activ.duel_raid
        rapport_battle = f'{target_call} {dang}{result}{mes}'
        print(rapport_battle)
        solid_memory.save_kv_config(info=False)
    fun.mouse_move_to_click(pos_click=kv_close, z_p_k=0.3)


def kv():
    fun.my_log_file('kv_and_raid.kv')
    selection_hero_in_kv()
    stat, data_kv = solid_memory.reading_kv_config()
    solid_memory.set_values_kv(data_kv)
    phrase_eff = complex_phrases.report_kv_efficiency()
    print(phrase_eff[0])
    print(phrase_eff[1])
    print()
    # print(color_text.tc_red('Время КВ установлено'))
    kv_reload = find.find_kv_reload()
    # fun.my_print_to_file(f'kv_reload {kv_reload}')
    fun.my_log_file("нажать 'обновить'")
    fun.mouse_move_to_click(pos_click=kv_reload, z_p_k=1)

    kv_wait_attack = find.find_kv_attack_for_money()
    attack = find.find_kv_attak()
    klan_war = find.find_klan_kv_label()
    if not attack and not kv_wait_attack:
        print('ждем начало кв')
    it_w_a = 0
    while True:
        if kv_wait_attack:
            it_w_a += 1
            if it_w_a == 1:
                # print("ждем возможность атаковать")
                kv_reload = find.find_kv_reload()
                fun.mouse_move_to_click(pos_click=kv_reload, z_p_k=1)
        if attack:
            heroes.Hero.set_last_attack(heroes.Activ.hero_activ, value=time.time())
            if klan_war:
                it_w_a = 0
                heroes.Hero.up_qty_duel_in_kv_all(heroes.Activ.hero_activ)
                fun.mouse_move_to_click(pos_click=attack, move_time=0.01, z_p_k=0)
                qty_duel = heroes.Hero.get_qty_duel_in_kv_all(heroes.Activ.hero_activ)
                target_attack = f'дуэль {qty_duel}'
                if qty_duel == 1:
                    print('Первый бой - истинное начало кв')
                    heroes.Hero.set_time_start_kv(self=heroes.Activ.hero_activ, value=time.time())
                    solid_memory.save_kv_config(info=False)

                battle(target_call=target_attack)
                phrase_eff = complex_phrases.report_kv_efficiency()
                print(phrase_eff[0])
                print(phrase_eff[1])
                if phrase_eff[2]:
                    print(phrase_eff[2])
                # print(complex_phrases.report_shoulder_straps())
                print()
            else:
                it_w_a = 0
                target_attack = 'Raid'
                fun.mouse_move_to_click(pos_click=attack, move_time=0.01, z_p_k=0)
                battle(target_call=target_attack)
        kv_wait_attack = find.find_kv_attack_for_money()
        attack = find.find_kv_attak()
        klan_war = find.find_klan_kv_label()


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
