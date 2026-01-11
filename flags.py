import fun
import baza_paths
import heroes
import event_arena


def get_nod(a, b):
    """
    Вычисление НОД для натуральных чисел a и b
    по быстрому алгоритму Евклида.
    :param a: Первое натуральное число
    :param b: Второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def create_img_arena_object():
    """Создаёт скрин arena_object из зала славы. Объект должен быть в верхней строке списка """
    qty_segment = 106
    # Определяю героя
    fun.selection_hero(show_name=False)
    # Получение пути для сохранения скрина противника
    path_img = baza_paths.arena_object
    hero_name = heroes.Activ.name_file_
    path_hero_img = f'{path_img}{hero_name}/'
    # # ориентир на зал славы
    hall = event_arena.hall_is_open()
    full_arena_region = event_arena.get_ful_region_arena_tabl(check_point=hall)
    height_line = event_arena.get_height_line(full_region_arena=full_arena_region)
    region_line1 = full_arena_region[0], full_arena_region[1], full_arena_region[2], height_line

    segment = int(full_arena_region[2] / qty_segment)
    # Создание картинки атакуемого персонажа
    # смещение внутри региона верхней левой точки на параметры (с увеличением смещение увеличивается)
    tune_x_obj = segment * 9
    tune_y_obj = segment
    # смещение внутри региона правой нижней точки на параметр (с увеличением размер уменьшается)
    tune_s_obj = segment * 43
    tune_s_ar_obj = segment * 74
    tune_v_obj = segment * 2
    fun.foto_pos(f'{path_hero_img}object1.png', region_line1,
                 tune_x=tune_x_obj, tune_y=tune_y_obj, tune_s=tune_s_obj, tune_v=tune_v_obj)
    fun.foto_pos(name_img=f'{path_hero_img}arena_object1.png', region=region_line1,
                 tune_x=tune_x_obj, tune_y=tune_y_obj, tune_s=tune_s_ar_obj, tune_v=tune_v_obj)

    print('фото сделано')

# res=get_nod(530, 5)
# print(530/5)
create_img_arena_object()