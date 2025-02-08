import my_color_text as mct


class Hero:

    def __init__(self, name_ru=None, name_en=None):
        self.name_en = name_en
        self.name_ru = name_ru
        self.path_task = ''

        self.vip = 0
        self.gifts = 0
        self.kiki = 0
        self.rat = 0
        self.arachne = 0
        self.raptor = 0
        self.wildman = 0

        self.duel_all = 0
        self.duel_now = 0
        self.duel_victory = 0
        self.duel_defeat = 0

    def get_path_task(self):
        return f'{self.path_task}'

    def vip_app(self):
        self.vip += 1

    def gifts_app(self):
        self.gifts += 1

    def app_kiki(self):
        self.kiki += 1

    def app_rat(self):
        self.rat += 1

    def get_qty_rat(self):
        return self.rat

    def get_qty_attribute(self, attribute):
        return self.attribute

    def app_arachne(self):
        self.arachne += 1

    def app_raptor(self):
        self.raptor += 1

    def wildman_app(self):
        self.wildman += 1

    def get_qty_wildman(self):
        return self.wildman

    def get_name_ru(self):
        return self.name_ru

    def get_name_en(self):
        return self.name_en

    def duel_kv(self):
        self.duel_now += 1
        self.duel_all += 1

    def duel_victory_app(self):
        self.duel_victory += 1
        self.duel_kv()

    def her_message(self):
        return f'обнаружен {self.name_ru}'

    def get_path_tasc(self):
        return self.path_task


gavr = Hero('Гавр', 'Gavr')
gavr.path_task = 'img/person/tasks_gavr/'

gady = Hero("Гадя", 'Gady')
gady.path_task = 'img/person/tasks_gady/'

veles = Hero('Велес', 'Велес')
veles.path_task = 'img/person/tasks_veles/'

mara = Hero('Мара', 'Mara')
mara.path_task = 'img/person/tasks_mara/'


class Activ:
    hero_activ_name = ''  # значение переменной
    hero_activ = ''
    result_duel = ""

# Activ.hero_activ = gady # значение, которое выдает fun.select_hero(True)
# Hero.duel_kv(Activ.hero_activ)  # формат обращения к методу
#
# print(Hero.get_path_task(Activ.hero_activ))
