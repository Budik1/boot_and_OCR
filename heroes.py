import time

import baza_dannyx as b_d
import color_text
import color_text as myCt

# from fun import time_now

nam = 0  # для подсчета чего?
temp_min = None
time_now_ = ""


class Activ:
    hero_activ = ''
    hero_activ_name = ''  # значение переменной
    check_date_ = ''
    date_now = ''
    name_file_ = None
    station_activ = ''
    qty_vip = 0
    duel_raid = 0
    result_load = ''
    #
    #
    hour_now = ''
    result_duel = ""
    value_energy = 0


class Hero:

    def __init__(self, name_ru_, name_en_, name_id, _id):
        # статичные
        self.name_en = name_en_
        self.name_ru = name_ru_
        self.name_id = name_id
        self.id_ = _id
        self.bypass = ()

        # обновляемые ежедневно
        self.vip = 0  #
        self.holiday_gift = 0  #
        self.grey_rat = 0  #
        self.white_rat = 0
        self.kiki = 0  #
        self.arachne = 0  #
        self.raptor = 0  #
        self.wildman = 'x'
        self.wildman_count = 0
        self.wild_activ = False

        self.energy_count_today = 0
        self.arena_count = 0  # счет арены
        self.arena_victory_count = 0

        # накопительные
        self.home_location = 'бомж'
        self.lvl_up_date = ''
        self.lvl_up_days = ''

        self.wildman_days_count = 0
        #
        self.energy_count_all = 0
        self.energy_kiev_count_all = 0
        # self.energy_spent_searching_for_white_rats = 0
        self.value_energy = 0

        # кв и рейд
        self.qty_duel_all = 0  # к-во боёв всего
        self.qty_duel_all_victory = 0  # к-во побед всего

        self.qty_duel_in_kv_all = 0
        self.qty_duel_in_kv_victory = 0

        self.danger = 0
        self.danger_victory = 0
        self.list_loot = []
        self.set_dist = {}

        self.count_shoulder_straps_all = 0
        self.count_shoulder_straps_kv = 0
        self.__numbers_wins_to_loot = -1

        self.time_start_kv = 0
        self.last_attack = 0

        self.timer = 0
        self.time_entree = 0

        self.duel_raid = 0

    def get_set_dist(self):
        return self.set_dist

    def set_set_dist(self, value):
        self.set_dist = value

    def get_up_date(self):
        return self.lvl_up_date

    def set_up_date(self):
        self.lvl_up_date = Activ.date_now

    def get_lvl_up_days(self):
        return self.lvl_up_days

    def set_lvl_up_days(self, value):
        self.lvl_up_days = value

    def get_state_kv(self):
        data_to_save = {
            'time_start_kv': self.time_start_kv,

            'qty_duel_all': self.qty_duel_all,
            'qty_duel_all_victory': self.qty_duel_all_victory,
            'qty_duel_in_kv_all': self.qty_duel_in_kv_all,
            'qty_duel_in_kv_victory': self.qty_duel_in_kv_victory,
            'count_shoulder_straps_all': self.count_shoulder_straps_all,
            'count_shoulder_straps_kv': self.count_shoulder_straps_kv,
            'list_loot': self.list_loot,
            'set_dist': self.set_dist,
        }
        hero_id = Hero.get_id(self)
        list_kv_state[hero_id] = data_to_save
        return

    def set_state_kv(self):
        hero_id = Hero.get_id(self)

        data_kv = list_kv_state[hero_id]
        time_now = time.time()
        time_check = data_kv['time_start_kv']
        if (time_now - time_check) < 3 * 3600:
            print('Время старта КВ не изменилось')
            self.time_start_kv = data_kv.get('time_start_kv', 0)

            self.qty_duel_in_kv_all = data_kv.get('qty_duel_in_kv_all', 0)
            self.qty_duel_in_kv_victory = data_kv.get('qty_duel_in_kv_victory', 0)
            self.count_shoulder_straps_kv = data_kv.get('count_shoulder_straps_kv', 0)
            self.list_loot = data_kv.get('list_loot', [])
            self.set_dist = data_kv.get('set_dist', {})
        else:
            print('Время старта КВ обновилось')
            self.time_start_kv = time_now

            self.qty_duel_in_kv_all = 0
            self.qty_duel_in_kv_victory = 0

        self.qty_duel_all_victory = data_kv.get('gady.duel_victory_all', 0)
        self.qty_duel_all = data_kv.get('gady.duel_all', 0)
        self.count_shoulder_straps_all = data_kv.get('gady.count_shoulder_straps', 0)

    def get_state_all(self):
        data_to_save = {
            'check_date_k': Activ.date_now,
            # updatable
            # мобы
            'grey_rat_k': self.grey_rat,
            'white_rat_k': self.white_rat,
            'arachne_k': self.arachne,
            'wildman_k': self.wildman,
            'kiki_k': self.kiki,
            'raptor_k': self.raptor,
            # арена
            'arena_count_k': self.arena_count,
            'arena_victory_count_k': self.arena_victory_count,

            'vip_k': self.vip,
            'energy_count_today_k': self.energy_count_today,
            'wild_activ_k': self.wild_activ,
            'holiday_gift_k': self.holiday_gift,

            # cumulative
            'home_location_k': self.home_location,
            'energy_count_all_k': self.energy_count_all,
            'wildman_count_k': self.wildman_count,
            'wildman_days_count_k': self.wildman_days_count,
            'time_entree_k': self.time_entree,
            'energy_kiev_count_all_k': self.energy_kiev_count_all,
            'lvl_up_date_k': self.lvl_up_date,
        }
        hero_id = Hero.get_id(self)
        list_all_state[hero_id] = data_to_save
        # отладка
        # home_location = data_to_save['home_location_k']
        # check_date = data_to_save['check_date_k']
        # print(f'get_state_all {self.name_ru=}, {home_location=}, {check_date=}')
        # конец отладки
        return

    def set_updatable_values(self):
        # print(f'Вызов set_updatable_values {self.name_ru}')

        hero_id = Hero.get_id(self)
        # print(f'{list_all_state=}')
        loaded_data = list_all_state[hero_id]
        check_date_ = loaded_data.get('check_date_k', 0)
        # print(check_date_, Activ.date_now)
        # print(f'{hero_id=} {check_date_=}, {Activ.date_now=}')
        if check_date_ == Activ.date_now:
            Activ.result_load = (color_text.tc_blue('Даты совпадают'))

            # мобы
            self.grey_rat = loaded_data.get('grey_rat_k', 0)
            self.white_rat = loaded_data.get('white_rat_k', 0)
            self.arachne = loaded_data.get('arachne_k', 0)
            self.wildman = loaded_data.get('wildman_k', 0)
            self.kiki = loaded_data.get('kiki_k', 0)
            self.raptor = loaded_data.get('raptor_k', 0)
            # арена
            self.arena_count = loaded_data.get('arena_count_k', 0)
            self.arena_victory_count = loaded_data.get('arena_victory_count_k', 0)

            self.vip = loaded_data.get('vip_k', 0)
            self.energy_count_today = loaded_data.get('energy_count_today_k', 0)
            self.wild_activ = loaded_data.get('wild_activ_k', 0)
            self.holiday_gift = loaded_data.get('gifts_k', 0)
        else:
            Activ.result_load = color_text.tc_blue('даты не совпадают, смена суток')
        # print(Activ.result_load)
        # print()
        # print(f'set_updatable_values {self.name_ru}')
        return

    #

    def set_cumulative_values(self):
        # print(f'Вызов set_cumulative_values {self.name_ru}')

        hero_id = Hero.get_id(self)
        loaded_data = list_all_state[hero_id]
        home_location_v = loaded_data['home_location_k']
        self.home_location = loaded_data.get('home_location_k', 'бомж')
        self.energy_count_all = loaded_data.get('energy_count_all_k', 0)
        self.wildman_count = loaded_data.get('wildman_count_k', 0)
        self.wildman_days_count = loaded_data.get('wildman_days_count_k', 0)
        self.time_entree = loaded_data.get('time_entree_k', 0)
        self.energy_kiev_count_all = loaded_data.get('energy_kiev_count_all_k', 0)
        self.lvl_up_date = loaded_data.get('lvl_up_date_k', '')
        # отладка

        # print(f'set_cumulative_values {self.name_ru}, {self.lvl_up_date}') #
        # print()
        # конец отладки

    def get_list_loot(self):
        return self.list_loot

    def set_list_loot(self, value):
        self.list_loot = value

    def get_id(self):
        return self.id_

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

    def app_wildman_days_count(self):
        if not self.wild_activ:
            self.wild_activ = True
            self.wildman_days_count += 1
            # print(f'{self.name_ru} {self.days_count_wildman}')

    def set_wild_activ(self):
        self.wild_activ = Activ.date_now

    def app_vip(self):
        self.vip += 1

    def app_gifts(self):
        self.holiday_gift += 1

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

    def app_white_rat(self):
        self.white_rat += 1

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

    def get_report_wildman_now(self):
        if self.wildman:
            return f'{myCt.tc_yellow(str(self.wildman))} {myCt.tc_green("за сегодня")}'
        else:
            return f'по дикарям нет данных'  #

    def get_days_count_wildman(self):
        return self.wildman_days_count

    def get_qty_gift(self):
        return self.holiday_gift

    def get_qty_arachne(self):
        return self.arachne

    def get_qty_raptor(self):
        return self.raptor

    def get_qty_grey_rat(self):
        return self.grey_rat

    def get_qty_white_rat(self):
        return self.white_rat

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


gady = Hero(name_ru_="Гадя", name_en_='Gady', name_id='gady', _id=0)
gady.path_task = 'img/station_master/tasks_gady/'
gady.bypass = b_d.bypass

gavr = Hero(name_ru_='Гавр', name_en_='Gavr', name_id='gavr', _id=1)
gavr.path_task = 'img/station_master/tasks_gavr/'
gavr.bypass = b_d.bypass

# veles = Hero(name_ru_='Велес', name_en_='Велес', name_id='veles', id_n=3)
# veles.path_task = 'img/station_master/tasks_veles/'
# veles.bypass = b_d.bypass_veles

mara = Hero(name_ru_='Мара', name_en_='Mara', name_id='mara', _id=2)
mara.path_task = 'img/station_master/tasks_mara/'
mara.bypass = b_d.bypass_mara

list_all_state = [{}, {}, {}]  #
list_kv_state = [{}, {}, {}]
hero_dict = {'Gady': gady, 'Gavr': gavr, 'Mara': mara}  #
# Activ.hero_activ = gady # значение, которое выдает fun.select_hero(True)
# Hero.duel_kv(Activ.hero_activ)  # формат обращения к методу
#
# print(Hero.get_path_task(Activ.hero_activ))
