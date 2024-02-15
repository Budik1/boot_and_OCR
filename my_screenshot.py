"""Файл показывает как перевести картинку в текст"""
import pyautogui
from time import sleep
from event_OCR import visualization_result
from my_OCR import recognized
from fun import push_close_all_
from fun_station_master import station_master


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def get_task_area_small(width=77, height=42):
    """из my_screenshot"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423
    # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    push_close_all_()
    # получение координат привязки
    pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
    pyautogui.moveTo(pos_klan)
    sleep(0.5)
    # print(pos_klan, 'ориентир клан')
    x_or, y_or = pos_klan

    station_master()

    x_an_xp = x_or + xp_
    x_an_pul = x_or + pul

    # регион поиска 1 (позиция анализа)
    y_1an = y_or + pos_1
    # y_1an = int(y_1an)
    region1 = [x_an_xp, y_1an, width, height]
    region1_pul = [x_an_pul, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = y_or + pos_2
    # y_2an = int(y_2an)
    region2 = [x_an_xp, y_2an, width, height]
    region2_pul = [x_an_pul, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = y_or + pos_3
    # y_3an = int(y_3an)
    region3 = [x_an_xp, y_3an, width, height]
    region3_pul = [x_an_pul, y_3an, width, height]

    return region1_pul, region2_pul, region3_pul, region1, region2, region3


def get_task_area_big(width=77, height=42):
    """из my_screenshot"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423
    big = 100
    # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    push_close_all_()
    # получение координат привязки
    pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
    pyautogui.moveTo(pos_klan)
    sleep(0.5)
    # print(pos_klan, 'ориентир клан')
    x_or, y_or = pos_klan

    station_master()

    x_an_pul = x_or + pul

    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region1_big = [x_an_pul, y_1an, width + big, height]

    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region2_big = [x_an_pul, y_2an, width + big, height]

    # регион поиска 3 (позиция анализа)
    y_3an = int(y_or + pos_3)
    region3_big = [x_an_pul, y_3an, width + big, height]

    return region1_big, region2_big, region3_big


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x
    y_s = y_p_an + tune_y
    width_s = width_ - tune_s
    height_s = height_ - tune_v
    foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = get_task_area_small()
    region1_big, region2_big, region3_big = get_task_area_big()
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
list_1_xp = recognized("img/test/1_xp.png")
list_2_xp = recognized("img/test/2_xp.png")
list_3_xp = recognized("img/test/3_xp.png")
list_1_pul = recognized('img/test/1_pul.png')
list_2_pul = recognized('img/test/2_pul.png')
list_3_pul = recognized('img/test/3_pul.png')
#
visualization_result(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)
#
