import pyautogui
from time import sleep
from fun import mouse_move_to_click, vizit_to_station_master

son = 0.9
par_conf = 0.8


def foto(put_imya, _region):
    im1 = pyautogui.screenshot(region=_region)
    im1.save(put_imya)


def skriny_zadaniy_u_na4stanc():
    shirina, vysota = 77, 42
    # смещение скрина внутри региона
    popravka_x_s = 4
    popravka_y_s = 1
    popravka_s_s = 21 # с увеличением поправки регион уменьшается
    popravka_v_s = 1 # 9

    def orientir():
        pul = 444
        # закрыть если открыто, т.к. за чем-то может быть не видна позиция привязки
        zakr = pyautogui.locateCenterOnScreen('img/close.png', confidence=0.9)
        if zakr is not None:
            mouse_move_to_click(zakr, 0.3)
        # получение координат привязки
        pos_orV = pyautogui.locateCenterOnScreen('img/klan.png', confidence=0.9)
        pyautogui.moveTo(pos_orV)
        sleep(0.5)
        # print(pos_orV, 'ориентир клан')
        x_or, y_or = pos_orV

        vizit_to_station_master()

        # регион поиска 1 (позиция анализа)
        x_pOan1 = x_or + 518
        x_pOan1_pul = x_or + pul  # 518
        y_pOan1 = y_or + 217
        x_pOan1, y_pOan1 = int(x_pOan1), int(y_pOan1)
        region1 = [x_pOan1, y_pOan1, shirina, vysota]
        region1_pul = [x_pOan1_pul, y_pOan1, shirina, vysota]

        # регион поиска 2 (позиция анализа)
        x_pOan2 = x_or + 518
        x_pOan2_pul = x_or + pul
        y_pOan2 = y_or + 320  # 43
        x_pOan2, y_pOan2 = int(x_pOan2), int(y_pOan2)
        region2 = [x_pOan2, y_pOan2, shirina, vysota]
        region2_pul = [x_pOan2_pul, y_pOan2, shirina, vysota]

        # регион поиска 3 (позиция анализа)
        x_pOan3 = x_or + 518
        x_pOan3_pul = x_or + pul
        y_pOan3 = y_or + 423  # 146
        x_pOan3, y_pOan3 = int(x_pOan3), int(y_pOan3)
        region3 = [x_pOan3, y_pOan3, shirina, vysota]
        region3_pul = [x_pOan3_pul, y_pOan3, shirina, vysota]

        return region1, region2, region3, region1_pul, region2_pul, region3_pul

    def pokaz_pos_pul():
        *a, region1_pul, region2_pul, region3_pul = orientir()
        # 1
        # snimok1 = 'img/test/primer_1_pul.png'
        # foto(snimok1, region1_pul)
        x_pOan1, y_pOan1, shirina, vysota = region1_pul
        print('region1_pul', x_pOan1, y_pOan1)
        x_s = x_pOan1 + popravka_x_s
        y_s = y_pOan1 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok_1 = 'img/test/1_pul.png'
        foto(snimok_1, (x_s, y_s, shirina_s, vysota_s))
        pos = (x_pOan1, y_pOan1)
        pyautogui.moveTo(pos, duration=1)

        # 2
        # snimok2 = 'img/test/primer_2_pul.png'
        # foto(snimok2, region2_pul)
        x_pOan2, y_pOan2, shirina, vysota = region2_pul
        print('region2_pul', x_pOan2, y_pOan2)
        x_s = x_pOan2 + popravka_x_s
        y_s = y_pOan2 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok2 = 'img/test/2_pul.png'
        foto(snimok2, (x_s, y_s, shirina_s, vysota_s))
        pos = (x_pOan2, y_pOan2)
        pyautogui.moveTo(pos, duration=1)

        # 3
        # snimok3 = 'img/test/primer_3_pul.png'
        # foto(snimok3, region3_pul)
        x_pOan3, y_pOan3, shirina, vysota = region3_pul
        print('region3_pul', x_pOan3, y_pOan3)
        x_s = x_pOan3 + popravka_x_s
        y_s = y_pOan3 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok3 = 'img/test/3_pul.png'
        foto(snimok3, (x_s, y_s, shirina_s, vysota_s))
        pos = (x_pOan3, y_pOan3)
        pyautogui.moveTo(pos, duration=1)

    def pokaz_pos_xp():
        region1, region2, region3, *a = orientir()
        # 1
        # snimok1 = 'img/test/primer_1_xp.png'
        # foto(snimok1, region1)
        x_pOan1, y_pOan1, shirina, vysota = region1
        print('region1 xp', x_pOan1, y_pOan1)
        x_s = x_pOan1 + popravka_x_s
        y_s = y_pOan1 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok_1 = 'img/test/1_xp.png'
        foto(snimok_1, (x_s, y_s, shirina_s, vysota_s))

        pos = (x_pOan1, y_pOan1)
        pyautogui.moveTo(pos, duration=1)

        # 2
        # snimok2 = 'img/test/primer_2_xp.png'
        # foto(snimok2, region2)
        x_pOan2, y_pOan2, shirina, vysota = region2
        print('region2 xp', x_pOan2, y_pOan2)
        x_s = x_pOan2 + popravka_x_s
        y_s = y_pOan2 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok2 = 'img/test/2_xp.png'
        foto(snimok2, (x_s, y_s, shirina_s, vysota_s))

        pos = (x_pOan2, y_pOan2)
        pyautogui.moveTo(pos, duration=1)

        # 3
        # snimok3 = 'img/test/primer_3_xp.png'
        # foto(snimok3, region3)
        x_pOan3, y_pOan3, shirina, vysota = region3
        print('region3 xp', x_pOan3, y_pOan3)
        x_s = x_pOan3 + popravka_x_s
        y_s = y_pOan3 + popravka_y_s
        shirina_s = shirina - popravka_s_s
        vysota_s = vysota - popravka_v_s
        snimok3 = 'img/test/3_xp.png'
        foto(snimok3, (x_s, y_s, shirina_s, vysota_s))
        pos = (x_pOan3, y_pOan3)
        pyautogui.moveTo(pos, duration=1)

    # snimok()
    sleep(2)
    pokaz_pos_pul()
    pokaz_pos_xp()


def skrin_viktori():
    battle_end = pyautogui.locateCenterOnScreen('img/b_battle_end.png', confidence=par_conf)
    pyautogui.moveTo(battle_end, duration=2)
    x, y = battle_end
    x = x + 165
    y = y + 40
    pyautogui.moveTo(x, y, duration=2)
    # x = x + 185
    # y = y + 55
    # pyautogui.moveTo(x, y, duration=2)
    foto("img/arena/result.png", (x, y, 185, 55))

skrin_viktori()
# skriny_zadaniy_u_na4stanc()

# 13 20 21 22 23 26 39 41 42 43 45
# 52 59 62 63 65 68 78 82 84 86 88 90 91
# 117 123 126 129 132 135 137 176 180 185 189 198
# 203 225 246 252 258 270 338 369 378
# 468 492
