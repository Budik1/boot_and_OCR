from time import sleep
import pyautogui


def move_to_click(pos_click: tuple, z_p_k: float):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """
    # print('move_to_click', pos_click)
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=0.1, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_click)
    sleep(0.18)


def push_close():
    pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    # print(pos_close)
    while pos_close is not None:
        # print(push_close)
        pyautogui.moveTo(pos_close, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_close)
        sleep(1)
        pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)


def my_print_list(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp):
    # print(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)
    print(list_1_pul[0], ' ', list_1_xp[0], ' ', list_2_pul[0], ' ', list_2_xp[0], ' ', list_3_pul[0], ' ',
          list_3_xp[0])
    print()
    # print(list_1_pul[0], ' / ', list_1_xp[0], ' => ',round(int(list_1_pul[0])/int(list_1_xp[0]),2))
    # print(list_2_pul[0], ' / ', list_2_xp[0], ' => ',round(int(list_2_pul[0])/int(list_2_xp[0]),2))
    # print(list_3_pul[0], ' / ', list_3_xp[0], ' => ',round(int(list_3_pul[0])/int(list_3_xp[0]),2))
    # print()
    # ##########
    # print(list_1_pul[0], ' / ', list_1_xp[0], ' => ',round(int(list_1_pul[0])/int(list_1_xp[0]),1))
    # print(list_2_pul[0], ' / ', list_2_xp[0], ' => ',round(int(list_2_pul[0])/int(list_2_xp[0]),1))
    # print(list_3_pul[0], ' / ', list_3_xp[0], ' => ',round(int(list_3_pul[0])/int(list_3_xp[0]),1))
    # print()
    # ##########
    print(list_1_pul[0], ' / ', list_1_xp[0], ' => ', round(int(list_1_pul[0]) / int(list_1_xp[0])))
    print(list_2_pul[0], ' / ', list_2_xp[0], ' => ', round(int(list_2_pul[0]) / int(list_2_xp[0])))
    print(list_3_pul[0], ' / ', list_3_xp[0], ' => ', round(int(list_3_pul[0]) / int(list_3_xp[0])))
