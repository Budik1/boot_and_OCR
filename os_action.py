import os
import time

import tools
from baza import variables as var

hour = 3600
day = 24 * 3600
two_weeks = 14 * 24 * 3600

qty_del_files = 0


def chek_and_del_file(*, check_file, old_day):
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


def check_files(*, old_day: int, check_list_directory):
    """
    Процедура проверки и удаления файлов.
    :param check_list_directory:
    :param old_day: Срок хранения.
    :return:
    """
    qty_filez_verif = 0
    for directory in check_list_directory:
        file_list = os.listdir(directory)
        for file in file_list:
            qty_filez_verif += 1
            file_path = directory + file
            chek_and_del_file(check_file=file_path, old_day=old_day)
    word_file = tools.transform_word_file(qty_files=qty_filez_verif)
    print(f'{qty_filez_verif} {word_file} прошли проверку. {var.qty_del_files} удалено')
    print()
    return qty_filez_verif,


def create_folder(path, info=False):
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


