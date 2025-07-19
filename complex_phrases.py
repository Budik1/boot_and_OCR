"""
сложные сообщения
"""
import fun
import my_color_text as myCt
import heroes


def display_info_energy_all():
    print()
    print('Всего израсходовано энергии')
    print(f'    Gady - {heroes.gady.energy_count_all}')
    print(f'    Gavr - {heroes.gavr.energy_count_all}')
    print(f'    Veles - {heroes.veles.energy_count_all}')
    print(f'    Mara - {heroes.mara.energy_count_all}')
    return


def display_home_location_hero(*, her):
    home_location = heroes.Hero.get_home_location(her)
    print(home_location)
    return home_location


def report_wildman(*, hero):
    # 'За ''3'' дня ''4'' шт.
    # Это 7 эн на 1го'
    # На Х заданий потрачено ХХХ ед энергии
    text_11 = myCt.tc_green('За ')  # 'За '
    days_all_count = myCt.tc_cyan(str(heroes.Hero.get_days_count_wildman(hero)))  # '3'
    text_12 = myCt.tc_green(f' {fun.transform_days(qty_days=heroes.Hero.get_days_count_wildman(hero))} ')  # ' дня '
    wildman_all_count = myCt.tc_cyan(str(heroes.Hero.get_wildman_count(hero)))  # '4'
    text_13 = myCt.tc_green(' шт.')  # ' шт.'
    phrase1 = f'{text_11}{days_all_count}{text_12}{wildman_all_count}{text_13}'

    text_21 = myCt.tc_green('На ')  # 'На '
    all_task_count = myCt.tc_yellow(f'{heroes.Hero.get_task_count(hero)}')  # '10'
    text_22 = myCt.tc_green(' заданий потрачено ')  # ' заданий потрачено '
    all_energy_count = myCt.tc_yellow(f'{heroes.Hero.get_energy_count_all(hero)}')  # 'XXX'
    text_23 = myCt.tc_green(' единиц энергии')
    phrase2 = f'{text_21}{all_task_count}{text_22}{all_energy_count}{text_23}'

    # количество энергии на одного
    text_31 = myCt.tc_green(' Это ')
    average_value_3 = myCt.tc_blue(
        f'{round(heroes.Hero.get_energy_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}')  # '7'
    text_32 = myCt.tc_green(' эн на 1го')  # ' эн на 1го'
    phrase3 = f'{text_31}{average_value_3}{text_32}'
    report_wildman_hero = f'{phrase1}{phrase3}\n{phrase2}'
    return report_wildman_hero
# display_home_location_hero(her=heroes.gady)
