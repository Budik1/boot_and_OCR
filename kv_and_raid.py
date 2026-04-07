import time
from time import sleep

import find_img
import fun
import find_img as find
import heroes
import os_action
import solid_memory
import tools

from baza import baza_paths as b_p
from baza import paths_img as p_i
from tools import color_text as c_t
from tools import sounds


def foto_danger():
    fun.log_with_caller(message='a')
    kv_close = find.find_close()
    x, y = kv_close
    x -= 585
    y -= 435
    x_s, y_s = x, y
    x += 862
    y += 485
    x_r, y_r = x, y
    # Проверить наличие пути для создания файла!!!
    os_action.create_folder(path=b_p.danger)  # f'img/{actual_caliber}/kv/temp/danger/'
    name_foto = tools.date_and_time_in_name_file() + ".png"
    fun.foto((b_p.danger + name_foto), (x_s, y_s, x_r, y_r))
    # print('foto')
    fun.log_with_caller(message='e')


def foto_result_round(*, pos_v, pos_n, path=b_p.result_round_temp, sound=False):
    """

    :param pos_v:
    :param pos_n:
    :param path: f'img/{actual_caliber}/kv/temp/result_round/result_all_round/'
    :param sound:
    :return:
    """
    fun.log_with_caller(message='a')
    # коррекция верхнего угла
    pos_x, pos_y = pos_v
    pos_x += 180
    pos_y += 45
    # коррекция нижнего угла
    x2, y2 = pos_n
    x_r = x2 - pos_x + 80 - 13
    y_r = y2 - pos_y - 20
    # Проверить наличие пути для создания файла!!!
    os_action.create_folder(path=path)
    #
    name_foto = tools.date_and_time_in_name_file() + ".png"
    fun.foto((path + name_foto), (pos_x, pos_y, x_r, y_r))
    # print('Создан фото ', (path + name_foto))
    if sound:
        sounds.sound_victory()
    fun.log_with_caller(message='e')
    return


def get_name_loot_kv():
    fun.log_with_caller(message='a')
    dict_name_loot = {'сержант': p_i.p1_png,
                      'лейтенант': p_i.p2_png,
                      'капитан': p_i.p3_png,
                      'полковник': p_i.p4_png,
                      'генерал': p_i.p5_png}
    result = 'неопознан'
    for name in dict_name_loot:
        name_loot = find_img.find_img(path_img=dict_name_loot[name])
        if name_loot:
            result = name
            break
    fun.log_with_caller(message='e')
    return result


def selection_hero_in_kv():
    fun.log_with_caller(message='a')
    hero = fun.selection_hero()
    if not hero:
        exit_kv = find.find_exit_kv()
        if exit_kv:
            tools.Mouse.move_to_click(pos_click=exit_kv)
        hero = fun.selection_hero()
    klan = fun.find_link_klan()
    if klan:
        x, y = klan
        x += 100
        pos = x, y
        tools.Mouse.move_to_click(pos_click=pos)
    fun.log_with_caller(message='e')
    return hero


def update_set_dist(*, value_dist):
    fun.log_with_caller(message='a')
    temp_set_dist = heroes.Hero.get_set_dist(heroes.Activ.hero_activ)
    if temp_set_dist:
        temp_list = list(temp_set_dist)
    else:
        temp_list = []
    temp_list.append(value_dist)
    set_dist = set(temp_list)
    heroes.Hero.set_set_dist(heroes.Activ.hero_activ, set_dist)
    fun.log_with_caller(message='e')
    return


def battle(*, target_call):
    fun.log_with_caller(message='a')
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
            tools.Mouse.move_to_click(pos_click=kv_skip_battle, z_p_k=0.5)
        sleep(1)
        kv_skip_battle = find.find_kv_skip_battle()
        danger = find.find_kv_danger()
        kv_close = find.find_kv_close()
    if danger:
        dang = c_t.tc_magenta("опасный ")
        heroes.Hero.app_qty_danger(heroes.Activ.hero_activ)
    kv_close = find.find_kv_close()
    if kv_close:
        victory = find.find_victory_battle_in_kv()
        defeat = find.find_defeat_battle_in_kv()
        if victory:
            result = c_t.tc_yellow("победа ")

            heroes.Hero.up_qty_duel_in_kv_victory(heroes.Activ.hero_activ)
            fig, dist_report = fun.distance(pos_upper=victory, pos_lower=kv_close)
            update_set_dist(value_dist=dist_report)
            min_dist = min(heroes.Hero.get_set_dist(heroes.Activ.hero_activ))
            foto_result_round(pos_v=victory, pos_n=kv_close)
            if dist_report > (min_dist / 10 + min_dist):
                heroes.Hero.up_count_shoulder_straps_all(heroes.Activ.hero_activ)
                heroes.Hero.up_count_shoulder_straps_kv(heroes.Activ.hero_activ)
                mes = c_t.tc_red('Погон!!')
                foto_result_round(pos_v=victory, pos_n=kv_close,
                                  path=b_p.result_round_p, sound=True)
                # опознать погон
                name_loot = get_name_loot_kv()
                # записать в лист
                list_loot = heroes.Hero.get_list_loot(heroes.Activ.hero_activ)
                list_loot.append(str(name_loot))
                heroes.Hero.set_list_loot(heroes.Activ.hero_activ, list_loot)

            if danger:
                heroes.Hero.app_danger_v(heroes.Activ.hero_activ)
                foto_danger()
        elif defeat:
            result = c_t.tc_red("поражение ")
        else:
            heroes.Activ.duel_raid += 1
            result = heroes.Activ.duel_raid
        rapport_battle = f'{target_call} {dang}{result}{mes}'
        print(rapport_battle)
        solid_memory.save_kv_state_config_json(info=False)
    tools.Mouse.move_to_click(pos_click=kv_close, z_p_k=0.3)
    fun.log_with_caller(message='e')


def kv():
    fun.log_with_caller(message='a')
    selection_hero_in_kv()
    solid_memory.reading_kv_config_json()
    solid_memory.set_values_kv()
    phrase_eff = tools.report_kv_efficiency()
    print(phrase_eff[0])
    print(phrase_eff[1])
    if phrase_eff[2]:
        print(phrase_eff[2])
    print()
    kv_reload = find.find_kv_reload()
    # fun.my_print_to_file(f'kv_reload {kv_reload}')
    fun.my_log_file("нажать 'обновить'")
    tools.Mouse.move_to_click(pos_click=kv_reload, z_p_k=1)
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
                tools.Mouse.move_to_click(pos_click=kv_reload, z_p_k=1)
        if attack:
            heroes.Hero.set_last_attack(heroes.Activ.hero_activ, value=time.time())
            if klan_war:
                it_w_a = 0
                heroes.Hero.up_qty_duel_in_kv_all(heroes.Activ.hero_activ)
                tools.Mouse.move_to_click(pos_click=attack, speed=0.01, z_p_k=0)
                qty_duel = heroes.Hero.get_qty_duel_in_kv_all(heroes.Activ.hero_activ)
                target_attack = f'дуэль {qty_duel}'
                if qty_duel == 1:
                    print('Первый бой - истинное начало кв')
                    heroes.Hero.set_time_start_kv(self=heroes.Activ.hero_activ, value=time.time())
                    solid_memory.save_kv_state_config_json(info=False)

                battle(target_call=target_attack)
                phrase_eff = tools.report_kv_efficiency()
                print(phrase_eff[0])
                print(phrase_eff[1])
                if phrase_eff[2]:
                    print(phrase_eff[2])
                print()
            else:
                it_w_a = 0
                target_attack = 'Raid'
                tools.Mouse.move_to_click(pos_click=attack, speed=0.01, z_p_k=0)
                battle(target_call=target_attack)
        kv_wait_attack = find.find_kv_attack_for_money()
        attack = find.find_kv_attak()
        klan_war = find.find_klan_kv_label()
    # fun.log_with_caller(message='e')
