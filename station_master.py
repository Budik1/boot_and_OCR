""" Точки для отладки в press_en()"""
import os
from time import sleep

import fun
import find_img
import os_action
import solid_memory
import create_and_analiz_task_img

import tools
import heroes
from tools import color_text as c_t
from heroes import Hero, Activ


conf_ = 0.95
par_conf = 0.799
conf_mobs = 0.99
energy_availability = 1
number_tasks = 1
variable = None
target_name = 'smol'

find = {
    'name': 'def',
    'name_kikimora': find_img.find_name6_kikimora(),
}


def wait_skip_battle_button():
    fun.log_with_caller(message='a')
    skip_battle = find_img.find_skip_battle()
    while not skip_battle:
        skip_battle = find_img.find_skip_battle()
    fun.log_with_caller(message='e')


def enemy_battle(prolong_=2.0, dog_activ=True, add_up=True, arena=False, tour=False) -> str:
    """

    :param prolong_:
    :param dog_activ:
    :param add_up:
    :param arena:
    :param tour: Для учета мобов в тоннелях используется True
    :return: "победа" или "поражение"
    """
    fun.log_with_caller(message='a')
    log_pet = False
    heroes.nam += 1

    battle_end = find_img.find_b_battle_end(confidence_param=par_conf)
    skip_battle = find_img.find_skip_battle()
    dog = find_img.find_dog_2(par_conf_=0.79)

    name1_grey_rat = find_img.find_name1_grey_rat()
    name1_white_rat = find_img.find_name1_white_rat()
    name1_black_rat = find_img.find_name1_black_rat()
    name1_sand_rat = find_img.find_name1_sand_rat()
    name2_spy = find_img.find_name2_spy()
    name3_smuggler = find_img.find_name3_smuggler()
    name4_arachne = find_img.find_name4_arachne()
    name5_wildman = find_img.find_name5_wildman()
    name6_kikimora = find_img.find_name6_kikimora()
    name7_raptor = find_img.find_name7_raptor()

    duration_fight = 0
    dog_flag = True
    skip_battle_count = True
    mob_identified = None
    count_mob_identified = 0
    cycle = True
    result = None
    phrase = ''
    to_say = False # Поменять на True если фраза не пуста
    while not battle_end:
        if add_up:
            while not mob_identified and count_mob_identified <= 3:
                count_mob_identified += 1
                if name1_grey_rat and cycle:
                    cycle = False
                    mob_identified = 'grey_rat'
                    Hero.app_rat(Activ.hero_activ)
                    text = f'{Hero.get_qty_grey_rat(Activ.hero_activ)} серая крыса'
                    print(c_t.tc_magenta(text=text))
                    fun.pr_in_file(text=text, mod_name=target_name)

                if name1_black_rat and cycle:
                    cycle = False
                    mob_identified = 'black_rat'
                    text = 'черная крыса'
                    print(c_t.tc_magenta(text=text))
                    fun.pr_in_file(text=text, mod_name=target_name)

                if name1_white_rat and cycle:
                    cycle = False
                    mob_identified = 'white_rat'
                    # увеличение счетчика
                    Hero.app_white_rat(Activ.hero_activ)
                    text_1 = f'{Hero.get_qty_white_rat(Activ.hero_activ)} белая крыса'
                    print(c_t.tc_magenta(text=text_1))
                    fun.pr_in_file(text=text_1, mod_name=target_name)
                    text_2_c = tools.report_white_rat_c(hero=Activ.hero_activ)
                    text_2_g = tools.report_white_rat_bw(hero=Activ.hero_activ)

                    print(text_2_c)
                    fun.pr_in_file(text=text_2_g, mod_name=target_name)

                if name1_sand_rat and cycle:
                    cycle = False
                    mob_identified = 'sand_rat'
                    text = 'песчаная крыса'
                    print(c_t.tc_magenta(text=text))
                    fun.pr_in_file(text=text, mod_name=target_name)

                if name2_spy and cycle:
                    cycle = False
                    mob_identified = 'spy'
                    phrase = 'шпион пойман'
                    to_say = True

                    print(c_t.tc_magenta(text=phrase))
                    fun.pr_in_file(text=phrase, mod_name=target_name)

                if name3_smuggler and cycle:
                    cycle = False
                    mob_identified = 'smuggler'
                    phrase = 'контрабандист пойман'
                    to_say = True

                    print(c_t.tc_magenta(text=phrase))
                    fun.pr_in_file(text=phrase, mod_name=target_name)

                if name4_arachne and cycle:
                    cycle = False
                    mob_identified = 'arachne'
                    if tour:
                        Hero.app_arachne(Activ.hero_activ)
                    ph1 = 'арахна'
                    ph2 = Hero.get_qty_arachne(Activ.hero_activ)
                    phrase = f'{ph2} {ph1} '
                    to_say = True
                    print(c_t.tc_magenta(text=phrase))
                    fun.pr_in_file(text=phrase, mod_name=target_name)

                if name5_wildman and cycle:
                    cycle = False
                    mob_identified = "wildman"
                    ph1 = "дикарь пойман"
                    ph2 = Hero.get_report_wildman_now(Activ.hero_activ)
                    text_c = f'{c_t.tc_magenta(ph1)},{c_t.tc_yellow(str(ph2[0]))}, {c_t.tc_green(ph2[1])}'
                    phrase = ph1 + str(ph2[0]) + ph2[1]
                    to_say = True
                    print(text_c)
                    fun.pr_in_file(text=phrase, mod_name=target_name)


                if name6_kikimora and cycle:
                    cycle = False
                    mob_identified = 'kikimora'
                    if tour:
                        Hero.app_kiki(Activ.hero_activ)
                    text_g = f'{Hero.get_qty_kiki(Activ.hero_activ)} кикимора'
                    print(c_t.tc_magenta(text_g))
                    fun.pr_in_file(text=text_g, mod_name=target_name)

                if name7_raptor and cycle:
                    cycle = False
                    mob_identified = 'raptor'
                    if tour:
                        Hero.app_raptor(Activ.hero_activ)
                    ph1 = Hero.get_qty_raptor(Activ.hero_activ)
                    ph2 = 'ящер'
                    phrase = ph1, ph2
                    to_say = True
                    text = f'{ph1} {ph2}'
                    print(c_t.tc_magenta(text=text))
                    fun.pr_in_file(text=text, mod_name=target_name)

                if to_say:
                    tools.sounds.say_txt(phrase=phrase)
                    to_say = False
                # нужен ли тут этот блок?
                name1_grey_rat = find_img.find_name1_grey_rat()
                name1_white_rat = find_img.find_name1_white_rat()
                name1_black_rat = find_img.find_name1_black_rat()
                name1_sand_rat = find_img.find_name1_sand_rat()
                name2_spy = find_img.find_name2_spy()
                name3_smuggler = find_img.find_name3_smuggler()
                name4_arachne = find_img.find_name4_arachne()
                name5_wildman = find_img.find_name5_wildman()
                name6_kikimora = find_img.find_name6_kikimora()
                name7_raptor = find_img.find_name7_raptor()

        if dog_activ:
            if dog and dog_flag:
                # нажать "на собаку"
                par_conf_pet = par_conf
                mes_pet = f'обнаружение пета {dog=}, {par_conf_pet=}'
                dog_flag = False
                dog = find_img.find_dog_2(par_conf_=par_conf_pet)
                if dog:
                    mes_pet = f'обнаружение пета {dog=}, {par_conf_pet=}'
                    while dog and dog[0] > 800:
                        par_conf_pet += 0.001
                        dog = find_img.find_dog_2(par_conf_=par_conf_pet)
                        mes_pet = f'обнаружение пета {dog=}, {par_conf_pet=}'
                        if par_conf_pet > 0.999:
                            dog = None
                            break
                if dog:
                    tools.Mouse.move_to_click(pos_click=dog, speed=0.1, z_p_k=0.1,
                                              message=f'нажал на собаку {dog=}')
                    mes_pet = f'обнаружение пета {dog=}, {par_conf_pet=}'
                if log_pet:
                    print(mes_pet)
                    fun.pr_in_file(text=mes_pet, mod_name=target_name)
        if skip_battle and skip_battle_count:
            duration_fight += 1
        if skip_battle and skip_battle_count and duration_fight == 4:  # нажать "пропустить бой"
            skip_battle_count = False
            # print('нажать "пропустить бой"')
            skip_battle = find_img.find_skip_battle()

            fun.my_log_file(f'{skip_battle=}')
            tools.Mouse.move_to_click(pos_click=skip_battle, speed=0.4, z_p_k=0.5,
                                      message='нажал пропустить бой')

        sleep(1 * prolong_)  # для задержки нажатия "пропустить бой"
        fun.my_log_file('ожидание battle_end, close, dog, skip_battle')
        fun.my_log_file(f'')

        battle_end = find_img.find_b_battle_end(confidence_param=par_conf)
        if battle_end:
            tools.Mouse.move(pos=battle_end, speed=1)
        close = find_img.find_close()

        name1_grey_rat = find_img.find_name1_grey_rat()
        name1_white_rat = find_img.find_name1_white_rat()
        name1_black_rat = find_img.find_name1_black_rat()
        name1_sand_rat = find_img.find_name1_sand_rat()
        name2_spy = find_img.find_name2_spy()
        name3_smuggler = find_img.find_name3_smuggler()
        name4_arachne = find_img.find_name4_arachne()
        name5_wildman = find_img.find_name5_wildman()
        name6_kikimora = find_img.find_name6_kikimora()
        name7_raptor = find_img.find_name7_raptor()

        dog = find_img.find_dog_2(par_conf_=0.99)
        skip_battle = find_img.find_skip_battle()

        if battle_end and close:  # нажать закрыть в конце боя
            victory = find_img.find_victory_in_arena()
            defeat = find_img.find_defeat_in_arena()
            if victory:
                result = "победа"
            elif defeat:
                result = "поражение"
            fun.my_log_file("нажать закрыть в конце боя")
            fun.push_close_all_(speed_mouse=0.3)
            # sleep(0)
        if close:
            popup = fun.close_popup_window()
            if popup:
                fun.push_close_all_()

    skip_battle1_end_ver = find_img.find_skip_battle()
    fun.my_log_file(f'{skip_battle1_end_ver=}')
    while skip_battle1_end_ver:
        fun.push_close()
        skip_battle1_end_ver = find_img.find_skip_battle()
        fun.my_log_file(f'{skip_battle1_end_ver=}')
    if arena:
        mes = f'{result} выход'
    else:
        mes = f' выход'
        solid_memory.save_all_state_config_json(info=False)
    fun.log_with_caller(message=mes)
    return result


def press_en(*, task_number, pos, value_energy):  #
    """
    Args:
        task_number (int): номер строки заданий
        pos ( list[int]): регион его расположения
        value_energy (int): количество энергии нужной для задания
        :param task_number :
        :param pos: 
        :param value_energy:
    """
    fun.log_with_caller(message='a')
    global energy_availability, conf_
    x = pos[0] - 70
    y = pos[1] - 20
    pos_clik = x, y
    # tools.Mouse.move(pos=pos_clik, message=f'показал выбранное задание ({task_number})')
    # print('тут должен быть клик')                                        # для отладки раскомментировать
    tools.Mouse.move_to_click(pos_click=pos_clik, speed=0.4, z_p_k=0.3,
                              message=f'нажал {task_number} задание')  # для отладки закомментировать
    # sleep(0.5)
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

        text_report_color = tools.report_energy_now_color(vers_in_print=vers_in_print, value_energy=value_energy)
        print(text_report_color)
        text_report_bw = tools.report_energy_now_bw(vers_in_print=vers_in_print, value_energy=value_energy)
        fun.pr_in_file(text=text_report_bw, mod_name=target_name)
        solid_memory.save_all_state_config_json(info=False)
        # Жду появления кнопки "пропустить бой"
        wait_skip_battle_button()
        #
        enemy_battle()

        energy_availability = 1  # для выполнения всех заданий
        # energy_availability = 0 # для выполнения одного задания
    else:
        energy_availability = 0

        if Hero.get_qty_wildman(Activ.hero_activ) == 'x':
            Hero.zero_wildman(Activ.hero_activ)
        ph2_0, ph2_1 = Hero.get_report_wildman_now(Activ.hero_activ)
        if ph2_1:
            text = f'{c_t.tc_yellow(str(ph2_0))}, {c_t.tc_green(ph2_1)}'
        else:
            text = f'{c_t.tc_yellow(str(ph2_0))}'
        print(text)
        fun.pr_in_file(text=f'{ph2_0}, {ph2_1}', mod_name=target_name)
        if Hero.get_wildman_count(Activ.hero_activ) != 0:
            text_c = tools.report_wildman_c(hero=Activ.hero_activ)
            text_bw = tools.report_wildman_bw(hero=Activ.hero_activ)
            print(text_c)
            fun.pr_in_file(text=text_bw, mod_name=target_name)
        else:
            print()
            fun.pr_in_file(text='', mod_name=target_name)
        sleep(1)
        close = find_img.find_close()
        while close:
            close = find_img.find_close()
            if close:
                tools.Mouse.move_to_click(pos_click=close, z_p_k=0.5, message='нажал закрыть')
    fun.log_with_caller(message='e')
    return


def task_analysis(img1, img2, region):
    """
    При анализе через картинки получает их имена и region= поиска
    :param img1: *.png
    :param img2: *.png
    :param region: tuple[Point, int] | tuple[None, None]
    :return: Point, int | None
    """
    fun.log_with_caller(message='a')
    global variable
    # fun.push_close_all_()
    fun.vizit_to_station_master()
    # print(f'{img1=}')
    # print(f'{img2=}')

    img1_alt_split = img1.split('.')
    img1_alt_split[0] += 'event'
    img1_alt = '.'.join(img1_alt_split)

    img2_alt_split = img2.split('.')
    img2_alt_split[0] += 'event'
    img2_alt = '.'.join(img2_alt_split)

    variant1 = find_img.find_img_param(path_name=img1, confidence=conf_, region=region)
    img_1a = os_action.check_folder_or_file(my_path=img1_alt)
    if not variant1 and img_1a:
        variant1 = find_img.find_img_param(path_name=img1_alt, confidence=conf_, region=region)
    variant2 = find_img.find_img_param(path_name=img2, confidence=conf_, region=region)
    img_2a = os_action.check_folder_or_file(my_path=img2_alt)
    if not variant2 and img_2a:
        variant2 = find_img.find_img_param(path_name=img2_alt, confidence=conf_, region=region)
    if variant1:
        price_task = fun.extraction_digit(item=img1)
        val_1 = variant1
        val_2 = price_task
    elif variant2:
        price_task = fun.extraction_digit(item=img2)
        variable = variant2
        val_1 = variant2
        val_2 = price_task
    else:
        val_1 = None
        val_2 = None
    fun.log_with_caller(message='e')
    return val_1, val_2



def station_task_list():
    """ Получение списка заданий """
    fun.log_with_caller(message='a')
    station = fun.loc_now()
    task_list = (station[4])
    fun.log_with_caller(message='e')
    return task_list


def option_task_money():
    fun.log_with_caller(message='a')
    global energy_availability, number_tasks  # , conf_
    # price_task = None
    conf_ = 0.95
    # определяю локацию
    fun.push_close_all_()
    fun.selection_hero(show_name=False)
    list_location = fun.loc_now()
    # получаю список доступных заданий
    task = list_location[4]

    heroes.Activ.station_activ = list_location[0]

    if heroes.Activ.station_activ == 'ст. Киевская':
        if not Activ.hero_activ:
            fun.selection_hero()
        heroes.Hero.app_wildman_days_count(heroes.Activ.hero_activ)
    hero = fun.selection_hero()
    # получаю путь заданий героя
    if hero:
        path = Hero.get_path_task(Activ.hero_activ)
    else:
        return
    while energy_availability == 1 and number_tasks > 0:
        # Проверка на доступность палатки начстанции. Возможно собрана коллекция
        tent_open = fun.find_link_station_master_alt()
        while not tent_open:
            fun.push_close_all_()
            tools.sounds.say_txt('Возможно собрана коллекция')
            tent_open = fun.find_link_station_master_alt()

        region_1, region_2, region_3 = fun.get_full_areas_task()

        variant1, price_task1 = task_analysis(F'{path}{task[0]}', F'{path}{task[1]}', region_1)
        tools.Mouse.move(pos=variant1)
        # sleep(0.1)

        variant2, price_task2 = task_analysis(F'{path}{task[2]}', F'{path}{task[3]}', region_2)
        tools.Mouse.move(pos=variant2)
        # sleep(0.1)

        variant3, price_task3 = task_analysis(F'{path}{task[4]}', F'{path}{task[5]}', region_3)
        tools.Mouse.move(pos=variant3)
        # sleep(0.1)

        if variant1:
            press_en(task_number=1, pos=region_1, value_energy=price_task1)
        elif variant2:
            press_en(task_number=2, pos=region_2, value_energy=price_task2)
        if variant3:
            press_en(task_number=3, pos=region_3, value_energy=price_task3)

        if variant1 == variant2 == variant3:
            text = F'confidence={conf_}'
            print(text)
            fun.pr_in_file(text=text, mod_name=target_name)

            conf_ -= 0.005
            conf_ = round(conf_, 3)

        if conf_ <= 0.935:
            # # получение картинки
            text = 'Попытка прочитать аппаратно'
            print(text)
            fun.pr_in_file(text=text, mod_name=target_name)
            analiz = create_and_analiz_task_img.search_and_create_img_best_offer(person_identified=True)

            conf_ = 0.95
            if not analiz:
                path = create_and_analiz_task_img.get_imgs_task_big_manual_select()
                full_path = f'C:/python/bot_ocr1/{path}'
                print(c_t.tc_cyan(f'Для ручного выбора результат "{full_path}" '))
                os.startfile(full_path)
                #
                number_tasks = 1
                energy_availability = 0
                return
            # return
    number_tasks = 1
    energy_availability = 1
    close = find_img.find_close()
    while close:
        tools.Mouse.move_to_click(pos_click=close, z_p_k=0.3)
        close = find_img.find_close()
    tools.sounds.say_txt('Задания выполнены.')
    fun.log_with_caller(message='e')
    return


def option_task_line(*, task_line):
    """ Выбор по позиции задания """
    fun.log_with_caller(message='a')
    # print(f'{task_line=}, {type(task_line)}')
    fun.selection_hero()
    list_location = fun.loc_now()
    heroes.Activ.station_activ = list_location[0]
    global energy_availability, number_tasks
    region_1, region_2, region_3 = fun.get_areas_task_big()
    if task_line == 1:
        region = region_1
    elif task_line == 2:
        region = region_2
    else:
        region = region_3

    while energy_availability == 1 and number_tasks > 0:
        fun.vizit_to_station_master()
        # нужно получить значение потраченной энергии
        en_value = create_and_analiz_task_img.get_energy_value_in_line(line=task_line - 1)
        press_en(task_number=task_line, pos=region, value_energy=en_value)
    text_g = ' Задания выполнены'
    print(c_t.tc_green(text=text_g))
    fun.pr_in_file(text=text_g, mod_name=target_name)
    number_tasks = 1
    energy_availability = 1
    close = find_img.find_close()
    while close:
        print(f'station_master.task_pos_item {close=}')
        tools.Mouse.move_to_click(pos_click=close, z_p_k=0.3)
        close = find_img.find_close()
    fun.log_with_caller(message='e')
    return
