"""Файл показывает как перевести картинку в текст
 и создаёт картинку уровня"""
import time

import fun
import event_OCR
import my_OCR
import baza_paths as b_p
import heroes


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot_task_big():
    # создание скринов заданий
    path = 'img/test/test_tasks/test big tasks'
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    # скрины большие
    region1_big, region2_big, region3_big = fun.get_areas_task_big()
    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, f'{path}/big_1.png')
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, f'{path}/big_2.png')
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, f'{path}/big_3.png')


def big_img_task(*, line, value_energy, hero):
    """
    Создание big_img задания нужной строки
    """
    task_hero: str = 'img/test/test_tasks/task/'
    path_hero = f'{b_p.task_hero}{hero}'
    # name =
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region = fun.get_areas_task_big()
    name_img = f'{path_hero}/t{value_energy}.png'
    foto_pos(region[line], tune_x, tune_y, tune_s, tune_v, name_img=name_img)
    return name_img


def get_energy_value_in_line(*, line):
    """
    Возвращает значение количества энергии в линии
    """
    region_img = fun.get_region_lines_task()
    path_energy_task = b_p.energy_task_value
    value_energy = None
    list_energy = ['en_1.png', 'en_2.png', 'en_3.png', 'en_4.png', 'en_5.png', 'en_7.png', ]
    for img in list_energy:
        pos_en = fun.locCenterImg(f'{path_energy_task}{img}', region=region_img[line])
        if pos_en:
            value_energy = fun.extraction_digit(item=img)
            print(value_energy)
            # fun.Mouse.move(pos=pos_en, speed=0.5)
    return value_energy


def get_screenshot_task_smol():
    # создание скринов заданий
    little_tasks = 'img/test/test_tasks/test_little_tasks/'
    path = b_p.tasks_little
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    # скрины маленькие
    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = fun.get_areas_task_small()
    foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, f'{path}1_pul.png')
    foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, f'{path}2_pul.png')
    foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, f'{path}3_pul.png')
    foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, f'{path}1_xp.png')
    foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, f'{path}2_xp.png')
    foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, f'{path}3_xp.png')
    return


def rating_task(*, line_number):
    path_little_tasks = b_p.tasks_little
    pul = my_OCR.recognized(f'{path_little_tasks}{line_number}_pul.png')
    xp = my_OCR.recognized(f'{path_little_tasks}{line_number}_xp.png')
    bene = event_OCR.find_benefit(pul=pul, xp=xp)
    return bene


def analiz_task():
    fun.selection_hero()
    fun.vizit_to_station_master()

    little_tasks = 'img/test/test_tasks/test_little_tasks/'
    path_little_tasks = b_p.tasks_little
    # получаю по две картинки на строку для анализа
    get_screenshot_task_smol()
    # анализ заданий
    list_1_pul = my_OCR.recognized(f'{path_little_tasks}1_pul.png')
    list_1_xp = my_OCR.recognized(f'{path_little_tasks}1_xp.png')
    # time.sleep(2)
    list_2_pul = my_OCR.recognized(f'{path_little_tasks}2_pul.png')
    list_2_xp = my_OCR.recognized(f'{path_little_tasks}2_xp.png')
    # time.sleep(2)
    list_3_pul = my_OCR.recognized(f'{path_little_tasks}3_pul.png')
    list_3_xp = my_OCR.recognized(f'{path_little_tasks}3_xp.png')
    # поиск номера  строки лучшего предложения
    bene = list(event_OCR.find_tasks_benefit(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp))
    best_line = None
    if 4 in bene:
        best_line = bene.index(4) + 1
        print(f'line {best_line} надо сохранять')
    else:
        pass
    # номер лучшей строки
    # print(f'{best_line=}')
    # получение количества энергии в best_line и создание большого скрина задания
    if best_line:
        value_energy = get_energy_value_in_line(line=best_line - 1)
        print(f'{heroes.Activ.name_file_=}')
        img = big_img_task(line=best_line - 1, value_energy=value_energy, hero=heroes.Activ.name_file_)
        print(f'создан {img}')
    else:
        print('неудача')


def select_best_offer():
    """
    Построчный анализ заданий
    При результате "4" должен оставить поиск
    :return:    list_line - список результатов оценки
                line_number - количество проанализированных линий
    """
    line_number = 0
    list_line = []
    for i in range(3):
        line_number += 1
        list_line.append(line_number)
        benefit = rating_task(line_number=line_number)
        if benefit == 4:
            break
        else:
            list_line.append(line_number)
    return list_line, line_number

