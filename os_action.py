import os
import time

import tools
from baza import variables as var

hour = 3600
day = 24 * 3600
two_weeks = 14 * 24 * 3600


def check_and_del_file(*, check_file, old_day):
    creation_time = get_data_creation_file(check_file=check_file, info=False)
    time_now = time.time()
    if int((time_now - creation_time) // day) >= old_day:
        var.qty_del_files += 1
        os.remove(check_file)


def get_data_creation_file(*, check_file, info=False):
    """
    Дата создания файла доступна через функцию os.path.getctime(). Она возвращает время создания файла в секундах
    с эпохи (1 января 1970 года). Если нужно вывести дату в читаемом для человека формате, можно использовать
    функцию ctime() из модуля time
    :param check_file:
    :param info: В состоянии True выводит в консоль дату создания
    :return:
    """
    file_stats = os.stat(check_file)
    creation_time = file_stats.st_ctime
    if info:
        days = time.ctime(creation_time)
        # print(type(days))
        print("The file was created on:", days)
    # (https://www.slingacademy.com/article/python-getting-creation-date-file-directory/)
    return creation_time


def check_files(*, old_day: int, check_list_directory=None, check_list_file=None):
    """
    Процедура проверки и удаления файлов.
    :param check_list_directory: Список директорий.
    :param check_list_file: Список файлов.
    :param old_day: Срок хранения.
    :return:
    """
    qty_filez_verif = 0
    if check_list_directory:
        for directory in check_list_directory:
            file_list = os.listdir(directory)
            for file in file_list:
                qty_filez_verif += 1
                file_path = directory + file
                print(f'{file_path=}')
                check_and_del_file(check_file=file_path, old_day=old_day)
    elif check_list_file:
        for file in check_list_file:
            qty_filez_verif += 1
            check_and_del_file(check_file=file, old_day=old_day)
    word_file = tools.transform_word_file(qty_files=qty_filez_verif)
    word_day = tools.transform_word_days(qty_days=old_day)
    # 177 файлов сроком хранения  прошли проверку. 0 удалено
    print(f'{qty_filez_verif} {word_file}, сроком хранения {old_day} {word_day}, прошли проверку. {var.qty_del_files} удалено')
    var.qty_del_files = 0
    return qty_filez_verif,


def create_folder(*, path, info=False):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        if info:
            print(f"Папка `{path}` уже существует, всё в порядке!")
    return


def check_folder(my_path):
    """
    :param my_path: Путь к папке или файлу.
    :return: Bool
    """
    return os.path.exists(path=my_path)


def get_lst_files(*, path):
    """
    Получение списка файлов во всех вложенных директориях начиная с 'path'
    :return: Список файлов
    """
    lst_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            lst_files.append(os.path.join(root, file))
    return lst_files


def get_lst_dirs(*, path):
    """
    Получение списка всех вложенных директорий начиная с 'path'
    :param path: Старт поиска.
    :return: Список вложенных директорий.
    """
    lst_dir = []
    for root, dirs, files in os.walk(path):
        for dir_ in dirs:
            lst_dir.append(os.path.join(root, dir_))
    return lst_dir


def deleting_empty_folders(path='temp_pack'):
    qty_folder_del = 0
    lst_dirs = get_lst_dirs(path=path)
    for check_dirs in lst_dirs:
        lst_check = os.listdir(str(check_dirs))
        if not lst_check:
            qty_folder_del += 1
            os.rmdir(check_dirs)
    print(f'Удалено {qty_folder_del} пустых директорий')
    print()
