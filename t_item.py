import fun
import pyautogui
# item = [profile, name]
grey_rat_1 = ['img/tonelli/mobi/name1_grey_rat.png', 'серая крыса']
white_rat_1 = ['img/tonelli/mobi/name1_white_rat.png', 'белая крыса']
black_rat_1 = ['img/tonelli/mobi/name1_black_rat.png', 'черная крыса']
# sand_rat = ['img/tonelli/mobi/name1_sand_rat.png', 'песчаная крыса']
spy_2 = ['img/tonelli/mobi/name2_spy.png', 'шпион']
smuggler_3 = ['img/tonelli/mobi/name3_smuggler.png', 'контрабандисты']
arachne_4 = ['img/tonelli/mobi/name4_arachne.png', 'паук']
wildman_5 = ['img/tonelli/mobi/name5_wildman.png', 'дикарь']
kikimora_6 = ['img/tonelli/mobi/name6_kikimora.png', 'кикимора']
raptor_7 = ['img/tonelli/mobi/name7_raptor.png', 'ящер']
mobi_list = [grey_rat_1, white_rat_1, black_rat_1, spy_2, smuggler_3,  arachne_4, wildman_5, kikimora_6, raptor_7]
for mob, name in mobi_list:
    mob_ident = fun.locCenterImg(mob)
    print(mob)
    if mob_ident:
        print(name)
        break

