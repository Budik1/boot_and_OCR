# имя станции = [имя для Print, поиск на карте, ID станции, если её не видно на карте,[задания]]
import baza.paths_img

task_11_22_33 = ['t1.png', 't1.png', 't2.png', 't2.png', 't3.png', 't3.png']
task_12_23_34 = ['t1.png', 't2.png', 't2.png', 't3.png', 't3.png', 't4.png']
task_11_22_77 = ['t1.png', 't1.png', 't2.png', 't2.png', 't7.png', 't7.png']
task_22_33_77 = ['t2.png', 't2.png', 't3.png', 't3.png', 't7.png', 't7.png']
task_23_34_45 = ['t2.png', 't3.png', 't3.png', 't4.png', 't4.png', 't5.png']
task_0 = 0

dir_arrow_south = 'стрелка юг'
dir_arrow_north = 'стрелка север'

st_alexs = ['ст. Алексеевская',
            baza.paths_img.k_Alexs_png,
            baza.paths_img.s_Alexs_png,
            None,
            []]
st_biblioteka = ['ст. Библиотека им. Ленина',
                 baza.paths_img.k_Biblioteka_png,
                 baza.paths_img.s_Biblioteka_png,
                 0,
                 task_11_22_33]
st_borov = ['ст. Боровицкая',
            baza.paths_img.k_Borov_png,
            baza.paths_img.s_Borov_png,
            dir_arrow_south,
            task_11_22_33]
st_chekhov = ['ст. Чеховская',
              baza.paths_img.k_Chekhov_png,
              baza.paths_img.s_Chekhov_png,
              dir_arrow_north,
              task_0]
st_communist = ['ст. Коммунистическая',
                baza.paths_img.k_Communist_png,
                baza.paths_img.s_Communist_png,
                None,
                []]
st_cv_bulvar = ['ст. Цветной бульвар',
                baza.paths_img.k_Cvetnoy_png,
                baza.paths_img.s_Cvetnoy_png,
                None,
                task_11_22_33]
st_frunze = ['ст. Фрунзенская',
             baza.paths_img.k_Frunze_png,
             baza.paths_img.s_Frunze_png,
             None,
             task_22_33_77]
st_kiev = ['ст. Киевская',
           baza.paths_img.k_Kiev_png,
           baza.paths_img.s_Kiev_png,
           None,
           task_23_34_45]
st_kiev_a = ['ст. Киевская(A)',
             baza.paths_img.k_Kiev_a_png,
             baza.paths_img.s_Kiev_a_png,
             None,
             task_0]
st_kitay = ['ст. Китай-город',
            baza.paths_img.k_Kitay_png,
            baza.paths_img.s_Kitay_png,
            dir_arrow_north,
            []]
st_kropot = ['ст. Кропоткинская',
             baza.paths_img.k_Kropotkin_png,
             baza.paths_img.s_Kropotkin_png,
             None,
             task_0]
st_k_most = ['ст. Кузнецкий мост',
             baza.paths_img.k_Kuzneckiy_png,
             baza.paths_img.s_Kuzneckiy_png,
             None,
             task_11_22_33]
st_novok = ['ст. Новокузнецкая',
            baza.paths_img.k_Novokuznec_png,
            baza.paths_img.s_Novokuznec_png,
            None,
            task_11_22_33]
st_park_g = ['ст. Парк культуры(Г)',
             baza.paths_img.k_Park_ganza_png,
             baza.paths_img.s_Park_ganza_png,
             None,
             task_0]
st_park_kr = ['ст. Парк культуры(КР)',
              baza.paths_img.k_Park_kr_png,
              baza.paths_img.s_Park_kr_png,
              None,
              task_12_23_34]
st_pavelec = ['ст. Павелецкая',
              baza.paths_img.k_Pavelec_png,
              baza.paths_img.s_Pavelec_png,
              None,
              task_11_22_33]
st_pavelec_g = ['ст. Павелецкая(Г)',
                baza.paths_img.k_Pavelec_g_png,
                baza.paths_img.s_Pavelec_g_png,
                None,
                task_11_22_33]
st_polyanka = ['ст. Полянка',
               baza.paths_img.k_Polyanka_png,
               baza.paths_img.s_Polyanka_png,
               None,
               []]
st_pr_kt_vernadskogo = ['ст. Пр-кт Вернадского',
                        baza.paths_img.k_Pr_kt_Vernadskogo_png,
                        baza.paths_img.s_Pr_kt_Vernadskogo_png,
                        None,
                        []]
st_pr_kt_mira = ['ст. Проспект мира',
                 baza.paths_img.k_Prospekt_png,
                 baza.paths_img.s_Prospekt_png,
                 None,
                 []]
st_pushkin = ['ст. Пушкинская',
              baza.paths_img.k_Pushkin_png,
              baza.paths_img.s_Pushkin_png,
              None,
              task_11_22_33]
st_riga = ['ст. Рижская',
           baza.paths_img.k_Rizgskaya_png,
           baza.paths_img.s_Rizgskaya_png,
           None,
           []]
st_suxarev = ['ст. Сухаревская',
              baza.paths_img.k_Suxarev_png,
              baza.paths_img.s_Suxarev_png,
              None,
              []]
st_teatr = ['ст. Театральная',
            baza.paths_img.k_Teatr_png,
            baza.paths_img.s_Teatr_png,
            dir_arrow_north,
            task_11_22_33]
st_tretya = ['ст. Третьяковская',
             baza.paths_img.k_Tretyakov_png,
             baza.paths_img.s_Tretyakov_png,
             dir_arrow_south,
             task_0]
st_turgenev = ['ст. Тургеневская',
               baza.paths_img.k_Turgenev_png,
               baza.paths_img.s_Turgenev_png,
               None,
               task_0]
st_tver = ['ст. Тверская',
           baza.paths_img.k_Tver_png,
           baza.paths_img.s_Tver_png,
           None,
           task_11_22_33]
st_univer = ['ст. Университет',
             baza.paths_img.k_Univer_png,
             baza.paths_img.s_Univer_png,
             None,
             task_11_22_77]
st_vdnx = ['ст. ВДНХ',
           baza.paths_img.k_VDNX_png,
           baza.paths_img.s_VDNX_png,
           None,
           []]

# пути-дороги
# основная дорога
grand_road = [st_pr_kt_vernadskogo, st_univer, st_communist, st_frunze, st_park_kr, st_kropot, st_biblioteka, st_borov,
              st_chekhov, st_tver, st_teatr, st_novok, st_tretya, st_kitay, st_turgenev, st_suxarev, st_pr_kt_mira,
              st_riga, st_alexs, st_vdnx]
# допдороги (ответвления)
park_kiev_a = [st_park_kr, st_park_g, st_kiev, st_kiev_a]
borov_polyanka = [st_borov, st_polyanka]
chekhov_bulvar = [st_chekhov, st_cv_bulvar]
tver_most = [st_tver, st_pushkin, st_k_most]
novok_pavelec = [st_novok, st_pavelec, st_pavelec_g]

# все дороги в одном листе
road_list = (grand_road, park_kiev_a, borov_polyanka, chekhov_bulvar, tver_most, novok_pavelec)
# все станции
list_of_stations = [st_kiev, st_riga,
                    st_pr_kt_vernadskogo, st_univer, st_communist, st_frunze, st_park_kr, st_park_g, st_kiev_a,
                    st_kropot, st_biblioteka, st_borov, st_polyanka, st_chekhov, st_cv_bulvar, st_tver, st_pushkin,
                    st_k_most, st_teatr, st_novok, st_pavelec, st_pavelec_g, st_tretya, st_kitay, st_turgenev,
                    st_suxarev, st_pr_kt_mira, st_alexs, st_vdnx, ]

#  с фрунзе оббежать все станции в поисках подарков
bypass = [
    st_park_kr, st_park_g, st_kiev, st_kiev_a, st_kiev, st_park_g,
    st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov,
    st_tver, st_teatr, st_novok, st_pavelec, st_pavelec_g, st_pavelec, st_novok, st_tretya, st_kitay,
    st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_alexs, st_vdnx,
    st_alexs, st_riga, st_pr_kt_mira, st_suxarev, st_turgenev, st_kitay,
    st_tretya, st_novok, st_teatr, st_tver, st_pushkin, st_k_most, st_pushkin,
    st_chekhov, st_cv_bulvar, st_chekhov,
    st_borov, st_polyanka, st_borov, st_biblioteka, st_kropot, st_park_kr, st_frunze,
    st_communist, st_univer, st_pr_kt_vernadskogo, st_univer, st_communist,
    st_frunze]
# сбор подарков для Мар`яны
bypass_mara = [
    st_novok, st_pavelec, st_pavelec_g, st_pavelec, st_novok, st_tretya, st_novok, st_teatr, st_tver,
    st_pushkin, st_k_most, st_pushkin, st_chekhov, st_cv_bulvar, st_chekhov, st_tver, st_teatr, ]
bypass_veles = [st_pavelec, st_novok, st_tretya, st_novok, st_teatr, st_tver, st_pushkin, st_k_most, st_pushkin,
                st_chekhov, st_cv_bulvar, st_chekhov, st_borov, st_polyanka, st_borov, st_biblioteka,
                st_kropot, st_park_kr, st_park_g, st_kiev, st_park_g, st_park_kr, st_kropot, st_biblioteka,
                st_borov, st_chekhov, st_tver, st_teatr, st_novok, st_pavelec, st_pavelec_g, ]
# за кикиморами в туннелях

frunze_kikimory = [st_park_kr, st_kropot, st_biblioteka, st_borov, st_chekhov, st_tver, st_teatr, st_novok, st_tretya,
                   st_kitay,
                   st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_pr_kt_mira, st_suxarev,
                   st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_pr_kt_mira, st_suxarev,
                   st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_pr_kt_mira, st_suxarev,
                   st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_pr_kt_mira, st_suxarev,
                   st_turgenev, st_suxarev, st_pr_kt_mira, st_riga, st_pr_kt_mira, st_suxarev,
                   st_turgenev, st_kitay, st_tretya, st_novok, st_teatr, st_tver, st_chekhov, st_borov, st_biblioteka,
                   st_kropot, st_park_kr, st_frunze]

#
frunze_kiev = [st_park_kr, st_park_g, st_kiev]
kiev_univer = [st_park_g, st_park_kr, st_frunze, st_communist, st_univer]
univer_frunze = [st_communist, st_frunze]

#
energy_capacity = ('en1.png', 'en2.png', 'en3.png', 'en4.png', 'en5.png', 'en6.png', 'en7.png')
task_list = ['t1.png', 't2.png', 't3.png', 't4.png', 't5.png', 't6.png', 't7.png']

height_line = 30  # высота линии 30
line0 = 0
line1 = height_line * 1
line2 = height_line * 2
line3 = height_line * 3
line4 = height_line * 4
line5 = height_line * 5
line6 = height_line * 6
line7 = height_line * 7
line8 = height_line * 8
line9 = height_line * 9
line10 = height_line * 10

line11 = height_line * 11
line12 = height_line * 12
line13 = height_line * 13
line14 = height_line * 14
line15 = height_line * 15
line16 = height_line * 16
line17 = height_line * 17
line18 = height_line * 18
line19 = height_line * 19

label_shift = 3  # смещение строки для Label
label_line0 = line0 + label_shift
label_line1 = line1 + label_shift
label_line2 = line2 + label_shift
label_line3 = line3 + label_shift
label_line4 = line4 + label_shift

gady_y = label_line1
gavr_y = label_line2
mara_y = label_line3
veles_y = label_line4

step_col = 47
s = 14
col_0 = 0
col_1 = step_col + s
col_2 = step_col * 2 + s
col_3 = step_col * 3 + s
col_4 = step_col * 4 + s
col_5 = step_col * 5 + s
col_6 = step_col * 6 + s
col_7 = step_col * 7 + s
col_8 = step_col * 8 - 9
col_9 = step_col * 9 -3
lst_columns_root = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]

separator_1 = col_2 - 18
separator_2 = col_3 - 18
separator_3 = col_4 - 18
separator_4 = col_5 - 18
separator_5 = col_6 - 18
separator_6 = col_7 - 18

timer24 = 24 * 3600
timer8 = 8 * 3600
timer1 = 1 * 3600

caliber = 100
caliber_percent = caliber / 100
