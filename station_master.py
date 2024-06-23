import baza_dannyx as b_d
import pyautogui
from time import sleep
from fun import move_to_click, push_close_all_, vizit_to_station_master, get_areas_task_big, my_print_to_file
from my_screenshot import get_screenshot_task

conf_ = 0.95
par_conf = 0.799
energy_availability = 1
number_tasks = 1
# width, height = 87, 39
variable = None


# region1, region2, region3 = 0, 0, 0


def enemy_battle(prolong=2):
    """
    Событие сражения с противником
    :param prolong: регулирует длительность сражения
    """
    my_print_to_file('station_master.enemy_battle')
    my_print_to_file(' поиск battle_end, skip_battle, dog')
    battle_end = pyautogui.locateCenterOnScreen('img/b_battle_end.png', confidence=par_conf)
    skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
    dog = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
    it = 0
    while not battle_end:
        if dog:  # нажать "на собаку"
            my_print_to_file(f'dog = {dog}')
            my_print_to_file("нажал на собаку")
            move_to_click(dog, 0.1)
        if skip_battle and it >= 2:  # нажать "пропустить бой"
            my_print_to_file(f'skip_battle = {skip_battle}')
            move_to_click(skip_battle, 0.5)
        it += 1
        sleep(1 * prolong)  # для задержки нажатия "пропустить бой"
        my_print_to_file('ожидание battle_end, close, dog, skip_battle')
        battle_end = pyautogui.locateCenterOnScreen('img/b_battle_end.png', confidence=par_conf)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=par_conf)
        dog = pyautogui.locateCenterOnScreen('img/dog.png', confidence=par_conf)
        skip_battle = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
        if battle_end and close:  # нажать закрыть в конце боя
            my_print_to_file("нажать закрыть в конце боя")
            push_close_all_()
            sleep(0.)

    skip_battle1_end_ver = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
    my_print_to_file(f'skip_battle1_end_ver = {skip_battle1_end_ver}')
    while skip_battle1_end_ver:
        sleep(0.2)
        skip_battle1_end_ver = pyautogui.locateCenterOnScreen('img/skip_battle.png', confidence=par_conf)
        my_print_to_file(f'skip_battle1_end_ver = {skip_battle1_end_ver}')

    my_print_to_file("выход из 'enemy_battle")


def press_en(task_number, pos):
    global energy_availability, conf_
    x = pos[0]
    y = pos[1] - 20
    pos_clik = x, y
    # pyautogui.moveTo(pos_clik) # для отладки
    # print('тут должен быть клик') # для отладки
    move_to_click(pos_clik, 1.5)  # для отладки закомментировать
    sleep(0.5)
    nal_energy = pyautogui.locateCenterOnScreen('img/low_energy.png', confidence=0.8)
    if not nal_energy:
        print(f'Выполняю  {task_number}  задание, conf_={conf_}')
        enemy_battle()
    else:
        energy_availability = 0
        print(' Энергия закончилась!!')
        sleep(1)
        close = pyautogui.locateCenterOnScreen('img/close.png')
        move_to_click(close, 0.5)


def task_analysis(img1, img2, region):
    """
    При анализе через картинки получает их имена и region= поиска
    :param img1: *.png
    :param img2: *.png
    :param region:
    :return: Point | None
    """
    global variable
    vizit_to_station_master()
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


def data_station():
    """ Получение списка заданий """
    it = 0
    n_in_list = 0
    while it < len(b_d.list_of_stations):
        img_station = b_d.list_of_stations[it][2]
        pos = pyautogui.locateCenterOnScreen(img_station, confidence=0.9)
        if pos:
            it = len(b_d.list_of_stations)
        else:
            n_in_list += 1
            it += 1
    task_options = (b_d.list_of_stations[n_in_list][4])
    return task_options


def vybor_zadaniya_na_puli():
    global energy_availability, number_tasks, conf_
    xp_img = data_station()
    region_1, region_2, region_3 = get_areas_task_big()
    while energy_availability == 1 and number_tasks > 0:
        task_analysis(xp_img[0], xp_img[1], region_1)
        variant1 = variable
        move(variant1)
        sleep(0.1)

        task_analysis(xp_img[2], xp_img[3], region_2)
        variant2 = variable
        move(variant2)
        sleep(0.1)

        task_analysis(xp_img[4], xp_img[5], region_3)
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
            print('confidence=', conf_)
            conf_ -= 0.005
            conf_ = round(conf_, 3)
        if conf_ <= 0.8:
            print('задания не найдены, результаты "D:\\bot in br\\testOCR\img\\test" ')
            get_screenshot_task()
            number_tasks = 1
            energy_availability = 0

    print(' Задания выполнены!!!!')
    number_tasks = 1
    energy_availability = 1
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while close:
        move_to_click(close, 0.3)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)


def en_task_item(task_number):
    global energy_availability, number_tasks  # , conf_
    region_1, region_2, region_3 = get_areas_task_big()
    if task_number == 1:
        region = region_1
    elif task_number == 2:
        region = region_2
    else:
        region = region_3

    while energy_availability == 1 and number_tasks > 0:
        vizit_to_station_master()
        press_en(task_number, region)
    print(' Задания выполнены!!!!')
    number_tasks = 1
    energy_availability = 1
    close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
    while close:
        move_to_click(close, 0.3)
        close = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
