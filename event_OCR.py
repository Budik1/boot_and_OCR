def visualization_tascks_result(list_1_pul, list_1_xp, list_2_pul, list_2_xp, list_3_pul, list_3_xp):
    print(f'{list_1_pul[0]} {list_1_xp[0]} {list_2_pul[0]} {list_2_xp[0]} {list_3_pul[0]} {list_3_xp[0]}')
    print()
    # С округлением до сотых
    print(f"{list_1_pul[0]} / {list_1_xp[0]} => {round(int(list_1_pul[0]) / int(list_1_xp[0]), 2)}")
    print(f"{list_2_pul[0]} / {list_2_xp[0]} => {round(int(list_2_pul[0]) / int(list_2_xp[0]), 2)}")
    print(f"{list_3_pul[0]} / {list_3_xp[0]} => {round(int(list_3_pul[0]) / int(list_3_xp[0]), 2)}")
    print()
    # С округлением до десятых
    print(f"{list_1_pul[0]} / {list_1_xp[0]} => {round(int(list_1_pul[0]) / int(list_1_xp[0]), 1)}")
    print(f"{list_2_pul[0]} / {list_2_xp[0]} => {round(int(list_2_pul[0]) / int(list_2_xp[0]), 1)}")
    print(f"{list_3_pul[0]} / {list_3_xp[0]} => {round(int(list_3_pul[0]) / int(list_3_xp[0]), 1)}")
    print()
    # С округлением до целых
    print(f"{list_1_pul[0]} / {list_1_xp[0]} => {round(int(list_1_pul[0]) / int(list_1_xp[0]))}")
    print(f"{list_2_pul[0]} / {list_2_xp[0]} => {round(int(list_2_pul[0]) / int(list_2_xp[0]))}")
    print(f"{list_3_pul[0]} / {list_3_xp[0]} => {round(int(list_3_pul[0]) / int(list_3_xp[0]))}")


def find_benefit(*, pul, xp):
    result = round(int(pul[0]) / int(xp[0]))
    return result


def find_tasks_benefit(value_1_pul, value_1_xp, value_2_pul, value_2_xp, value_3_pul, value_3_xp):
    """
    Результат с округлением до целых

    """
    # нужна проверка на "0" ?
    if value_1_xp and value_1_pul:
        rez_1 = round(int(value_1_pul[0]) / int(value_1_xp[0]))
    else:
        rez_1 = 0
    if value_2_xp and value_2_pul:
        rez_2 = round(int(value_2_pul[0]) / int(value_2_xp[0]))
    else:
        rez_2 = 0
    if value_3_xp and value_3_pul:
        rez_3 = round(int(value_3_pul[0]) / int(value_3_xp[0]))
    else:
        rez_3 = 0
    print()
    print(f'{rez_1=}, {rez_2=}, {rez_3=}')
    return rez_1, rez_2, rez_3


def visualization_lvl_result(list_lvl):
    rezult = list_lvl[0]
    print(f"{list_lvl}")
