import pickle
import fun
from my_color_text import tc_green, tc_cyan, tc_blue, tc_red
import heroes as her
from heroes import Activ

# def check_date(loaded_data):
#     """Установка значений при (пере)запуске программы"""
#     check_date_ = loaded_data['date']
#     # check_date_ = 0
#
#     her.gady.wildman_count = loaded_data['gady.wildman_all']
#     her.gavr.wildman_count = loaded_data['gavr.wildman_all']
#
#     her.gady.days_count = loaded_data['gady.days_counting']
#     her.gavr.days_count = loaded_data['gavr.days_counting']
#     # her.gavr.days_counting += 1
#
#     # если даты совпадают:- значения устанавливаются из файла
#     if check_date_ == Activ.date_start:
#         print(tc_blue("даты совпадают"))
#         # присваиваем значения
#         her.gady.wild_activ = loaded_data['gady.wild_activ']
#         her.gady.completing_tasks = loaded_data['gady.completing_tasks']
#         her.gavr.wild_activ = loaded_data['gavr.wild_activ']
#         her.gavr.completing_tasks = loaded_data['gavr.completing_tasks']
#
#         her.gavr.vip = loaded_data['gavr_vip']
#         her.gady.vip = loaded_data['gady_vip']
#         her.mara.vip = loaded_data['mara_vip']
#         her.veles.vip = loaded_data['veles_vip']
#
#         her.gavr.grey_rat = loaded_data['gavr_krysy']
#         her.gady.grey_rat = loaded_data['gady_krysy']
#         her.mara.grey_rat = loaded_data['mara_krysy']
#         her.veles.grey_rat = loaded_data['veles_krysy']
#
#         her.gavr.kiki = loaded_data['gavr_kiki']
#         her.gady.kiki = loaded_data['gady_kiki']
#         her.mara.kiki = loaded_data['mara_kiki']
#         her.veles.kiki = loaded_data['veles_kiki']
#
#         her.gavr.arachne = loaded_data['gavr_arachne']
#         her.gady.arachne = loaded_data['gady_arachne']
#         her.mara.arachne = loaded_data['mara_arachne']
#         her.veles.arachne = loaded_data['veles_arachne']
#
#         her.gavr.raptor = loaded_data['gavr_raptor']
#         her.gady.raptor = loaded_data['gady_raptor']
#         her.mara.raptor = loaded_data['mara_raptor']
#         her.veles.raptor = loaded_data['veles_raptor']
#
#         her.gavr.gifts = loaded_data['gavr_gifts']
#         her.gady.gifts = loaded_data['gady_gifts']
#         her.mara.gifts = loaded_data['mara_gifts']
#         her.veles.gifts = loaded_data['veles_gifts']
#
#         her.gavr.wildman = loaded_data['gavr_wild']
#         her.gady.wildman = loaded_data['gady_wild']
#         her.mara.wildman = loaded_data['mara_wild']
#         her.veles.wildman = loaded_data['veles_wild']
#
#         # her.gady.completing_tasks = l
#
#         # отображаем значения
#
#
#         displaying_values()
#     # иначе отображение и сохранение стартовых значений
#     else:
#
#         her.gady.days_count += 1
#         # her.gady.days_counting = 0
#         her.gavr.days_count += 1
#         # her.gavr.days_counting = 0
#         print(f"gady {her.gady.days_count} {fun.transform_days(her.gady.days_count)}, {her.gady.wildman_count} дикарей")
#         print(f'gavr {her.gavr.days_count} {fun.transform_days(her.gavr.days_count)}, {her.gavr.wildman_count} дикарей')
#
#         print(tc_cyan("даты не совпадают, смена суток"))
#         gavr_vip.set(str(starting_value))
#         gady_vip.set(str(starting_value))
#         mara_vip.set(starting_value)
#         veles_vip.set(starting_value)
#
#         displaying_values()
#         save_to_file()


def save_to_file():
    print(tc_green("запись состояния"))

    data_to_save = {
        'date': Activ.date_start,
        'gavr_vip': her.gavr.vip,
        'gady_vip': her.gady.vip,
        'mara_vip': her.mara.vip,
        'veles_vip': her.veles.vip,

        'gavr_krysy': her.gavr.grey_rat,
        'gady_krysy': her.gady.grey_rat,
        'mara_krysy': her.mara.grey_rat,
        'veles_krysy': her.veles.grey_rat,

        'gavr_kiki': her.gavr.kiki,
        'gady_kiki': her.gady.kiki,
        'mara_kiki': her.mara.kiki,
        'veles_kiki': her.veles.kiki,

        'gavr_arachne': her.gavr.arachne,
        'gady_arachne': her.gady.arachne,
        'mara_arachne': her.mara.arachne,
        'veles_arachne': her.veles.arachne,

        'gavr_raptor': her.gavr.raptor,
        'gady_raptor': her.gady.raptor,
        'mara_raptor': her.mara.raptor,
        'veles_raptor': her.veles.raptor,

        'gavr_gifts': her.gavr.gifts,
        'gady_gifts': her.gady.gifts,
        'mara_gifts': her.mara.gifts,
        'veles_gifts': her.veles.gifts,

        'gavr_wild': her.gavr.wildman,
        'gady_wild': her.gady.wildman,
        'mara_wild': her.mara.wildman,
        'veles_wild': her.veles.wildman,

        'gady.wildman_all': her.gady.wildman_count,
        'gavr.wildman_all': her.gavr.wildman_count,

        'gady.days_counting': her.gady.days_count,
        'gavr.days_counting': her.gavr.days_count,

        'gady.completing_tasks' : her.gady.completing_tasks,
        'gady.wild_activ'  : her.gady.wild_activ,
        'gavr.completing_tasks' : her.gavr.completing_tasks,
        'her.gavr.wild_activ' : her.gavr.wild_activ,

    }
    # print(data_to_save)
    file1 = open('config.bin', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


# def read_from_file():
#     print(tc_green("чтение состояния"))
#     try:
#         file1 = open('config.bin', 'rb')
#         data_to_load = pickle.load(file1)
#         file1.close()
#         check_date(data_to_load)
#     except:
#         print(tc_red("файл поврежден или не создан"))
#         displaying_values()
#         save_to_file()
