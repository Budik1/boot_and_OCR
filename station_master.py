import baza_dannyx as b_d
import pyautogui
from time import sleep
import fun
import create_and_analiz_img
import my_color_text as myCt

conf_ = 0.95
par_conf = 0.799
energy_availability = 1
number_tasks = 1
variable = None


def enemy_battle(prolong_=2):
    """
    Событие сражения с противником
    :param prolong_: регулирует длительность сражения
    """
    fun.my_print_to_file('station_master.enemy_battle')
    fun.my_print_to_file(' поиск battle_end, skip_battle, dog')
    battle_end = fun.locCenterImg('img/b_battle_end.png', confidence=par_conf)
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    dog = fun.locCenterImg('img/dog_2.png', confidence=par_conf)
    # print('dog', dog)
    it = 0
    result = None
    while not battle_end:
        if dog:  # нажать "на собаку"
            fun.my_print_to_file(f'dog = {dog}')
            fun.my_print_to_file("нажал на собаку")
            fun.move_to_click(dog, 0.1)
        if skip_battle and it >= 2:  # нажать "пропустить бой"
            fun.my_print_to_file(f'skip_battle = {skip_battle}')
            fun.move_to_click(skip_battle, 0.5)
        it += 1
        sleep(1 * prolong_)  # для задержки нажатия "пропустить бой"
        fun.my_print_to_file('ожидание battle_end, close, dog, skip_battle')
        battle_end = fun.locCenterImg('img/b_battle_end.png', confidence=par_conf)
        close = fun.locCenterImg('img/overall/close.png', confidence=par_conf)
        dog = fun.locCenterImg('img/dog.png', confidence=par_conf)
        skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
        if battle_end and close:  # нажать закрыть в конце боя
            victory = fun.locCenterImg('img/arena/victory_in_arena.png', confidence=par_conf)
            defeat = fun.locCenterImg('img/arena/defeat_in_arena.png', confidence=par_conf)
            if victory:
                result = "победа"
            elif defeat:
                result = "поражение"
            fun.my_print_to_file("нажать закрыть в конце боя")
            fun.push_close_all_()
            sleep(0)

    skip_battle1_end_ver = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    fun.my_print_to_file(f'skip_battle1_end_ver = {skip_battle1_end_ver}')
    while skip_battle1_end_ver:
        sleep(0.2)
        skip_battle1_end_ver = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
        fun.my_print_to_file(f'skip_battle1_end_ver = {skip_battle1_end_ver}')

    fun.my_print_to_file("выход из 'enemy_battle")
    return result


def press_en(task_number, pos):
    global energy_availability, conf_
    x = pos[0] - 100
    y = pos[1] - 20
    pos_clik = x, y
    # pyautogui.moveTo(pos_clik)  # для отладки раскомментировать
    # print('тут должен быть клик')  # для отладки
    fun.move_to_click(pos_clik, 1.5)  # для отладки закомментировать
    sleep(0.5)
    nal_energy = fun.locCenterImg('img/low_energy.png', confidence=0.8)
    if not nal_energy:
        vers_in_print = "" if conf_ == 0.95 else f', conf_={conf_}'
        print(f'Выполняю  {task_number}  задание{vers_in_print}')
        enemy_battle()
    else:
        energy_availability = 0
        print(' Энергия закончилась!!')
        sleep(1)
        close = fun.locCenterImg('img/overall/close.png')
        fun.move_to_click(close, 0.5)


def task_analysis(img1, img2, region):
    """
    При анализе через картинки получает их имена и region= поиска
    :param img1: *.png
    :param img2: *.png
    :param region:
    :return: Point | None
    """
    global variable
    fun.vizit_to_station_master()
    variant1 = pyautogui.locateCenterOnScreen(img1, confidence=conf_, region=region)
    variant2 = pyautogui.locateCenterOnScreen(img2, confidence=conf_, region=region)
    if variant1:
        variable = variant1
    else:
        variable = variant2
    return variable


def move(pos):
    if pos:
        pyautogui.moveTo(pos, duration=1)
        sleep(3)


def station_task_list():
    """ Получение списка заданий """
    it = 0
    n_in_list = 0
    while it < len(b_d.list_of_stations):
        img_station = b_d.list_of_stations[it][2]
        pos = fun.locCenterImg(img_station, confidence=0.9)
        if pos:
            it = len(b_d.list_of_stations)
        else:
            n_in_list += 1
            it += 1
    task_list = (b_d.list_of_stations[n_in_list][4])
    return task_list


def vybor_zadaniya_na_puli():
    global energy_availability, number_tasks  # , conf_
    conf_ = 0.95
    fun.push_close_all_()
    task = station_task_list()
    hero = fun.selection_hero()
    if hero == 'Gady':
        path = 'img/person/tasks_gady/'
    elif hero == 'Gavr':
        path = 'img/person/tasks_gavr/'
    elif hero == 'Mara':
        path = 'img/person/tasks_mara/'
    elif hero == 'Велес':
        path = 'img/person/tasks_veles/'
    else:
        return
    region_1, region_2, region_3 = fun.get_areas_task_big()
    while energy_availability == 1 and number_tasks > 0:
        task_analysis(F'{path}{task[0]}', F'{path}{task[1]}', region_1)
        # print(f'{path}{task[0]}', f"{path}{task[1]}")
        variant1 = variable
        move(variant1)
        sleep(0.1)

        task_analysis(F'{path}{task[2]}', F'{path}{task[3]}', region_2)
        variant2 = variable
        move(variant2)
        sleep(0.1)

        task_analysis(F'{path}{task[4]}', F'{path}{task[5]}', region_3)
        variant3 = variable
        move(variant3)
        sleep(0.1)

        if variant1:
            press_en(1, region_1)
        if variant2:
            press_en(2, region_2)
        if variant3:
            press_en(3, region_3)

        if variant1 == variant2 == variant3:
            print(F'confidence={conf_}')
            conf_ -= 0.005
            conf_ = round(conf_, 3)
        if conf_ <= 0.92:
            print(myCt.tc_cyan('задания не найдены, результаты "D:\\bot in br\\testOCR\\img\\test" '))
            create_and_analiz_img.get_screenshot_task()
            number_tasks = 1
            energy_availability = 0
            return
    print(myCt.tc_green(' Задания выполнены!!!!'))
    number_tasks = 1
    energy_availability = 1
    close = fun.locCenterImg('img/overall/close.png', confidence=0.9)
    while close:
        fun.move_to_click(close, 0.3)
        close = fun.locCenterImg('img/overall/close.png', confidence=0.9)


def en_task_item(task_number):
    """ Выбор по позиции задания """
    global energy_availability, number_tasks  # , conf_
    region_1, region_2, region_3 = fun.get_areas_task_big()
    if task_number == 1:
        region = region_1
    elif task_number == 2:
        region = region_2
    else:
        region = region_3

    while energy_availability == 1 and number_tasks > 0:
        fun.vizit_to_station_master()
        press_en(task_number, region)
    print(myCt.tc_green(' Задания выполнены'))
    number_tasks = 1
    energy_availability = 1
    close = fun.locCenterImg('img/overall/close.png', confidence=0.9)
    while close:
        fun.move_to_click(close, 0.3)
        close = fun.locCenterImg('img/overall/close.png', confidence=0.9)

# закоментировал 19.01.25
# def vybor_zadaniya_na_puli_S():
#     global energy_availability, number_tasks, conf_
#
#     task = station_task_list()
#     hero = fun.selection_hero()
#     if hero == 'Gady':
#         pass
#     elif hero == 'Gavr':
#         path = 'img/person/tasks_gavr/'
#         pass
#     else:
#         return
#     region_1, region_2, region_3 = fun.get_areas_task_big()
#     while energy_availability == 1 and number_tasks > 0:
#         task_analysis(f'{path}{task[0]}', task[1], region_1)
#         variant1 = variable
#         move(variant1)
#         sleep(0.1)
#
#         task_analysis(task[2], task[3], region_2)
#         variant2 = variable
#         move(variant2)
#         sleep(0.1)
#
#         task_analysis(task[4], task[5], region_3)
#         variant3 = variable
#         move(variant3)
#         sleep(0.1)
#
#         if variant1:
#             press_en(1, region_1)
#         if variant2:
#             press_en(2, region_2)
#         if variant3:
#             press_en(3, region_3)
#
#         if variant1 == variant2 == variant3:
#             print(F'confidence= {conf_} строка 217')
#             conf_ -= 0.005
#             conf_ = round(conf_, 3)
#         if conf_ <= 0.92:
#             print(myCt.tc_cyan('задания не найдены, результаты "D:\\bot in br\\testOCR\img\\test" '))
#             create_and_analiz_img.get_screenshot_task()
#             number_tasks = 1
#             energy_availability = 0
#
#     print(myCt.tc_green(' Задания выполнены!!!!'))
#     number_tasks = 1
#     energy_availability = 1
#     close = fun.locCenterImg('img/overall/close.png', confidence=0.9)
#     while close:
#         fun.move_to_click(close, 0.3)
#         close = fun.locCenterImg('img/overall/close.png', confidence=0.9)
