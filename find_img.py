import pyautogui
import fun_down

norm = 0.9
par_conf = 0.79


def locCenterImg(*, name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None):
    pos_img = pyautogui.locateCenterOnScreen(name_img,
                                             confidence=confidence,
                                             region=region)
    return pos_img


def find_knob():
    knob = fun_down.locateCenterImg(name_img='img/overall/knob.png')
    return knob


def find_cancel():
    cancel = locCenterImg(name_img='img/overall/cancel.png')
    return cancel


def find_close():
    kv_close = locCenterImg(name_img='img/kv/kv_close.png', confidence=par_conf)
    close = locCenterImg(name_img='img/overall/close.png')
    if kv_close:
        return kv_close
    elif close:
        return close
    else:
        return False


def find_hall_of_glory_tabl():
    hall = locCenterImg(name_img='img/arena/hall_of_glory_tabl.png')
    return hall


def find_hall_of_glory_icon():
    point_hall_of_glory = locCenterImg(name_img='img/arena/hall_of_glory_icon.png')
    return point_hall_of_glory


def find_station_master():
    station_master = locCenterImg(name_img='img/station_master/station_master.png')
    return station_master


def find_klan():
    pos_klan = locCenterImg(name_img='img/overall/klan.png', confidence=0.9)
    return pos_klan


def find_attack(*, region: tuple[int, int, int, int] | None = None):
    attack = locCenterImg(name_img='img/arena/attack.png', region=region)
    return attack


def find_b_exit():
    b_exit = locCenterImg(name_img='img/b_exit.png')
    return b_exit


def find_arena_object(*, region):
    arena_object = locCenterImg(name_img="img/arena/arena_object.png", region=region)  # 0.89
    return arena_object


def find_scroll_up():
    scroll_up = locCenterImg(name_img='img/arena/scroll_up.png')
    return scroll_up


def find_scroll_down():
    scroll_down = locCenterImg(name_img='img/arena/scroll_down.png')
    return scroll_down


def find_hero_vs_opponent():
    hero_vs_opponent = locCenterImg(name_img='img/arena/hero_vs_opponent.png')
    return hero_vs_opponent


def find_her_gadya():
    hero_gadya = locCenterImg(name_img='img/person/her_gadya.png')
    return hero_gadya


def find_her_gavr():
    her_gavr = locCenterImg(name_img='img/person/her_gavr.png')
    return her_gavr


def find_her_veles():
    her_veles = locCenterImg(name_img='img/person/her_veles.png')
    return her_veles


def find_her_mara():
    her_mara = locCenterImg(name_img='img/person/her_mara.png')
    return her_mara


def find_work():
    pos_work = locCenterImg(name_img='img/overall/work.png')
    return pos_work


def find_work_8_hour():
    work_8hour = locCenterImg(name_img='img/overall/work_8_hour.png')
    return work_8hour


def find_exit_kv():
    exit_kv = locCenterImg(name_img='img/kv/exit_kv.png')
    return exit_kv


def find_kv_close():
    kv_close = locCenterImg(name_img='img/kv/kv_close.png')
    return kv_close


def find_kv_skip_battle():
    kv_skip_battle = locCenterImg(name_img='img/kv/kv_skip_battle.png', confidence=0.85)
    return kv_skip_battle


def find_skip_battle():
    skip_battle = locCenterImg(name_img='img/skip_battle.png', confidence=par_conf)
    return skip_battle


def find_kv_danger():
    danger = locCenterImg(name_img='img/kv/kv_danger.png')
    return danger


def find_victory_battle_in_kv():
    victory = locCenterImg(name_img='img/kv/victory_battle_in_kv.png', confidence=0.95)
    return victory


def find_defeat_battle_in_kv():
    defeat = locCenterImg(name_img='img/kv/defeat_battle_in_kv.png', confidence=0.95)
    return defeat


def find_kv_reload():
    kv_reload = locCenterImg(name_img='img/kv/kv_reload.png')
    return kv_reload


def find_kv_attack_for_money():
    attack_for_money = locCenterImg(name_img='img/kv/kv_attack for money.png')
    return attack_for_money


def find_kv_attak():
    kv_attak = locCenterImg(name_img='img/kv/kv_attak.png')
    return kv_attak


def find_b_vip(*, region_search):
    pos_vip = locCenterImg(name_img='img/tents_R/b_vip.png', confidence=0.8, region=region_search)
    return pos_vip


def find_inspect_tent():
    visit = locCenterImg(name_img="img/tents_R/inspect tent.png", confidence=0.8)
    return visit


def find_b_tent(*, region_search):
    dom = locCenterImg(name_img='img/tents_R/b_tent.png', region=region_search, confidence=0.9)
    return dom


def find_setting():
    pos_settings = locCenterImg(name_img='img/setting.png', confidence=0.9)
    return pos_settings


def find_station_exit():
    station_exit = locCenterImg(name_img='img/tonelli/station_exit.png', confidence=0.9)
    return station_exit

def find_tonelli_attack():
    attack = locCenterImg(name_img='img/tonelli/attack.png')
    return attack

def find_info():
    info = locCenterImg(name_img='img/overall/info.png') # img/overall/info.png
    return info

def name():
    pos = fun_down.locateCenterImg('')
    return pos