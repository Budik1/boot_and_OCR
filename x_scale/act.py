import os_action
import baza
import find_img
import tools


def get_actual_path(*, path: str):
    # print(f'create_actual_path.{baza.baza_paths.actual_caliber_folder}')
    return path.replace('default', baza.baza_paths.actual_caliber_folder)


def get_pers_name(*, skale: str):
    """
    Попробовать опознать персонажа.
    :return: None / имя
    """
    #
    print(f'get_pers_name.{baza.baza_paths.actual_caliber_folder=}')
    path_hero_id_folder = get_actual_path(path=baza.baza_paths.hero_id)
    print(f'{path_hero_id_folder=}')
    lst_hero_id_files = os_action.get_lst_files(path=path_hero_id_folder)
    print(f'{lst_hero_id_files=}')
    lst_hero_fase_file = []
    pers_name = None
    for files in lst_hero_id_files:
        if not 'acc' in files:
            lst_hero_fase_file.append(files)
    if lst_hero_fase_file:
        for file in lst_hero_id_files:
            fase = find_img.find_img(name_img=file)
            if fase:
                # получить имя перса из имени файла
                lst_pers = file.split('/')
                if '\\' in lst_pers[-1]:
                    name, img = lst_pers[-1].split('\\')
                else:
                    name = lst_pers[-2]
                pers_name = name
                break
    return pers_name


def cr_pers_png(*, name: str, skale: str):
    dict_img = {
        'gady': f'{baza.baza_paths.hero_id}gady/her_gady.png',
        'gavr': f'{baza.baza_paths.hero_id}gavr/her_gavr.png',
        'mara': f'{baza.baza_paths.hero_id}mara/her_mara.png',
    }
    path_img = get_actual_path(path=dict_img[name])
    # print(path_img, 'актуальный путь')
    path_point_mark = f'{baza.baza_paths.path_folder_line_menu}/line_button_pm_{skale}.png'
    point_mark = find_img.find_img(name_img=path_point_mark)
    tools.Mouse.move(pos=point_mark, message='point_mark')
    

