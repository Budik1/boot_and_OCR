import pyautogui
from fun import find_link_klan, get_areas_task_small, get_areas_task_big, foto
from time import sleep

def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot_task():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_big, region2_big, region3_big = get_areas_task_big()

    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_3.png")

    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = get_areas_task_small()
    # foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/1_pul.png')
    # foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/2_pul.png')
    # foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/3_pul.png')
    # foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/1_xp.png")
    # foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/2_xp.png')
    # foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/3_xp.png')


def hero_img():
    pos = find_link_klan()
    x, y = pos
    x -= 179
    y -= 65
    x_v = x
    y_v = y
    foto('img/test/her1.png', (x_v, y_v, 84, 84))
    print("сделано")


hero_img()