import fun
import find_img as find


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


def k_Communist():
    pos_close = find.find_close()
    fun.mouse_move(pos=pos_close, speed=1)
    x, y = pos_close
    x -= 400
    y -= 210
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 174
    change_y = 34
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), speed=1)
    fun.foto(f'img/tonelli/map_item/k_Communist.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/tonelli/map_item/k_Communist.png')
    fun.mouse_move(pos=pos)

def k_Park_kr():
    pos_close = find.find_close()
    fun.mouse_move(pos=pos_close, speed=1)
    x, y = pos_close
    x -= 550
    y -= 365
    # fun.mouse_move(pos=(x, y), speed=1)
    x_demo, y_demo = x, y
    change_x = 58
    change_y = 30
    x_demo += change_x
    y_demo += change_y
    # fun.mouse_move(pos=(x_demo, y_demo), speed=1)
    # fun.foto(f'img/tonelli/map_item/k_Park_kr_.png', (x, y, change_x, change_y))
    pos = fun.locCenterImg(f'img/tonelli/map_item/k_Park_kr_.png')
    fun.mouse_move(pos=pos)


# k_Communist()
k_Park_kr()