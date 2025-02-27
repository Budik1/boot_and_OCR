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
from heroes import Hero, Activ

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

date_start = fun.date_utc_now()
# date_start = 1
# стартовые значения
starting_value = 0

'''
wildman_all
    при встрече увеличивается
    при загрузке считывается состояние из файла
    при записи сохраняется состояние
days_counting
'''


def displaying_values():
    gady_rat.set(her.gady.rat)
    gavr_rat.set(her.gavr.rat)
    mara_rat.set(her.mara.rat)
    veles_rat.set(her.veles.rat)

    gady_kiki.set(her.gady.kiki)
    gavr_kiki.set(her.gavr.kiki)
    mara_kiki.set(her.mara.kiki)
    veles_kiki.set(her.veles.kiki)

    gady_arachne.set(her.gady.arachne)
    gavr_arachne.set(her.gavr.arachne)
    mara_arachne.set(her.mara.arachne)
    veles_arachne.set(her.veles.arachne)

    gady_raptor.set(her.gady.raptor)
    gavr_raptor.set(her.gavr.raptor)
    mara_raptor.set(her.mara.raptor)
    veles_raptor.set(her.veles.raptor)

    gady_gift.set(her.gady.gifts)
    gavr_gift.set(her.gavr.gifts)
    mara_gift.set(her.mara.gifts)
    veles_gift.set(her.veles.gifts)

    gady_wild.set(her.gady.wildman)
    gavr_wild.set(her.gavr.wildman)


def check_date(loaded_data):
    """Установка значений при (пере)запуске программы"""
    date_ver = loaded_data['date']
    # date_ver = 0

    her.gady.wildman_count = loaded_data['gady.wildman_all']
    her.gavr.wildman_count = loaded_data['gavr.wildman_all']

    her.gady.days_count = loaded_data['gady.days_counting']
    her.gavr.days_count = loaded_data['gavr.days_counting']
    # her.gavr.days_counting += 1

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

        her.gavr.wildman = loaded_data['gavr_wild']
        her.gady.wildman = loaded_data['gady_wild']
        her.mara.wildman = loaded_data['mara_wild']
        her.veles.wildman = loaded_data['veles_wild']

        # отображаем значения
        gavr_vip.set(her.gavr.vip)
        gady_vip.set(her.gady.vip)
        mara_vip.set(her.mara.vip)
        veles_vip.set(her.veles.vip)

        displaying_values()
    # иначе отображение и сохранение стартовых значений
    else:

        her.gady.days_count +=1
        # her.gady.days_counting = 0
        her.gavr.days_count +=1
        # her.gavr.days_counting = 0
        print(f"gady {her.gady.days_count} дней, {her.gady.wildman_count} дикарей")
        print(f'gavr {her.gavr.days_count} дней, {her.gavr.wildman_count} дикарей')

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

        'gavr_wild': her.gavr.wildman,
        'gady_wild': her.gady.wildman,
        'mara_wild': her.mara.wildman,
        'veles_wild': her.veles.wildman,

        'gady.wildman_all': her.gady.wildman_count,
        'gavr.wildman_all': her.gavr.wildman_count,

        'gady.days_counting': her.gady.days_count,
        'gavr.days_counting': her.gavr.days_count,

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
    displaying_values()
    save_to_file()


def en_2():
    station_master.en_task_item(2)
    displaying_values()
    save_to_file()


def en_3():
    station_master.en_task_item(3)
    displaying_values()
    save_to_file()


def puli():
    station_master.vybor_zadaniya_na_puli()
    displaying_values()
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
    vip_case_all = 0
    it_revision = 0
    fun.move_friends_list_to_top()

    while vip_case_all < 10:
        if hero == 'Gady':
            vip_case_all += revision_of_tents.tent_raid()
            her.gady.vip = vip_case_all
            gady_vip.set(str(her.gady.vip))
        if hero == 'Gavr':
            vip_case_all += revision_of_tents.tent_raid()
            her.gavr.vip = vip_case_all
            gavr_vip.set(str(her.gavr.vip))
        if hero == 'Mara':
            vip_case_all += revision_of_tents.tent_raid()
            her.mara.vip = vip_case_all
            mara_vip.set(her.mara.vip)
        if hero == 'Велес':
            vip_case_all += revision_of_tents.tent_raid()
            her.veles.vip = vip_case_all
            veles_vip.set(her.veles.vip)
        it_revision += 1
        print(f'{vip_case_all} из {it_revision} осмотренных')
        fun.move_friends_list_left()
        if it_revision == 12:
            vip_case_all = 10
            if hero == 'Gady':
                her.gady.vip = vip_case_all
                gady_vip.set(str(her.gady.vip))
            if hero == 'Gavr':
                her.gavr.vip = vip_case_all
                gavr_vip.set(str(her.gavr.vip))
            if hero == 'Mara':
                her.mara.vip = vip_case_all
                mara_vip.set(her.mara.vip)
            if hero == 'Велес':
                her.veles.vip = vip_case_all
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
    if hero:
        bypass_hero = Hero.get_bypass(Activ.hero_activ)
    # if hero == 'Велес':
    #     bypass_hero = b_d.bypass_veles
    # elif hero == 'Mara':
    #     bypass_hero = b_d.bypass_mara
    # elif hero == 'Gady':
    #     bypass_hero = b_d.bypass
    # elif hero == 'Gavr':
    #     bypass_hero = b_d.bypass
    else:
        print('герой не опознан')
        return
    # движение по маршруту
    touring.sbor_podarkov(bypass_hero)
    # получение количества станций на маршруте
    q_st = fun.get_len_bypass(bypass_hero)
    # получение количества собранных подарков
    if hero:
        q_gifts = Hero.get_qty_gift(Activ.hero_activ)
    # if hero == 'Велес':
    #     q_gifts = her.veles.gifts
    # elif hero == 'Mara':
    #     q_gifts = her.mara.gifts
    # elif hero == 'Gady':
    #     q_gifts = her.gady.gifts
    # elif hero == 'Gavr':
    #     q_gifts = her.gavr.gifts
    else:
        print('герой не опознан')
        return

    # вывод информации
    print(f'На {q_st} станциях собрано {q_gifts} подарков')

    displaying_values()
    save_to_file()


root = Tk()

root.title(' помощник "Метро 2033"')
root.geometry("370x362+1200+50")  # Ширина x Высота + координата X + координата Y
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

gavr_wild = IntVar()
gady_wild = IntVar()
mara_wild = IntVar()
veles_wild = IntVar()

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
line11 = height_line * 11
line12 = height_line * 12
line13 = height_line * 13
line14 = height_line * 14
line15 = height_line * 15
line16 = height_line * 16
line17 = height_line * 17
line18 = height_line * 18
line19 = height_line * 19

label_shift = 3  # смещение строки для Label
label_line0 = line0 + label_shift
label_line1 = line1 + label_shift
label_line2 = line2 + label_shift
label_line3 = line3 + label_shift
label_line4 = line4 + label_shift
label_line5 = line5 + label_shift
label_line6 = line6 + label_shift
label_line7 = line7 + label_shift
label_line8 = line8 + label_shift
label_line9 = line9 + label_shift
label_line10 = line10 + label_shift

# блок командных кнопок
ttk.Button(text="КВ", width=8, command=kv_and_raid.kv).place(x=114, y=line5)
ttk.Button(text=" Start ", width=14, command=fun.start_p_m).place(x=200, y=line5)
ttk.Button(text="за дикарями", width=10, command=tasks_na_kievskoy).place(x=114, y=line6)
ttk.Button(text="на Киев", width=7, command=frunze_kiev).place(x=215, y=line6)
ttk.Button(text="домой ", width=7, command=kiev_frunze).place(x=291, y=line6)
ttk.Button(text="Паук+Ящер", width=10, command=arachne_and_raptor).place(x=267, y=line7)
ttk.Button(text="обход всех станций", width=16, command=collecting_gifts_at_stations).place(x=114, y=line7)
ttk.Button(text='Save', width=12, command=save_to_file).place(x=125, y=line8)
ttk.Button(text="frunze_riga", width=12, command=frunze_riga).place(x=0, y=line9)
ttk.Button(text="riga_frunze", width=12, command=riga_frunze).place(x=125, y=line9)
ttk.Button(text="test гардероб", width=12, command=person.pereodevanie).place(x=250, y=line9)
ttk.Button(text="frunze_bulvar", width=12, command=frunze_bulvar).place(x=0, y=line10)
ttk.Button(text="bulvar_frunze", width=12, command=bulvar_frunze).place(x=125, y=line10)
ttk.Button(text="тест tour", width=12, command=dvizh_test).place(x=250, y=line10)

ttk.Button(text="фото противника", width=17, command=create_img_arena_object).place(x=0, y=line11)
ttk.Button(text="атака противника", width=17, command=kill).place(x=205, y=line11)
# блок инфо строк
gady_y = label_line1
gavr_y = label_line2
veles_y = label_line3
mara_y = label_line4

step = 47
s = 14
g_st0 = 0
vip_x = step + s
kiki_x = step * 2 + s
arah_x = step * 3 + s
rapt_x = step * 4 + s
rat_x = step * 5 + s
gift_x = step * 6 + s
wild_x = step * 7 + s

separator_1 = kiki_x - 18
separator_2 = arah_x - 18
separator_3 = rapt_x - 18
separator_4 = rat_x - 18
separator_5 = gift_x - 18
separator_6 = wild_x - 18

ttk.Label(text="Gady", width=5, background='#858585', foreground='#050505').place(x=0, y=gady_y)
ttk.Label(text="Gavr", width=5, background='#858585', foreground='#050505').place(x=0, y=gavr_y)
ttk.Label(text="Велес", width=5, background='#858585', foreground='#050505').place(x=0, y=veles_y)
ttk.Label(text="Мара", width=5, background='#858585', foreground='#050505').place(x=0, y=mara_y)

# ttk.Button(text=" обход VIP ", width=10, command=tent_inspection).place(x=114, y=line10)
ttk.Button(text="VIP", width=4, command=tent_inspection).place(x=vip_x - s, y=label_line0 - 3)
ttk.Label(textvariable=gady_vip).place(x=vip_x, y=gady_y)
ttk.Label(textvariable=gavr_vip).place(x=vip_x, y=gavr_y)
ttk.Label(textvariable=veles_vip).place(x=vip_x, y=veles_y)
ttk.Label(textvariable=mara_vip).place(x=vip_x, y=mara_y)
ttk.Label(text='|').place(x=separator_1, y=gady_y)
ttk.Label(text='|').place(x=separator_1, y=gavr_y)
ttk.Label(text='|').place(x=separator_1, y=veles_y)
ttk.Label(text='|').place(x=separator_1, y=mara_y)

# ttk.Button(text="кикиморы", width=10, command=kiki).place(x=114, y=line11)
ttk.Button(text="kiki", width=4, command=kiki).place(x=kiki_x - s, y=label_line0 - 3)
ttk.Label(textvariable=gavr_kiki).place(x=kiki_x, y=gavr_y)
ttk.Label(textvariable=gady_kiki).place(x=kiki_x, y=gady_y)
ttk.Label(textvariable=veles_kiki).place(x=kiki_x, y=veles_y)
ttk.Label(textvariable=mara_kiki).place(x=kiki_x, y=mara_y)
ttk.Label(text='|').place(x=separator_2, y=gady_y)
ttk.Label(text='|').place(x=separator_2, y=gavr_y)
ttk.Label(text='|').place(x=separator_2, y=veles_y)
ttk.Label(text='|').place(x=separator_2, y=mara_y)

ttk.Label(text="arah", width=4, background='#858585', foreground='#050505').place(x=arah_x - s, y=label_line0)
ttk.Label(textvariable=gavr_arachne).place(x=arah_x, y=gavr_y)
ttk.Label(textvariable=gady_arachne).place(x=arah_x, y=gady_y)
ttk.Label(textvariable=veles_arachne).place(x=arah_x, y=veles_y)
ttk.Label(textvariable=mara_arachne).place(x=arah_x, y=mara_y)
ttk.Label(text='|').place(x=separator_3, y=gady_y)
ttk.Label(text='|').place(x=separator_3, y=gavr_y)
ttk.Label(text='|').place(x=separator_3, y=veles_y)
ttk.Label(text='|').place(x=separator_3, y=mara_y)

ttk.Label(text="rapt", width=4, background='#858585', foreground='#050505').place(x=rapt_x - s, y=label_line0)
ttk.Label(textvariable=gavr_raptor).place(x=rapt_x, y=gavr_y)
ttk.Label(textvariable=gady_raptor).place(x=rapt_x, y=gady_y)
ttk.Label(textvariable=veles_raptor).place(x=rapt_x, y=veles_y)
ttk.Label(textvariable=mara_raptor).place(x=rapt_x, y=mara_y)
ttk.Label(text='|').place(x=separator_4, y=gady_y)
ttk.Label(text='|').place(x=separator_4, y=gavr_y)
ttk.Label(text='|').place(x=separator_4, y=veles_y)
ttk.Label(text='|').place(x=separator_4, y=mara_y)

ttk.Label(text="rat", width=4, background='#858585', foreground='#050505').place(x=rat_x - s, y=label_line0)
ttk.Label(textvariable=gavr_rat).place(x=rat_x, y=gavr_y)
ttk.Label(textvariable=gady_rat).place(x=rat_x, y=gady_y)
ttk.Label(textvariable=veles_rat).place(x=rat_x, y=veles_y)
ttk.Label(textvariable=mara_rat).place(x=rat_x, y=mara_y)
ttk.Label(text='|').place(x=separator_5, y=gady_y)
ttk.Label(text='|').place(x=separator_5, y=gavr_y)
ttk.Label(text='|').place(x=separator_5, y=veles_y)
ttk.Label(text='|').place(x=separator_5, y=mara_y)

ttk.Label(text="gift", width=4, background='#858585', foreground='#050505').place(x=gift_x - s, y=label_line0)
ttk.Label(textvariable=gavr_gift).place(x=gift_x, y=gavr_y)
ttk.Label(textvariable=gady_gift).place(x=gift_x, y=gady_y)
ttk.Label(textvariable=veles_gift).place(x=gift_x, y=veles_y)
ttk.Label(textvariable=mara_gift).place(x=gift_x, y=mara_y)
ttk.Label(text='|').place(x=separator_6, y=gady_y)
ttk.Label(text='|').place(x=separator_6, y=gavr_y)
ttk.Label(text='|').place(x=separator_6, y=veles_y)
ttk.Label(text='|').place(x=separator_6, y=mara_y)

ttk.Label(text="wild", width=4, background='#858585', foreground='#050505').place(x=wild_x - s, y=label_line0)
ttk.Label(textvariable=gavr_wild).place(x=wild_x, y=gavr_y)
ttk.Label(textvariable=gady_wild).place(x=wild_x, y=gady_y)
ttk.Label(textvariable=veles_wild).place(x=wild_x, y=veles_y)
ttk.Label(textvariable=mara_wild).place(x=wild_x, y=mara_y)

# блок выбора заданий
difference_str_img = 11
line_img = line5 + 1
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=puli).place(x=56, y=line_img + 15)
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
