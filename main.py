from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import fun
import station_master
import kv_and_raid
import touring
import person
import revision_of_tents
from event_arena import create_img_arena_object, kill
import pickle
from my_color_text import tc_green, tc_cyan, tc_blue, tc_red
import baza_dannyx as b_d
import heroes as her

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

date_start = fun.date_utc_now()
# стартовые значения
starting_value = 0


def displaying_values():
    gady_rat.set(her.gady.rat)
    gady_kiki.set(her.gady.kiki)
    gady_arachne.set(her.gady.arachne)
    gady_raptor.set(her.gady.raptor)
    gady_gift.set(her.gady.gifts)

    gavr_rat.set(her.gavr.rat)
    gavr_kiki.set(her.gavr.kiki)
    gavr_arachne.set(her.gavr.arachne)
    gavr_raptor.set(her.gavr.raptor)
    gavr_gift.set(her.gavr.gifts)

    mara_rat.set(her.mara.rat)
    mara_kiki.set(her.mara.kiki)
    mara_arachne.set(her.mara.arachne)
    mara_raptor.set(her.mara.raptor)
    mara_gift.set(her.mara.gifts)

    veles_rat.set(her.veles.rat)
    veles_kiki.set(her.veles.kiki)
    veles_arachne.set(her.veles.arachne)
    veles_raptor.set(her.veles.raptor)
    veles_gift.set(her.veles.gifts)


def check_date(loaded_data):
    """Установка значений при (пере)запуске программы"""
    date_ver = loaded_data['date']
    # если даты совпадают:- значения устанавливаются из файла
    if date_ver == date_start:
        print(tc_blue("даты совпадают"))
        # присваиваем значения
        her.gavr.vip = loaded_data['gavr_vip']
        her.gady.vip = loaded_data['gady_vip']
        her.mara.vip = loaded_data['mara_vip']
        her.veles.vip = loaded_data['veles_vip']

        her.gavr.rat = loaded_data['gavr_krysy']
        her.gady.rat = loaded_data['gady_krysy']
        her.mara.rat = loaded_data['mara_krysy']
        her.veles.rat = loaded_data['veles_krysy']

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
        # отображаем значения
        gavr_vip.set(her.gavr.vip)
        gady_vip.set(her.gady.vip)
        mara_vip.set(her.mara.vip)
        veles_vip.set(her.veles.vip)

        displaying_values()
    # иначе отображение и сохранение стартовых значений
    else:

        print(tc_cyan("даты не совпадают, смена суток"))
        gavr_vip.set(str(starting_value))
        gady_vip.set(str(starting_value))
        mara_vip.set(starting_value)
        veles_vip.set(starting_value)

        displaying_values()
        save_to_file()


def save_to_file():
    print(tc_green("запись состояния"))

    data_to_save = {
        'date': date_start,
        'gavr_vip': her.gavr.vip,
        'gady_vip': her.gady.vip,
        'mara_vip': her.mara.vip,
        'veles_vip': her.veles.vip,

        'gavr_krysy': her.gavr.rat,
        'gady_krysy': her.gady.rat,
        'mara_krysy': her.mara.rat,
        'veles_krysy': her.veles.rat,

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
    }
    # print(data_to_save)
    file1 = open('config.bin', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    print(tc_green("чтение состояния"))
    try:
        file1 = open('config.bin', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        check_date(data_to_load)
    except:
        print(tc_red("файл поврежден или не создан"))
        displaying_values()
        save_to_file()


def bonus():
    fun.bonus()


def en_1():
    station_master.en_task_item(1)
    save_to_file()


def en_2():
    station_master.en_task_item(2)
    save_to_file()


def en_3():
    station_master.en_task_item(3)
    save_to_file()


def dvizh_test():
    touring.test_run()
    displaying_values()
    save_to_file()


def kiki():
    touring.za_kikimorami()
    displaying_values()
    save_to_file()


def arachne_and_raptor():
    touring.pauk_yascher()
    displaying_values()
    save_to_file()


def tent_inspection():
    hero = fun.selection_hero()
    it_s = 0
    it_revision = 0
    fun.move_friends_list_to_top()

    while it_s < 10:
        if hero == 'Gady':
            it_s += revision_of_tents.tent_raid()
            her.gady.vip = it_s
            gady_vip.set(str(her.gady.vip))
            fun.move_friends_list_left()
        if hero == 'Gavr':
            it_s += revision_of_tents.tent_raid()
            her.gavr.vip = it_s
            gavr_vip.set(str(her.gavr.vip))
            fun.move_friends_list_left()
        if hero == 'Mara':
            it_s += revision_of_tents.tent_raid()
            her.mara.vip = it_s
            mara_vip.set(her.mara.vip)
            fun.move_friends_list_left()
        if hero == 'Велес':
            it_s += revision_of_tents.tent_raid()
            her.veles.vip = it_s
            veles_vip.set(her.veles.vip)
            fun.move_friends_list_left()
        it_revision += 1
        print(f'{it_s} из {it_revision}')
        if it_revision == 12:
            it_s = 10
            if hero == 'Gady':
                her.gady.vip = it_s
                gady_vip.set(str(her.gady.vip))
            if hero == 'Gavr':
                her.gavr.vip = it_s
                gavr_vip.set(str(her.gavr.vip))
            if hero == 'Mara':
                her.mara.vip = it_s
                mara_vip.set(her.mara.vip)
            if hero == 'Велес':
                her.veles.vip = it_s
                veles_vip.set(her.veles.vip)
    revision_of_tents.end_raid()
    save_to_file()


def frunze_kiev():
    touring.frunze_kiev()
    displaying_values()
    save_to_file()


def kiev_frunze():
    touring.kiev_frunze()
    displaying_values()
    save_to_file()


def most_frunze():
    touring.most_frunze()
    displaying_values()
    save_to_file()


def bulvar_frunze():
    touring.bulvar_frunze()
    displaying_values()
    save_to_file()


def frunze_bulvar():
    touring.frunze_bulvar()
    displaying_values()
    save_to_file()


def most_riga():
    touring.most_riga()
    displaying_values()
    save_to_file()


def riga_most():
    touring.riga_most()
    displaying_values()
    save_to_file()


def frunze_riga():
    touring.frunze_riga()
    displaying_values()
    save_to_file()


def riga_frunze():
    touring.riga_frunze()
    displaying_values()
    save_to_file()


def tasks_na_kievskoy():
    touring.tasks_na_kievskoy()
    displaying_values()
    save_to_file()


def collecting_gifts_at_stations():
    fun.push_close_all_()
    # определение героя
    hero = fun.selection_hero()
    # получение маршрута для определенного героя
    if hero == 'Велес':
        bypass_hero = b_d.bypass_veles
    elif hero == 'Mara':
        bypass_hero = b_d.bypass_mara
    elif hero == 'Gady':
        bypass_hero = b_d.bypass
    elif hero == 'Gavr':
        bypass_hero = b_d.bypass
    else:
        print('герой не опознан')
        return
    # движение по маршруту
    touring.sbor_podarkov(bypass_hero)
    # получение количества собранных подарков
    if hero == 'Велес':
        q_gifts = her.veles.gifts
    elif hero == 'Mara':
        q_gifts = her.mara.gifts
    elif hero == 'Gady':
        q_gifts = her.gady.gifts
    elif hero == 'Gavr':
        q_gifts = her.gavr.gifts
    else:
        print('герой не опознан')
        return
    # получение количества станций на маршруте
    q_st = fun.q_st_in_bypass(bypass_hero)
    # вывод информации
    print(f'На {q_st} станциях собрано {q_gifts} подарков')

    displaying_values()
    save_to_file()


root = Tk()

root.title(' помощник "Метро 2033"')
root.geometry("370x332+1200+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

gavr_vip = StringVar()
gady_vip = StringVar()
mara_vip = IntVar()
veles_vip = IntVar()

gavr_rat = StringVar()
gady_rat = StringVar()
mara_rat = IntVar()
veles_rat = IntVar()

gavr_kiki = StringVar()
gady_kiki = StringVar()
mara_kiki = StringVar()
veles_kiki = IntVar()

gavr_arachne = StringVar()
gady_arachne = StringVar()
mara_arachne = IntVar()
veles_arachne = IntVar()

gavr_raptor = StringVar()
gady_raptor = StringVar()
mara_raptor = IntVar()
veles_raptor = IntVar()

gavr_gift = StringVar()
gady_gift = StringVar()
mara_gift = IntVar()
veles_gift = IntVar()

read_from_file()

height_line = 30  # высота линии
line0 = 0
line1 = height_line * 1
line2 = height_line * 2
line3 = height_line * 3
line4 = height_line * 4
line5 = height_line * 5
line6 = height_line * 6
line7 = height_line * 7
line8 = height_line * 8
line9 = height_line * 9
line10 = height_line * 10

label_shift = 3  # смещение строки для Label
l_line0 = line0 + label_shift
l_line1 = line1 + label_shift
l_line2 = line2 + label_shift
l_line3 = line3 + label_shift
l_line4 = line4 + label_shift
l_line5 = line5 + label_shift
l_line6 = line6 + label_shift
l_line7 = line7 + label_shift
l_line8 = line8 + label_shift
l_line9 = line9 + label_shift
l_line10 = line10 + label_shift

# блок командных кнопок
ttk.Button(text="КВ", width=8, command=kv_and_raid.kv).place(x=0, y=line0)
ttk.Button(text=" Start ", width=14, command=fun.start_p_m).place(x=96, y=line0)
ttk.Button(text=" обход VIP ", width=10, command=tent_inspection).place(x=114, y=line1)
ttk.Button(text="кикиморы", width=10, command=kiki).place(x=114, y=line2)
ttk.Button(text="Паук+Ящер", width=10, command=arachne_and_raptor).place(x=114, y=line3)
ttk.Button(text="за дикарями", width=10, command=tasks_na_kievskoy).place(x=114, y=line4)
ttk.Button(text="обход всех станций", width=17, command=collecting_gifts_at_stations).place(x=51, y=line6)
ttk.Button(text="на Киев", width=8, command=frunze_kiev).place(x=51, y=line5)
ttk.Button(text="домой ", width=8, command=kiev_frunze).place(x=132, y=line5)
ttk.Button(text="frunze_riga", width=12, command=frunze_riga).place(x=0, y=line7)
ttk.Button(text="riga_frunze", width=12, command=riga_frunze).place(x=125, y=line7)
ttk.Button(text="test гардероб", width=12, command=person.pereodevanie).place(x=250, y=line7)
ttk.Button(text="frunze_bulvar", width=12, command=frunze_bulvar).place(x=0, y=line8)
ttk.Button(text="bulvar_frunze", width=12, command=bulvar_frunze).place(x=125, y=line8)
ttk.Button(text="тест tour", width=12, command=dvizh_test).place(x=250, y=line8)

ttk.Button(text="фото противника", width=17, command=create_img_arena_object).place(x=0, y=line10)
ttk.Button(text="атака противника", width=17, command=kill).place(x=205, y=line10)
# блок инфо строк
st_gady = 255  # столб инфо Гавр
st_gavr = st_gady + 41  # столб инфо Гадя
st_veles = st_gady + 82
st_item = st_gady - 39  # столб инфо
separator = st_gady + 26
separator_2 = st_veles - 14  # st_gavr + 26 + 43
ttk.Label(text="Gady", background='#858585', foreground='#050505').place(x=st_gady - 10, y=l_line0)
ttk.Label(text="Gavr", background='#858585', foreground='#050505').place(x=st_gavr - 9, y=l_line0)
ttk.Label(text="Велес", background='#858585', foreground='#050505').place(x=st_veles - 11, y=l_line0)
ttk.Label(text="VIP", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line1)
ttk.Label(textvariable=gady_vip).place(x=st_gady, y=l_line1)
ttk.Label(text='|').place(x=separator, y=l_line1)
ttk.Label(textvariable=gavr_vip).place(x=st_gavr, y=l_line1)
ttk.Label(text='|').place(x=separator_2, y=l_line1)
ttk.Label(textvariable=veles_vip).place(x=st_veles, y=l_line1)

ttk.Label(text="kiki", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line2)
ttk.Label(textvariable=gavr_kiki).place(x=st_gavr, y=l_line2)
ttk.Label(text='|').place(x=separator, y=l_line2)
ttk.Label(textvariable=gady_kiki).place(x=st_gady, y=l_line2)
ttk.Label(text='|').place(x=separator_2, y=l_line2)
ttk.Label(textvariable=veles_kiki).place(x=st_veles, y=l_line2)

ttk.Label(text="arah", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line3)
ttk.Label(textvariable=gavr_arachne).place(x=st_gavr, y=l_line3)
ttk.Label(text='|').place(x=separator, y=l_line3)
ttk.Label(textvariable=gady_arachne).place(x=st_gady, y=l_line3)
ttk.Label(text='|').place(x=separator_2, y=l_line3)
ttk.Label(textvariable=veles_arachne).place(x=st_veles, y=l_line3)

ttk.Label(text="rapt", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line4)
ttk.Label(textvariable=gavr_raptor).place(x=st_gavr, y=l_line4)
ttk.Label(text='|').place(x=separator, y=l_line4)
ttk.Label(textvariable=gady_raptor).place(x=st_gady, y=l_line4)
ttk.Label(text='|').place(x=separator_2, y=l_line4)
ttk.Label(textvariable=veles_raptor).place(x=st_veles, y=l_line4)

ttk.Label(text="rat", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line5)
ttk.Label(textvariable=gavr_rat).place(x=st_gavr, y=l_line5)
ttk.Label(text='|').place(x=separator, y=l_line5)
ttk.Label(textvariable=gady_rat).place(x=st_gady, y=l_line5)
ttk.Label(text='|').place(x=separator_2, y=l_line5)
ttk.Label(textvariable=veles_rat).place(x=st_veles, y=l_line5)

ttk.Label(text="gift", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line6)
ttk.Label(textvariable=gavr_gift).place(x=st_gavr, y=l_line6)
ttk.Label(text='|').place(x=separator, y=l_line6)
ttk.Label(textvariable=gady_gift).place(x=st_gady, y=l_line6)
ttk.Label(text='|').place(x=separator_2, y=l_line6)
ttk.Label(textvariable=veles_gift).place(x=st_veles, y=l_line6)

# блок выбора заданий
difference_str_img = 11
line_img = line1
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=station_master.vybor_zadaniya_na_puli).place(x=56, y=line_img + 15)
img_e1 = ImageTk.PhotoImage(file="img/overall/en1v3.png")
ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=line_img)
img_e2 = ImageTk.PhotoImage(file="img/overall/en2v3.png")
ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=line_img + height_line + difference_str_img)
img_e3 = ImageTk.PhotoImage(file="img/overall/en3v3.png")
ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=line_img + height_line * 2 + difference_str_img * 2)
#
root.mainloop()

# ttk.Button(text="most_riga", width=11, command=most_riga).place(x=109, y=277)  # x=133
# ttk.Button(text="riga_most", width=11, command=riga_most).place(x=109, y=308)
