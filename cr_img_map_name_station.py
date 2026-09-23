import tools

import tools.color_text as c_t
import fun
import find_img
from tools import sounds


def img_map_name():
    """
        образец
        """
    show_move = True
    # name_create_img = 'img/tonelli/station_exit.png'
    # name_create_img = 'img/tonelli/map_item/k_Park_kr.png'
    # name_create_img = 'img/tonelli/map_item/k_Park_ganza.png'
    # name_create_img = 'img/tonelli/map_item/k_Frunze.png'
    # name_create_img = 'img/tonelli/map_item/k_Kiev.png'
    # name_create_img = 'img/tonelli/map_item/k_Kiev_a.png'
    # name_create_img = 'img/tonelli/map_item/k_Communist.png'
    # name_create_img = 'img/tonelli/map_item/k_Univer.png'
    # name_create_img = 'img/tonelli/map_item/k_Pr-kt_Vernadskogo.png'
    # name_create_img = 'img/tonelli/map_item/k_Kropotkin.png'
    # name_create_img = 'img/tonelli/map_item/k_Biblioteka.png'
    # name_create_img = 'img/tonelli/map_item/k_Borov.png'
    # name_create_img = 'img/tonelli/map_item/k_Polyanka.png'
    # name_create_img = 'img/tonelli/map_item/k_Chekhov.png'
    # name_create_img = 'img/tonelli/map_item/k_Pushkin.png'
    # name_create_img = 'img/tonelli/map_item/k_Cvetnoy.png'
    # name_create_img = 'img/tonelli/map_item/k_Teatr.png'
    # name_create_img = 'img/tonelli/map_item/k_Tver.png'
    # name_create_img = 'img/tonelli/map_item/k_Novokuznec.png'
    # name_create_img = 'img/tonelli/map_item/k_Tretyakov.png'
    # name_create_img = 'img/tonelli/mark_sever.png'
    # name_create_img = 'img/tonelli/mark_yug.png'
    # name_create_img = 'img/tonelli/map_item/k_Kuzneckiy.png'
    # name_create_img = 'img/tonelli/map_item/k_Pavelec.png'
    # name_create_img = 'img/tonelli/map_item/k_Pavelec_g.png'
    # name_create_img = 'img/tonelli/map_item/k_Kitay.png'
    # name_create_img = 'img/tonelli/map_item/k_Turgenev.png'
    # name_create_img = 'img/tonelli/map_item/k_Suxarev.png'
    # name_create_img = 'img/tonelli/map_item/k_Prospekt.png'
    # name_create_img = 'img/tonelli/map_item/k_Rizgskaya.png'
    # name_create_img = 'img/tonelli/map_item/k_Alexs.png'
    # name_create_img = 'img/tonelli/map_item/k_VDNX.png'

    pos_start = find_img.find_station_exit()

    map_dict = {
        'img/default/tonelli/map_item/k_Sport.png': (46, 413, 110, 31, 'с фрунзе'),
        'img/default/tonelli/map_item/k_Univer.png': (46, 465, 120, 32, 'с Спортивной'),
        'img/default/tonelli/map_item/k_Pr-kt_Vernadskogo.png': (46, 517, 200, 32),
        'img/default/tonelli/map_item/k_Frunze.png': (45, 373, 120, 32, 'с Парк-кр'),
        'img/default/tonelli/map_item/k_Kropotkin.png': (140, 235, 145, 32),
        'img/default/tonelli/map_item/k_Park_ganza.png': (-60, 334, 113, 32, 'с Парк-кр'),
        'img/default/tonelli/map_item/k_Park_kr.png': (-60, 273, 113, 32, 'с фрунзе'),
        'img/default/tonelli/map_item/k_Kiev.png': (-7, 179, 98, 32, 'с Парк-г'),
        'img/default/tonelli/map_item/k_Kiev_a.png': (-40, 326, 90, 32, 'с Киевской'),

        'img/tonelli/station_exit.png': (522, 555, 249, 35),


        'img/default/tonelli/map_item/k_Communist.png': (46, 352, 120, 32, 'с фрунзе'),

        'img/default/tonelli/map_item/k_Biblioteka.png': (-28, 179, 200, 32, 'с кропот'),
        'img/default/tonelli/map_item/k_Borov.png': (243, 244, 110, 32, 'с Biblioteka'),
        'img/default/tonelli/map_item/k_Polyanka.png': (192, 352, 80, 32, 'с Borov'),
        'img/default/tonelli/map_item/k_Chekhov.png': (192, 114, 95, 32, 'с Borov'),
        'img/default/tonelli/map_item/k_Pushkin.png': (-3, 194, 113, 32, 'с Chekhov'),
        'img/default/tonelli/map_item/k_Cvetnoy.png': (50, 157, 130, 32, 'с Chekhov'),
        'img/default/tonelli/map_item/k_Teatr.png': (337, 444, 70, 32, 'с Tver'),
        'img/default/tonelli/map_item/k_Tver.png': (30, 243, 86, 32, 'с Chekhov'),
        'img/default/tonelli/map_item/k_Novokuznec.png': (240, 457, 86, 23, 'с Teatr'),
        'img/default/tonelli/map_item/k_Tretyakov.png': (-10, 271, 86, 32, 'с Novokuznec'),
        'img/default/tonelli/mark_sever.png': (144, 27, 50, 32),
        'img/default/tonelli/mark_yug.png': (144, 487, 50, 32),
        'img/default/tonelli/map_item/k_Kuzneckiy.png': (332, 257, 86, 32, 'с Pushkin'),
        'img/default/tonelli/map_item/k_Pavelec.png': (296, 361, 100, 32, 'с Pushkin'),
        'img/default/tonelli/map_item/k_Pavelec_g.png': (249, 290, 106, 32, 'с Pavelec'),
        'img/default/tonelli/map_item/k_Kitay.png': (299, 152, 100, 32, 'с Tretyakov'),
        'img/default/tonelli/map_item/k_Turgenev.png': (151, 169, 124, 32, 'с Kitay'),
        'img/default/tonelli/map_item/k_Suxarev.png': (173, 186, 116, 32, 'с Turgenev'),
        'img/default/tonelli/map_item/k_Prospekt.png': (110, 138, 133, 32, 'с Suxarev'),
        'img/default/tonelli/map_item/k_Rizgskaya.png': (120, 207, 75, 32, 'с Prospekt'),
        'img/default/tonelli/map_item/k_Alexs.png': (78, 180, 124, 32, 'с Rizgskaya'),
        'img/default/tonelli/map_item/k_VDNX.png': (149, 127, 55, 32, 'с Rizgskaya'),

    }

    test_img = 'img/temp/token.png'
    path_img = 'img/default/tonelli/map_item/'
    name_create_img = f'{path_img}k_Kiev_a.png'
    x, y = pos_start
    # tools.Mouse.move(pos=(x, y), speed=1, show=show_move)
    x += map_dict[name_create_img][0]
    y += map_dict[name_create_img][1]
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = map_dict[name_create_img][2]
    change_y = map_dict[name_create_img][3]
    x_demo += change_x
    y_demo += change_y
    q = input(f"{name_create_img} сохранить?(y/n) Или сделать {test_img} (t): ")
    if q == 'y':
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        print(f'{name_create_img} сделано')
    elif q == 't':
        fun.foto(f'{test_img}', (x, y, change_x, change_y))
        print(f'{test_img} сделано')
    else:
        pass
    # pos = fun.locCenterImg(f'{name_create_img}')
    # fun.Mouse.move(pos=pos)
    # sounds.sound_vic()
    # print(f'{name_create_img} сделано')
    # check_img(name=name_create_img)
    return


def name_id_station():
    """
    Добавить название файла в конец списка.
    Создать(заменить) файл
           """
    names_list = [
        'img/default/tonelli/id_stations/s_Communist.png',
        'img/default/tonelli/id_stations/s_Frunze.png',
        'img/default/tonelli/id_stations/s_Park_kr.png',
        'img/default/tonelli/id_stations/s_Park_ganza.png',
        'img/default/tonelli/id_stations/s_Kiev.png',
        'img/default/tonelli/id_stations/s_Kropotkin.png',
        'img/default/tonelli/id_stations/s_Biblioteka.png',
        'img/default/tonelli/id_stations/s_Borov.png',
        'img/default/tonelli/id_stations/s_Polyanka.png',
        'img/default/tonelli/id_stations/s_Chekhov.png',
        'img/default/tonelli/id_stations/s_Tver.png',
        'img/default/tonelli/id_stations/s_Pushkin.png',
        'img/default/tonelli/id_stations/s_Kuzneckiy.png',
        'img/default/tonelli/id_stations/s_Cvetnoy.png',
        'img/default/tonelli/id_stations/s_Teatr.png',
        'img/default/tonelli/id_stations/s_Novokuznec.png',
        'img/default/tonelli/id_stations/s_Pavelec.png',
        'img/default/tonelli/id_stations/s_Pavelec_g.png',
        'img/default/tonelli/id_stations/s_Tretyakov.png',
        'img/default/tonelli/id_stations/s_Kitay.png',
        'img/default/tonelli/id_stations/s_Turgenev.png',
        'img/default/tonelli/id_stations/s_Suxarev.png',
        'img/default/tonelli/id_stations/s_Prospekt.png',
        'img/default/tonelli/id_stations/s_Rizgskaya.png',
        'img/default/tonelli/id_stations/s_Alexs.png',
        'img/default/tonelli/id_stations/s_VDNX.png',

        'img/default/tonelli/id_stations/s_Kiev.png',
        'img/default/tonelli/id_stations/s_Park_ganza.png',
        'img/default/tonelli/id_stations/s_Park_kr.png',
        'img/default/tonelli/id_stations/s_Frunze.png',
        'img/default/tonelli/id_stations/s_Sport.png',
        'img/default/tonelli/id_stations/s_Univer.png',
        'img/default/tonelli/id_stations/s_Pr-kt_Vernadskogo.png',

    ]
    test_img = 'img/temp/token.png'
    name_create_img = names_list[-1]
    show_move = False
    pos_start = find_img.find_info()
    # показать привязку
    tools.Mouse.move(pos=pos_start, speed=1, show=show_move)
    # найдем верхний угол
    x, y = pos_start
    x += 80
    y += 450
    tools.Mouse.move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 370
    change_y = 27
    x_demo += change_x
    y_demo += change_y
    tools.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    q = input(f"{name_create_img} сохранить?(y/n) Или сделать {test_img} (t): ")
    if  q == 'y':
        fun.foto(path_name=name_create_img, region=(x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{name_create_img}')
        tools.Mouse.move(pos=pos, show=show_move)
        print(f'{name_create_img}сделано')
    elif q == 't':
        fun.foto(path_name=test_img, region=(x, y, change_x, change_y))
        print(f'{test_img} сделано')
    else:
        pass
    return


def check_img(*, name=None):
    img_check = name
    if name:
        pos = fun.locCenterImg(img_check, confidence=0.99)
        if pos:
            # fun.Mouse.move(pos=pos, speed=1)
            print(name)
            print(c_t.tc_green('Найден'))
        else:
            print(name)
            print(c_t.tc_red('не найден'))
    return


def entry_img():
    # name_create_img = 'img/tonelli/entry_station.png'
    name_create_img = 'img/tonelli/attack.png'
    # name_create_img = 'img/test/token.png'
    map_dict = {
        'img/tonelli/entry_station.png': (-136, 278, 147, 21),
        'img/tonelli/attack.png': (-116, 425, 106, 32),
    }
    pos_start = fun.locCenterImg('img/tonelli/post.png')
    # fun.Mouse.move(pos=pos_start, speed=1)

    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        # показать привязку
        key = 'img/tonelli/attack.png'
        # найдем верхний угол
        x, y = pos_start
        x += map_dict[key][0]
        y += map_dict[key][1]
        # fun.Mouse.move(pos=(x, y), speed=1)
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = map_dict[key][2]
        change_y = map_dict[key][3]
        x_demo += change_x
        y_demo += change_y
        # fun.Mouse.move(pos=(x_demo, y_demo), show=show_move)
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        print(f'{name_create_img} сделано')
    else:
        x, y = pos_start
        x += map_dict[name_create_img][0]
        y += map_dict[name_create_img][1]
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = map_dict[name_create_img][2]
        change_y = map_dict[name_create_img][3]
        x_demo += change_x
        y_demo += change_y
        q = input(f"{name_create_img}сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            print(f'{name_create_img} сделано')
        else:
            pass
    sounds.sound_vic()
    return


# img_map_name()
# name_id_station()
check_img(name='img/default/tonelli/map_item/k_Frunze.png')