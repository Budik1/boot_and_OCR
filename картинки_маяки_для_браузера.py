import fun
import sounds
import find_img


def fashion():
    """
        образец
        """
    name_create_img = 'img/overall/token.png'
    show_move = True
    pos_start = find_img.find_g()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 20
    y += 25 + 6
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 39
    change_y = 51
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    if name_create_img == 'img/test/token.png':
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{name_create_img}')
        fun.mouse_move(pos=pos)
    else:
        q = input(f"{name_create_img}сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            pos = fun.locCenterImg(f'{name_create_img}')
            fun.mouse_move(pos=pos)
        else:
            pass
    sounds.sound_vic()
    print('сделано')
    return


def hero_img():
    name_create_img = 'img/test/her1.png'
    # name_create_img = 'img/person/hero_id/gady/her_gadya.png'
    show_move = False
    pos_start = find_img.find_g()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 49
    y += 58 + 3
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 80 - 13
    change_y = 80 - 13
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # # собственно создание снимка
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('сделано')
    return

def link_money_token():
    """
    образец
    """
    # name_create_img = 'img/test/link_money_token.png'
    name_create_img = 'img/overall/link_money_token.png'
    show_move = False
    pos_start = find_img.find_g()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 385 + 10
    y += 60
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 31
    change_y = 31
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # собственно создание снимка
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('ok')
    return


def close_img():
    # name_create_img = 'img/test/token.png'
    #
    name_create_img = 'img/overall/close.png'
    show_move = False
    pos_start = find_img.find_g()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += 360 + 2
    y += 500 + 5 + 6
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 91
    change_y = 25
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    fun.mouse_move(pos=pos)
    sounds.sound_vic()
    print('сделано')
    return

def b1_begin():
    # name_create_img = 'img/test/token.png'

    name_create_img = 'img/overall/b1_begin.png'
    show_move = False
    pos_start = find_img.find_g()
    # показать привязку
    fun.mouse_move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 55
    y += 547
    fun.mouse_move(pos=(x, y), speed=1, show=show_move)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 29
    change_y = 37 - 4
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    # fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    # pos = fun.locCenterImg(f'{name_create_img}')
    # fun.mouse_move(pos=pos)

    if name_create_img == 'img/test/token.png':
        fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
        pos = fun.locCenterImg(f'{name_create_img}')
        fun.mouse_move(pos=pos)
    else:
        q = input(f"{name_create_img}сохранить? (y/n): ")
        if q == 'y':
            fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
            pos = fun.locCenterImg(f'{name_create_img}')
            fun.mouse_move(pos=pos)
        else:
            pass
    sounds.sound_vic()
    print('сделано')
    return

b1_begin()