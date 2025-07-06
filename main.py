from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from time import time

import fun
import station_master
import kv_and_raid
import touring
import person
import revision_tents
import baza_dannyx as b_d
import solid_memory
import heroes as her
import info_messages as i_mess
from heroes import Hero, Activ
from event_arena import create_img_arena_object, kill
from my_color_text import tc_red


fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

Activ.date_now = fun.date_utc_now()


def start_prog():
    state_file, data_to_load = solid_memory.reading_file()
    if state_file:
        # print(tc_green('установка значений из файла'))
        try:
            solid_memory.setting_cumulative_values(data_to_load)
            solid_memory.setting_updatable_values(data_to_load)
        except KeyError:
            print(tc_red('KeyError'))
        except Exception as cod:
            print(tc_red(f'Не понятно что произошло)). Код ошибки {cod}'))
        displaying_values(info=False)
    else:
        displaying_values()


def displaying_values(info=True):
    gady_rat.set(her.gady.grey_rat)
    gavr_rat.set(her.gavr.grey_rat)
    veles_rat.set(her.veles.grey_rat)
    mara_rat.set(her.mara.grey_rat)

    gady_kiki.set(her.gady.kiki)
    gavr_kiki.set(her.gavr.kiki)
    veles_kiki.set(her.veles.kiki)
    mara_kiki.set(her.mara.kiki)

    gady_arachne.set(her.gady.arachne)
    gavr_arachne.set(her.gavr.arachne)
    veles_arachne.set(her.veles.arachne)
    mara_arachne.set(her.mara.arachne)

    gady_raptor.set(her.gady.raptor)
    gavr_raptor.set(her.gavr.raptor)
    veles_raptor.set(her.veles.raptor)
    mara_raptor.set(her.mara.raptor)

    gady_gift.set(her.gady.gifts)
    gavr_gift.set(her.gavr.gifts)
    veles_gift.set(her.veles.gifts)
    mara_gift.set(her.mara.gifts)

    gavr_vip.set(her.gavr.vip)
    gady_vip.set(her.gady.vip)
    veles_vip.set(her.veles.vip)
    mara_vip.set(her.mara.vip)

    gady_wild.set(her.gady.wildman)
    gavr_wild.set(her.gavr.wildman)
    veles_wild.set(her.veles.wildman)
    mara_wild.set(her.mara.wildman)

    if info:
        solid_memory.save_to_file(info=True)
    else:
        solid_memory.save_to_file(info=False)


def bonus():
    fun.bonus()


def en_1():
    station_master.task_pos_item(1)
    displaying_values()


def en_2():
    station_master.task_pos_item(2)
    displaying_values()


def en_3():
    station_master.task_pos_item(3)
    displaying_values()


def puli():
    station_master.choosing_task_money()
    displaying_values()


def kiki():
    touring.for_kiki()
    fun.work_8_hour()
    displaying_values()


def tent_inspection():
    hero = fun.selection_hero()
    vip_case_all = 0
    it_revision = 0
    fun.move_friends_list_to_top()

    while vip_case_all < 10:
        if hero == 'Gady':
            vip_case_all += revision_tents.tent_raid()
            her.gady.vip = vip_case_all
        if hero == 'Gavr':
            vip_case_all += revision_tents.tent_raid()
            her.gavr.vip = vip_case_all
        if hero == 'Mara':
            vip_case_all += revision_tents.tent_raid()
            her.mara.vip = vip_case_all
        if hero == 'Велес':
            vip_case_all += revision_tents.tent_raid()
            her.veles.vip = vip_case_all
        it_revision += 1
        print(f'{vip_case_all} из {it_revision} осмотренных')
        fun.move_friends_list_left()
        if it_revision == 13:
            vip_case_all = 10
            if hero == 'Gady':
                her.gady.vip = vip_case_all
            if hero == 'Gavr':
                her.gavr.vip = vip_case_all
            if hero == 'Mara':
                her.mara.vip = vip_case_all
            if hero == 'Велес':
                her.veles.vip = vip_case_all
    revision_tents.end_raid()
    displaying_values()


def tasks_na_kievskoy():
    hero = fun.selection_hero()
    if hero:
        Hero.app_days_count_wildman(Activ.hero_activ)
        # print(Hero.get_days_count_wildman(Activ.hero_activ))
    else:
        print('герой не опознан')
        return
    touring.for_wilds()
    fun.work_8_hour()
    # Hero.a
    displaying_values()


def wild_kiki():
    start_time = time()
    hero = fun.selection_hero()
    if hero:
        Hero.app_days_count_wildman(Activ.hero_activ)
        # print(Hero.get_days_count_wildman(Activ.hero_activ))
    else:
        print('герой не опознан')
        return
    touring.for_wilds()
    displaying_values()
    touring.for_kiki()
    fun.work_8_hour()
    displaying_values()
    finish_time = float(time() - start_time)  # общее количество секунд
    minutes = int(finish_time // 60)  # количество минут
    seconds = round((finish_time % minutes), 2)
    print('Потрачено время', minutes, 'минут', seconds, 'сек.')


def collecting_gifts_at_stations():
    fun.push_close_all_()
    # определение героя
    hero = fun.selection_hero()
    # получение маршрута для определенного героя
    if hero:
        bypass_hero = Hero.get_bypass(Activ.hero_activ)
        # движение по маршруту
        touring.sbor_podarkov(bypass_hero)
        # получение количества станций на маршруте
        q_st = fun.get_len_bypass(bypass_hero)
        # получение количества собранных подарков
        q_gifts = Hero.get_qty_gift(Activ.hero_activ)
    else:
        print('герой не опознан')
        return
    # вывод информации
    print(f'На {q_st} станциях собрано {q_gifts} подарков')
    displaying_values()


def change_gady():
    person.change_acc(change_hero_name='gady')
    displaying_values(info=False)


def change_gavr():
    person.change_acc(change_hero_name='gavr')
    displaying_values(info=False)


def change_veles():
    person.change_acc(change_hero_name='veles')
    displaying_values(info=False)


def change_mara():
    person.change_acc(change_hero_name='mara')
    displaying_values(info=False)


def report():
    print(f'Gady {i_mess.report_wildman(hero=her.gady)}')
    print(f'Gavr {i_mess.report_wildman(hero=her.gavr)}')


def save_home_point():
    fun.selection_hero(show_name=False)
    adres = Hero.get_home_location(Activ.hero_activ)
    location = touring.loc_now()[0]
    mes = F'Твой адрес - {adres} .\nНовый адрес {location}. Сохранить?'
    ansver = messagebox.askyesno(title='Паспортист ))', message=mes)
    if ansver:
        fun.selection_hero()
        Hero.seting_home(Activ.hero_activ, location)

    displaying_values()
    print(f'{her.gady.home_location=}')
    print(f'{her.gavr.home_location=}')
    print(f'{her.veles.home_location=}')
    print(f'{her.mara.home_location=}')


def get_target(event):
    selection = combobox.get()
    print(f'Прокладываю маршрут к {selection}')
    touring.move_to_target(target_point=selection)
    displaying_values()


root = Tk()
root.title(' помощник "Метро 2033"')
# root.geometry("370x362+1200+50")  # Ширина x Высота + координата X + координата Y
root.geometry(f'371x{b_d.line10 + b_d.height_line + 2}+1200+50')  # Ширина x Высота + координата X + координата Y
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

gavr_wild = StringVar()
gady_wild = StringVar()
mara_wild = StringVar()
veles_wild = StringVar()

boxlist = touring.list_names_station
boxlist.insert(0, 'домой')
lang_var = StringVar(value=boxlist[0])

# -------------------------------------------------------------
start_prog()
# -------------------------------------------------------------

# блок командных кнопок
ttk.Button(text="КВ", width=13, command=kv_and_raid.kv).place(x=115, y=b_d.line5)
ttk.Button(text=" Start ", width=13, command=fun.start_p_m).place(x=241, y=b_d.line5)

ttk.Button(text="wild+kiki", width=9, command=wild_kiki).place(x=115, y=b_d.line6)
ttk.Button(text="обход всех станций", width=17, command=collecting_gifts_at_stations).place(x=205, y=b_d.line6)

ttk.Button(text='Save', width=13, command=displaying_values).place(x=115, y=b_d.line7)
ttk.Button(text='рапорт', width=13, command=report).place(x=241, y=b_d.line7)

ttk.Label(text='            куда пойдем ?', width=21, background='#858585', foreground='#050505').place(x=144,
                                                                                                        y=b_d.line8)

combobox = ttk.Combobox(textvariable=lang_var, values=boxlist, state="readonly", width=25)
combobox.place(x=117, y=b_d.line9)
combobox.bind("<<ComboboxSelected>>", get_target)
ttk.Button(text='S_H', width=4, command=save_home_point).place(x=63, y=b_d.line9 - 2)

ttk.Button(text="фото противника", width=15, command=create_img_arena_object).place(x=0, y=b_d.line10)
ttk.Button(text="атака противника", width=15, command=kill).place(x=225, y=b_d.line10)
# ttk.Button(text='Проверка', width=8, command=fun.verifi_img).place(x=144, y=b_d.line10)
ttk.Button(text='Где я ?', width=8, command=touring.loc_now).place(x=144, y=b_d.line10)

ttk.Button(text="Gady", width=5, command=change_gady).place(x=0, y=b_d.gady_y)
ttk.Button(text="Gavr", width=5, command=change_gavr).place(x=0, y=b_d.gavr_y)
ttk.Button(text="Велес", width=5, command=change_veles).place(x=0, y=b_d.veles_y)
ttk.Button(text="Мара", width=5, command=change_mara).place(x=0, y=b_d.mara_y)

ttk.Button(text="VIP", width=4, command=tent_inspection).place(x=b_d.vip_x - b_d.s, y=b_d.label_line0 - 3)
ttk.Button(text="kiki", width=4, command=kiki).place(x=b_d.kiki_x - b_d.s, y=b_d.label_line0 - 3)
ttk.Button(text="wild", width=4, command=tasks_na_kievskoy).place(x=b_d.wild_x - (b_d.s + 3), y=b_d.label_line0 - 3)

# блок инфо строк
ttk.Label(textvariable=gady_vip).place(x=b_d.vip_x, y=b_d.gady_y)
ttk.Label(textvariable=gavr_vip).place(x=b_d.vip_x, y=b_d.gavr_y)
ttk.Label(textvariable=veles_vip).place(x=b_d.vip_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_vip).place(x=b_d.vip_x, y=b_d.mara_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.mara_y)

ttk.Label(textvariable=gavr_kiki).place(x=b_d.kiki_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_kiki).place(x=b_d.kiki_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_kiki).place(x=b_d.kiki_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_kiki).place(x=b_d.kiki_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.mara_y)

ttk.Label(text="arah", width=4, background='#858585', foreground='#050505').place(x=b_d.arah_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_arachne).place(x=b_d.arah_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_arachne).place(x=b_d.arah_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_arachne).place(x=b_d.arah_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_arachne).place(x=b_d.arah_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.mara_y)

ttk.Label(text="rapt", width=4, background='#858585', foreground='#050505').place(x=b_d.rapt_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_raptor).place(x=b_d.rapt_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_raptor).place(x=b_d.rapt_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_raptor).place(x=b_d.rapt_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_raptor).place(x=b_d.rapt_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.mara_y)

ttk.Label(text="rat", width=4, background='#858585', foreground='#050505').place(x=b_d.rat_x - b_d.s,
                                                                                 y=b_d.label_line0)
ttk.Label(textvariable=gavr_rat).place(x=b_d.rat_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_rat).place(x=b_d.rat_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_rat).place(x=b_d.rat_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_rat).place(x=b_d.rat_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.mara_y)

ttk.Label(text="gift", width=4, background='#858585', foreground='#050505').place(x=b_d.gift_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_gift).place(x=b_d.gift_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_gift).place(x=b_d.gift_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_gift).place(x=b_d.gift_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_gift).place(x=b_d.gift_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gavr_y)
ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.mara_y)

ttk.Label(textvariable=gavr_wild).place(x=b_d.wild_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_wild).place(x=b_d.wild_x, y=b_d.gady_y)
ttk.Label(textvariable=veles_wild).place(x=b_d.wild_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_wild).place(x=b_d.wild_x, y=b_d.mara_y)

# блок выбора заданий
difference_str_img = 11
line_img = b_d.line5 + 15
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=puli).place(x=56, y=line_img + 15)
img_e1 = ImageTk.PhotoImage(file="img/overall/en1v3.png")
ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=line_img)
img_e2 = ImageTk.PhotoImage(file="img/overall/en2v3.png")
ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=line_img + b_d.height_line + difference_str_img)
img_e3 = ImageTk.PhotoImage(file="img/overall/en3v3.png")
ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=line_img + b_d.height_line * 2 + difference_str_img * 2)
#
root.mainloop()
