# import tkinter as tk
# from tkinter import ttk
# import baza_dannyx as b_d
# import fun
# import touring
#
#
#
# class MyGui(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title(' помощник "Метро 2033"')
#         self.geometry("370x362+1200+50")  # Ширина x Высота + координата X + координата Y
#         self.resizable(False, False)
#
#         self.set_gui()
#
#     def set_gui(self):
#         ttk.Button(self, text="КВ", width=8).place(x=114, y=b_d.line5)
#         ttk.Button(self, text=" Start ", width=14, command=fun.start_p_m).place(x=200, y=b_d.line5)
#         ttk.Button(self, text="wild+kiki", width=10).place(x=114, y=b_d.line6)
#         ttk.Button(self, text="на Киев", width=7, command=self.frunze_kiev).place(x=215, y=b_d.line6)
#         ttk.Button(self, text="домой ", width=7, command=kiev_frunze).place(x=291, y=b_d.line6)
#         ttk.Button(self, text="Паук+Ящер", width=10, command=arachne_and_raptor).place(x=267, y=b_d.line7)
#         ttk.Button(self, text="обход всех станций", width=16, command=collecting_gifts_at_stations).place(x=114, y=b_d.line7)
#         ttk.Button(self, text='Save', width=12, command=displaying_values).place(x=125, y=b_d.line8)
#         ttk.Button(self, text='рапорт', width=12, command=report).place(x=250, y=b_d.line8)
#         ttk.Button(self, text="frunze_riga", width=12, command=frunze_riga).place(x=0, y=b_d.line9)
#         ttk.Button(self, text="riga_frunze", width=12, command=riga_frunze).place(x=125, y=b_d.line9)
#         ttk.Button(self, text="test гардероб", width=12, command=person.pereodevanie).place(x=250, y=b_d.line9)
#         ttk.Button(self, text="frunze_bulvar", width=12, command=frunze_bulvar).place(x=0, y=b_d.line10)
#         ttk.Button(self, text="bulvar_frunze", width=12, command=bulvar_frunze).place(x=125, y=b_d.line10)
#         ttk.Button(self, text="тест tour", width=12, command=dvizh_test).place(x=250, y=b_d.line10)
#         ttk.Button(self, text="фото противника", width=14, command=create_img_arena_object).place(x=0, y=b_d.line11)
#         ttk.Button(self, text="атака противника", width=14, command=kill).place(x=232, y=b_d.line11)
#
#         ttk.Button(self, text="Gady", width=5, command=change_gady).place(x=0, y=b_d.gady_y)
#         ttk.Button(self, text="Gavr", width=5, command=change_gavr).place(x=0, y=b_d.gavr_y)
#         ttk.Button(self, text="Велес", width=5, command=change_veles).place(x=0, y=b_d.veles_y)
#         ttk.Button(self, text="Мара", width=5, command=change_mara).place(x=0, y=b_d.mara_y)
#
#         ttk.Button(self, text="VIP", width=4, command=tent_inspection).place(x=b_d.vip_x - b_d.s, y=b_d.label_line0 - 3)
#         ttk.Button(self, text="kiki", width=4, command=kiki).place(x=b_d.kiki_x - b_d.s, y=b_d.label_line0 - 3)
#         ttk.Button(self, text="wild", width=4, command=tasks_na_kievskoy).place(x=b_d.wild_x - (b_d.s + 3),
#                                                                           y=b_d.label_line0 - 3)
#
#     def frunze_kiev(self):
#         touring.frunze_kiev()
#         self.displaying_values()
#
#     def kiev_frunze(self):
#         touring.kiev_frunze()
#         self.displaying_values()
#
#     def displaying_values(self):
#         gady_rat.set(her.gady.grey_rat)
#         gavr_rat.set(her.gavr.grey_rat)
#         veles_rat.set(her.veles.grey_rat)
#         mara_rat.set(her.mara.grey_rat)
#
#         gady_kiki.set(her.gady.kiki)
#         gavr_kiki.set(her.gavr.kiki)
#         veles_kiki.set(her.veles.kiki)
#         mara_kiki.set(her.mara.kiki)
#
#         gady_arachne.set(her.gady.arachne)
#         gavr_arachne.set(her.gavr.arachne)
#         veles_arachne.set(her.veles.arachne)
#         mara_arachne.set(her.mara.arachne)
#
#         gady_raptor.set(her.gady.raptor)
#         gavr_raptor.set(her.gavr.raptor)
#         veles_raptor.set(her.veles.raptor)
#         mara_raptor.set(her.mara.raptor)
#
#         gady_gift.set(her.gady.gifts)
#         gavr_gift.set(her.gavr.gifts)
#         veles_gift.set(her.veles.gifts)
#         mara_gift.set(her.mara.gifts)
#
#         gavr_vip.set(her.gavr.vip)
#         gady_vip.set(her.gady.vip)
#         veles_vip.set(her.veles.vip)
#         mara_vip.set(her.mara.vip)
#
#         gady_wild.set(her.gady.wildman)
#         gavr_wild.set(her.gavr.wildman)
#
#         solid_memory.save_to_file()
#
