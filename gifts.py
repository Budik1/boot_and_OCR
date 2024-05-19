import pyautogui
from time import sleep
from fun import move_to_click, push_close_all_, exit_to_zero_screen

def open_loc_daily_gifts():
    link_gifts = pyautogui.locateCenterOnScreen('img/b_gifts.png', confidence=0.9)
    if not link_gifts:
        exit_to_zero_screen()
        link_gifts = pyautogui.locateCenterOnScreen('img/b_gifts.png', confidence=0.9)
        move_to_click(link_gifts, 0.1)
    move_to_click(link_gifts, 0.1)

def open_daily_gift():
    b_gift_open = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)
    while b_gift_open:
        move_to_click(b_gift_open, 0.2)
        b_thanks = pyautogui.locateCenterOnScreen('img/b_thanks.png', confidence=0.9)
        while not b_thanks:
            sleep(0.2)
            b_thanks = pyautogui.locateCenterOnScreen('img/b_thanks.png', confidence=0.9)
        move_to_click(b_thanks, 0.2)
        b_give = pyautogui.locateCenterOnScreen('img/b_give.png', confidence=0.9)
        while not b_give:
            sleep(0.2)
            b_give = pyautogui.locateCenterOnScreen('img/b_give.png', confidence=0.9)
        move_to_click(b_give, 0.2)
        b_gift_open = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)


open_loc_daily_gifts()
open_daily_gift()