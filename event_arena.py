from time import sleep

import fun
import find_img
import heroes
import solid_memory
import station_master

from baza import baza_paths as b_p
from tools import color_text as c_t


def get_ful_region_arena_tabl():
    """
    Возвращает регион полной таблицы
    :return:
    """
    # маяки
    point_hall = hall_is_open()
    pos_close = find_img.find_close()
    # вычисление региона поиска
    # вычисление сторон между маяками
    width_arena, height_arena = fun.distance(pos_upper=point_hall, pos_lower=pos_close)
    x, y = point_hall
    region_x = x - int(width_arena / 8.4)  #
    region_y = y + int(height_arena / 5.8)  #
    region_width = width_arena + int(width_arena / 5.6)  # с увеличением числа уменьшается (5.6 - 530)
    region_height = height_arena - int(height_arena / 3.284)  # с увеличением числа увеличивается (3.284 - 360)
    full_region = (region_x, region_y, region_width, region_height)
    return full_region


def get_height_line(*, full_region_arena):
    """
    Получить высоту строки таблицы арены
    :param full_region_arena:
    :return:
    """
    qty_lines = 6
    x, y, width_full, height_full = full_region_arena
    #  высота строки таблицы
    height_line = int(height_full / qty_lines)
    return height_line


def hall_is_open():
    """
    Ожидает отрисовки таблицы арены
    :return: позиция таблички арены
    """
    hall = find_img.find_hall_of_glory_tabl()
    while not hall:
        sleep(0.1)
        hall = find_img.find_hall_of_glory_tabl()
    return hall


def create_img_arena_object():
    """Создаёт скрин arena_object из зала славы. Объект должен быть в верхней строке списка """
    qty_segment = 106  # 265
    # Определяю героя
    fun.selection_hero(show_name=False)
    # Получение пути для сохранения скрина противника
    path_img = b_p.arena_object
    hero_name = heroes.Activ.name_file_
    path_hero_img = f'{path_img}{hero_name}/'
    # # ориентир на зал славы
    full_arena_region = get_ful_region_arena_tabl()
    height_line = get_height_line(full_region_arena=full_arena_region)
    region_line1 = full_arena_region[0], full_arena_region[1], full_arena_region[2], height_line

    segment = int(full_arena_region[2] / qty_segment)
    # Создание картинки атакуемого персонажа
    # смещение внутри региона верхней левой точки на параметры (с увеличением смещение увеличивается)
    tune_x_obj = segment * 9  # 5*9=45 2*22=44
    tune_y_obj = segment  # 5 2*2=4
    # смещение внутри региона правой нижней точки на параметр (с увеличением размер уменьшается)
    tune_s_obj = segment * 43
    tune_s_ar_obj = segment * 74
    tune_v_obj = segment * 2
    fun.foto_pos(f'{path_hero_img}object.png', region_line1,
                 tune_x=tune_x_obj, tune_y=tune_y_obj, tune_s=tune_s_obj, tune_v=tune_v_obj)
    fun.foto_pos(name_img=f'{path_hero_img}arena_object.png', region=region_line1,
                 tune_x=tune_x_obj, tune_y=tune_y_obj, tune_s=tune_s_ar_obj, tune_v=tune_v_obj)

    print('фото сделано')


def kill():
    # Определяю героя
    fun.selection_hero(show_name=False)
    # Получаю количество боёв на арене сегодня
    boy_in_arena = heroes.Hero.get_arena_count(heroes.Activ.hero_activ)
    # Получаю количество побед в боях на арене сегодня
    vict_in_arena = heroes.Hero.get_arena_victory_count(heroes.Activ.hero_activ)

    print(f"боёв {heroes.Hero.get_arena_count(heroes.Activ.hero_activ)}, побед {vict_in_arena}, следующий..")
    while boy_in_arena < 101:
        # Проверка на смену героя
        fun.selection_hero(show_name=True)
        # ориентир на зал славы
        pos_or_v = fun.find_link_hall_of_glory()
        fun.Mouse.move_to_click(pos_click=pos_or_v, z_p_k=0.3, message_l='открыть зал славы')  # открыть зал славы
        # Ожидание открытия зала славы
        # hall = hall_is_open()
        # fun.Mouse.move(pos=hall, message_l='зал славы открыт')
        ful_region = get_ful_region_arena_tabl()
        height_line = get_height_line(full_region_arena=ful_region)
        region_line1 = ful_region[0], ful_region[1], ful_region[2], height_line
        fun.foto_pos(name_img=b_p.img_token, region=region_line1)

        arena_object = find_img.find_arena_object(region=region_line1,
                                                  hero=heroes.Hero.get_name_id(heroes.Activ.hero_activ))
        arena_object_region = region_line1
        fun.Mouse.move(pos=arena_object)

        # Построчный поиск без смещения
        if arena_object is None:
            _it = 0
            x, y, sh, v = region_line1
            while arena_object is None and _it <= 5:  # поиск в шести регионах без смещения списка
                _it += 1
                y += height_line
                region_next = (x, y, sh, v)
                arena_object = find_img.find_arena_object(region=region_next,
                                                          hero=heroes.Hero.get_name_id(heroes.Activ.hero_activ))
                arena_object_region = region_next
        scroll_up = find_img.find_scroll_up()
        # scroll_down = find_img.find_scroll_down()
        if scroll_up:
            search_vector = 'up'
        else:
            search_vector = "down"
        while arena_object is None:
            scroll_up = find_img.find_scroll_up()
            # if scroll_up:
            #     search_vector = 'up'
            # else:
            #     search_vector = "down"
            scroll_down = find_img.find_scroll_down()
            region = region_line1
            # Если не найден раньше ищем со смещением списка в начало
            # while scroll_up and arena_object is None:
            if not arena_object and search_vector == 'up':
                fun.Mouse.move_to_click(pos_click=scroll_up,
                                        log=False, message_l="прокрутка вверх")
                # batt_attack = fun.await_arena(region)
                fun.Mouse.move(pos=(scroll_up[0] - 70, scroll_up[1]),
                               log=False, message_l='отвести в сторону от стрелки?')
                find_img.find_hall_of_glory_tabl()
                arena_object = find_img.find_arena_object(region=region,
                                                          hero=heroes.Hero.get_name_id(heroes.Activ.hero_activ))
                scroll_up = find_img.find_scroll_up()
                if not scroll_up:
                    search_vector = "down"
            if not arena_object and search_vector == 'down':  # Если не найден раньше ищем со смещением списка в конец
                fun.Mouse.move_to_click(pos_click=scroll_down,
                                        log=False, message_l="прокрутка вниз")
                fun.Mouse.move(pos=(scroll_down[0] - 70, scroll_down[1]),
                               log=False, message_l='отвести в сторону от стрелки вниз?')
                fun.await_arena(region)
                arena_object = find_img.find_arena_object(region=region,
                                                          hero=heroes.Hero.get_name_id(heroes.Activ.hero_activ))
                scroll_down = find_img.find_scroll_down()
                if not scroll_down:
                    search_vector = 'up'
            arena_object_region = region
        choice_of_the_attacked = find_img.find_choice_of_the_attacked(region=arena_object_region)
        fun.Mouse.move(pos=choice_of_the_attacked)
        fun.Mouse.move_to_click(pos_click=choice_of_the_attacked, z_p_k=0.5)
        hero_vs_opponent_img = find_img.find_attack_arena_opponent()
        while hero_vs_opponent_img is None:
            # sleep(0.1)
            hero_vs_opponent_img = find_img.find_attack_arena_opponent()
        fun.Mouse.move_to_click(pos_click=hero_vs_opponent_img, z_p_k=0.1)

        heroes.Hero.app_arena_count(heroes.Activ.hero_activ)
        solid_memory.save_all_state_config_json(info=False)
        # sleep(2)
        # print('переход в enemy_battle')
        res = station_master.enemy_battle(0.4, arena=True, add_up=False, dog_activ=False)
        # print('выход из enemy_battle')
        if res == "победа":
            vict_in_arena += 1
            heroes.Hero.app_arena_victory_count(heroes.Activ.hero_activ)
            result_text = c_t.tc_yellow(F"победа,{vict_in_arena}")
            solid_memory.save_all_state_config_json(info=False)
        else:
            result_text = c_t.tc_red("поражение")
        boy_in_arena = heroes.Hero.get_arena_count(heroes.Activ.hero_activ)
        print(f"боёв {heroes.Hero.get_arena_count(heroes.Activ.hero_activ)}, {result_text}, следующий..")
        fun.find_link_hall_of_glory()
