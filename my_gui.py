import tkinter as tk
from tkinter import ttk
import baza_dannyx as b_d



class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title(' помощник) "Метро 2033"')
        # self.geometry(f'374x{b_d.line10 + b_d.height_line + 2}+1200+50')
        self.geometry(f'474x{b_d.line10 + b_d.height_line + 2}+1100+50')
        self.resizable(False, False)

        self.info_bar = None
        self.l1_batt = None
        self.l2_batt = None
        self.l3_batt = None

        self.set_ui()

    def set_ui(self):
        # ["raised", "sunken", "flat", "ridge", "solid", "groove"]
        self.info_bar = ttk.Frame(self, borderwidth=1, relief="ridge", height=156, width=374)
        self.info_bar.place(anchor="nw")

        ttk.Button(self.info_bar, text="Gady", width=5).place(x=1, y=b_d.gady_y)
        ttk.Button(self.info_bar, text="Gavr", width=5).place(x=1, y=b_d.gavr_y)
        ttk.Button(self.info_bar, text="Велес", width=5).place(x=1, y=b_d.veles_y)
        ttk.Button(self.info_bar, text="Мара", width=5).place(x=1, y=b_d.mara_y)

        ttk.Button(self.info_bar, text="VIP", width=4).place(x=b_d.vip_x - b_d.s, y=b_d.label_line0  - 2)
        ttk.Button(self.info_bar, text="kiki", width=4).place(x=b_d.kiki_x - b_d.s, y=b_d.label_line0 - 2)
        ttk.Button(self.info_bar, text="wild", width=4).place(x=b_d.wild_x - (b_d.s + 3), y=b_d.label_line0 - 2)

        (ttk.Label(self.info_bar, text="arah", width=4, background='#858585', foreground='#050505').
         place(x=b_d.arah_x - b_d.s, y=b_d.label_line0))

        self.l1_batt = ttk.Frame(self, borderwidth=1, relief="ridge", height=30, width=260)
        self.l1_batt.place(x=115, y=160)
        ttk.Button(self.l1_batt, text="КВ", width=13).pack(side=tk.LEFT)
        ttk.Button(self.l1_batt, text=" Start ", width=13).pack(side=tk.LEFT)

        self.l2_batt = ttk.Frame(self, borderwidth=1, relief="ridge", height=30, width=260)
        self.l2_batt.place(x=115, y=191)
        ttk.Button(self.l2_batt, text="wild+kiki", width=9).pack(side=tk.LEFT)
        ttk.Button(self.l2_batt, text="обход всех станций", width=17).pack(side=tk.LEFT)

        self.l3_batt = ttk.Frame(self, borderwidth=1, relief="ridge", height=30, width=260)
        self.l3_batt.place(x=115, y=222)
        ttk.Button(self.l3_batt, text='Save').pack(side=tk.LEFT)
        ttk.Button(self.l3_batt, text='рапорт E').pack()
        ttk.Button(self.l3_batt, text='рапорт W').pack(side=tk.RIGHT)

root = Application()
root.mainloop()