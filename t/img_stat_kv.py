import fun
import color_text


def img():
    kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
    print("kv_reload = ", kv_reload)
    if kv_reload:
        x, y = kv_reload
        fun.Mouse.move(pos=(x, y), speed=1)
        x -= 225
        y -= 25
        fun.Mouse.move(pos=(x, y), speed=1)
        x_sh, y_sh = x, y
        x_sh += 225
        y_sh += 270
        fun.Mouse.move(pos=(x_sh, y_sh), speed=1)
        fun.foto('../img/kv/tests/klan_raid.png', region=(x, y, 225, 270))


def img_label_raid():
    name_file = 'klan_raid_label'
    img_1 = fun.locCenterImg(name_img=f'img/kv/tests/{name_file}.png')
    if img_1:
        fun.Mouse.move(pos=img_1, speed=1)
        print(color_text.tc_cyan('Есть такой файл'))
    else:
        kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
        if kv_reload:
            x, y = kv_reload
            fun.Mouse.move(pos=(x, y), speed=1)
            x -= 100
            y -= 20
            fun.Mouse.move(pos=(x, y), speed=1)
            x_demo, y_demo = x, y
            x_sh = 80
            y_sh = 45
            x_demo += x_sh
            y_demo += y_sh
            fun.Mouse.move(pos=(x_demo, y_demo), speed=1)
            fun.foto(f'img/kv/tests/{name_file}.png', region=(x, y, x_sh, y_sh))

def img_label_kv():
    name_file = 'klan_kv_label'
    kv_reload = fun.locCenterImg('img/kv/kv_reload.png', confidence=0.9)
    if kv_reload:
        x, y = kv_reload
        fun.Mouse.move(pos=(x, y), speed=1)
        shifts_x = 221
        x -= shifts_x
        y -= 24
        fun.Mouse.move(pos=(x, y), speed=1)
        x_demo, y_demo = x, y
        x_sh = shifts_x - 22
        y_sh = 45
        x_demo += x_sh
        y_demo += y_sh
        fun.Mouse.move(pos=(x_demo, y_demo), speed=1)
        fun.foto(f'img/kv/tests/{name_file}.png', region=(x, y, x_sh, y_sh))


# img_label_raid()
# img_label_kv()
