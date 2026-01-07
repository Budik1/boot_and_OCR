import os
import fun
import find_img
from PIL import Image


def tests_img_value_energy():
    master = find_img.find_station_master()
    fun.Mouse.move(pos=master)
    list_value_energy = ['en_1', 'en_2', 'en_3', 'en_4', 'en_5', 'en_7', ]  # 'en_6',
    for value_energy in list_value_energy:
        name_file = f'img/station_master/energy_value/{value_energy}.png'
        pos_img = fun.locCenterImg(name_img=name_file, confidence=0.93)
        if pos_img:
            print(value_energy)
            fun.Mouse.move(pos=pos_img, speed=1)


def cr_box_loot_img(*, name_create_img):
    """
    Создание большой картинки содержимого подарка на станции для дальнейшей обработки.
    :param name_create_img: Имя картинки.
    :return:
    """
    img_map = (-54, -140, 119, 119,)
    # от чего оттолкнуться
    pos_start = find_img.find_close()
    # # найдем верхний угол
    x, y = pos_start
    x += img_map[0]
    y += img_map[1]
    # # найдем нижний угол
    change_x = img_map[2]
    change_y = img_map[3]
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    return


def tenderloin(*, name_fold, name_crop_img):
    """
    Обрезка большой картинки содержимого подарка на станции на два фрагмента, где возможны изображения.
    :param name_fold:
    :param name_crop_img:
    :return:
    """
    down_obl = [50, 50, 59, 59, f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}_down.png']
    up_obl = [25, 5, 88, 30, f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}_up.png']
    name_open = f'img/tonelli/loot_gift_box/big/buf/{name_crop_img}.png'
    img = Image.open(name_open)
    #  box=(left, upper, right, lower)
    for i in [down_obl, up_obl]:
        left = i[0]
        upper = i[1]
        right = i[2] + left
        lower = i[3] + upper
        img_crop = img.crop((left, upper, right, lower))
        img_crop.save(i[4])
    # И удаление исходного файла
    # os.remove(name_open)
    return


def check_loot(*, name_hero_dir):
    """
    Ищет совпадения из общей папки и папки героя.
    Возвращает имя файла без расширения. Или 'None' в случае отсутствия совпадений.
    :param name_hero_dir:
    :return:
    """
    name_img_ = None
    directory_big_hero = f'img/tonelli/loot_gift_box/big/{name_hero_dir}'
    directory_big_all = 'img/tonelli/loot_gift_box/big/all'
    list_dir_hero = os.listdir(directory_big_hero)
    list_dir_all = os.listdir(directory_big_all)
    list_dir_general = []
    for item in list_dir_all:
        list_dir_general.append(f'{directory_big_all}/{item}')
    for item in list_dir_hero:
        list_dir_general.append(f'{directory_big_hero}/{item}')
    for img in list_dir_general:
        pos_img = fun.locCenterImg(name_img=img, confidence=0.99)
        if pos_img:
            # отсечка img
            name_img_list = (img.split('/')[-1]).split('.')
            name_img_ = name_img_list[0]
            break
    return name_img_

