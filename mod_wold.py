def transform_word_duel(*, qty_duel: int):
    col_days_ed = qty_duel % 10
    col_days_des = (qty_duel // 10) % 10
    if col_days_ed == 0 and col_days_des == 0:
        result = 'дуэлей'
    elif col_days_ed == 1 and col_days_des != 1:
        result = 'дуэли'
    else:
        result = 'дуэлях'
    return result


def transform_word_victory(*, qty_victory: int):
    col_days_ed = qty_victory % 10
    col_days_des = (qty_victory // 10) % 10
    if col_days_ed == 1 and col_days_des != 1:
        result = 'победа'
    elif col_days_ed in [2, 3, 4] and col_days_des != 1:
        result = 'победы'
    else:
        result = 'побед'
    return result


def transform_word_days(*, qty_days: int):
    col_days_ed = qty_days % 10
    col_days_des = (qty_days // 10) % 10
    if col_days_ed == 1 and col_days_des != 1:
        result = 'день'
    elif col_days_ed in [2, 3, 4] and col_days_des != 1:
        result = 'дня'
    else:
        result = 'дней'
    return result


def transform_word_file(*, qty_files: int):
    col_days_ed = qty_files % 10
    col_days_des = (qty_files // 10) % 10
    if col_days_ed == 1 and col_days_des != 1:
        results = 'файл'
    elif col_days_ed in [2, 3, 4] and col_days_des != 1:
        results = 'файла'
    else:
        results = 'файлов'
    return results


def transform_word_wilds(*, qty_wilds: int):
    col_days_ed = qty_wilds % 10
    col_days_des = (qty_wilds // 10) % 10
    if col_days_ed == 1 and col_days_des != 1:
        result = 'дикарь'
    elif col_days_ed in [2, 3, 4] and col_days_des != 1:
        result = 'дикаря'
    else:
        result = 'дикарей'
    return result


def modification_name(*, old_path_name: object | str, modifier: object | str, new_path: object | str = None) -> str:
    """
    Использую для модификации имени файла при изменении. К родительскому имени добавляется модификатор.
    :param old_path_name: Родительский путь_имя.
    :param modifier: Добавляемая часть.
    :param new_path: Новый путь, если есть необходимость.
    :return: Путь_имя
    """
    # Получаю расширение файла в конце списка
    path_name_lst = old_path_name.split('.')
    # Получаю имя файла в конце списка
    paths_lst = path_name_lst[0].split('/')
    #  Получаю имя файла
    old_name_pict = paths_lst[-1]
    #  Создаю путь
    if new_path:
        path_pict = new_path
    else:
        paths_only_lst = paths_lst[:-1]
        path_pict = '/'.join(paths_only_lst)
    if path_pict[-1] != '/':
        path_pict += '/'
    #  Создаю путь и имя
    new_name = f'{path_pict}{old_name_pict}_{modifier}.{path_name_lst[-1]}'
    return new_name
