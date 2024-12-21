import fun
import my_OCR
import baza_dannyx as b_d

# Параметр смещения от позиции 'Начстанции'
pul = 444
xp_ = 518

line1pos = 217
line2pos = 320
line3pos = 423
line_pos = [0, 217, 320, 423]

# высота и ширина
height = 42
width_smol = 77
width_big = 154

tune_x = 4  #
tune_y = 1  #
tune_s = 21  # 21 с увеличением регион уменьшается
tune_v = 1  #


def foto_pos(region, name_img):
    """ Создание файла """
    # получает регион и корректировки снимка внутри него
    # значения для уменьшения img внутри региона поиска
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def get_areas_pul_line(number_line):
    """ Получение региона pul по номеру линии"""
    x_pos, y_pos = fun.find_link_station_master()
    x_an_pul = x_pos + pul
    y_an = y_pos + line_pos[number_line]
    region_pul = [x_an_pul, y_an, width_smol, height]
    return region_pul


def get_areas_xp_line(number_line):
    """ Получение региона xp по number_line линии """
    x_or, y_or = fun.find_link_station_master()
    x_an_xp = x_or + xp_
    y_an = y_or + line_pos[number_line]
    region_xp = [x_an_xp, y_an, width_smol, height]
    return region_xp


def get_areas_task_big(number_line):
    """ Получение значения region для number_line линии """
    x_or, y_or = fun.find_link_station_master()
    x_an_pul = x_or + pul
    y_an = int(y_or + line_pos[number_line])
    region_big = [x_an_pul, y_an, width_big, height]
    return region_big


def create_img_task_pul_line(number_line):
    """ Получение pul img по номеру линии """
    region_pul = get_areas_pul_line(number_line)
    file_name = f'img/test/test_tasks/{number_line}_pul.png'
    foto_pos(region_pul, file_name)
    return file_name


def create_img_task_xp_line(number_line):
    """ Получение xp img по номеру линии """
    region_xp = get_areas_xp_line(number_line)
    file_name = f"img/test/test_tasks/{number_line}_xp.png"
    foto_pos(region_xp, file_name)
    return file_name


def create_img_task_big(number_line):
    region_big = get_areas_task_big(number_line)
    foto_pos(region_big, f"img/test/test_tasks/big_{number_line}.png")


def analiz_img(file_name):
    rezult = int(my_OCR.recognized(file_name))
    return rezult


def lvl_img():
    pos = fun.find_link_klan()
    x, y = pos
    x_f = x - 85
    y_f = y - 70
    file_name = 'img/test/test_tasks/lvl.png'
    fun.foto(file_name, (x_f, y_f, 57, 42))
    print("сделано")
    return file_name


def recognize_tasks(number_line):
    img_pul = create_img_task_pul_line(number_line)
    # print(img_pul)
    img_xp = create_img_task_xp_line(number_line)
    # print(img_xp)
    list_pul = my_OCR.recognized(img_pul)
    # if list_pul:
    #     print(list_pul)
    # else:
    #     print("Нераспознан")
    list_xp = my_OCR.recognized(img_xp)
    # if list_xp:
    #     print(list_xp)
    # else:
    #     print("Нераспознан")
    if list_pul and list_xp:
        rezult = round(int(list_pul[0]) / int(list_xp[0]))
        pul_rez = int(list_pul[0])
        xp_rez = int(list_xp[0])
        # print(rezult)
    else:
        rezult, pul_rez, xp_rez = False, False, False
        # print("Нераспознан")
    return rezult, pul_rez, xp_rez


def task_selection():
    result_search_task = None
    hero = fun.selection_hero()
    if hero == 'Gady':
        path = 'img/person/tasks_gady/'
        q_task = 7
        print('Gady')
    elif hero == 'Gavr':
        path = 'img/person/tasks_gavr/'
        q_task = 7
        print('Gavr')
    elif hero == 'Mara':
        path = 'img/person/tasks_mara/'
        q_task = 3
        print('Mara')
    else:
        print("Герой не опознан")
        return
    fun.vizit_to_station_master()
    for number_task in range(q_task):
        number_task += 1
        try:
            test_for_img = fun.locCenterImg(f"{path}t{number_task}.png")
        except:
            test_for_img = False
            print("файл(ы) не найдены")
        if test_for_img:
            # print(f"Задание опознано, t{number_task}.img")
            result_search_task = number_task
            break
        else:
            # print('задание не опознано')
            result_search_task = False
    if result_search_task:
        print(f"Задание опознано, t{result_search_task}.img")
    else:
        line1, pul_line1, xp_line1 = recognize_tasks(1)
        line2, pul_line2, xp_line2 = recognize_tasks(2)
        line3, pul_line3, xp_line3 = recognize_tasks(3)
        print(line1, line2, line3)
        if line1 == 4:
            print('Line 1')
            region = get_areas_task_big(1)
            name_img = f"{path}big_1.png"
        elif line2 == 4:
            print('Line 2')
            region = get_areas_task_big(2)
            name_img = f"{path}big_2.png"
        elif line3 == 4:
            print('Line 3')
            region = get_areas_task_big(3)
            name_img = F"{path}big_3.png"
        else:
            print("простой подбор не сработал")
        if not line1:
            if line2 < 4 and line3 < 4:
                region = get_areas_task_big(1)
                name_img = "img/test/test_tasks/big_1.png"

        foto_pos(region, name_img)
        print(f"img создан с именем {name_img}")


task_selection()
# опознание уровня
# lvl_img()
