import pyautogui
from time import sleep
from event_OCR import visualization_result
from my_OCR import recognized
from fun import move_to_click
from fun_station_master import station_master


def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def get_task_area(width=77, height=42):
    pul = 444
    big = 100
    # закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    if close is not None:
        move_to_click(close, 0.3)
    # получение координат привязки
    pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
    pyautogui.moveTo(pos_klan)
    sleep(0.5)
    # print(pos_klan, 'ориентир клан')
    x_or, y_or = pos_klan

    station_master()

    # регион поиска 1 (позиция анализа)
    x_1an_pul = x_or + pul
    x_1an_xp = x_or + 518
    y_1an = y_or + 217
    x_1an_xp, y_1an = int(x_1an_xp), int(y_1an)
    region1 = [x_1an_xp, y_1an, width, height]
    region1_pul = [x_1an_pul, y_1an, width, height]
    region1_big = [x_1an_pul, y_1an, width + big, height]

    # регион поиска 2 (позиция анализа)
    x_2an_pul = x_or + pul
    x_2an_xp = x_or + 518
    y_2an = y_or + 320
    x_2an_xp, y_2an = int(x_2an_xp), int(y_2an)
    region2 = [x_2an_xp, y_2an, width, height]
    region2_pul = [x_2an_pul, y_2an, width, height]
    region2_big = [x_2an_pul, y_1an, width + big, height]

    # регион поиска 3 (позиция анализа)
    x_3an_pul = x_or + pul
    x_3an_xp = x_or + 518
    y_3an = y_or + 423
    x_3an_xp, y_3an = int(x_3an_xp), int(y_3an)
    region3 = [x_3an_xp, y_3an, width, height]
    region3_pul = [x_3an_pul, y_3an, width, height]
    region3_big = [x_3an_pul, y_1an, width + big, height]

    return region1_pul, region2_pul, region3_pul, region1, region2, region3, region1_big, region2_big, region3_big


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и коректировки снимка внутри него
    x_pOan, y_pOan, width_, height_ = region
    x_s = x_pOan + tune_x
    y_s = y_pOan + tune_y
    width_s = width_ - tune_s
    height_s = height_ - tune_v
    foto(name_img, (x_s, y_s, width_s, height_s))


def snimki():
    # смещение скрина внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    (region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp, region1_big, region2_big,
     region3_big) = get_task_area()
    foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/1_pul.png')
    foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/2_pul.png')
    foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/3_pul.png')
    foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/1_xp.png")
    foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/2_xp.png')
    foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/3_xp.png')

    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_3.png")


snimki()
list_1_xp = recognized("img/test/1_xp.png")
list_2_xp = recognized("img/test/2_xp.png")
list_3_xp = recognized("img/test/3_xp.png")
list_1_pul = recognized('img/test/1_pul.png')
list_2_pul = recognized('img/test/2_pul.png')
list_3_pul = recognized('img/test/3_pul.png')
#
visualization_result(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)
#
