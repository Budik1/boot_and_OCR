
import baza.baza_paths
import stereotypes
import os_action
import tools
import find_img
from tools import print_log
import x_scale

view_log: bool = True
color_sys = tools.color_text.tc_cyan


### 1 Действие:
# Определить масштаб.
caliber = str(stereotypes.interest_point.get_caliber_line_menu())
print_log(caliber, type(caliber), log=view_log)
if caliber:
    check_img_caliber_line_menu = True
else:
    caliber = str(stereotypes.interest_point.get_caliber_corner())
    check_img_caliber_line_menu = False
# переопределить переменную для путей
baza.baza_paths.actual_caliber_folder = caliber

print()
print(f'Определён масштаб = {caliber}')
print(f'Папка масштаба = {baza.baza_paths.actual_caliber_folder}')
#
check_folder_caliber = os_action.check_folder_or_file(my_path=f'img/{caliber}')
print_log('определение масштаба по меню',check_folder_caliber, log=view_log)
if not check_folder_caliber:
    os_action.create_folder(path=f'img/{caliber}')
if not check_img_caliber_line_menu:
    stereotypes.interest_point.cr_img_line_button_pm(caliber=caliber)

### 2 Действие:
# Попробовать опознать персонажа
pers_name = x_scale.act.get_pers_name(skale=caliber)
if pers_name:
    capitalize_pers_name = pers_name.capitalize()
    print(F'Опознан {capitalize_pers_name}')
else:
    print('Персонаж не опознан))')
    print('Будем знакомиться. Выбери имя')
    name = input('Gady(1), Gavr(2), Mara(3) : ')
    hero_name_dict = {'1': 'gady', '2': 'gavr', '3': 'mara'}
    x_scale.act.cr_pers_png(name=hero_name_dict[name], skale=caliber)


# print(color_sys('Для корректного проведения калибровки перемести своего персонажа на ст. Киевская или ст. Фрунзенская'))
# print(color_sys('На какой из указанных станций ты сейчас?'))
# ans_1 = input(color_sys('ст. Киевская (1) ст. Фрунзенская (2) : '))
# if ans_1 == '1':
#     print(color_sys('Выбрана ст. Киевская'))
#     start_st = 'ст. Киевская'
# elif ans_1 == '2':
#     print(color_sys('Выбрана ст. Фрунзенская'))
#     start_st = 'ст. Фрунзенская'



# получить

# 3


### Герой
### Инфо
### клан
### Иконка зал славы
### Идентификатор станции
