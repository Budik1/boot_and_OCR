import pyautogui
import datetime
from time import sleep, time

# import fun
import sounds
import find_img
import fun_down
import baza_dannyx as b_d
import color_text

import heroes

par_conf = 0.79
oblast = (51, 707, 92, 111)


def screen_size():
    screen_width, screen_height = pyautogui.size()
    return screen_width, screen_height


def locCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None, grayscale=None):
    pos_img = fun_down.locateCenterImg(name_img=name_img,
                                       confidence=confidence,
                                       region=region,
                                       grayscale=grayscale)
    return pos_img


def wait_static_pos(*, name_img, region=None, confidence=0.99,
                    message=False, message_l=None):
    my_log_file('')
    my_log_file(f'fun.wait_static_pos {message_l}')
    my_log_file(f'{name_img=}')
    if message:
        print(f'fun.wait_static_pos {message_l=}')
    pos = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    while not pos:
        pos = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    pos_img = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    return pos_img


def wait_and_stop_img(*, name_img, region: tuple[int, int, int, int] | None = None, confidence=0.9,
                      message=False, message_l=None):
    my_log_file('')
    my_log_file(f'fun.wait_and_stop_img {message_l}')
    my_log_file(f'{name_img=}')
    if message:
        print(f'fun.wait_and_stop_img {message_l}')
    img_1 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    sleep(0.3)
    img_2 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    while not img_1 or img_1 != img_2:
        img_1 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
        sleep(0.3)
        img_2 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    return img_1


def mouse_left_click(*, pos, message=False):
    my_log_file('')
    my_log_file(f'fun.mouse_left_click {pos=}')
    if message:
        print(f'fun.mouse_left_click {message=} {pos=}')
    sounds.click_mouse()
    pyautogui.hotkey('Ctrl')
    pyautogui.click(pos)


class Mouse:

    @staticmethod
    def position_print():
        print()
        print('position()')
        print(pyautogui.position())

    @staticmethod
    def move(*, pos: tuple, speed=0.2, show=True, log=False, message_l=None):
        """

        :param pos:
        :param speed:
        :param show:
        :param log:
        :param message_l:
        :return:
        """
        my_log_file('')
        my_log_file(f'fun.Mouse.move {message_l}')
        my_log_file(f'{pos=}')
        if log:
            print(f'fun.Mouse.move {message_l=}')
        if show:
            pyautogui.moveTo(pos, duration=speed)
        return

    @staticmethod
    def left_click(*, pos, message=False, message_l=None):
        """

        :param pos:
        :param message:
        :param message_l:
        :return:
        """
        my_log_file('')
        my_log_file(f'fun.Mouse.left_click {message_l}')
        my_log_file(f' {pos=}')
        if message:
            print(f'fun.Mouse.left_click {message_l=}')
        sounds.click_mouse()
        pyautogui.hotkey('Ctrl')
        pyautogui.click(pos)
        return

    @staticmethod
    def take_drag_drop_y(*, pos_take, distance, speed=0.2, ):  # message=None, message_l=None
        """
        
        :param pos_take: 
        :param distance: 
        :param speed: 
        :return: 
        """
        pyautogui.mouseDown(pos_take)
        x, y = pos_take
        y += distance
        new_pos = x, y
        Mouse.move(pos=new_pos, speed=speed)
        pyautogui.mouseUp()
        return

    @staticmethod
    def take_drag_drop(*, pos_take: tuple, pos_drop: tuple, speed: float = 0.2, message=False, message_l=None) -> None:
        """

        :param pos_take:
        :param pos_drop: 
        :param speed: 
        :param message:
        :param message_l:
        :return:
        """
        my_log_file(f'fun.Mouse.take_drag_drop {message_l}')
        if message:
            print(f'fun.Mouse.take_drag_drop {message_l=}')
        pyautogui.mouseDown(pos_take)
        Mouse.move(pos=pos_drop, speed=speed)
        pyautogui.mouseUp()
        return

    @staticmethod
    def move_to_click(*, pos_click: tuple, move_time: float = 0.75, z_p_k: float = 0.05, log=False,
                      message_l=None) -> None:
        """
        Поместить указатель мыши по координатам и кликнуть, учитывая задержку.

        :param pos_click: Point
        :param move_time: время перемещения указателя мыши в секундах
        :param z_p_k: задержка перед кликом(float)
        :param log:
        :param message_l: цель клика
        :return: None
        """
        my_log_file(f'fun.Mouse.move_to_click {message_l=}, {pos_click=}')
        if log:
            print(f'fun.Mouse.move_to_click {message_l=}, {pos_click=}')
        sleep(0.3)
        Mouse.move(pos=pos_click, speed=move_time)
        # print('должен быть клик')
        sleep(z_p_k)
        Mouse.left_click(pos=pos_click)
        sleep(0.18)
        return


def my_log_file(text):
    date_ = date_now()
    time_ = time_now()
    date_time = f'{date_} {time_}'
    file_name = date_ + ".txt"
    file_1 = open('log/' + str(file_name), 'a+', encoding='utf-8')
    try:
        print(date_time, text, file=file_1)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        print(f"Файл '{file_1}' не найден!")
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        print("Произошла ошибка ввода-вывода при чтении файла!")
    except Exception as e:
        # Обработка других неожиданных исключений
        print(f"Произошла неожиданная ошибка: {e}")
    finally:
        file_1.close()


def date_utc_now():
    now = datetime.datetime.now(datetime.timezone.utc)
    date_utc = (now.strftime('%Y-%m-%d'))  # год-месяц-день
    return date_utc


def time_now():
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    time_now_ = (now.strftime('%H:%M:%S'))
    return time_now_


def date_time_now():
    """

    :return:
    """
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    date_time_now_ = (now.strftime('%Y-%m-%d %H:%M:%S'))
    date = (now.strftime('%Y-%m-%d'))
    return date_time_now_, date


def date_now():
    """
    Возвращает дату в формате Год-месяц-день
    :return: str
    """
    now = datetime.datetime.now()
    date = (now.strftime('%Y-%m-%d'))
    return date


def minutes_now():
    now = datetime.datetime.now()
    minutes_now_ = (now.strftime('%M'))
    return minutes_now_


def date_and_time_in_name_file():
    """
    '%Y-%m-%d %H-%M-%S'
    :return: str
    """
    now = datetime.datetime.now()
    date_time_now_f = (now.strftime('%Y-%m-%d %H-%M-%S'))
    return date_time_now_f


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
    my_log_file('fun.station_gifts')
    pass
    gifts = locCenterImg('img/b_gifts.png', 0.91)
    pyautogui.moveTo(gifts, duration=1)
    Mouse.left_click(pos=gifts)
    open_ = locCenterImg('img/b_gift_open.png', 0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1)
        Mouse.left_click(pos=open_)
        sleep(1)
        thanks = locCenterImg('img/b_thanks.png', 0.9)
        pyautogui.moveTo(thanks, duration=1)
        Mouse.left_click(pos=thanks)
        sleep(1)
        give = locCenterImg('img/b_give.png', 0.85)
        print(give)
        pyautogui.moveTo(give, duration=1)
        Mouse.left_click(pos=give)

        open_ = locCenterImg('img/b_gift_open.png', 0.9)


def push_close_all_(speed_mouse=0.75):
    my_log_file('fun.push_close_all_')
    pos_close = find_img.find_close()
    print(f'fun.push_close_all_ {pos_close=}')
    while pos_close:
        close_popup_window(speed_mouse)
        push_close(speed_mouse)
        # sleep(1)
        pos_close = find_img.find_close()
        print(f"fun.push_close_all_  цикл close {pos_close=}")


def close_popup_window(speed_mouse=0.75):
    my_log_file('fun.close_popup_window')
    knob = find_img.find_knob()
    cancel = find_img.find_cancel()
    res = False
    if knob:
        Mouse.move_to_click(pos_click=knob, move_time=speed_mouse, z_p_k=1)
        res = True
    if cancel:
        Mouse.move_to_click(pos_click=cancel, move_time=speed_mouse, z_p_k=1)
        res = True
    return res


def push_close(speed_mouse=0.75, event=''):
    my_log_file(f'')
    my_log_file('fun.push_close')
    pos_close = find_img.find_close()
    # print(f'fun.push_close {pos_close=}')
    if pos_close:
        event_mes = color_text.tc_cyan(f'{event}')
        my_log_file(f'')
        my_log_file(f'fun.push_close {event_mes} {pos_close=}')
        print(f'fun.push_close {event_mes} {pos_close=}')
        Mouse.move_to_click(pos_click=pos_close, move_time=speed_mouse, z_p_k=0.1, log=True, message_l=event)
        close_flag = True
    else:
        close_flag = False
    return close_flag


def exit_to_zero_screen():
    my_log_file('fun.exit_to_zero_screen')
    push_close_all_()
    b_exit = find_img.find_b_exit()
    print(b_exit, 'b_exit')
    if b_exit:
        Mouse.move_to_click(pos_click=b_exit, z_p_k=0.1)


def bonus():
    my_log_file('fun.bonus')
    # кнопка добавить
    add_bonus = locCenterImg('img/add.png', 0.8)
    Mouse.move(pos=add_bonus, speed=1)
    sleep(1)
    Mouse.left_click(pos=add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = locCenterImg('img/take.png', 0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1)
        Mouse.left_click(pos=take_bonus)
        print('Бонус найден')
    else:
        print('Бонус не найден')
    # кнопка закрыть
    push_close_all_()


def move_friends_list_left():
    """
    Смещает список друзей в лево на одну позицию
    :return: 1
    """
    my_log_file('fun.move_friends_list_left')
    sleep(1)
    ar_right = locCenterImg('img/overall/b_arrow_right.png', 0.8)
    Mouse.move(pos=ar_right, speed=1)
    Mouse.left_click(pos=ar_right)
    sleep(1)
    return 1


def move_friends_list_right():
    """
    Смещает список друзей в право на одну позицию
    :return: 1
    """
    my_log_file('fun.move_friends_list_right')
    sleep(0.2)
    ar_right = locCenterImg('img/overall/b_arrow_left.png', 0.8)

    Mouse.move(pos=ar_right, speed=1)
    Mouse.left_click(pos=ar_right)
    sleep(0.2)
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    my_log_file('fun.move_friends_list_to_top')
    begin = locCenterImg('img/overall/b_begin.png', 0.96)
    if begin:  # если увидел
        # pyautogui.moveTo(begin, duration=1)
        Mouse.move(pos=begin, speed=1)
        print(' перемотка в начало ')
        sleep(1)
        Mouse.left_click(pos=begin)
        print('клик в начало ' + str(begin))
    # pyautogui.moveTo(50, 600, duration=1)
    sleep(1)
    return


def foto(path_name, region: tuple[int, int, int, int] | object | None = None):
    """
        Создает снимок нужного участка экрана
        :param path_name: имя файла
        :param region: регион (X, Y, ширина, высота). None - весь экран
    """
    my_log_file('fun.foto')
    im1 = pyautogui.screenshot(region=region)
    im1.save(path_name)
    return


def foto_pos(name_img, region, tune_x=0, tune_y=0, tune_s=0, tune_v=0):
    """
    Получает имя файла, регион и корректирует (если надо) регион снимка.
    Дубль в event_arena.py
    :param region:
    :param tune_x:
    :param tune_y:
    :param tune_s:
    :param tune_v:
    :param name_img:
    :return:
    """
    # получает регион и корректировки снимка внутри него
    x_, y_, width_, height_ = region
    x_corrected = x_ + tune_x  # внесение изменений в параметр координаты "х"
    y_corrected = y_ + tune_y  # внесение изменений в параметр координаты "y"
    width_corrected = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_corrected = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_corrected, y_corrected, width_corrected, height_corrected))
    foto(name_img, (x_corrected, y_corrected, width_corrected, height_corrected))


def find_link_hall_of_glory():
    """
    Закрыть если открыто, Tак как за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    my_log_file('fun.find_link_hall_of_glory')
    close = find_img.find_close()
    while close:
        push_close_all_()
        close = find_img.find_close()
        print('поиск close')
    # получение координат привязки
    point_hall_of_glory = find_img.find_hall_of_glory_icon()
    while not point_hall_of_glory:
        sleep(0.2)
        point_hall_of_glory = find_img.find_hall_of_glory_icon()
    sleep(0.5)
    return point_hall_of_glory


def find_link_station_master():
    my_log_file('fun.find_link_station_master')
    station_master = find_img.find_station_master()
    pos_klan = find_img.find_klan()
    if station_master or pos_klan:
        if pos_klan:
            point = pos_klan
            vizit_to_station_master()
        else:
            x_or, y_or = station_master
            x_or -= 23
            y_or -= 27
            point = x_or, y_or
    else:
        # Закрыть если открыто, так как за чем-то может быть не видна позиция привязки
        push_close_all_()
        pos_klan = find_img.find_klan()
        sleep(0.5)
        point = pos_klan
        vizit_to_station_master()
    return point


def find_link_station_master_alt():
    my_log_file('')
    my_log_file('fun.find_link_station_master_alt')
    station_master = find_img.find_station_master()
    pos_klan = find_img.find_klan()
    # Если нет ни того ни другого всё закрыть
    if not pos_klan and not station_master:
        my_log_file(f'ничего не видно')
        push_close_all_()
        pos_klan = wait_static_pos(name_img='img/overall/klan.png')
    if pos_klan:
        point = vizit_to_station_master()
        my_log_file(f'{point=} если видно клан')
    else:
        point = find_img.find_station_master()
    my_log_file(f'{point=}')
    my_log_file('выход из fun.find_link_station_master_alt')
    return point


def get_areas_task_small(width=77, height=42):
    """Получение значений "region=" для поиска значений в малых регионах пуль и опыта
        :return: кортеж из шести списков значений"""
    my_log_file('fun.get_areas_task_small')
    pul, xp_ = 404 - 34 - 10 + 1, 518 - 40 - 34 - 10 - 10 + 2
    line_1, line_2, line_3 = 160, 250, 340

    x_or, y_or = find_link_station_master_alt()

    x_an_xp = x_or + xp_
    x_an_pul = x_or + pul

    # регион поиска 1 (позиция анализа)
    y_1an = y_or + line_1
    region1_pul = [x_an_pul, y_1an, width, height]
    region1_xp = [x_an_xp, y_1an, width, height]

    # регион поиска 2 (позиция анализа)
    y_2an = y_or + line_2
    region2_pul = [x_an_pul, y_2an, width, height]
    region2_xp = [x_an_xp, y_2an, width, height]

    # регион поиска 3 (позиция анализа)
    y_3an = y_or + line_3
    region3_pul = [x_an_pul, y_3an, width, height]
    region3_xp = [x_an_xp, y_3an, width, height]

    return region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp


def get_areas_task_big_1_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_1')
    # width, height = 77, 42
    pul = 404
    pos_1 = 190
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul
    width += big
    # регион поиска 1 (позиция анализа)
    y_1an = int(y_or + pos_1)
    region_big_1 = [x_an_pul, y_1an, width, height]
    return region_big_1


def get_areas_task_big_2_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_2')
    # width, height = 77, 42
    pul = 404
    pos_2 = 280
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul  # начальная точка
    width += big  #
    # регион поиска 2 (позиция анализа)
    y_2an = int(y_or + pos_2)
    region_big_2 = [x_an_pul, y_2an, width, height]
    return region_big_2


def get_areas_task_big_3_line(width=77, height=42):
    my_log_file('fun.get_areas_task_big_2')
    # width, height = 77, 42
    pul = 404
    pos_3 = 370
    big = 50  # 100

    x_or, y_or = find_link_station_master_alt()

    x_an_pul = x_or + pul  # начальная точка
    width += big  #
    # регион поиска 2 (позиция анализа)
    y_3an = int(y_or + pos_3)
    region_big_3 = [x_an_pul, y_3an, width, height]
    return region_big_3


def get_areas_task_big(width=77, height=42):
    """Получение значений "region=" для поиска заданий в больших регионах
        :param width:
        :param height:
        :return: кортеж из трех списков значений"""
    my_log_file('')
    my_log_file('fun.get_areas_task_big')
    # my_print_to_file('fun.get_areas_task_big')
    # print('')
    pul = 370
    # pos_1, pos_2, pos_3 = 217, 320, 423
    pos_1, pos_2, pos_3 = 160, 250, 340
    big = 56  # 56

    x_or, y_or = find_link_station_master_alt()
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


def find_link_klan(show=True):
    my_log_file('')
    my_log_file('fun.find_link_klan')
    pos_klan = find_img.find_klan()
    while not pos_klan:
        print('no')
        pos_klan = find_img.find_klan()
        if pos_klan:
            Mouse.move(pos=pos_klan, show=show)

    return pos_klan


def is_open_station():
    """

    :return: Point station_master
    """
    my_log_file('')
    my_log_file('fun.is_open_station')
    open_station1 = find_img.find_link_money_token()
    while not open_station1:
        open_station1 = find_img.find_link_money_token()


def vizit_to_station_master():
    """заходит в палатку к нач.станции
    :return: Point 'station_master'
    """
    my_log_file('')
    my_log_file('fun.vizit_to_station_master')
    # print('fun.vizit_to_station_master')
    is_open_station()
    station_master = find_img.find_station_master()
    if station_master:
        Mouse.move(pos=station_master, speed=0.4)
        # print(" уже у начальника ")
        sleep(1 / 3)
    else:
        pos_klan = find_link_klan()
        if not pos_klan:
            push_close_all_()
        pos_klan = find_link_klan()

        # print('клан = ', pos_klan)
        x1, y1 = pos_klan
        x1, y1 = x1 - 60, y1 + 300
        master = x1, y1
        Mouse.move_to_click(pos_click=master, move_time=0.4, z_p_k=0.2)
        # print('зашел к начальнику')
        sleep(0.5)
        station_master = find_img.find_station_master()
        Mouse.move(pos=station_master, speed=0.4)
    return station_master


def find_lvl():
    my_log_file('fun.find_lvl')
    pass


def await_arena(region):
    my_log_file('')
    my_log_file('fun.await_arena')
    attack_arena_object = find_img.find_choice_of_the_attacked(region=region)
    while attack_arena_object is None:
        attack_arena_object = find_img.find_choice_of_the_attacked(region=region)
    # mouse_move(pos=attack_arena_object)
    return attack_arena_object


def selection_hero(*, show_name=True):
    # print('fun.selection_hero')
    my_log_file('')
    my_log_file('fun.selection_hero')
    hero_gadya = find_img.find_her_gadya()
    hero_gavr = find_img.find_her_gavr()
    hero_veles = find_img.find_her_veles()
    hero_mara = find_img.find_her_mara()
    hero = None
    if hero_gadya:
        if show_name:
            print(color_text.tc_yellow('Гадя'))
        hero = 'Gady'
        heroes.hero_activ_name = 'Gady'
        heroes.Activ.name_file_ = 'gady'
        heroes.Activ.hero_activ = heroes.gady
    elif hero_gavr:
        if show_name:
            print(color_text.tc_yellow('Гавр'))
        hero = 'Gavr'
        heroes.Activ.hero_activ_name = 'Gavr'
        heroes.Activ.name_file_ = 'gavr'
        heroes.Activ.hero_activ = heroes.gavr
    elif hero_veles:
        pass
        # if show_name:
        #     print(myCt.tc_yellow('Велес'))
        # hero = 'Велес'
        # heroes.Activ.hero_activ_name = 'Велес'
        # heroes.Activ.name_file_ = 'veles'
        # heroes.Activ.hero_activ = heroes.veles
    elif hero_mara:
        if show_name:
            print(color_text.tc_yellow('Мар`яна'))
        hero = 'Mara'
        heroes.Activ.hero_activ_name = 'Mara'
        heroes.Activ.name_file_ = 'mara'
        heroes.Activ.hero_activ = heroes.mara
    else:
        if show_name:
            print(color_text.tc_red("Невозможно опознать героя!! (("))
            print()

        heroes.Activ.hero_activ = None
    return hero


def get_len_bypass(bypass_hero):
    my_log_file('')
    my_log_file('fun.get_len_bypass')
    arr2 = []
    for i in bypass_hero:
        if i not in arr2:
            arr2.append(i)
    return len(arr2)


def work():
    my_log_file('')
    my_log_file('fun.work')

    rest = get_rest_tim(h_max=22)

    vizit_to_station_master()
    pos_work = find_img.find_work()
    Mouse.move_to_click(pos_click=pos_work)
    work_rest_hour = find_img.find_work_rest_hour(rest=rest)
    Mouse.move_to_click(pos_click=work_rest_hour)
    return


def verifi_img():
    path_img = input('Введи полное имя искомой картинки бес кавычек: ')
    pos = locCenterImg(name_img=path_img)
    if pos:
        Mouse.move(pos=pos)
        print(color_text.tc_yellow(f'{path_img} - Найден )) все хорошо'))
    else:
        print(color_text.tc_red(f'{path_img} - Не найден  !!'))
    return


def extraction_digit(*, item):
    """Извлекаю цифру из названия файла"""
    dig = int(''.join(c if c.isdigit() else ' ' for c in item))
    return dig


def ac():
    pos_my = find_img.find_my_game2()
    while not pos_my:
        pos_my = find_img.find_my_game2()
    x, y = pos_my
    x -= 50
    y -= 50
    Mouse.move_to_click(pos_click=(x, y), move_time=0.3, z_p_k=0.2)


def get_areas_energy_1():
    x_or, y_or = find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + 548
    y = y_or + 182
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    return x, y, change_x, change_y


def get_areas_energy_2():
    x_or, y_or = find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + 548
    y = y_or + 285
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    return x, y, change_x, change_y


def get_areas_energy_3():
    x_or, y_or = find_link_station_master()
    # регион поиска 1 (позиция анализа)
    x = x_or + 548
    y = y_or + 388
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 17
    change_y = 23
    x_demo += change_x
    y_demo += change_y
    return x, y, change_x, change_y


def get_full_areal_tasks():
    """
    Получение региона заданий
    """
    pos_start = find_link_station_master()
    # найдем верхний угол
    x, y = pos_start
    x += 300
    y += 160
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 310
    change_y = 320
    x_demo += change_x
    y_demo += change_y
    return x, y, change_x, change_y


def get_region_lines_task():
    """
        Получение региона для трех строк с заданием
    """
    print('get_region_lines_task')
    pos_start = find_link_station_master()
    change_x = 280
    change_y = 90
    # найдем верхний угол
    x, y = pos_start
    x += 270
    y += 150

    x_demo, y_demo = x, y

    x_demo += change_x
    y_demo += change_y

    region_task_line1 = x, y, change_x, change_y
    #
    x, y = pos_start
    x += 270
    y += 150 + 90

    x_demo, y_demo = x, y
    x_demo += change_x
    y_demo += change_y

    region_task_line2 = x, y, change_x, change_y
    #
    x, y = pos_start
    x += 270
    y += 150 + 90 + 90
    x_demo, y_demo = x, y
    x_demo += change_x
    y_demo += change_y
    region_task_line3 = x, y, change_x, change_y
    return region_task_line1, region_task_line2, region_task_line3


def loc_now():
    """
    Определяю имя станции нахождения
    :return: list станции
    """
    list_location = ['станция не опознана']
    for station in range(len(b_d.list_of_stations)):
        img_station = b_d.list_of_stations[station][2]
        pos = locCenterImg(name_img=img_station, confidence=0.99)
        if pos:
            list_location = b_d.list_of_stations[station]
            Mouse.move(pos=pos, speed=0.1)
            # print(f'{b_d.list_of_stations[station][2]}') # img/tonelli/id_stations/s_Chekhov.png
            # print(f'имя станции старта - {list_location[0]}') # имя станции старта - ст. Чеховская
            break
        else:
            pass
            # print(list_location)
    return list_location


def dif_days(*, date_old, date_today=date_utc_now()):
    """
    Вычисляет разницу между двумя датами в днях.
    :param date_old: Прошедшая дата в формате "2025-11-29"
    :param date_today: Сегодняшняя дата в формате "2025-11-29"
    :return: Количество в днях
    """
    list_date_old = date_old.split(sep='-')
    list_date_today = date_today.split(sep='-')
    par_year = 0
    par_month = 1
    par_day = 2
    d_old = datetime.date(int(list_date_old[par_year]),
                          int(list_date_old[par_month]),
                          int(list_date_old[par_day]))
    d_today = datetime.date(int(list_date_today[par_year]),
                            int(list_date_today[par_month]),
                            int(list_date_today[par_day]))
    dif = d_today - d_old
    # print('fun.dif_days ', dif.days)
    return dif.days


def rap_explore(*, text, ex=''):
    """
    Рапорт использования.
    :param text: Имя используемой функции.
    :param ex:
    :return:
    """
    if ex:
        ex = 'выход'
    print(color_text.tc_green(f'{text} {ex}'))
    return


def get_rest_tim(*, h_max):
    t_now = time_now()
    h, m, s = t_now.split(':')
    t_work = 8
    rest_t = h_max - int(h)
    if rest_t > 8:
        t_work = 8
    elif 8 >= rest_t > 5:
        t_work = 5
    elif 5 >= rest_t > 2:
        t_work = 2
    elif 2 >= rest_t > 1:
        t_work = 1
    return t_work


def pos_parking():
    m_g = find_img.find_my_game2()
    x, y = m_g
    y += 40
    parking = x, y
    return parking


def distance(*, pos_upper: tuple, pos_lower: tuple) -> tuple[int, int]:
    """
    Возвращает расстояние между двумя точками по высоте и ширине
    :param pos_upper: верхняя точка
    :param pos_lower: нижняя точка
    :return: ширина и высота (width and height)
    """
    my_log_file(f'')
    my_log_file(f'kv_and_raid.distance')
    x_upper, y_upper = pos_upper
    x_lower, y_lower = pos_lower
    dist_x = x_lower - x_upper
    dist_y = y_lower - y_upper
    return dist_x, dist_y
