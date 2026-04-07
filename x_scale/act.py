import os_action
import baza
import find_img
import tools
import fun


def get_actual_path(*, path: str) -> str:
    """
    Изменяет папку актуального масштаба.
    :param path: Путь к файлу.
    :return: Актуальный путь к файлу.
    """
    # print()
    # print(f'{path=}')
    # print(f'{baza.baza_paths.actual_caliber_folder=}')
    # Путь зависит от масштаба.
    if 'default' in path:
        # Если в данный момент калибр 'default'
        if baza.baza_paths.actual_caliber_folder == 'default':
            # Действий не производим
            actual_path = path
        else:
            actual_path = path.replace('default', baza.baza_paths.actual_caliber_folder)
    # Путь не зависит от масштаба.
    else:
        actual_path = path
    # print(f'{actual_path=}')
    return actual_path


def get_pers_name():
    """
    Попробовать опознать персонажа.
    :return: None / имя
    """
    # Получаем актуальный путь
    path_hero_id_folder = get_actual_path(path=baza.baza_paths.hero_id)
    # Получаем список существующих файлов
    lst_hero_id_files = os_action.get_lst_files(path=path_hero_id_folder)

    print(f'список существующих файлов {lst_hero_id_files=}')
    lst_hero_fase_file = []
    pers_name = None
    for files in lst_hero_id_files:
        if not 'acc' in files:
            lst_hero_fase_file.append(files)

    if lst_hero_fase_file:
        for file in lst_hero_id_files:
            fase = find_img.find_img(path_img=file)
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
        'gady': baza.paths_img.gady_id,
        'gavr': baza.paths_img.gavr_id,
        'mara': baza.paths_img.mara_id,
    }
    path_img = get_actual_path(path=dict_img[name])
    print(path_img, 'актуальный путь')
    folder_img = '/'.join(path_img.split('/')[:-1])
    os_action.create_folder(path=folder_img)
    path_point_mark = f'{baza.baza_paths.path_folder_line_menu}/line_button_pm_{skale}.png'
    point_mark = find_img.find_img(path_img=path_point_mark)
    tools.Mouse.move(pos=point_mark, message='point_mark')
    x, y = point_mark
    x -= int(395 * (int(skale) / 100))
    y += int(122 * (int(skale) / 100))
    print(f'{x=}, {y=}')
    tools.Mouse.move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = (74 * (int(skale) / 100))
    change_y = (74 * (int(skale) / 100))
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # # собственно создание снимка
    fun.foto(f'{path_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{path_img}')
    # fun.mouse_move(pos=pos)
    tools.sounds.sound_vic()
    print('ok')
