from time import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk

import baza_dannyx as b_d
import color_text
import complex_phrases
import fun
import fun_events
import heroes
import kv_and_raid
import os_action
import person
import revision_tents
import solid_memory
import station_master
import touring
from event_arena import create_img_arena_object, kill

fun.my_print_to_file('')
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file("******* перезапуск программы *******")
fun.my_print_to_file('*******                      *******')
fun.my_print_to_file('')

heroes.Activ.date_now = fun.date_utc_now()


def start_prog():
    state_file = solid_memory.reading_all_state_config()
    if state_file:
        # print(tc_green('установка значений из файла'))
        try:
            solid_memory.setting_updatable_values()
            # print(heroes.Activ.result_load)
        except KeyError:
            print(color_text.tc_red('KeyError'))
        except Exception as cod:
            print(color_text.tc_red(f'Не понятно что произошло в updatable)). Код ошибки {cod}'))

        try:
            solid_memory.setting_cumulative_values()
            # print(heroes.Activ.result_load)
        except KeyError:
            print(color_text.tc_red('KeyError'))
        except Exception as cod:
            print(color_text.tc_red(f'Не понятно что произошло в cumulative )). Код ошибки {cod}'))

        displaying_values(info=False)
    else:
        displaying_values()
    # вывод инфо состояния
    complex_phrases.display_smol_report_wildman()
    complex_phrases.display_info_energy_all()
    # удаление файлов старше 10 дней
    os_action.check_files(old_day=10)
    return


def displaying_values(info=True):
    if info:
        solid_memory.save_all_state_config(info=True)
    else:
        solid_memory.save_all_state_config(info=False)

    gady_rat.set(heroes.gady.grey_rat)
    gavr_rat.set(heroes.gavr.grey_rat)
    # veles_rat.set(heroes.veles.grey_rat)
    mara_rat.set(heroes.mara.grey_rat)

    gady_kiki.set(heroes.gady.kiki)
    gavr_kiki.set(heroes.gavr.kiki)
    # veles_kiki.set(heroes.veles.kiki)
    mara_kiki.set(heroes.mara.kiki)

    gady_arachne.set(heroes.gady.arachne)
    gavr_arachne.set(heroes.gavr.arachne)
    # veles_arachne.set(heroes.veles.arachne)
    mara_arachne.set(heroes.mara.arachne)

    gady_raptor.set(heroes.gady.raptor)
    gavr_raptor.set(heroes.gavr.raptor)
    # veles_raptor.set(heroes.veles.raptor)
    mara_raptor.set(heroes.mara.raptor)

    gady_gift.set(heroes.gady.holiday_gift)
    gavr_gift.set(heroes.gavr.holiday_gift)
    # veles_gift.set(heroes.veles.holiday_gift)
    mara_gift.set(heroes.mara.holiday_gift)

    gavr_vip.set(heroes.gavr.vip)
    gady_vip.set(heroes.gady.vip)
    # veles_vip.set(heroes.veles.vip)
    mara_vip.set(heroes.mara.vip)

    gady_wild.set(heroes.gady.wildman)
    gavr_wild.set(heroes.gavr.wildman)
    # veles_wild.set(heroes.veles.wildman)
    mara_wild.set(heroes.mara.wildman)


def start_pm():
    fun_events.start_p_m()
    displaying_values(info=False)


def bonus():
    fun.bonus()


def en_1():
    station_master.task_pos_item(1)
    displaying_values(info=False)


def en_2():
    station_master.task_pos_item(2)
    displaying_values(info=False)


def en_3():
    station_master.task_pos_item(3)
    displaying_values(info=False)


def puli():
    station_master.option_task_money()
    displaying_values(info=False)


def kiki():
    touring.for_kiki()
    fun.work_8_hour()
    displaying_values(info=False)


def tent_inspection():
    hero = fun.selection_hero()
    ins = heroes.Hero.get_vip_all(heroes.Activ.hero_activ)
    if ins == 10:
        print(complex_phrases.set_inspect_report())
        return
    else:
        vip_case_all = 0
        it_revision = 0
        fun.move_friends_list_to_top()

        while vip_case_all < 10:
            if hero == 'Gady':
                vip_case_all += revision_tents.tent_raid()
                heroes.gady.vip = vip_case_all
            if hero == 'Gavr':
                vip_case_all += revision_tents.tent_raid()
                heroes.gavr.vip = vip_case_all
            if hero == 'Mara':
                vip_case_all += revision_tents.tent_raid()
                heroes.mara.vip = vip_case_all
            # if hero == 'Велес':
            #     vip_case_all += revision_tents.tent_raid()
            #     heroes.veles.vip = vip_case_all
            it_revision += 1
            print(f'{vip_case_all} из {it_revision} осмотренных')
            fun.move_friends_list_left()
            if it_revision == 13:
                vip_case_all = 10
                if hero == 'Gady':
                    heroes.gady.vip = vip_case_all
                if hero == 'Gavr':
                    heroes.gavr.vip = vip_case_all
                if hero == 'Mara':
                    heroes.mara.vip = vip_case_all
                # if hero == 'Велес':
                #     heroes.veles.vip = vip_case_all
        revision_tents.end_raid()
        displaying_values(info=False)
        return


def tasks_na_kievskoy():
    hero = fun.selection_hero(show_name=False)
    if hero:
        heroes.Hero.app_wildman_days_count(heroes.Activ.hero_activ)
        # print(Hero.get_days_count_wildman(Activ.hero_activ))
    else:
        print('герой не опознан')
        return
    touring.for_wilds()
    fun.work_8_hour()
    # Hero.a
    displaying_values(info=False)


def wild_kiki():
    start_time = time()
    hero = fun.selection_hero()
    if hero:
        heroes.Hero.app_wildman_days_count(heroes.Activ.hero_activ)
        # print(Hero.get_days_count_wildman(Activ.hero_activ))
    else:
        print('герой не опознан')
        return
    touring.for_wilds()
    displaying_values()
    touring.for_kiki()
    fun.work_8_hour()
    displaying_values(info=False)
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
        bypass_hero = heroes.Hero.get_bypass(heroes.Activ.hero_activ)
        # движение по маршруту
        touring.sbor_podarkov(bypass_hero)
        # получение количества станций на маршруте
        q_st = fun.get_len_bypass(bypass_hero)
        # получение количества собранных подарков
        q_gifts = heroes.Hero.get_qty_gift(heroes.Activ.hero_activ)
    else:
        print('герой не опознан')
        return
    # вывод информации
    print(f'На {q_st} станциях собрано {q_gifts} подарков')
    displaying_values(info=False)


def changeColor(*, her_active):
    if her_active == 'Gady':
        label_1.configure(background="yellow")
    else:
        label_1.configure(background='white')
    if her_active == 'Gavr':
        label_2.configure(background="yellow")
    else:
        label_2.configure(background='white')
    # if her_active == 'Велес':
    #     label_3.configure(background="yellow")
    # else:
    #     label_3.configure(background='white')
    if her_active == 'Mara':
        label_4.configure(background="yellow")
    else:
        label_4.configure(background='white')


def change_gady():
    person.change_acc(change_hero_name='gady')
    displaying_values(info=False)
    changeColor(her_active=fun.selection_hero(show_name=False))


def change_gavr():
    person.change_acc(change_hero_name='gavr')
    displaying_values(info=False)
    changeColor(her_active=fun.selection_hero(show_name=False))


def change_veles():
    person.change_acc(change_hero_name='veles')
    displaying_values(info=False)
    changeColor(her_active=fun.selection_hero(show_name=False))


def change_mara():
    person.change_acc(change_hero_name='mara')
    displaying_values(info=False)
    changeColor(her_active=fun.selection_hero(show_name=False))


def save_home_point():
    fun.selection_hero(show_name=False)
    address = heroes.Hero.get_home_location(heroes.Activ.hero_activ)
    location = fun.loc_now()[0]
    mes = F'Твой адрес - {address} .\nНовый адрес {location}. Сохранить?'
    answer = messagebox.askyesno(title='Паспортист ))', message=mes)
    # print(f'{type(answer)}, {answer=}')
    if answer:
        heroes.Hero.setting_home(heroes.Activ.hero_activ, location)
    displaying_values(info=True)


def save_date_up():
    fun.selection_hero(show_name=False)
    date_temp = heroes.Hero.get_up_date(heroes.Activ.hero_activ)
    if date_temp == heroes.Activ.date_now:
        mes = 'Дата сегодня уже обновлена'
        answer = messagebox.showinfo(title='lvlup', message=mes)
        # print(f'{type(answer)}, {answer=}')
    else:
        if date_temp == '':
            mes = 'Последней записи нет. Запишем?'
        else:
            mes = f'Последняя запись {date_temp}.\nПерезаписать дату?'
        answer = messagebox.askyesno(title='lvlup', message=mes)
    if answer and answer != 'ok':
        # print(f'{type(answer)}, {answer=}')
        heroes.Hero.set_up_date(heroes.Activ.hero_activ)
        displaying_values(info=True)


def get_target(event):
    selection = combobox.get()
    touring.move_to_target(target_point=selection)
    displaying_values(info=False)
    return


def timer():
    tim_gady = int(heroes.Hero.get_time_entree(heroes.gady) - time())
    if tim_gady > 0:
        hours = tim_gady // 3600
        minutes = (tim_gady - hours * 3600) // 60
        seconds = tim_gady % 60
        tim_gady -= 1
        timer_gady_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        date_up = heroes.Hero.get_up_date(heroes.gady)
        if date_up != '':
            number_days = fun.dif_days(date_old=date_up)
            msg = f'{number_days} day  ур'
            # print(f'{msg=}')
            timer_gady_label.config(text=msg)
        else:
            timer_gady_label.config(text="00:00:00")

    tim_gavr = int(heroes.Hero.get_time_entree(heroes.gavr) - time())
    if tim_gavr > 0:
        hours = tim_gavr // 3600
        minutes = (tim_gavr - hours * 3600) // 60
        seconds = tim_gavr % 60
        tim_gavr -= 1
        timer_gavr_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        date_up = heroes.Hero.get_up_date(heroes.gavr)
        if date_up:
            number_days = fun.dif_days(date_old=date_up)
            msg = f'{number_days} day  ур'
            timer_gavr_label.config(text=msg)
        else:
            timer_gavr_label.config(text="00:00:00")

    # tim_veles = int(heroes.Hero.get_time_entree(heroes.veles) - time())
    # if tim_veles > 0:
    #     hours = tim_veles // 3600
    #     minutes = (tim_veles - hours * 3600) // 60
    #     seconds = tim_veles % 60
    #     tim_veles -= 1
    #     timer_veles_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    # else:
    #     timer_veles_label.config(text="00:00:00")

    tim_mara = int(heroes.Hero.get_time_entree(heroes.mara) - time())
    if tim_mara > 0:
        hours = tim_mara // 3600
        minutes = (tim_mara - hours * 3600) // 60
        seconds = tim_mara % 60
        tim_mara -= 1
        timer_mara_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    else:
        date_up = heroes.Hero.get_up_date(heroes.mara)
        if date_up:
            number_days = fun.dif_days(date_old=date_up)
            msg = f'{number_days} day  ур'
            timer_mara_label.config(text=msg)
        else:
            timer_mara_label.config(text="00:00:00")

    tim = int(time())
    # hours_now = tim // 3600
    minutes_now = (tim - (tim // 3600) * 3600) // 60
    if minutes_now != heroes.temp_min:
        heroes.temp_min = minutes_now
        heroes.time_now_ = fun.time_now()

    root.after(1000, timer)


def set_timer24():
    fun.selection_hero(show_name=False)
    tim_entree = int(time() + b_d.timer24)  #
    heroes.Hero.set_time_entree(heroes.Activ.hero_activ, tim_entree)
    solid_memory.save_all_state_config(info=False)


def set_timer8():
    fun.selection_hero(show_name=False)
    tim_entree = int(time() + b_d.timer8)  #
    heroes.Hero.set_time_entree(heroes.Activ.hero_activ, tim_entree)
    solid_memory.save_all_state_config(info=False)


def set_timer1():
    fun.selection_hero(show_name=False)
    tim_entree = int(time() + b_d.timer1)  #
    heroes.Hero.set_time_entree(heroes.Activ.hero_activ, tim_entree)
    solid_memory.save_all_state_config(info=False)


root = Tk()
root.title(f' помощник "Метро 2033"')

width = b_d.timer_x + 73  # Ширина
# width = 371# Ширина
height = b_d.line10 + b_d.height_line + 2  # Высота
h = width - 371
position_x = 1200 - h
position_y = 50
# root.geometry("370x362+1200+50")  # Ширина x Высота + положение X + положение Y
# root.geometry(f'371x{b_d.line11 + b_d.height_line + 2}+1200+50')  # Ширина x Высота + положение X + положение Y
root.geometry(f'{width}x{height}+{position_x}+{position_y}')  # Ширина x Высота + положение X + положение Y
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

box_paths = touring.list_names_all_station
box_paths.insert(0, 'домой')
lang_var = StringVar(value=box_paths[0])

# -------------------------------------------------------------
start_prog()
# -------------------------------------------------------------

# блок командных кнопок
ttk.Button(text="КВ", width=13, command=kv_and_raid.kv).place(x=115, y=b_d.line5)
ttk.Button(text=" Start ", width=13, command=start_pm).place(x=241, y=b_d.line5)

ttk.Button(text="set 24 h", width=8, command=set_timer24).place(x=b_d.timer_x, y=b_d.line5)
ttk.Button(text="set 8 h ", width=8, command=set_timer8).place(x=b_d.timer_x, y=b_d.line6)
ttk.Button(text="set 1 h ", width=8, command=set_timer1).place(x=b_d.timer_x, y=b_d.line7)

ttk.Button(text="wild+kiki", width=9, command=wild_kiki).place(x=115, y=b_d.line6)
ttk.Button(text="обход всех станций", width=17, command=collecting_gifts_at_stations).place(x=205, y=b_d.line6)

ttk.Button(text='Save', width=12, command=displaying_values).place(x=115, y=b_d.line7)
ttk.Button(text='рапорт E', width=12, command=complex_phrases.display_info_energy_all).place(x=200, y=b_d.line7)
ttk.Button(text='рапорт W', width=12, command=complex_phrases.display_report_wildman).place(x=285, y=b_d.line7)

ttk.Label(text='            куда пойдем ?', width=21, background='#858585', foreground='#050505').place(x=156,
                                                                                                        y=b_d.line8)

combobox = ttk.Combobox(textvariable=lang_var, values=box_paths, state="readonly", width=23)
combobox.place(x=138, y=b_d.line9)
combobox.bind("<<ComboboxSelected>>", get_target)
ttk.Button(text='Паспортист', width=14, command=save_home_point).place(x=0, y=b_d.line9 - 2)

ttk.Button(text="фото противника", width=15, command=create_img_arena_object).place(x=0, y=b_d.line10)
ttk.Button(text="атака противника", width=15, command=kill).place(x=225, y=b_d.line10)
# ttk.Button(text="kv rapport", width=6, command=kv_report).place(x=150, y=b_d.line10)

timer_gady_label = ttk.Label()
timer_gady_label.config(text="", font=("Helvetica", 12))  # , font=("Helvetica", 12)
timer_gady_label.place(x=b_d.timer_x, y=b_d.gady_y)

timer_gavr_label = ttk.Label()
timer_gavr_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
timer_gavr_label.place(x=b_d.timer_x, y=b_d.gavr_y)

# timer_veles_label = ttk.Label()
# timer_veles_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
# timer_veles_label.place(x=b_d.timer_x, y=b_d.veles_y)

timer_mara_label = ttk.Label()
timer_mara_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
timer_mara_label.place(x=b_d.timer_x, y=b_d.mara_y)

ttk.Button(text="Gady", width=5, command=change_gady).place(x=0, y=b_d.gady_y)
ttk.Button(text="Gavr", width=5, command=change_gavr).place(x=0, y=b_d.gavr_y)
# ttk.Button(text="Велес", width=5, command=change_veles).place(x=0, y=b_d.veles_y)
ttk.Button(text="Мара", width=5, command=change_mara).place(x=0, y=b_d.mara_y)

ttk.Button(text="VIP", width=4, command=tent_inspection).place(x=b_d.vip_x - b_d.s, y=b_d.label_line0 - 3)
ttk.Button(text="kiki", width=4, command=kiki).place(x=b_d.kiki_x - b_d.s, y=b_d.label_line0 - 3)
ttk.Button(text="wild", width=4, command=tasks_na_kievskoy).place(x=b_d.wild_x - (b_d.s + 3), y=b_d.label_line0 - 3)
ttk.Button(text="up", width=4, command=save_date_up).place(x=0, y=b_d.label_line0 - 3)
w_l = 3
# блок инфо строк
label_1 = ttk.Label()
label_1.configure(textvariable=gady_vip, width=w_l)
label_1.place(x=b_d.vip_x, y=b_d.gady_y)

label_2 = ttk.Label()
label_2.configure(textvariable=gavr_vip, width=w_l)
label_2.place(x=b_d.vip_x, y=b_d.gavr_y)

# label_3 = ttk.Label()
# label_3.configure(textvariable=veles_vip, width=w_l)
# label_3.place(x=b_d.vip_x, y=b_d.veles_y)

label_4 = ttk.Label()
label_4.configure(textvariable=mara_vip, width=w_l)
label_4.place(x=b_d.vip_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.mara_y)

ttk.Label(textvariable=gavr_kiki).place(x=b_d.kiki_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_kiki).place(x=b_d.kiki_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_kiki).place(x=b_d.kiki_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_kiki).place(x=b_d.kiki_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.mara_y)

ttk.Label(text="arah", width=4, background='#858585', foreground='#050505').place(x=b_d.arah_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_arachne).place(x=b_d.arah_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_arachne).place(x=b_d.arah_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_arachne).place(x=b_d.arah_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_arachne).place(x=b_d.arah_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.mara_y)

ttk.Label(text="rapt", width=4, background='#858585', foreground='#050505').place(x=b_d.rapt_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_raptor).place(x=b_d.rapt_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_raptor).place(x=b_d.rapt_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_raptor).place(x=b_d.rapt_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_raptor).place(x=b_d.rapt_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.mara_y)

ttk.Label(text="rat", width=4, background='#858585', foreground='#050505').place(x=b_d.rat_x - b_d.s,
                                                                                 y=b_d.label_line0)
ttk.Label(textvariable=gavr_rat).place(x=b_d.rat_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_rat).place(x=b_d.rat_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_rat).place(x=b_d.rat_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_rat).place(x=b_d.rat_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.mara_y)

ttk.Label(text="gift", width=4, background='#858585', foreground='#050505').place(x=b_d.gift_x - b_d.s,
                                                                                  y=b_d.label_line0)
ttk.Label(textvariable=gavr_gift).place(x=b_d.gift_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_gift).place(x=b_d.gift_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_gift).place(x=b_d.gift_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_gift).place(x=b_d.gift_x, y=b_d.mara_y)

ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gady_y)
ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gavr_y)
# ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.veles_y)
ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.mara_y)

ttk.Label(textvariable=gavr_wild).place(x=b_d.wild_x, y=b_d.gavr_y)
ttk.Label(textvariable=gady_wild).place(x=b_d.wild_x, y=b_d.gady_y)
# ttk.Label(textvariable=veles_wild).place(x=b_d.wild_x, y=b_d.veles_y)
ttk.Label(textvariable=mara_wild).place(x=b_d.wild_x, y=b_d.mara_y)

# блок выбора заданий
difference_str_img = 8
line_img = b_d.line5 + 5
imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
ttk.Button(root, image=imagePul, command=puli).place(x=56, y=line_img + 15)
img_e1 = ImageTk.PhotoImage(file="img/overall/en1v3.png")
ttk.Button(root, image=img_e1, command=en_1).place(x=0, y=line_img)
img_e2 = ImageTk.PhotoImage(file="img/overall/en2v3.png")
ttk.Button(root, image=img_e2, command=en_2).place(x=0, y=line_img + b_d.height_line + difference_str_img)
img_e3 = ImageTk.PhotoImage(file="img/overall/en3v3.png")
ttk.Button(root, image=img_e3, command=en_3).place(x=0, y=line_img + b_d.height_line * 2 + difference_str_img * 2)
#
timer()
root.mainloop()
