import pyautogui
from time import sleep, time
import datetime

sum_vip = 0
status_bonus = "0"
par_conf = 0.79
energy_availability = 1
number_tasks = 3
oblast = (51, 707, 92, 111)
img_sl = {'спецпредложение': 'img/spec_proposal.png', 'закрыть спецпредложение': 'img/s_p_close.png',
          'продолжить как Гаврил': 'img/authorization_button.png',
          'мои игры V1': 'img/my_game1.png', 'мои игры V2': 'img/my_game2.png',
          'иконка на рабочем столе': 'img/icon_in_desktop.png'}
iter_detect_search_region = 0  # ?????????


def close_popup_window():
    knob = pyautogui.locateCenterOnScreen('img/knob.png', confidence=0.9)
    cancel = pyautogui.locateCenterOnScreen('img/cancel.png', confidence=0.9)
    if knob:
        move_to_click(knob, 1)
    if cancel:
        move_to_click(cancel, 1)


def print_to_file(text: str) -> None:
    date_time, date = time_now()
    file_name = date_time + ".txt"
    file = open(file_name, 'a+', encoding='utf-8')
    print(date_time, text, file=file)
    file.close()  # закрыть файл после работы с ним.


def time_now():
    """Получение текущего времени и даты. Отдаёт формирование имени файла"""
    now = datetime.datetime.now()
    date_time_now = (now.strftime('%Y-%m-%d %H°%M\'\'%S\''))  # '%Y-%m-%d %H:%M:%S'
    date = (now.date())
    return date_time_now, date


def test_time(funk):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = funk(*args, *kwargs)
        finish_time = float(time() - start_time)  # общее количество секунд
        minutes = int(finish_time // 60)  # количество минут
        seconds = round((finish_time % minutes), 2)
        print(f'Потрачено время {minutes} минут {seconds} сек.')
        return res

    return wrapper()


def daily_gifts():
    """Обмен ежедневными подарками"""
    pass
    gifts = pyautogui.locateCenterOnScreen('img/b_gifts.png', confidence=0.91)
    pyautogui.moveTo(gifts, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(gifts)

    open_ = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(open_)
        sleep(1)
        thanks = pyautogui.locateCenterOnScreen('img/b_thanks.png', confidence=0.9)
        pyautogui.moveTo(thanks, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(thanks)
        sleep(1)
        give = pyautogui.locateCenterOnScreen('img/b_give.png', confidence=0.85)
        print(give)
        pyautogui.moveTo(give, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(give)

        open_ = pyautogui.locateCenterOnScreen('img/b_gift_open.png', confidence=0.9)


def push_close_all_():
    pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while pos_close:
        close_popup_window()
        pyautogui.moveTo(pos_close, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(pos_close)
        sleep(1)
        pos_close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)


def bonus():
    # кнопка добавить
    add_bonus = pyautogui.locateCenterOnScreen('img/add.png', confidence=0.8)
    pyautogui.moveTo(add_bonus, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)
    pyautogui.click(add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = pyautogui.locateCenterOnScreen('img/take.png', confidence=0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        print('Бонус найден')
    else:
        print('Бонус не найден')
    # кнопка закрыть
    push_close_all_()


def start_p_m():
    def spec_proposal():
        sz = 0
        proposal = pyautogui.locateCenterOnScreen('img/spec_proposal.png', confidence=0.96)
        if proposal is not None:
            s_p_close = pyautogui.locateCenterOnScreen('img/s_p_close.png', confidence=0.96)
            while s_p_close is not None and sz <= 5:
                sleep(2)
                s_p_close = pyautogui.locateCenterOnScreen('img/s_p_close.png', confidence=0.96)
                sz += 1
            pyautogui.click(s_p_close)

    def authorization():  # авторизация при необходимости
        sleep(2)
        pos_authorization = pyautogui.locateCenterOnScreen('img/authorization_button.png', confidence=0.8)
        if pos_authorization is not None:
            pyautogui.moveTo(pos_authorization, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_authorization)
            sleep(2)

    def click_my_game():
        pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
        pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
        while pos_my_game is None and pos_my_game1 is None:
            sleep(0.5)
            pos_my_game = pyautogui.locateCenterOnScreen('img/my_game1.png', confidence=0.8)
            pos_my_game1 = pyautogui.locateCenterOnScreen('img/my_game2.png', confidence=0.8)
            print(pos_my_game, pos_my_game1, ' в ожидании появления кнопки "my_game"')
        if pos_my_game is not None:
            pyautogui.moveTo(pos_my_game, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game)
            print('pos_my_game ' + str(pos_my_game))
        elif pos_my_game1 is not None:
            pyautogui.moveTo(pos_my_game1, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game1)
            print('pos_my_game1' + str(pos_my_game1))
        else:
            print('Не найдено кнопки "My game"')
            im1 = pyautogui.screenshot('img/screen1.png')
            im1.save('img/screen1.png')
            sleep(2)
        pos_autor = pyautogui.locateCenterOnScreen('img/authorization_button.png', confidence=0.8)
        if pos_autor is not None:
            authorization()

    def click_icon_game():
        p_i = 0
        # sleep(2)
        pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
        while pos_icon_game is None and p_i <= 100:
            p_i += 1
            sleep(1)
            pos_icon_game = pyautogui.locateCenterOnScreen('img/icon_game.png', confidence=0.8)
        pyautogui.click(pos_icon_game)
        sleep(1)

    def geography():
        # растягивание вверх
        pyautogui.moveTo(670, 86, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.dragTo(670, 1, duration=1)
        sleep(1)
        # растягивание вниз
        pyautogui.moveTo(670, 763, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.dragTo(670, 848, duration=1)
        # уменьшение масштаба
        pyautogui.hotkey('Ctrl', '-')
        pyautogui.hotkey('Ctrl', '-')
        # смещение окна в лево на 382
        pyautogui.moveTo(682, 11, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.dragTo(300, 11, duration=1)
        # смещение ползунка на 45
        slider = pyautogui.locateCenterOnScreen('img/slider_v.png', confidence=0.7)
        print(slider, 'ползунок')
        if slider is not None:
            x, y = slider
            pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.dragTo(x, y + 45, duration=1)

    authorization()
    click_my_game()
    click_icon_game()
    geography()
    spec_proposal()


def move_friends_list_left():
    """
    Смещает список друзей в лево на одну позицию
    :return: 1
    """
    sleep(1)
    ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_right.png', confidence=0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(1)
    return 1


def move_friends_list_right():
    """
    Смещает список друзей в право на одну позицию
    :return: 1
    """
    sleep(0.2)
    ar_right = pyautogui.locateCenterOnScreen('img/b_arrow_left.png', confidence=0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(0.2)
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    begin = pyautogui.locateCenterOnScreen('img/b_begin.png', confidence=0.96)
    if begin:  # если увидел
        pyautogui.moveTo(begin, duration=1, tween=pyautogui.easeInOutQuad)
        print(' перемотка в начало ')
        sleep(1)
        pyautogui.click(begin)
        print('клик в начало ' + str(begin))
    # pyautogui.moveTo(50, 600, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)


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


def find_link_hall_of_glory():
    """
    Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    push_close_all_()
    # получение координат привязки
    pos_or_v = pyautogui.locateCenterOnScreen('img/hall_of_glory_icon.png', confidence=0.9)
    sleep(0.5)
    return pos_or_v


def foto(path_name, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_station_master():
    station_master = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
    pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
    if station_master or pos_klan:
        print(pos_klan)  # Point(x=192, y=158)
        print(station_master)  # Point(x=221, y=187)
        if pos_klan:
            # pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
            pyautogui.moveTo(pos_klan)
            # получение координат привязки
            print(pos_klan)
            sleep(0.5)
            x_or, y_or = pos_klan
            vizit_to_station_master()
        else:
            pyautogui.moveTo(station_master)
            x_or, y_or = station_master
            x_or -= 29
            y_or -= 29
    else:
        # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
        push_close_all_()
        pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
        pyautogui.moveTo(pos_klan)
        # получение координат привязки
        print(pos_klan)
        sleep(0.5)
        x_or, y_or = pos_klan
        vizit_to_station_master()

    return x_or, y_or


def get_areas_task_small(width=77, height=42):
    """Получение значений "region=" для поиска значений в малых регионах
        :return: кортеж из шести списков значений"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423

    x_or, y_or = find_link_station_master()

    x_an_xp = x_or + xp_
    x_an_pul = x_or + pul

    # регион поиска 1 (позиция анализа)
    y_1an = y_or + pos_1
    region1_xp = [x_an_xp, y_1an, width, height]
    region1_pul = [x_an_pul, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = y_or + pos_2
    region2_xp = [x_an_xp, y_2an, width, height]
    region2_pul = [x_an_pul, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = y_or + pos_3
    region3_xp = [x_an_xp, y_3an, width, height]
    region3_pul = [x_an_pul, y_3an, width, height]

    return region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp


def get_areas_task_big(width=77, height=42):
    """Получение значений "region=" для поиска заданий в больших регионах
        :return: кортеж из трех списков значений"""
    pul, xp_ = 444, 518
    pos_1, pos_2, pos_3 = 217, 320, 423
    big = 100

    x_or, y_or = find_link_station_master()

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


def vizit_to_station_master():
    """заходит в палатку к нач станции"""
    # print('vizit_to_station_master')
    check = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=0.9)
    if check:
        pyautogui.moveTo(check, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(1 / 3)
    else:
        pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
        while not pos_klan:
            sleep(0.1)
            pos_klan = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
            # print('в поиске клана', pos_klan)
        # print('клан = ', pos_klan)
        x1, y1 = pos_klan
        x1, y1 = x1 - 60, y1 + 300
        pos_klan = x1, y1
        move_to_click(pos_klan, 0.2)
        # print('зашел к начальнику')
        sleep(1)
        na4 = pyautogui.locateCenterOnScreen('img/station_master.png', confidence=par_conf)
        pyautogui.moveTo(na4, duration=1, tween=pyautogui.easeInOutQuad)
