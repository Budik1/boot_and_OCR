from fun import locCenterImg, mouse_move
import find_img as find

cof = 0.98


def tests_img():
    pos = find.find_station_master()
    mouse_move(pos=pos, speed=1)
    e1 = locCenterImg('img/stationmaster/energy_indicator/en1.png', confidence=0.98)
    e2 = locCenterImg('img/stationmaster/energy_indicator/en2.png', confidence=0.98)
    e3 = locCenterImg('img/stationmaster/energy_indicator/en3.png', confidence=0.98)
    e7 = locCenterImg('img/stationmaster/energy_indicator/en7.png', confidence=cof)
    if e1:
        mouse_move(pos=e1, speed=1)
        print("1")
    if e2:
        mouse_move(pos=e2, speed=1)
        print("2")
    if e3:
        mouse_move(pos=e3, speed=1)
        print("3")
    if e7:
        mouse_move(pos=e7, speed=1)
        print("7")
    if (not e1) and (not e2) and (not e3) and (not e7):
        print('ничего не найдено')
    else:
        print('все что найдено - показано и написано')


tests_img()
