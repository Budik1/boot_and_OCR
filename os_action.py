import os
import time

import baza_paths as b_p
import fun

hour = 3600
day = 24 * 3600
two_weeks = 14 * 24 * 3600

qty_del_files = 0


def chek_and_del_file(*, check_file, old_day):
    global qty_del_files
    creation_time = get_data_creation_file(check_file=check_file)
    time_now = time.time()
    if int((time_now - creation_time) // day) >= old_day:
        qty_del_files += 1
        os.remove(check_file)


def get_data_creation_file(*, check_file):
    """
    Дата создания файла доступна через функцию os.path.getctime(). Она возвращает время создания файла в секундах
    с эпохи (1 января 1970 года). Если нужно вывести дату в читаемом для человека формате, можно использовать
    функцию ctime() из модуля time
    :param check_file:
    :return:
    """
    file_stats = os.stat(check_file)
    creation_time = file_stats.st_ctime
    # print("The file was created on:", time.ctime(creation_time))
    # (https://www.slingacademy.com/article/python-getting-creation-date-file-directory/)
    return creation_time


def check_files(*, old_day):
    global qty_del_files
    chek_list_directory = b_p.chek_list_directory
    qty_filez = 0
    for directory in chek_list_directory:
        file_list = os.listdir(directory)
        for file in file_list:
            qty_filez += 1
            file_path = directory + file
            chek_and_del_file(check_file=file_path, old_day=old_day)
    word_file = fun.transform_word_file(qty_files=qty_filez)
    print(f'{qty_filez} {word_file} прошли проверку. {qty_del_files} удалено')
