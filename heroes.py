import baza_dannyx as b_d
import color_text as myCt

# from fun import time_now

nam = 0  # для подсчета чего?
temp_min = None
time_now_ = ""


class Activ:
    hero_activ_name = ''  # значение переменной
    hero_activ = ''
    result_duel = ""
    check_date_ = ''
    date_now = ''
    hour_now = ''
    value_energy = 0
    name_file_ = None
    station_activ = ''
    qty_vip = 0
    duel_raid = 0


class Hero:

    def __init__(self, name_ru_=None, name_en_=None, name_id=None):
        self.name_en = name_en_
        self.name_ru = name_ru_
        self.name_id = name_id
        self.path_task = ''
        self.home_location = 'бомж'
        self.bypass = ()
        # self.bac_color = '#FFFFFF'

        self.vip = 0  #
        self.gifts = 0  #
        self.kiki = 0  #
        self.grey_rat = 0  #
        self.arachne = 0  #
        self.raptor = 0  #
        #
        self.wildman = 'x'
        self.wildman_count = 0
        self.wild_activ = False
        self.wildman_days_count = 0

        self.completing_tasks = False
        self.task_count = 0
        self.energy_count_today = 0
        self.energy_count_all = 0
        self.energy_kiev_count_all = 0
        self.value_energy = 0

        self.arena_count = 0  # счет арены
        self.arena_victory_count = 0

        # кв и рейд
        self.qty_duel_all = 0  # к-во боёв всего
        self.qty_duel_all_victory = 0  # к-во побед всего

        self.qty_duel_in_kv_all = 0
        self.qty_duel_in_kv_victory = 0

        self.danger = 0
        self.danger_victory = 0

        self.count_shoulder_straps_all = 0
        self.count_shoulder_straps_kv = 0
        self.__numbers_wins_to_loot = -1

        self.time_start_kv = 0
        self.last_attack = 0

        self.timer = 0
        self.time_entree = 0

        self.duel_raid = 0

    # kv
    @property
    def numbers_wins_to_loot(self):
        return self.__numbers_wins_to_loot

    @numbers_wins_to_loot.setter
    def numbers_wins_to_loot(self, value):
        self.__numbers_wins_to_loot = value


    def get_time_start_kv(self):
        return self.time_start_kv

    def set_time_start_kv(self, value):
        self.time_start_kv = value

    def get_last_attack(self):
        return self.last_attack

    def set_last_attack(self, value):
        self.last_attack = value

    def get_qty_duel_all(self):
        return self.qty_duel_all

    def up_qty_duel_all(self):
        self.qty_duel_all += 1

    def get_qty_duel_all_victory(self):
        return self.qty_duel_all_victory

    def up_qty_duel_all_victory(self):
        self.qty_duel_all_victory += 1

    def get_qty_duel_in_kv_all(self):
        return self.qty_duel_in_kv_all

    def up_qty_duel_in_kv_all(self):
        self.qty_duel_all += 1
        self.qty_duel_in_kv_all += 1

    def get_qty_duel_in_kv_victory(self):
        return self.qty_duel_in_kv_victory

    def up_qty_duel_in_kv_victory(self):
        self.qty_duel_in_kv_victory += 1
        self.qty_duel_all_victory += 1

    def get_qty_danger(self):
        return self.danger

    def app_qty_danger(self):
        self.danger += 1

    def get_qty_danger_v(self):
        return self.danger_victory

    def app_danger_v(self):
        self.danger_victory += 1

    def get_count_shoulder_straps_all(self):
        return self.count_shoulder_straps_all

    def up_count_shoulder_straps_all(self):
        self.count_shoulder_straps_all += 1

    def get_count_shoulder_straps_kv(self):
        return self.count_shoulder_straps_kv

    def up_count_shoulder_straps_kv(self):
        self.count_shoulder_straps_kv += 1

    def get_hour_start_kv(self):
        return self.time_start_kv

    def set_hour_start_kv(self, value):
        self.time_start_kv = value

    # timer
    def set_time_entree(self, value):
        self.time_entree = value

    def get_time_entree(self):
        return self.time_entree

    def set_timer(self, value):
        self.timer = value

    def get_timer(self):
        return self.timer

    def setting_value_energy(self, value):
        self.value_energy = value

    def setting_home(self, location):
        self.home_location = location

    # Uppers
    def app_arena_count(self):
        self.arena_count += 1

    def app_arena_victory_count(self):
        self.arena_victory_count += 1

    def app_energy_count_today(self, value):
        self.energy_count_today += value
        self.energy_count_all += value
        if Activ.station_activ == 'ст. Киевская':
            self.energy_kiev_count_all += value
            # print(color_text.tc_yellow('set energy_kiev_count_all'))

    def get_energy_kiev_count_all(self):
        return self.energy_kiev_count_all

    def app_task_count(self):
        self.task_count += 1

    def app_wildman_days_count(self):
        if not self.wild_activ:
            self.wild_activ = True
            self.wildman_days_count += 1
            # print(f'{self.name_ru} {self.days_count_wildman}')

    def set_wild_activ(self):
        """
        True надо заменить на дату сегодня
        """
        self.wild_activ = Activ.date_now

    def app_vip(self):
        self.vip += 1

    def app_gifts(self):
        self.gifts += 1

    def app_kiki(self):
        self.kiki += 1

    def app_arachne(self):
        self.arachne += 1

    def app_raptor(self):
        self.raptor += 1

    def app_wildman(self):
        self.wildman += 1
        self.wildman_count += 1

    def zero_wildman(self):
        self.wildman = 0

    def app_rat(self):
        self.grey_rat += 1

    def app_completing_tasks(self):
        self.completing_tasks = True

    # Гетеры
    def get_vip_all(self):
        return self.vip

    def get_arena_count(self):
        return self.arena_count

    def get_arena_victory_count(self):
        return self.arena_victory_count

    def get_home_location(self):
        return self.home_location

    def get_energy_count_all(self):
        return self.energy_count_all

    def get_energy_count_today(self):
        return self.energy_count_today

    def get_task_count(self):
        return self.task_count

    def get_report_wildman_now(self):
        if self.wildman:
            return f'{myCt.tc_yellow(str(self.wildman))} {myCt.tc_green("за сегодня")}'
        else:
            return f'по дикарям нет данных'  #

    def get_days_count_wildman(self):
        return self.wildman_days_count

    def get_qty_gift(self):
        return self.gifts

    def get_qty_arachne(self):
        return self.arachne

    def get_qty_raptor(self):
        return self.raptor

    def get_qty_grey_rat(self):
        return self.grey_rat

    def get_qty_wildman(self):
        return self.wildman

    def get_wildman_count(self):
        return self.wildman_count

    def get_qty_kiki(self):
        return self.kiki

    def get_bypass(self):
        return self.bypass

    def get_path_task(self):
        return f'{self.path_task}'

    def get_name_ru(self):
        return self.name_ru

    def get_name_en(self):
        return self.name_en

    def get_name_id(self):
        return self.name_id


gady = Hero(name_ru_="Гадя", name_en_='Gady', name_id='gady')
gady.path_task = 'img/station_master/tasks_gady/'
gady.bypass = b_d.bypass

gavr = Hero(name_ru_='Гавр', name_en_='Gavr', name_id='gavr')
gavr.path_task = 'img/station_master/tasks_gavr/'
gavr.bypass = b_d.bypass

veles = Hero(name_ru_='Велес', name_en_='Велес', name_id='veles')
veles.path_task = 'img/station_master/tasks_veles/'
veles.bypass = b_d.bypass_veles

mara = Hero(name_ru_='Мара', name_en_='Mara', name_id='mara')
mara.path_task = 'img/station_master/tasks_mara/'
mara.bypass = b_d.bypass_mara

# Activ.hero_activ = gady # значение, которое выдает fun.select_hero(True)
# Hero.duel_kv(Activ.hero_activ)  # формат обращения к методу
#
# print(Hero.get_path_task(Activ.hero_activ))
