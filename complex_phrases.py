"""
сложные сообщения
"""
import fun
import color_text
import heroes


def display_report_energy_now(*, task_number, vers_in_print, value_energy):
    """
    Пример сообщения:
    "{3} задание,{ conf_=0.94}. Сейчас {3}, сегодня {20}, всего/на Киевской {120}/{12}"
    Args:
        task_number (int): номер строки заданий
        vers_in_print (str): пробел или значение {conf_=}
        value_energy (int): количество энергии потраченной на задание
    """
    print(f'{vers_in_print}'  # {task_number} задание
          f'Сейчас {value_energy}, '
          f'сегодня {heroes.Hero.get_energy_count_today(heroes.Activ.hero_activ)}, '
          f'всего/на Киевской: {heroes.Hero.get_energy_count_all(heroes.Activ.hero_activ)}/'
          f'{heroes.Hero.get_energy_kiev_count_all(heroes.Activ.hero_activ)}')


def set_inspect_report():
    fraze = 'Чего их еще раз шмонать? Сегодня всё уже найдено.'
    return fraze


def display_info_energy_all():
    print()
    print('Расход энергии')

    indent_ = " "
    len_1 = 3
    len_2 = 6
    len_3 = 8
    len_4 = 18
    hero_dict = {'Gady:': heroes.gady, 'Gavr:': heroes.gavr, 'Veles:': heroes.veles, 'Mara:': heroes.mara}

    for key in hero_dict:
        indent = indent_.ljust(4, " ")
        name = key.rjust(6, " ")
        energy_count_today = str(heroes.Hero.get_energy_count_today(hero_dict[key])).rjust(3, " ")
        energy_count_all = str(heroes.Hero.get_energy_count_all(hero_dict[key])).rjust(6, " ")
        now = "сегодня-".rjust(10, " ")
        all = 'всего:'.rjust(8, ' ')
        en_kiev = str(heroes.Hero.get_energy_kiev_count_all(hero_dict[key])).ljust(5, ' ')
        dif = str(int(energy_count_all)-int(en_kiev)).rjust(5, ' ')
        print(
            f'{indent}{name}{now}{energy_count_today}{all}'
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
    hero_dict = {'Gady:': heroes.gady, 'Gavr:': heroes.gavr, 'Veles:': heroes.veles, 'Mara:': heroes.mara}
    for key in hero_dict:
        name = heroes.Hero.get_name_ru(hero_dict[key]).rjust(8, ' ')

        print(f'{name}:{report_wildman2(hero=hero_dict[key])}')

    return


def display_smol_report_wildman():
    """
    gady 0 дней, 0 дикарей
    :return:
    """
    print()
    hero_dict = {'Gady:': heroes.gady, 'Gavr:': heroes.gavr, 'Veles:': heroes.veles, 'Mara:': heroes.mara}
    for key in hero_dict:
        name = key.rjust(8, ' ')
        q_days = str(heroes.Hero.get_days_count_wildman(hero_dict[key])).rjust(3, ' ')
        days = (fun.transform_word_days(qty_days=(heroes.Hero.get_days_count_wildman(hero_dict[key])))).rjust(5, ' ')
        q_wild = str(heroes.Hero.get_wildman_count(hero_dict[key])).rjust(4)
        wild = fun.transform_word_wilds(qty_wilds=heroes.Hero.get_wildman_count(hero_dict[key])).rjust(8)
        print(f'{name}{q_days}{days}{q_wild}{wild}')

    return


def report_wildman1(*, hero):
    # 'За ''3'' дня ''4'' шт.
    # Всего потрачено ХХХ единиц энергии
    # За {} дня {} шт. Это {} эн на 1го
    # На Киевской потрачено {} единиц энергии
    text_11 = color_text.tc_green('За ')  # 'За '
    days_all_count = color_text.tc_cyan(str(heroes.Hero.get_days_count_wildman(hero)))  # '3'
    text_12 = color_text.tc_green(
        f' {fun.transform_word_days(qty_days=heroes.Hero.get_days_count_wildman(hero))} ')  # ' дня '
    wildman_all_count = color_text.tc_cyan(str(heroes.Hero.get_wildman_count(hero)))  # '4'
    text_13 = color_text.tc_green(' шт.')  # ' шт.'
    phrase1 = f'{text_11}{days_all_count}{text_12}{wildman_all_count}{text_13}'

    text_22 = color_text.tc_green('На Киевской потрачено ')  # 'Потрачено '
    all_energy_count = color_text.tc_yellow(f'{heroes.Hero.get_energy_kiev_count_all(hero)}')  # 'XXX'
    text_23 = color_text.tc_green(' единиц энергии')
    phrase2 = f'{text_22}{all_energy_count}{text_23}'

    # количество энергии на одного
    if heroes.Hero.get_wildman_count(hero):
        text_31 = color_text.tc_green(' Это ')
        average_value_3 = color_text.tc_blue(
            f'{round(heroes.Hero.get_energy_kiev_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}')  # '7'
        text_32 = color_text.tc_green(' эн на 1го')  # ' эн на 1го'
        phrase3 = f'{text_31}{average_value_3}{text_32}'
        report_wildman_hero = f'{phrase1}{phrase3}\n{phrase2}'
    else:
        report_wildman_hero = f'{phrase1}\n{phrase2} пока 0'
    return report_wildman_hero


def report_wildman2(*, hero):
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
    зеленым({} побед в {} боях.) фиолетовым((x%)). желтым({} погон ({x%})
    голубым(в кв {} побед в {} боях (x%))
    :return:
    """
    qty_all_viktory = heroes.Hero.get_qty_all_victory(heroes.Activ.hero_activ)
    qty_all = heroes.Hero.get_qty_all(heroes.Activ.hero_activ)
    percent_vik_all = round((qty_all_viktory / (qty_all / 100)), 1)
    text1 = color_text.tc_green(f'{qty_all_viktory} побед в {qty_all} боях.')
    text2 = color_text.tc_magenta(f'( {percent_vik_all}% )')

    qty_shoulder_straps = heroes.Hero.get_count_shoulder_straps_all(heroes.Activ.hero_activ)
    if qty_shoulder_straps:
        percent_straps_all = round((qty_all_viktory / qty_shoulder_straps), 2)
        phrase = f'{percent_straps_all}/1'
    else:
        phrase = ''
    text3 = color_text.tc_yellow(f' Погоны {qty_shoulder_straps} ({phrase})')
    phrase1 = f'{text1}{text2}{text3}'

    qty_kv_victory = heroes.Hero.get_qty_kv_victory(heroes.Activ.hero_activ)
    qty_kv_all = heroes.Hero.get_qty_kv_all(heroes.Activ.hero_activ)
    if qty_kv_all and qty_kv_victory:
        percent_vik_kv = round((qty_kv_victory / (qty_kv_all / 100)), 1)
    else:
        percent_vik_kv = '0%'
    phrase2 = color_text.tc_cyan(f'в кв боёв {qty_kv_all}, побед {qty_kv_victory} ( {percent_vik_kv}% )')
    return phrase1, phrase2


def report_shoulder_straps():
    qty_victory_all = heroes.Hero.get_qty_all_victory(heroes.Activ.hero_activ)
    qty_shoulder_straps = heroes.Hero.get_count_shoulder_straps_all(heroes.Activ.hero_activ)
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
