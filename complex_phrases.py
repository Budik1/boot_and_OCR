"""
Сложные сообщения
"""
import fun
import heroes
import color_text


def display_report_energy_now(*, vers_in_print, value_energy):
    """
    Пример сообщения:
    "{3} задание,{ conf_=0.94}. Сейчас {3}, сегодня {20}, всего/на Киевской {120}/{12}"
    Args:
        vers_in_print (str): пробел или значение {conf_=}
        value_energy (int): количество энергии потраченной на задание
    """
    print(f'{vers_in_print}'  # {task_number} задание
          f'Сейчас {value_energy}, '
          f'сегодня {heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)}, '
          f'всего/на Киевской: {heroes.Hero.get_energy_count_all(heroes.Activ.hero_activ)}/'
          f'{heroes.Hero.get_energy_kiev_count_all(heroes.Activ.hero_activ)}'
          )


def set_inspect_report():
    fraze = 'Чего их еще раз шмонать? Сегодня всё уже найдено.'
    return fraze


def display_info_energy_all():
    print()
    print('Расход энергии')

    for key in heroes.hero_dict:
        name = key.rjust(8, " ")
        energy_count_today = str(heroes.Hero.get_energy_count_today(heroes.hero_dict[key])).rjust(3, " ")
        energy_count_all = str(heroes.Hero.get_energy_count_all(heroes.hero_dict[key])).rjust(6, " ")
        now = "сегодня-".rjust(10, " ")
        all_ = 'всего:'.rjust(8, ' ')
        en_kiev = str(heroes.Hero.get_energy_kiev_count_all(heroes.hero_dict[key])).ljust(5, ' ')
        dif = str(int(energy_count_all) - int(en_kiev)).rjust(5, ' ')
        print(
            f'{name}{now}{energy_count_today}{all_}'
            f'{energy_count_all}/{en_kiev}'
            f'{dif}')
    print()
    return


def display_home_location_hero(*, her):
    home_location = heroes.Hero.get_home_location(her)
    print(home_location)
    return home_location


def display_report_wildman():
    print()
    print('Дикари')

    for key in heroes.hero_dict:
        name = heroes.Hero.get_name_ru(heroes.hero_dict[key]).rjust(7, ' ')

        print(f'{name}:{report_wildman(hero=heroes.hero_dict[key])}')
    return

def display_report_w_rat():
    print()
    print('white rat')
    for key in heroes.hero_dict:
        name = heroes.Hero.get_name_ru(heroes.hero_dict[key]).rjust(7, ' ')

        print(f'{name}:{report_white_rat(hero=heroes.hero_dict[key])}')
    return


def display_smol_report_wildman():
    """
    gady 0 дней, 0 дикарей
    :return:
    """
    print()
    for key in heroes.hero_dict:
        name = key.rjust(8, ' ')
        q_days = str(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])).rjust(3, ' ')
        days = (fun.transform_word_days(qty_days=(heroes.Hero.get_days_count_wildman(heroes.hero_dict[key])))).rjust(5,
                                                                                                                     ' ')
        q_wild = str(heroes.Hero.get_wildman_count(heroes.hero_dict[key])).rjust(4)
        wild = fun.transform_word_wilds(qty_wilds=heroes.Hero.get_wildman_count(heroes.hero_dict[key])).rjust(8)
        print(f'{name}{q_days}{days}{q_wild}{wild}')

    return


def report_white_rat(*, hero):
    #  Потрачено {} ед.эн.
    # {} эн на 1го.

    text_22 = color_text.tc_green(' Потрачено ')  # 'Потрачено '
    energy_w_rat_count_all = color_text.tc_yellow(f'{heroes.Hero.get_white_rat_energy(hero)}')  # 'XXX'
    text_23 = color_text.tc_green(' ед.эн.')
    phrase2 = f'{text_22}{energy_w_rat_count_all}{text_23}'

    # количество энергии на одного
    if heroes.Hero.get_white_rat_count_all(hero):
        # text_31 = color_text.tc_green(' Это ')
        average_value_3 = color_text.tc_blue(
            f'{round(heroes.Hero.get_white_rat_energy(hero) / heroes.Hero.get_white_rat_count_all(hero), 4)}')  # '7'
        text_32 = color_text.tc_green(' эн на 1ну крысу.')  # ' эн на 1го'
        phrase1 = f'{average_value_3.rjust(17)}{text_32}'
        report_w_rat_hero = f'{phrase1}{phrase2}'
    else:
        phrase1 = 'Нет данных.'.rjust(19)
        report_w_rat_hero = f'{phrase1}{phrase2}'
    return report_w_rat_hero


def report_wildman(*, hero):
    # {} эн на 1го.
    #  Потрачено {} ед.эн.

    text_22 = color_text.tc_green(' Потрачено ')  # 'Потрачено '
    energy_kiev_count_all = color_text.tc_yellow(f'{heroes.Hero.get_energy_kiev_count_all(hero)}')  # 'XXX'
    text_23 = color_text.tc_green(' ед.эн.')
    phrase2 = f'{text_22}{energy_kiev_count_all}{text_23}'

    # количество энергии на одного
    if heroes.Hero.get_wildman_count(hero):
        # text_31 = color_text.tc_green(' Это ')
        average_value_3 = color_text.tc_blue(
            f'{round(heroes.Hero.get_energy_kiev_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}')  # '7'
        text_32 = color_text.tc_green(' эн на 1го.')  # ' эн на 1го'
        phrase1 = f'{average_value_3.rjust(17)}{text_32}'
        report_wildman_hero = f'{phrase1}{phrase2}'
    else:
        phrase1 = 'Нет данных.'.rjust(19)
        report_wildman_hero = f'{phrase1}{phrase2}'
    return report_wildman_hero


def report_kv_efficiency():
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
    vik_all = fun.transform_word_victory(qty_victory=qty_all_victory)
    word_duel_al = fun.transform_word_duel(qty_duel=qty_all)
    text1 = color_text.tc_green(f'Всего {qty_all_victory} {vik_all} в {qty_all} {word_duel_al}')
    text2 = color_text.tc_magenta(f'({percent_vik_all}%)')

    qty_shoulder_straps_all = heroes.Hero.get_count_shoulder_straps_all(activ_her)
    if qty_shoulder_straps_all:
        percent_straps_all = round((qty_all_victory / qty_shoulder_straps_all), 1)
        phrase = f'{percent_straps_all}/1'
    else:
        phrase = ''
    text3 = color_text.tc_yellow(f' Погоны {qty_shoulder_straps_all} ({phrase})')
    phrase1 = f'{text1}{text2}{text3}'

    qty_duel_in_kv_victory = heroes.Hero.get_qty_duel_in_kv_victory(activ_her)
    qty_duel_in_kv_all = heroes.Hero.get_qty_duel_in_kv_all(activ_her)
    word_vik_in_kv = fun.transform_word_victory(qty_victory=qty_duel_in_kv_victory)
    word_duel_in_kv = fun.transform_word_duel(qty_duel=qty_duel_in_kv_all)
    if qty_duel_in_kv_all and qty_duel_in_kv_victory:
        percent_vik_kv = round((qty_duel_in_kv_victory / (qty_duel_in_kv_all / 100)), 1)
    else:
        percent_vik_kv = '0'
    qty_duel_loot = heroes.Hero.get_count_shoulder_straps_kv(activ_her)
    phrase2 = color_text.tc_cyan(f'в кв {qty_duel_in_kv_victory} {word_vik_in_kv} в '
                                 f'{qty_duel_in_kv_all} {word_duel_in_kv}'
                                 f'({percent_vik_kv}%). Погоны {qty_duel_loot}')

    list_loot = heroes.Hero.get_list_loot(activ_her)
    # print(f'{list_loot=}')
    if list_loot:
        phrase3 = ', '.join(list_loot)
    else:
        phrase3 = []
    return phrase1, phrase2, phrase3


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
