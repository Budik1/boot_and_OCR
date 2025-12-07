import heroes

print(len(heroes.hero_dict))
len_hero_dict = len(heroes.hero_dict)
for i in heroes.hero_dict:
    print(i)
    heroes.dict_all_state[i]= {}
    heroes.dict_kv_state[i]= {}

print(heroes.dict_all_state)
print(heroes.dict_kv_state)