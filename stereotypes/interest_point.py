import fun_down
import fun


def get_left_corner():
    """
    Отправная точка всех построений.
    :return:
    """
    pos = fun_down.locateCenterImg(name_img='./img/mark_scale/mark_left.png')
    x, y, = pos
    x -= 7
    y += 2
    left_corner = x, y
    return left_corner

def get_right_corner():
    pos = fun_down.locateCenterImg(name_img='./img/mark_scale/mark_right.png')
    x, y, = pos
    x += 8
    y += 2
    right_corner = x, y
    return right_corner


def get_skale():
    NORM_DISTANCE = 760

    left_corner = get_left_corner()
    right_corner = get_right_corner()
    if left_corner and right_corner:
        x_left_cor, y_left = left_corner
        x_right_cor, y_right = right_corner
        if x_left_cor < x_right_cor:
            distance = x_right_cor - x_left_cor
        else:
            distance = x_left_cor - x_right_cor
    else:
        print("углы не определены")
        distance = None
    value_large_scale = int(distance / NORM_DISTANCE)
    return value_large_scale


def cr_img():
    target_img = "None"
    # смещение по х, смещение по у, ширина, высота
    img_dict = {
        'hero_fase': [(8 + 6, 8 + 6, 70 - 6 * 2, 70 - 6 * 2), ['gady', 'gavr', 'mara'] ]
    }
    target_img = './img/test/token.png'
    #
    key = 'hero_fase'
    pos_start = get_left_corner()
    lst_offsets = img_dict[key][0]
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += lst_offsets[0]
    y += lst_offsets[1]
    # fun.Mouse.move(pos=(x, y), speed=1)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = lst_offsets[2]
    change_y = lst_offsets[3]
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    if target_img == './img/test/token.png':
        fun.foto(f'{target_img}', (x, y, change_x, change_y))
        print(f'{target_img} сделан')
    else:
        answer = input(f"{key} Как сохранить? Варианты 1: ")
        if answer == 'y':
            fun.foto(f'{key}', (x, y, change_x, change_y))
            print(f'{key} сделано')
        else:
            print("выход без создания снимка")
    # sounds.sound_vic(block=False)
