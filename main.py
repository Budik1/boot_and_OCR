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

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

status_bonus = "0"


def bonus():
    fun.bonus()


def en_1():
    station_master.en_task_item(1)


def en_2():
    station_master.en_task_item(2)


def en_3():
    station_master.en_task_item(3)


def dvizh_test():
    sum_krys = touring.test()
    status_krysa.set(sum_krys)


def tent_inspection():
    def vip():
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


root = Tk()

root.title(' помощник "Метро 2033"')
root.geometry("327x380+1240+50")  # Ширина x Высота + координата X + координата Y
root.resizable(False, False)

status_kiki = IntVar(value=0)
status_krysa = StringVar(value='0')
status_vip = StringVar(value='0')

ttk.Button(text=" Start ", width=13, command=fun.start_p_m).place(x=0, y=0)
ttk.Button(text=" сбор бонуса ", width=13, command=fun.bonus, state="disabled").place(x=0, y=32)
ttk.Label(text=status_bonus).place(x=130, y=32)
ttk.Button(text="  сбор подарков  ", width=13, command=fun.station_gifts, state="disabled").place(x=0, y=64)
ttk.Button(text=" обход VIP ", width=13, command=tent_inspection).place(x=0, y=96)
ttk.Label(textvariable=status_vip).place(x=130, y=96)
# шаг 31
ttk.Button(text=" на Киевскую ", width=11, command=touring.frunze_kiev).place(x=120, y=169)
ttk.Button(text=" домой ", width=11, command=touring.kiev_most).place(x=120, y=200)
ttk.Button(text="кикиморы", width=11, command=touring.za_kikimorami).place(x=153, y=31)
ttk.Label(textvariable=status_kiki, background="#FFCDD2", foreground="#B71C1C", padding=4).place(x=263, y=31)
ttk.Button(text="Паук + Ящер", width=11, command=touring.pauk_yascher).place(x=153, y=0)

ttk.Button(text="test гардероб", width=11, command=person.pereodevanie).place(x=109, y=245)

ttk.Button(text="most_frunze", width=11, command=touring.most_frunze).place(x=218, y=277)
ttk.Button(text="frunze_most", width=11, command=touring.frunze_most).place(x=218, y=308)

ttk.Button(text="most_riga", width=11, command=touring.most_riga).place(x=109, y=277)  # x=133
ttk.Button(text="riga_most", width=11, command=touring.riga_most).place(x=109, y=308)

ttk.Button(text="frunze_riga", width=11, command=touring.frunze_riga).place(x=0, y=277)
ttk.Button(text="riga_frunze", width=11, command=touring.riga_frunze).place(x=0, y=308)

ttk.Button(text="задания на Киевской", width=17, command=touring.tasks_na_kievskoy).place(x=120, y=138)
# тест пробежка
ttk.Button(text="тест пробежка", width=13, command=dvizh_test).place(x=153, y=64)
ttk.Label(textvariable=status_krysa, background="#FFCDD2", foreground="#0000FF", padding=4).place(x=285, y=64)
ttk.Button(text="обход всех станций", width=16, command=touring.sbor_podarkov).place(x=153, y=96)

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
