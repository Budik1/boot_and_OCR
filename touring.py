
from time import sleep, time
from typing import Any

from pyscreeze import Point

from t import gift_station_service
import fun
import heroes
import solid_memory
import station_master
import tools
import find_img

from tools import color_text as c_t
from baza import baza_dannyx as b_d
from heroes import Hero, Activ


def translate(world):
    dikt_en_ru = {
        'Christmas_tree_star': 'новогодняя звезда',
        'Christmas_tree_garland': 'новогодняя гирлянда',
        'Christmas_tree_cracker': 'новогодняя хлопушка',
        'Christmas_tree_ball': 'новогодний шар',
        'Christmas_tree_branch': 'новогодняя ветка',

        'jetton': 'жетон',
        'bullets': 'пуль',
        'feed': 'корм',

        'sergeant': 'сержант',
        'lieutenant': 'лейтенант',
        'captain': 'капитан',
        'colonel': 'полковник',
        'general': 'генерал',

        'stamp_10_kopeck': 'марка 10 копеек',
        'stamp_30_kopeck': 'марка 30 копеек',
        'stamp_40_kopeck': 'марка 40 копеек',
        'stamp_50_kopeck': 'марка 50 копеек',
    }
    return dikt_en_ru.get(world, '')


def bypass_len():
    location_station = fun.loc_now()

    bypass_set_temp = heroes.Hero.get_bypass_set(heroes.Activ.hero_activ)
    # print(bypass_set_temp)
    if bypass_set_temp:
        bypass_temp = list(bypass_set_temp)
        # print(bypass_temp)
    else:
        bypass_temp = []
        # print(bypass_temp)

    bypass_temp.append(location_station[0])
    bypass = set(bypass_temp)
    # print(len(bypass))
    heroes.Hero.set_bypass_set(heroes.Activ.hero_activ, value_set=bypass)


def event_gifts():
    """
    Поиск подарков на станции. Возвращает его позицию
    """
    bypass_len()
    print(c_t.tc_green('touring.event_gifts'))
    fun.my_log_file(f'')
    fun.my_log_file('touring.event_gifts')
    sleep(1)
    pos_gift = fun.locCenterImg(name_img='img/tonelli/gift.png', confidence=0.75)
    if not pos_gift:
        pos_gift_commune = fun.locCenterImg(name_img='img/tonelli/gift2.png', confidence=0.75)
        pos_gift = pos_gift_commune
    fun.my_log_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        Hero.app_gifts(Activ.hero_activ)
        solid_memory.save_all_state_config_json(info=False)
        # print(name_st, ' подарков ' , Hero.get_qty_gift(Activ.hero_activ))
        # x, y = pos_gift
        fun.Mouse.move(pos=pos_gift, speed=0.5, log=True, message_l='подарок найден')
        fun.Mouse.left_click(pos=pos_gift, message=True, message_l=f'открыть подарок {pos_gift=}')
        # sleep(1 * 2)
        close = find_img.find_close()
        # если тормозит отрисовка, ожидает появление кнопки "закрыть"
        it = 0
        while not close:
            it += 1
            sleep(1)
            close = find_img.find_close()
            print(it, 'поиск закрыть в подарках')
        # print(close)
        # Создание имени
        name_file_date_time = tools.date_and_time_in_name_file()
        # name_crop_img = fun.date_time_now()
        name_her = Hero.get_name_id(Activ.hero_activ)
        # name_img = f'img/tonelli/loot_gift_box/big/{name_her}/{date_time}.png'
        name_img = f'img/tonelli/loot_gift_box/big/buf/{name_file_date_time}.png'
        # проверить наличие
        name_loot = gift_station_service.check_loot(name_hero_dir=name_her)
        if not name_loot:
            tools.sounds.say_txt('содержимое не опознано')
            gift_station_service.cr_box_loot_img(name_create_img=name_img)
            gift_station_service.tenderloin(name_fold=name_her, name_crop_img=name_file_date_time)
        elif name_loot.count('-') >= 3:
            pass
        elif len(name_loot) > 3:
            list_loot = heroes.Hero.get_loot_touring(heroes.Activ.hero_activ)
            list_loot.append(name_loot)
            heroes.Hero.set_loot_touring(heroes.Activ.hero_activ, value=list_loot)

            list_name = name_loot.split('_')
            if list_name[0].isnumeric():

                phrase = f'{list_name[0]} пуль'
            elif list_name[0] == 'cp':
                name_loot = list_name[2]
                phrase = translate(world=name_loot)
            else:
                phrase = translate(world=name_loot)
            tools.sounds.say_txt(str(phrase))

        # a_serial_scrin_for_pm.cr_other_img(name_create_img=name_img)
        fun.Mouse.move(pos=close, speed=1, log=True, message_l='нажал закрыть окно "подарок"')
        fun.Mouse.left_click(pos=close, message=True, message_l='нажал закрыть окно "подарок"')

        print(c_t.tc_green('touring.event_gifts выход'))
    return pos_gift


def open_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    print()
    print(c_t.tc_green('touring.open_map'))
    fun.my_log_file(f'')
    fun.my_log_file('touring.open_map')
    location_station = fun.loc_now()

    # bypass_set_temp = heroes.Hero.get_bypass_set(heroes.Activ.hero_activ)
    # print(bypass_set_temp)
    # if bypass_set_temp:
    #     bypass_temp = list(bypass_set_temp)
    #     print(bypass_temp)
    # else:
    #     bypass_temp = []
    #     print(bypass_temp)
    #
    # bypass_temp.append(location_station[0])
    # bypass = set(bypass_temp)
    # heroes.Hero.set_bypass_set(heroes.Activ.hero_activ, value_set=bypass)

    fun.my_log_file(f'выход из {location_station[0]}')
    # print(color_text.tc_cyan(f'выход из {location_station[0]}'))
    # получение координат
    if location_station[0] == 'ст. Тургеневская':
        pos_or1 = fun.find_link_klan()
        x = pos_or1[0] + 180
        y = pos_or1[1] + 205
        pos_run_out = x, y
        fun.Mouse.move(pos=pos_run_out, speed=0.1)
    else:
        pos_or1 = find_img.find_info()
        x = pos_or1[0] + 300
        y = pos_or1[1] + 180
        pos_run_out = x, y
        fun.Mouse.move(pos=pos_run_out, speed=0.1)
    # открыть карту
    fun.Mouse.left_click(pos=pos_run_out)
    # Убрать курсор с поля карты, чтобы ничего не перекрыл
    station_exit = fun.wait_static_pos(name_img='img/tonelli/station_exit.png')
    fun.Mouse.move(pos=station_exit, speed=0.1)
    print(c_t.tc_green('touring.open_map выход'))
    return


def events_tunnel(name_st, st_id_file):
    """
    События в туннеле
    :param name_st: название станции из списка
    :param st_id_file: имя файла ID станции
    """
    print()
    print(c_t.tc_green('touring.events_tunnel'))
    fun.my_log_file('touring.events_tunnel')
    fun.selection_hero(show_name=False)

    dog_activ = True
    id_st = fun.locCenterImg(name_img=st_id_file)  # , confidence=0.85
    info = fun.locCenterImg(name_img='img/overall/info.png', confidence=0.8)

    fun.my_log_file(f'{info=}, {id_st=}')
    parking = fun.pos_parking()
    fun.Mouse.move(pos=parking, log=True, message_l='убрать указатель с поля в ожидании событий')
    while not id_st:
        fun.close_popup_window()
        post = fun.locCenterImg(name_img='img/tonelli/post.png', confidence=0.8)
        skip_battle = find_img.find_skip_battle()
        fun.my_log_file(f'skip_battle = {skip_battle}')
        if skip_battle:
            station_master.enemy_battle(1, add_up=True, tour=True, dog_activ=dog_activ)  # вызов обработки события
            parking = fun.pos_parking()
            fun.Mouse.move(pos=parking, log=True, message_l='убрать указатель с поля в ожидании событий')
        if post:
            fun.my_log_file(f'post = {post}')
            fun.Mouse.move(pos=post, speed=0.2, log=True, message_l='Пост обнаружен')
            attack = find_img.find_tonelli_attack()
            entry = fun.locCenterImg(name_img='img/tonelli/entry_station.png', confidence=0.8)

            if entry:
                fun.my_log_file(f'entry = {entry}')
                fun.Mouse.move_to_click(pos_click=entry, move_time=0.2, z_p_k=0.1,
                                        log=True, message_l='войти на станцию')
                parking = fun.pos_parking()
                fun.Mouse.move(pos=parking, speed=0.5, show=True,
                               log=True, message_l='убрать указатель с поля, после входа на станцию')
                entry = fun.locCenterImg(name_img='img/tonelli/entry_station.png', confidence=0.8)
                while entry:
                    entry = fun.locCenterImg(name_img='img/tonelli/entry_station.png', confidence=0.8)
            else:
                if attack:
                    # dog_activ = False
                    fun.my_log_file(f'attack = {attack}')
                    fun.Mouse.move_to_click(pos_click=attack, move_time=0.2, z_p_k=0.1, log=True,
                                            message_l='атака поста')
                    parking = fun.pos_parking()
                    fun.Mouse.move(pos=parking, speed=0.5, show=True,
                                   log=True, message_l='убрать указатель с поля, после атаки поста')
                    attack = find_img.find_tonelli_attack()
                    while attack:
                        attack = find_img.find_tonelli_attack()

        id_st = fun.locCenterImg(name_img=st_id_file)  # , confidence=0.85
        fun.my_log_file(f'id_st = {id_st}')

    fun.my_log_file(name_st)
    # поиск и подсчет количества подарков
    pos_gift = event_gifts()
    # указать на id станции
    fun.Mouse.move(pos=id_st, speed=0.2)
    fun.my_log_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        # Hero.app_gifts(Activ.hero_activ)
        print(name_st, ' подарков ', Hero.get_qty_gift(Activ.hero_activ))
    else:
        print(name_st)  # название станции
    print()
    print(c_t.tc_green(f'touring.events_tunnel выход'))
    return


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(search_object: str, param_confidence: float = 0.99) -> tuple[Point, float | Any]:
    """

    :param search_object: имя файла
    :param param_confidence:
    :return:
    """
    print()
    print(c_t.tc_green('touring.poisk'))
    fun.my_log_file('touring.poisk')
    sleep(1)
    pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
    while pos_search is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_search = fun.locCenterImg(name_img=search_object, confidence=param_confidence)
        # print(pos_search)
    print()
    print(c_t.tc_green('touring.poisk выход'))
    return pos_search, param_confidence


def traffic_on_the_map(stan: list) -> None:
    """
    Движение по карте на соседнюю станцию.
    Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
    получает из него Point(x, y) поиска и параметр confidence,
    :param stan: (list):
    :return: None
    """
    print()
    print(c_t.tc_green('touring.traffic_on_the_map'))
    fun.my_log_file('touring.traffic_on_the_map')
    open_map()
    # sleep(1 * 2)
    ev_map = stan[3]
    fun.my_log_file(f'ev_map = {ev_map}')
    next_station = fun.locCenterImg(name_img=stan[1], confidence=0.84)
    fun.my_log_file(f'pos_stan = {next_station}, stan[1] = {stan[1]}')
    if ev_map == 'стрелка север' and next_station is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_sever.png', confidence=0.85)
        fun.my_log_file(f'pos_click = {pos_click}, нажал на стрелку "север"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_sever.png', confidence=0.85)
        fun.my_log_file(f'pos_click = {pos_click}, нажал на стрелку "север"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        # sleep(1)
    elif ev_map == 'стрелка юг' and next_station is None:
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_yug.png', confidence=0.85)
        fun.my_log_file(f'pos_click = {pos_click}, нажал на стрелку "юг"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        pos_click = fun.locCenterImg(name_img='img/tonelli/mark_yug.png', confidence=0.85)
        fun.my_log_file(f'pos_click = {pos_click}, нажал на стрелку "юг"')
        fun.Mouse.move_to_click(pos_click=pos_click, move_time=0.1, z_p_k=0.1)
        # sleep(1)
    next_station = fun.locCenterImg(name_img=stan[1])
    confidence_poisk = 0.9
    if next_station:
        next_station = fun.wait_and_stop_img(name_img=stan[1])
    else:
        next_station, confidence_poisk = poisk(stan[1])
    fun.my_log_file(f'point_poisk = {next_station}, confidence_poisk = {confidence_poisk}')
    fun.Mouse.move_to_click(pos_click=next_station, move_time=0.2, z_p_k=0.3)
    events_tunnel(stan[0], stan[2])
    print()
    print(c_t.tc_green('touring.traffic_on_the_map выход'))
    return


def travel(path_list: list) -> None:
    """
    Осуществляет движение по маршруту.
    :param path_list: (list): Список содержащий маршрут
    :return:
    """
    print()
    print(c_t.tc_green('touring.travel'))
    fun.my_log_file('touring.travel')
    for it in range(len(path_list)):
        k = it % len(path_list)

        traffic_on_the_map(path_list[k])
    print(c_t.tc_green('touring.travel выход'))
    return


def move_to_target(*, target_point, rapport=True):
    """
    :param rapport: сообщение о прибытии
    :param target_point: имя станции, например - 'ст. Чеховская'
    """
    print()
    print(c_t.tc_green('touring.move_to_target'))
    # определяю героя
    her = fun.selection_hero()  #
    # while not her:
    #     close = find_img.find_close()
    #     fun.Mouse.move_to_click(pos_click=close)
    #     her = fun.selection_hero()
    if not her:
        print(c_t.tc_yellow('Этот НИКТО никуда не пойдет)))'))
        return
    home_location = Hero.get_home_location(Activ.hero_activ)
    # print(home_location)
    if home_location == 'бомж':
        print('Милок, не уходи со станции.. Память отшибет - заблудишься. Лучше документик сделай. '
              'Тебе тогда хоть подскажут.. ')
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
        mess = c_t.tc_cyan('своей палатке')
    else:
        mess = c_t.tc_cyan(target_point)
    print(f'Прокладываю маршрут к {mess}')

    # получаю маршрут
    if start_point != 'станция не опознана':
        route_list = create_route_list(start=start_point, stop=target_point)
    else:
        print(c_t.tc_red('no start_point'))
        return

    # движение по маршруту
    travel(path_list=route_list)
    if rapport:
        print(f'Пришел на {target_point}')
    print(c_t.tc_green('touring.move_to_target выход'))
    return


def create_new_list_only_name(*, massive):
    """
    Из массива создаёт новый массив содержащий только имена
    :param massive: массив данных
    :return: Новый список только имена
    """
    fun.rap_explore(text='touring.create_new_list_only_name')
    new_list_road_name = []
    for i in range(len(massive)):
        # получаю списки содержащие дороги из списка дорог
        new_list_road_name.append(extraction_name_in_list(value=massive[i]))

    fun.rap_explore(text='touring.create_new_list_only_name', ex=1)
    return new_list_road_name


def extraction_name_in_list(*, value: list) -> list:
    """ Получает список содержащий дорогу. Извлекает имена станций и помещает их в новый список. Возвращает список
    содержащий имена станций
    :param value:
    :return: """
    # def_name = 'touring.extraction_name_in_list'
    # def_name = a
    # fun.rap_explore(text=def_name)
    list_name = []
    for name in value:
        # list_name.append(extraction_name(variable=name))
        list_name.append(name[0])
        # Перебирая полученный список пишет названия станций.
        # print(extraction_name(variable=name))
    # fun.rap_explore(text=def_name, ex=1)
    return list_name


def create_route_list(*, start: str, stop: str) -> list:
    """
    :param start: Имя станции
    :param stop: Имя станции
    :return: готовый список содержащий полный маршрут
    """
    def_name = 'touring.create_route_list'
    fun.rap_explore(text=def_name)

    # ========================================================================
    def create_new_list_route(*, route_names: list) -> list:
        """
        Преобразование листа из имен для нахождения маршрута в готовый лист маршрута
        :param route_names: лист маршрута из имен
        :return: Готовый list маршрута
        """
        sub_def_name = 'touring.create_route_list.create_new_list_route'
        fun.rap_explore(text=sub_def_name)
        new_list_route = []
        for name in route_names:
            for i in range(len(b_d.list_of_stations)):
                if name in b_d.list_of_stations[i]:
                    new_list_route.append(b_d.list_of_stations[i])
        fun.rap_explore(text=sub_def_name, ex=1)
        return new_list_route

    # ========================================================================
    grand_road = create_new_list_only_name(massive=b_d.road_list)[0]
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

    fun.rap_explore(text=def_name, ex=1)
    return create_new_list_route(route_names=full_route_names)


def name_belonging_to_the_list(*, item: str):
    """
    Определяет принадлежность имени к списку
    :param item: имя
    :return: список
    """
    def_name = 'touring.name_belonging_to_the_list'
    fun.rap_explore(text=def_name)
    # print(type(item))
    list_road_names = create_new_list_only_name(massive=b_d.road_list)

    path_list = ['путь неопознан']
    for i in range(len(list_road_names)):
        if item in list_road_names[i]:
            path_list = list_road_names[i]
            break
    fun.rap_explore(text=def_name, ex=1)
    return path_list


def for_wilds():
    """
    Для Велеса:
        С домашней станции на Киевскую,
     задания на пули, потом на 'ст. Парк культуры(КР)' проверить есть ли доступное задание,
     задания на пули, потом на 'ст. Библиотека им. Ленина' проверить есть ли доступное задание,
     и домой, на крыс потратить остаток.
    Для всех остальных:
        С домашней станции на Киевскую,
     задания на пули, потом на ст. Пушкинская,
     на белых крыс потратить остаток,
     и домой на Фрунзенскую.
    """
    def_name = 'touring.for_wilds'
    fun.rap_explore(text=def_name)

    fun.my_log_file('touring.for_wilds')
    fun.push_close_all_()
    hero = fun.selection_hero(show_name=False)
    if hero == 'Mara':
        move_to_target(target_point='ст. Киевская')
        station_master.option_task_money()
        col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)
        print(f'нет доступных заданий. {col}')
        if col in [30, 50]:
            print(f'энергия исчерпана {col} потрачено сегодня')
        else:
            move_to_target(target_point='ст. Парк культуры(КР)')
            station_master.option_task_money()
            col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)
            print(f'нет доступных заданий. {col}')
            if col in [30, 50]:
                print(f'энергия исчерпана {col} потрачено сегодня')
            else:
                # за белыми крысами на Пушкинской
                print(f'нет доступных заданий. {col}')
                move_to_target(target_point='ст. Пушкинская')
                station_master.task_pos_item(1)
                col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)
                print(f'энергия исчерпана {col} потрачено сегодня')
        move_to_target(target_point='домой')
    else:
        move_to_target(target_point='ст. Киевская')
        station_master.option_task_money()
        col = heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)
        if col in [30, 50]:
            print('энергия исчерпана')
            move_to_target(target_point='домой')
        else:
            # за белыми крысами на Пушкинской
            print(f'нет доступных заданий на Киевской, {col}')
            move_to_target(target_point='ст. Пушкинская')
            station_master.task_pos_item(1)
            print('энергия исчерпана')
            move_to_target(target_point='домой')
        tools.sounds.say_txt('вернулся домой))')
        fun.rap_explore(text=def_name, ex=1)
        return


def for_kiki():
    """Маршрут определяется автоматически"""
    def_name = 'touring.for_wilds'
    fun.rap_explore(text=def_name)
    fun.my_log_file('touring.for_kiki')
    start_time = time()
    fun.push_close_all_()
    while heroes.Hero.get_qty_kiki(Activ.hero_activ) < 30:
        move_to_target(target_point='ст. Рижская')
        move_to_target(target_point='ст. Тургеневская')
    move_to_target(target_point='домой')
    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')
    tools.sounds.say_txt('вернулся домой))')
    fun.rap_explore(text=def_name, ex=1)
    return


def sbor_podarkov(bypass_hero: list) -> None:
    """Обход всех станций. По статичному списку
    :param bypass_hero:
    :return: None
    """
    def_name = 'touring.sbor_podarkov'
    fun.rap_explore(text=def_name)
    pers = fun.selection_hero()
    if pers in ['Gady', 'Gavr']:
        move_to_target(target_point='ст. Пр-кт Вернадского')
        move_to_target(target_point='ст. Киевская(A)')
        move_to_target(target_point='ст. Полянка')
        move_to_target(target_point='ст. Цветной бульвар')
        move_to_target(target_point='ст. Кузнецкий мост')
        move_to_target(target_point='ст. Павелецкая(Г)')
        move_to_target(target_point='ст. ВДНХ')
        move_to_target(target_point='домой')
    if pers == 'Mara':
        move_to_target(target_point='ст. Полянка')
        move_to_target(target_point='ст. Цветной бульвар')
        move_to_target(target_point='ст. Кузнецкий мост')
        move_to_target(target_point='ст. Павелецкая(Г)')
        move_to_target(target_point='ст. Третьяковская')
        move_to_target(target_point='домой')
    tools.sounds.say_txt('вернулся домой))')
    fun.rap_explore(text=def_name, ex=1)
    return
