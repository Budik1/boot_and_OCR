from time import sleep, time

import fun
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
        fun.mouse_move(pos= pos_gift, speed=0.5)
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
        fun.mouse_move(pos= close, speed=1)
        fun.mouse_left_click(pos=close)
        sleep(1)

    return pos_gift


def to_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    fun.my_print_to_file('touring.to_map')
    sleep(1)
    turgenev_st = fun.locCenterImg(name_img=b_d.st_turgenev[2], confidence=0.85)
    fun.my_print_to_file(f'turgenev_st = {turgenev_st}')
    if turgenev_st:
        pos_or1 = fun.find_link_klan()
        x1, y1 = pos_or1
        x1, y1 = x1 + 205, y1 + 205
        pos_or1 = x1, y1
        fun.mouse_move(pos=pos_or1)
    else:
        pos_or1 = fun.find_link_klan()
        x1, y1 = pos_or1
        x1, y1 = x1 + 270, y1 + 180
        #
        pos_or1 = x1, y1
        fun.mouse_move(pos= pos_or1)
    sleep(1)
    fun.mouse_left_click(pos=pos_or1)
    sleep(1)
    # Убрать курсор с поля карты, чтобы ничего не перекрыл
    station_exit = find.find_station_exit()
    fun.mouse_move(pos=station_exit)


def events_tunnel(st0, st2):
    """
    События в туннеле
    :param st0: название станции из списка
    :param st2: имя файла ID станции
    """
    fun.my_print_to_file('touring.events_tunnel')
    display_element = '***'
    hero = fun.selection_hero()

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
        skip_battle = fun.locCenterImg(name_img='img/skip_battle.png', confidence=0.79)
        fun.my_print_to_file(f'skip_battle = {skip_battle}')
        if skip_battle:
            station_master.enemy_battle(1, add_up=True)  # вызов обработки события
        if post:
            fun.my_print_to_file(f'post = {post}')
            fun.mouse_move(pos= post, speed=0.2)
            attack = fun.locCenterImg(name_img='img/tonelli/attack.png', confidence=0.85)
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


# Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
# получает из него Point(x, y) поиска и параметр confidence,
def traffic_on_the_map(stan):
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


# получает список маршрута и осуществляет движение по нему
def travel(track: list):
    """
    Принимает список содержащий маршрут
    :param track: list
    """
    fun.my_print_to_file('touring.travel')
    for it in range(len(track)):
        k = it % len(track)
        # print(k, track[k])

        traffic_on_the_map(track[k])


def test_run():
    """
    Тест передвижения между станциями
    :return: количество встреченных крыс
    """
    hero = fun.selection_hero()
    if hero == 'Mara':
        fun.my_print_to_file('touring.test')
        fun.push_close_all_()
        travel(b_d.test_running_mara)
        print("тест успешно выполнен")
    else:
        fun.my_print_to_file('touring.test')
        fun.push_close_all_()
        travel(b_d.test_running3)
        print("тест успешно выполнен")


def tasks_na_kievskoy():
    """ С Фрунзенской на Киевскую,
     задания на пули, потом на Университет,
     на черных крыс потратить остаток,
     и домой на Фрунзенскую.
    """
    fun.my_print_to_file('touring.tasks_na_kievskoy')
    fun.push_close_all_()
    frunze_kiev()
    station_master.choosing_task_money()
    print('задания на Киевской выполнены')
    kiev_univer()
    station_master.task_pos_item(1)
    print('энергия исчерпана')
    univer_frunze()


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


# движение от st_park_kr до Кузнецкого моста
def most_riga():
    # движение от
    """Маршрут Кузнецкий мост - Киевская"""
    fun.my_print_to_file('touring.most_riga')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.most_riga)
    print("пришел на Рижскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def riga_most():
    """Маршрут Рижская - Кузнецкий мост"""
    fun.my_print_to_file('touring.riga_most')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.riga_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def bulvar_riga():
    # движение от
    """Маршрут Кузнецкий мост - Киевская"""
    fun.my_print_to_file('touring.most_riga')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.most_riga)
    print("пришел на Рижскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_bulvar():
    """Маршрут Рижская - Кузнецкий мост"""
    fun.my_print_to_file('touring.riga_most')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.frunze_bulvar)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def bulvar_frunze():
    """Маршрут Фрунзенская - Кузнецкий мост"""
    fun.my_print_to_file('touring.frunze_most')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.bulvar_frunze)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def most_frunze():
    """Маршрут Кузнецкий мост - Фрунзенская"""
    fun.my_print_to_file('touring.most_frunze')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.most_frunze)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def most_kiev():
    """Маршрут Кузнецкий мост - Киевская"""
    fun.my_print_to_file('touring.most_kiev')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.most_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def kiev_most():
    """Маршрут Киевская - Кузнецккий мост """
    fun.my_print_to_file('touring.kiev_frunze')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.kiev_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_kiev():
    """Маршрут Фрунзенская - Киевская"""
    fun.my_print_to_file('touring.frunze_kiev')
    fun.push_close_all_()
    travel(b_d.frunze_kiev)
    print("пришел на Киевскую")


def kiev_frunze():
    """Маршрут Киевская - Фрунзенская"""
    fun.my_print_to_file('touring.kiev_frunze')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.kiev_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_riga():
    """Маршрут Фрунзенская"""
    fun.my_print_to_file('touring.frunze_riga')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.frunze_riga)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def riga_frunze():
    """Маршрут  Фрунзенская"""
    fun.my_print_to_file('touring.riga_frunze')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.riga_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


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


def pauk_yascher():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    fun.my_print_to_file('touring.pauk_yascher')
    start_time = time()
    fun.push_close_all_()
    travel(b_d.pauk_yascher)
    print('на сегодня все пауки с ящерами зачищены')
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
