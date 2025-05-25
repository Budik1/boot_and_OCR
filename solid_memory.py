import pickle
import heroes as her
from heroes import Activ
from my_color_text import tc_green, tc_cyan, tc_blue, tc_red
import fun

def save_to_file(info=True):
    if info:
        print(tc_green("запись состояния"))
    data_to_save = {
        # дата
        'date': Activ.date_now,
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
        #
        'gady.energy_count_now': her.gady.energy_count_today,
        'gavr.energy_count_now': her.gavr.energy_count_today,
        'veles.energy_count_now': her.veles.energy_count_today,
        'mara.energy_count_now': her.mara.energy_count_today,
        #
        'gady.energy_count_all': her.gady.energy_all_count,
        'gavr.energy_count_all': her.gavr.energy_all_count,
        'veles.energy_count_all': her.veles.energy_all_count,
        'mara.energy_count_all': her.mara.energy_all_count,
        #
        'gady.wildman_all': her.gady.wildman_count,
        'gavr.wildman_all': her.gavr.wildman_count,
        #
        'gady.days_counting': her.gady.wildman_days_count,
        'gavr.days_counting': her.gavr.wildman_days_count,
        #
        'gady.completing_tasks': her.gady.completing_tasks,
        'gavr.completing_tasks': her.gavr.completing_tasks,
        #
        'gady.wild_activ': her.gady.wild_activ,
        'gavr.wild_activ': her.gavr.wild_activ,
    }
    try:
        file1 = open('config.bin', 'wb')
        pickle.dump(data_to_save, file1)
    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        print(tc_red(f"Файл  не найден!"))
    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        print(tc_red("Произошла ошибка ввода-вывода при чтении файла!"))
    except Exception as e:
        # Обработка других неожиданных исключений
        print(tc_red(f"Произошла неожиданная ошибка: {e}"))
    finally:
        file1.close()


def read_from_file():
    print(tc_green("чтение состояния"))
    file_name = 'config.bin'
    try:
        file1 = open(file_name, 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        result =  True, data_to_load
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
        print('???')
        save_to_file()
    return result


def setting_updatable_values(loaded_data):
    """Установка обновляемых(ежедневных) значений при (пере)запуске программы"""
    Activ.check_date_ = loaded_data['date']
    # если даты совпадают:- значения устанавливаются из файла
    if Activ.check_date_ == Activ.date_now:
        print(tc_blue("даты совпадают"))
        # присваиваем значения
        her.gady.energy_count_today = loaded_data['gady.energy_count_now']
        her.gavr.energy_count_today = loaded_data['gavr.energy_count_now']
        her.veles.energy_count_today = loaded_data['veles.energy_count_now']
        her.mara.energy_count_today = loaded_data['mara.energy_count_now']

        her.gady.wild_activ = loaded_data['gady.wild_activ']
        her.gavr.wild_activ = loaded_data['gavr.wild_activ']

        her.gavr.completing_tasks = loaded_data['gavr.completing_tasks']
        her.gady.completing_tasks = loaded_data['gady.completing_tasks']

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

    else:
        # если даты не совпадают:- значения устанавливаются на "0"
        print(tc_cyan("даты не совпадают, смена суток"))



def setting_cumulative_values(loaded_data):
    """Установка накопительных значений при (пере)запуске программы"""
    # кол-во потраченной энергии за время учета
    her.gady.energy_all_count = loaded_data['gady.energy_count_all']
    her.gavr.energy_all_count = loaded_data['gavr.energy_count_all']
    her.veles.energy_all_count = loaded_data['veles.energy_count_all']
    her.mara.energy_all_count = loaded_data['mara.energy_count_all']
    # кол-во дикарей
    her.gady.wildman_count = loaded_data['gady.wildman_all']
    her.gavr.wildman_count = loaded_data['gavr.wildman_all']
    # кол-во дней учета дикарей
    her.gady.wildman_days_count = loaded_data['gady.days_counting']
    her.gavr.wildman_days_count = loaded_data['gavr.days_counting']
    # кол-во выполненных заданий
    her.gady.task_count = loaded_data['gady.task_count']
    her.gavr.task_count = loaded_data['gavr.task_count']
    her.veles.task_count = loaded_data['veles.task_count']
    her.mara.task_count = loaded_data['mara.task_count']

    print(
        f"gady {her.gady.wildman_days_count} {fun.transform_days(qty_days=her.gady.wildman_days_count)},"
        f" {her.gady.wildman_count} {fun.transform_wilds(qty_days=her.gady.wildman_count)}")
    print(
        f'gavr {her.gavr.wildman_days_count} {fun.transform_days(qty_days=her.gavr.wildman_days_count)},'
        f' {her.gavr.wildman_count} {fun.transform_wilds(qty_days=her.gavr.wildman_count)}')