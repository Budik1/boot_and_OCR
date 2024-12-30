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

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

date_start = fun.date_utc_now()
# стартовые значения
starting_value = '0'

gavr_sum_vip = 0
gady_sum_vip = 0


def displaying_values():
    gady_rat.set(touring.gady_rat_q)
    gady_kiki.set(touring.gady_kiki_q)
    gady_arachne.set(touring.gady_arachne_q)
    gady_raptor.set(touring.gady_raptor_q)
    gady_gift.set(touring.gady_gifts_q)

    gavr_rat.set(touring.gavr_rat_q)
    gavr_kiki.set(touring.gavr_kiki_q)
    gavr_arachne.set(touring.gavr_arachne_q)
    gavr_raptor.set(touring.gavr_raptor_q)
    gavr_gift.set(touring.gavr_gifts_q)


def check_date(loaded_data):
    """Установка значений при (пере)запуске программы"""
    global gavr_sum_vip, gady_sum_vip
    date_ver = loaded_data['date']
    # если даты совпадают:- значения устанавливаются из файла
    if date_ver == date_start:
        print(tc_blue("даты совпадают"))
        # присваиваем значения
        gavr_sum_vip = loaded_data['gavr_vip']
        gady_sum_vip = loaded_data['gady_vip']

        touring.gavr_rat_q = loaded_data['gavr_krysy']
        touring.gady_rat_q = loaded_data['gady_krysy']

        touring.gavr_kiki_q = loaded_data['gavr_kiki']
        touring.gady_kiki_q = loaded_data['gady_kiki']

        touring.gavr_arachne_q = loaded_data['gavr_arachne']
        touring.gady_arachne_q = loaded_data['gady_arachne']

        touring.gavr_raptor_q = loaded_data['gavr_raptor']
        touring.gady_raptor_q = loaded_data['gady_raptor']

        touring.gavr_gifts_q = loaded_data['gavr_gifts']
        touring.gady_gifts_q = loaded_data['gady_gifts']
        # отображаем значения
        gavr_vip.set(gavr_sum_vip)
        gady_vip.set(gady_sum_vip)

        displaying_values()
    # иначе отображение и сохранение стартовых значений
    else:

        print(tc_cyan("даты не совпадают, смена суток"))
        gavr_vip.set(starting_value)
        gady_vip.set(starting_value)

        displaying_values()
        save_to_file()


def save_to_file():
    print(tc_green("запись состояния"))

    data_to_save = {
        'date': date_start,
        'gavr_vip': gavr_sum_vip,
        'gady_vip': gady_sum_vip,

        'gavr_krysy': touring.gavr_rat_q,
        'gady_krysy': touring.gady_rat_q,

        'gavr_kiki': touring.gavr_kiki_q,
        'gady_kiki': touring.gady_kiki_q,

        'gavr_arachne': touring.gavr_arachne_q,
        'gady_arachne': touring.gady_arachne_q,

        'gavr_raptor': touring.gavr_raptor_q,
        'gady_raptor': touring.gady_raptor_q,

        'gavr_gifts': touring.gavr_gifts_q,
        'gady_gifts': touring.gady_gifts_q,
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
        # print(data_to_load)
        check_date(data_to_load)
        # save_to_file()
    except:
        print(tc_red("файл поврежден или не создан"))
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
    global gady_sum_vip, gavr_sum_vip

    def vip():
        fun.move_friends_list_to_top()
        vip_q = revision_of_tents.tent_raid()
        it = 1
        print(f'{vip_q} / {it}')
        while it < 11:
            it += 1
            fun.move_friends_list_left()
            vip_q += revision_of_tents.tent_raid()
            print(f'{vip_q} / {it}')
        revision_of_tents.end_raid()
        return vip_q

    hero = fun.selection_hero()
    if hero == 'Gady':
        gady_sum_vip = vip()
        gady_vip.set(gady_sum_vip)
    if hero == 'Gavr':
        gavr_sum_vip = vip()
        gavr_vip.set(gavr_sum_vip)
    if hero == 'Велес':
        veles_sum_vip = vip()
    save_to_file()


def frunze_kiev():
    hero = fun.selection_hero()
    if hero == "Gady":
        touring.frunze_kiev()
    if hero == "Gavr":
        touring.frunze_kiev()
    displaying_values()
    save_to_file()


def kiev_frunze():
    hero = fun.selection_hero()
    if hero == "Gady":
        touring.kiev_frunze()
    if hero == "Gavr":
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
    touring.sbor_podarkov()
    displaying_values()
    save_to_file()


root = Tk()

root.title(' помощник "Метро 2033"')
root.geometry("328x332+1240+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

gavr_vip = StringVar()
gady_vip = StringVar()

gavr_rat = StringVar()
gady_rat = StringVar()

gavr_kiki = StringVar()
gady_kiki = StringVar()

gavr_arachne = StringVar()
gady_arachne = StringVar()

gavr_raptor = StringVar()
gady_raptor = StringVar()

gavr_gift = StringVar()
gady_gift = StringVar()

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
ttk.Button(text=" Start ", width=13, command=fun.start_p_m).place(x=60, y=line0)
ttk.Button(text=" обход VIP ", width=10, command=tent_inspection).place(x=114, y=line1)
ttk.Button(text="кикиморы", width=10, command=kiki).place(x=114, y=line2)
ttk.Button(text="Паук+Ящер", width=10, command=arachne_and_raptor).place(x=114, y=line3)
ttk.Button(text="за дикарями", width=10, command=tasks_na_kievskoy).place(x=114, y=line4)
ttk.Button(text="обход всех станций", width=16, command=collecting_gifts_at_stations).place(x=0, y=line6)
ttk.Button(text="КВ", width=4, command=kv_and_raid.kv).place(x=0, y=line5)
ttk.Button(text="на Киев", width=8, command=frunze_kiev).place(x=50, y=line5)
ttk.Button(text="домой ", width=8, command=kiev_frunze).place(x=132, y=line5)
ttk.Button(text="frunze_riga", width=10, command=frunze_riga).place(x=0, y=line7)
ttk.Button(text="riga_frunze", width=10, command=riga_frunze).place(x=109, y=line7)
ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=218, y=line7)
ttk.Button(text="bulvar_frunze", width=11, command=bulvar_frunze).place(x=218, y=line8)
ttk.Button(text="тест tour", width=8, command=dvizh_test).place(x=122, y=line8)
ttk.Button(text="frunze_bulvar", width=11, command=frunze_bulvar).place(x=0, y=line8)

ttk.Button(text="фото противника", width=16, command=create_img_arena_object).place(x=0, y=line10)
ttk.Button(text="атака противника", width=16, command=kill).place(x=170, y=line10)
# блок инфо строк
st_gavr = 255  # столб инфо Гавр
st_gady = st_gavr + 40  # столб инфо Гадя
st_item = st_gavr - 38  # столб инфо
separator = st_gavr + 26
ttk.Label(text="Gavr", background='#858585', foreground='#050505').place(x=st_gavr - 10, y=l_line0)
ttk.Label(text="Gady", background='#858585', foreground='#050505').place(x=st_gady - 10, y=l_line0)
ttk.Label(text="VIP", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line1)
ttk.Label(textvariable=gavr_vip).place(x=st_gavr, y=l_line1)
ttk.Label(text='|').place(x=separator, y=l_line1)
ttk.Label(textvariable=gady_vip).place(x=st_gady, y=l_line1)
ttk.Label(text="kiki", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line2)
ttk.Label(textvariable=gavr_kiki).place(x=st_gavr, y=l_line2)
ttk.Label(text='|').place(x=separator, y=l_line2)
ttk.Label(textvariable=gady_kiki).place(x=st_gady, y=l_line2)
ttk.Label(text="arah", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line3)
ttk.Label(textvariable=gavr_arachne).place(x=st_gavr, y=l_line3)
ttk.Label(text='|').place(x=separator, y=l_line3)
ttk.Label(textvariable=gady_arachne).place(x=st_gady, y=l_line3)
ttk.Label(text="rapt", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line4)
ttk.Label(textvariable=gavr_raptor).place(x=st_gavr, y=l_line4)
ttk.Label(text='|').place(x=separator, y=l_line4)
ttk.Label(textvariable=gady_raptor).place(x=st_gady, y=l_line4)
ttk.Label(text="rat", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line5)
ttk.Label(textvariable=gavr_rat).place(x=st_gavr, y=l_line5)
ttk.Label(text='|').place(x=separator, y=l_line5)
ttk.Label(textvariable=gady_rat).place(x=st_gady, y=l_line5)
ttk.Label(text="gift", width=4, background='#858585', foreground='#050505').place(x=st_item, y=l_line6)
ttk.Label(textvariable=gavr_gift).place(x=st_gavr, y=l_line6)
ttk.Label(text='|').place(x=separator, y=l_line6)
ttk.Label(textvariable=gady_gift).place(x=st_gady, y=l_line6)

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
