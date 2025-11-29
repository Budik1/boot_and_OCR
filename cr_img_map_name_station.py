import color_text
import fun
import find_img
import sounds
import baza_dannyx as b_d



def fashion():
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
    name_create_img = 'img/tonelli/map_item/k_Suxarev.png'
    name_create_img = 'img/tonelli/map_item/k_Prospekt.png'
    name_create_img = 'img/tonelli/map_item/k_Rizgskaya.png'
    name_create_img = 'img/tonelli/map_item/k_Alexs.png'
    name_create_img = 'img/tonelli/map_item/k_VDNX.png'

    pos_start = find_img.find_station_exit()

    map_dict = {
        'img/tonelli/station_exit.png': (522, 555, 249, 35),
        'img/tonelli/map_item/k_Park_kr.png': (-60, 213, 113, 32, 'с фрунзе'),
        'img/tonelli/map_item/k_Park_ganza.png': (-60, 304, 113, 32, 'с Парк-кр'),
        'img/tonelli/map_item/k_Frunze.png': (45, 343, 120, 32, 'с Парк-кр'),
        'img/tonelli/map_item/k_Kiev.png': (-7, 119, 98, 32, 'с Парк-г'),
        'img/tonelli/map_item/k_Kiev_a.png': (-40, 296, 90, 32, 'с Киевской'),
        'img/tonelli/map_item/k_Communist.png': (46, 352, 120, 32, 'с фрунзе'),
        'img/tonelli/map_item/k_Univer.png': (46, 404, 120, 32, 'с Коммун'),
        'img/tonelli/map_item/k_Pr-kt_Vernadskogo.png': (46, 456, 200, 32),
        'img/tonelli/map_item/k_Kropotkin.png': (140, 205, 145, 32),
        'img/tonelli/map_item/k_Biblioteka.png': (-28, 179, 200, 32, 'с кропот'),
        'img/tonelli/map_item/k_Borov.png': (243, 244, 110, 32, 'с Biblioteka'),
        'img/tonelli/map_item/k_Polyanka.png': (192, 352, 80, 32, 'с Borov'),
        'img/tonelli/map_item/k_Chekhov.png': (192, 114, 95, 32, 'с Borov'),
        'img/tonelli/map_item/k_Pushkin.png': (-3, 194, 113, 32, 'с Chekhov'),
        'img/tonelli/map_item/k_Cvetnoy.png': (50, 157, 130, 32, 'с Chekhov'),
        'img/tonelli/map_item/k_Teatr.png': (337, 444, 70, 32, 'с Tver'),
        'img/tonelli/map_item/k_Tver.png': (30, 243, 86, 32, 'с Chekhov'),
        'img/tonelli/map_item/k_Novokuznec.png': (240, 457, 86, 23, 'с Teatr'),
        'img/tonelli/map_item/k_Tretyakov.png': (-10, 271, 86, 32, 'с Novokuznec'),
        'img/tonelli/mark_sever.png': (144, 27, 50, 32),
        'img/tonelli/mark_yug.png': (144, 487, 50, 32),
        'img/tonelli/map_item/k_Kuzneckiy.png': (332, 257, 86, 32, 'с Pushkin'),
        'img/tonelli/map_item/k_Pavelec.png': (296, 361, 100, 32, 'с Pushkin'),
        'img/tonelli/map_item/k_Pavelec_g.png': (249, 290, 106, 32, 'с Pavelec'),
        'img/tonelli/map_item/k_Kitay.png': (299, 152, 100, 32, 'с Tretyakov'),
        'img/tonelli/map_item/k_Turgenev.png': (151, 169, 124, 32, 'с Kitay'),
        'img/tonelli/map_item/k_Suxarev.png': (173, 186, 116, 32, 'с Turgenev'),
        'img/tonelli/map_item/k_Prospekt.png': (110, 138, 133, 32, 'с Suxarev'),
        'img/tonelli/map_item/k_Rizgskaya.png': (120, 207, 75, 32, 'с Prospekt'),
        'img/tonelli/map_item/k_Alexs.png': (78, 180, 124, 32, 'с Rizgskaya'),
        'img/tonelli/map_item/k_VDNX.png': (149, 127, 55, 32, 'с Rizgskaya'),

    }

    # name_create_img = 'img/test/token.png'
    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        # показать привязку
        key = 'img/tonelli/map_item/k_VDNX.png'
        # найдем верхний угол
        x, y = pos_start
        x += map_dict[key][0]
        y += map_dict[key][1]
        # fun.mouse_move(pos=(x, y), speed=1, show=show_move)
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = map_dict[key][2]
        change_y = map_dict[key][3]
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
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
        q = input(f"{name_create_img} сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            print(f'{name_create_img} сделано')
        else:
            pass
    pos = fun.locCenterImg(f'{name_create_img}')
    # fun.mouse_move(pos=pos)
    sounds.sound_vic()
    # print(f'{name_create_img} сделано')
    # check_img(name=name_create_img)
    return


def check_img(*, name=None):
    img_check = name
    if name:
        pos = fun.locCenterImg(img_check, confidence=0.99)
        if pos:
            # fun.Mouse.move(pos=pos, speed=1)
            print(color_text.tc_green('Найден'))
        else:
            print(color_text.tc_red('не найден'))
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
    # fun.mouse_move(pos=pos_start, speed=1)

    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        # показать привязку
        key = 'img/tonelli/attack.png'
        # найдем верхний угол
        x, y = pos_start
        x += map_dict[key][0]
        y += map_dict[key][1]
        # fun.mouse_move(pos=(x, y), speed=1)
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = map_dict[key][2]
        change_y = map_dict[key][3]
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
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




# check_img(name='img/tonelli/map_item/k_Park_kr.png')
fashion()
# entry_img()
