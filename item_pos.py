import pyautogui
import fun
from time import sleep


def mob_foto(name):
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=0.79)
    if skip_battle:
        # raptor = fun.locCenterImg('img/tonelli/raptor.png', confidence=0.85)
        # arachne = fun.locCenterImg('img/tonelli/arachne.png', confidence=0.85)
        # krysa = fun.locCenterImg('img/tonelli/krysa.png', confidence=0.85)
        # kiki = fun.locCenterImg('img/tonelli/kikimora.png', confidence=0.85)
        # if raptor or arachne or krysa or kiki:
        #     return
        # else:
        # print(f'{skip_battle=}')
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
        fun.foto(f'img/tonelli/mobi/mobi_{name}.png', (x_f, y_f, cor_x, cor_y))
        print(f'mobi_{name} сделан')


def mob_name(name):
    skip_battle = fun.locCenterImg('img/skip_battle.png', confidence=0.79)
    if skip_battle:
        # fun.move_mause(pos=skip_battle)
        # print(f'{skip_battle=}')
        x, y = skip_battle
        x += 80
        y -= 22
        # fun.move_mause(pos=(x, y), speed=1)
        sleep(1)
        x_demo, y_demo = x, y
        change_x = 180
        change_y = 28
        x_demo += change_x
        y_demo += change_y
        # fun.move_mause(pos=(x_demo, y_demo))
        fun.foto(f'img/tonelli/mobi/name_{name}.png', (x, y, change_x, change_y))
        print(f'имя "name_{name}" сфотографировано')


def mob_id(name):
    con = 0.98
    print(f'поиск {name}')
    skip_battle = fun.locCenterImg('img/overall/skip_battle.png', confidence=con)
    while not skip_battle:
        skip_battle = fun.locCenterImg('img/overall/skip_battle.png', confidence=con)

    sleep(2)
    # 1
    # серая
    gray_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_grey_rat.png', confidence=con)
    name_gray_rat = fun.locCenterImg('img/tonelli/mobi/name1_grey_rat.png', confidence=con)
    # черная
    black_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_black_rat.png', confidence=con)
    name_black_rat = fun.locCenterImg('img/tonelli/mobi/name1_black_rat.png', confidence=con)
    # белая
    white_rat = fun.locCenterImg('img/tonelli/mobi/mobi1_white_rat.png', confidence=con)
    name_white_rat = fun.locCenterImg('img/tonelli/mobi/name1_white_rat.png', confidence=con)
    # 2 шпион
    # name_spy = fun.locCenterImg('img/tonelli/mobi/name2_spy.png', confidence=con)
    # mobi_spy = fun.locCenterImg('img/tonelli/mobi/mobi2_spy.png', confidence=con)
    # 3 контрабандист
    # name_smuggler = fun.locCenterImg('img/tonelli/mobi/name3_smuggler.png', confidence=con)
    # mobi_smuggler = fun.locCenterImg('img/tonelli/mobi/mobi3_smuggler.png', confidence=con)
    # 7 ящер
    # name_raptor = fun.locCenterImg('img/tonelli/mobi/name7_raptor.png', confidence=con)
    # mobi_raptor = fun.locCenterImg('img/tonelli/mobi/mobi7_raptor.png', confidence=con)

    if gray_rat or name_gray_rat:
        print(f'{gray_rat=}')
        print(f'{name_gray_rat=}')
        if gray_rat and name_gray_rat:
            fun.move_mause(pos=gray_rat, speed=0.5)
            fun.move_mause(pos=name_gray_rat, speed=0.5)
            print('серая крыса поймана')
            return
        else:
            if not gray_rat:
                mob_foto(name)
            if not name_gray_rat:
                mob_name(name)

    if white_rat or name_white_rat:
        print(f'{white_rat=}')
        print(f'{name_white_rat=}')
        if white_rat and name_white_rat:
            fun.move_mause(pos=white_rat, speed=0.5)
            fun.move_mause(pos=name_white_rat, speed=0.5)
            print('белая крыса поймана')
            return
        else:
            if not white_rat:
                mob_foto(name)
            if not name_white_rat:
                mob_name(name)

    if black_rat or name_black_rat:
        print(f'{black_rat=}')
        print(f'{name_black_rat=}')
        if black_rat and name_black_rat:
            fun.move_mause(pos=black_rat, speed=0.5)
            fun.move_mause(pos=name_black_rat, speed=0.5)
            print('черная крыса поймана')
            return
        if not black_rat:
            mob_foto(name)
        if not name_black_rat:
            mob_name(name)
    # if mobi_raptor or name_raptor:
    #     if mobi_raptor and name_raptor:
    #         fun.move_mause(pos=mobi_raptor, speed=0.5)
    #         fun.move_mause(pos=name_raptor, speed=0.5)
    #         print('ящер пойман')
    #         return
    #     if not mobi_raptor:
    #         mob_foto(name)
    #     if not name_raptor:
    #         mob_name(name)

    # if mobi_spy or name_spy:
    #     if mobi_spy and name_spy:
    #         fun.move_mause(pos=mobi_spy, speed=0.5)
    #         fun.move_mause(pos=name_spy, speed=0.5)
    #         print('шпион пойман')
    #         return
    #     if not mobi_spy:
    #         mob_foto(name)
    #     if not name_spy:
    #         mob_name(name)

    # if mobi_smuggler or name_smuggler:
    #     if mobi_smuggler and name_smuggler:
    #         fun.move_mause(pos=mobi_smuggler, speed=0.5)
    #         fun.move_mause(pos=name_smuggler, speed=0.5)
    #         print('контрабандист пойман')
    #         return
    #     if not mobi_smuggler:
    #         mob_foto(name)
    #     if name_smuggler:
    #         mob_name(name)
    else:
        print('моб не опознан')
        mob_name(name)
        mob_foto(name)
        print('результат "img/tonelli/mobi/"')
        return



mob_id('black_rat')   # черная
