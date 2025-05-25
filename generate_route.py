import fun
import baza_dannyx as b_d
import my_color_text as mct


def extraction_name(variable):
    return variable[0]


def name_in_road_to_lists(variable: list):
    """ Получает список содержащий дорогу. Извлекает имена станций и помещает их в новый список. Возвращает список
    содержащий имена станций """
    list_name = []
    for name in variable:
        list_name.append(extraction_name(name))
        # Перебирая полученный список пишет названия станций.
        # print(extraction_name(name))
    # print(list_name)
    return list_name


def create_new_list_road_name():
    """Создаёт новый список содержащий только имена"""
    new_list_road_name = []
    for i in range(len(b_d.road_list)):
        # получаю списки содержащие дороги из списка дорог
        new_list_road_name.append(name_in_road_to_lists(b_d.road_list[i]))
    return new_list_road_name


def create_new_list_route(route_names: list):
    new_list_route = []
    for name in route_names:
        for i in range(len(b_d.list_of_stations)):
            if name in b_d.list_of_stations[i]:
                new_list_route += b_d.list_of_stations[i]
    return new_list_route


road_name_list = create_new_list_road_name()


def loc_now():
    list_location = ['станция не опознана']
    for i in range(len(b_d.list_of_stations)):
        img_station = b_d.list_of_stations[i][2]
        pos = fun.locCenterImg(name_img=img_station, confidence=0.9)
        if pos:
            list_location = b_d.list_of_stations[i]
    return list_location


def in_list(item: str):
    """
    Определяет принадлежность имени к списку

    param: item: имя
    return: список
    """
    print(type(item))
    path_list = ['путь неопознан']
    for i in range(len(road_name_list)):
        if item in road_name_list[i]:
            path_list = road_name_list[i]
    return path_list


def route_list(start: str, stop: str):
    """
    param: start: Имя станции
    param: stop: Имя станции
    return: список имен станций на маршруте
    """
    grand_road = road_name_list[0]
    road_start_point = in_list(start)
    road_stop_point = in_list(stop)

    # если старт и стоп в одном списке
    if road_start_point == road_stop_point:
        print('на одной дороге')
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

    print(f'идем из {start} в {stop}.')
    print(f'Полный путь {full_route_names}')
    print()
    print(create_new_list_route(full_route_names))
    return full_route_names


route_list('ст. Киевская_A', 'ст. Кропоткинская')
