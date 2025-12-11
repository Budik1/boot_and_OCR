""" Точки для отладки в press_en()"""
from time import sleep

import color_text
import fun
import find_img
import solid_memory
import complex_phrases
import create_and_analiz_img

import heroes
import color_text as myCt
from heroes import Hero, Activ

conf_ = 0.95
par_conf = 0.799
conf_mobs = 0.99
energy_availability = 1
number_tasks = 1
variable = None

find = {
    'name': 'def',
    'name_kikimora': find_img.find_name_kikimora(),
}


def wait_skip_battle_button():
    # print('station_master.wait_skip_battle_button()')
    skip_battle = find_img.find_skip_battle()
    while not skip_battle:
        skip_battle = find_img.find_skip_battle()


def mob_indicator():
    grey_rat = ['name1_grey_rat', 'серая крыса']
    white_rat = ['name1_white_rat', 'белая крыса']
    black_rat = ['name1_black_rat', 'черная крыса']
    sand_rat = ['name1_sand_rat', 'песчаная крыса']
    spy = ['name2_spy', 'шпион']
    smuggler = ['name3_smuggler', 'контрабандист']
    arachne = ['name4_arachne', 'араха']
    wildman = ['name5_wildman', 'дикарь']
    kikimora = ['name6_kikimora', 'кикимора']
    raptor = ['name7_raptor', 'ящер']
    list_mob = [grey_rat, white_rat, black_rat, sand_rat, spy,
                smuggler, arachne, wildman, kikimora, raptor]
    mob, name = False, False
    for mob, name in list_mob:
        mob_png = f'img/tonelli/mobi/{mob}.png'
        mob_id = fun.locCenterImg(mob_png)
        if mob_id:
            break
    return mob, name


def enemy_battle(prolong_=2.0, dog_activ=True, add_up=True, arena=False, tour=False):
    """

    :param prolong_:
    :param dog_activ:
    :param add_up:
    :param arena:
    :param tour: Для учета мобов в тоннелях используется True
    :return:
    """
    print(color_text.tc_green('в бой'))
    fun.my_log_file(f'')
    fun.my_log_file('station_master.enemy_battle()')
    # fun.my_log_file(' поиск battle_end, skip_battle, dog')
    # print('station_master.enemy_battle()')

    heroes.nam += 1

    battle_end = find_img.find_b_battle_end(confidence_param=par_conf)
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
    name6_kikimora = find_img.find_name_kikimora()
    name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

    duration_fight = 0
    dog_flag = True
    skip_battle_count = True
    mob_identified = None
    count_mob_identified = 0
    cycle = True
    result = None
    while not battle_end:
        if add_up:
            while not mob_identified and count_mob_identified <= 3:
                count_mob_identified += 1
                if name1_grey_rat and cycle:
                    cycle = False
                    Hero.app_rat(Activ.hero_activ)

                    print(myCt.tc_magenta(f'{Hero.get_qty_grey_rat(Activ.hero_activ)} серая крыса'))
                    mob_identified = 'grey_rat'
                if name1_black_rat and cycle:
                    cycle = False
                    mob_identified = 'black_rat'

                    print(myCt.tc_magenta('черная крыса'))
                if name1_white_rat and cycle:
                    cycle = False
                    # увеличение счетчика
                    Hero.app_white_rat(Activ.hero_activ)
                    mob_identified = 'white_rat'

                    print(myCt.tc_magenta(f'{Hero.get_qty_white_rat(Activ.hero_activ)} белая крыса'))
                    print(complex_phrases.report_white_rat(hero=Activ.hero_activ))
                if name1_sand_rat and cycle:
                    cycle = False
                    mob_identified = 'sand_rat'

                    print(myCt.tc_magenta('песчаная крыса'))
                if name2_spy and cycle:
                    cycle = False
                    mob_identified = 'spy'

                    print(myCt.tc_magenta('шпион пойман'))
                if name3_smuggler and cycle:
                    cycle = False
                    mob_identified = 'smuggler'

                    print(myCt.tc_magenta('контрабандист пойман'))
                if name4_arachne and cycle:
                    cycle = False
                    if tour:
                        Hero.app_arachne(Activ.hero_activ)

                    print(myCt.tc_magenta(f'{Hero.get_qty_arachne(Activ.hero_activ)} арахна'))
                    mob_identified = 'arachne'

                if name5_wildman and cycle:
                    cycle = False

                    print(f'{Hero.get_report_wildman_now(Activ.hero_activ)}')
                    print(complex_phrases.report_wildman(hero=Activ.hero_activ))
                    mob_identified = "wildman"

                if name6_kikimora and cycle:
                    cycle = False
                    if tour:
                        Hero.app_kiki(Activ.hero_activ)

                    print(myCt.tc_magenta(f'{Hero.get_qty_kiki(Activ.hero_activ)} кикимора'))
                    mob_identified = 'kikimora'

                if name7_raptor and cycle:
                    cycle = False
                    if tour:
                        Hero.app_raptor(Activ.hero_activ)

                    print(myCt.tc_magenta(f'{Hero.get_qty_raptor(Activ.hero_activ)} ящер'))
                    mob_identified = 'raptor'
                # нужен ли тут этот блок?
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
                name6_kikimora = find_img.find_name_kikimora()
                name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

        if dog_activ:
            if dog and dog_flag:
                # нажать "на собаку"
                dog_flag = False
                dog = fun.locCenterImg(name_img='img/dog_2.png', confidence=par_conf)
                fun.Mouse.move_to_click(pos_click=dog, move_time=0.1, z_p_k=0.1,
                                        message=True, message_l='нажал на собаку')
        if skip_battle and skip_battle_count:
            duration_fight += 1
        if skip_battle and skip_battle_count and duration_fight == 4:  # нажать "пропустить бой"
            skip_battle_count = False
            # print('нажать "пропустить бой"')
            skip_battle = fun.wait_static_pos(name_img='img/skip_battle.png', confidence=par_conf,
                                              message=True ,message_l='пропустить бой')

            fun.my_log_file(f'{skip_battle=}')
            fun.Mouse.move_to_click(pos_click=skip_battle, move_time=0.4, z_p_k=0.5,
                                    message=True, message_l='нажал пропустить бой')

        sleep(1 * prolong_)  # для задержки нажатия "пропустить бой"
        fun.my_log_file('ожидание battle_end, close, dog, skip_battle')
        fun.my_log_file(f'')

        battle_end = find_img.find_b_battle_end(confidence_param=par_conf)
        if battle_end:
            fun.Mouse.move(pos=battle_end, speed=1)
        close = find_img.find_close()

        name1_grey_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_grey_rat.png', confidence=conf_mobs)
        name1_white_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_white_rat.png', confidence=conf_mobs)
        name1_black_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_black_rat.png', confidence=conf_mobs)
        name1_sand_rat = fun.locCenterImg(name_img='img/tonelli/mobi/name1_sand_rat.png', confidence=conf_mobs)
        name2_spy = fun.locCenterImg(name_img='img/tonelli/mobi/name2_spy.png', confidence=conf_mobs)
        name3_smuggler = fun.locCenterImg(name_img='img/tonelli/mobi/name3_smuggler.png', confidence=conf_mobs)
        name4_arachne = fun.locCenterImg(name_img='img/tonelli/mobi/name4_arachne.png', confidence=conf_mobs)
        name5_wildman = fun.locCenterImg(name_img='img/tonelli/mobi/name5_wildman.png', confidence=conf_mobs)
        name6_kikimora = find_img.find_name_kikimora()
        name7_raptor = fun.locCenterImg(name_img='img/tonelli/mobi/name7_raptor.png', confidence=conf_mobs)

        dog = fun.locCenterImg('img/dog.png', confidence=par_conf)
        skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)

        if battle_end and close:  # нажать закрыть в конце боя
            victory = fun.locCenterImg('img/arena/overall/victory_in_arena.png', confidence=par_conf)
            defeat = fun.locCenterImg('img/arena/overall/defeat_in_arena.png', confidence=par_conf)
            if victory:
                result = "победа"
            elif defeat:
                result = "поражение"
            fun.my_log_file("нажать закрыть в конце боя")
            fun.push_close_all_(speed_mouse=0.3)
            # sleep(0)

    skip_battle1_end_ver = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
    fun.my_log_file(f'{skip_battle1_end_ver=}')
    while skip_battle1_end_ver:
        fun.push_close()
        skip_battle1_end_ver = fun.locCenterImg('img/skip_battle.png', confidence=par_conf)
        fun.my_log_file(f'{skip_battle1_end_ver=}')

    if not arena:
        solid_memory.save_all_state_config(info=False)

    fun.my_log_file("выход из 'enemy_battle")
    print(color_text.tc_green(f'выход из "enemy_battle" {result}'))
    return result


def press_en(*, task_number, pos, value_energy):  # , report_en=True
    """
    Args:
        task_number (int): номер строки заданий
        pos ( list[int]): регион его расположения
        value_energy (int): количество энергии нужной для задания
        :param task_number:
        :param pos: 
        :param value_energy: 
        # :param report_en:
    """
    fun.my_log_file(f'')
    fun.my_log_file("station_master.press_en()")
    global energy_availability, conf_
    x = pos[0] - 100
    y = pos[1] - 20
    pos_clik = x, y
    fun.Mouse.move(pos=pos_clik)
    # print('тут должен быть клик')                                        # для отладки раскомментировать
    fun.Mouse.move_to_click(pos_click=pos_clik, move_time=0.4, z_p_k=1.5, message=True, message_l='нажал задание')  # для отладки закомментировать
    sleep(0.5)
    low_energy = find_img.find_low_energy_label()
    if not low_energy:
        vers_in_print = "" if conf_ == 0.95 else f', conf_={conf_}. '
        # увеличение счетчиков
        Hero.app_energy_count_today(Activ.hero_activ, value_energy)
        if value_energy == 4:
            Hero.app_arachne(Activ.hero_activ)
        if value_energy == 5:
            if Hero.get_qty_wildman(Activ.hero_activ) == 'x':
                Hero.zero_wildman(Activ.hero_activ)
            Hero.app_wildman(Activ.hero_activ)
        if value_energy == 6:
            Hero.app_kiki(Activ.hero_activ)
        if value_energy == 7:
            Hero.app_raptor(Activ.hero_activ)

        # print(f'{Activ.station_activ=}')

        ## Выполняю {3} задание,{ conf_=0.94}. Сейчас {3}, сегодня 20, всего 120
        complex_phrases.display_report_energy_now(vers_in_print=vers_in_print,
                                                  value_energy=value_energy)
        solid_memory.save_all_state_config(info=False)
        # Жду появления кнопки "пропустить бой"
        wait_skip_battle_button()
        #
        enemy_battle()
        energy_availability = 1  # для выполнения всех заданий
        # energy_availability = 0 # для выполнения одного задания
    else:
        energy_availability = 0
        # if report_en:
        #     print(' Энергия закончилась!!')

        if Hero.get_qty_wildman(Activ.hero_activ) == 'x':
            Hero.zero_wildman(Activ.hero_activ)

        print(Hero.get_report_wildman_now(Activ.hero_activ))
        if Hero.get_wildman_count(Activ.hero_activ) != 0:
            print(complex_phrases.report_wildman(hero=Activ.hero_activ))
        else:
            print()
        sleep(1)
        close = find_img.find_close()
        while close:
            close = find_img.find_close()
            if close:
                # print(f'station_master.press_en {close=}')
                fun.Mouse.move_to_click(pos_click=close, z_p_k=0.5, message=True, message_l='нажал закрыть')


def task_analysis(img1, img2, region):
    """
    При анализе через картинки получает их имена и region= поиска
    :param img1: *.png
    :param img2: *.png
    :param region: tuple[Point, int] | tuple[None, None]
    :return: Point, int | None
    """
    fun.my_log_file('station_master.task_analysis()')
    global variable
    # fun.push_close_all_()
    fun.vizit_to_station_master()
    variant1 = fun.locCenterImg(name_img=img1, confidence=conf_, region=region)
    # v3 = pyautogui.locateCenterOnScreen(img2, minSearchTime=1.0, region=region, confidence=conf_)
    variant2 = fun.locCenterImg(name_img=img2, confidence=conf_, region=region)
    if variant1:
        price_task = fun.extraction_digit(item=img1)
        return variant1, price_task
    elif variant2:
        variable = variant2
        price_task = fun.extraction_digit(item=img2)
        return variant2, price_task
    else:
        return None, None


def move(pos , message=True, message_l=None):
    fun.my_log_file('station_master.move()')
    if message:
        print(f'station_master.move() {pos=}')
    if pos:
        fun.Mouse.move(pos=pos, speed=0.5)
        sleep(1)


def station_task_list():
    fun.my_log_file("station_master.station_task_list()")
    """ Получение списка заданий """
    station = fun.loc_now()
    task_list = (station[4])
    return task_list


def option_task_money(report_en=True):
    fun.my_log_file("station_master.option_task_money()")
    # print('station_master.option_task_money')
    global energy_availability, number_tasks  # , conf_
    # price_task = None
    conf_ = 0.95

    # определяю локацию
    fun.push_close_all_()
    list_location = fun.loc_now()
    # получаю список доступных заданий
    task = list_location[4]

    heroes.Activ.station_activ = list_location[0]

    if heroes.Activ.station_activ == 'ст. Киевская':
        if Activ.hero_activ == '':
            fun.selection_hero()
        heroes.Hero.set_wild_activ(Activ.hero_activ)
    hero = fun.selection_hero()
    # получаю путь заданий героя
    if hero:
        path = Hero.get_path_task(Activ.hero_activ)
        # print(f'{path=}')
    else:
        return
    while energy_availability == 1 and number_tasks > 0:
        region_1, region_2, region_3 = fun.get_areas_task_big()

        variant1, price_task1 = task_analysis(F'{path}{task[0]}', F'{path}{task[1]}', region_1)
        # print(f'{variant1=}, {price_task1=}')
        fun.Mouse.move(pos=variant1)
        sleep(0.1)

        variant2, price_task2 = task_analysis(F'{path}{task[2]}', F'{path}{task[3]}', region_2)
        # print(f'{variant2}, {price_task2=}')
        fun.Mouse.move(pos=variant2)
        sleep(0.1)

        variant3, price_task3 = task_analysis(F'{path}{task[4]}', F'{path}{task[5]}', region_3)
        # print(f'{variant3}, {price_task3=}')
        fun.Mouse.move(pos=variant3)
        sleep(0.1)

        if variant1:
            press_en(task_number=1, pos=region_1, value_energy=price_task1)
        elif variant2:
            press_en(task_number=2, pos=region_2, value_energy=price_task2)
        if variant3:
            press_en(task_number=3, pos=region_3, value_energy=price_task3)

        if variant1 == variant2 == variant3:
            print(F'confidence={conf_}')
            conf_ -= 0.005
            conf_ = round(conf_, 3)

        if conf_ <= 0.92:
            print(myCt.tc_cyan(
                'задания не найдены, результаты "D:\\bot in br\\testOCR\\img\\test\\test_tasks\\test big tasks" '))
            create_and_analiz_img.get_screenshot_task_big()
            number_tasks = 1
            energy_availability = 0
            return
            # [create_and_analiz_img.analiz_task(target='auto')
            # number_tasks = 1
            # energy_availability = 1
            # return]

    number_tasks = 1
    energy_availability = 1
    close = find_img.find_close()
    while close:
        fun.Mouse.move_to_click(pos_click=close, z_p_k=0.3)
        close = find_img.find_close()


def task_pos_item(task_num):
    """ Выбор по позиции задания """
    fun.selection_hero()
    list_location = fun.loc_now()
    heroes.Activ.station_activ = list_location[0]
    global energy_availability, number_tasks  # , conf_
    region_1, region_2, region_3 = fun.get_areas_task_big()
    if task_num == 1:
        region = region_1
    elif task_num == 2:
        region = region_2
    else:
        region = region_3

    while energy_availability == 1 and number_tasks > 0:
        # fun.push_close_all_(speed_mouse=0.75)
        fun.vizit_to_station_master()
        press_en(task_number=task_num, pos=region, value_energy=1)
    print(myCt.tc_green(' Задания выполнены'))
    number_tasks = 1
    energy_availability = 1
    close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
    # print(f'station_master.task_pos_item {close=}')
    while close:
        print(f'station_master.task_pos_item {close=}')
        fun.Mouse.move_to_click(pos_click=close, z_p_k=0.3)
        close = fun.locCenterImg(name_img='img/overall/close.png', confidence=0.9)
