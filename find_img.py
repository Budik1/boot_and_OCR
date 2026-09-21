# from PIL import Image
import tools
from x_scale.act import get_actual_path
from baza import paths_img as p_i
from baza.baza_paths import actual_caliber_folder

import fun_down as fund

# from baza.paths_img import knob_png, kv_close_png

norm = 0.9
par_conf = 0.79
# img = None


def find_knob():
    actual_path = get_actual_path(path=p_i.knob_png)
    knob = fund.locateCenterImg(img=actual_path, confidence=0.99)
    return knob


def find_cancel():
    actual_path = get_actual_path(path=p_i.cansel_png)
    cancel = fund.locateCenterImg(img=actual_path)
    return cancel


def find_close():
    actual_path = get_actual_path(path=p_i.close_png)
    kv_close = find_kv_close()
    close = fund.locateCenterImg(img=actual_path)
    if kv_close:
        return kv_close
    elif close:
        return close
    else:
        return False


def find_hall_of_glory_tabl():
    actual_path = get_actual_path(path=p_i.hall_of_glory_tabl_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_hall_of_glory_icon():
    actual_path = get_actual_path(path=p_i.hall_of_glory_icon_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_station_master():
    actual_path = get_actual_path(path=p_i.station_master_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.91)
    return img


def find_klan():
    actual_path = get_actual_path(path=p_i.klan_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.9)
    return img


def find_choice_of_the_attacked(*, region: tuple[int, int, int, int] | None = None):
    actual_path = get_actual_path(path=p_i.choice_of_the_attacked_png)
    img = fund.locateCenterImg(img=actual_path, region=region)
    return img


def find_b_exit():
    actual_path = get_actual_path(path=p_i.b_exit_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_arena_object(*, region, hero):
    actual_path = get_actual_path(path=f"img/default/arena/{hero}/arena_object.png")
    img = fund.locateCenterImg(img=actual_path, region=region)  # 0.89
    return img


def find_scroll_up():
    actual_path = get_actual_path(path=p_i.scroll_up_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_scroll_down():
    actual_path = get_actual_path(path=p_i.scroll_down_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_attack_arena_opponent():
    actual_path = get_actual_path(path=p_i.attack_arena_opponent_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_her_gadya():
    actual_path = get_actual_path(path=p_i.gady_id)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_her_gavr():
    actual_path_arm = get_actual_path(path=p_i.gavr_arm)
    actual_path_id = get_actual_path(path=p_i.gavr_id)
    list_link = [actual_path_arm, actual_path_id]
    img_link = None
    for link in list_link:
        her_gavr = fund.locateCenterImg(img=link)
        if her_gavr:
            img_link = her_gavr
            break
    return img_link


def find_her_mara():
    actual_path = get_actual_path(path=p_i.mara_id)
    her_mara = fund.locateCenterImg(img=actual_path)
    return her_mara


def find_work():
    actual_path = get_actual_path(path=p_i.work_b_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_work_rest_hour(*, rest):
    actual_path = get_actual_path(path=f'img/default/station_master/work_hour/work_{rest}h.png')
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_exit_kv():
    actual_path = get_actual_path(path=p_i.exit_kv_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_kv_close():
    actual_path = get_actual_path(path=p_i.kv_close_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_kv_skip_battle():
    actual_path = get_actual_path(path=p_i.kv_skip_battle_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.85)
    return img


def find_kv_skip_battle_test():
    actual_path = get_actual_path(path=p_i.kv_skip_battle_test_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.85)
    return img


def find_skip_battle():
    actual_path = get_actual_path(path=p_i.skip_battle_png)
    img = fund.locateCenterImg(img=actual_path, confidence=par_conf)
    return img


def find_kv_danger():
    actual_path = get_actual_path(path=p_i.kv_danger_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_victory_battle_in_kv():
    actual_path = get_actual_path(path=p_i.victory_battle_in_kv_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.95)
    return img


def find_defeat_battle_in_kv():
    actual_path = get_actual_path(path=p_i.defeat_battle_in_kv_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.95)
    return img


def find_kv_reload():
    actual_path = get_actual_path(path=p_i.kv_reload_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_kv_attack_for_money():
    actual_path  = get_actual_path(path=p_i.kv_attack_for_money_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_kv_attak():
    actual_path = get_actual_path(path=p_i.kv_attak_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_b_vip(*, region_search):
    actual_path = get_actual_path(path=p_i.b_vip_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.8, region=region_search)
    return img


def find_inspect_tent():
    actual_path = get_actual_path(path=p_i.inspect_tent_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.8)
    return img


def find_b_tent(*, region_search):
    actual_path  = get_actual_path(path=p_i.b_tent_png)
    img = fund.locateCenterImg(img=actual_path, region=region_search, confidence=0.9)
    return img


def find_setting():
    actual_path = get_actual_path(path=p_i.setting_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.9)
    return img


def find_station_exit():
    actual_path = get_actual_path(path=p_i.station_exit_png)
    img = fund.locateCenterImg(img=actual_path, confidence=0.9)
    return img


def find_tonelli_attack():
    actual_path = get_actual_path(path=p_i.tonelli_attack_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_info():
    actual_path = get_actual_path(path=p_i.info_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_park_point():
    actual_path = get_actual_path(path=p_i.park_point)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_button_expand():
    actual_path = get_actual_path(path=p_i.button_expand_png)
    img = fund.locateCenterImg(img=actual_path)
    return img


def find_img_param(*, path_name, confidence, region=None):
    actual_path = get_actual_path(path=path_name)
    img = fund.locateCenterImg(img=actual_path, confidence=confidence, region=region)
    return img


def find_img(path_img):
    actual_path = get_actual_path(path=path_img)
    img = fund.locateCenterImg(img=actual_path)
    return img


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


def find_name6_kikimora():
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

def find_patron_mark(*, region):
    name_img = 'img/default/station_master/numbers/patron_mark.png'
    pos = fund.locateCenterImg(img=name_img, region=region)
    size = tools.img_processing.get_size_img(name_img=name_img)
    return pos, size

def find_xp_mark(*, region):
    name_img = 'img/default/station_master/numbers/xp_mark.png'
    pos = fund.locateCenterImg(img=name_img, region=region)
    size = tools.img_processing.get_size_img(name_img=name_img)
    return pos, size

def find_event_patron_mark(*, region):
    name_img='img/default/station_master/numbers/event_patron_mark.png'
    pos = fund.locateCenterImg(img=name_img, region=region)
    size = tools.img_processing.get_size_img(name_img=name_img)
    return pos, size

def find_event_xp_mark(*, region):
    name_img = 'img/default/station_master/numbers/event_xp_mark.png'
    pos = fund.locateCenterImg(img=name_img, region=region)
    size = tools.img_processing.get_size_img(name_img=name_img)
    return pos, size