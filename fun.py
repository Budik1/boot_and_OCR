import pyautogui
from time import sleep, time
import datetime
from playsound3 import playsound

import my_color_text as myCt
import find_img
import heroes as her
import fun_down
from heroes import Activ

par_conf = 0.79
oblast = (51, 707, 92, 111)
log = 1


def locCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None):
    pos_img = fun_down.locateCenterImg(name_img=name_img,
                                       confidence=confidence,
                                       region=region)
    return pos_img


def mouse_left_click(*, pos):
    playsound('sound/mouse-click.wav')
    pyautogui.click(pos)
    pyautogui.hotkey('Ctrl')


def mouse_move_to_click(*, pos_click: tuple, move_time=0.75, z_p_k=0.05):
    """
    Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
    :param pos_click: Point
    :param move_time: время перемещения указателя мыши в секундах
    :param z_p_k: задержка перед кликом(float)
    :return: None
    """
    my_print_to_file('fun.mouse_move_to_click')
    # print('mouse_move_to_click', pos_click)
    sleep(0.3)
    mouse_move(pos=pos_click, speed=move_time)
    # print('должен быть клик')
    sleep(z_p_k)
    mouse_left_click(pos=pos_click)
    sleep(0.18)


def mouse_move(*, pos: tuple, speed=0.2, show=True):
    if show:
        pyautogui.moveTo(pos, duration=speed)

class Mouse:

    @staticmethod
    def position_print():
        # print('getInfo()')
        # print()
        # print(pyautogui.getInfo())
        print()
        print('position()')
        print(pyautogui.position())
        # pyautogui.position()

    @staticmethod
    def move(*, pos: tuple, speed=0.2, show=True):
        if show:
            pyautogui.moveTo(pos, duration=speed)
        return

    @staticmethod
    def left_click(*, pos):
        playsound('sound/mouse-click.wav')
        pyautogui.click(pos)
        pyautogui.hotkey('Ctrl')
        return

    @staticmethod
    def take_drag_drop_y(*, pos_take, dist, speed=0.2):
        pyautogui.mouseDown(pos_take)
        x, y = pos_take
        y += dist
        new_pos = x, y
        Mouse.move(pos=new_pos, speed=speed)
        pyautogui.mouseUp()
        return

    @staticmethod
    def take_drag_drop(*, pos_take, pos_drop, speed=0.2):
        pyautogui.mouseDown(pos_take)
        Mouse.move(pos=pos_drop, speed=speed)
        pyautogui.mouseUp()
        return

    @staticmethod
    def move_to_click(*, pos_click: tuple, move_time=0.75, z_p_k=0.05):
        """
        Поместить указатель мыши по координатам и кликнуть, учитывая задержку.
        :param pos_click: Point
        :param move_time: время перемещения указателя мыши в секундах
        :param z_p_k: задержка перед кликом(float)
        :return: None
        """
        my_print_to_file('fun.mouse_move_to_click')
        # print('mouse_move_to_click', pos_click)
        sleep(0.3)
        Mouse.move(pos=pos_click, speed=move_time)
        # print('должен быть клик')
        sleep(z_p_k)
        mouse_left_click(pos=pos_click)
        sleep(0.18)
        return


def my_print_to_file(text):
    if log == 1:
        date_time, date = time_now()
        file_name = date + ".txt"
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
    pyautogui.moveTo(gifts, duration=1)
    mouse_left_click(pos=gifts)
    open_ = locCenterImg('img/b_gift_open.png', 0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1)
        mouse_left_click(pos=open_)
        sleep(1)
        thanks = locCenterImg('img/b_thanks.png', 0.9)
        pyautogui.moveTo(thanks, duration=1)
        mouse_left_click(pos=thanks)
        sleep(1)
        give = locCenterImg('img/b_give.png', 0.85)
        print(give)
        pyautogui.moveTo(give, duration=1)
        mouse_left_click(pos=give)

        open_ = locCenterImg('img/b_gift_open.png', 0.9)


def push_close_all_():
    my_print_to_file('fun.push_close_all_')
    pos_close = find_img.find_close()
    while pos_close:
        close_popup_window()
        push_close()
        sleep(1)
        pos_close = find_img.find_close()
        # print("цикл close")


def close_popup_window():
    my_print_to_file('fun.close_popup_window')
    knob = find_img.find_knob()
    cancel = find_img.find_cancel()
    if knob:
        mouse_move_to_click(pos_click=knob, z_p_k=1)
    if cancel:
        mouse_move_to_click(pos_click=cancel, z_p_k=1)


def push_close():
    my_print_to_file('fun.push_close')
    pos_close = find_img.find_close()
    if pos_close:
        mouse_move_to_click(pos_click=pos_close, z_p_k=0.1)
        close_flag = True
    else:
        close_flag = False
    return close_flag


def exit_to_zero_screen():
    my_print_to_file('fun.exit_to_zero_screen')
    push_close_all_()
    b_exit = find_img.find_b_exit()
    print(b_exit, 'b_exit')
    if b_exit:
        mouse_move_to_click(pos_click=b_exit, z_p_k=0.1)


def bonus():
    my_print_to_file('fun.bonus')
    # кнопка добавить
    add_bonus = locCenterImg('img/add.png', 0.8)
    mouse_move(pos=add_bonus, speed=1)
    sleep(1)
    mouse_left_click(pos=add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = locCenterImg('img/take.png', 0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1)
        mouse_left_click(pos=take_bonus)
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
                s_p_close = locCenterImg('img/overall/s_p_close.png', 0.96)
                sz += 1
            mouse_left_click(pos=s_p_close)

    def authorization():  # авторизация при необходимости
        sleep(2)
        pos_authorization = locCenterImg('img/overall/authorization_button.png', 0.8)
        if pos_authorization:
            pyautogui.moveTo(pos_authorization, duration=1)
            mouse_left_click(pos=pos_authorization)
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
            pyautogui.moveTo(pos_my_game, duration=1)
            mouse_left_click(pos=pos_my_game)
            # print('pos_my_game ' + str(pos_my_game))
        elif pos_my_game1:
            pyautogui.moveTo(pos_my_game1, duration=1)
            mouse_left_click(pos=pos_my_game1)

    def click_icon_game():
        p_i = 0
        # sleep(2)
        pos_icon_game = locCenterImg('img/overall/icon_game.png', 0.8)
        while pos_icon_game is None and p_i <= 100:
            p_i += 1
            sleep(1)
            pos_icon_game = locCenterImg('img/overall/icon_game.png', 0.8)
        mouse_left_click(pos=pos_icon_game)
        sleep(1)

    def geography():
        # уменьшение масштаба
        pyautogui.hotkey('Ctrl', '-')
        pyautogui.hotkey('Ctrl', '-')
        # растягивание вверх
        pyautogui.moveTo(670, 86, duration=1)
        pyautogui.dragTo(670, 1, duration=1)
        sleep(1)
        # растягивание вниз
        pyautogui.moveTo(670, 763, duration=1)
        pyautogui.dragTo(670, 848, duration=1)

        # смещение окна в лево на 382
        pyautogui.moveTo(682, 11, duration=1)
        pyautogui.dragTo(300, 11, duration=1)
        # смещение ползунка на 45
        slider = locCenterImg('img/overall/slider_v.png', 0.7)
        if slider:
            x, y = slider
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.dragTo(x, y + 45, duration=1)

    # authorization()
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
    pyautogui.moveTo(ar_right, duration=1)
    mouse_left_click(pos=ar_right)
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
    pyautogui.moveTo(ar_right, duration=1)
    mouse_left_click(pos=ar_right)
    sleep(0.2)
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    my_print_to_file('fun.move_friends_list_to_top')
    begin = locCenterImg('img/overall/b_begin.png', 0.96)
    if begin:  # если увидел
        pyautogui.moveTo(begin, duration=1)
        print(' перемотка в начало ')
        sleep(1)
        mouse_left_click(pos=begin)
        print('клик в начало ' + str(begin))
    # pyautogui.moveTo(50, 600, duration=1)
    sleep(1)


def foto(path_name, region: tuple[int, int, int, int] | None = None):
    """
        Создает снимок нужного участка экрана
        :param path_name: имя файла
        :param region: регион (X, Y, ширина, высота). None - весь экран
    """
    my_print_to_file('fun.foto')
    im1 = pyautogui.screenshot(region=region)
    im1.save(path_name)


def find_link_hall_of_glory():
    """
    Закрыть если открыто, Tак как за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    my_print_to_file('fun.find_link_hall_of_glory')
    close = find_img.find_close()
    while close:
        push_close_all_()
        close = find_img.find_close()
    # получение координат привязки
    point_hall_of_glory = find_img.find_hall_of_glory_icon()
    while not point_hall_of_glory:
        sleep(0.2)
        point_hall_of_glory = find_img.find_hall_of_glory_icon()
    sleep(0.5)

    return point_hall_of_glory


def find_link_station_master():
    my_print_to_file('fun.find_link_station_master')
    station_master = find_img.find_station_master()
    pos_klan = find_img.find_klan()
    if station_master or pos_klan:
        if pos_klan:
            pyautogui.moveTo(pos_klan)
            mouse_move(pos=pos_klan)
            # получение координат привязки
            sleep(0.5)
            point = pos_klan

            vizit_to_station_master()
        else:
            mouse_move(pos=station_master)
            x_or, y_or = station_master
            x_or -= 29
            y_or -= 29
            point = x_or, y_or
    else:
        # Закрыть если открыто, так как за чем-то может быть не видна позиция привязки
        push_close_all_()
        pos_klan = find_img.find_klan()
        mouse_move(pos=pos_klan)
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
    pos_klan = find_img.find_klan()
    while not pos_klan:
        sleep(0.1)
        pos_klan = find_img.find_klan()

    return pos_klan


def vizit_to_station_master():
    """заходит в палатку к нач.станции"""
    my_print_to_file('fun.vizit_to_station_master')
    station_master = find_img.find_station_master()
    if station_master:
        mouse_move(pos=station_master, speed=0.4)
        # print(" уже у начальника ")
        sleep(1 / 3)
    else:
        pos_klan = find_link_klan()
        # print('клан = ', pos_klan)
        x1, y1 = pos_klan
        x1, y1 = x1 - 60, y1 + 300
        master = x1, y1
        mouse_move_to_click(pos_click=master, move_time=0.4, z_p_k=0.2)
        # print('зашел к начальнику')
        sleep(0.5)
        station_master = find_img.find_station_master()
        mouse_move(pos=station_master, speed=0.4)
    return station_master


def find_lvl():
    my_print_to_file('fun.find_lvl')
    pass


def await_arena(region):
    attack_arena_object = find_img.find_attack(region=region)
    while attack_arena_object is None:
        attack_arena_object = find_img.find_attack(region=region)
    mouse_move(pos=attack_arena_object)


def selection_hero(*, show_name=True):
    # print('fun.selection_hero')
    hero_gadya = find_img.find_her_gadya()
    hero_gavr = find_img.find_her_gavr()
    hero_veles = find_img.find_her_veles()
    hero_mara = find_img.find_her_mara()

    if hero_gadya:
        if show_name:
            print(myCt.tc_yellow('Гадя'))
        hero = 'Gady'
        Activ.hero_activ_name = 'Gady'
        Activ.hero_activ = her.gady
    elif hero_gavr:
        if show_name:
            print(myCt.tc_yellow('Гавр'))
        hero = 'Gavr'
        Activ.hero_activ_name = 'Gavr'
        Activ.hero_activ = her.gavr
    elif hero_veles:
        if show_name:
            print(myCt.tc_yellow('Велес'))
        hero = 'Велес'
        Activ.hero_activ_name = 'Велес'
        Activ.hero_activ = her.veles
    elif hero_mara:
        if show_name:
            print(myCt.tc_yellow('Мар`яна'))
        hero = 'Mara'
        Activ.hero_activ_name = 'Mara'
        Activ.hero_activ = her.mara
    else:
        print(myCt.tc_red("Невозможно опознать героя (("))
        hero = None
        Activ.hero_activ = None

    return hero


def get_len_bypass(bypass_hero):
    arr2 = []
    for i in bypass_hero:
        if i not in arr2:
            arr2.append(i)
    return len(arr2)


def work_8_hour():
    vizit_to_station_master()
    pos_work = find_img.find_work()
    mouse_move_to_click(pos_click=pos_work)
    work_8hour = find_img.find_work_8_hour()
    mouse_move_to_click(pos_click=work_8hour)


def transform_days(*, qty_days: int):
    days_des = qty_days % 10
    days_col = qty_days // 10

    if days_des == 1 and days_col != 1:
        return 'день'
    elif days_des in [2, 3, 4] and days_col != 1:
        return 'дня'
    elif days_col == 1:
        return 'дней'
    elif days_des in [0, 5, 6, 7, 8, 9] and days_col != 1:
        return 'дней'
    return 'дни'


def transform_wilds(*, qty_days: int):
    days_des = qty_days % 10
    days_col = qty_days // 10

    if days_des == 1 and days_col != 1:
        return 'дикарь'
    elif days_des in [2, 3, 4] and days_col != 1:
        return 'дикаря'
    elif days_col == 1:
        return 'дикарей'
    elif days_des in [0, 5, 6, 7, 8, 9] and days_col != 1:
        return 'дикарей'
    return 'дикари))'


def verifi_img():
    path_img = input('Введи полное имя искомой картинки бес кавычек: ')
    pos = locCenterImg(name_img=path_img)
    if pos:
        mouse_move(pos=pos)
        print(myCt.tc_yellow(f'{path_img} - Найден )) все хорошо'))
    else:
        print(myCt.tc_red(f'{path_img} - Не найден  !!'))


def extraction_digit(*, item):
    dig = int(''.join(c if c.isdigit() else ' ' for c in item))
    return dig

def ac():
    pos_my = find_img.find_my_game2()
    while not pos_my:
        pos_my = find_img.find_my_game2()
    x, y = pos_my
    x -= 50
    y -= 50
    mouse_move_to_click(pos_click=(x, y), move_time=0.3, z_p_k=0.2)

