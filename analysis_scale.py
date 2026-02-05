import fun
import find_img
import stereotypes


def cr_mark_img():
    """

    :return:
    """
    target_img = 'заглушка'
    img_dict = {
        'img/test/mark/mark_left.png': (-423, 113, 19, 5, (), find_img.find_my_game2()),
        'img/test/mark/mark_right.png': (322, 113, 19, 5, (), find_img.find_my_game2()),

    }
    # target_img = 'img/test/token.png'

    key = 'img/test/mark/mark_right.png'
    pos_start = img_dict[key][5]
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
    if target_img == 'img/test/token.png':
        fun.foto(f'{target_img}', (x, y, change_x, change_y))
        print(f'{target_img} сделан')
    else:
        answer = input(f"{key}  сохранить? (y/n): ")
        if answer == 'y':
            fun.foto(f'{key}', (x, y, change_x, change_y))
            print(f'{key} сделано')
        else:
            print("выход без создания снимка")
    return


def test_long(*, vizual=None):
    DISTANCE = 760
    pos_left_corner = fun.locCenterImg(name_img='img/test/mark/mark_left.png', confidence=0.99)
    pos_right_corner = fun.locCenterImg(name_img='img/test/mark/mark_right.png', confidence=0.99)

    if pos_left_corner and pos_right_corner:
        x_left, y_left = pos_left_corner
        x_left_cor = x_left - 7
        y_left_cor = y_left + 2

        x_right, y_right = pos_right_corner
        x_right_cor = x_right + 8
        y_right_cor = y_right + 2
        if vizual:
            ans = input('Оба угла видны. Показать? (y/n): ')
            if ans == 'y':
                ans = input('Показать левый угол? (y/n): ')
                if ans == 'y':
                    fun.Mouse.move(pos=(x_left_cor, y_left_cor), speed=1)
                ans = input('Показать правый угол? (y/n): ')
                if ans == 'y':
                    fun.Mouse.move(pos=(x_right_cor, y_right_cor), speed=1)
        if x_left_cor < x_right_cor:
            distance = x_right_cor - x_left_cor
        else:
            distance = x_left_cor - x_right_cor
        name_img = f'img/test/mark/long{distance}.png'
        fun.foto(path_name=name_img, region=(x_left_cor, y_left, distance, 5))
        percentage_change = int((distance / DISTANCE) * 100)
        print(f'Длина картинки {distance} пикселей. {int(percentage_change)}%')
    else:
        if not pos_left_corner:
            print('pos_left_corner no')
        if not pos_right_corner:
            print('pos_right_corner no')


# create_folder('img/Cr/wq/uy/hgt')
# cr_mark_img()
# test_long()
stereotypes.interest_point.cr_img()

# Длина картинки 999 пикселей. 131%
# Длина картинки 912 пикселей. 120%
# Длина картинки 833 пикселей. 109%
# Длина картинки 760 пикселей. 100%
# Длина картинки 694 пикселей. 91%
# Длина картинки 633 пикселей. 83%
# Длина картинки 578 пикселей. 76%
# Длина картинки 528 пикселей. 69%
# Длина картинки 482 пикселей. 63%
# Длина картинки 440 пикселей. 57%
# Длина картинки 401 пикселей. 52%
# Длина картинки 367 пикселей. 48%
