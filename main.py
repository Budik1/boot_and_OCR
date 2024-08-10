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
from my_text_color import text_green, text_cyan, text_blue, text_red

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

sum_vip = 0
status_bonus = "0"
date_start = fun.date_utc_now()
sum_kiki = touring.kiki_q
sum_rat = touring.rat_q
sum_arachne = touring.arachne_q
sum_raptor = touring.raptor_q


def transform():
    global sum_vip, sum_rat, sum_kiki, sum_arachne, sum_raptor

    sum_rat = touring.rat_q
    sum_kiki = touring.kiki_q
    sum_arachne = touring.arachne_q
    sum_raptor = touring.raptor_q

    status_rat.set(sum_rat)
    status_kiki.set(sum_kiki)
    status_arachne.set(sum_arachne)
    status_raptor.set(sum_raptor)


def check_date(loaded_data):
    global sum_vip, sum_rat, sum_kiki, sum_arachne, sum_raptor

    date_ver = loaded_data['date']
    if date_ver == date_start:
        print(text_blue("даты совпадают"))

        sum_vip = loaded_data['vip']
        sum_rat = loaded_data['krysy']
        sum_kiki = loaded_data['kiki']
        sum_arachne = loaded_data['arachne']
        sum_raptor = loaded_data['raptor']

        status_vip.set(sum_vip)
        status_rat.set(sum_rat)
        status_kiki.set(sum_kiki)
        status_arachne.set(sum_arachne)
        status_raptor.set(sum_raptor)

        touring.rat_q = sum_rat
        touring.kiki_q = sum_kiki
        touring.arachne_q = sum_arachne
        touring.raptor_q = sum_raptor

    else:
        print(text_cyan("даты не совпадают, смена суток"))
        status_vip.set(sum_vip)
        # sum_rat = touring.rat_q
        # sum_kiki = touring.kiki_q
        # sum_arachne = touring.arachne_q
        # sum_raptor = touring.raptor_q
        #
        # status_rat.set(sum_rat)
        # status_kiki.set(sum_kiki)
        # status_arachne.set(sum_arachne)
        # status_raptor.set(sum_raptor)
        save_to_file()


def save_to_file():
    print(text_green("запись состояния"))
    global date_start, sum_vip, sum_rat, sum_kiki, sum_arachne, sum_raptor

    sum_rat = touring.rat_q
    sum_kiki = touring.kiki_q
    sum_arachne = touring.arachne_q
    sum_raptor = touring.raptor_q

    status_rat.set(sum_rat)
    status_kiki.set(sum_kiki)
    status_arachne.set(sum_arachne)
    status_raptor.set(sum_raptor)

    data_to_save = {
        'date': date_start,
        'vip': sum_vip,
        'krysy': sum_rat,
        'kiki': sum_kiki,
        'arachne': sum_arachne,
        'raptor': sum_raptor,
    }
    print(data_to_save)
    file1 = open('config.bin', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    print(text_green("чтение состояния"))
    try:
        file1 = open('config.bin', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        print(data_to_load)

        check_date(data_to_load)

    except:
        print(text_red("файл поврежден или не создан"))
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
    touring.test()
    # transform()
    save_to_file()


def kiki():
    touring.za_kikimorami()
    # transform()
    save_to_file()


def arachne_and_raptor():
    touring.pauk_yascher()
    # transform()
    save_to_file()


def tent_inspection():
    def vip():
        global sum_vip
        fun.move_friends_list_to_top()
        sum_vip = revision_of_tents.tent_raid()
        it = 1
        print(f'{sum_vip} / {it}')
        while it < 11:
            it += 1
            fun.move_friends_list_left()
            sum_vip += revision_of_tents.tent_raid()
            print(f'{sum_vip} / {it}')
            status_vip.set(sum_vip)
        revision_of_tents.end_raid()

    vip()
    save_to_file()


def frunze_kiev():
    touring.frunze_kiev()
    # transform()
    save_to_file()


def kiev_most():
    touring.kiev_most()
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
root.geometry("327x380+1240+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

status_vip = StringVar()
status_rat = StringVar()
status_kiki = StringVar()
status_arachne = StringVar()
status_raptor = StringVar()

read_from_file()

# шаг 31
ttk.Button(text=" Start ", width=13, command=fun.start_p_m).place(x=0, y=0)
ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus, state="disabled").place(x=0, y=32)
ttk.Label(text=status_bonus, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=130, y=32)
ttk.Button(text="  сбор подарков  ", width=13, command=fun.station_gifts, state="disabled").place(x=0, y=64)
#
ttk.Button(text=" обход VIP ", width=13, command=tent_inspection).place(x=0, y=96)
ttk.Label(textvariable=status_vip).place(x=130, y=96)
#
ttk.Button(text="(f)на Киев", width=11, command=frunze_kiev).place(x=120, y=169)
ttk.Button(text="(k)домой(m) ", width=11, command=kiev_most).place(x=120, y=200)
#
ttk.Button(text="кикиморы", width=11, command=kiki).place(x=153, y=31)
ttk.Label(textvariable=status_kiki).place(x=285, y=31)
#
ttk.Button(text="Паук + Ящер", width=11, command=arachne_and_raptor).place(x=153, y=0)
ttk.Label(textvariable=status_arachne).place(x=262, y=0)
ttk.Label(text='/').place(x=282, y=0)
ttk.Label(textvariable=status_raptor).place(x=292, y=0)
#

ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=109, y=245)

ttk.Button(text="most_frunze", width=11, command=most_frunze).place(x=218, y=277)
ttk.Button(text="frunze_most", width=11, command=frunze_most).place(x=218, y=308)

ttk.Button(text="most_riga", width=11, command=most_riga).place(x=109, y=277)  # x=133
ttk.Button(text="riga_most", width=11, command=riga_most).place(x=109, y=308)

ttk.Button(text="frunze_riga", width=11, command=frunze_riga).place(x=0, y=277)
ttk.Button(text="riga_frunze", width=11, command=riga_frunze).place(x=0, y=308)

ttk.Button(text="задания на Киевской", width=17, command=tasks_na_kievskoy).place(x=120, y=138)
# тест пробежка
ttk.Button(text="тест пробежка", width=13, command=dvizh_test).place(x=153, y=64)
ttk.Label(textvariable=status_rat).place(x=285, y=64)

ttk.Button(text="обход всех станций", width=16, command=sbor_podarkov).place(x=153, y=96)

imagePul = ImageTk.PhotoImage(file="img/pulya.png")
ttk.Button(root, image=imagePul, command=station_master.vybor_zadaniya_na_puli).place(x=60, y=145)

img_e1 = ImageTk.PhotoImage(file="img/en1v3.png")
ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=128)
#
img_e2 = ImageTk.PhotoImage(file="img/en2v3.png")
ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=168)
#
img_e3 = ImageTk.PhotoImage(file="img/en3v3.png")
ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=208)
ttk.Button(text="КВ", width=5, command=kv_and_raid.kv).place(x=250, y=208)

ttk.Button(text="фото противника", width=16, command=create_img_arena_object).place(x=0, y=340)
ttk.Button(text="атака противника", width=16, command=kill).place(x=170, y=340)

root.mainloop()
