import fun

pul = 444
xp_ = 518

line1pos = 217
line2pos = 320
line3pos = 423

height = 42
width_smol = 77
width_big = 154




def get_areas_pul_line1():
    """
    Получение значения region для пуль первой линии
    """
    x_pos, y_pos = fun.find_link_station_master()
    x_an_pul = x_pos + pul
    # регион поиска 1 (позиция анализа)
    y_1an = y_pos + line1pos
    region1_pul = [x_an_pul, y_1an, width_smol, height]
    return region1_pul


def get_areas_pul_line2():
    """
    Получение значения region для пуль второй линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    # регион поиска 2 (позиция анализа)
    y_2an = y_or + line2pos
    region2_pul = [x_an_pul, y_2an, width_smol, height]
    return region2_pul


def get_areas_pul_line3():
    """
    Получение значения region для пуль третьей линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    # регион поиска 3 (позиция анализа)
    y_3an = y_or + line3pos
    region3_pul = [x_an_pul, y_3an, width_smol, height]
    return region3_pul


def get_areas_xp_line1():
    """
    Получение значения region для xp первой линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_xp = x_or + xp_
    y_1an = y_or + line1pos
    region1_xp = [x_an_xp, y_1an, width_smol, height]
    return region1_xp


def get_areas_xp_line2():
    """
    Получение значения region для xp второй линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_xp = x_or + xp_
    y_2an = y_or + line2pos
    region2_xp = [x_an_xp, y_2an, width_smol, height]
    return region2_xp


def get_areas_xp_line3():
    """
    Получение значения region для xp третьей линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_xp = x_or + xp_
    y_3an = y_or + line3pos
    region3_xp = [x_an_xp, y_3an, width_smol, height]
    return region3_xp


def get_areas_task_big_1():
    """
    Получение значения region для первой линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    y_1an = int(y_or + line1pos)
    region_big_1 = [x_an_pul, y_1an, width_big, height]
    return region_big_1


def get_areas_task_big_2():
    """
    Получение значения region для второй линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    y_2an = int(y_or + line2pos)
    region_big_2 = [x_an_pul, y_2an, width_big, height]
    return region_big_2


def get_areas_task_big_3():
    """
    Получение значения region для третьей линии
    """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    y_3an = int(y_or + line3pos)
    region_big_3 = [x_an_pul, y_3an, width_big, height]
    return region_big_3
