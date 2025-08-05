import pickle

import fun
import complex_phrases
import heroes as her
from heroes import Activ
from color_text import tc_green, tc_cyan, tc_blue, tc_red


def save_to_file(info=True):
    file_name = 'config.bin'
    if info:
        text = tc_green('запись состояния')
        print(f"{file_name} {text}")
    data_to_save = {
        # дата
        'date': Activ.date_now,
        # прописка
        'gady.home_location': her.gady.home_location,
        'gavr.home_location': her.gavr.home_location,
        'mara.home_location': her.mara.home_location,
        'veles.home_location': her.veles.home_location,

        # состояние
        'gavr_vip': her.gavr.vip,
        'gady_vip': her.gady.vip,
        'mara_vip': her.mara.vip,
        'veles_vip': her.veles.vip,
        #
        'gavr_krysy': her.gavr.grey_rat,
        'gady_krysy': her.gady.grey_rat,
        'mara_krysy': her.mara.grey_rat,
        'veles_krysy': her.veles.grey_rat,
        #
        'gavr_kiki': her.gavr.kiki,
        'gady_kiki': her.gady.kiki,
        'mara_kiki': her.mara.kiki,
        'veles_kiki': her.veles.kiki,
        #
        'gavr_arachne': her.gavr.arachne,
        'gady_arachne': her.gady.arachne,
        'mara_arachne': her.mara.arachne,
        'veles_arachne': her.veles.arachne,
        #
        'gavr_raptor': her.gavr.raptor,
        'gady_raptor': her.gady.raptor,
        'mara_raptor': her.mara.raptor,
        'veles_raptor': her.veles.raptor,
        #
        'gavr_gifts': her.gavr.gifts,
        'gady_gifts': her.gady.gifts,
        'mara_gifts': her.mara.gifts,
        'veles_gifts': her.veles.gifts,
        #
        'gavr_wild': her.gavr.wildman,
        'gady_wild': her.gady.wildman,
        'mara_wild': her.mara.wildman,
        'veles_wild': her.veles.wildman,
        #
        'gady.task_count': her.gady.task_count,
        'gavr.task_count': her.gavr.task_count,
        'veles.task_count': her.veles.task_count,
        'mara.task_count': her.mara.task_count,
        # по арене
        'gady.arena_count': her.gady.arena_count,
        'gady.arena_victory_count': her.gady.arena_victory_count,
        #
        'gady.energy_count_now': her.gady.energy_count_today,
        'gavr.energy_count_now': her.gavr.energy_count_today,
        'veles.energy_count_now': her.veles.energy_count_today,
        'mara.energy_count_now': her.mara.energy_count_today,
        #
        'gady.energy_count_all': her.gady.energy_count_all,
        'gavr.energy_count_all': her.gavr.energy_count_all,
        'veles.energy_count_all': her.veles.energy_count_all,
        'mara.energy_count_all': her.mara.energy_count_all,
        #
        'gady.wildman_all': her.gady.wildman_count,
        'gavr.wildman_all': her.gavr.wildman_count,
        'veles.wildman_all': her.veles.wildman_count,
        'mara.wildman_all': her.mara.wildman_count,
        #
        'gady.days_counting': her.gady.wildman_days_count,
        'gavr.days_counting': her.gavr.wildman_days_count,
        'veles.days_counting': her.veles.wildman_days_count,
        'mara.days_counting': her.mara.wildman_days_count,
        #
        'gady.completing_tasks': her.gady.completing_tasks,
        'gavr.completing_tasks': her.gavr.completing_tasks,
        'veles.completing_tasks': her.veles.completing_tasks,
        'mara.completing_tasks': her.mara.completing_tasks,
        #
        'gady.wild_activ': her.gady.wild_activ,
        'gavr.wild_activ': her.gavr.wild_activ,
        'veles.wild_activ': her.veles.wild_activ,
        'mara.wild_activ': her.mara.wild_activ,
    }
    # heroes123 = [
    #      {
    #         "id": "gady",
    #         'home_location': "",
    #         'vip': "",
    #         'grey_rat': "",
    #         'kiki': "",
    #         'arachne': "",
    #         'raptor': "",
    #     },{
    #         "id": "gavr",
    #         'home_location': "",
    #         'vip': "",
    #         'grey_rat': "",
    #         'kiki': "",
    #         'arachne': "",
    #         'raptor': "",
    #     },
    # ]
    #
    # heroes_to_save = []
    # for heroTemplate in heroes123:
    #     hero = heroes.Hero(name_ru_=heroTemplate.name_ru_, name_en_=heroTemplate.id, name_file_=heroTemplate.file)
    #     heroes_to_save.append(hero)
    #
    # for hero in heroes_to_save:
    #     data_to_save = hero.get_data_to_save()

    try:
        file1 = open(file_name, 'wb')
        pickle.dump(data_to_save, file1)
        file1.close()
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = tc_red('Файл  не найден!')
        print(f"{file_name} {text}")
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = tc_red('Произошла ошибка ввода-вывода при чтении файла!')
        print(f"{file_name} {text}")
    except Exception as e:
        # Обработка других неожиданных исключений
        text = tc_red(f'Произошла неожиданная ошибка: {e}')
        print(f"{file_name} {text}")
    return


def save_wild_state(info=True):
    file_name = 'config_wild.bin'
    if info:
        text = tc_green('запись состояния')
        print(f"{file_name} {text}")
    data_wild = {
        'gavr_wild': her.gavr.wildman,
        'gady_wild': her.gady.wildman,
        'mara_wild': her.mara.wildman,
        'veles_wild': her.veles.wildman,
        #
        'gady.energy_count_all': her.gady.energy_count_all,
        'gavr.energy_count_all': her.gavr.energy_count_all,
        'veles.energy_count_all': her.veles.energy_count_all,
        'mara.energy_count_all': her.mara.energy_count_all,
        #
        'gady.wildman_all': her.gady.wildman_count,
        'gavr.wildman_all': her.gavr.wildman_count,
        'veles.wildman_all': her.veles.wildman_count,
        'mara.wildman_all': her.mara.wildman_count,
        #
        'gady.days_counting': her.gady.wildman_days_count,
        'gavr.days_counting': her.gavr.wildman_days_count,
        'veles.days_counting': her.veles.wildman_days_count,
        'mara.days_counting': her.mara.wildman_days_count,
        #
        'gady.wild_activ': her.gady.wild_activ,
        'gavr.wild_activ': her.gavr.wild_activ,
        'veles.wild_activ': her.veles.wild_activ,
        'mara.wild_activ': her.mara.wild_activ,
    }
    try:
        file1 = open(file_name, 'wb')
        pickle.dump(data_wild, file1)
        file1.close()
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = tc_red('Файл  не найден!')
        print(f"{file_name} {text}")
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = tc_red('Произошла ошибка ввода-вывода при чтении файла!')
        print(f"{file_name} {text}")
    except Exception as e:
        # Обработка других неожиданных исключений
        text = tc_red(f'Произошла неожиданная ошибка: {e}')
        print(f"{file_name} {text}")


def reading_file(*, info=True):
    file_name = 'config.bin'
    if info:
        text = tc_green("чтение состояния")
        print(f'{file_name} {text}')
    try:
        file1 = open(file_name, 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result = True, data_to_load
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        print(f"Файл '{file_name}' не найден!")
        result = False, False
        save_to_file()
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        print(f"Произошла ошибка ввода-вывода при чтении '{file_name}' файла!")
        result = False, False
        save_to_file()
    except Exception as e:
        # Обработка других неожиданных исключений
        print(f"Файл '{file_name}'")
        print(f"Произошла неожиданная ошибка: {e}")
        result = False, False
        save_to_file()
    finally:
        # print('???')
        save_to_file(info=False)
    return result


def reading_wild_file(*, info=True):
    file_name = 'config_wild.bin'
    if info:
        text = tc_green("чтение состояния")
        print(f'{file_name} {text}')
    try:
        file1 = open(file_name, 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result = True, data_to_load
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        text = tc_red('не найден!')
        print(f"'{file_name}' {text}")
        result = False, False
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        text = tc_red('Произошла ошибка ввода-вывода при чтении ')
        print(f"'{file_name}' {text}")
        result = False, False
    except Exception as e:
        # Обработка других неожиданных исключений
        text = f"Произошла неожиданная ошибка: {e}"
        print(f"'{file_name}' {text}")
        result = False, False
    finally:
        # print('???')
        pass
    return result


def setting_updatable_values(loaded_data):
    """Установка обновляемых(ежедневных) значений при (пере)запуске программы"""
    # Activ.check_date_ = 1
    Activ.check_date_ = loaded_data['date']
    # если даты совпадают:- значения устанавливаются из файла
    if Activ.check_date_ == Activ.date_now:
        print(tc_blue("даты совпадают"))
        # присваиваем значения
        her.gady.arena_count = loaded_data['gady.arena_count']

        her.gady.energy_count_today = loaded_data['gady.energy_count_now']
        her.gavr.energy_count_today = loaded_data['gavr.energy_count_now']
        her.veles.energy_count_today = loaded_data['veles.energy_count_now']
        her.mara.energy_count_today = loaded_data['mara.energy_count_now']

        her.gady.wild_activ = loaded_data['gady.wild_activ']
        her.gavr.wild_activ = loaded_data['gavr.wild_activ']
        her.veles.wild_activ = loaded_data['veles.wild_activ']
        her.mara.wild_activ = loaded_data['mara.wild_activ']

        her.gavr.completing_tasks = loaded_data['gavr.completing_tasks']
        her.gady.completing_tasks = loaded_data['gady.completing_tasks']
        her.veles.completing_tasks = loaded_data['veles.completing_tasks']
        her.mara.completing_tasks = loaded_data['mara.completing_tasks']

        her.gavr.vip = loaded_data['gavr_vip']
        her.gady.vip = loaded_data['gady_vip']
        her.mara.vip = loaded_data['mara_vip']
        her.veles.vip = loaded_data['veles_vip']

        her.gavr.grey_rat = loaded_data['gavr_krysy']
        her.gady.grey_rat = loaded_data['gady_krysy']
        her.mara.grey_rat = loaded_data['mara_krysy']
        her.veles.grey_rat = loaded_data['veles_krysy']

        her.gavr.kiki = loaded_data['gavr_kiki']
        her.gady.kiki = loaded_data['gady_kiki']
        her.mara.kiki = loaded_data['mara_kiki']
        her.veles.kiki = loaded_data['veles_kiki']

        her.gavr.arachne = loaded_data['gavr_arachne']
        her.gady.arachne = loaded_data['gady_arachne']
        her.mara.arachne = loaded_data['mara_arachne']
        her.veles.arachne = loaded_data['veles_arachne']

        her.gavr.raptor = loaded_data['gavr_raptor']
        her.gady.raptor = loaded_data['gady_raptor']
        her.mara.raptor = loaded_data['mara_raptor']
        her.veles.raptor = loaded_data['veles_raptor']

        her.gavr.gifts = loaded_data['gavr_gifts']
        her.gady.gifts = loaded_data['gady_gifts']
        her.mara.gifts = loaded_data['mara_gifts']
        her.veles.gifts = loaded_data['veles_gifts']

        her.gavr.wildman = loaded_data['gavr_wild']
        her.gady.wildman = loaded_data['gady_wild']
        her.mara.wildman = loaded_data['mara_wild']
        her.veles.wildman = loaded_data['veles_wild']

        print()
        print('solid_memory.setting_updatable_values')
        print(f'{her.gady.wild_activ=}')
        print(f'{her.gavr.wild_activ=}')
        print(f'{her.veles.wild_activ=}')
        print(f'{her.mara.wild_activ=}')
    else:
        # если даты не совпадают:- значения устанавливаются на "0"
        print(tc_cyan("даты не совпадают, смена суток"))


def setting_cumulative_values(loaded_data):
    """Установка накопительных значений при (пере)запуске программы"""
    #
    her.gady.home_location = loaded_data['gady.home_location']
    her.gavr.home_location = loaded_data['gavr.home_location']
    her.veles.home_location = loaded_data['veles.home_location']
    her.mara.home_location = loaded_data['mara.home_location']

    # кол-во потраченной энергии за время учета
    her.gady.energy_count_all = loaded_data['gady.energy_count_all']
    her.gavr.energy_count_all = loaded_data['gavr.energy_count_all']
    her.veles.energy_count_all = loaded_data['veles.energy_count_all']
    her.mara.energy_count_all = loaded_data['mara.energy_count_all']
    # кол-во дикарей
    her.gady.wildman_count = loaded_data['gady.wildman_all']
    her.gavr.wildman_count = loaded_data['gavr.wildman_all']
    her.veles.wildman_count = loaded_data['veles.wildman_all']
    her.mara.wildman_count = loaded_data['mara.wildman_all']
    # кол-во дней учета дикарей
    her.gady.wildman_days_count = loaded_data['gady.days_counting']
    her.gavr.wildman_days_count = loaded_data['gavr.days_counting']
    her.veles.wildman_days_count = loaded_data['veles.days_counting']
    her.mara.wildman_days_count = loaded_data['mara.days_counting']
    # кол-во выполненных заданий
    her.gady.task_count = loaded_data['gady.task_count']
    her.gavr.task_count = loaded_data['gavr.task_count']
    her.veles.task_count = loaded_data['veles.task_count']
    her.mara.task_count = loaded_data['mara.task_count']
