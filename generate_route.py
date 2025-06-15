import touring

print('import generate_route ))')

grand_road = [['a1', 'A1'], ['b1', 'B1'], ['c1', 'C1'], ['d1', 'D1'], ['e1', 'E1'], ['f1', 'F1'], ['g1', 'G1'],
              ['h1', 'H1'], ['i1', 'I1'], ['j1', 'J1'], ['k1', 'K1'], ['l1', 'L1'], ['m1', 'M1'], ['n1', 'N1'],
              ['o1', 'O1'], ['p1', 'P1'], ['q1', 'Q1'], ['r1', 'R1'], ['s1', 'S1'], ['t1', 'T1']]
park_kiev_a = [['e1', 'E1'], ['e2', 'E2'], ['e3', 'E3'], ['e4', 'E4']]
borov_polyanka = [['h1', 'H1'], ['h2', 'H2']]
chekhov_bulvar = [['i1', 'I1'], ['i2', 'I2']]
tver_most = [['j1', 'J1'], ['j2', 'J2'], ['j3', 'J3']]
novok_pavelec = [['l1', 'L1'], ['l2', 'L2'], ['l3', 'L3']]

road_list = (grand_road, park_kiev_a, borov_polyanka, chekhov_bulvar, tver_most, novok_pavelec)

def extraction_name(*, variable):
    return variable[0]

def name_in_list(*, value: list):
    """ Получает список содержащий дорогу. Извлекает имена станций и помещает их в новый список. Возвращает список
    содержащий имена станций """
    list_name = []
    for name in value:
        list_name.append(extraction_name(variable=name))
        # Перебирая полученный список пишет названия станций.
        # print(extraction_name(variable=name))
    # print()
    # print(f'[name_in_list] {value=}')
    # print(f'[name_in_list] {list_name=}')

    return list_name


def create_new_list_only_name(*, massive):
    """
    Из массива создаёт новый список содержащий только имена
    :param massive: массив данных
    :return: Новый список содержащий только имена
    """
    new_list_road_name = []
    for i in range(len(massive)):
        # получаю списки содержащие дороги из списка дорог
        # print(f'{massive[i]}')
        new_list_road_name.append(name_in_list(value=massive[i]))
    # print()
    # print(f'[create_new_list_only_name] {new_list_road_name=}')
    return new_list_road_name


def create_new_list_route(*, route_names: list):
    """
    Преобразование листа из имен для нахождения маршрута в готовый лист маршрута
    :param route_names: лист маршрута из имен
    :return: Готовый list маршрута
    """
    # new_list_route = []
    # for name in route_names:
    #     for i in range(len(b_d.list_of_stations)):
    #         if name in b_d.list_of_stations[i]:
    #             new_list_route.append(b_d.list_of_stations[i])
    # return new_list_route
    return route_names


def move_target(*, start_point, target_point):
    # определяю героя
    # her = fun.selection_hero()
    # if not her:
    #     print(my_color_text.tc_yellow('Никуда не пойдем)))'))
    #     return
    # получаю локацию старта
    # start_point = loc_now()[0]
    # print(f'{start_point=}, {type(start_point)}')

    # если указано 'домой'
    # if target_point == 'домой':
    #     target_point = Hero.get_home_location(Activ.hero_activ)

    # получаю маршрут
    # print(f'{target_point=}, {type(target_point)}')
    print(f'Для движения из {start_point} в {target_point}')
    route_list = generate_route_list(start=start_point, stop=target_point)

    # движение по маршруту
    # travel(track=route_list)
    print(f'{route_list=}')

    print(f'Пришел на {target_point}')
    return


def generate_route_list(*, start: str, stop: str):
    """

    :param start: Имя станции
    :param stop: Имя станции
    :return: список, который содержит маршрут
    """
    grand_road_ = list_road_names[0]
    # print()
    # print(f'{grand_road_=}')
    road_start_point = name_belonging_to_the_list(item=start)
    road_stop_point = name_belonging_to_the_list(item=stop)
    # print()
    # print(f'{road_start_point=}')
    # print(f'{road_stop_point=}')

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
            crossroad1 = list(set(road_start_point) & set(grand_road_))[0]
            crossroad2 = list(set(road_stop_point) & set(grand_road_))[0]
            index_point_start_road = road_start_point.index(start)
            index_crossroad1_grand_road = grand_road_.index(crossroad1)
            index_point_stop_road = road_stop_point.index(stop)
            index_crossroad2_grand_road = grand_road_.index(crossroad2)
            path1 = road_start_point[(index_point_start_road - 1):0:-1]

            if index_crossroad1_grand_road < index_crossroad2_grand_road:
                alley = grand_road_[index_crossroad1_grand_road:(index_crossroad2_grand_road + 1)]
            else:
                alley = grand_road_[index_crossroad1_grand_road:(index_crossroad2_grand_road - 1):-1]
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


list_road_names = create_new_list_only_name(massive=road_list)

move_target(start_point='e1',target_point='d1')