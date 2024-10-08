import pyautogui
from time import sleep, time
from station_master import enemy_battle, vybor_zadaniya_na_puli, en_task_item
import baza_dannyx as b_d
from fun import push_close_all_, move_to_click, my_print_to_file

# son = 1
# station = 1
number_of_gifts = 0
kiki_q = 0
rat_q = 0
arachne_q = 0
raptor_q = 0


def event_gifts():
    """Поиск подарков на станции. Возвращает его позицию"""
    my_print_to_file('touring.event_gifts')
    sleep(1)
    pos_gift = pyautogui.locateCenterOnScreen('img/tonelli/gift.png', confidence=0.75)
    my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        x, y = pos_gift
        pyautogui.moveTo(x, y, duration=0.5, tween=pyautogui.easeInOutQuad)
        pyautogui.click(x, y)
        sleep(1 * 2)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        # если тормозит отрисовка, ожидает появление кнопки "закрыть"
        it = 0
        while not close:
            it += 1
            sleep(1)
            close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
            print(it, 'поиск закрыть в подарках')
        # print(close)
        pyautogui.moveTo(close, duration=1, tween=pyautogui.easeInOutQuad)
        pyautogui.click(close)
        sleep(1)
    return pos_gift


def to_map():
    """Из окна станции открывает карту. На Тургеневской выход смещен"""
    my_print_to_file('touring.to_map')
    sleep(1)
    turgenev_st = pyautogui.locateCenterOnScreen(b_d.st_turgenev[2], confidence=0.85)
    my_print_to_file(f'turgenev_st = {turgenev_st}')
    if turgenev_st:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
        x1, y1 = pos_or1
        x1, y1 = x1 + 205, y1 + 205
        pos_or1 = x1, y1
        pyautogui.moveTo(pos_or1, duration=0.2)
    else:
        pos_or1 = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.85)
        x1, y1 = pos_or1
        x1, y1 = x1 + 270, y1 + 180
        #
        pos_or1 = x1, y1
        pyautogui.moveTo(pos_or1, duration=0.2)
    sleep(1)
    pyautogui.click(pos_or1)
    sleep(1)
    # Убрать курсор с поля карты, чтобы ничего не перекрыл
    station_exit = pyautogui.locateCenterOnScreen('img/tonelli/station_exit.png', confidence=0.8)
    pyautogui.moveTo(station_exit, duration=0.2)


def events_tunnel(st0, st2):
    """
    События в туннеле
    :param st0: название станции из списка
    :param st2: имя файла ID станции
    """
    my_print_to_file('touring.events_tunnel')
    global number_of_gifts, kiki_q, rat_q, raptor_q, arachne_q

    sleep(1)
    id_st = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
    my_print_to_file(f'id_st = {id_st}')
    info = pyautogui.locateCenterOnScreen('img/info.png', confidence=0.8)
    my_print_to_file(f'info = {info}')
    while not id_st:
        x, y = info
        y += 350
        pyautogui.moveTo(x, y)
        post = pyautogui.locateCenterOnScreen('img/tonelli/post.png', confidence=0.8)
        skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=0.79)
        my_print_to_file(f'skip_battle = {skip_battle}')
        if skip_battle:
            raptor = pyautogui.locateCenterOnScreen('img/tonelli/raptor.png', confidence=0.85)
            my_print_to_file(f'raptor = {raptor}')
            arachne = pyautogui.locateCenterOnScreen('img/tonelli/arachne.png', confidence=0.85)
            my_print_to_file(f'arachne = {arachne}')
            krysa = pyautogui.locateCenterOnScreen('img/tonelli/krysa.png', confidence=0.85)
            my_print_to_file(f'krysa = {krysa}')
            kiki = pyautogui.locateCenterOnScreen('img/tonelli/kikimora.png', confidence=0.85)
            my_print_to_file(f'kiki = {kiki}')
            if krysa:
                rat_q += 1
                print(f'{rat_q} Detekt krysa')
            if kiki:
                kiki_q += 1
                print(f'{kiki_q} Detekt Kikimora')
            if arachne:
                arachne_q += 1
                print(f'{arachne_q} Detekt arachne')
            if raptor:
                raptor_q += 1
                print(f'{raptor_q} Detekt raptor')
            enemy_battle(1)
        if post:
            my_print_to_file(f'post = {post}')
            pyautogui.moveTo(post, duration=0.2)
            attack = pyautogui.locateCenterOnScreen('img/tonelli/attack.png', confidence=0.85)
            entry = pyautogui.locateCenterOnScreen('img/tonelli/entry_station.png', confidence=0.8)
            if entry:
                my_print_to_file(f'entry = {entry}')
                move_to_click(entry, 0.3)
                sleep(1)
            elif attack:
                my_print_to_file(f'attack = {attack}')
                move_to_click(attack, 0.3)
                sleep(1)
        id_st = pyautogui.locateCenterOnScreen(st2, confidence=0.85)
        my_print_to_file(f'id_st = {id_st}')
    print(st0)  # название станции
    my_print_to_file(st0)
    pyautogui.moveTo(id_st, duration=1, tween=pyautogui.easeInOutQuad)
    # вызов функции "event_gifts()" и подсчет количества найденных
    pos_gift = event_gifts()
    my_print_to_file(f'pos_gift = {pos_gift}')
    if pos_gift:
        number_of_gifts += 1
    if number_of_gifts:
        print(st0, ' подарков ', number_of_gifts)


# принимает имя файла поиска, выдаёт Point(x, y), параметр confidence
def poisk(chto_ishchem, param_confidence=0.99):
    my_print_to_file('touring.poisk')
    sleep(1)
    pos_search = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
    while pos_search is None:
        param_confidence -= 0.01
        # print('в поиске станции confidence=', param_confidence)
        pos_search = pyautogui.locateCenterOnScreen(chto_ishchem, confidence=param_confidence)
        # print(pos_search)
    return pos_search, param_confidence


# Получает в переменной станцию из списка, при необходимости смещает карту. Передав в poisk название следующей станции,
# получает из него Point(x, y) поиска и параметр confidence,
def traffic_on_the_map(stan):
    my_print_to_file('touring.traffic_on_the_map')
    to_map()
    sleep(1 * 2)
    ev_map = stan[3]
    my_print_to_file(f'ev_map = {ev_map}')
    pos_stan = pyautogui.locateCenterOnScreen(stan[1], confidence=0.84)
    my_print_to_file(f'pos_stan = {pos_stan}, stan[1] = {stan[1]}')
    if ev_map == 'стрелка север' and pos_stan is None:
        pos_click = pyautogui.locateCenterOnScreen('img/tonelli/mark_sever.png', confidence=0.85)
        my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "север"')
        move_to_click(pos_click, 0.3)
        sleep(1)
    elif ev_map == 'стрелка юг' and pos_stan is None:
        pos_click = pyautogui.locateCenterOnScreen('img/tonelli/mark_yug.png', confidence=0.85)
        my_print_to_file(f'pos_click = {pos_click}, нажал на стрелку "юг"')
        move_to_click(pos_click, 0.3)
        sleep(1)
    point_poisk, confidence_poisk = poisk(stan[1])
    my_print_to_file(f'point_poisk = {point_poisk}, confidence_poisk = {confidence_poisk}')
    move_to_click(point_poisk, 0.3)
    events_tunnel(stan[0], stan[2])


# получает список маршрута и осуществляет движение по нему
def travel(track: list):
    """
    Принимает список содержащий маршрут
    :param track: list
    """
    my_print_to_file('touring.travel')
    for it in range(len(track)):
        k = it % len(track)
        # print(k, track[k])
        traffic_on_the_map(track[k])


def test():
    """
    Тест передвижения между станциями
    :return: количество встреченных крыс
    """
    my_print_to_file('touring.test')
    global rat_q
    push_close_all_()
    travel(b_d.test_running2)
    print("тест успешно выполнен")
    return rat_q


def tasks_na_kievskoy():
    """ С Фрунзенской на Киевскую,
     задания на пули, потом на Университет,
     на ч.крыс потратить остаток,
     и домой на Фрунзенскую.
    """
    my_print_to_file('touring.tasks_na_kievskoy')
    push_close_all_()
    frunze_kiev()
    vybor_zadaniya_na_puli()
    print('задания на Киевской выполнены')
    kiev_univer()
    en_task_item(1)
    print('энергия исчерпана')
    univer_frunze()
    # """Движение от Кузнецкого моста на Киевскую - выполнение заданий нач. станции - движение до Кузнецкого моста -
    # выполнение заданий нач. станции пока есть задания удовлетворяющие поиск"""
    # my_print_to_file('touring.tasks_na_kievskoy')
    # push_close_all_()
    # frunze_kiev()
    # vybor_zadaniya_na_puli()
    # print('задания на Киевской выполнены')
    # kiev_frunze()
    # vybor_zadaniya_na_puli()
    # print('энергия исчерпана')


def univer_frunze():
    my_print_to_file('touring.univer_frunze')

    push_close_all_()
    travel(b_d.univer_frunze)
    print("пришел на Фрунзе")



def kiev_univer():
    my_print_to_file('touring.kiev_univer')

    push_close_all_()
    travel(b_d.kiev_univer)
    print("пришел на Универ")



# движение от st_park_kr до Кузнецкого моста
def most_riga():
    # движение от
    """Маршрут Кузнецкий мост - Киевская"""
    my_print_to_file('touring.most_riga')
    start_time = time()
    push_close_all_()
    travel(b_d.most_riga)
    print("пришел на Рижскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def riga_most():
    """Маршрут Рижская - Кузнецкий мост"""
    my_print_to_file('touring.riga_most')
    start_time = time()
    push_close_all_()
    travel(b_d.riga_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def frunze_most():
    """Маршрут Фрунзенская - Кузнецкий мост"""
    my_print_to_file('touring.frunze_most')
    start_time = time()
    push_close_all_()
    travel(b_d.frunze_most)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def most_frunze():
    """Маршрут Кузнецкий мост - Фрунзенская"""
    my_print_to_file('touring.most_frunze')
    start_time = time()
    push_close_all_()
    travel(b_d.most_frunze)
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


# движение от


def most_kiev():
    """Маршрут Кузнецкий мост - Киевская"""
    my_print_to_file('touring.most_kiev')
    start_time = time()
    push_close_all_()
    travel(b_d.most_kiev)
    print("пришел на Киевскую")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def kiev_most():
    """Маршрут Киевская - Кузнецккий мост """
    my_print_to_file('touring.kiev_most')
    start_time = time()
    push_close_all_()
    travel(b_d.kiev_most)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_kiev():
    """Маршрут Фрунзенская - Киевская"""
    my_print_to_file('touring.frunze_kiev')
    push_close_all_()
    travel(b_d.frunze_kiev)
    print("пришел на Киевскую")


def kiev_frunze():
    """Маршрут Киевская - Фрунзенская"""
    my_print_to_file('touring.kiev_frunze')
    start_time = time()
    push_close_all_()
    travel(b_d.kiev_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def frunze_riga():
    """Маршрут Фрунзенская"""
    my_print_to_file('touring.frunze_riga')
    start_time = time()
    push_close_all_()
    travel(b_d.frunze_riga)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def riga_frunze():
    """Маршрут  Фрунзенская"""
    my_print_to_file('touring.riga_frunze')
    start_time = time()
    push_close_all_()
    travel(b_d.riga_frunze)
    print("вернулся домой")
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, ' минут', seconds, ' сек.')


def za_kikimorami():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    my_print_to_file('touring.za_kikimorami')

    start_time = time()
    push_close_all_()
    travel(b_d.frunze_kikimory)
    print('на сегодня кикиморы выбиты')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def pauk_yascher():
    """При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    my_print_to_file('touring.pauk_yascher')
    start_time = time()
    push_close_all_()
    travel(b_d.pauk_yascher)
    print('на сегодня все пауки с ящерами зачищены')
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def sbor_podarkov():
    """Обход всех станций. При смене станции прописки список содержащий маршрут надо переписывать вручную."""
    my_print_to_file('touring.sbor_podarkov')
    push_close_all_()
    # travel(b_d.bypass)
    for it in range(len(b_d.bypass)):
        k = it % len(b_d.bypass)
        # print(k, b_d.bypass[k])
        traffic_on_the_map(b_d.bypass[k])
    print("все подарки под ёлками собраны")

# 353
