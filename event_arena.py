import pyautogui
from time import sleep
from station_master import enemy_battle
import fun
import my_color_text as myCt


def foto(path_name, _region):
    """
    Создает снимок нужного участка экрана
    :param path_name: имя файла
    :param _region: регион (X, Y, ширина, высота)
    """
    im1 = pyautogui.screenshot(region=_region)
    im1.save(path_name)


def foto_pos(name_img: str, region: tuple, tune_x=0, tune_y=0, tune_s=0, tune_v=0):
    """Получает имя файла, регион и корректирует (если надо) регион снимка"""
    x_p_oan, y_p_oan, width, height = region
    x_s = x_p_oan + tune_x
    y_s = y_p_oan + tune_y
    width_s = width - tune_s
    height_s = height - tune_v
    foto(name_img, (x_s, y_s, width_s, height_s))


def hall_is_open():
    hall = pyautogui.locateCenterOnScreen('img/arena/hall_of_glory_tabl.png', confidence=0.9)
    while not hall:
        sleep(0.1)
        hall = pyautogui.locateCenterOnScreen('img/arena/hall_of_glory_tabl.png', confidence=0.9)
    pyautogui.moveTo(hall)
    sleep(2)


def create_img_arena_object():
    """Создаёт скрин arena_object из зала славы. Объект должен быть вверху списка """
    pos_or_v = fun.find_link_hall_of_glory()  # ориентир на зал славы
    fun.move_to_click(pos_or_v, 0.3)  # открыть зал славы
    pyautogui.moveTo(pos_or_v[0] - 678, pos_or_v[1] + 144)
    hall_is_open()
    region = (pos_or_v[0] - 678, pos_or_v[1] + 142, 368, 80)
    # смещение внутри региона верхней левой точки на параметры (с увеличением смещение увеличивается)
    tune_x = 13
    tune_y = 7
    # смещение внутри региона правой нижней точки на параметр (с увеличением размер уменьшается)
    tune_s = 183
    tune_v = 20
    foto('img/arena/object.png', region)
    # foto_pos('img/test/object1.png', region, tune_x - 60, tune_y, tune_s - 60, tune_v)
    foto_pos('img/arena/arena_object.png', region, tune_x, tune_y, tune_s, tune_v)
    print('фото сделано')


def kill():
    boy_in_arena = 0
    vict_in_arena = 0
    while boy_in_arena < 101:
        pos_or_v = fun.find_link_hall_of_glory()  # ориентир на зал славы
        # print(pos_or_v)
        fun.move_to_click(pos_or_v, 0.3)  # открыть зал славы
        hall_is_open()
        # вычисление региона поиска
        x, y = pos_or_v
        x -= 665
        y += 144
        region = (x, y, 560, 80)
        const_region = region  # сохранение региона
        pyautogui.moveTo(174, 260)
        sleep(1)
        arena_object = pyautogui.locateCenterOnScreen("img/arena/arena_object.png", region=region,
                                                      confidence=0.89)
        pyautogui.moveTo(arena_object)
        scroll_up = fun.locCenterImg('img/arena/scroll_up.png', 0.9)
        if arena_object is None:
            _it = 0
            x, y, sh, v = region
            while arena_object is None and _it <= 5:  # поиск в шести регионах без смещения списка
                _it += 1
                y += 68
                # print(_it, y)
                region = (x, y, sh, v)
                arena_object = pyautogui.locateCenterOnScreen("img/arena/arena_object.png", region=region,
                                                              confidence=0.89)
        while arena_object is None:
            region = const_region
            # Если не найден раньше ищем со смещением списка в начало
            while scroll_up is not None and arena_object is None:
                fun.move_to_click(scroll_up, 0.01)
                # pyautogui.moveTo(174, 260)
                scroll_up = fun.locCenterImg('img/arena/scroll_up.png', 0.9)
                fun.await_arena(region)
                arena_object = pyautogui.locateCenterOnScreen("img/arena/arena_object.png", region=region,
                                                              confidence=0.85)
            if arena_object is None:  # Если не найден раньше ищем со смещением списка в конец
                scroll_down = fun.locCenterImg('img/arena/scroll_down.png', 0.9)
                fun.move_to_click(scroll_down, 0.01)
                fun.await_arena(region)
                arena_object = pyautogui.locateCenterOnScreen("img/arena/arena_object.png", region=region,
                                                              confidence=0.85)
        boy_in_arena += 1
        name_file = str("img/test/arena_obl_поиска" + str(boy_in_arena) + ".png")
        # print(boy_in_arena)
        # print(name_file)
        foto(name_file, region)
        attack_arena_object = pyautogui.locateCenterOnScreen('img/arena/attack.png', confidence=0.9, region=region)
        pyautogui.moveTo(attack_arena_object)
        fun.move_to_click(attack_arena_object, 0.5)
        hero_vs_opponent_img = fun.locCenterImg('img/arena/hero_vs_opponent.png', 0.9)
        while hero_vs_opponent_img is None:
            sleep(0.1)
            hero_vs_opponent_img = fun.locCenterImg('img/arena/hero_vs_opponent.png', 0.9)
        fun.move_to_click(hero_vs_opponent_img, 0.1)
        sleep(2)
        res = enemy_battle(0.5)
        if res == "победа":
            vict_in_arena += 1
            result = myCt.tc_yellow(F"победа,{vict_in_arena}")
        else:
            result = myCt.tc_red("поражение")
        print(f"боёв {boy_in_arena}, {result}, следующий..")
        ver = fun.find_link_hall_of_glory()

# create_img_arena_object()  # создание метки объекта атаки
# kill()  # цикл атаки объекта
