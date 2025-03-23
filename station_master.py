""" Точка для отладки, остановка на выбранном задании, на строках 103 - 105 """
import baza_dannyx as b_d
import pyautogui
from time import sleep
import fun
import create_and_analiz_img
import my_color_text as myCt
from heroes import Hero, Activ
import heroes as her
import cr_img

# import station_master

conf_ = 0.95
par_conf = 0.799
conf_mobs = 0.99
energy_availability = 1
number_tasks = 1
variable = None


def wait_skip_battle_button():
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    while not skip_battle:
        skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    # if skip_battle:
    #     cr_img.cri_event_img(x_reg=96, y_reg=36, name='img/skip_battle.png')


def enemy_battle(prolong_=2, add_up=True):
    fun.my_print_to_file('station_master.enemy_battle()')
    fun.my_print_to_file(' поиск battle_end, skip_battle, dog')

    her.nam += 1

    battle_end = fun.locCenterImg('img/b_battle_end.png', confidence=par_conf)
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    dog = fun.locCenterImg('img/dog_2.png', confidence=par_conf)

    # 1 серая крыса
    name1_grey_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
    # 1 белая крыса
    name1_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
    # 1 черная крыса
    name1_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
    # 1 песчаная крыса
    # name1_sand_rat = fun.locCenterImg('img/tonelli/mobi/name1_sand_rat.png', confidence=conf_mobs)
    # 2 шпион
    name2_spy = fun.locCenterImg('img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
    # 3 контрабандисты
    name3_smuggler = fun.locCenterImg('img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
    # 4 паук
    name4_arachne = fun.locCenterImg('img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
    # 5 дикарь
    name5_wildman = fun.locCenterImg('img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
    # 6 кикиморы
    name6_kikimora = fun.locCenterImg('img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
    # 7 ящер
    name7_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

    # print('dog', dog)
    it = 0
    mob_identified = None
    count_mob_identified = 0
    cycle = True
    result = None
    while not battle_end:
        # cr_img.mob_foto(her.nam)
        if add_up:
            while not mob_identified and count_mob_identified <= 3:
                count_mob_identified += 1
                # if count_mob_identified > 1:
                #     print(f'{count_mob_identified=}')
                if name1_grey_rat and cycle:
                    cycle = False
                    fun.move_mause(pos=name1_grey_rat, speed=0.5)
                    Hero.app_rat(Activ.hero_activ)
                    print(myCt.tc_magenta(f'detekt {Hero.get_qty_grey_rat(Activ.hero_activ)} grey rat'))
                    mob_identified = 'grey_rat'
                if name1_black_rat and cycle:
                    cycle = False
                    fun.move_mause(pos=name1_black_rat, speed=0.5)
                    mob_identified = 'black_rat'
                    print(myCt.tc_magenta('черная крыса'))
                if name1_white_rat and cycle:
                    cycle = False
                    fun.move_mause(pos=name1_white_rat, speed=0.5)
                    mob_identified = 'white_rat'
                    print(myCt.tc_magenta('белая крыса'))
                if name2_spy and cycle:
                    cycle = False
                    fun.move_mause(pos=name2_spy, speed=0.5)
                    mob_identified = 'spy'
                    print(myCt.tc_magenta('шпион пойман'))
                if name3_smuggler and cycle:
                    cycle = False
                    fun.move_mause(pos=name3_smuggler, speed=0.5)
                    mob_identified = 'smuggler'
                    print(myCt.tc_magenta('контрабандист пойман'))
                if name4_arachne and cycle:
                    cycle = False
                    fun.my_print_to_file(f'{name4_arachne=}')
                    # cr_img.mob_id('arachne')
                    Hero.app_arachne(Activ.hero_activ)
                    print(f'detekt {Hero.get_qty_arachne(Activ.hero_activ)} arachne')
                    mob_identified = 'arachne'
                if name5_wildman and cycle:
                    cycle = False
                    fun.move_mause(pos=name5_wildman, speed=1)
                    Hero.app_wildman(Activ.hero_activ)
                    print(Hero.get_report_wildman_now(Activ.hero_activ))
                    print(Hero.get_report_wildman(Activ.hero_activ))
                    mob_identified = "wildman"
                if name6_kikimora and cycle:
                    cycle = False
                    fun.my_print_to_file(f'{name6_kikimora=}')
                    # cr_img.mob_id('kikimora')
                    Hero.app_kiki(Activ.hero_activ)
                    print(f' Detekt {Hero.get_qty_kiki(Activ.hero_activ)} kikimora')
                    mob_identified = 'kikimora'
                if name7_raptor and cycle:
                    cycle = False
                    fun.move_mause(pos=name7_raptor, speed=0.5)
                    Hero.app_raptor(Activ.hero_activ)
                    print(f'Detekt {Hero.get_qty_raptor(Activ.hero_activ)} raptor')
                    mob_identified = 'raptor'
                # if count_mob_identified == 3:
                #     cr_img.mob_id(her.nam)
                # 1 серая крыса
                name1_grey_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
                # 1 белая крыса
                name1_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
                # 1 черная крыса
                name1_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
                # 1 песчаная крыса
                # name1_sand_rat = fun.locCenterImg('img/tonelli/mobi/name1_sand_rat.png', confidence=0.85)
                # 2 шпион
                name2_spy = fun.locCenterImg('img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
                # 3 контрабандисты
                name3_smuggler = fun.locCenterImg('img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
                # 4 паук
                name4_arachne = fun.locCenterImg('img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
                # 5 дикарь
                name5_wildman = fun.locCenterImg('img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
                # 6 кикиморы
                name6_kikimora = fun.locCenterImg('img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
                # 7 ящер
                name7_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

                # print(f'{mob_identified=}, {count_mob_identified=}')

            # print(f'{mob_identified=}, {count_mob_identified=}')
        if dog:  # нажать "на собаку"
            fun.my_print_to_file(f'{dog=}')
            fun.my_print_to_file("нажал на собаку")
            fun.move_to_click(dog, 0.1)
        if skip_battle and it >= 2:  # нажать "пропустить бой"
            fun.my_print_to_file(f'{skip_battle=}')
            fun.move_to_click(skip_battle, 0.5)
        it += 1
        sleep(1 * prolong_)  # для задержки нажатия "пропустить бой"
        fun.my_print_to_file('ожидание battle_end, close, dog, skip_battle')
        battle_end = fun.locCenterImg('img/b_battle_end.png', confidence=par_conf)
        close = fun.locCenterImg('img/overall/close.png', confidence=par_conf)

        # 1 серая крыса
        name1_grey_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
        # 1 белая крыса
        name1_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
        # 1 черная крыса
        name1_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
        # 1 песчаная крыса
        # name1_sand_rat = fun.locCenterImg('img/tonelli/mobi/name1_sand_rat.png', confidence=0.85)
        # 2 шпион
        name2_spy = fun.locCenterImg('img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
        # 3 контрабандисты
        name3_smuggler = fun.locCenterImg('img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
        # 4 паук
        name4_arachne = fun.locCenterImg('img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
        # 5 дикарь
        name5_wildman = fun.locCenterImg('img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
        # 6 кикиморы
        name6_kikimora = fun.locCenterImg('img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
        # 7 ящер
        name7_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

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
    fun.my_print_to_file(f'{skip_battle1_end_ver=}')
    while skip_battle1_end_ver:
        fun.push_close()
        sleep(0.2)
        skip_battle1_end_ver = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
        fun.my_print_to_file(f'{skip_battle1_end_ver=}')

    fun.my_print_to_file("выход из 'enemy_battle")
    return result


def press_en(task_number, pos):
    fun.my_print_to_file("station_master.press_en()")
    global energy_availability, conf_
    x = pos[0] - 100
    y = pos[1] - 20
    pos_clik = x, y
    # pyautogui.moveTo(pos_clik)            # для отладки раскомментировать
    # print('тут должен быть клик')         # для отладки раскомментировать
    fun.move_to_click(pos_clik, 1.5)  # для отладки закомментировать
    sleep(0.5)
    nal_energy = fun.locCenterImg('img/low_energy.png', confidence=0.8)
    if not nal_energy:
        vers_in_print = "" if conf_ == 0.95 else f', conf_={conf_}'
        print(f'Выполняю  {task_number}  задание{vers_in_print}')
        wait_skip_battle_button()
        enemy_battle()
        energy_availability = 1
    else:
        energy_availability = 0
        print(' Энергия закончилась!!')
        print(Hero.get_report_wildman_now(Activ.hero_activ))
        print(Hero.get_report_wildman(Activ.hero_activ))
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
    fun.my_print_to_file('station_master.task_analysis()')
    global variable
    fun.vizit_to_station_master()
    variant1 = pyautogui.locateCenterOnScreen(img1, minSearchTime=1.0, region=region, confidence=conf_)
    # v3 = pyautogui.locateCenterOnScreen(img2, minSearchTime=1.0, region=region, confidence=conf_)
    variant2 = pyautogui.locateCenterOnScreen(img2, minSearchTime=1.0, confidence=conf_, region=region)
    if variant1:
        variable = variant1
    else:
        variable = variant2
    return variable


def move(pos):
    fun.my_print_to_file('station_master.move()')
    if pos:
        pyautogui.moveTo(pos, duration=1)
        sleep(3)


def station_task_list():
    fun.my_print_to_file("station_master.station_task_list()")
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


def choosing_task_money():
    fun.my_print_to_file("station_master.choosing_task_money()")
    # print('station_master.choosing_task_money')
    global energy_availability, number_tasks  # , conf_
    conf_ = 0.95
    fun.push_close_all_()
    task = station_task_list()
    hero = fun.selection_hero()
    # print('герой определён station_master.стр 168')
    if hero:
        path = Hero.get_path_task(Activ.hero_activ)
        # print(path, "station_master.choosing_task_money стр 172")
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
    fun.selection_hero()
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
