import fun_down
import fun


def find_mark_left():
    pos = fun_down.locateCenterImg(name_img='./img/test/mark/mark_left.png')
    x, y, = pos
    x -= 7
    y += 2
    pos = x, y
    return pos

def get_skale():
    DISTANCE = 760
    def get_left_corner():
        pos = fun_down.locateCenterImg(name_img='./img/test/mark/mark_left.png')
        x, y, = pos
        x -= 7
        y += 2
        left_corner = x, y
        return left_corner

    def get_right_corner():
        pos = fun_down.locateCenterImg(name_img='./img/test/mark/mark_right.png')
        x, y, = pos
        x += 8
        y += 2
        right_corner = x, y
        return right_corner


def cr_img():
    target_img = "None"
    # смещение по х, смещение по у, ширина, высота
    img_dict = {
        'hero_fase': (8 + 6, 8 + 6, 70 - 6 * 2, 70 - 6 * 2)
    }
    target_img = './img/test/token.png'
    #
    key = 'hero_fase'
    pos_start = find_mark_left()
    # показать привязку
    # fun.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x += img_dict[key][0]
    y += img_dict[key][1]
    # fun.Mouse.move(pos=(x, y), speed=1)
    # # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = img_dict[key][2]
    change_y = img_dict[key][3]
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), show=show_move)
    # # собственно создание снимка
    if target_img == './img/test/token.png':
        fun.foto(f'{target_img}', (x, y, change_x, change_y))
        print(f'{target_img} сделан')
    else:
        answer = input(f"{key}  сохранить? (y/n): ")
        if answer == 'y':
            fun.foto(f'{key}', (x, y, change_x, change_y))
            print(f'{key} сделано')
        else:
            print("выход без создания снимка")
    # sounds.sound_vic(block=False)

