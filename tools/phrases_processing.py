"""
Сложные сообщения
"""
import tools
import heroes
import tools.color_text as c_t


def report_energy_now_color(*, vers_in_print, value_energy):
    """
    Пример сообщения:
    "{3} задание,{ conf_=0.94}. Сейчас {3}, сегодня {20}, всего/на Киевской {120}/{12}"
    Args:
        vers_in_print (str): пробел или значение {conf_=}
        value_energy (int): количество энергии потраченной на задание
    """
    text_g = (f'{vers_in_print}'  # {task_number} задание
              f'Сейчас {value_energy}, '
              f'сегодня {heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)}, '
              f'всего/на Киевской: {heroes.Hero.get_energy_count_all(heroes.Activ.hero_activ)}/'
              f'{heroes.Hero.get_energy_kiev_count_all(heroes.Activ.hero_activ)}')
    return c_t.tc_blue(text_g)


def report_energy_now_bw(*, vers_in_print, value_energy):
    """
    Пример сообщения:
    "{3} задание,{ conf_=0.94}. Сейчас {3}, сегодня {20}, всего/на Киевской {120}/{12}"
    Args:
        vers_in_print (str): пробел или значение {conf_=}
        value_energy (int): количество энергии потраченной на задание
    """
    text_g = (f'{vers_in_print}'  # {task_number} задание
              f'Сейчас {value_energy}, '
              f'сегодня {heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)}, '
              f'всего/на Киевской: {heroes.Hero.get_energy_count_all(heroes.Activ.hero_activ)}/'
              f'{heroes.Hero.get_energy_kiev_count_all(heroes.Activ.hero_activ)}')
    return text_g


def set_inspect_report():
    fraze = 'Чего их еще раз шмонать? Сегодня всё уже найдено.'
    return fraze


def display_info_energy_all_2():
    # найти значение длинны самого длинного имени
    len_name = []
    len_energy_count_today = []
    len_energy_count_all = []
    len_en_kiev = []
    len_dif = []
    for key in heroes.hero_dict:
        len_name.append(len(key))
        len_energy_count_today.append(len(str(heroes.Hero.get_energy_count_today(heroes.hero_dict[key]))))
        len_energy_count_all.append(len(str(heroes.Hero.get_energy_count_all(heroes.hero_dict[key]))))
        len_en_kiev.append(len(str(heroes.Hero.get_energy_kiev_count_all(heroes.hero_dict[key]))))
        len_dif.append(len(str(
            heroes.Hero.get_energy_count_all(heroes.hero_dict[key]) - heroes.Hero.get_energy_kiev_count_all(
                heroes.hero_dict[key]))))
        # len_dif_up_dif.append(len(str(heroes.Hero.get_dif_up_days(hero_dict[key]))))
    rjust_name = max(len_name)
    rjust_en_count_today = max(len_energy_count_today) + 1
    rjust_en_count_all = max(len_energy_count_all) + 1
    ljust_en_kiev = max(len_en_kiev) + 1
    ljust_dif = max(len_dif) + 1
    phrase_zagl_1 = 'Расход энергии'
    char0 = '    '
    char1 = '/'
    char2 = ' '
    len_now = 9
    len_all_ = 8
    print()
    # "Расход энергии"
    print(phrase_zagl_1)  #
    for key in heroes.hero_dict:
        # print(len(key))
        w_name = key.rjust(rjust_name, " ")
        energy_count_today = (str(heroes.Hero.get_energy_count_today(heroes.hero_dict[key])).
                              rjust(rjust_en_count_today, " "))
        energy_count_all = (str(heroes.Hero.get_energy_count_all(heroes.hero_dict[key])).
                            rjust(rjust_en_count_all, " "))
        w_now = "сегодня:".rjust(len_now, " ")
        w_all = 'всего:'.rjust(len_all_, ' ')
        en_kiev = (str(heroes.Hero.get_energy_kiev_count_all(heroes.hero_dict[key])).
                   ljust(ljust_en_kiev, ' '))
        dif = (str(int(energy_count_all) - int(en_kiev)).
               ljust(ljust_dif, ' '))

        print(f'{char0}{w_name}{w_now}{energy_count_today}{w_all}{energy_count_all}{char1}{en_kiev}{dif}{char2}')
    print()
    return


# def display_home_location_hero(*, her):
#     home_location = heroes.Hero.get_home_location(her)
#     print(home_location)
#     return home_location


def display_report_wildman():
    print()
    print('Дикари')

    for key in heroes.hero_dict:
        name = heroes.Hero.get_name_ru(heroes.hero_dict[key]).rjust(7, ' ')

        print(f'{name}:{report_wildman_c(hero=heroes.hero_dict[key])}')
    return


def display_report_w_rat():
    print()
    print('white rat')
    for key in heroes.hero_dict:
        name = heroes.Hero.get_name_ru(heroes.hero_dict[key]).rjust(7, ' ')

        print(f'{name}:{report_white_rat_c(hero=heroes.hero_dict[key])}')
    return


# def display_smol_report_wildman():
#     """
#     gady 0 дней, 0 дикарей
#     :return:
#     """
#     print()
#     for key in heroes.hero_dict:
#         name = key.rjust(8, ' ')
#         q_days = str(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])).rjust(3, ' ')
#         days = (tools.transform_word_days(qty_days=(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])))).rjust(
#             5,
#             ' ')
#         q_wild = str(heroes.Hero.get_wildman_count(heroes.hero_dict[key])).rjust(4)
#         wild = tools.transform_word_wilds(qty_wilds=heroes.Hero.get_wildman_count(heroes.hero_dict[key])).rjust(8)
#         print(f'{name}{q_days}{days}{q_wild}{wild}')
#
#     return


def display_smol_report_wildman_1():
    """
    gady 0 дней, 0 дикарей
    :return:
    """
    print()
    print('Wildman')
    char0 = '    '
    len_name = []
    len_q_days = []
    len_world_days = []
    len_q_wild = []
    len_world_wild = []
    for key in heroes.hero_dict:
        len_name.append(len(key))
        len_q_days.append(len(str(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key]))))
        len_world_days.append(
            len(tools.transform_word_days(qty_days=(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])))))
        len_q_wild.append(len(str(heroes.Hero.get_wildman_count(heroes.hero_dict[key]))))
        len_world_wild.append(
            len(tools.transform_word_wilds(qty_wilds=heroes.Hero.get_wildman_count(heroes.hero_dict[key]))))
    rjust_name = max(len_name)
    rjust_q_days = max(len_q_days) + 1
    rjust_world_days = max(len_world_days) + 1
    rjust_q_wild = max(len_q_wild) + 1
    rjust_world_wild = max(len_world_wild) + 1
    for key in heroes.hero_dict:
        name = key.rjust(rjust_name)
        q_days = str(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])).rjust(rjust_q_days)
        world_days = ((tools.transform_word_days(qty_days=(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])))).
                      rjust(rjust_world_days))
        q_wild = str(heroes.Hero.get_wildman_count(heroes.hero_dict[key])).rjust(rjust_q_wild)
        world_wild = tools.transform_word_wilds(qty_wilds=heroes.Hero.get_wildman_count(heroes.hero_dict[key])).ljust(
            rjust_world_wild)
        print(f'{char0}{name}{q_days}{world_days}{q_wild} {world_wild}')
    return


def report_white_rat_c(*, hero):
    #  Потрачено {} ед.эн.
    # {} эн на 1го.

    text_22 = c_t.tc_green(' Потрачено ')  # 'Потрачено '
    energy_w_rat_count_all = c_t.tc_yellow(f'{heroes.Hero.get_white_rat_energy(hero)}')  # 'XXX'
    text_23 = c_t.tc_green(' ед.эн.')
    phrase2 = f'{text_22}{energy_w_rat_count_all}{text_23}'

    # количество энергии на одного
    if heroes.Hero.get_white_rat_count_all(hero):
        qty_wr = str(heroes.Hero.get_white_rat_count_all(hero))
        val_all = c_t.tc_blue(qty_wr)
        phrase3 = f' {val_all} шт.'
        average_value_3 = c_t.tc_blue(
            f'{round(heroes.Hero.get_white_rat_energy(hero) / heroes.Hero.get_white_rat_count_all(hero), 4)}')  # '7'
        text_32 = c_t.tc_green(' эн на 1ну крысу.')  # ' эн на 1го'
        phrase1 = f'{average_value_3.rjust(17)}{text_32}'
        report_w_rat_hero = f'{phrase1}{phrase2}{phrase3}'
    else:
        phrase1 = 'Нет данных.'.rjust(19)
        report_w_rat_hero = f'{phrase1}{phrase2}'
    return report_w_rat_hero


def report_white_rat_bw(*, hero):
    #  Потрачено {} ед.эн.
    # {} эн на 1го.

    text_22 = ' Потрачено '  # 'Потрачено '
    energy_w_rat_count_all = f'{heroes.Hero.get_white_rat_energy(hero)}'  # 'XXX'
    text_23 = ' ед.эн.'
    phrase2 = f'{text_22}{energy_w_rat_count_all}{text_23}'

    # количество энергии на одного
    if heroes.Hero.get_white_rat_count_all(hero):
        qty_wr = str(heroes.Hero.get_white_rat_count_all(hero))
        val_all = qty_wr
        phrase3 = f' {val_all} шт.'
        average_value_3 = f'{round(heroes.Hero.get_white_rat_energy(hero) / heroes.Hero.get_white_rat_count_all(hero), 4)}'  # '7'
        text_32 = ' эн на 1ну крысу.'  # ' эн на 1го'
        phrase1 = f'{average_value_3.rjust(17)}{text_32}'
        report_w_rat_hero = f'{phrase1}{phrase2}{phrase3}'
    else:
        phrase1 = 'Нет данных.'.rjust(19)
        report_w_rat_hero = f'{phrase1}{phrase2}'
    return report_w_rat_hero


def report_wildman_c(*, hero):
    # {} эн на 1го.
    #  Потрачено {} ед.эн.

    text_22_g = ' Потрачено '
    text_22_c = c_t.tc_green(text_22_g)  # 'Потрачено '
    energy_kiev_count_all_g = f'{heroes.Hero.get_energy_kiev_count_all(hero)}'
    energy_kiev_count_all_c = c_t.tc_yellow(energy_kiev_count_all_g)  # 'XXX'
    text_23_g = ' ед.эн.'
    text_23_c = c_t.tc_green(text_23_g)
    phrase2_c = f'{text_22_c}{energy_kiev_count_all_c}{text_23_c}'

    # количество энергии на одного
    if heroes.Hero.get_wildman_count(hero):
        # text_31 = color_text.tc_green(' Это ')
        average_value_3_g = f'{round(heroes.Hero.get_energy_kiev_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}'
        average_value_3_c = c_t.tc_blue(average_value_3_g)  # '7'
        text_32_g = ' эн на 1го.'  # ' эн на 1го'
        text_32_c = c_t.tc_green(text_32_g)  # ' эн на 1го'
        phrase1_c = f'{average_value_3_c.rjust(17)}{text_32_c}'
        report_wildman_hero_color = f'{phrase1_c}{phrase2_c}'
    else:
        phrase1_g = 'Нет данных.'.rjust(19)
        phrase1_c = phrase1_g
        report_wildman_hero_color = f'{phrase1_c}{phrase2_c}'
    return report_wildman_hero_color


def report_wildman_bw(*, hero):
    # {} эн на 1го.
    #  Потрачено {} ед.эн.

    text_22_g = ' Потрачено '
    energy_kiev_count_all_g = f'{heroes.Hero.get_energy_kiev_count_all(hero)}'
    text_23_g = ' ед.эн.'
    phrase2_g = f'{text_22_g}{energy_kiev_count_all_g}{text_23_g}'

    # количество энергии на одного
    if heroes.Hero.get_wildman_count(hero):
        average_value_3_g = f'{round(heroes.Hero.get_energy_kiev_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}'
        text_32_g = ' эн на 1го.'  # ' эн на 1го'
        phrase1_g = f'{average_value_3_g.rjust(17)}{text_32_g}'
        report_wildman_hero_bw = f'{phrase1_g}{phrase2_g}'
    else:
        phrase1_g = 'Нет данных.'.rjust(19)
        report_wildman_hero_bw = f'{phrase1_g}{phrase2_g}'
    return report_wildman_hero_bw


def report_kv_efficiency_g():
    activ_her = heroes.Activ.hero_activ
    qty_all_victory = heroes.Hero.get_qty_duel_all_victory(activ_her)
    qty_all = heroes.Hero.get_qty_duel_all(activ_her)
    if qty_all:
        percent_vik_all = round((qty_all_victory / (qty_all / 100)), 1)
    else:
        percent_vik_all = 0
    vik_all = tools.transform_word_victory(qty_victory=qty_all_victory)
    word_duel_al = tools.transform_word_duel(qty_duel=qty_all)
    text1_g = f'Всего {qty_all_victory} {vik_all} в {qty_all} {word_duel_al}'
    text2_g = f'({percent_vik_all}%)'

    qty_shoulder_straps_all = heroes.Hero.get_count_shoulder_straps_all(activ_her)
    if qty_shoulder_straps_all:
        percent_straps_all = round((qty_all_victory / qty_shoulder_straps_all), 1)
        phrase = f'{percent_straps_all}/1'
    else:
        phrase = ''
    text3_g = f' Погоны {qty_shoulder_straps_all} ({phrase})'
    phrase1_g = f'{text1_g}{text2_g}{text3_g}'

    qty_duel_in_kv_victory = heroes.Hero.get_qty_duel_in_kv_victory(activ_her)
    qty_duel_in_kv_all = heroes.Hero.get_qty_duel_in_kv_all(activ_her)
    word_vik_in_kv = tools.transform_word_victory(qty_victory=qty_duel_in_kv_victory)
    word_duel_in_kv = tools.transform_word_duel(qty_duel=qty_duel_in_kv_all)
    if qty_duel_in_kv_all and qty_duel_in_kv_victory:
        percent_vik_kv = round((qty_duel_in_kv_victory / (qty_duel_in_kv_all / 100)), 1)
    else:
        percent_vik_kv = '0'
    qty_duel_loot = heroes.Hero.get_count_shoulder_straps_kv(activ_her)
    phrase2_g = (f'в кв {qty_duel_in_kv_victory} {word_vik_in_kv} '
                 f'в {qty_duel_in_kv_all} {word_duel_in_kv}'
                 f'({percent_vik_kv}%). Погоны {qty_duel_loot}')

    list_loot = heroes.Hero.get_list_loot(activ_her)
    # print(f'{list_loot=}')
    if list_loot:
        phrase3 = ', '.join(list_loot)
    else:
        phrase3 = ''
    return phrase1_g, phrase2_g, phrase3


def report_kv_efficiency_c():
    """
    зеленым(Всего {} побед в {} боях.) фиолетовым((x%)). Желтым({} погон ({x%})
    голубым(в кв {} побед в {} боях (x%))
    :return:
    """
    activ_her = heroes.Activ.hero_activ
    qty_all_victory = heroes.Hero.get_qty_duel_all_victory(activ_her)
    qty_all = heroes.Hero.get_qty_duel_all(activ_her)
    if qty_all:
        percent_vik_all = round((qty_all_victory / (qty_all / 100)), 1)
    else:
        percent_vik_all = 0
    vik_all = tools.transform_word_victory(qty_victory=qty_all_victory)
    word_duel_al = tools.transform_word_duel(qty_duel=qty_all)
    text1_g = f'Всего {qty_all_victory} {vik_all} в {qty_all} {word_duel_al}'
    text1_c = c_t.tc_green(text1_g)
    text2_g = f'({percent_vik_all}%)'
    text2_c = c_t.tc_magenta(text2_g)

    qty_shoulder_straps_all = heroes.Hero.get_count_shoulder_straps_all(activ_her)
    if qty_shoulder_straps_all:
        percent_straps_all = round((qty_all_victory / qty_shoulder_straps_all), 1)
        phrase = f'{percent_straps_all}/1'
    else:
        phrase = ''
    text3_g = f' Погоны {qty_shoulder_straps_all} ({phrase})'
    text3_c = c_t.tc_yellow(text3_g)
    phrase1_g = f'{text1_g}{text2_g}{text3_g}'
    phrase1_c = f'{text1_c}{text2_c}{text3_c}'

    qty_duel_in_kv_victory = heroes.Hero.get_qty_duel_in_kv_victory(activ_her)
    qty_duel_in_kv_all = heroes.Hero.get_qty_duel_in_kv_all(activ_her)
    word_vik_in_kv = tools.transform_word_victory(qty_victory=qty_duel_in_kv_victory)
    word_duel_in_kv = tools.transform_word_duel(qty_duel=qty_duel_in_kv_all)
    if qty_duel_in_kv_all and qty_duel_in_kv_victory:
        percent_vik_kv = round((qty_duel_in_kv_victory / (qty_duel_in_kv_all / 100)), 1)
    else:
        percent_vik_kv = '0'
    qty_duel_loot = heroes.Hero.get_count_shoulder_straps_kv(activ_her)
    phrase2_g = (f'в кв {qty_duel_in_kv_victory} {word_vik_in_kv} '
                 f'в {qty_duel_in_kv_all} {word_duel_in_kv}'
                 f'({percent_vik_kv}%). Погоны {qty_duel_loot}')
    phrase2_c = c_t.tc_cyan(phrase2_g)

    list_loot = heroes.Hero.get_list_loot(activ_her)
    # print(f'{list_loot=}')
    if list_loot:
        phrase3 = ', '.join(list_loot)
    else:
        phrase3 = ''
    return phrase1_c, phrase2_c, phrase3


def report_shoulder_straps():
    activ_her = heroes.Activ.hero_activ
    qty_victory_all = heroes.Hero.get_qty_duel_all_victory(activ_her)
    qty_shoulder_straps = heroes.Hero.get_count_shoulder_straps_all(activ_her)
    if qty_shoulder_straps:
        phrase = (f'Из {qty_victory_all} побед выпало {qty_shoulder_straps} погон. '
                  f'Т.е. {qty_victory_all / qty_shoulder_straps} боёв на 1 погон')
    else:
        phrase = f'Из {qty_victory_all} побед выпало {qty_shoulder_straps} погон'
    return phrase


def display_tim_start_kv():
    tim_kv = int(heroes.gady.time_start_kv)
    h = tim_kv // 3600
    m = (tim_kv - h * 3600) // 60
    s = tim_kv % 60
    print(f'Время старта КВ{h:02d}:{m:02d}:{s:02d}')
