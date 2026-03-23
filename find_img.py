from PIL import Image
from x_scale.act import get_actual_path
from baza import paths_img as p_i
from baza.baza_paths import actual_caliber_folder

import fun_down as fund
# from baza.paths_img import knob_png, kv_close_png

norm = 0.9
par_conf = 0.79


def find_knob():
    path_img = get_actual_path(path=p_i.knob_png)
    knob = fund.locateCenterImg(img=path_img, confidence=0.99)
    return knob


def find_cancel():

    cancel = fund.locateCenterImg(img=p_i.cansel_png)
    return cancel


def find_close():
    kv_close = find_kv_close()
    close = fund.locateCenterImg(img=p_i.close_png)
    if kv_close:
        return kv_close
    elif close:
        return close
    else:
        return False


def find_hall_of_glory_tabl():
    hall = fund.locateCenterImg(img=p_i.hall_of_glory_tabl_png)
    return hall


def find_hall_of_glory_icon():
    point_hall_of_glory = fund.locateCenterImg(img=p_i.hall_of_glory_icon_png)
    return point_hall_of_glory


def find_station_master():
    station_master = fund.locateCenterImg(img=p_i.station_master_png, confidence=0.91)
    return station_master


def find_klan():
    pos_klan = fund.locateCenterImg(img=p_i.klan_png, confidence=0.9)
    return pos_klan


def find_choice_of_the_attacked(*, region: tuple[int, int, int, int] | None = None):
    attack = fund.locateCenterImg(img=p_i.choice_of_the_attacked_png, region=region)
    return attack


def find_b_exit():
    b_exit = fund.locateCenterImg(img=p_i.b_exit_png)
    return b_exit


def find_arena_object(*, region, hero):
    arena_object = fund.locateCenterImg(img=f"img/{actual_caliber_folder}/arena/{hero}/arena_object.png",
                                        region=region)  # 0.89
    return arena_object


def find_scroll_up():
    scroll_up = fund.locateCenterImg(img=p_i.scroll_up_png)
    return scroll_up


def find_scroll_down():
    scroll_down = fund.locateCenterImg(img=p_i.scroll_down_png)
    return scroll_down


def find_attack_arena_opponent():
    hero_vs_opponent = fund.locateCenterImg(img=p_i.attack_arena_opponent_png)
    return hero_vs_opponent


def find_her_gadya():
    hero_gadya = fund.locateCenterImg(img=p_i.gady_id)
    return hero_gadya


def find_her_gavr():
    list_link = [p_i.gavr_arm, p_i.gavr_id]
    img_link = None
    for link in list_link:
        her_gavr = fund.locateCenterImg(img=link)
        if her_gavr:
            img_link = her_gavr
            break
    return img_link


def find_her_mara():
    her_mara = fund.locateCenterImg(img=p_i.mara_id)
    return her_mara


def find_work():
    pos_work = fund.locateCenterImg(img=p_i.work_b_png)
    return pos_work


def find_work_rest_hour(*, rest):
    pos_work = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/station_master/work_hour/work_{rest}h.png')
    return pos_work


def find_exit_kv():
    exit_kv = fund.locateCenterImg(img=p_i.exit_kv_png)
    return exit_kv


def find_kv_close():
    kv_close = fund.locateCenterImg(img=p_i.kv_close_png)
    return kv_close


def find_kv_skip_battle():
    kv_skip_battle = fund.locateCenterImg(img=p_i.kv_skip_battle_png, confidence=0.85)
    return kv_skip_battle


def find_kv_skip_battle_test():
    kv_skip_battle = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/kv/kv_skip_battle_test.png',
                                          confidence=0.85)
    return kv_skip_battle


def find_skip_battle():
    skip_battle = fund.locateCenterImg(img=p_i.skip_battle_png, confidence=par_conf)
    return skip_battle


def find_kv_danger():
    danger = fund.locateCenterImg(img=p_i.kv_danger_png)
    return danger


def find_victory_battle_in_kv():
    victory = fund.locateCenterImg(img=p_i.victory_battle_in_kv_png, confidence=0.95)
    return victory


def find_defeat_battle_in_kv():
    defeat = fund.locateCenterImg(img=p_i.defeat_battle_in_kv_png, confidence=0.95)
    return defeat


def find_kv_reload():
    kv_reload = fund.locateCenterImg(img=p_i.kv_reload_png)
    return kv_reload


def find_kv_attack_for_money():
    attack_for_money = fund.locateCenterImg(img=p_i.kv_attack_for_money_png)
    return attack_for_money


def find_kv_attak():
    kv_attak = fund.locateCenterImg(img=p_i.kv_attak_png)
    return kv_attak


def find_b_vip(*, region_search):
    pos_vip = fund.locateCenterImg(img=p_i.b_vip_png, confidence=0.8, region=region_search)
    return pos_vip


def find_inspect_tent():
    visit = fund.locateCenterImg(img=p_i.inspect_tent_png, confidence=0.8)
    return visit


def find_b_tent(*, region_search):
    dom = fund.locateCenterImg(img=p_i.b_tent_png, region=region_search, confidence=0.9)
    return dom


def find_setting():
    pos_settings = fund.locateCenterImg(img=p_i.setting_png, confidence=0.9)
    return pos_settings


def find_station_exit():
    station_exit = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/station_exit.png', confidence=0.9)
    return station_exit


def find_tonelli_attack():
    attack = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/attack.png')
    return attack


def find_info():
    info = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/info.png')  # img/overall/info.png
    return info


def find_my_game2():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/my_game2.png')
    return pos


def find_button_expand():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/button_expand.png')
    return pos


def find_img_param(*, path_name, confidence, region=None):
    pos = fund.locateCenterImg(img=path_name, confidence=confidence, region=region)
    return pos


def find_img(name_img):
    pos = fund.locateCenterImg(img=name_img)
    return pos


def find_smol_slot():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/slots/smol_slot.png')
    return pos


def find_exit_person():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/exit_person.png')
    return pos


def find_low_energy_label():
    pos = fund.locateCenterImg(
        img=f'img/{actual_caliber_folder}/station_master/energy_indicator/low_energy_label.png',
        confidence=0.8)
    return pos


def find_no_energy():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/station_master/energy_indicator/no_energy.png')
    return pos


def find_en_1():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/station_master/energy_value/en_1.png')
    return pos


def find_klan_kv_label():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/kv/tests/klan_kv_label.png')
    return pos


def find_g():
    pos_g = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/metro.png')
    return pos_g


def find_link_money_token():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/link_money_token.png')
    return pos


def find_b_battle_end(confidence_param=None):
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/b_battle_end.png', confidence=confidence_param)
    return pos


def find_mark_left():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/test/mark/mark_left.png')
    return pos


def find_mark_sever():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mark_sever.png')
    return pos


def find_mark_yug():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mark_yug.png')
    return pos


def find_add_acc():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/change_hero/add_acc.png')
    return pos


def find_menu_acc_her_gadya():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/hero_id/gady/menu_acc_her_gadya.png')
    return pos


def find_menu_acc_her_gavr():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/hero_id/gavr/menu_acc_her_gavr.png')
    return pos


def find_menu_acc_her_mara():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/hero_id/mara/menu_acc_her_mara.png')
    return pos


def find_change_hero_gady():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/change_hero/change_hero_gady.png')
    return pos


def find_change_hero_gavr():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/change_hero/change_hero_gavr.png')
    return pos


def find_change_hero_mara():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/person/change_hero/change_hero_mara.png')
    return pos


def find_continue_gady():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/event_entry/continue_gady.png')
    return pos


def find_continue_gavr():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/event_entry/continue_gavr.png')
    return pos


def find_continue_mara():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/event_entry/continue_mara.png')
    return pos


def find_my_game1():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/my_game1.png')
    return pos


def find_dog_2(par_conf_):
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/overall/dog_2.png', confidence=par_conf_)
    return pos


def find_dog():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/dog.png')
    return pos


def find_name1_grey_rat():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name1_grey_rat.png')
    return pos


def find_name1_white_rat():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name1_white_rat.png')
    return pos


def find_name1_black_rat():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name1_black_rat.png')
    return pos


def find_name1_sand_rat():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name1_sand_rat.png')
    return pos


def find_name2_spy():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name2_spy.png')
    return pos


def find_name3_smuggler():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name3_smuggler.png')
    return pos


def find_name4_arachne():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name4_arachne.png')
    return pos


def find_name5_wildman():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name5_wildman.png')
    return pos


def find_name_kikimora():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name6_kikimora.png')
    return pos


def find_name7_raptor():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/mobi/name7_raptor.png')
    return pos


def find_victory_in_arena():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/arena/overall/victory_in_arena.png')
    return pos


def find_defeat_in_arena():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/arena/overall/defeat_in_arena.png')
    return pos


def find_gift():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/gift.png')
    return pos


def find_gift2():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/gift2.png')
    return pos


def find_post():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/post.png')
    return pos


def find_entry_station():
    pos = fund.locateCenterImg(img=f'img/{actual_caliber_folder}/tonelli/entry_station.png')
    return pos
