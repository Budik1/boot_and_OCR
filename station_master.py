""" Точки для отладки в press_en()"""
import baza_dannyx as b_d
from time import sleep
import fun
import find_img as find
import create_and_analiz_img
import solid_memory
import my_color_text as myCt
from heroes import Hero, Activ
import heroes as her

conf_ = 0.95
par_conf = 0.799
conf_mobs = 0.99
energy_availability = 1
number_tasks = 1
variable = None


def wait_skip_battle_button():
    skip_battle = find.find_skip_battle()
    while not skip_battle:
        skip_battle = find.find_skip_battle()


def enemy_battle(prolong_=2, dog_activ=True, add_up=True, count_task=False, arena=False):
    fun.my_print_to_file('station_master.enemy_battle()')
    fun.my_print_to_file(' поиск battle_end, skip_battle, dog')

    her.nam += 1

    battle_end = fun.locCenterImg(name_img='img/b_battle_end.png', confidence=par_conf)
    skip_battle = fun.locCenterImg(name_img='img/skip_battle.png', confidence=par_conf)
    dog = fun.locCenterImg(name_img='img/dog_2.png', confidence=par_conf)

    name1_grey_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
    name1_white_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
    name1_black_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
    name1_sand_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_sand_rat.png', confidence=conf_mobs)
    name2_spy = fun.locCenterImg(name_img='img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
    name3_smuggler = fun.locCenterImg(name_img='img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
    name4_arachne = fun.locCenterImg(name_img='img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
    name5_wildman = fun.locCenterImg(name_img='img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
    name6_kikimora = fun.locCenterImg(name_img='img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
    name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

    duration_fight = 0
    dog_count = True
    skip_battle_count = True
    mob_identified = None
    count_mob_identified = 0
    cycle = True
    result = None
    if not arena:
        count_task_now = Hero.get_task_count(Activ.hero_activ)

    while not battle_end:
        if add_up:
            while not mob_identified and count_mob_identified <= 3:
                count_mob_identified += 1
                if name1_grey_rat and cycle:
                    cycle = False
                    fun.mouse_move(pos=name1_grey_rat, speed=0.4)
                    Hero.app_rat(Activ.hero_activ)
                    if count_task:
                        print(myCt.tc_magenta(
                            f'detekt {Hero.get_qty_grey_rat(Activ.hero_activ)} grey rat. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta(f'detekt {Hero.get_qty_grey_rat(Activ.hero_activ)} grey rat'))
                    mob_identified = 'grey_rat'
                if name1_black_rat and cycle:
                    cycle = False
                    fun.mouse_move(pos=name1_black_rat, speed=0.4)
                    mob_identified = 'black_rat'
                    if count_task:
                        print(myCt.tc_magenta(f'черная крыса. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta('черная крыса'))
                if name1_white_rat and cycle:
                    cycle = False
                    fun.mouse_move(pos=name1_white_rat, speed=0.4)
                    mob_identified = 'white_rat'
                    if count_task:
                        print(myCt.tc_magenta(f'белая крыса. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta('белая крыса'))
                if name1_sand_rat and cycle:
                    cycle = False
                    fun.mouse_move(pos=name1_sand_rat, speed=0.4)
                    mob_identified = 'sand_rat'
                    if count_task:
                        print(myCt.tc_magenta(f'песчаная крыса. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta('песчаная крыса'))
                if name2_spy and cycle:
                    cycle = False
                    fun.mouse_move(pos=name2_spy, speed=0.4)
                    mob_identified = 'spy'
                    if count_task:
                        print(myCt.tc_magenta(f'шпион пойман. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta('шпион пойман'))
                if name3_smuggler and cycle:
                    cycle = False
                    fun.mouse_move(pos=name3_smuggler, speed=0.4)
                    mob_identified = 'smuggler'
                    if count_task:
                        print(myCt.tc_magenta(f'контрабандист пойман. {count_task_now}'))
                    else:
                        print(myCt.tc_magenta('контрабандист пойман'))
                if name4_arachne and cycle:
                    cycle = False
                    fun.my_print_to_file(f'{name4_arachne=}')
                    # cr_img.mob_id('arachne')
                    Hero.app_arachne(Activ.hero_activ)
                    if count_task:
                        print(f'detekt {Hero.get_qty_arachne(Activ.hero_activ)} arachne. {count_task_now}')
                    else:
                        print(f'detekt {Hero.get_qty_arachne(Activ.hero_activ)} arachne')
                    mob_identified = 'arachne'
                if name5_wildman and cycle:
                    cycle = False
                    fun.mouse_move(pos=name5_wildman, speed=0.4)
                    Hero.app_wildman(Activ.hero_activ)
                    if count_task:
                        print(f'{Hero.get_report_wildman_now(Activ.hero_activ)}. {count_task_now}')
                        print(Hero.get_report_wildman(Activ.hero_activ))
                    else:
                        print(f'{Hero.get_report_wildman_now(Activ.hero_activ)}')
                        print(Hero.get_report_wildman(Activ.hero_activ))
                    mob_identified = "wildman"
                if name6_kikimora and cycle:
                    cycle = False
                    fun.my_print_to_file(f'{name6_kikimora=}')
                    Hero.app_kiki(Activ.hero_activ)
                    if count_task:
                        print(f' Detekt {Hero.get_qty_kiki(Activ.hero_activ)} kikimora. {count_task_now}')
                    else:
                        print(f' Detekt {Hero.get_qty_kiki(Activ.hero_activ)} kikimora')
                    mob_identified = 'kikimora'
                if name7_raptor and cycle:
                    cycle = False
                    fun.mouse_move(pos=name7_raptor, speed=0.4)
                    Hero.app_raptor(Activ.hero_activ)
                    if count_task:
                        print(f'Detekt {Hero.get_qty_raptor(Activ.hero_activ)} raptor. {count_task_now}')
                    else:
                        print(f'Detekt {Hero.get_qty_raptor(Activ.hero_activ)} raptor')
                    mob_identified = 'raptor'

                name1_grey_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
                name1_white_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_white_rat.png',
                                                   confidence=conf_mobs)
                name1_black_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_black_rat.png',
                                                   confidence=conf_mobs)
                name1_sand_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_sand_rat.png', confidence=conf_mobs)
                name2_spy = fun.locCenterImg(name_img='img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
                name3_smuggler = fun.locCenterImg(name_img='img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
                name4_arachne = fun.locCenterImg(name_img='img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
                name5_wildman = fun.locCenterImg(name_img='img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
                name6_kikimora = fun.locCenterImg(name_img='img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
                name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)
        if dog_activ:
            if dog and dog_count:
                # нажать "на собаку"
                dog_count = False
                fun.my_print_to_file(f'{dog=}')
                # print(f'{dog=}')
                fun.my_print_to_file("нажал на собаку")
                # print('"нажал на собаку"')
                fun.mouse_move_to_click(pos_click=dog, move_time=0.4, z_p_k=0.1)
        if skip_battle and skip_battle_count:
            # print(f'{skip_battle=}, {skip_battle_count=}, {duration_fight=}')
            duration_fight += 1
        if skip_battle and skip_battle_count and duration_fight == 4:  # нажать "пропустить бой"
            skip_battle_count = False
            fun.my_print_to_file(f'{skip_battle=}')
            # print('жму пропустить бой')
            fun.mouse_move_to_click(pos_click=skip_battle, move_time=0.4, z_p_k=0.5)
        sleep(1 * prolong_)  # для задержки нажатия "пропустить бой"
        fun.my_print_to_file('ожидание battle_end, close, dog, skip_battle')
        battle_end = fun.locCenterImg(name_img='img/b_battle_end.png', confidence=par_conf)
        close = fun.locCenterImg(name_img='img/overall/close.png', confidence=par_conf)

        name1_grey_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
        name1_white_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
        name1_black_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
        name1_sand_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_sand_rat.png', confidence=conf_mobs)
        name2_spy = fun.locCenterImg(name_img='img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
        name3_smuggler = fun.locCenterImg(name_img='img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
        name4_arachne = fun.locCenterImg(name_img='img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
        name5_wildman = fun.locCenterImg(name_img='img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
        name6_kikimora = fun.locCenterImg(name_img='img/tonelli/mobi/name6_kikimora.png', confidence=conf_mobs)
        name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

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

    if not arena:
        solid_memory.save_to_file(info=False)
    fun.my_print_to_file("выход из 'enemy_battle")
    return result


def press_en(*, task_number, pos, value_energy):
    fun.my_print_to_file("station_master.press_en()")
    global energy_availability, conf_
    x = pos[0] - 100
    y = pos[1] - 20
    pos_clik = x, y
    # pyautogui.moveTo(pos_clik)            # для отладки раскомментировать
    # print('тут должен быть клик')         # для отладки раскомментировать
    fun.mouse_move_to_click(pos_click=pos_clik, move_time=0.4, z_p_k=1.5)  # для отладки закомментировать
    sleep(0.5)
    low_energy = fun.locCenterImg(name_img='img/low_energy.png', confidence=0.8)
    if not low_energy:
        vers_in_print = "" if conf_ == 0.95 else f', conf_={conf_}'
        Hero.app_task_count(Activ.hero_activ)
        Hero.app_energy_count_today(Activ.hero_activ, value_energy)
        value_energy_today = Hero.get_energy_count_today(Activ.hero_activ)
        value_energy_all = Hero.get_energy_count_all(Activ.hero_activ)
        # Выполняю 3 задание, conf_=0.94. Сейчас 3, сегодня 20, всего 120
        print(f'Выполняю {task_number} задание, {vers_in_print}.'
              f' Сейчас {value_energy}, сегодня {value_energy_today}, всего {value_energy_all}')
        solid_memory.save_to_file(info=False)
        wait_skip_battle_button()
        enemy_battle(count_task=True)
        energy_availability = 1  # для выполнения всех заданий
        # energy_availability = 0 # для выполнения одного задания
    else:
        energy_availability = 0
        print(' Энергия закончилась!!')
        if Hero.get_report_wildman(Activ.hero_activ):
            print(Hero.get_report_wildman_now(Activ.hero_activ))
            print(Hero.get_report_wildman(Activ.hero_activ))
        sleep(1)
        close = fun.locCenterImg(name_img='img/overall/close.png')
        fun.mouse_move_to_click(pos_click=close, z_p_k=0.5)


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
    variant1 = fun.locCenterImg(name_img=img1, confidence=conf_, region=region)
    # v3 = pyautogui.locateCenterOnScreen(img2, minSearchTime=1.0, region=region, confidence=conf_)
    variant2 = fun.locCenterImg(name_img=img2, confidence=conf_, region=region)
    if variant1:
        price_task = int(''.join(c if c.isdigit() else ' ' for c in img1))
        return variant1, price_task
    elif variant2:
        variable = variant2
        price_task = int(''.join(c if c.isdigit() else ' ' for c in img2))
        return variant2, price_task
    else:
        return None, None


def move(pos):
    fun.my_print_to_file('station_master.move()')
    if pos:
        fun.mouse_move(pos=pos, speed=0.5)
        sleep(1)


def station_task_list():
    fun.my_print_to_file("station_master.station_task_list()")
    """ Получение списка заданий """
    it = 0
    n_in_list = 0
    while it < len(b_d.list_of_stations):
        img_station = b_d.list_of_stations[it][2]
        pos = fun.locCenterImg(name_img=img_station, confidence=0.9)
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
    price_task = None
    conf_ = 0.95
    fun.push_close_all_()
    task = station_task_list()
    hero = fun.selection_hero()
    # print('герой определён station_master.стр 168')
    if hero:
        path = Hero.get_path_task(Activ.hero_activ)
        # print(path, "station_master.choosing_task_money стр 297")
    else:
        return
    region_1, region_2, region_3 = fun.get_areas_task_big()
    while energy_availability == 1 and number_tasks > 0:
        # task_analysis(F'{path}{task[0]}', F'{path}{task[1]}', region_1)
        # print(f'{path}{task[0]}', f"{path}{task[1]}")
        variant1, price_task1 = task_analysis(F'{path}{task[0]}', F'{path}{task[1]}', region_1)
        # print(f'{variant1=}, {price_task1=}')
        move(variant1)
        sleep(0.1)

        variant2, price_task2 = task_analysis(F'{path}{task[2]}', F'{path}{task[3]}', region_2)
        # print(f'{variant2}, {price_task2=}')
        move(variant2)
        sleep(0.1)

        variant3, price_task3 = task_analysis(F'{path}{task[4]}', F'{path}{task[5]}', region_3)
        # print(f'{variant3}, {price_task3=}')
        move(variant3)
        sleep(0.1)

        if variant1:
            price_task = price_task1
            press_en(task_number=1, pos=region_1, value_energy=price_task)
        if variant2:
            price_task = price_task2
            press_en(task_number=2, pos=region_2, value_energy=price_task)
        if variant3:
            price_task = price_task3
            press_en(task_number=3, pos=region_3, value_energy=price_task)

        if variant1 == variant2 == variant3:
            print(F'confidence={conf_}')
            conf_ -= 0.005
            conf_ = round(conf_, 3)
        if conf_ <= 0.92:
            print(myCt.tc_cyan('задания не найдены, результаты "D:\\bot in br\\testOCR\\img\\test\\test_tasks" '))
            create_and_analiz_img.get_screenshot_task()
            number_tasks = 1
            energy_availability = 0
            return

    print(myCt.tc_green(' Задания выполнены!!!!'))
    number_tasks = 1
    energy_availability = 1
    close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
    while close:
        fun.mouse_move_to_click(pos_click=close, z_p_k=0.3)
        close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)


def task_pos_item(task_num):
    """ Выбор по позиции задания """
    fun.selection_hero()
    global energy_availability, number_tasks  # , conf_
    region_1, region_2, region_3 = fun.get_areas_task_big()
    if task_num == 1:
        region = region_1
    elif task_num == 2:
        region = region_2
    else:
        region = region_3

    while energy_availability == 1 and number_tasks > 0:
        fun.vizit_to_station_master()
        press_en(task_number=task_num, pos=region, value_energy=1)
    print(myCt.tc_green(' Задания выполнены'))
    number_tasks = 1
    energy_availability = 1
    close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
    while close:
        fun.mouse_move_to_click(pos_click=close, z_p_k=0.3)
        close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
