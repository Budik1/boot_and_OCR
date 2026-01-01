import pyautogui
from time import sleep
import find_img as find
import fun
import heroes

speed_mouse = 1

# определить регион поиска
def detect_region_search_vip():
    pos_klan = find.find_klan()
    pos_settings = find.find_setting()
    while not pos_klan and not pos_settings:
        sleep(0.2)
        pos_klan = find.find_klan()
        pos_settings = find.find_setting()
    if pos_klan:
        x_region, y_region = pos_klan
        x_region -= 125
        y_region += 503
        region_search = (x_region, y_region, 59, 132)
    else:
        x_region, y_region = pos_settings
        x_region -= 776
        y_region -= 10
        region_search = (x_region, y_region, 59, 132)

    return region_search


def vip_click(region_search):
    sleep(1)
    pos_vip = find.find_b_vip(region_search=region_search)
    pyautogui.moveTo(pos_vip, duration=1)
    fun.mouse_left_click(pos=pos_vip)
    # print('клик по VIP ' + str(pos_vip))
    sleep(1)


def tent_detected(region_search):
    sleep(1)
    dom = find.find_b_tent(region_search=region_search)
    fun.Mouse.move(pos= dom, speed=1)
    fun.Mouse.left_click(pos=dom)
    # print('клик по дом ' + str(dom))
    sleep(1)


def visit_to_tent():
    """Возвращает 1 если есть и 0 если пусто """
    visit = find.find_inspect_tent()
    if visit:
        fun.Mouse.move(pos=visit, speed=1)
        fun.Mouse.left_click(pos=visit)
        cl = fun.push_close()
        if not cl:
            # print("клик обыск" + str(visit))
            vip = 1
        else:
            vip = 0
    else:
        # print(' уже обыскан ')
        vip = 0
    return vip


def end_raid():
    pyautogui.moveTo(200, 670)
    sleep(1)
    b_exit = find.find_b_exit()
    fun.Mouse.move(pos= b_exit, speed=1)
    fun.Mouse.left_click(pos=b_exit)
    print('обход палаток окончен')
    fun.Mouse.move(pos=(200, 670), speed=2)


def tent_raid():
    region = detect_region_search_vip()
    pos_vip = find.find_b_vip(region_search=region)
    while not pos_vip:
        fun.move_friends_list_left()
        #
        region = detect_region_search_vip()
        pos_vip = find.find_b_vip(region_search=region)
    vip_click(region)
    tent = find.find_b_tent(region_search=region)
    while not tent:
        sleep(0.2)
        vip_click(region)
        tent = find.find_b_tent(region_search=region)
    # print(' дом найден')
    tent_detected(region)
    vip_result = visit_to_tent()
    #
    return vip_result

def qty_vip():
    sleep(1)
    region = detect_region_search_vip()
    # print(f'{region=}')
    pos_vip = find.find_b_vip(region_search=region)
    # print(f'{pos_vip=}')
    while not pos_vip:
        fun.move_friends_list_left()
        region = detect_region_search_vip()
        pos_vip = find.find_b_vip(region_search=region)
    if pos_vip:
        print('vip detect')
        heroes.Activ.qty_vip += 1
        print(f'{heroes.Activ.qty_vip}')
        fun.move_friends_list_left()
