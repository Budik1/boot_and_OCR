import time
import pickle

# import fun
# import complex_phrases
import heroes
import heroes as her
from heroes import Activ
from color_text import tc_green, tc_cyan, tc_blue, tc_red


def save_all_state_config(info=True):
    file_name = 'config.bin'
    rapport = ''
    if info:
        text = tc_green('запись состояния')
        rapport = f"{file_name} {text}"

    for key in heroes.hero_dict:
        heroes.Hero.get_state_all(heroes.hero_dict[key])
    # print('save')
    # print(heroes.list_all_state)
    try:
        file1 = open(file_name, 'wb')
        pickle.dump(heroes.list_all_state, file1)
        file1.close()
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = tc_red(f'Файл  не найден!')
        rapport = f'{file_name} {text}'
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = tc_red('Произошла ошибка ввода-вывода при чтении файла!')
        rapport = f"{file_name} {text}"
    except Exception as e:
        # Обработка других неожиданных исключений
        text = tc_red(f'Произошла неожиданная ошибка: {e}')
        rapport = "{file_name} {text}"
    finally:
        if rapport != '':
            print(rapport)
    return


def reading_all_state_config(*, info=True):
    file_name = 'config.bin'
    rapport = ''
    if info:
        text = tc_green("чтение состояния")
        rapport = f'{file_name} {text}'
    try:
        file1 = open(file_name, 'rb')
        heroes.list_all_state = pickle.load(file1)
        file1.close()
        result = True
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        # print(f"Файл '{file_name}' не найден!")
        rapport = f"Файл '{file_name}' не найден!"
        result = False
        save_all_state_config()
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        rapport = f"Произошла ошибка ввода-вывода при чтении '{file_name}' файла!"
        result = False
        save_all_state_config()
    except Exception as e:
        # Обработка других неожиданных исключений
        rapport = f"Файл '{file_name}'. Произошла неожиданная ошибка: {e}"
        result = False
        save_all_state_config()
    finally:
        if rapport != '':
            print(rapport)
    return result


def save_kv_config(info=True):
    file_name = 'kv_config.bin'
    rapport = ''
    if info:
        text = tc_green(f'запись состояния')
        rapport = f"{file_name} {text}"
    data_to_save = {
        # дата
        'gady.hour_start_kv': heroes.gady.time_start_kv,

        'gady.duel_all': heroes.gady.qty_duel_all,
        'gady.duel_victory_all': heroes.gady.qty_duel_all_victory,
        'gady.duel_now': heroes.gady.qty_duel_in_kv_all,
        'gady.duel_victory_now': heroes.gady.qty_duel_in_kv_victory,
        'gady.count_shoulder_straps': heroes.gady.count_shoulder_straps_all,
        'gady.count_shoulder_straps_kv': heroes.gady.count_shoulder_straps_kv,

    }

    try:
        file1 = open(file_name, 'wb')
        pickle.dump(data_to_save, file1)
        file1.close()
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = tc_red('Файл  не найден!')
        rapport = f"{file_name} {text}"
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = tc_red('Произошла ошибка ввода-вывода при чтении файла!')
        rapport = f"{file_name} {text}"
    except Exception as e:
        # Обработка других неожиданных исключений
        text = tc_red(f'Произошла неожиданная ошибка: {e}')
        rapport = f"{file_name} {text}"
    finally:
        if rapport != '':
            print(rapport)
    return


def reading_kv_config(*, info=True):
    file_name = 'kv_config.bin'
    rapport = ''
    if info:
        text = tc_green(f"чтение состояния")
        rapport = f'{file_name} {text}'
    try:
        file1 = open(file_name, 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result = True, data_to_load
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        rapport = f"Файл '{file_name}' не найден!"
        result = False, False
        save_kv_config()
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        rapport = f"Произошла ошибка ввода-вывода при чтении '{file_name}' файла!"
        result = False, False
        save_kv_config()
    except Exception as e:
        # Обработка других неожиданных исключений
        print(f"")
        rapport = f"Файл '{file_name}' Произошла неожиданная ошибка: {e}"
        result = False, False
        save_kv_config()
    finally:
        if rapport != '':
            print(rapport)
    return result


def setting_updatable_values():
    """Установка обновляемых(ежедневных) значений при (пере)запуске программы"""
    for key in heroes.hero_dict:
        heroes.Hero.set_updatable_values(heroes.hero_dict[key])


def setting_cumulative_values():
    """Установка накопительных значений при (пере)запуске программы"""
    for key in heroes.hero_dict:
        heroes.Hero.set_cumulative_values(heroes.hero_dict[key])


def set_values_kv(data_kv):
    # print(data_kv)
    time_now = time.time()
    time_save = data_kv['gady.hour_start_kv']
    if (time_now - time_save) < 3 * 3600:
        print('Время старта КВ не изменилось')
        heroes.gady.time_start_kv = data_kv['gady.hour_start_kv']

        heroes.gady.qty_duel_in_kv_all = data_kv['gady.duel_now']
        heroes.gady.qty_duel_in_kv_victory = data_kv['gady.duel_victory_now']
        heroes.gady.count_shoulder_straps_kv = data_kv['gady.count_shoulder_straps_kv']

    else:
        print('Время старта КВ обновилось')
        heroes.gady.time_start_kv = time_now

        heroes.gady.qty_duel_in_kv_all = 0
        heroes.gady.qty_duel_in_kv_victory = 0

    # values_kv_cumulative
    heroes.gady.qty_duel_all_victory = data_kv['gady.duel_victory_all']
    heroes.gady.qty_duel_all = data_kv['gady.duel_all']
    heroes.gady.count_shoulder_straps_all = data_kv['gady.count_shoulder_straps']

    save_kv_config(info=False)
