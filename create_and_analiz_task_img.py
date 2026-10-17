from pywin.framework.toolmenu import tools

import fun
import event_OCR
import heroes
import my_OCR
import os_action
import find_img
import tools
from baza import baza_paths as b_p


def get_big_img_task_manual_select():
    """
    Создание трех картинок по линиям для ручного выбора
    :return:
    """
    fun.log_with_caller(message='a')
    # создание скринов заданий
    path = b_p.manual_selection_tasks
    'img/temp/sample_tasks/'
    old_dir = os_action.create_folder(path=path)
    if old_dir:
        os_action.del_all_file_in_dir(path_dir=path)
        print('Старые файлы были удалены.')
    ''
    region_line = fun.get_full_areas_task()
    n_line = 0
    for line in region_line:
        n_line += 1
        en = get_energy_value_in_line(line=n_line - 1)
        while not en:
            en = get_energy_value_in_line(line=n_line - 1)

        x_point, y_point, length_big_task, height_img, article_event = get_big_img_areas(region_line=line)
        name_img = f'{path}t{en}{article_event}.png'
        print(name_img)
        fun.foto_pos(name_img=name_img, region=(x_point, y_point, length_big_task, height_img))

    fun.log_with_caller(message='e')
    return path


def get_big_img_areas(*, region_line):
    article_event = ''

    pos_patron = None
    size_patron = None
    while not pos_patron:
        pos_patron_m, size_patron = find_img.find_patron_mark(region=region_line)
        pos_patron_event, size_patron = find_img.find_event_patron_mark(region=region_line)
        if pos_patron_m:
            pos_patron = pos_patron_m
            article_event = ''
        if pos_patron_event:
            pos_patron = pos_patron_event
            article_event = 'event'


    pos_xp = None
    size_xp = None
    while not pos_xp:
        pos_xp_m, size_xp = find_img.find_xp_mark(region=region_line)
        pos_xp_event, size_xp = find_img.find_event_xp_mark(region=region_line)
        if pos_xp_m:
            pos_xp = pos_xp_m
            article_event = ''
        if pos_xp_event:
            pos_xp = pos_xp_event
            article_event = 'event'

    pos_colon_mark = None
    size_colon = None
    while not pos_colon_mark:
        pos_colon_mark, size_colon = find_img.find_colon_mark(region=region_line)

    # ==================
    # получаю регион фото
    height_img = 31
    # получаю длину картинки

    length_value_xp = pos_xp[0] - pos_patron[0] - size_patron[0]
    length_value_patron = pos_patron[0] - pos_colon_mark[0] - int(size_patron[0] / 2)

    if length_value_xp < length_value_patron:
        length_value_patron = length_value_xp - size_colon[0]
    length_big_task = length_value_patron + length_value_xp + size_patron[0] + size_colon[0] + int(size_xp[0] / 2)
    #
    x_point = pos_patron[0] - length_value_patron - size_colon[0]
    y_point = pos_patron[1] - int(height_img / 2)
    return x_point, y_point, length_big_task, height_img, article_event


def create_big_img_task_line(*, line, value_energy, hero):
    """
    Создание большой картинки задания для сохранения.
    :param line: Номер линии.
    :param value_energy: Количество энергии.
    :param hero: Имя героя.
    :return: Путь/имя содержащий имя героя.
    """
    fun.log_with_caller(message='a')
    path = f'{b_p.task_hero}{hero}'
    os_action.create_folder(path=path)
    # name =
    article_event = ''

    # получаю регион нужной линии
    all_region = fun.get_full_areas_task()
    region_line = all_region[line - 1]
    # получаю позицию значка патрона и значка хр
    x_point, y_point, length_big_task, height_img, article_event = get_big_img_areas(region_line=region_line)

    name_img = f'{path}/t{value_energy}{article_event}.png'
    fun.foto_pos(name_img=name_img, region=(x_point, y_point, length_big_task, height_img))
    fun.log_with_caller(message='e')
    return name_img


def get_areas_task_smol_line1(*, region_line, height_img, setting=False):
    if setting:
        path = b_p.tasks_little_temp
        name_img = f'{path}line1.png'
        fun.foto_pos(name_img=name_img, region=region_line)
    # 1==================
    # получаю позицию значка патрона
    # получаю позицию значка хр

    pos_patron = None
    size_patron = None
    while not pos_patron:
        pos_patron_m, size_patron = find_img.find_patron_mark(region=region_line)
        pos_patron_event, size_patron = find_img.find_event_patron_mark(region=region_line)
        if pos_patron_m:
            pos_patron = pos_patron_m
            article_event = ''
        if pos_patron_event:
            pos_patron = pos_patron_event
            article_event = 'event'

    pos_xp = None
    size_xp = None
    while not pos_xp:
        pos_xp_m, size_xp = find_img.find_xp_mark(region=region_line)
        pos_xp_event, size_xp = find_img.find_event_xp_mark(region=region_line)
        if pos_xp_m:
            pos_xp = pos_xp_m
            article_event = ''
        if pos_xp_event:
            pos_xp = pos_xp_event
            article_event = 'event'

    pos_colon_mark = None
    size_colon = None
    while not pos_colon_mark:
        pos_colon_mark, size_colon = find_img.find_colon_mark(region=region_line)

    # получаю длину картинки
    length_value_xp = pos_xp[0] - pos_patron[0] - size_patron[0]
    length_value_patron = pos_patron[0] - pos_colon_mark[0] - int(size_patron[0] / 2)

    if length_value_xp < length_value_patron:
        length_value_patron = length_value_xp - size_colon[0]

    x_point_patron = pos_patron[0] - length_value_patron - size_colon[0]
    y_point_patron = pos_patron[1] - int(height_img / 2)
    region_patron_line = x_point_patron, y_point_patron, length_value_patron, height_img

    x_point_xp = pos_xp[0] - length_value_xp - int(size_xp[0] / 2)
    y_point_xp = pos_xp[1] - int(height_img / 2)

    region_xp_line = x_point_xp, y_point_xp, length_value_xp, height_img
    return region_patron_line, region_xp_line


def get_areas_task_smol_line2(*, region_line2, height_img, setting=False):
    """

    :param region_line2: Область обработки
    :param height_img:
    :param setting:
    :return:Регион двух картинок
    """
    if setting:
        path = b_p.tasks_little_temp
        name_img2 = f'{path}line2.png'
        fun.foto_pos(name_img=name_img2, region=region_line2)
    pos_patron2, sp = find_img.find_patron_mark(region=region_line2)
    pos_xp2, sx = find_img.find_xp_mark(region=region_line2)
    if not pos_patron2:
        pos_patron2, sp = find_img.find_event_patron_mark(region=region_line2)
        pos_xp2, sx = find_img.find_event_xp_mark(region=region_line2)
    # получаю длину картинки
    length_2 = pos_xp2[0] - pos_patron2[0] - sp[0] - 10
    # получаю позицию начала картинки
    x_point_2patron = pos_patron2[0] - length_2 - int(sp[0] / 2)
    x_point_2xp = pos_xp2[0] - length_2 - int(sp[0] / 2)

    y_point_2patron = pos_patron2[1] - int(height_img / 2)
    y_point_2xp = pos_xp2[1] - int(height_img / 2)

    region_xp_2_line = x_point_2xp, y_point_2xp, length_2, height_img
    region_patron_2_line = x_point_2patron, y_point_2patron, length_2, height_img
    return region_patron_2_line, region_xp_2_line


def get_areas_task_smol_line3(*, region_line3, height_img, setting=False):
    if setting:
        path = b_p.tasks_little_temp
        name_img3 = f'{path}line3.png'
        fun.foto_pos(name_img=name_img3, region=region_line3)
    pos_patron3, sp = find_img.find_patron_mark(region=region_line3)
    if not pos_patron3:
        pos_patron3, sp = find_img.find_event_patron_mark(region=region_line3)
    pos_xp3, sx = find_img.find_xp_mark(region=region_line3)
    if not pos_xp3:
        pos_xp3, sx = find_img.find_event_xp_mark(region=region_line3)

    # получаю длину картинки
    length_3 = pos_xp3[0] - pos_patron3[0] - sp[0] - 10
    # получаю позицию начала картинки
    x_point_3xp = pos_xp3[0] - length_3 - int(sp[0] / 2)
    x_point_3patron = pos_patron3[0] - length_3 - int(sp[0] / 2)

    y_point_3xp = pos_xp3[1] - int(height_img / 2)
    y_point_3patron = pos_patron3[1] - int(height_img / 2)

    region_xp_3_line = x_point_3xp, y_point_3xp, length_3, height_img
    region_patron_3_line = x_point_3patron, y_point_3patron, length_3, height_img

    return region_patron_3_line, region_xp_3_line


def get_screenshot_task_smol(manual=False, setting=False):
    """
    Создание шести маленьких картинок для анализа.
    :return:
    """
    fun.log_with_caller(message='a')
    # создание скринов заданий
    path = b_p.tasks_little_temp
    'img/default/temp/tasks/'
    os_action.create_folder(path=path)
    #
    'rl - region_line'
    ar_l1, ar_l2, ar_l3 = fun.get_full_areas_task()
    # скрины маленькие
    height_img = 30
    pul_rl1, xp_rl1 = get_areas_task_smol_line1(region_line=ar_l1, height_img=height_img, setting=setting)
    pul_rl2, xp_rl2 = get_areas_task_smol_line2(region_line2=ar_l2, height_img=height_img, setting=setting)
    pul_rl3, xp_rl3 = get_areas_task_smol_line3(region_line3=ar_l3, height_img=height_img, setting=setting)
    if setting:
        print(f'{pul_rl1=}')
        print(f'{pul_rl2=}')
        print(f'{pul_rl3=}')
        print(f'{xp_rl1=}')
        print(f'{xp_rl2=}')
        print(f'{xp_rl3=}')
    if pul_rl1 and xp_rl1:
        fun.foto_pos(name_img=f'{path}1_pul.png', region=pul_rl1)
        fun.foto_pos(name_img=f'{path}1_xp.png', region=xp_rl1)
    if pul_rl2 and xp_rl2:
        fun.foto_pos(name_img=f'{path}2_pul.png', region=pul_rl2)
        fun.foto_pos(name_img=f'{path}2_xp.png', region=xp_rl2)
    if pul_rl3 and xp_rl3:
        fun.foto_pos(name_img=f'{path}3_pul.png', region=pul_rl3)
        fun.foto_pos(name_img=f'{path}3_xp.png', region=xp_rl3)

    fun.log_with_caller(message='e')
    return


def get_energy_value_in_line(*, line):
    """
    Получение значения количества энергии в линии
    """
    fun.log_with_caller(message='a')
    region_img = fun.get_region_lines_task()
    path_energy_task = b_p.energy_task_value
    value_energy = None
    list_energy = ['en_1.png', 'en_2.png', 'en_3.png', 'en_4.png', 'en_5.png', 'en_7.png', ]
    for img in list_energy:
        pos_en = fun.locCenterImg(f'{path_energy_task}{img}', region=region_img[line], confidence=0.95)
        if pos_en:
            value_energy = fun.extraction_digit(item=img)
    fun.log_with_caller(message='e')
    return value_energy


def search_and_create_img_best_offer(*, person_identified=False, manual=False, analiz=True):
    """
    Анализ заданий.
    :param analiz:
    :param manual:
    :param person_identified: Персонаж опознан. 'True' если опознан. Иначе 'False'
    :return:
    """
    fun.log_with_caller(message='a')
    result_found = False
    if person_identified:
        res = fun.selection_hero()
        while not res:
            fun.push_close()
            res = fun.selection_hero()

        fun.vizit_to_station_master()

    path_little_tasks = b_p.tasks_little_temp
    # получаю по две картинки на строку для анализа
    if not person_identified:
        print(f'{manual=}, {analiz=}')
    get_screenshot_task_smol(manual=manual)

    # анализ заданий
    if analiz:
        list_1_pul = my_OCR.recognized(f'{path_little_tasks}1_pul.png')
        print(f'{list_1_pul=}')
        list_1_xp = my_OCR.recognized(f'{path_little_tasks}1_xp.png')
        print(f'{list_1_xp=}')
        # анализ второй строки
        list_2_pul = my_OCR.recognized(f'{path_little_tasks}2_pul.png')
        print(f'{list_2_pul=}')
        list_2_xp = my_OCR.recognized(f'{path_little_tasks}2_xp.png')
        print(f'{list_2_xp=}')
        # анализ третьей строки
        list_3_pul = my_OCR.recognized(f'{path_little_tasks}3_pul.png')
        print(f'{list_3_pul=}')
        list_3_xp = my_OCR.recognized(f'{path_little_tasks}3_xp.png')
        print(f'{list_3_xp=}')

        # поиск номера строки лучшего предложения
        bene = list(event_OCR.find_tasks_benefit(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp))
        print(f'{bene=}')
        best_line = None
        if 4 in bene:
            # print('Найдена лучшая строка')
            best_line = bene.index(4) + 1
            print(f'line {best_line} надо сохранять')

        elif 1 in bene and 2 in bene:
            # print('Опознаны две строки')
            # print(f'{bene.index(2)=}, {bene.index(0)=}, {bene.index(1)=}')
            best_line = bene.index(0) + 1
            print(f'line {best_line} надо сохранять')

        # получение количества энергии в best_line и создание большого скрина задания
        if best_line:
            value_energy = get_energy_value_in_line(line=best_line - 1)
            # print(f'{heroes.Activ.name_file_=}')
            if not manual:
                img = create_big_img_task_line(line=best_line, value_energy=value_energy,
                                               hero=heroes.Activ.name_for_file_)
                print(f'создан {img}')
                print()
                result_found = True
            else:
                img = create_big_img_task_line(line=best_line, value_energy=value_energy, hero='temp')
                print(f'создан {img}')
                print()

        else:
            print('Строка с результатом "4x1" не найдена')
    else:
        print(f"Анализ не проводился. Картинки расположены {path_little_tasks}")
    fun.log_with_caller(message='e')
    return result_found


def select_best_offer():
    """
    Построчный анализ заданий
    При результате "4" должен оставить поиск
    :return:    list_line - список результатов оценки
                line_number - количество проанализированных линий
    """
    fun.log_with_caller(message='a')

    def rating_task(*, analiz_line_number):
        fun.log_with_caller(message='a')
        path_little_tasks = b_p.tasks_little_temp
        pul = my_OCR.recognized(f'{path_little_tasks}{analiz_line_number}_pul.png')
        xp = my_OCR.recognized(f'{path_little_tasks}{analiz_line_number}_xp.png')
        bene = event_OCR.find_benefit(pul=pul, xp=xp)
        fun.log_with_caller(message='e')
        return bene

    line_number = 0
    list_line = []
    for i in range(3):
        line_number += 1
        list_line.append(line_number)
        benefit = rating_task(analiz_line_number=line_number)
        if benefit == 4:
            break
        else:
            list_line.append(line_number)
    fun.log_with_caller(message='e')
    return list_line, line_number
