import json
# import icecream

import heroes
import tools
import os_action
from baza import baza_paths as b_p
from tools import color_text as c_t


def save_all_state_config_json(*, info=False):
    date_n = tools.date_now()
    time_n = tools.date_and_time_in_name_file()
    path_temp_folder = f'temp_pack/all/{date_n}'
    os_action.create_folder(path=path_temp_folder)
    path_lst = ['storage/config.json', f'{path_temp_folder}/config_{time_n}.json']
    for key in heroes.hero_dict:
        heroes.Hero.get_state_all(heroes.hero_dict[key])
    json_data = json.dumps(heroes.list_all_state, ensure_ascii=False)
    for file_name_json in path_lst:
        write_json_file(file_name=file_name_json, json_data=json_data, info=info)


def save_kv_state_config_json(*, info=False):
    date_n = tools.date_now()
    time_n = tools.date_and_time_in_name_file()
    path_temp_folder = f'temp_pack/kv/kv_{date_n}'
    os_action.create_folder(path=path_temp_folder)
    path_lst = ['storage/config_kv.json', f'{path_temp_folder}/config_kv {time_n}.json']
    for key in heroes.hero_dict:
        heroes.Hero.get_state_kv(heroes.hero_dict[key])
    json_data = json.dumps(heroes.list_kv_state2, ensure_ascii=False)
    for file_name_json in path_lst:
        write_json_file(file_name=file_name_json, json_data=json_data, info=info)


def write_json_file(*, file_name, json_data, info=False):
    rapport = ''
    if info:
        text = c_t.tc_green('запись состояния')
        rapport = f"{file_name} {text}"
    try:
        with open(file_name, 'w', encoding='utf-8') as file_:
            file_.write(json_data)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = c_t.tc_red(f'Файл  не найден!')
        rapport = f'{file_name} {text}'
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = c_t.tc_red('Произошла ошибка ввода-вывода при чтении файла!')
        rapport = f"{file_name} {text}"
    except Exception as e:
        # Обработка других неожиданных исключений
        text = c_t.tc_red(f'Произошла неожиданная ошибка: {e}')
        rapport = f"{file_name} {text}"
    finally:
        if rapport:
            print(rapport)
    return


def load_json_file(*, file_name, info=False):
    """
    Чтение json файла и обработка возможных ошибок.
    :param file_name:
    :param info:
    :return result: Первый параметр True если чтение прошло без ошибок. Иначе False
    :return data_load: Содержимое файла
    """
    tx2 = f"'{file_name}'"
    rapport = ''
    data_load = None
    if info:
        text = c_t.tc_green("чтение состояния")
        rapport = f'{file_name} {text}'
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data_load = json.load(f)
            result = True
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        # print(f"Файл '{file_name}' не найден!")
        tx1 = c_t.tc_red('Файл ')
        tx3 = c_t.tc_red(' не найден!')
        rapport = f"{tx1}{tx2}{tx3}"
        result = False
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        tx1 = c_t.tc_red('Произошла ошибка ввода-вывода при чтении ')
        tx3 = c_t.tc_red(' файла!')
        rapport = f"{tx1}{tx2}{tx3}"
        result = False
    except Exception as e:
        # Обработка других неожиданных исключений
        tx1 = c_t.tc_red("Файл ")
        tx3 = c_t.tc_red(f". Произошла неожиданная ошибка: {e}")
        rapport = f"{tx1}{tx2}{tx3}"
        rapport = f"{file_name}"
        result = False
    finally:
        if rapport:
            print(rapport)
    return result, data_load


def reading_all_state_config(*, info=True):
    file_name_json = b_p.retention_all
    rapport = ''
    result = True
    if info:
        text = c_t.tc_green("чтение состояния")
        rapport = f'{file_name_json} {text}'
    try:
        with open(file_name_json, 'r', encoding='utf-8') as f:
            heroes.list_all_state = json.load(f)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        rapport = f"Файл '{file_name_json}' не найден!"
        result = False
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        rapport = f"Произошла ошибка ввода-вывода при чтении '{file_name_json}' файла!"
        result = False
    except Exception as e:
        # Обработка других неожиданных исключений
        rapport = f"Файл '{file_name_json}'. Произошла неожиданная ошибка: {e}"
        result = False
    finally:
        if not result:
            save_all_state_config_json(info=False)
        if rapport:
            print(rapport)
    return result


def reading_kv_config_json(*, info=True):
    file_name_json = b_p.retention_kv
    result, data_load = load_json_file(file_name=file_name_json, info=info)
    if result:
        heroes.list_kv_state = data_load
    return result



def setting_updatable_values():
    """Установка обновляемых(ежедневных) значений при (пере)запуске программы"""
    for key in heroes.hero_dict:
        heroes.Hero.set_updatable_values(heroes.hero_dict[key])


def setting_cumulative_values():
    """Установка накопительных значений при (пере)запуске программы"""
    for key in heroes.hero_dict:
        heroes.Hero.set_cumulative_values(heroes.hero_dict[key])


def set_values_kv():
    heroes.Hero.set_state_kv(heroes.Activ.hero_activ)
    save_kv_state_config_json(info=False)
