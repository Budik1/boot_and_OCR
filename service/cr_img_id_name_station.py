import fun
import find_img as find
import color_text as mct


def name_id_station():
    pos_info = fun.locCenterImg(name_img='img/overall/info1.png')
    fun.mouse_move(pos=pos_info, speed=1)
    x, y = pos_info
    x += 95
    y += 515
    fun.mouse_move(pos=(x, y), speed=1)
    change_x = 350
    change_y = 28
    x_demo, y_demo = x, y
    x_demo += change_x
    y_demo += change_y
    fun.mouse_move(pos=(x_demo, y_demo), speed=1)

    name_file = '../img/tonelli/id_stations/s_Pr-kt_Vernadskogo.png'

    fun.foto(name_file, (x, y, change_x, change_y))
    print()
    print(mct.tc_cyan(f'{name_file} обновлён'))
    pos = fun.locCenterImg(name_img=name_file)
    fun.mouse_move(pos=pos)


name_id_station()
# верхняя левая точка - top left point
# нижняя правая точка - lower right point