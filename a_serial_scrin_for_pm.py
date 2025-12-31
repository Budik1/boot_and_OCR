import color_text
import find_img
import fun
import sounds
import person
# import create_and_analiz_img

# import a_servis


# Создание картинок значения энергии.
def energy_img():
    """
    Создание картинок значения энергии.
    a_servis.tests_img_value_energy() для проверки наличия
    """
    pos_mark = find_img.find_station_master()
    # name_create_img = 'img/test/token.png'
    # проверить видимость
    list_en = ['en_2.png', 'en_3.png', 'en_4.png', 'en_5.png', 'en_7.png']  # 'en_1.png',
    print(color_text.tc_cyan('Проверка'))
    for img_ in list_en:
        name_img = f'img/station_master/energy_value/{img_}'
        en = fun.locCenterImg(name_img, confidence=0.95)
        if en:
            fun.Mouse.move(pos=pos_mark, speed=1)
            fun.Mouse.move(pos=en, speed=1)
            print(color_text.tc_green(img_))
    # если не видно - создать
    ask = input('Всё увидел (y/n): ')
    if ask == 'y':
        return
    else:
        nam_line = None
        val_en = None
        while not nam_line:
            try:
                nam_line = int(input('Введи номер нужной строки(цифрой): '))
                if 1 <= nam_line <= 3:
                    print('Хорошая цифра))')
                else:
                    print('Строк всего три))')
            except ValueError:
                print('Это должна быть цифра')
        while not val_en:
            try:
                val_en = int(input('Какое количество энергии на этой строке?(цифрой): '))
                if 1 <= val_en <= 7:
                    print(val_en, 'хорошо.')
                else:
                    print('надо от 1 до 7')
            except ValueError:
                print('Это должна быть цифра')

        name_create_img = f'img/station_master/energy_value/en_{val_en}.png'

        e_line = 128 + (90 * (nam_line - 1))
        e_line_1 = 128
        e_line_2 = 128 + 90
        e_line_3 = 128 + 90 + 90
        x, y = pos_mark
        x += 450
        # ----------
        y += e_line
        # ----------
        # fun.Mouse.move(pos=(x,y), speed=0.5)
        change_x = 45
        change_y = 28
        x_demo, y_demo = x, y
        x_demo += change_x
        y_demo += change_y
        # fun.Mouse.move(pos=(x_demo, y_demo), speed=0.5)
        msg = color_text.tc_red(f'{name_create_img} создан.')
        print(msg)
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))

        return


def hero_img():
    """
    Для создания иконок героев
    name_create_img = путь сохранения
    'img/test/token.png' путь тестовой картинки
    :return:
    """
    # name_create_img = 'img/test/token.png'
    # name_create_img = 'img/person/hero_id/gady/her_gadya.png'
    name_create_img = 'img/person/hero_id/mara/her_mara.png'
    # name_create_img = 'img/person/hero_id/gavr/her_gavr.png'
    # name_create_img = 'img/person/hero_id/gavr/gavr_armor.png'
    show_move = False
    pos_start = find_img.find_info()
    # показать привязку
    # fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 105
    y -= 55
    # fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 74
    change_y = 74
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # # собственно создание снимка
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    # fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return


def task_img():
    # create_and_analiz_img.analiz_task()
    pass


def cr_other_img(name_create_img='img/test/token.png'):
    """
    
    :return: 
    """
    # name_create_img = 'img/overall/event_entry/pos_t.png'
    # name_create_img = 'img/tonelli/gift2.png'
    # name_create_img = 'img/tonelli/gift.png'
    # name_create_img = 'img/tonelli/loot_gift_box/feed3.png'
    # name_create_img = 'img/tonelli/loot_gift_box/many.png'
    # name_create_img = 'img/tonelli/loot_gift_box/p3.png'
    # name_create_img = 'img/tonelli/loot_gift_box/p4.png'
    # name_create_img = 'img/tonelli/loot_gift_box/big/720.png'

    # name_create_img = 'img/tonelli/loot_gift_box/ng1.png'
    # name_create_img = 'img/tonelli/loot_gift_box/ng2.png'
    # name_create_img = 'img/tonelli/loot_gift_box/ng3.png'
    # name_create_img = 'img/tonelli/loot_gift_box/ng4.png'
    # name_create_img = 'img/tonelli/loot_gift_box/marc30.png'

    # name_create_img = 'img/station_master/any/work_b.png'
    # name_create_img = 'img/station_master/work_hour/work_30m.png'
    # name_create_img = 'img/station_master/work_hour/work_1h.png'
    # name_create_img = 'img/station_master/work_hour/work_2h.png'
    # name_create_img = 'img/station_master/work_hour/work_5h.png'
    # name_create_img = 'img/station_master/work_hour/work_8h.png'
    # name_create_img = 'img/overall/klan.png'
    # name_create_img = 'img/kv/kv_attak.png'
    name_create_img = 'img/overall/knob.png'

    img_dict = {
        'img/b_battle_end.png': (-330, -404, 170, 30, (), find_img.find_close()),
        'img/station_master/energy_indicator/low_energy_label.png': (-274, -140, 320, 120, (), find_img.find_close()),
        'img/kv/kv_attack for money.png': (-145, 275, 220, 40, (), find_img.find_kv_reload()),
        'img/kv/kv_attak.png': (-145, 275, 220, 40, (), find_img.find_kv_reload()),
        'img/overall/link_money_token.png': (389, -55, 32, 32, (), find_img.find_info()),
        'img/overall/klan.png': (33, -13, 37, 32, (), find_img.find_info()),
        'img/kv/kv_skip_battle.png': (-48, -21, 96, 37, (), find_img.find_kv_skip_battle_test()),
        'img/overall/event_entry/pos_t.png': (246, -85, 32, 62, (), find_img.find_info()),
        'img/tonelli/gift2.png': (148, 313, 32, 19, (), find_img.find_info()),
        'img/tonelli/gift.png': (160, 315, 20, 19, (), find_img.find_info()),
        'img/tonelli/loot_gift_box/feed3.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/tonelli/loot_gift_box/many.png': (30, -134, 28, 27, (), find_img.find_close()),

        'img/tonelli/loot_gift_box/big/720.png': (-54, -140, 119, 119, (), find_img.find_close()),

        'img/tonelli/loot_gift_box/p3.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/tonelli/loot_gift_box/p4.png': (-4, -90, 60, 59, (), find_img.find_close()),

        'img/tonelli/loot_gift_box/ng1.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/tonelli/loot_gift_box/ng2.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/tonelli/loot_gift_box/ng3.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/tonelli/loot_gift_box/ng4.png': (-4, -90, 60, 59, (), find_img.find_close()),

        'img/tonelli/loot_gift_box/marc1.png': (-4, -90, 60, 59, (), find_img.find_close()),
        'img/station_master/any/work_b.png': (405, -6, 65, 29, (), find_img.find_station_master()),
        'img/station_master/work_hour/work_30m.png': (250, 137, 160, 27, (), find_img.find_station_master()),
        'img/station_master/work_hour/work_1h.png': (250, 194, 160, 25, (), find_img.find_station_master()),
        'img/station_master/work_hour/work_2h.png': (250, 260, 160, 25, (), find_img.find_station_master()),
        'img/station_master/work_hour/work_5h.png': (250, 260+65, 160, 25, (), find_img.find_station_master()),
        'img/station_master/work_hour/work_8h.png': (250, 260+65+65, 160, 25, (), find_img.find_station_master()),

        'img/overall/knob.png': (-496, -463, 16, 16, (), find_img.find_close()),

    }
    # name_create_img = 'img/test/token.png'

    key = 'img/overall/knob.png'
    pos_start = img_dict[key][5]

    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        # показать привязку
        # fun.mouse_move(pos=(pos_start), speed=1)
        # найдем верхний угол
        x, y = pos_start
        x += img_dict[key][0]
        y += img_dict[key][1]
        # fun.mouse_move(pos=(x, y), speed=1)
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = img_dict[key][2]
        change_y = img_dict[key][3]
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        print(f'{name_create_img} сделан')
    else:
        if key != name_create_img:
            x, y = pos_start
            x += img_dict[key][0]
            y += img_dict[key][1]
            # # найдем нижний угол
            x_demo, y_demo = x, y
            change_x = img_dict[key][2]
            change_y = img_dict[key][3]
            x_demo += change_x
            y_demo += change_y
        else:
            x, y = pos_start
            x += img_dict[name_create_img][0]
            y += img_dict[name_create_img][1]
            # # найдем нижний угол
            x_demo, y_demo = x, y
            change_x = img_dict[name_create_img][2]
            change_y = img_dict[name_create_img][3]
            x_demo += change_x
            y_demo += change_y
        q = input(f"{name_create_img}  сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            print(f'{name_create_img} сделано')
        else:
            pass
    # pos = fun.locCenterImg(f'{name_create_img}')
    # fun.mouse_move(pos=pos)
    sounds.sound_vic()
    # print(f'{name_create_img} сделано')
    # check_img(name=name_create_img)
    return


def mob_name(name=None):
    print(color_text.tc_green('cr_name_mob_img.mob_name'))
    skip_battle = fun.locCenterImg('img/overall/skip_battle.png')
    skip_battle1 = fun.locCenterImg('img/skip_battle.png')
    print(f'{skip_battle1=}')
    print(f'{skip_battle=}')
    while not skip_battle:
        skip_battle = fun.locCenterImg('img/overall/skip_battle.png')
    if skip_battle:
        x, y = skip_battle
        x += 70
        y -= 18
        # fun.mouse_move(pos=(x, y), speed=1)
        # sleep(1)
        x_demo, y_demo = x, y
        change_x = 160
        change_y = 25
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo))
        fun.foto(f'img/tonelli/mobi/{name}.png', (x, y, change_x, change_y))


def mob_id(name):
    print(color_text.tc_green('cr_name_mob_img.mob_id'))
    q_print = 1
    con = 0.99
    print(f'поиск {name}')
    skip_battle = fun.locCenterImg('img/overall/skip_battle.png')
    # skip_battle1 = fun.locCenterImg('img/skip_battle.png')
    # print(f'{skip_battle=}')
    while not skip_battle:
        skip_battle = fun.locCenterImg('img/overall/skip_battle.png')
        # skip_battle1 = fun.locCenterImg('img/skip_battle.png')
        if q_print > 0:
            print(f'{skip_battle=}')
        q_print -= 1

    # sleep(2)
    # 1
    # серая *
    name_gray_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=con)
    # черная *
    name_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=con)
    # белая *
    name_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=con)
    # песчаная *
    name_sand_rat = fun.locCenterImg('img/tonelli/mobi/name1_sand_rat.png', confidence=con)
    # 2 шпион
    name_spy = fun.locCenterImg('img/tonelli/mobi/name2_spy.png', confidence=con)
    # 3 контра
    name_smuggler = fun.locCenterImg('img/tonelli/mobi/name3_smuggler.png', confidence=con)
    # 4 паук
    name_arachne = fun.locCenterImg('img/tonelli/mobi/name4_arachne.png', confidence=con)
    # 5 дикарь *
    name_wildman = fun.locCenterImg('img/tonelli/mobi/name5_wildman.png', confidence=con)
    # 6 кикимора *
    name_kiki = fun.locCenterImg('img/tonelli/mobi/name6_kikimora.png', confidence=con)
    # 7 ящер *
    name_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=con)

    # 1 серая
    if name_gray_rat:
        fun.Mouse.move(pos=name_gray_rat, speed=0.5)
        print('серая крыса поймана')
        return
    # 1 белая
    elif name_white_rat:
        fun.Mouse.move(pos=name_white_rat, speed=0.5)
        print('белая крыса поймана')
        return
    # 1 черная
    elif name_black_rat:
        fun.Mouse.move(pos=name_black_rat, speed=0.5)
        print('черная крыса поймана')
        return
    # 1 песчаная
    elif name_sand_rat:
        fun.Mouse.move(pos=name_sand_rat, speed=0.5)
        print('песчаная крыса поймана')
        return
    # 2 шпион
    elif name_spy:
        fun.Mouse.move(pos=name_spy, speed=0.5)
        print('шпион пойман')
        return
    # 3 контра
    elif name_smuggler:
        fun.Mouse.move(pos=name_smuggler, speed=0.5)
        print('контра пойман')
        return
    # 4 паук
    elif name_arachne:
        fun.Mouse.move(pos=name_arachne, speed=0.5)
        print('арахна пойман')
        return
    # 5 дикарь
    elif name_wildman:
        print('ящер пойман')
        return
    # 6 кикимора
    elif name_kiki:
        print('кикимора пойман')
        return
    # 7 ящер
    elif name_raptor:
        print('ящер пойман')
        return
    # создание картинки
    else:
        print('моб не опознан')
        mob_name(name)
        print(f'результат "img/tonelli/mobi/{name}"')
        return


def name_id_station():
    """
    Добавить название файла в конец списка.
    Создать(заменить) файл
           """
    names_list = ['img/tonelli/id_stations/s_Pr-kt_Vernadskogo.png',
                  'img/tonelli/id_stations/s_Univer.png',
                  'img/tonelli/id_stations/s_Communist.png',
                  'img/tonelli/id_stations/s_Frunze.png',
                  'img/tonelli/id_stations/s_Park_kr.png',
                  'img/tonelli/id_stations/s_Park_ganza.png',
                  'img/tonelli/id_stations/s_Kiev.png',
                  'img/tonelli/id_stations/s_Kropotkin.png',
                  'img/tonelli/id_stations/s_Biblioteka.png',
                  'img/tonelli/id_stations/s_Borov.png',
                  'img/tonelli/id_stations/s_Polyanka.png',
                  'img/tonelli/id_stations/s_Chekhov.png',
                  'img/tonelli/id_stations/s_Tver.png',
                  'img/tonelli/id_stations/s_Pushkin.png',
                  'img/tonelli/id_stations/s_Kuzneckiy.png',
                  'img/tonelli/id_stations/s_Cvetnoy.png',
                  'img/tonelli/id_stations/s_Teatr.png',
                  'img/tonelli/id_stations/s_Novokuznec.png',
                  'img/tonelli/id_stations/s_Pavelec.png',
                  'img/tonelli/id_stations/s_Pavelec_g.png',
                  'img/tonelli/id_stations/s_Tretyakov.png',
                  'img/tonelli/id_stations/s_Kitay.png',
                  'img/tonelli/id_stations/s_Turgenev.png',
                  'img/tonelli/id_stations/s_Suxarev.png',
                  'img/tonelli/id_stations/s_Prospekt.png',
                  'img/tonelli/id_stations/s_Rizgskaya.png',
                  'img/tonelli/id_stations/s_Alexs.png',
                  'img/tonelli/id_stations/s_VDNX.png'

                  ]
    # name_create_img = 'img/test/token.png'
    name_create_img = names_list[-1]
    show_move = True
    pos_start = find_img.find_info()
    # показать привязку
    # fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 80
    y += 450
    # fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 250 + 120
    change_y = 27
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        # pos = fun.locCenterImg(f'{name_create_img}')
        # fun.mouse_move(pos=pos)
        print('img/test/token.png сделано')
    else:
        q = input(f"{name_create_img} сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            pos = fun.locCenterImg(f'{name_create_img}')
            fun.Mouse.move(pos=pos)
            print('сделано')
        else:
            pass
    sounds.sound_vic()
    return


def event_entry_img():
    # name_create_img = 'img/overall/event_entry/continue_gavr.png'
    # name_create_img = 'img/person/hero_id/gady/menu_acc_her_gadya.png'
    # name_create_img = 'img/person/hero_id/gavr/menu_acc_her_gavr.png'
    # name_create_img = 'img/person/hero_id/mara/menu_acc_her_mara.png'
    # name_create_img = 'img/person/change_hero/change_hero_gady.png'
    # name_create_img = 'img/person/change_hero/change_hero_mara.png'
    # name_create_img = 'img/person/change_hero/change_hero_gavr.png'
    # name_create_img = 'img/person/change_hero/add_acc.png'
    # name_create_img = 'img/overall/event_entry/continue_mara.png'
    # name_create_img = 'img/overall/event_entry/continue_gady.png'

    img_dict = {
        'img/overall/event_entry/continue_mara.png': (
            -152, 37, 304, 35, (), fun.locCenterImg(name_img='img/overall/event_entry/transmitted data.png')),
        'img/overall/event_entry/continue_gady.png': (
            -152, 37, 304, 35, (), fun.locCenterImg(name_img='img/overall/event_entry/transmitted data.png')),
        'img/overall/event_entry/continue_gavr.png': (
            -152, 37, 304, 35, (), fun.locCenterImg(name_img='img/overall/event_entry/transmitted data.png')),
        'img/person/hero_id/gady/menu_acc_her_gadya.png': (-48, 25, 90, 30, (), person.is_activate_win()),
        'img/person/hero_id/gavr/menu_acc_her_gavr.png': (-48, 25, 90, 30, (), person.is_activate_win()),
        'img/person/hero_id/mara/menu_acc_her_mara.png': (-48, 25, 90, 30, (), person.is_activate_win()),
        # 'img/person/change_hero/change_hero_gady.png': (-108, 31 + 50, 170, 30, (), person.activated_change_menu()),
        # 'img/person/change_hero/change_hero_mara.png': (-108, 31 + 50, 170, 30, (), person.activated_change_menu()),
        # 'img/person/change_hero/change_hero_gavr.png': (-108, 31 + 50, 170, 30, (), person.activated_change_menu()),
        # 'img/person/change_hero/add_acc.png': (-88 , 31 + 148, 170, 30, (), person.activated_change_menu()),

    }
    name_create_img = 'img/test/token.png'

    key = 'img/person/hero_id/gady/menu_acc_her_gadya.png'
    # key = 'img/person/change_hero/change_hero_mara.png'
    pos_start = img_dict[key][5]

    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        # показать привязку
        # fun.mouse_move(pos=(pos_start), speed=1)
        # найдем верхний угол
        x, y = pos_start
        x += img_dict[key][0]
        y += img_dict[key][1]
        # fun.mouse_move(pos=(x, y), speed=1)
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = img_dict[key][2]
        change_y = img_dict[key][3]
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        print(f'{name_create_img} сделан')
    else:
        x, y = pos_start
        x += img_dict[name_create_img][0]
        y += img_dict[name_create_img][1]
        # # найдем нижний угол
        x_demo, y_demo = x, y
        change_x = img_dict[name_create_img][2]
        change_y = img_dict[name_create_img][3]
        x_demo += change_x
        y_demo += change_y
        q = input(f"{name_create_img}  сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            print(f'{name_create_img} сделано')
        else:
            pass
    # pos = fun.locCenterImg(f'{name_create_img}')
    # fun.mouse_move(pos=pos)
    sounds.sound_vic()
    # print(f'{name_create_img} сделано')
    # check_img(name=name_create_img)
    return




# event_entry_img()
# hero_img()
# name_id_station()
cr_other_img()
# task_img()
# mob_id(name='name6_kikimora')
# mob_id(name='name3_smuggler') #
# mob_id(name='name2_spy')

# mob_id(name='name1_grey_rat')
# mob_id(name='name1_black_rat')
# mob_id(name='name1_white_rat')
# mob_id(name='name1_sand_rat')

## mob_id(name='name4_arachne')
# mob_id(name='name5_wildman')
## mob_id(name='name7_raptor')
