import pyautogui
from fun import find_link_klan
import fun
from time import sleep


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot_task():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_big, region2_big, region3_big = fun.get_areas_task_big()

    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_3.png")

    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = fun.get_areas_task_small()
    # foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/1_pul.png')
    # foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/2_pul.png')
    # foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/3_pul.png')
    # foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/1_xp.png")
    # foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/2_xp.png')
    # foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/3_xp.png')


def hero_img():
    pos = fun.find_link_klan()
    x, y = pos
    x -= 179
    y -= 65
    x_v = x
    y_v = y
    fun.foto('img/test/her1.png', (x_v, y_v, 84, 84))
    print("сделано")


def victory_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 390
        y -= 264
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        # region = x, y
        # pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/victory_battle_in_kv.png', _region=(x, y, 140, 65))


def defeat_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 390
        y -= 264
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/defeat_battle_in_kv.png', _region=(x, y, 140, 65))


def detecting():
    victory = fun.locCenterImg('img/kv/victory_battle_in_kv.png', confidence=0.95)
    defeat = fun.locCenterImg('img/kv/defeat_battle_in_kv.png', confidence=0.95)
    if victory:
        result = "победа"
        print(result)

    elif defeat:
        result = "поражение"
        print(result)


def victory_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 55
        y -= 405
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/victory_in_arena.png', _region=(x, y, 140, 65))
    print('отработал')


def defeat_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 110
        y -= 295
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 180
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/defeat_in_arena.png', _region=(x, y, 180, 65))
    print('отработал')


def gift_img():
    pos = fun.find_link_klan()
    x, y = pos
    x += 118 # 148
    y += 350 # 300
    pyautogui.moveTo(x,y)
    x_v = x
    y_v = y
    x_v += 28
    pyautogui.moveTo(x_v, y)
    y_v += 40
    # pyautogui.moveTo(x_v, y_v)
    fun.foto('img/test/gift2.png', (x, y, 28, 25))
    print("сделано")


gift_img()
# defeat_in_arena()
# victory_in_arena()
# detecting()
# defeat_battle_in_kv()
# victory_battle_in_kv()
# hero_img()
