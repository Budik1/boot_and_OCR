import pyautogui
from fun import move_to_click
from time import sleep
from fun_station_master import station_master


def get_task_area_small(width=77, height=42):
    """из my_screenshot"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423
    big = 100
    # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
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
    y_1an = y_or + pos_1
    x_1an_pul = x_or + pul
    x_1an_xp = x_or + xp_
    x_1an_xp, y_1an = int(x_1an_xp), int(y_1an)
    region1 = [x_1an_xp, y_1an, width, height]
    region1_pul = [x_1an_pul, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = y_or + pos_2
    x_2an_pul = x_or + pul
    x_2an_xp = x_or + xp_
    x_2an_xp, y_2an = int(x_2an_xp), int(y_2an)
    region2 = [x_2an_xp, y_2an, width, height]
    region2_pul = [x_2an_pul, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = y_or + pos_3
    x_3an_pul = x_or + pul
    x_3an_xp = x_or + xp_
    x_3an_xp, y_3an = int(x_3an_xp), int(y_3an)
    region3 = [x_3an_xp, y_3an, width, height]
    region3_pul = [x_3an_pul, y_3an, width, height]

    return region1_pul, region2_pul, region3_pul, region1, region2, region3


def get_task_area_big(width=77, height=42):
    """из my_screenshot"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423
    big = 100
    # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
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

    y_an = int(y_or + pos_1)

    # регион поиска 1 (позиция анализа)
    x_1an_pul = x_or + pul
    region1_big = [x_1an_pul, y_an, width + big, height]

    # регион поиска 2 (позиция анализа)
    x_2an_pul = x_or + pul
    region2_big = [x_2an_pul, y_an, width + big, height]

    # регион поиска 3 (позиция анализа)
    x_3an_pul = x_or + pul
    region3_big = [x_3an_pul, y_an, width + big, height]

    return region1_big, region2_big, region3_big

