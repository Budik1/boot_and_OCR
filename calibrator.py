import baza.baza_paths
from baza.baza_paths import actual_caliber
import stereotypes
import os_action
from tools import print_log

view_log = True
### 1 Действие:
# Определить масштаб.
caliber = str(stereotypes.interest_point.get_caliber_corner())
# переопределить переменную для путей
baza.baza_paths.actual_caliber = caliber

print_log(caliber, type(caliber), log=view_log)
print(f'масштаб {caliber}')
#
check_folder_caliber = os_action.check_folder_or_file(my_path=f'img/{caliber}')
print_log(check_folder_caliber, log=view_log)
if not check_folder_caliber:
    os_action.create_folder(path=f'img/{caliber}')
stereotypes.interest_point.cr_img_line_button_pm()

### 2 Действие:
# Попробовать опознать персонажа.
# Получить имя персонажа если не опоз.
ans_1 = 'Назови героя, чтобы помощник с ним мог общаться: '
name_pers = 'pers_id'
### 3 Действие:

###

###
###

salute = 'Начнем знакомство.'
ans_2 = ''
msg_starting_point = 'Для корректного проведения калибровки перемести своего персонажа на ст. Новокузнецкая'
# default
# Создание : img/{caliber}/person/hero_id/{pers_id}/her_gadya.png
# Создание :img/{caliber}/person/hero_id/{pers_id}/menu_acc_her_gadya.png
