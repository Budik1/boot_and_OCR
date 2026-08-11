import find_img as find
import baza.paths_img as p_i
import tools
import fun
import pyautogui


def dress():
    """
    образец
    """
    name_create_img = p_i.park_point
    show_move = True
    pos_start = find.find_close()
    # показать привязку
    # tools.Mouse.move(pos=pos_start, speed=1)
    # найдем верхний угол
    x, y = pos_start
    x -= 500
    y -= 600
    # tools.Mouse.move(pos=(x, y), speed=1, show=show_move)
    # найдем нижний угол
    x_demo, y_demo = x, y
    change_x = 160
    change_y = 30
    x_demo += change_x
    y_demo += change_y
    # tools.Mouse.move(pos=(x_demo, y_demo), show=show_move)
    #
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'{name_create_img}')
    tools.Mouse.move(pos=pos)
    # sounds.sound_vic()
    print(f'{name_create_img} Ok')
    return


dress()
# pos_x = 460
# pos_y = 645
# sh_x = 120
# sh_y = 30
# tools.Mouse.move(pos=(pos_x, pos_y))
# tools.Mouse.move(pos=(pos_x + sh_x, pos_y + sh_y))
# "C:\python/bot_ocr1\img\default\overall\close.png"
# name_img = "C:\python/bot_ocr1\img\default\overall\close.png"
# fun.foto(path_name=name_img, region=(pos_x, pos_y, sh_x, sh_y))