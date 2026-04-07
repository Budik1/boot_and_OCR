import pyautogui
import builtins
import inspect
from time import sleep, time

# from icecream import ic
# ic.configureOutput(includeContext=True)
# print = ic

import find_img
import fun_down
import heroes
import os_action
import tools
import baza
from baza import baza_dannyx as b_d
from baza import baza_paths as b_p
from baza import paths_img as p_i
from tools import color_text as c_t

par_conf = 0.79
oblast = (51, 707, 92, 111)


def screen_size():
    """
    Получение размеров экрана.
    :return: ширина, высота
    """
    log_with_caller(message='a')
    screen_width, screen_height = pyautogui.size()
    log_with_caller(message='e')
    return screen_width, screen_height


def locCenterImg(name_img, confidence=0.9, region: tuple[int, int, int, int] | None = None, grayscale=None):
    pos_img = fun_down.locateCenterImg(img=name_img,
                                       confidence=confidence,
                                       region=region,
                                       grayscale=grayscale)
    return pos_img


def wait_static_pos(*, name_img, region=None, confidence=0.99,
                    message=False, message_l=None):
    log_with_caller(message='a')
    log_with_caller(message=message_l)
    log_with_caller(message=name_img)
    pos = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    while not pos:
        pos = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    pos_img = locCenterImg(name_img=name_img, region=region, confidence=confidence)
    log_with_caller(message='e')
    return pos_img


def wait_and_stop_img(*, name_img, region: tuple[int, int, int, int] | None = None, confidence=0.9,
                      message=False, message_l=None):
    log_with_caller(message='a')
    log_with_caller(message=message_l)
    log_with_caller(message=name_img)
    if message:
        print(f'fun.wait_and_stop_img {message_l}')
    img_1 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    sleep(0.3)
    img_2 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    while not img_1 or img_1 != img_2:
        img_1 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
        sleep(0.3)
        img_2 = locCenterImg(name_img=name_img, confidence=confidence, region=region)
    log_with_caller(message='e')
    return img_1


def my_log_file(text):
    date_ = tools.date_now()
    time_ = tools.time_now()
    date_time = f'{date_} {time_}'
    path_file = b_p.log_path
    os_action.create_folder(path=path_file)
    file_name = date_ + ".txt"
    file_1 = open('txt/log/' + str(file_name), 'a+', encoding='utf-8')
    try:
        # print = print()
        builtins.print(date_time, text, file=file_1)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        builtins.print(f"Файл '{file_1}' не найден!")
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        builtins.print("Произошла ошибка ввода-вывода при чтении файла!")
    except Exception as e:
        # Обработка других неожиданных исключений
        builtins.print(f"Произошла неожиданная ошибка: {e}")
    finally:
        file_1.close()


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
    tools.Mouse.left_click(pos=gifts)
    open_ = locCenterImg('img/b_gift_open.png', 0.9)
    while open_:
        pyautogui.moveTo(open_, duration=1)
        tools.Mouse.left_click(pos=open_)
        sleep(1)
        thanks = locCenterImg('img/b_thanks.png', 0.9)
        pyautogui.moveTo(thanks, duration=1)
        tools.Mouse.left_click(pos=thanks)
        sleep(1)
        give = locCenterImg('img/b_give.png', 0.85)
        print(give)
        pyautogui.moveTo(give, duration=1)
        tools.Mouse.left_click(pos=give)

        open_ = locCenterImg('img/b_gift_open.png', 0.9)


def push_close_all_(speed_mouse=0.75):
    log_with_caller(message='a')
    pos_close = find_img.find_close()
    while pos_close:
        close_popup_window(speed_mouse)
        push_close(speed_mouse)
        pos_close = find_img.find_close()
    log_with_caller(message='e')


def close_popup_window(speed_mouse=0.75):
    log_with_caller(message='a')
    knob = find_img.find_knob()
    cancel = find_img.find_cancel()
    res = False
    if knob:
        tools.Mouse.move_to_click(pos_click=knob, speed=speed_mouse, z_p_k=1)
        res = True
    if cancel:
        tools.Mouse.move_to_click(pos_click=cancel, speed=speed_mouse, z_p_k=1)
        res = True
    log_with_caller(message='e')
    return res


def push_close(speed_mouse=0.75, event=''):
    log_with_caller(message='a')
    pos_close = find_img.find_close()
    if pos_close:
        event_mes = c_t.tc_cyan(f'{event}')
        log_with_caller(message=f'{event_mes} {pos_close=}')
        tools.Mouse.move_to_click(pos_click=pos_close, speed=speed_mouse, z_p_k=0.1, message=event)
        close_flag = True
    else:
        close_flag = False
    log_with_caller(message='e')
    return close_flag


def exit_to_zero_screen():
    log_with_caller(message='a')
    push_close_all_()
    b_exit = find_img.find_b_exit()
    log_with_caller(message=f'{b_exit=}')
    if b_exit:
        tools.Mouse.move_to_click(pos_click=b_exit, z_p_k=0.1)
    log_with_caller(message='e')


def bonus():
    log_with_caller(message='a')
    # кнопка добавить
    add_bonus = locCenterImg('img/add.png', 0.8)
    tools.Mouse.move(pos=add_bonus, speed=1)
    sleep(1)
    tools.Mouse.left_click(pos=add_bonus)
    sleep(2)
    # кнопка забрать
    take_bonus = locCenterImg('img/take.png', 0.9)
    if take_bonus:  # != None:
        pyautogui.moveTo(take_bonus, duration=1)
        tools.Mouse.left_click(pos=take_bonus)
        print('Бонус найден')
    else:
        print('Бонус не найден')
    # кнопка закрыть
    push_close_all_()
    log_with_caller(message='e')


def move_friends_list_left():
    """
    Смещает список друзей в лево на одну позицию
    :return: 1
    """
    log_with_caller(message='a')
    sleep(1)
    ar_right = locCenterImg('img/overall/b_arrow_right.png', 0.8)
    tools.Mouse.move(pos=ar_right, speed=1)
    tools.Mouse.left_click(pos=ar_right)
    sleep(1)
    log_with_caller(message='e')
    return 1


def move_friends_list_right():
    """
    Смещает список друзей в право на одну позицию
    :return: 1
    """
    log_with_caller(message='a')
    sleep(0.2)
    ar_right = locCenterImg('img/overall/b_arrow_left.png', 0.8)

    tools.Mouse.move(pos=ar_right, speed=1)
    tools.Mouse.left_click(pos=ar_right)
    sleep(0.2)
    log_with_caller(message='e')
    return 1


def move_friends_list_to_top():
    """Смещает список друзей в лево в начало"""
    log_with_caller(message='a')
    begin = locCenterImg('img/overall/b_begin.png', 0.96)
    if begin:  # если увидел
        tools.Mouse.move(pos=begin, speed=1)
        print(' перемотка в начало ')
        sleep(1)
        tools.Mouse.left_click(pos=begin)
        print('клик в начало ' + str(begin))
    sleep(1)
    log_with_caller(message='e')
    return


def foto(path_name, region: tuple[int, int, int, int] | object | None = None):
    """
        Создает снимок нужного участка экрана
        :param path_name: имя файла
        :param region: регион (X, Y, ширина, высота). None - весь экран
    """
    log_with_caller(message='a')
    im1 = pyautogui.screenshot(region=region)
    # Проверить наличие пути для создания файла!!!
    im1.save(path_name)
    log_with_caller(message='e')
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
    log_with_caller(message='a')
    # получает регион и корректировки снимка внутри него
    x_, y_, width_, height_ = region
    x_corrected = x_ + tune_x  # внесение изменений в параметр координаты "х"
    y_corrected = y_ + tune_y  # внесение изменений в параметр координаты "y"
    width_corrected = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_corrected = height_ - tune_v  # внесение изменений в параметр длинна "height"
    foto(name_img, (x_corrected, y_corrected, width_corrected, height_corrected))
    log_with_caller(message='e')


def find_link_hall_of_glory():
    """
    Закрыть если открыто, Tак как за чем-то может быть не видна позиция привязки
    :return: Point 'Зал славы'
    """
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return point_hall_of_glory


def find_link_station_master():
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return point


def find_link_station_master_alt():
    log_with_caller(message='a')
    station_master = find_img.find_station_master()
    pos_klan = find_img.find_klan()
    # Если нет ни того ни другого всё закрыть
    if not pos_klan and not station_master:
        my_log_file(f'ничего не видно')
        push_close_all_()
        pos_klan = wait_static_pos(name_img=p_i.klan_png)
    if pos_klan:
        point = vizit_to_station_master()
        my_log_file(f'{point=} если видно клан')
    else:
        point = find_img.find_station_master()
    log_with_caller(message=f'{point=}')
    log_with_caller(message='e')
    return point


def get_areas_task_small(width=77, height=42):
    """Получение значений "region=" для поиска значений в малых регионах пуль и опыта
        :return: кортеж из шести списков значений"""
    log_with_caller(message='a')
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

    log_with_caller(message='e')
    return region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp


def get_areas_task_big_1_line(width=77, height=42):
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return region_big_1


def get_areas_task_big_2_line(width=77, height=42):
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return region_big_2


def get_areas_task_big_3_line(width=77, height=42):
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return region_big_3


def get_areas_task_big(width=77, height=42):
    """Получение значений "region=" для поиска заданий в больших регионах
        :param width:
        :param height:
        :return: кортеж из трех списков значений"""
    log_with_caller(message='a')
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
    log_with_caller(message='e')
    return region1_big, region2_big, region3_big


def find_link_klan(show=True):
    log_with_caller(message='a')
    pos_klan = find_img.find_klan()
    while not pos_klan:
        print('no find_link_klan')
        pos_klan = find_img.find_klan()
        if pos_klan:
            tools.Mouse.move(pos=pos_klan, show=show)
    log_with_caller(message='e')
    return pos_klan


def is_open_station():
    """

    :return: Point station_master
    """
    log_with_caller(message='a')
    open_station1 = find_img.find_link_money_token()
    while not open_station1:
        open_station1 = find_img.find_link_money_token()
    log_with_caller(message='e')


def vizit_to_station_master():
    """заходит в палатку к нач.станции
    :return: Point 'station_master'
    """
    log_with_caller(message='a')
    is_open_station()
    station_master = find_img.find_station_master()
    if station_master:
        tools.Mouse.move(pos=station_master, speed=0.4)
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
        tools.Mouse.move_to_click(pos_click=master, speed=0.4, z_p_k=0.2)
        # print('зашел к начальнику')
        sleep(0.5)
        station_master = find_img.find_station_master()
        tools.Mouse.move(pos=station_master, speed=0.4)
    log_with_caller(message='e')
    return station_master



def await_arena(region):
    log_with_caller(message='a')
    attack_arena_object = find_img.find_choice_of_the_attacked(region=region)
    while attack_arena_object is None:
        attack_arena_object = find_img.find_choice_of_the_attacked(region=region)
    log_with_caller(message='e')
    return attack_arena_object


def selection_hero(*, show_name=True):
    log_with_caller(message='a')
    hero_gadya = find_img.find_her_gadya()
    hero_gavr = find_img.find_her_gavr()
    hero_mara = find_img.find_her_mara()
    hero = None
    if hero_gadya:
        if show_name:
            print(c_t.tc_yellow('Гадя'))
        hero = 'Gady'
        heroes.hero_activ_name = 'Gady'
        heroes.Activ.name_file_ = 'gady'
        heroes.Activ.hero_activ = heroes.gady
    elif hero_gavr:
        if show_name:
            print(c_t.tc_yellow('Гавр'))
        hero = 'Gavr'
        heroes.Activ.hero_activ_name = 'Gavr'
        heroes.Activ.name_file_ = 'gavr'
        heroes.Activ.hero_activ = heroes.gavr
    elif hero_mara:
        if show_name:
            print(c_t.tc_yellow('Мар`яна'))
        hero = 'Mara'
        heroes.Activ.hero_activ_name = 'Mara'
        heroes.Activ.name_file_ = 'mara'
        heroes.Activ.hero_activ = heroes.mara
    else:
        if show_name:
            print(c_t.tc_red("Невозможно опознать героя!! (("))
            print()

        heroes.Activ.hero_activ = None
    log_with_caller(message='e')
    return hero


def get_len_bypass(bypass_hero):
    log_with_caller(message='a')
    arr2 = []
    for i in bypass_hero:
        if i not in arr2:
            arr2.append(i)
    log_with_caller(message='e')
    return len(arr2)


def work():
    log_with_caller(message='a')

    rest = tools.get_rest_tim(h_max=22)

    vizit_to_station_master()
    pos_work = find_img.find_work()
    tools.Mouse.move_to_click(pos_click=pos_work)
    work_rest_hour = find_img.find_work_rest_hour(rest=rest)
    tools.Mouse.move_to_click(pos_click=work_rest_hour)
    log_with_caller(message='e')
    return


def verifi_img():
    path_img = input('Введи полное имя искомой картинки бес кавычек: ')
    pos = locCenterImg(name_img=path_img)
    if pos:
        tools.Mouse.move(pos=pos)
        print(c_t.tc_yellow(f'{path_img} - Найден )) все хорошо'))
    else:
        print(c_t.tc_red(f'{path_img} - Не найден  !!'))
    return


def extraction_digit(*, item):
    log_with_caller(message='a')
    """Извлекаю цифру из названия файла"""
    dig = int(''.join(c if c.isdigit() else ' ' for c in item))
    log_with_caller(message='e')
    return dig



def get_region_lines_task():
    """
        Получение региона для трех строк с заданием
    """
    log_with_caller(message='a')
    pos_start = find_link_station_master()

    line_height = int(90 * b_d.caliber_percent)  # высота строки задания
    line_length = int(280 * b_d.caliber_percent) # длина строки задания
    offset_from_starting_point_x = int(270 * b_d.caliber_percent)
    offset_from_starting_point_y = int(150 * b_d.caliber_percent)

    # найдем верхний угол
    x, y = pos_start
    x += offset_from_starting_point_x
    y_line_1 = y + offset_from_starting_point_y

    x_demo = x + line_length
    y_demo = y_line_1 + line_height

    region_task_line1 = x, y_line_1, line_length, line_height
    #

    y_line_2 = y + offset_from_starting_point_y + line_height

    x_demo = x + line_length
    y_demo = y_line_2 + line_height

    region_task_line2 = x, y_line_2, line_length, line_height
    #

    y_line_3 = y + offset_from_starting_point_y + (line_height * 2)

    x_demo = x + line_length
    y_demo = y_line_3 + line_height

    region_task_line3 = x, y_line_3, line_length, line_height
    log_with_caller(message='e')
    return region_task_line1, region_task_line2, region_task_line3


def loc_now():
    """
    Определяю имя станции нахождения
    :return: list станции
    """
    list_location = ['станция не опознана']
    for station in range(len(b_d.list_of_stations)):
        img_station = b_d.list_of_stations[station][2]
        # pos = locCenterImg(name_img=img_station, confidence=0.99)
        pos = find_img.find_img_param(path_name=img_station, confidence=0.99)
        if pos:
            list_location = b_d.list_of_stations[station]
            tools.Mouse.move(pos=pos, speed=0.1, )
            break
        else:
            pass
            # print(list_location)
    return list_location


def log_with_caller(message=None) -> str:
    """
    :param message: 'a'=активация and 'e'=выход. Если None - без сообщения
    :return: строка f"[{module_name}.{func_name}: line-{line_no}] {message}"
    """
    # Получение фрейма вызывающей функции
    current_frame = inspect.currentframe().f_back
    # Извлечение имени функции
    func_name = current_frame.f_code.co_name
    # Извлечение номера строки
    line_no = current_frame.f_lineno
    # Извлечение имени модуля
    module_name = inspect.getmodule(current_frame).__name__
    # Важно освободить ссылку на фрейм для избежания утечек памяти
    del current_frame
    # Форматирование сообщения с контекстом
    if message == 'a':
        context_message = f"[{module_name}.{func_name}: line-{line_no}] вызов"
    elif message == 'e':
        context_message = f"[{module_name}.{func_name}: line-{line_no}] выход"
    else:
        context_message = f"[{module_name}.{func_name}: line-{line_no}] {message}"
    my_log_file(context_message)
    if baza.variables.Parameters.def_rapport:
        print(tools.color_text.tc_green(context_message))
    return context_message


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
    dist_x = int(x_lower) - int(x_upper)
    dist_y = int(y_lower) - int(y_upper)
    return dist_x, dist_y
