import fun
import find_img


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

# tests_img_value_energy1()
