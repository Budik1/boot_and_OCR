from cmath import phase

import fun

# fun.Mouse.move(pos=(453, 457))
def get_name_loot():
    fun.my_log_file(f'')
    fun.my_log_file(f'kv_and_raid.get_name_loot')
    dict_name_loot = {'сержант': 'img/kv/result_round/loot/p1.png',
                      'лейтенант': 'img/kv/result_round/loot/p2.png',
                      'капитан': 'img/kv/result_round/loot/p3.png',
                      'полковник': 'img/kv/result_round/loot/p4.png',
                      'генерал': 'img/kv/result_round/loot/p5.png'}
    result = 'неопознан'
    for name in dict_name_loot:
        name_loot = fun.locCenterImg(name_img=dict_name_loot[name])
        if name_loot:
            result = name
            print(result)
            # break
    return result


print(get_name_loot())