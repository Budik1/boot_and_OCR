from time import sleep, time

import fun
import my_color_text
import station_master
import baza_dannyx as b_d
import find_img as find
from heroes import Hero, Activ


def event_gifts():
    """Поиск подарков на станции. Возвращает его позицию"""
    fun.my_print_to_file('touring.event_gifts')
    sleep(1)
    pos_gift = fun.locCenterImg(name_img='img/tonelli/gift.png', confidence=0.75)
    if not pos_gift:
        pos_gift_komun = fun.locCenterImg(name_img='img/tonelli/gift2.png', confidence=0.75)
        pos_gift = pos_gift_komun
    fun.my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        x, y = pos_gift
        fun.mouse_move(pos=pos_gift, speed=0.5)
        fun.mouse_left_click(pos=pos_gift)
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
        fun.mouse_move(pos=close, speed=1)
        fun.mouse_left_click(pos=close)
        sleep(1)

    return pos_gift


def to_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    fun.my_print_to_file('touring.to_map')
    sleep(1)
    turgenev_st = fun.locCenterImg(name_img=b_d.st_turgenev[2], confidence=0.85)
    fun.my_print_to_file(f'turgenev_st = {turgenev_st}')
    pos_slip = [0, 0]
    if turgenev_st:
        pos_or1 = fun.find_link_klan()
        pos_slip[0] = pos_or1[0] + 205
        pos_slip[1] = pos_or1[1] + 205
        fun.mouse_move(pos=pos_slip)
    else:
        pos_or1 = find.find_info()
        pos_slip[0] = pos_or1[0] + 270 + 70
        pos_slip[1] = pos_or1[1] + 180
        #
        fun.mouse_move(pos=pos_slip)
    sleep(1)
    fun.mouse_left_click(pos=pos_slip)
    sleep(1)
    # Убрать курсор с поля карты, чтобы ничего не перекрыл
    station_exit = find.find_station_exit()
    fun.mouse_move(pos=station_exit)
    return


def events_tunnel(st0, st2):
    """
    События в туннеле
    :param st0: название станции из списка
    :param st2: имя файла ID станции
    """
    fun.my_print_to_file('touring.events_tunnel')
    fun.selection_hero(show_name=False)

    sleep(1)
    id_st = fun.locCenterImg(name_img=st2, confidence=0.85)
    fun.my_print_to_file(f'id_st = {id_st}')
    info = fun.locCenterImg(name_img='img/overall/info.png', confidence=0.8)
    fun.my_print_to_file(f'info = {info}')
    while not id_st:
        x, y = info
        y += 350
        fun.mouse_move(pos=(x, y))
        post = fun.locCenterImg(name_img='img/tonelli/post.png', confidence=0.8)
        skip_battle = find.find_skip_battle()
        fun.my_print_to_file(f'skip_battle = {skip_battle}')
        if skip_battle:
            station_master.enemy_battle(1, add_up=True)  # вызов обработки события
        if post:
            fun.my_print_to_file(f'post = {post}')
            fun.mouse_move(pos=post, speed=0.2)
            attack = find.find_tonelli_attack()
            entry = fun.locCenterImg(name_img='img/tonelli/entry_station.png', confidence=0.8)
            if entry:
                fun.my_print_to_file(f'entry = {entry}')
                fun.mouse_move_to_click(pos_click=entry, z_p_k=0.3)
                sleep(1)
            elif attack:
                fun.my_print_to_file(f'attack = {attack}')
                fun.mouse_move_to_click(pos_click=attack, z_p_k=0.3)
                sleep(1)
        id_st = fun.locCenterImg(st2, confidence=0.85)
        fun.my_print_to_file(f'id_st = {id_st}')
    print(st0)  # название станции
    fun.my_print_to_file(st0)
    fun.mouse_move(pos=id_st, speed=1)
    # вызов функции "event_gifts()" и подсчет количества найденных
    pos_gift = event_gifts()
    fun.my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        Hero.app_gifts(Activ.hero_activ)
        print(st0, ' подарков ', Hero.get_qty_gift(Activ.hero_activ))
    return


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(search_object, param_confidence=0.99):
    fun.my_print_to_file('touring.poisk')
    sleep(1)
    pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
    while pos_search is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
        # print(pos_search)
    return pos_search, param_confidence


def traffic_on_the_map(stan):
    """
    Движение по карте на соседнюю станцию.
    Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
    получает из него Point(x, y) поиска и параметр confidence,

    """
    fun.my_print_to_file('touring.traffic_on_the_map')
    to_map()
    sleep(1 * 2)
    ev_map = stan[3]
    fun.my_print_to_file(f'ev_map = {ev_map}')
    pos_stan = fun.locCenterImg(name_img=stan[1], confidence=0.84)
    fun.my_print_to_file(f'pos_stan = {pos_stan}, stan[1] = {stan[1]}')
    if ev_map == 'стрелка север' and pos_stan is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_sever.png', confidence=0.85)
        fun.my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "север"')
        fun.mouse_move_to_click(pos_click=pos_click, z_p_k=0.3)
        sleep(1)
    elif ev_map == 'стрелка юг' and pos_stan is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_yug.png', confidence=0.85)
        fun.my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "юг"')
        fun.mouse_move_to_click(pos_click=pos_click, z_p_k=0.3)
        sleep(1)
    point_poisk, confidence_poisk = poisk(stan[1])
    fun.my_print_to_file(f'point_poisk = {point_poisk}, confidence_poisk = {confidence_poisk}')
    fun.mouse_move_to_click(pos_click=point_poisk, z_p_k=0.3)
    events_tunnel(stan[0], stan[2])
    return


def travel(track: list):
    """
    Принимает список содержащий маршрут и осуществляет движение по нему
    :param track: list
    """
    fun.my_print_to_file('touring.travel')
    for it in range(len(track)):
        k = it % len(track)
        # print(k, track[k])

        traffic_on_the_map(track[k])
    return


def move_to_target(*, target_point):
    """
    :param target_point: имя станции, например - 'ст. Чеховская'
    """
    # определяю героя
    her = fun.selection_hero()
    if not her:
        print(my_color_text.tc_yellow('Этот НИКТО никуда не пойдет)))'))
        return
    # получаю локацию старта
    start_point = loc_now()[0]
    # print(f'{start_point=}, {type(start_point)}') # start_point='ст. Чеховская', <class 'str'>

    # если указано 'домой'
    if target_point == 'домой':
        target_point = Hero.get_home_location(Activ.hero_activ)

    # получаю маршрут
    # print(f'{target_point=}, {type(target_point)}')
    route_list = create_route_list(start=start_point, stop=target_point)

    # движение по маршруту
    travel(track=route_list)

    print(f'Пришел на {target_point}')
    return


def create_new_list_only_name(*, massive):
    """
    Из массива создаёт новый список содержащий только имена
    :param massive: массив данных
    :return: Новый список только имена
    """
    new_list_road_name = []
    for i in range(len(massive)):
        # получаю списки содержащие дороги из списка дорог
        new_list_road_name.append(name_in_list(value=massive[i]))
    return new_list_road_name


def name_in_list(*, value: list):
    """ Получает список содержащий дорогу. Извлекает имена станций и помещает их в новый список. Возвращает список
    содержащий имена станций """
    list_name = []
    for name in value:
        list_name.append(extraction_name(variable=name))
        # Перебирая полученный список пишет названия станций.
        # print(extraction_name(variable=name))
    return list_name


def extraction_name(*, variable):
    return variable[0]


def loc_now():
    """
    Определяю имя станции старта
    :return: list станции
    """
    list_location = ['станция не опознана']
    for i in range(len(b_d.list_of_stations)):
        img_station = b_d.list_of_stations[i][2]
        pos = fun.locCenterImg(name_img=img_station, confidence=0.99)
        if pos:
            list_location = b_d.list_of_stations[i]
            fun.mouse_move(pos=pos)
            # print(f'{b_d.list_of_stations[i][2]}') # img/tonelli/id_stations/s_Chekhov.png
            # print(f'имя станции старта - {list_location[0]}') # имя станции старта - ст. Чеховская
            break
    return list_location


def create_route_list(*, start: str, stop: str):
    """
    :param start: Имя станции
    :param stop: Имя станции
    :return: список, который содержит маршрут
    """
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


def create_new_list_route(*, route_names: list):
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
list_names_station = name_in_list(value=b_d.list_of_stations)


def tasks_na_kievskoy():
    """ С Фрунзенской на Киевскую,
     задания на пули, потом на Университет,
     на черных крыс потратить остаток,
     и домой на Фрунзенскую.
    """
    fun.my_print_to_file('touring.tasks_na_kievskoy')
    fun.push_close_all_()
    # frunze_kiev()
    move_to_target(target_point='ст. Киевская')
    station_master.choosing_task_money()
    print('задания на Киевской выполнены')
    # kiev_univer()
    # за черными крысами на Универ
    move_to_target(target_point='ст. Университет')
    station_master.task_pos_item(1)
    print('энергия исчерпана')
    # univer_frunze()
    move_to_target(target_point='домой')

def frunze_kiev():
    """Маршрут Фрунзенская - Киевская"""
    fun.my_print_to_file('touring.frunze_kiev')
    fun.push_close_all_()
    travel(b_d.frunze_kiev)
    print("пришел на Киевскую")


def univer_frunze():
    fun.my_print_to_file('touring.univer_frunze')

    fun.push_close_all_()
    travel(b_d.univer_frunze)
    print("пришел на Фрунзе")


def kiev_univer():
    fun.my_print_to_file('touring.kiev_univer')

    fun.push_close_all_()
    travel(b_d.kiev_univer)
    print("пришел на Универ")


def za_kikimorami():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    fun.my_print_to_file('touring.za_kikimorami')

    start_time = time()
    fun.push_close_all_()

    travel(b_d.frunze_kikimory)

    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def sbor_podarkov(bypass_hero):
    """Обход всех станций. При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    fun.my_print_to_file('touring.collecting_gifts_at_stations')
    for it in range(len(bypass_hero)):
        k = it % len(bypass_hero)
        traffic_on_the_map(bypass_hero[k])
