import pyautogui
from station_master import enemy_battle
from time import sleep
import fun


def search_friend():
    """
    Анализ друга. Возвращает позицию активной кнопки 'Атаковать'
    :return: Point | None
    """
    # print('def "e_frend.search_friend"')
    pos_or = fun.find_link_hall_of_glory()  # ориентир на зал славы
    x, y = pos_or
    x -= 160
    y += 650
    pos_friend = x, y
    x_r = x - 78
    y_r = y - 350
    friend_battle_region = x_r, y_r, 155, 295
    pyautogui.moveTo(pos_friend, duration=1)
    fun.move_to_click(pos_friend, 0.2)
    dom = pyautogui.locateCenterOnScreen('img/tents_R/b_tent.png', region=friend_battle_region, confidence=0.9)
    while not dom:
        fun.move_to_click(pos_friend, 0.2)
        dom = pyautogui.locateCenterOnScreen('img/tents_R/b_tent.png', region=friend_battle_region, confidence=0.9)
    hero_vs_friend = pyautogui.locateCenterOnScreen("img/frends/hero_vs_friend.png", region=friend_battle_region,
                                                    confidence=0.95)  # 0.95 #  0.986
    # foto('img/kent.png', friend_battle_region)
    if hero_vs_friend:
        gangster = pyautogui.locateCenterOnScreen("img/frends/f_gangster.png", region=friend_battle_region, confidence=0.95)
        ganza = pyautogui.locateCenterOnScreen("img/frends/f_ganza.png", region=friend_battle_region, confidence=0.95)
        reich = pyautogui.locateCenterOnScreen("img/frends/f_reich.png", region=friend_battle_region, confidence=0.95)
        red = pyautogui.locateCenterOnScreen("img/frends/f_red.png", region=friend_battle_region, confidence=0.95)
        if  not gangster or not ganza or not reich or not red:  #
            friend_battle = hero_vs_friend
        else:
            friend_battle = False
    else:
        friend_battle = False
    # print(friend_battle)
    return friend_battle


def friend_kill(required_quantity=30):  # требуемое количество=5
    quantity_battle = 0
    while quantity_battle <= required_quantity:
        friend_battle_ = search_friend()
        if friend_battle_:
            print('Атакую')
            quantity_battle += 1
            fun.move_to_click(friend_battle_, 0.5)
            hero_vs_opponent = fun.locCenterImg('img/frends/hero_vs_opponent.png', 0.9)
            while hero_vs_opponent is None:
                sleep(0.1)
                hero_vs_opponent = fun.locCenterImg('img/frends/hero_vs_opponent.png', 0.9)
            fun.move_to_click(hero_vs_opponent, 0.3)
            sleep(1)
            enemy_battle(0.5)
            print(quantity_battle, 'quantity_battle')
            fun.move_friends_list_right()
        else:
            print('Следующий')
            fun.move_friends_list_right()


friend_kill()
# search_friend()
