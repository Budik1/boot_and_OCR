import pyautogui
from time import sleep
from event import move_to_click, my_print_list
from my_OCR import recognized


def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def station_master():
    # print('station_master')
    check = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
    # print(check, "check наличия 'img/station_master.png'")
    if check is not None:
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
        # print(na4)
        # proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(1)
    else:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
        while pos_or1 is None:
            sleep(0.1)
            pos_or1 = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
            # print('в поиске клана', pos_or1)
        # print('клан = ', pos_or1)
        x1, y1 = pos_or1
        x1, y1 = x1 - 60, y1 + 300  # x1 - 60, y1 + 200
        pos_or1 = x1, y1
        move_to_click(pos_or1, 0.1)
        # print('зашел к начальнику')
        sleep(1)
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
        # proverka_None(na4)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)


def orientir(shirina=77, vysota=42):
    # shirina, vysota = 77, 42
    # pul = 444
    # закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    if zakr is not None:
        move_to_click(zakr, 0.3)
    # получение координат привязки
    pos_orV = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
    pyautogui.moveTo(pos_orV)
    sleep(0.5)
    # print(pos_orV, 'ориентир клан')
    x_or, y_or = pos_orV

    station_master()

    # регион поиска 1 (позиция анализа)
    x_pOan1 = x_or + 518
    x_pOan1_pul = x_or + 444  # 518
    y_pOan1 = y_or + 217
    x_pOan1, y_pOan1 = int(x_pOan1), int(y_pOan1)
    region1 = [x_pOan1, y_pOan1, shirina, vysota]
    region1_pul = [x_pOan1_pul, y_pOan1, shirina, vysota]
    region1_big = [x_pOan1_pul, y_pOan1, shirina + 100, vysota]

    # регион поиска 2 (позиция анализа)
    x_pOan2 = x_or + 518
    x_pOan2_pul = x_or + 444
    y_pOan2 = y_or + 320  # 43
    x_pOan2, y_pOan2 = int(x_pOan2), int(y_pOan2)
    region2 = [x_pOan2, y_pOan2, shirina, vysota]
    region2_pul = [x_pOan2_pul, y_pOan2, shirina, vysota]
    region2_big = [x_pOan2_pul, y_pOan1, shirina + 100, vysota]

    # регион поиска 3 (позиция анализа)
    x_pOan3 = x_or + 518
    x_pOan3_pul = x_or + 444
    y_pOan3 = y_or + 423  # 146
    x_pOan3, y_pOan3 = int(x_pOan3), int(y_pOan3)
    region3 = [x_pOan3, y_pOan3, shirina, vysota]
    region3_pul = [x_pOan3_pul, y_pOan3, shirina, vysota]
    region3_big = [x_pOan3_pul, y_pOan1, shirina + 100, vysota]

    return region1_pul, region2_pul, region3_pul, region1, region2, region3, region1_big, region2_big, region3_big


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и коректировки снимка внутри него
    x_pOan, y_pOan, shirina, vysota = region
    # print(x_pOan, y_pOan)
    x_s = x_pOan + tune_x
    y_s = y_pOan + tune_y
    shirina_s = shirina - tune_s
    vysota_s = vysota - tune_v
    foto(name_img, (x_s, y_s, shirina_s, vysota_s))


def snimki():
    # смещение скрина внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp, region1_big, region2_big, region3_big = orientir()
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
my_print_list(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)
#

