import fun
import my_color_text as myCt
import baza_dannyx as b_d

nam = 0 # для подсчета заданий


class Activ:
    hero_activ_name = ''  # значение переменной
    hero_activ = ''
    result_duel = ""
    check_date_ = ''
    date_now = ''
    value_energy = 0


class Hero:

    def __init__(self, name_ru_=None, name_en_=None, name_file_=None):
        self.name_en = name_en_
        self.name_ru = name_ru_
        self.name_file = name_file_
        self.path_task = ''
        self.bypass = ()

        self.vip = 0  #
        self.gifts = 0  #
        self.kiki = 0  #
        self.grey_rat = 0  #
        self.arachne = 0  #
        self.raptor = 0  #
        self.wildman = 0  #
        self.wildman_count = 0
        self.wild_activ = False
        self.completing_tasks = False
        self.wildman_days_count = 0
        self.task_count = 0
        self.energy_count_today = 0
        self.energy_all_count = 0
        self.value_energy = 0

        self.duel_all = 0
        self.duel_now = 0
        self.duel_victory = 0
        self.duel_defeat = 0
        self.danger = 0
        self.danger_victory = 0

    def setting_value_energy(self, value):
        self.value_energy = value

    # Uppers

    def app_energy_count_today(self, value):
        self.energy_count_today += value
        self.energy_all_count += value

    def app_task_count(self):
        self.task_count += 1

    def app_days_count_wildman(self):
        if not self.wild_activ:
            self.wild_activ = True
            self.wildman_days_count += 1
            # print(f'{self.name_ru} {self.days_count_wildman}')

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

    def app_rat(self):
        self.grey_rat += 1

    def app_danger(self):
        self.danger += 1

    def app_danger_v(self):
        self.danger_victory += 1

    def app_completing_tasks(self):
        self.completing_tasks = True

    # Гетеры
    def get_energy_count_all(self):
        return self.energy_all_count

    def get_energy_count_today(self):
        return self.energy_count_today

    def get_task_count(self):
        return self.task_count

    def get_report_wildman(self):
        # 'За ''3'' дня ''4'' шт. В среднем ''1.333'' в день. Или 7 эн на 1го'
        if self.wildman_days_count != 0 and self.wildman_count != 0:
            text1 = myCt.tc_green('За ')  # 'За '
            d_all_c = myCt.tc_cyan(str(self.wildman_days_count))  # '3'
            text2 = myCt.tc_green(f' {fun.transform_days(self.wildman_days_count)} ')  # ' дня '
            w_all_c = myCt.tc_cyan(str(self.wildman_count))  # '4'
            text3 = myCt.tc_green(' шт. В среднем ')  # ' шт. В среднем '
            average_value1 = myCt.tc_yellow(f'{round(self.wildman_count / self.wildman_days_count, 3)}')  # '1.333'
            text4 = myCt.tc_green(' в день. Или ')  # ' в день. Или '
            # количество энергии на одного
            average_value2 = myCt.tc_blue(f'{round(self.energy_all_count / self.wildman_count, 4)}')  # '7'
            text5 = myCt.tc_green(' эн на 1го')  # ' эн на 1го'
            line1 = f'{text1}{d_all_c}{text2}{w_all_c}{text3}{average_value1}{text4}{average_value2}{text5}'
            return line1
        else:
            return f'по дикарям нет данных'  # , {self.wildman_days_count =}, {self.wildman_count =}

    def get_report_wildman_now(self):
        if self.wildman:
            return f'{myCt.tc_yellow(str(self.wildman))} {myCt.tc_green("за сегодня")}'
        else:
            return f'по дикарям нет данных'  # , {self.wildman =}

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

    def get_qty_danger(self):
        return self.danger

    def get_qty_danger_v(self):
        return self.danger_victory

    def get_path_task(self):
        return f'{self.path_task}'

    def get_name_ru(self):
        return self.name_ru

    def get_name_en(self):
        return self.name_en

    def get_hero_name_in_file(self):
        return self.name_file

    #
    def duel_kv(self):
        self.duel_now += 1
        self.duel_all += 1

    def duel_victory_app(self):
        self.duel_victory += 1
        self.duel_kv()

    def her_message(self):
        return f'обнаружен {self.name_ru}'


gady = Hero(name_ru_="Гадя", name_en_='Gady', name_file_='gady')
gady.path_task = 'img/stationmaster/tasks_gady/'
gady.bypass = b_d.bypass

gavr = Hero(name_ru_='Гавр', name_en_='Gavr', name_file_='gavr')
gavr.path_task = 'img/stationmaster/tasks_gavr/'
gavr.bypass = b_d.bypass

veles = Hero(name_ru_='Велес', name_en_='Велес', name_file_='veles')
veles.path_task = 'img/stationmaster/tasks_veles/'
veles.bypass = b_d.bypass_veles

mara = Hero(name_ru_='Мара', name_en_='Mara', name_file_='mara')
mara.path_task = 'img/stationmaster/tasks_mara/'
mara.bypass = b_d.bypass_mara

# Activ.hero_activ = gady # значение, которое выдает fun.select_hero(True)
# Hero.duel_kv(Activ.hero_activ)  # формат обращения к методу
#
# print(Hero.get_path_task(Activ.hero_activ))
