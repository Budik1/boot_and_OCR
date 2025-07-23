"""Файл показывает как перевести картинку в текст
 и создаёт картинку уровня"""
import fun


def foto_pos(region, tune_x, tune_y, tune_s, tune_v, name_img):
    # получает регион и корректировки снимка внутри него
    x_p_an, y_p_an, width_, height_ = region
    x_s = x_p_an + tune_x  # внесение изменений в параметр координаты "х"
    y_s = y_p_an + tune_y  # внесение изменений в параметр координаты "y"
    width_s = width_ - tune_s  # внесение изменений в параметр ширина "width"
    height_s = height_ - tune_v  # внесение изменений в параметр длинна "height"
    # print(region, (x_s, y_s, width_s, height_s))
    fun.foto(name_img, (x_s, y_s, width_s, height_s))


def get_screenshot_task():
    # создание скринов заданий
    # смещение скриншота внутри региона
    tune_x = 4  #
    tune_y = 1  #
    tune_s = 21  # 21 с увеличением регион уменьшается
    tune_v = 1  #
    # скрины маленькие
    # region1_pul, region2_pul, region3_pul, region1_xp, region2_xp, region3_xp = fun.get_areas_task_small()
    # foto_pos(region1_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/test_tasks/1_pul.png')
    # foto_pos(region2_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/test_tasks/2_pul.png')
    # foto_pos(region3_pul, tune_x, tune_y, tune_s, tune_v, 'img/test/test_tasks/3_pul.png')
    # foto_pos(region1_xp, tune_x, tune_y, tune_s, tune_v, "img/test/test_tasks/1_xp.png")
    # foto_pos(region2_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/test_tasks/2_xp.png')
    # foto_pos(region3_xp, tune_x, tune_y, tune_s, tune_v, 'img/test/test_tasks/3_xp.png')
    # скрины большие
    region1_big, region2_big, region3_big = fun.get_areas_task_big()
    foto_pos(region1_big, tune_x, tune_y, tune_s, tune_v, "img/test/test_tasks/big_1.png")
    foto_pos(region2_big, tune_x, tune_y, tune_s, tune_v, "img/test/test_tasks/big_2.png")
    foto_pos(region3_big, tune_x, tune_y, tune_s, tune_v, "img/test/test_tasks/big_3.png")


# get_screenshot_task()
#
# list_1_pul = my_OCR.recognized('img/test/test_tasks/1_pul.png')
# list_1_xp = my_OCR.recognized("img/test/test_tasks/1_xp.png")
# sleep(2)
# list_2_pul = my_OCR.recognized('img/test/test_tasks/2_pul.png')
# list_2_xp = my_OCR.recognized("img/test/test_tasks/2_xp.png")
# sleep(2)
# list_3_pul = my_OCR.recognized('img/test/test_tasks/3_pul.png')
# list_3_xp = my_OCR.recognized("img/test/test_tasks/3_xp.png")
# #
# event_OCR.visualization_tascks_result(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp)





# опознание уровня
# lvl_img()
# list_lvl = my_OCR.recognized('img/test/lvl.png')
# event_OCR.visualization_lvl_result(list_lvl)
