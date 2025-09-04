import heroes


indent = " "
len_1 = 5
len_2 = 6
len_3 = 6
len_4 = 18
hero_dict = {'Gady:': heroes.gady, 'Gavr:': heroes.gavr, 'Veles:': heroes.veles, 'Mara:': heroes.mara}

for key in hero_dict:
    indent_ =indent.ljust(5, '+')
    name = key.rjust(len_3).ljust(8)
    energy_count_today = '20'
    energy_count_all = '120'
    en_now = 'сегодня:' + energy_count_today.rjust(len_1, "*")
    en_all = f'всего:{energy_count_all.rjust(len_2)}/170'
    print(f'{indent_}{name}{en_now}')