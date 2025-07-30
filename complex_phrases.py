"""
сложные сообщения
"""
import fun
import color_text
import heroes


def display_set_inspect_report():
    fraze = ('Чего их еще раз шмонать? Сегодня всё уже найдено.')
    return fraze


def display_info_energy_all():
    print()
    print('Расход энергии')
    print(f'    Gady:   сегодня-{heroes.gady.energy_count_today},    всего-{heroes.gady.energy_count_all}')
    print(f'    Gavr:   сегодня-{heroes.gavr.energy_count_today},    всего-{heroes.gavr.energy_count_all}')
    print(f'    Veles:  сегодня-{heroes.veles.energy_count_today},    всего-{heroes.veles.energy_count_all}')
    print(f'    Mara:   сегодня-{heroes.mara.energy_count_today},    всего-{heroes.mara.energy_count_all}')
    return


def display_home_location_hero(*, her):
    home_location = heroes.Hero.get_home_location(her)
    print(home_location)
    return home_location


def display_report_wildman():
    print()
    print(f'Gady: {report_wildman(hero=heroes.gady)}')
    print(f'Gavr: {report_wildman(hero=heroes.gavr)}')
    print(f'Велес:  {report_wildman(hero=heroes.veles)}')
    return


def smol_report_wildman():
    print(
        f"gady {heroes.gady.wildman_days_count} {fun.transform_days(qty_days=heroes.gady.wildman_days_count)},"
        f" {heroes.gady.wildman_count} {fun.transform_wilds(qty_days=heroes.gady.wildman_count)}")

    print(
        f'gavr {heroes.gavr.wildman_days_count} {fun.transform_days(qty_days=heroes.gavr.wildman_days_count)},'
        f' {heroes.gavr.wildman_count} {fun.transform_wilds(qty_days=heroes.gavr.wildman_count)}')

    print(
        f'veles {heroes.veles.wildman_days_count} {fun.transform_days(qty_days=heroes.veles.wildman_days_count)},'
        f' {heroes.veles.wildman_count} {fun.transform_wilds(qty_days=heroes.veles.wildman_count)}')

    print(
        f'mara {heroes.mara.wildman_days_count} {fun.transform_days(qty_days=heroes.mara.wildman_days_count)},'
        f' {heroes.mara.wildman_count} {fun.transform_wilds(qty_days=heroes.mara.wildman_count)}')
    return


def report_wildman(*, hero):
    # 'За ''3'' дня ''4'' шт.
    # Всего потрачено ХХХ единиц энергии
    text_11 = color_text.tc_green('За ')  # 'За '
    days_all_count = color_text.tc_cyan(str(heroes.Hero.get_days_count_wildman(hero)))  # '3'
    text_12 = color_text.tc_green(f' {fun.transform_days(qty_days=heroes.Hero.get_days_count_wildman(hero))} ')  # ' дня '
    wildman_all_count = color_text.tc_cyan(str(heroes.Hero.get_wildman_count(hero)))  # '4'
    text_13 = color_text.tc_green(' шт.')  # ' шт.'
    phrase1 = f'{text_11}{days_all_count}{text_12}{wildman_all_count}{text_13}'

    text_22 = color_text.tc_green('Всего потрачено ')  # 'Потрачено '
    all_energy_count = color_text.tc_yellow(f'{heroes.Hero.get_energy_count_all(hero)}')  # 'XXX'
    text_23 = color_text.tc_green(' единиц энергии')
    phrase2 = f'{text_22}{all_energy_count}{text_23}'

    # количество энергии на одного
    text_31 = color_text.tc_green(' Это ')
    average_value_3 = color_text.tc_blue(
        f'{round(heroes.Hero.get_energy_count_all(hero) / heroes.Hero.get_wildman_count(hero), 4)}')  # '7'
    text_32 = color_text.tc_green(' эн на 1го')  # ' эн на 1го'
    phrase3 = f'{text_31}{average_value_3}{text_32}'
    report_wildman_hero = f'{phrase1}{phrase3}\n{phrase2}'
    return report_wildman_hero
