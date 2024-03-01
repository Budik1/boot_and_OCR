"""Файл показывает как перевести картинку в текст"""
import pyautogui
from event_OCR import visualization_result
from my_OCR import recognized
from fun import get_areas_task_small, get_areas_task_big


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x
    y_s = y_p_an + tune_y
    width_s = width_ - tune_s
    height_s = height_ - tune_v
    print(region, (x_s, y_s, width_s, height_s))
    foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = get_areas_task_small()
    region1_big, region2_big, region3_big = get_areas_task_big()
    foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/1_pul.png')
    foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/2_pul.png')
    foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/3_pul.png')
    foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/1_xp.png")
    foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/2_xp.png')
    foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/3_xp.png')

    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_3.png")


get_screenshot()
list_1_pul = recognized('img/test/1_pul.png')
list_1_xp = recognized("img/test/1_xp.png")

list_2_pul = recognized('img/test/2_pul.png')
list_2_xp = recognized("img/test/2_xp.png")

list_3_pul = recognized('img/test/3_pul.png')
list_3_xp = recognized("img/test/3_xp.png")
#
visualization_result(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)
#
