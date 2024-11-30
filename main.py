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
status_bonus = "0"

gavr_sum_vip = 0
gady_sum_vip = 0

gavr_sum_kiki = 0
gady_sum_kiki = 0

gavr_sum_rat = 0
gady_sum_rat = 0

gavr_sum_arachne = 0
gady_sum_arachne = 0

gavr_sum_raptor = 0
gady_sum_raptor = 0


def transform(gady_entity, gavr_entity):
    gady_sum_rat, gady_sum_kiki, gady_sum_arachne, gady_sum_raptor, gady_number_of_gifts = gady_entity
    gavr_sum_rat, gavr_sum_kiki, gavr_sum_arachne, gavr_sum_raptor, gavr_number_of_gifts = gavr_entity

    gady_rat.set(gady_sum_rat)
    gady_kiki.set(gady_sum_kiki)
    gady_arachne.set(gady_sum_arachne)
    gady_raptor.set(gady_sum_raptor)

    gavr_rat.set(gavr_sum_rat)
    gavr_kiki.set(gavr_sum_kiki)
    gavr_arachne.set(gavr_sum_arachne)
    gavr_raptor.set(gavr_sum_raptor)


def check_date(loaded_data):
    global gavr_sum_vip, gavr_sum_rat, gavr_sum_kiki, gavr_sum_arachne, gavr_sum_raptor
    global gady_sum_vip, gady_sum_rat, gady_sum_kiki, gady_sum_arachne, gady_sum_raptor

    date_ver = loaded_data['date']
    if date_ver == date_start:
        print(tc_blue("даты совпадают"))

        gavr_sum_vip = loaded_data['gavr_vip']
        gady_sum_vip = loaded_data['gady_vip']

        gavr_sum_rat = loaded_data['gavr_krysy']
        gady_sum_rat = loaded_data['gady_krysy']

        gavr_sum_kiki = loaded_data['gavr_kiki']
        gady_sum_kiki = loaded_data['gady_kiki']

        gavr_sum_arachne = loaded_data['gavr_arachne']
        gady_sum_arachne = loaded_data['gady_arachne']

        gavr_sum_raptor = loaded_data['gavr_raptor']
        gady_sum_raptor = loaded_data['gady_raptor']

        gavr_vip.set(gavr_sum_vip)
        gady_vip.set(gady_sum_vip)
        gavr_rat.set(gavr_sum_rat)
        gady_rat.set(gady_sum_rat)
        gavr_kiki.set(gavr_sum_kiki)
        gady_kiki.set(gady_sum_kiki)
        gavr_arachne.set(gavr_sum_arachne)
        gady_arachne.set(gady_sum_arachne)
        gavr_raptor.set(gavr_sum_raptor)
        gady_raptor.set(gady_sum_raptor)

    else:
        print(tc_cyan("даты не совпадают, смена суток"))
        gavr_vip.set(gavr_sum_vip)
        gady_vip.set(gady_sum_vip)
        save_to_file()


def save_to_file():
    print(tc_green("запись состояния"))
    # global date_start, gavr_sum_vip, gavr_sum_rat, gavr_sum_kiki, gavr_sum_arachne, gavr_sum_raptor

    data_to_save = {
        'date': date_start,
        'gavr_vip': gavr_sum_vip,
        'gady_vip': gady_sum_vip,

        'gavr_krysy': gavr_sum_rat,
        'gady_krysy': gavr_sum_rat,

        'gavr_kiki': gavr_sum_kiki,
        'gady_kiki': gady_sum_kiki,

        'gavr_arachne': gavr_sum_arachne,
        'gady_arachne': gady_sum_arachne,

        'gavr_raptor': gavr_sum_raptor,
        'gady_raptor': gady_sum_raptor,
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
    rezult_gady, rezult_gavr = touring.frunze_kiev()
    rezult_gady, rezult_gavr = touring.kiev_frunze()

    transform(rezult_gady, rezult_gavr)
    save_to_file()


def kiki():

    touring.za_kikimorami()
    # transform()
    save_to_file()


def arachne_and_raptor():
    rezult_gady, rezult_gavr = touring.pauk_yascher()

    transform(rezult_gady, rezult_gavr)
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
            # gavr_vip.set(gavr_sum_vip)
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
    # transform()
    save_to_file()


def kiev_frunze():
    hero = fun.selection_hero()
    if hero == "Gady":
        touring.kiev_frunze()
    if hero == "Gavr":
        touring.kiev_frunze()
    # transform()
    save_to_file()


def most_frunze():
    touring.most_frunze()
    # transform()
    save_to_file()


def frunze_most():
    touring.frunze_most()
    # transform()
    save_to_file()


def bulvar_frunze():
    touring.bulvar_frunze()
    # transform()
    save_to_file()


def frunze_bulvar():
    touring.frunze_bulvar()
    # transform()
    save_to_file()


def most_riga():
    touring.most_riga()
    # transform()
    save_to_file()


def riga_most():
    touring.riga_most()
    # transform()
    save_to_file()


def frunze_riga():
    touring.frunze_riga()
    # transform()
    save_to_file()


def riga_frunze():
    touring.riga_frunze()
    # transform()
    save_to_file()


def tasks_na_kievskoy():
    touring.tasks_na_kievskoy()
    # transform()
    save_to_file()


def sbor_podarkov():
    touring.sbor_podarkov()
    # transform()
    save_to_file()


root = Tk()

root.title(' помощник "Метро 2033"')
root.geometry("327x411+1240+50")  # Ширина x Высота + координата X + координата Y
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

read_from_file()

line0 = 0
line1 = 32
line2 = 64
line3 = 96
line4 = 128
line5 = 160

# шаг 31
ttk.Button(text=" Start ", width=13, command=fun.start_p_m).place(x=190, y=line0)
# ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus, state="disabled").place(x=0, y=line1)
# ttk.Label(text=status_bonus, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=130, y=line1)
# ttk.Button(text="  сбор подарков  ", width=13, command=fun.station_gifts, state="disabled").place(x=0, y=line2)
#
ttk.Button(text=" обход VIP ", width=13, command=tent_inspection).place(x=0, y=line1)
ttk.Label(textvariable=gavr_vip).place(x=130, y=line1)
ttk.Label(text='|').place(x=150, y=line1)
ttk.Label(textvariable=gady_vip).place(x=160, y=line1)
#
#
ttk.Button(text="кикиморы", width=13, command=kiki).place(x=0, y=line0)
ttk.Label(textvariable=gavr_kiki).place(x=130, y=line0)
ttk.Label(text='|').place(x=150, y=line0)
ttk.Label(textvariable=gady_kiki).place(x=160, y=line0)
#
ttk.Button(text="Паук + Ящер", width=13, command=arachne_and_raptor).place(x=0, y=line2)

ttk.Label(textvariable=gavr_arachne).place(x=0, y=line3)
ttk.Label(text='|').place(x=20, y=line3)
ttk.Label(textvariable=gavr_raptor).place(x=30, y=line3)

ttk.Label(textvariable=gady_arachne).place(x=65, y=line3)
ttk.Label(text='|').place(x=85, y=line3)
ttk.Label(textvariable=gady_raptor).place(x=95, y=line3)
#
#
#

# тест пробежка
ttk.Button(text="тест пробежка", width=13, command=dvizh_test).place(x=190, y=line1)
ttk.Label(textvariable=gavr_rat).place(x=230, y=line2)
ttk.Label(textvariable=gady_rat).place(x=280, y=line2)

ttk.Button(text="обход всех станций", width=16, command=sbor_podarkov).place(x=153, y=246)
# блок выбора заданий
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=station_master.vybor_zadaniya_na_puli).place(x=60, y=145)
#
img_e1 = ImageTk.PhotoImage(file="img/overall/en1v3.png")
ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=128)
#
img_e2 = ImageTk.PhotoImage(file="img/overall/en2v3.png")
ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=168)
#
img_e3 = ImageTk.PhotoImage(file="img/overall/en3v3.png")
ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=208)
#                                                                                               #
ttk.Button(text="КВ", width=5, command=kv_and_raid.kv).place(x=0, y=246)
##
ttk.Button(text="на Киев", width=8, command=frunze_kiev).place(x=0, y=277)  #
ttk.Button(text="задания на Киевской", width=17, command=tasks_na_kievskoy).place(x=82, y=277)  #
ttk.Button(text="домой ", width=8, command=kiev_frunze).place(x=244, y=277)  #
#                                                                                               #
ttk.Button(text="frunze_riga", width=10, command=frunze_riga).place(x=0, y=308)  #
ttk.Button(text="riga_frunze", width=10, command=riga_frunze).place(x=105, y=308)  #
ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=210, y=308)  #
#
ttk.Button(text="фото противника", width=16, command=create_img_arena_object).place(x=0, y=377)
ttk.Button(text="атака противника", width=16, command=kill).place(x=170, y=377)

ttk.Button(text="bulvar_frunze", width=11, command=bulvar_frunze).place(x=0, y=339)
ttk.Button(text="frunze_bulvar", width=11, command=frunze_bulvar).place(x=218, y=339)

root.mainloop()

# ttk.Button(text="most_riga", width=11, command=most_riga).place(x=109, y=277)  # x=133
# ttk.Button(text="riga_most", width=11, command=riga_most).place(x=109, y=308)
