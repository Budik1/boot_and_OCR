"""
Заготовки взяты из a_pil_image.py
Заготовки взяты из t_item.py

Создать большую картинку заданий для дальнейшей работы.
Обрезать малые значения одинаково.
Убрать цвет.
Прочитать.
"""

import my_OCR
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

import fun
import sounds
import baza_paths as b_p
import mod_wold


def conversion_to_gray(*, name_img):
    """
    Для конвертирования в оттенки серого.
    Создаёт новое имя.
    :return:
    """
    # (https://www.codespeedy.com/remove-a-specific-color-from-an-image-in-python/)
    # Откройте изображение
    image = Image.open(name_img)
    # Конвертируйте в оттенки серого методом 'L'
    image = image.convert('L')
    # Создайте новое имя файла добавив символы изменения.
    new_name_img = mod_wold.modification_name(old_path_name=name_img, modifier='_gray')
    # Сохраните изображение
    image.save(new_name_img)
    return new_name_img


def ramki(*, name_file):
    # Загрузка изображения с помощью PIL
    image_pil = Image.open(name_file)
    # Преобразование изображения в массив numpy
    image_np = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    # Выполнение операции поиска краев
    edges = cv2.Canny(gray, 150, 200)
    # Создание холста для отображения итогового изображения и краев
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    # Отображение исходного изображения на холсте
    axs[0].imshow(image_pil)
    axs[0].axis('off')
    # Отображение краев на холсте
    axs[1].imshow(edges, cmap='gray')
    axs[1].axis('off')
    # Сохранение результата в файл
    result_image = Image.fromarray(edges)
    mod_name_file = mod_wold.modification_name(old_path_name=name_file, modifier='_edges')
    result_image.save(mod_name_file)
    # Отображение результата
    plt.show()


def get_ful_arial_task_img(*, name_hero):
    """
    Взят из cr_img_dva.py
    Создание полной картинки заданий
    :return:
    """
    # big_task: str = 'img/test/test_tasks/'
    path_img = b_p.task_test
    name_img = 'ful_arial_task.png'
    pos_start = fun.find_link_station_master()
    # найдем верхний угол
    x, y = pos_start
    x += 270 - 6
    y += 152 - 2
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 268  # - 6
    change_y = 260  # - 2
    x_demo += change_x
    y_demo += change_y
    # # собственно создание снимка
    name_new_file = f'{name_hero}_{name_img}'
    path_name_new_file = f'{path_img}{name_new_file}'
    lst_folder = os.listdir(path_img)
    print(f'{lst_folder=}')
    print(f'{name_new_file=}')
    if name_new_file in lst_folder:
        ask = input('Файл с таким именем существует. Перезаписать? (y/n)')
        if ask == 'y':
            fun.foto(path_name_new_file, (x, y, change_x, change_y))
            # sounds.sound_vic(block=False)
            print(f'{path_name_new_file} создан')
    else:
        fun.foto(path_name_new_file, (x, y, change_x, change_y))
        # sounds.sound_vic(block=False)
        print(f'{path_name_new_file} создан')
        print('ok')
    return path_name_new_file


def crop_smol_task_img(*, name_open):
    lst_names = []
    img = Image.open(name_open)
    pul_1_line = [195, 42, 44, 31, f'_xp_1_line']
    for i in [pul_1_line]:
        left = i[0]
        upper = i[1]
        right = i[2] + left
        lower = i[3] + upper
        #  box=(left, upper, right, lower)
        img_crop = img.crop((left, upper, right, lower))
        new_name = mod_wold.modification_name(old_path_name=name_open, modifier=i[4])
        img_crop.save(new_name)
        lst_names.append(new_name)
    return lst_names


def crop_big_task_img(*, name_open):
    lst_names = []
    img = Image.open(name_open)
    pul_1_line = [130, 36, 120, 42, f'_xp_1_line']
    for i in [pul_1_line]:
        left = i[0]
        upper = i[1]
        right = i[2] + left
        lower = i[3] + upper
        #  box=(left, upper, right, lower)
        img_crop = img.crop((left, upper, right, lower))
        new_name = mod_wold.modification_name(old_path_name=name_open, modifier=i[4])
        img_crop.save(new_name)
        lst_names.append(new_name)
    return lst_names


def new_big_task_img():
    name_hero = input('ВВеди имя героя: ')
    name = get_ful_arial_task_img(name_hero=name_hero)
    return name


def change_color(name_img):
    """
    Основной цвет (96, 107, 88)
    :return:
    """
    target_color = [
        (76, 76, 76),
        (89, 89, 89),
        (93, 93, 93),
        (97, 97, 97),
        (98, 98, 98),
        (99, 99, 99),
        (100, 100, 100),
        (101, 101, 101),
        (102, 102, 102),
        (103, 103, 103),
        (114, 114, 114),
        (198, 198, 198),
        (199, 199, 199),
        (200, 200, 200),
        (201, 201, 201),

    ]
    # replacement_color = (90, 90, 90)
    col_change = 20
    replacement_color = (col_change, col_change, col_change)
    list_color_1 = []
    list_color_2 = []
    qty_point = 0

    image_open = Image.open(name_img)
    image_rgb = image_open.convert("RGB")
    width, height = image_rgb.size
    for x in range(width):
        for y in range(height):
            # Получаем цвет пикселя
            pixel_color = image_rgb.getpixel((x, y))
            list_color_1.append(pixel_color)
    set_color_2 = set(list_color_1)
    print(f'Количество цветов до обработки {len(set_color_2)} в {name_img}')
    # for color in set_color:
    #     # print(set_color)
    #     print(color)
    tar_col = []
    for i in range(202):  # 202
        # print(i+20)
        tar_col.append((i + 20, i + 20, i + 20))
    for x in range(width):
        for y in range(height):
            pixel_color = image_rgb.getpixel((x, y))
            # Если цвет пикселя равен целевому цвету, заменяем его на новый цвет
            if pixel_color in tar_col:
                image_rgb.putpixel((x, y), replacement_color)
                qty_point += 1
    mod_name = mod_wold.modification_name(old_path_name=name_img, modifier='_gr')
    image_rgb.save(mod_name)
    print(f'Количество измененных точек {qty_point}')
    image_gr = Image.open(mod_name)
    for x in range(width):
        for y in range(height):
            # Получаем цвет пикселя
            pixel_color = image_gr.getpixel((x, y))
            list_color_2.append(pixel_color)
    set_color_2 = set(list_color_2)
    print(f'Количество цветов после обработки {len(set_color_2)} {mod_name}')
    return mod_name


n1 = new_big_task_img()
lst_n = crop_smol_task_img(name_open=n1)
# lst_n = crop_smol_task_img(name_open='img/test/areas_task1.png')
# lst_n_b = crop_big_task_img(name_open='img/test/test_img/mara_ful_arial_task.png')
# n_i = conversion_to_gray(name_img=lst_n_b[0])
# n_i = conversion_to_gray(name_img="img/test/areas_task1.png")
# n_i2 = change_color(name_img=n_i)
# print(n_i2)
# res = my_OCR.recognized(file_path=n_i2)
# print(res)
