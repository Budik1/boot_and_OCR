import baza.baza_paths as b_p
import os_action
import find_img
import fun


def get_energy_value_in_line(*, line):
    """
    Получение значения количества энергии в линии
    """
    fun.log_with_caller(message='a')
    # print(f'{line=}, {type(line)}')
    region_img = fun.get_region_lines_task()
    path_energy_task = b_p.energy_task_value
    value_energy = None
    list_energy = ['en_1.png', 'en_2.png', 'en_3.png', 'en_4.png', 'en_5.png', 'en_7.png', ]
    for img in list_energy:
        pos_en = fun.locCenterImg(f'{path_energy_task}{img}', region=region_img[line], confidence=0.95)
        if pos_en:
            value_energy = fun.extraction_digit(item=img)
            # print(f'{value_energy=}')
    fun.log_with_caller(message='e')
    return value_energy


def get_imgs_task_big_manual_select():
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
    # print(f'{region_line=}')
    n_line = 0
    for line in region_line:
        n_line += 1
        en = get_energy_value_in_line(line=n_line - 1)
        while not en:
            en = get_energy_value_in_line(line=n_line - 1)
        article_event = ''
        pos_patron = None
        pos_xp = None
        size_patron = None
        size_xp = None
        while not pos_patron:
            pos_patron_m, size_patron = find_img.find_patron_mark(region=line)
            pos_patron_event, size_patron = find_img.find_event_patron_mark(region=line)
            if pos_patron_m:
                pos_patron = pos_patron_m
                article_event = ''
            if pos_patron_event:
                pos_patron = pos_patron_event
                article_event = 'event'

        while not pos_xp:
            pos_xp_m, size_xp = find_img.find_xp_mark(region=line)
            pos_xp_event, size_xp = find_img.find_event_xp_mark(region=line)
            if pos_xp_m:
                pos_xp = pos_xp_m
                article_event = ''
            if pos_xp_event:
                pos_xp = pos_xp_event
                article_event = 'event'

        pos_colon_mark = None
        colon_size = None
        while not pos_colon_mark:
            pos_colon_mark, colon_size = find_img.find_colon_mark(region=line)

        # ==================
        # получаю регион фото
        height_img1 = 31
        # получаю длину картинки

        length_value_xp = pos_xp[0] - pos_patron[0] - size_patron[0]
        length_value_patron = pos_patron[0] - pos_colon_mark[0] - int(size_patron[0] / 2)

        if length_value_xp < length_value_patron:
            print(length_value_xp, '<', length_value_patron)
            length_value_patron = length_value_xp - colon_size[0]
        print(length_value_patron)
        length_big_task1 = length_value_patron + length_value_xp + size_patron[0] + colon_size[0] + int(size_xp[0] / 2)
        #
        # x_xp = pos_xp[0] - length_value_xp - (size_xp[0] / 2)
        # x_patron =pos_patron[0] - size_patron[0]/2 - length_value_patron
        x1_point = pos_patron[0] - length_value_patron - colon_size[0]
        y1_point = pos_patron[1] - int(height_img1 / 2)

        name_img1 = f'{path}t{en}{article_event}.png'
        # name_img_xp = f'{path}t{en}xp{article_event}.png'
        # name_img_patron = f'{path}t{en}patron{article_event}.png'

        print(name_img1)
        # fun.foto_pos(name_img=name_img_xp, region=(x_xp, y1_point, length_value_xp, height_img1))
        # fun.foto_pos(name_img=name_img_patron, region=(x_patron, y1_point, length_value_patron, height_img1))
        fun.foto_pos(name_img=name_img1, region=(x1_point, y1_point, length_big_task1, height_img1))

    fun.log_with_caller(message='e')
    return path


get_imgs_task_big_manual_select()
