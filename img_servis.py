import os
import fun
import find_img
import heroes
from PIL import Image


def tests_img_value_energy():
    master = find_img.find_station_master()
    fun.Mouse.move(pos=master)
    list_value_energy = ['en_1', 'en_2', 'en_3', 'en_4', 'en_5', 'en_7', ]  # 'en_6',
    for value_energy in list_value_energy:
        name_file = f'img/station_master/energy_value/{value_energy}.png'
        pos_img = fun.locCenterImg(name_img=name_file, confidence=0.93)
        if pos_img:
            print(value_energy)
            fun.Mouse.move(pos=pos_img, speed=1)

def cr_box_loot_img(*, name_create_img):
    img_dict = {'img/tonelli/loot_gift_box/big/720.png': (-54, -140, 119, 119, (),), }
    key = 'img/tonelli/loot_gift_box/big/720.png'
    # от чего оттолкнуться
    pos_start =  find_img.find_close()
    # # найдем верхний угол
    x, y = pos_start
    x += img_dict[key][0]
    y += img_dict[key][1]
    # # найдем нижний угол
    change_x = img_dict[key][2]
    change_y = img_dict[key][3]
    fun.foto(f'{name_create_img}', (x, y, change_x, change_y))
    return

def tenderloin(*, name_fold, name_crop_img):
    # hero_dir = heroes.Hero.get_name_id(heroes.Activ.hero_activ)
    down_obl = [50, 50, 59, 59, f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}_up.png']
    up_obl = [25, 5, 88, 30, f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}_down.png']
    name_open = f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}.png'
    img = Image.open(name_open)
    #  box=(left, upper, right, lower)
    for i in [down_obl, up_obl]:
        left = i[0]
        upper = i[1]
        right = i[2] + left
        lower = i[3] + upper
        img_crop = img.crop((left, upper, right, lower))
        img_crop.save(i[4])
    name_remove_img = f'img/tonelli/loot_gift_box/big/{name_fold}/{name_crop_img}'
    os.remove(name_open)
    return

