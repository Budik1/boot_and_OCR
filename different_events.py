import time
import pyautogui

import solid_memory
import fun


def start_p_m():
    fun.my_print_to_file('fun.start_p_m')

    def spec_proposal():
        sz = 0
        proposal = fun.locCenterImg('img/spec_proposal.png', 0.96)
        if proposal is not None:
            s_p_close = fun.locCenterImg('img/overall/s_p_close.png', 0.96)
            while s_p_close is not None and sz <= 5:
                time.sleep(2)
                s_p_close = fun.locCenterImg('img/overall/s_p_close.png', 0.96)
                sz += 1
            fun.mouse_left_click(pos=s_p_close)

    def authorization():  # авторизация при необходимости
        time.sleep(2)
        pos_authorization = fun.locCenterImg('img/overall/authorization_button.png', 0.8)
        if pos_authorization:
            pyautogui.moveTo(pos_authorization, duration=1)
            fun.mouse_left_click(pos=pos_authorization)
            time.sleep(2)

    def click_my_game():
        pos_my_game = fun.locCenterImg('img/overall/my_game1.png', 0.8)
        pos_my_game1 = fun.locCenterImg('img/overall/my_game2.png', 0.8)
        while pos_my_game is None and pos_my_game1 is None:
            time.sleep(0.5)
            pos_my_game = fun.locCenterImg('img/overall/my_game1.png', 0.8)
            pos_my_game1 = fun.locCenterImg('img/overall/my_game2.png', 0.8)
            print(pos_my_game, pos_my_game1, ' в ожидании появления кнопки "my_game"')
        if pos_my_game:
            pyautogui.moveTo(pos_my_game, duration=1)
            fun.mouse_left_click(pos=pos_my_game)
            # print('pos_my_game ' + str(pos_my_game))
        elif pos_my_game1:
            pyautogui.moveTo(pos_my_game1, duration=1)
            fun.mouse_left_click(pos=pos_my_game1)

    def click_icon_game():
        p_i = 0
        # sleep(2)
        pos_icon_game = fun.locCenterImg('img/overall/icon_game.png', 0.8)
        while pos_icon_game is None and p_i <= 100:
            p_i += 1
            time.sleep(1)
            pos_icon_game = fun.locCenterImg('img/overall/icon_game.png', 0.8)
        fun.mouse_left_click(pos=pos_icon_game)
        time.sleep(1)

    def geography():
        # уменьшение масштаба
        pyautogui.hotkey('Ctrl', '-')
        pyautogui.hotkey('Ctrl', '-')
        # растягивание вверх
        pyautogui.moveTo(670, 86, duration=1)
        pyautogui.dragTo(670, 1, duration=1)
        time.sleep(1)
        # растягивание вниз
        pyautogui.moveTo(670, 763, duration=1)
        pyautogui.dragTo(670, 848, duration=1)

        # смещение окна в лево на 382
        pyautogui.moveTo(682, 11, duration=1)
        pyautogui.dragTo(300, 11, duration=1)
        # смещение ползунка на 45
        slider = fun.locCenterImg('img/overall/slider_v.png', 0.7)
        if slider:
            x, y = slider
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.dragTo(x, y + 45, duration=1)

    # authorization()
    click_my_game()
    click_icon_game()
    geography()
    spec_proposal()
    fun.selection_hero()
    # solid_memory.save_to_file(info=False)