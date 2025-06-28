import pyautogui
import fun
import find_img as find
from time import sleep


def cri_event_img(*, x_reg, y_reg, name):
    pos = fun.locCenterImg(name)
    if pos:
        x, y = pos
        x -= x_reg / 2
        y -= y_reg / 2
        fun.foto(name, (x, y, x_reg, y_reg))


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot_task():
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    region1_big, region2_big, region3_big = fun.get_areas_task_big()

    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/big_3.png")

    region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = fun.get_areas_task_small()
    # foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/1_pul.png')
    # foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/2_pul.png')
    # foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/3_pul.png')
    # foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/1_xp.png")
    # foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/2_xp.png')
    # foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/3_xp.png')


def hero_img():
    pos = fun.find_link_klan()
    x, y = pos
    x -= 179
    y -= 65
    x_v = x
    y_v = y
    fun.foto('img/test/her1.png', (x_v, y_v, 84, 84))
    print("сделано")


def victory_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 390
        y -= 264
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        # region = x, y
        # pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/victory_battle_in_kv.png', region=(x, y, 140, 65))


def defeat_battle_in_kv():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 390
        y -= 264
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/kv/defeat_battle_in_kv.png', region=(x, y, 140, 65))


def detecting():
    victory = fun.locCenterImg('img/kv/victory_battle_in_kv.png', confidence=0.95)
    defeat = fun.locCenterImg('img/kv/defeat_battle_in_kv.png', confidence=0.95)
    if victory:
        result = "победа"
        print(result)

    elif defeat:
        result = "поражение"
        print(result)


def victory_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 55
        y -= 405
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 140
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/victory_in_arena.png', region=(x, y, 140, 65))
    print('отработал')


def defeat_in_arena():
    kv_close = fun.locCenterImg('img/kv/kv_close.png', confidence=0.9)
    if kv_close:
        print(kv_close, 'kv_close')
        x, y = kv_close
        x -= 110
        y -= 295
        pos_foto = x, y
        pyautogui.moveTo(pos_foto, duration=1)
        # x += 180
        # y += 65
        region = x, y
        pyautogui.moveTo(region, duration=1)
        fun.foto('img/arena/defeat_in_arena.png', region=(x, y, 180, 65))
    print('отработал')


def gift_img():
    pos = fun.find_link_klan()
    x, y = pos
    x += 118  # 148
    y += 350  # 300
    pyautogui.moveTo(x, y)
    x_v = x
    y_v = y
    x_v += 28
    pyautogui.moveTo(x_v, y)
    y_v += 40
    # pyautogui.moveTo(x_v, y_v)
    fun.foto('img/test/gift2.png', (x, y, 28, 25))
    print("сделано")


def lvl_img():
    pos = fun.find_link_klan()
    x, y = pos
    x_f = x - 85
    y_f = y - 70
    # pyautogui.moveTo((x_f, y_f), duration=1)
    # x_r = x_f + 55
    # y_r = y_f + 40
    # pyautogui.moveTo((x_r, y_r), duration=1)
    fun.foto('img/test/lvl.png', (x_f, y_f, 55, 40))
    print("сделано")


def work():
    pos = fun.vizit_to_station_master()
    x, y = pos
    x += 450
    y -= 5
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 90
    change_y = 30
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/work.png', (x, y, change_x, change_y))
    pos_work = fun.locCenterImg(f'img/overall/work.png')
    fun.mouse_move(pos=pos_work)


def work_8_hour():
    fun.vizit_to_station_master()
    pos_work = fun.locCenterImg('img/overall/work.png')
    fun.mouse_move(pos=pos_work)
    x, y = pos_work
    x -= 224
    y += 430
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 200
    change_y = 50
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/work_8_hour.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/overall/work_8_hour.png')
    fun.mouse_move(pos=pos)


def station_exit():
    pos_close = find.find_close()
    fun.mouse_move(pos=pos_close, speed=1)
    x, y = pos_close
    x -= 600 - 6
    y -= 640 - 4
    fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 290 - 6 - 2
    change_y = 50 - 4
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/tonelli/station_exit.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/tonelli/station_exit.png')
    fun.mouse_move(pos=pos)


def button_expand():
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    # fun.mouse_move(pos=pos_my)
    x, y = pos_my
    x += 280
    y -= 55
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 25
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/button_expand.png', (x, y, change_x, change_y))
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.mouse_move(pos=img_button_expand, speed=1)


def img_change_hero():
    # развернуть на весь экран
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.mouse_move_to_click(pos_click=img_button_expand)
    #
    sleep(0.2)
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_my
    x += 500 - 10
    y -= 20
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 32
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    # fun.foto(f'img/person/change_hero_gavr.png', (x, y, change_x, change_y))
    change_hero = pyautogui.screenshot(region=(x, y, change_x, change_y))
    pos_menu_chenge_acc = fun.locCenterImg(change_hero)
    open_menu_chenge_acc = fun.locCenterImg('img/person/add_acc.png')
    if not open_menu_chenge_acc:
        fun.mouse_move_to_click(pos_click=pos_menu_chenge_acc)
    img(pos_menu_chenge_acc)


def img(pos_clic):
    x, y = pos_clic
    x -= 125
    y += 97
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 180
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    # создание
    fun.foto('img/person/change_hero/change_hero_mara.png', (x, y, change_x, change_y))
    # проверка
    sleep(1)
    her_gady = fun.locCenterImg('img/person/change_hero_gady.png')
    her_gavr = fun.locCenterImg('img/person/change_hero_gavr.png')
    her_mara = fun.locCenterImg('img/person/change_hero_mara.png')
    her_veles = fun.locCenterImg('img/person/change_hero_veles.png')
    if her_veles:
        print('her Veles')
        fun.mouse_move(pos=her_veles, speed=1)
        sleep(2)
    if her_gady:
        print('her Gady')
        fun.mouse_move(pos=her_gady, speed=1)
        sleep(2)
    if her_gavr:
        print('her Gavr')
        fun.mouse_move(pos=her_gavr, speed=1)
        sleep(2)
    if her_mara:
        print('her Mara')
        fun.mouse_move(pos=her_mara, speed=1)
        sleep(2)


def img2(pos_clic):
    # добавить аккаунт
    # pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)
    x, y = pos_clic
    x -= 95
    y += 97 + 130 + 35
    fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 180
    change_y = 32
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/person/change_hero/add_acc.png', (x, y, change_x, change_y))


def button_collapse():
    #
    # развернуть на весь экран
    img_button_expand = fun.locCenterImg('img/overall/button_expand.png')
    fun.mouse_move_to_click(pos_click=img_button_expand)
    #
    pos_my = fun.locCenterImg('img/overall/my_game2.png', 0.8)

    x, y = pos_my
    x += 700 - 17
    y -= 57
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 25
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo))
    fun.foto(f'img/overall/button_collapse.png', (x, y, change_x, change_y))
    img_button_collapse = fun.locCenterImg('img/overall/button_collapse.png')
    fun.mouse_move(pos=img_button_collapse, speed=1)


def mob_foto(name):
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=0.79)
    if skip_battle:
        x, y = skip_battle
        x_f = x + 300 + 14
        y_f = y - 35 + 13
        # pyautogui.moveTo((x_f, y_f), duration=1)
        sleep(1)
        cor_x = 130 - 16
        cor_y = 130 - 16
        x_cor = x_f + cor_x
        y_cor = y_f + cor_y
        # pyautogui.moveTo(x_cor, y_cor, duration=1)
        # fun.foto(f'img/tonelli/mobi/mobi_{name}.png', (x_f, y_f, cor_x, cor_y))
        # print(f'foto mobi_{name} сделан')


def mob_name(name):
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=0.79)
    if skip_battle:
        # fun.mouse_move(pos=skip_battle)
        # print(f'{skip_battle=}')
        x, y = skip_battle
        x += 80
        y -= 22
        # fun.mouse_move(pos=(x, y), speed=1)
        sleep(1)
        x_demo, y_demo = x, y
        change_x = 180
        change_y = 28
        x_demo += change_x
        y_demo += change_y
        # fun.mouse_move(pos=(x_demo, y_demo))
        fun.foto(f'img/tonelli/mobi/name_{name}.png', (x, y, change_x, change_y))
        print(f'имя "name_{name}" сфотографировано')


def mob_id(name):
    con = 0.99
    print(f'поиск {name}')
    skip_battle = fun.locCenterImg('img/overall/skip_battle.png', confidence=con)
    while not skip_battle:
        skip_battle = fun.locCenterImg('img/overall/skip_battle.png', confidence=con)

    sleep(2)
    # 1
    # серая *
    gray_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_grey_rat.png', confidence=con)
    name_gray_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=con)
    # черная *
    black_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_black_rat.png', confidence=con)
    name_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=con)
    # белая *
    white_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_white_rat.png', confidence=con)
    name_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=con)

    # 5 дикарь *
    name_wildman = fun.locCenterImg('img/tonelli/mobi/name5_wildman.png', confidence=con)
    mobi_wildman = fun.locCenterImg('img/tonelli/mobi/mobi5_wildman.png', confidence=con)
    # 7 ящер *
    name_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=con)
    mobi_raptor = fun.locCenterImg('img/tonelli/mobi/mobi7_raptor.png', confidence=con)
    # 1 серая
    if gray_rat or name_gray_rat:
        print(f'{gray_rat=}')
        print(f'{name_gray_rat=}')
        if gray_rat and name_gray_rat:
            fun.mouse_move(pos=gray_rat, speed=0.5)
            fun.mouse_move(pos=name_gray_rat, speed=0.5)
            print('серая крыса поймана')
            return
        else:
            if not gray_rat:
                mob_foto(name)
            if not name_gray_rat:
                mob_name(name)
    # 1 белая
    if white_rat or name_white_rat:
        print(f'{white_rat=}')
        print(f'{name_white_rat=}')
        if white_rat and name_white_rat:
            fun.mouse_move(pos=white_rat, speed=0.5)
            fun.mouse_move(pos=name_white_rat, speed=0.5)
            print('белая крыса поймана')
            return
        else:
            if not white_rat:
                mob_foto(name)
            if not name_white_rat:
                mob_name(name)
    # 1 черная
    if black_rat or name_black_rat:
        print(f'{black_rat=}')
        print(f'{name_black_rat=}')
        if black_rat and name_black_rat:
            fun.mouse_move(pos=black_rat, speed=0.5)
            fun.mouse_move(pos=name_black_rat, speed=0.5)
            print('черная крыса поймана')
            return
        if not black_rat:
            mob_foto(name)
        if not name_black_rat:
            mob_name(name)

    if mobi_wildman or name_wildman:
        if mobi_wildman and name_wildman:
            fun.mouse_move(pos=mobi_wildman, speed=0.5)
            fun.mouse_move(pos=name_wildman, speed=0.5)
            print('ящер пойман')
            return
        if not mobi_wildman:
            mob_foto(name)
        if not name_wildman:
            mob_name(name)
    # 7 ящер
    if mobi_raptor or name_raptor:
        if mobi_raptor and name_raptor:
            fun.mouse_move(pos=mobi_raptor, speed=0.5)
            fun.mouse_move(pos=name_raptor, speed=0.5)
            print('ящер пойман')
            return
        if not mobi_raptor:
            mob_foto(name)
        if not name_raptor:
            mob_name(name)
    # создание картинки
    else:
        print('моб не опознан')
        mob_name(name)
        mob_foto(name)
        print('результат "img/tonelli/mobi/"')
        return


def aktiv_win_game():
    pos = fun.locCenterImg('img/overall/avtoriz/aktiv_win_game.png')
    if pos:
        # 34x98
        x, y = pos
        x -= 34 / 2
        y -= 98 / 2
        fun.foto('img/overall/avtoriz/aktiv_win_game.png', (x, y, 34, 98))


def continue_hero():
    pos = fun.locCenterImg('img/overall/event_entry/continue_gavr.png')
    if pos:
        print('ok')
        # 34x98
        x, y = pos
        x -= 270 / 2
        y -= 60 / 2
        fun.foto('img/overall/event_entry/continue_gavr.png', (x, y, 270, 60))
    return


def info_img():
    pos = tuple(fun.locCenterImg(name_img='img/overall/info.png', confidence=0.8))
    print(type(pos))
    if pos:
        print('ok')
        # 33x41
        x, y = pos
        pos_change = 33, 41
        x -= (pos_change[0] / 2) - 2
        y -= (pos_change[1] / 2) - 2
        fun.foto('img/overall/info1.png', (x, y, pos_change[0], pos_change[1]))
    new_pos = fun.locCenterImg(name_img='img/overall/info1.png')
    fun.mouse_move(pos=new_pos)
    return


# info_img()
# station_exit()
continue_hero()
# aktiv_win_game()
# # 1
# mob_id('white_rat')   # белая
# mob_id('black_rat')   # черная
# mob_id('sand_rat')    # песчаная
# mob_id('grey_rat')    # серая
# # 2
# mob_id('spy')           # шпион
# # 3
# mob_id('smuggler')    # контрабандист
# # 4
# mob_id('arachne') # пауки
# # 5
# mob_id('wildman')     # дикарь
# # 6
# mob_id('kikimora')
# # 7
# mob_id('raptor')

# mob_name()
# mob_foto('a')
# button_collapse()
# img_change_hero()
# button_expand()
# work()
# work_8_hour()
# gift_img()
# defeat_in_arena()
# victory_in_arena()
# detecting()
# defeat_battle_in_kv()
# victory_battle_in_kv()
# hero_img()
