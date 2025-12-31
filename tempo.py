# from tkinter import *
# from tkinter import messagebox
# # from tkinter import
# from tkinter import ttk
#
# from PIL import ImageTk
# import baza_dannyx as b_d
#
# root = Tk()
# root.title(f' помощник "Метро 2033"')
#
# width = b_d.timer_x + 73  # Ширина
# # width = 371# Ширина
# height = b_d.line10 + b_d.height_line + 2  # Высота
# h = width - 371
# position_x = 1200 - h
# position_y = 50
# # root.geometry("370x362+1200+50")  # Ширина x Высота + положение X + положение Y
# # root.geometry(f'371x{b_d.line11 + b_d.height_line + 2}+1200+50')  # Ширина x Высота + положение X + положение Y
# root.geometry(f'{width}x{height}+{position_x}+{position_y}')  # Ширина x Высота + положение X + положение Y
# root.resizable(False, False)
#
# gavr_vip = StringVar()
# gady_vip = StringVar()
# mara_vip = IntVar()
# veles_vip = IntVar()
#
# gavr_rat = StringVar()
# gady_rat = StringVar()
# mara_rat = IntVar()
# veles_rat = IntVar()
#
# gavr_kiki = StringVar()
# gady_kiki = StringVar()
# mara_kiki = StringVar()
# veles_kiki = IntVar()
#
# gavr_arachne = StringVar()
# gady_arachne = StringVar()
# mara_arachne = IntVar()
# veles_arachne = IntVar()
#
# gavr_raptor = StringVar()
# gady_raptor = StringVar()
# mara_raptor = IntVar()
# veles_raptor = IntVar()
#
# gavr_gift = StringVar()
# gady_gift = StringVar()
# mara_gift = IntVar()
# veles_gift = IntVar()
#
# gavr_wild = StringVar()
# gady_wild = StringVar()
# mara_wild = StringVar()
# veles_wild = StringVar()
#
# box_paths = ['1', '2', '4']
# box_paths.insert(0, 'домой')
# lang_var = StringVar(value=box_paths[0])
#
# # -------------------------------------------------------------
# # start_prog()
# # -------------------------------------------------------------
#
# # блок командных кнопок
# ttk.Button(text="КВ", width=10).place(x=115, y=b_d.line4)
# ttk.Button(text=" Start ", width=10).place(x=190, y=b_d.line4)
# ttk.Button(text='Save', width=12).place(x=265, y=b_d.line4)
#
# ttk.Button(text="set 24 h", width=8).place(x=b_d.timer_x, y=b_d.line4)
# ttk.Button(text="set 8 h ", width=8,).place(x=b_d.timer_x, y=b_d.line5)
# ttk.Button(text="set 1 h ", width=8,).place(x=b_d.timer_x, y=b_d.line6)
#
# ttk.Button(text="wild+kiki", width=9).place(x=115, y=b_d.line5)
# ttk.Button(text="обход всех станций", width=18).place(x=205, y=b_d.line5)
#
# ttk.Button(text='рапорт W_R', width=12).place(x=115, y=b_d.line6)
# ttk.Button(text='рапорт W', width=12, ).place(x=200, y=b_d.line6)
# ttk.Button(text='рапорт E', width=12, ).place(x=285, y=b_d.line6)
#
# ttk.Label(text='            куда пойдем ?', width=21, background='#858585', foreground='#050505').place(x=156,
#                                                                                                         y=b_d.line7)
#
# combobox = ttk.Combobox(textvariable=lang_var, values=box_paths, state="readonly", width=23)
# combobox.place(x=138, y=b_d.line8)
# combobox.bind("<<ComboboxSelected>>")
# ttk.Button(text='Паспортист', width=14).place(x=0, y=b_d.line8 - 2)
#
# ttk.Button(text="фото противника", width=16).place(x=0, y=b_d.line9)
# ttk.Button(text="атака противника", width=16).place(x=225, y=b_d.line9)
# ttk.Button(text="set_param", width=10).place(x=150, y=b_d.line10)
#
# timer_gady_label = ttk.Label()
# timer_gady_label.config(text="", font=("Helvetica", 12))  # , font=("Helvetica", 12)
# timer_gady_label.place(x=b_d.timer_x, y=b_d.gady_y)
#
# timer_gavr_label = ttk.Label()
# timer_gavr_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
# timer_gavr_label.place(x=b_d.timer_x, y=b_d.gavr_y)
#
# # timer_veles_label = ttk.Label()
# # timer_veles_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
# # timer_veles_label.place(x=b_d.timer_x, y=b_d.veles_y)
#
# timer_mara_label = ttk.Label()
# timer_mara_label.config(text="00:00:00", font=("Helvetica", 12))  # , font=("Helvetica", 12)
# timer_mara_label.place(x=b_d.timer_x, y=b_d.mara_y)
#
# ttk.Button(text="Gady", width=5).place(x=0, y=b_d.gady_y)
# ttk.Button(text="Gavr", width=5).place(x=0, y=b_d.gavr_y)
# # ttk.Button(text="Велес", width=5, command=change_veles).place(x=0, y=b_d.veles_y)
# ttk.Button(text="Мара", width=5).place(x=0, y=b_d.mara_y)
#
# ttk.Button(text="VIP", width=5).place(x=b_d.vip_x - b_d.s, y=b_d.label_line0 - 3)
# ttk.Button(text="kiki", width=5).place(x=b_d.kiki_x - b_d.s, y=b_d.label_line0 - 3)
# ttk.Button(text="wild", width=5).place(x=b_d.wild_x - (b_d.s + 3), y=b_d.label_line0 - 3)
# ttk.Button(text="up", width=4).place(x=0, y=b_d.label_line0 - 3)
# w_l = 3
# # блок инфо строк
# label_1 = ttk.Label()
# label_1.configure(textvariable=gady_vip, width=w_l)
# label_1.place(x=b_d.vip_x, y=b_d.gady_y)
#
# label_2 = ttk.Label()
# label_2.configure(textvariable=gavr_vip, width=w_l)
# label_2.place(x=b_d.vip_x, y=b_d.gavr_y)
#
# # label_3 = ttk.Label()
# # label_3.configure(textvariable=veles_vip, width=w_l)
# # label_3.place(x=b_d.vip_x, y=b_d.veles_y)
#
# label_4 = ttk.Label()
# label_4.configure(textvariable=mara_vip, width=w_l)
# label_4.place(x=b_d.vip_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_1, y=b_d.mara_y)
#
# ttk.Label(textvariable=gavr_kiki).place(x=b_d.kiki_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_kiki).place(x=b_d.kiki_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_kiki).place(x=b_d.kiki_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_kiki).place(x=b_d.kiki_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_2, y=b_d.mara_y)
#
# ttk.Label(text="arah", width=5, background='#858585', foreground='#050505').place(x=b_d.arah_x - b_d.s,
#                                                                                   y=b_d.label_line0)
# ttk.Label(textvariable=gavr_arachne).place(x=b_d.arah_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_arachne).place(x=b_d.arah_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_arachne).place(x=b_d.arah_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_arachne).place(x=b_d.arah_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_3, y=b_d.mara_y)
#
# ttk.Label(text="rapt", width=5, background='#858585', foreground='#050505').place(x=b_d.rapt_x - b_d.s,
#                                                                                   y=b_d.label_line0)
# ttk.Label(textvariable=gavr_raptor).place(x=b_d.rapt_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_raptor).place(x=b_d.rapt_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_raptor).place(x=b_d.rapt_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_raptor).place(x=b_d.rapt_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_4, y=b_d.mara_y)
#
# ttk.Label(text="w_rat", width=5, background='#858585', foreground='#050505').place(x=b_d.rat_x - b_d.s,
#                                                                                  y=b_d.label_line0)
# ttk.Label(textvariable=gavr_rat).place(x=b_d.rat_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_rat).place(x=b_d.rat_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_rat).place(x=b_d.rat_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_rat).place(x=b_d.rat_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_5, y=b_d.mara_y)
#
# ttk.Label(text="gift", width=5, background='#858585', foreground='#050505').place(x=b_d.gift_x - b_d.s,
#                                                                                   y=b_d.label_line0)
# ttk.Label(textvariable=gavr_gift).place(x=b_d.gift_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_gift).place(x=b_d.gift_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_gift).place(x=b_d.gift_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_gift).place(x=b_d.gift_x, y=b_d.mara_y)
#
# ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gady_y)
# ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.gavr_y)
# # ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.veles_y)
# ttk.Label(text='|').place(x=b_d.separator_6, y=b_d.mara_y)
#
# ttk.Label(textvariable=gavr_wild).place(x=b_d.wild_x, y=b_d.gavr_y)
# ttk.Label(textvariable=gady_wild).place(x=b_d.wild_x, y=b_d.gady_y)
# # ttk.Label(textvariable=veles_wild).place(x=b_d.wild_x, y=b_d.veles_y)
# ttk.Label(textvariable=mara_wild).place(x=b_d.wild_x, y=b_d.mara_y)
#
# # блок выбора заданий
# difference_str_img = 8
# line_img = b_d.line4 + 5
# imagePul = ImageTk.PhotoImage(file="img/overall/pulya.png")
# ttk.Button(root, image=imagePul).place(x=56, y=line_img + 15)
# img_e1 = ImageTk.PhotoImage(file="img/overall/en1v3.png")
# ttk.Button(root, image=img_e1).place(x=0, y=line_img)
# img_e2 = ImageTk.PhotoImage(file="img/overall/en2v3.png")
# ttk.Button(root, image=img_e2).place(x=0, y=line_img + b_d.height_line + difference_str_img)
# img_e3 = ImageTk.PhotoImage(file="img/overall/en3v3.png")
# ttk.Button(root, image=img_e3).place(x=0, y=line_img + b_d.height_line * 2 + difference_str_img * 2)
# #
#
# root.mainloop()
{'сержант': 'img/kv/result_round/loot/p1.png',
 'лейтенант': 'img/kv/result_round/loot/p2.png',
 'капитан': 'img/kv/result_round/loot/p3.png',
 'полковник': 'img/kv/result_round/loot/p4.png',
 'генерал': 'img/kv/result_round/loot/p5.png'}

import fun
import sounds


def detect_loot():
    dict_name_loot = {'корм 3': 'img/tonelli/loot_gift_box/feed3.png',
                      'пули': 'img/tonelli/loot_gift_box/many.png',

                      'елочная гирлянда': 'img/tonelli/loot_gift_box/ng1.png',
                      'елочный шар': 'img/tonelli/loot_gift_box/ng2.png',
                      'елочная звезда': 'img/tonelli/loot_gift_box/ng3.png',
                      'елочная хлопушка': 'img/tonelli/loot_gift_box/ng4.png',

                      # 'марки первая': 'img/tonelli/loot_gift_box/marc1.png',

                      'капитан': 'img/tonelli/loot_gift_box/p3.png',
                      'полковник': 'img/tonelli/loot_gift_box/p4.png',

                      }
    result = False
    for name in dict_name_loot:
        name_loot = fun.locCenterImg(name_img=dict_name_loot[name])
        if name_loot:
            result = name
            break
    return result


rez = detect_loot()
print(rez)
sounds.say_txt(str(rez))