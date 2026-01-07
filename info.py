import color_text
import fun
import baza_dannyx as b_d
import find_img


def info_map():
    def map_info():
        """
        Определяю имя станции нахождения
        :return: list станции
        """
        list_location = ['станция не опознана']
        for stations in range(len(b_d.list_of_stations)):
            img_station = b_d.list_of_stations[stations][1]
            pos = fun.locCenterImg(name_img=img_station, confidence=0.99, grayscale=False)
            if pos:
                list_location = b_d.list_of_stations[stations]
                print(f'{b_d.list_of_stations[stations][0]}')
            else:
                pass
        return list_location

    station = find_img.find_info()
    maps = find_img.find_station_exit()
    if station:
        location = fun.loc_now()
        if location:
            if location[0] != 'станция не опознана':
                print(color_text.tc_cyan(location[0]))
            else:
                print(color_text.tc_red('нет инфы по имени станции'))
    elif maps:
        map_info()


def info_en():
    pos_mark = find_img.find_station_master()
    list_en = ['en_1.png', 'en_2.png', 'en_3.png', 'en_4.png', 'en_5.png', 'en_7.png']
    for img_ in list_en:
        name_img = f'img/station_master/energy_value/{img_}'
        en = fun.locCenterImg(name_img, confidence=0.95)
        if en:
            fun.Mouse.move(pos=pos_mark, speed=1)
            fun.Mouse.move(pos=en, speed=1)
            print(img_)


