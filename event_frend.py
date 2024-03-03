import pyautogui
from station_master import enemy_battle
from time import sleep
from fun import move_to_click, move_friends_list_right, find_link_hall_of_glory, foto


def search_friend():
    """
    Анализ друга. Возвращает позицию активной кнопки 'Атаковать'
    :return: Point | None
    """
    pos_or = find_link_hall_of_glory()  # ориентир на зал славы
    x, y = pos_or
    x -= 160
    y += 650
    pos_friend = x, y
    x_r = x - 78
    y_r = y - 350
    friend_battle_region = x_r, y_r, 155, 295
    pyautogui.moveTo(pos_friend, duration=1)
    # Point(x=613, y=627), Point(x=748, y=660)
    move_to_click(pos_friend, 0.2)
    dom = pyautogui.locateCenterOnScreen('img/b_tent.png', region=friend_battle_region, confidence=0.9)
    while not dom:
        move_to_click(pos_friend, 0.2)
        dom = pyautogui.locateCenterOnScreen('img/b_tent.png', region=friend_battle_region, confidence=0.9)
    hero_vs_friend = pyautogui.locateCenterOnScreen("img/hero_vs_friend.png", region=friend_battle_region,
                                                    confidence=0.95)
    foto('img/kent.png', friend_battle_region)
    if hero_vs_friend:
        gangster = pyautogui.locateCenterOnScreen("img/f_gangster.png", region=friend_battle_region, confidence=0.95)
        ganza = pyautogui.locateCenterOnScreen("img/f_ganza.png", region=friend_battle_region, confidence=0.95)
        reich = pyautogui.locateCenterOnScreen("img/f_reich.png", region=friend_battle_region, confidence=0.95)
        red = pyautogui.locateCenterOnScreen("img/f_red.png", region=friend_battle_region, confidence=0.95)
        if gangster or ganza or reich or red:  #
            friend_battle = hero_vs_friend
        else:
            friend_battle = False
    else:
        friend_battle = False
    # print(friend_battle)
    return friend_battle


def friend_kill(required_quantity=29):  # требуемое количество=5
    quantity_battle = 0
    while quantity_battle <= required_quantity:
        friend_battle_ = search_friend()
        if friend_battle_:
            print('Атакую')
            quantity_battle += 1
            move_to_click(friend_battle_, 0.5)
            hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            while hero_vs_opponent is None:
                sleep(0.1)
                hero_vs_opponent = pyautogui.locateCenterOnScreen('img/hero_vs_opponent.png', confidence=0.9)
            move_to_click(hero_vs_opponent, 0.3)
            sleep(1)
            enemy_battle(0.5)
            print(quantity_battle, 'quantity_battle')
            move_friends_list_right()
        else:
            print('Следующий')
            move_friends_list_right()


friend_kill()
# search_friend()
