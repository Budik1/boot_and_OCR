from time import sleep, time
from typing import Any

from pyscreeze import Point
from sympy.physics.units import speed

import fun
import heroes
import color_text
import sounds
import station_master
import baza_dannyx as b_d
import find_img as find
from heroes import Hero, Activ


def event_gifts():
    """
    Поиск подарков на станции. Возвращает его позицию
    """
    fun.my_print_to_file('touring.event_gifts')
    sleep(1)
    pos_gift = fun.locCenterImg(name_img='img/tonelli/gift.png', confidence=0.75)
    if not pos_gift:
        pos_gift_commune = fun.locCenterImg(name_img='img/tonelli/gift2.png', confidence=0.75)
        pos_gift = pos_gift_commune
    fun.my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        # x, y = pos_gift
        fun.Mouse.move(pos=pos_gift, speed=0.5)
        fun.Mouse.left_click(pos=pos_gift)
        sleep(1 * 2)
        close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
        # если тормозит отрисовка, ожидает появление кнопки "закрыть"
        it = 0
        while not close:
            it += 1
            sleep(1)
            close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
            print(it, 'поиск закрыть в подарках')
        # print(close)
        fun.Mouse.move(pos=close, speed=1)
        fun.Mouse.left_click(pos=close)
        sleep(1)

    return pos_gift


def open_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    fun.my_print_to_file('touring.open_map')
    location_station = fun.loc_now()
    # print(color_text.tc_cyan(f'выход из {location_station[0]}'))
    pos_run_out = [0, 0]
    if location_station[0] == 'ст. Тургеневская':
        pos_or1 = fun.find_link_klan()
        pos_run_out[0] = pos_or1[0] + 215
        pos_run_out[1] = pos_or1[1] + 205
        fun.Mouse.move(pos=pos_run_out, speed=0.1)
    else:
        pos_or1 = find.find_info()
        pos_run_out[0] = pos_or1[0] + 350
        pos_run_out[1] = pos_or1[1] + 180
        fun.Mouse.move(pos=pos_run_out, speed=0.1)
    fun.Mouse.left_click(pos=pos_run_out)
    # Убрать курсор с поля карты, чтобы ничего не перекрыл
    station_exit = fun.wait_static_pos(name_img='img/tonelli/station_exit.png')
    fun.Mouse.move(pos=station_exit, speed=0.1)
    return


def events_tunnel(name_st, st_id_file):
    """
    События в туннеле
    :param name_st: название станции из списка
    :param st_id_file: имя файла ID станции
    """
    fun.my_print_to_file('touring.events_tunnel')
    fun.selection_hero(show_name=False)

    dog_activ = True
    id_st = fun.locCenterImg(name_img=st_id_file)  # , confidence=0.85
    fun.my_print_to_file(f'id_st = {id_st}')
    info = fun.locCenterImg(name_img='img/overall/info.png', confidence=0.8)
    fun.my_print_to_file(f'info = {info}')
    while not id_st:
        x, y = info
        y += 350
        fun.Mouse.move(pos=(x, y))
        post = fun.locCenterImg(name_img='img/tonelli/post.png', confidence=0.8)
        skip_battle = find.find_skip_battle()
        fun.my_print_to_file(f'skip_battle = {skip_battle}')
        if skip_battle:
            station_master.enemy_battle(1, add_up=True, tour=True, dog_activ=dog_activ)  # вызов обработки события
        if post:
            fun.my_print_to_file(f'post = {post}')
            fun.Mouse.move(pos=post, speed=0.2)
            attack = find.find_tonelli_attack()
            entry = fun.locCenterImg(name_img='img/tonelli/entry_station.png', confidence=0.8)
            if entry:
                fun.my_print_to_file(f'entry = {entry}')
                fun.Mouse.move_to_click(pos_click=entry, move_time=0.2, z_p_k=0.1)
                # sleep(1)
            elif attack:
                dog_activ = False
                fun.my_print_to_file(f'attack = {attack}')
                fun.Mouse.move_to_click(pos_click=attack, move_time=0.2, z_p_k=0.1)
                # sleep(1)
        id_st = fun.locCenterImg(name_img=st_id_file)  # , confidence=0.85
        fun.my_print_to_file(f'id_st = {id_st}')
    fun.my_print_to_file(name_st)
    # поиск и подсчет количества подарков
    pos_gift = event_gifts()
    # указать на id станции
    fun.Mouse.move(pos=id_st, speed=0.2)
    fun.my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        Hero.app_gifts(Activ.hero_activ)
        print(name_st, ' подарков ', Hero.get_qty_gift(Activ.hero_activ))
    else:
        print(name_st)  # название станции
    return


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(search_object: str, param_confidence: float = 0.99) -> tuple[Point, float | Any]:
    """

    :param search_object: имя файла
    :param param_confidence:
    :return:
    """
    fun.my_print_to_file('touring.poisk')
    sleep(1)
    pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
    while pos_search is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
        # print(pos_search)
    return pos_search, param_confidence


def traffic_on_the_map(stan: list) -> None:
    """
    Движение по карте на соседнюю станцию.
    Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
    получает из него Point(x, y) поиска и параметр confidence,
    :param stan: (list):
    :return: None
    """
    fun.my_print_to_file('touring.traffic_on_the_map')
    open_map()
    # sleep(1 * 2)
    ev_map = stan[3]
    fun.my_print_to_file(f'ev_map = {ev_map}')
    next_station = fun.locCenterImg(name_img=stan[1], confidence=0.84)
    fun.my_print_to_file(f'pos_stan = {next_station}, stan[1] = {stan[1]}')
    if ev_map == 'стрелка север' and next_station is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_sever.png', confidence=0.85)
        fun.my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "север"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        # sleep(1)
    elif ev_map == 'стрелка юг' and next_station is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_yug.png', confidence=0.85)
        fun.my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "юг"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        # sleep(1)
    next_station = fun.locCenterImg(name_img=stan[1])
    confidence_poisk = 0.9
    if next_station:
        next_station = fun.wait_and_stop_img(name_img=stan[1])
    else:
        next_station, confidence_poisk = poisk(stan[1])
    fun.my_print_to_file(f'point_poisk = {next_station}, confidence_poisk = {confidence_poisk}')
    fun.Mouse.move_to_click(pos_click=next_station, move_time=0.2, z_p_k=0.3)
    events_tunnel(stan[0], stan[2])
    return


def travel(path_list: list) -> None:
    """
    Осуществляет движение по маршруту.
    :param path_list: (list): Список содержащий маршрут
    :return:
    """
    fun.my_print_to_file('touring.travel')
    for it in range(len(path_list)):
        k = it % len(path_list)

        traffic_on_the_map(path_list[k])
    return


def move_to_target(*, target_point, rapport=True):
    """
    :param rapport: сообщение о прибытии
    :param target_point: имя станции, например - 'ст. Чеховская'
    """
    # определяю героя
    her = fun.selection_hero()
    home_location = Hero.get_home_location(Activ.hero_activ)
    if home_location == 'бомж':
        print('Милок, не уходи со станции.. Память отшибет - заблудишься. Лучше документик сделай. '
              'Тебе тогда хоть подскажут.. ')
        return
    if not her:
        print(color_text.tc_yellow('Этот НИКТО никуда не пойдет)))'))
        return
    # получаю локацию старта
    start_point = fun.loc_now()[0]
    # print(f'{start_point=}')
    if start_point == 'станция не опознана':
        fun.push_close()
        start_point = fun.loc_now()[0]

    # если указано 'домой'
    if target_point == 'домой':
        target_point = Hero.get_home_location(Activ.hero_activ)
        mess = color_text.tc_cyan('своей палатке')
    else:
        mess = color_text.tc_cyan(target_point)
    print(f'Прокладываю маршрут к {mess}')


    # получаю маршрут
    if start_point != 'станция не опознана':
        route_list = create_route_list(start=start_point, stop=target_point)
    else:
        print(color_text.tc_red('no start_point'))
        return

    # движение по маршруту
    travel(path_list=route_list)
    if rapport:
        print(f'Пришел на {target_point}')
    return


def create_new_list_only_name(*, massive):
    """
    Из массива создаёт новый массив содержащий только имена
    :param massive: массив данных
    :return: Новый список только имена
    """
    new_list_road_name = []
    for i in range(len(massive)):
        # получаю списки содержащие дороги из списка дорог
        new_list_road_name.append(extraction_name_in_list(value=massive[i]))

    return new_list_road_name


def extraction_name_in_list(*, value: list) -> list:
    """ Получает список содержащий дорогу. Извлекает имена станций и помещает их в новый список. Возвращает список
    содержащий имена станций
    :param value:
    :return: """

    # def extraction_name(*, variable):
    #     return variable[0]

    list_name = []
    for name in value:
        # list_name.append(extraction_name(variable=name))
        list_name.append(name[0])
        # Перебирая полученный список пишет названия станций.
        # print(extraction_name(variable=name))
    return list_name


def create_route_list(*, start: str, stop: str) -> list:
    """
    :param start: Имя станции
    :param stop: Имя станции
    :return: готовый список содержащий полный маршрут
    """

    def create_new_list_route(*, route_names: list) -> list:
        """
        Преобразование листа из имен для нахождения маршрута в готовый лист маршрута
        :param route_names: лист маршрута из имен
        :return: Готовый list маршрута
        """
        new_list_route = []
        for name in route_names:
            for i in range(len(b_d.list_of_stations)):
                if name in b_d.list_of_stations[i]:
                    new_list_route.append(b_d.list_of_stations[i])
        return new_list_route

    grand_road = list_road_names[0]
    road_start_point = name_belonging_to_the_list(item=start)
    road_stop_point = name_belonging_to_the_list(item=stop)

    # если старт и стоп в одном списке
    if road_start_point == road_stop_point:
        # print('на одной дороге')
        path_list = road_start_point
        start_index = path_list.index(start)
        stop_index = path_list.index(stop)
        if start_index < stop_index:
            full_route_names = path_list[(start_index + 1):(stop_index + 1)]

        else:
            path_list.reverse()
            start_index = path_list.index(start)
            stop_index = path_list.index(stop)
            full_route_names = path_list[(start_index + 1):(stop_index + 1)]

    # если старт и стоп в разных списках
    else:
        # если старт и стоп в пересекающихся списках
        if set(road_start_point) & set(road_stop_point):
            crossroad = list(set(road_start_point) & set(road_stop_point))[0]
            index_point_start_road = road_start_point.index(start)
            index_crossroad_start_road = road_start_point.index(crossroad)
            index_point_stop_road = road_stop_point.index(stop)
            index_crossroad_stop_road = road_stop_point.index(crossroad)

            if index_point_start_road < index_crossroad_start_road:
                path1 = road_start_point[(index_point_start_road + 1):(index_crossroad_start_road + 1)]
            else:
                road_start_point.reverse()
                index_point_start_road = road_start_point.index(start)
                index_crossroad_start_road = road_start_point.index(crossroad)
                path1 = road_start_point[(index_point_start_road + 1):(index_crossroad_start_road + 1)]
            if index_point_stop_road > index_crossroad_stop_road:
                path2 = road_stop_point[(index_crossroad_stop_road + 1):(index_point_stop_road + 1)]
            else:
                road_stop_point.reverse()
                index_point_stop_road = road_stop_point.index(stop)
                index_crossroad_stop_road = road_stop_point.index(crossroad)
                path2 = road_stop_point[(index_crossroad_stop_road + 1):(index_point_stop_road + 1)]

            full_route_names = path1 + path2

        # если старт и стоп в непересекающихся списках
        else:
            # print('дорога имеет больше одного перекрестка')
            crossroad1 = list(set(road_start_point) & set(grand_road))[0]
            crossroad2 = list(set(road_stop_point) & set(grand_road))[0]
            index_point_start_road = road_start_point.index(start)
            index_crossroad1_grand_road = grand_road.index(crossroad1)
            index_point_stop_road = road_stop_point.index(stop)
            index_crossroad2_grand_road = grand_road.index(crossroad2)
            path1 = road_start_point[(index_point_start_road - 1):0:-1]

            if index_crossroad1_grand_road < index_crossroad2_grand_road:
                alley = grand_road[index_crossroad1_grand_road:(index_crossroad2_grand_road + 1)]
            else:
                alley = grand_road[index_crossroad1_grand_road:(index_crossroad2_grand_road - 1):-1]
            path2 = road_stop_point[1:index_point_stop_road + 1]

            full_route_names = path1 + alley + path2

    return create_new_list_route(route_names=full_route_names)


def name_belonging_to_the_list(*, item: str):
    """
    Определяет принадлежность имени к списку
    :param item: имя
    :return: список
    """
    # print(type(item))
    path_list = ['путь неопознан']
    for i in range(len(list_road_names)):
        if item in list_road_names[i]:
            path_list = list_road_names[i]
            break
    return path_list


list_road_names = create_new_list_only_name(massive=b_d.road_list)
list_names_all_station: list = extraction_name_in_list(value=b_d.list_of_stations)


def for_wilds():
    """
    Для Велеса:
        С домашней станции на Киевскую,
     задания на пули, потом на 'ст. Парк культуры(КР)' проверить есть ли доступное задание,
     задания на пули, потом на 'ст. Библиотека им. Ленина' проверить есть ли доступное задание,
     и домой, на крыс потратить остаток.
    Для всех остальных:
        С домашней станции на Киевскую,
     задания на пули, потом на Университет,
     на черных крыс потратить остаток,
     и домой на Фрунзенскую.
    """
    fun.my_print_to_file('touring.for_wilds')
    fun.push_close_all_()
    hero = fun.selection_hero(show_name=False)
    if hero == 'Велес':
        move_to_target(target_point='ст. Киевская')
        station_master.option_task_money(report_en=False)
        col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)
        print(f'нет доступных заданий. {col}')

        move_to_target(target_point='ст. Парк культуры(КР)')
        station_master.option_task_money(report_en=False)
        col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)

        print(f'нет доступных заданий. {col}')

        move_to_target(target_point='ст. Библиотека им. Ленина')
        station_master.option_task_money(report_en=False)
        col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)

        print(f'нет доступных заданий. {col}')

        move_to_target(target_point='домой')
        station_master.task_pos_item(1)
        print('энергия исчерпана')
    else:
        move_to_target(target_point='ст. Киевская')
        station_master.option_task_money()
        print('нет доступных заданий на Киевской')
        # univer()
        # за черными крысами на Универ
        move_to_target(target_point='ст. Университет')
        station_master.task_pos_item(1)
        print('энергия исчерпана')
        # univer_frunze()
        move_to_target(target_point='домой')
        sounds.say_txt('вернулся домой))')
        return


def for_kiki():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    fun.my_print_to_file('touring.for_kiki')

    start_time = time()
    fun.push_close_all_()

    # travel(b_d.frunze_kikimory)
    move_to_target(target_point='ст. Рижская')
    move_to_target(target_point='ст. Тургеневская')
    while heroes.Hero.get_qty_kiki(Activ.hero_activ) < 30:
        move_to_target(target_point='ст. Рижская')
        move_to_target(target_point='ст. Тургеневская')
    move_to_target(target_point='домой')
    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def sbor_podarkov(bypass_hero: list) -> None:
    """Обход всех станций. По статичному списку
    :param bypass_hero:
    :return: None
    """
    fun.my_print_to_file('touring.collecting_gifts_at_stations')
    for it in range(len(bypass_hero)):
        k = it % len(bypass_hero)
        traffic_on_the_map(bypass_hero[k])
    return
