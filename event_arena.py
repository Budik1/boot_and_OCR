import pyautogui
from time import sleep

import fun
import find_img as find
import station_master
import my_color_text as myCt


def foto_pos(name_img: str, region: tuple, tune_x=0, tune_y=0, tune_s=0, tune_v=0):
    """Получает имя файла, регион и корректирует (если надо) регион снимка"""
    x_p_oan, y_p_oan, width, height = region
    x_s = x_p_oan + tune_x
    y_s = y_p_oan + tune_y
    width_s = width - tune_s
    height_s = height - tune_v
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def hall_is_open():
    hall = find.find_hall_of_glory_tabl()
    while not hall:
        sleep(0.1)
        hall = find.find_hall_of_glory_tabl()

    fun.mouse_move(pos=hall)
    sleep(2)


def create_img_arena_object():
    """Создаёт скрин arena_object из зала славы. Объект должен быть вверху списка """
    pos_or_v = fun.find_link_hall_of_glory()  # ориентир на зал славы
    fun.mouse_move_to_click(pos_click=pos_or_v, z_p_k=0.3)  # открыть зал славы
    fun.mouse_move(pos=(pos_or_v[0] - 678, pos_or_v[1] + 144))
    hall_is_open()
    region = (pos_or_v[0] - 678, pos_or_v[1] + 142, 368, 80)
    # смещение внутри региона верхней левой точки на параметры (с увеличением смещение увеличивается)
    tune_x = 13
    tune_y = 7
    # смещение внутри региона правой нижней точки на параметр (с увеличением размер уменьшается)
    tune_s = 183
    tune_v = 20
    fun.foto('img/arena/object.png', region)
    # foto_pos('img/test/object1.png', region, tune_x - 60, tune_y, tune_s - 60, tune_v)
    foto_pos('img/arena/arena_object.png', region, tune_x, tune_y, tune_s, tune_v)
    print('фото сделано')


def kill():
    boy_in_arena = 0
    vict_in_arena = 0
    while boy_in_arena < 101:
        pos_or_v = fun.find_link_hall_of_glory()  # ориентир на зал славы
        # print(pos_or_v)
        fun.mouse_move_to_click(pos_click=pos_or_v, z_p_k=0.3)  # открыть зал славы
        hall_is_open()
        # вычисление региона поиска
        x, y = pos_or_v
        x -= 665
        y += 144
        region = (x, y, 560, 80)
        const_region = region  # сохранение региона
        fun.mouse_move(pos=(174, 260))
        sleep(1)
        arena_object = find.find_arena_object(region=region)
        fun.mouse_move(pos=arena_object)
        scroll_up = find.find_scroll_up()
        if arena_object is None:
            _it = 0
            x, y, sh, v = region
            while arena_object is None and _it <= 5:  # поиск в шести регионах без смещения списка
                _it += 1
                y += 68
                # print(_it, y)
                region = (x, y, sh, v)
                arena_object = find.find_arena_object(region=region)
        while arena_object is None:
            region = const_region
            # Если не найден раньше ищем со смещением списка в начало
            while scroll_up is not None and arena_object is None:
                fun.mouse_move_to_click(pos_click=scroll_up)
                # pyautogui.moveTo(174, 260)
                scroll_up = find.find_scroll_up()
                fun.await_arena(region)
                arena_object = find.find_arena_object(region=region)  # 0.85
            if arena_object is None:  # Если не найден раньше ищем со смещением списка в конец
                scroll_down = find.find_scroll_down()
                fun.mouse_move_to_click(pos_click=scroll_down)
                fun.await_arena(region)
                arena_object = find.find_arena_object(region=region)  # 0.85
        boy_in_arena += 1
        name_file = str("img/test/arena_obl_поиска" + str(boy_in_arena) + ".png")
        # print(boy_in_arena)
        # print(name_file)
        fun.foto(name_file, region)
        attack_arena_object = find.find_attack(region=region)
        fun.mouse_move(pos=attack_arena_object)
        fun.mouse_move_to_click(pos_click=attack_arena_object, z_p_k=0.5)
        hero_vs_opponent_img = find.find_hero_vs_opponent()
        while hero_vs_opponent_img is None:
            sleep(0.1)
            hero_vs_opponent_img = find.find_hero_vs_opponent()
        fun.mouse_move_to_click(pos_click=hero_vs_opponent_img, z_p_k=0.1)
        sleep(2)
        # print('переход в enemy_battle')
        res = station_master.enemy_battle(0.5, arena=True, add_up=False, dog_activ=False)
        # print('выход из enemy_battle')
        if res == "победа":
            vict_in_arena += 1
            result = myCt.tc_yellow(F"победа,{vict_in_arena}")
        else:
            result = myCt.tc_red("поражение")
        print(f"боёв {boy_in_arena}, {result}, следующий..")
        fun.find_link_hall_of_glory()

# create_img_arena_object()  # создание метки объекта атаки
# kill()  # цикл атаки объекта
