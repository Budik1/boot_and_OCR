import pyautogui
from time import sleep, time
import datetime
import my_color_text as my_c_t

par_conf = 0.79
oblast = (51, 707, 92, 111)
log = 1


def locCenterImg(name_img, confidence=0.9):
    pos_img = pyautogui.locateCenterOnScreen(name_img, confidence=confidence)
    return pos_img


def my_print_to_file(text):
    if log == 1:
        date_time, date = time_now()
        file_name = date + ".txt"
        file = open('log/' + str(file_name), 'a+', encoding='utf-8')
        print(date_time, text, file=file)
        file.close()


def date_utc_now():
    now = datetime.datetime.utcnow()
    date_utc = (now.strftime('%Y-%m-%d'))
    return date_utc


def time_now():
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    date_time_now = (now.strftime('%Y-%m-%d %H:%M:%S'))
    date = (now.strftime('%Y-%m-%d'))
    return date_time_now, date


def minutes_now():
    now = datetime.datetime.now()
    minutes_now_ = (now.strftime('%M'))
    return minutes_now_


def date_and_time_in_name_file():
    now = datetime.datetime.now()
    date_time_now_f = (now.strftime('%Y-%m-%d %H-%M-%S'))
    return date_time_now_f


def close_popup_window():
    my_print_to_file('fun.close_popup_window')
    # print('def "fun.close_popup_window"')
    knob = locCenterImg('img/overall/knob.png',0.9)
    cancel = locCenterImg('img/overall/cancel.png', 0.9)
    if knob:
        move_to_click(knob, 1)
    if cancel:
        move_to_click(cancel, 1)


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


def station_gifts():
    """Обмен ежедневными подарками"""
    my_print_to_file('fun.station_gifts')
    pass
    gifts = locCenterImg('img/b_gifts.png', 0.91)
    pyautogui.moveTo(gifts, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(gifts)

    open_ = locCenterImg('img/b_gift_open.png', 0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(open_)
        sleep(1)
        thanks = locCenterImg('img/b_thanks.png', 0.9)
        pyautogui.moveTo(thanks, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(thanks)
        sleep(1)
        give = locCenterImg('img/b_give.png', 0.85)
        print(give)
        pyautogui.moveTo(give, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(give)

        open_ = locCenterImg('img/b_gift_open.png', 0.9)


def push_close():
    my_print_to_file('fun.push_close')
    kv_close = locCenterImg('img/kv/kv_close.png', par_conf)
    close = locCenterImg('img/overall/close.png', 0.9)
    if kv_close:
        move_to_click(kv_close, 0.1)
    else:
        move_to_click(close, 0.1)


def exit_to_zero_screen():
    my_print_to_file('fun.exit_to_zero_screen')
    push_close_all_()
    b_exit = locCenterImg('img/b_exit.png', 0.9)
    print(b_exit, 'b_exit')
    if b_exit:
        move_to_click(b_exit, 0.1)


def push_close_all_():
    my_print_to_file('fun.push_close_all_')
    close = locCenterImg('img/overall/close.png', 0.9)
    kv_close = locCenterImg('img/kv/kv_close.png', par_conf)
    while close or kv_close:
        close_popup_window()
        push_close()
        sleep(1)
        kv_close = locCenterImg('img/kv/kv_close.png', par_conf)
        close = locCenterImg('img/overall/close.png', 0.9)
        # print("цикл close")


def bonus():
    my_print_to_file('fun.bonus')
    # кнопка добавить
    add_bonus = locCenterImg('img/add.png', 0.8)
    pyautogui.moveTo(add_bonus, duration=1, tween=pyautogui.easeInOutQuad)
    sleep(1)
    pyautogui.click(add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = locCenterImg('img/take.png', 0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click()
        print('Бонус найден')
    else:
        print('Бонус не найден')
    # кнопка закрыть
    push_close_all_()


def start_p_m():
    my_print_to_file('fun.start_p_m')

    def spec_proposal():
        sz = 0
        proposal = locCenterImg('img/spec_proposal.png', 0.96)
        if proposal is not None:
            s_p_close = locCenterImg('img/overall/s_p_close.png', 0.96)
            while s_p_close is not None and sz <= 5:
                sleep(2)
                s_p_close = locCenterImg('img/overall/icon_in_desktop/s_p_close.png', 0.96)
                sz += 1
            pyautogui.click(s_p_close)

    def authorization():  # авторизация при необходимости
        sleep(2)
        pos_authorization = locCenterImg('img/overall/authorization_button.png', 0.8)
        if pos_authorization:
            pyautogui.moveTo(pos_authorization, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_authorization)
            sleep(2)

    def click_my_game():
        pos_my_game = locCenterImg('img/overall/my_game1.png', 0.8)
        pos_my_game1 = locCenterImg('img/overall/my_game2.png', 0.8)
        while pos_my_game is None and pos_my_game1 is None:
            sleep(0.5)
            pos_my_game = locCenterImg('img/overall/my_game1.png', 0.8)
            pos_my_game1 = locCenterImg('img/overall/my_game2.png', 0.8)
            print(pos_my_game, pos_my_game1, ' в ожидании появления кнопки "my_game"')
        if pos_my_game:
            pyautogui.moveTo(pos_my_game, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game)
            # print('pos_my_game ' + str(pos_my_game))
        elif pos_my_game1:
            pyautogui.moveTo(pos_my_game1, duration=1, tween=pyautogui.easeInOutQuad)
            pyautogui.click(pos_my_game1)
            # print('pos_my_game1' + str(pos_my_game1))
        else:
            print('Не найдено кнопки "My game"')
            im1 = pyautogui.screenshot('img/screen1.png')
            im1.save('img/screen1.png')
            sleep(2)
        pos_autor = locCenterImg('img/overall/authorization_button.png', 0.8)
        if pos_autor:
            authorization()

    def click_icon_game():
        p_i = 0
        # sleep(2)
        pos_icon_game = locCenterImg('img/overall/icon_game.png', 0.8)
        while pos_icon_game is None and p_i <= 100:
            p_i += 1
            sleep(1)
            pos_icon_game = locCenterImg('img/overall/icon_game.png', 0.8)
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
        slider = locCenterImg('img/overall/slider_v.png', 0.7)
        if slider:
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
    my_print_to_file('fun.move_friends_list_left')
    sleep(1)
    ar_right = locCenterImg('img/overall/b_arrow_right.png', 0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(1)
    return 1


def move_friends_list_right():
    """
    Смещает список друзей в право на одну позицию
    :return: 1
    """
    my_print_to_file('fun.move_friends_list_right')
    sleep(0.2)
    ar_right = locCenterImg('img/overall/b_arrow_left.png', 0.8)
    pyautogui.moveTo(ar_right, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(ar_right)
    sleep(0.2)
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    my_print_to_file('fun.move_friends_list_to_top')
    begin = locCenterImg('img/overall/b_begin.png', 0.96)
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
    my_print_to_file('fun.move_to_click')
    # print('move_to_click', pos_click)
    sleep(0.3)
    pyautogui.moveTo(pos_click, duration=1, tween=pyautogui.easeInOutQuad)
    # print('должен быть клик')
    sleep(z_p_k)
    pyautogui.click(pos_click)
    sleep(0.18)


def foto(path_name, _region):
    my_print_to_file('fun.foto')
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def find_link_hall_of_glory():
    """
    Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    my_print_to_file('fun.find_link_hall_of_glory')
    close = locCenterImg('img/overall/close.png', 0.9)
    while close:
        push_close_all_()
        close = locCenterImg('img/overall/close.png', 0.9)
    # получение координат привязки
    point_hall_of_glory = locCenterImg('img/arena/hall_of_glory_icon.png', 0.9)
    while not point_hall_of_glory:
        sleep(0.2)
        point_hall_of_glory = locCenterImg('img/arena/hall_of_glory_icon.png', 0.9)

    sleep(0.5)

    return point_hall_of_glory


def find_link_station_master():
    my_print_to_file('fun.find_link_station_master')
    station_master = locCenterImg('img/station_master.png', 0.9)
    pos_klan = locCenterImg('img/overall/klan.png', 0.9)
    if station_master or pos_klan:
        if pos_klan:
            pyautogui.moveTo(pos_klan)
            # получение координат привязки
            sleep(0.5)
            point = pos_klan

            vizit_to_station_master()
        else:
            pyautogui.moveTo(station_master)
            x_or, y_or = station_master
            x_or -= 29
            y_or -= 29
            point = x_or, y_or
    else:
        # Закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
        push_close_all_()
        pos_klan = locCenterImg('img/overall/klan.png', 0.9)
        pyautogui.moveTo(pos_klan)
        # получение координат привязки
        sleep(0.5)
        point = pos_klan
        vizit_to_station_master()

    return point


def get_areas_task_small(width=77, height=42):
    """Получение значений "region=" для поиска значений в малых регионах пуль и опыта
        :return: кортеж из шести списков значений"""
    my_print_to_file('fun.get_areas_task_small')
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


def get_areas_task_big_1(width=77, height=42):
    my_print_to_file('fun.get_areas_task_big_1')
    # width, height = 77, 42
    pul = 444
    pos_1 = 217
    big = 77  # 100

    x_or, y_or = find_link_station_master()

    x_an_pul = x_or + pul
    width += big
    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region_big_1 = [x_an_pul, y_1an, width, height]
    return region_big_1


def get_areas_task_big_2(width=77, height=42):
    my_print_to_file('fun.get_areas_task_big_2')
    # width, height = 77, 42
    pul = 444
    pos_2 = 320
    big = 77  # 100

    x_or, y_or = find_link_station_master()

    x_an_pul = x_or + pul  # начальная точка
    width += big  #
    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region_big_2 = [x_an_pul, y_2an, width, height]
    return region_big_2


def get_areas_task_big(width=77, height=42):
    """Получение значений "region=" для поиска заданий в больших регионах
        :return: кортеж из трех списков значений"""
    my_print_to_file('fun.get_areas_task_big')
    pul = 444
    pos_1, pos_2, pos_3 = 217, 320, 423
    big = 77  # 100

    x_or, y_or = find_link_station_master()

    x_an_pul = x_or + pul
    width += big

    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region1_big = [x_an_pul, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region2_big = [x_an_pul, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = int(y_or + pos_3)
    region3_big = [x_an_pul, y_3an, width, height]

    return region1_big, region2_big, region3_big


def find_link_klan():
    my_print_to_file('fun.find_link_klan')
    pos_klan = locCenterImg('img/overall/klan.png', 0.85)
    while not pos_klan:
        sleep(0.1)
        pos_klan = locCenterImg('img/overall/klan.png', 0.85)

    return pos_klan


def vizit_to_station_master():
    """заходит в палатку к нач станции"""
    my_print_to_file('fun.vizit_to_station_master')
    check = locCenterImg('img/station_master.png', 0.9)
    if check:
        pyautogui.moveTo(check, duration=1, tween=pyautogui.easeInOutQuad)
        # print(" уже у начальника ")
        sleep(1 / 3)
    else:
        pos_klan = locCenterImg('img/overall/klan.png', 0.85)
        while not pos_klan:
            sleep(0.1)
            pos_klan = locCenterImg('img/overall/b_arrow_right.png', 0.85)
            # print('в поиске клана', pos_klan)
        # print('клан = ', pos_klan)
        x1, y1 = pos_klan
        x1, y1 = x1 - 60, y1 + 300
        master = x1, y1
        move_to_click(master, 0.2)
        # print('зашел к начальнику')
        sleep(1)
        station_master = locCenterImg('img/station_master.png', par_conf)
        pyautogui.moveTo(station_master, duration=1, tween=pyautogui.easeInOutQuad)


def find_lvl():
    my_print_to_file('fun.find_lvl')
    pass


def await_arena(region):
    attack_arena_object = pyautogui.locateCenterOnScreen('img/arena/attack.png', confidence=0.9,
                                                         region=region)
    while attack_arena_object is None:
        attack_arena_object = pyautogui.locateCenterOnScreen('img/arena/attack.png', confidence=0.9,
                                                             region=region)
    pyautogui.moveTo(attack_arena_object)


def selection_hero():
    hero_gadya = locCenterImg('img/person/her_gadya.png')
    hero_gavr = locCenterImg('img/person/her_gavr.png')
    hero_veles = locCenterImg('img/person/her_veles.png')

    if hero_gadya:
        # print(my_c.tc_yellow('Гадя'))
        hero = 'Gady'
    elif hero_gavr:
        # print(my_c.tc_yellow('Гавр'))
        hero = 'Gavr'
    elif hero_veles:
        # print(my_c.tc_yellow('Велес'))
        hero = 'Велес'
    else:
        print(my_c_t.tc_red("Невозможно опознать героя (("))
        hero = None

    return hero